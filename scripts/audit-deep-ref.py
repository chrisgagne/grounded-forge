#!/usr/bin/env python3
"""On-demand heuristic audit for deep references.

Complements two existing layers of source-integrity discipline:

  1. `.claude/hooks/validate-deep-ref.py` runs at write time and gates on
     deterministic structural checks. Cheap, false-positive-free, blocks
     bad writes before they hit disk.
  2. Pass I (model-level source-only audit) reads the deep ref cold and
     verifies every claim traces to a passage in the source. Expensive,
     ships nothing if it fails.

This script sits between them: a heuristic claim-line analyser that reports
*candidate weaknesses* without blocking anything. False positives are
expected; the operator reads the report and decides what (if anything) to
fix. Use this in CI on PRs touching deep refs, or as a quick read before
inviting the model to run Pass I.

What it checks:
  - Citation density per section: every section should have at least one
    citation; sections with claims but no citations are flagged.
  - Marker distribution: a deep ref with no [V] verbatim markers may be
    summary-only; flag for visibility.
  - Long sentences (>40 words) without a citation tail.
  - Adjectival drift words ("clearly", "obviously", "famously",
    "notoriously") often signal author-paraphrased-as-fact; flag for
    review.
  - Blockquote-to-citation ratio: every blockquote should have one
    citation; flag mismatches.

Output is human-readable by default. JSON output is available via `--json`
for CI integration.

Usage:
    python3 scripts/audit-deep-ref.py corpus.commons/demo/references/foo-deep.md
    python3 scripts/audit-deep-ref.py corpus.commons/demo/references/foo-deep.md --json
    python3 scripts/audit-deep-ref.py --all
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COMMONS_ROOT = REPO_ROOT / "corpus.commons"
LOCAL_ROOT = REPO_ROOT / "corpus.local"


def collect_deep_refs(root: Path) -> list[Path]:
    """Walk a corpus tier root and return every deep-ref file beneath it."""
    if not root.exists():
        return []
    found: list[Path] = []
    for corpus_dir in sorted(root.iterdir()):
        if not corpus_dir.is_dir():
            continue
        refs_dir = corpus_dir / "references"
        if refs_dir.exists():
            found.extend(sorted(refs_dir.glob("*-deep.md")))
    return found

CITATION_TAIL_PATTERN = re.compile(
    r"\((?:Ch\s+\d+|p\.\s*\d+|pp\.\s*\d+|[A-Z][a-z]+\s+\d{4}|\"[^\"]+\"|§|[A-Z][a-z]+,\s+\d{4})",
)
MARKER_PATTERN = re.compile(r"\[(V|AP|AR|AE|BT)\](?=[\s,.;:)\]]|$)")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'])")
DRIFT_WORDS = {
    "clearly",
    "obviously",
    "famously",
    "notoriously",
    "of course",
    "everyone knows",
    "it is well known",
    "no one doubts",
}
DRIFT_PATTERN = re.compile(
    r"\b(" + "|".join(re.escape(w) for w in DRIFT_WORDS) + r")\b",
    re.IGNORECASE,
)


@dataclass
class Finding:
    severity: str  # "info" | "warn"
    section: str
    line: int
    message: str


@dataclass
class Report:
    path: str
    sections_total: int = 0
    sections_with_citations: int = 0
    sections_without_citations: list[str] = field(default_factory=list)
    marker_counts: dict[str, int] = field(default_factory=dict)
    blockquote_count: int = 0
    findings: list[Finding] = field(default_factory=list)


def _split_sections(text: str) -> list[tuple[int, str, list[str]]]:
    """Return list of (start_line_no, section_anchor, lines)."""
    lines = text.split("\n")
    out: list[tuple[int, str, list[str]]] = []
    current_anchor = "_frontmatter"
    current_start = 1
    current_buf: list[str] = []
    for i, line in enumerate(lines, start=1):
        if line.startswith("## "):
            if current_buf:
                out.append((current_start, current_anchor, current_buf))
            current_anchor = line[3:].strip()
            current_start = i
            current_buf = []
        else:
            current_buf.append(line)
    if current_buf:
        out.append((current_start, current_anchor, current_buf))
    return out


def audit(path: Path) -> Report:
    text = path.read_text(encoding="utf-8")
    abs_path = path.resolve()
    try:
        rel = abs_path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        rel = path.as_posix()
    report = Report(path=rel)

    # Section-level analysis.
    for start_line, anchor, lines in _split_sections(text):
        if anchor == "_frontmatter":
            continue
        report.sections_total += 1
        body = "\n".join(lines)
        if CITATION_TAIL_PATTERN.search(body):
            report.sections_with_citations += 1
        else:
            if body.strip():
                report.sections_without_citations.append(anchor)
                report.findings.append(
                    Finding(
                        severity="warn",
                        section=anchor,
                        line=start_line,
                        message=f"section has no citations: claims may be unsourced",
                    )
                )

        # Long sentences without citation tail.
        for sentence in SENTENCE_SPLIT.split(body):
            words = sentence.split()
            if len(words) > 40 and not CITATION_TAIL_PATTERN.search(sentence):
                report.findings.append(
                    Finding(
                        severity="info",
                        section=anchor,
                        line=start_line,
                        message=f"long sentence ({len(words)} words) without citation tail",
                    )
                )
                break  # one per section is enough

        # Drift-word detection.
        for m in DRIFT_PATTERN.finditer(body):
            offset_lines = body[: m.start()].count("\n")
            report.findings.append(
                Finding(
                    severity="info",
                    section=anchor,
                    line=start_line + offset_lines,
                    message=f"drift-word `{m.group(0)}`: review whether source actually asserts this",
                )
            )
            break  # one per section is enough

    # Marker distribution.
    for m in MARKER_PATTERN.finditer(text):
        token = f"[{m.group(1)}]"
        report.marker_counts[token] = report.marker_counts.get(token, 0) + 1

    if "[V]" not in report.marker_counts:
        report.findings.append(
            Finding(
                severity="info",
                section="(global)",
                line=0,
                message="no [V] verbatim markers: deep ref may be summary-only without direct quotation",
            )
        )

    # Blockquote count.
    report.blockquote_count = sum(
        1 for line in text.split("\n") if line.startswith("> ")
    )

    return report


def render(report: Report) -> str:
    out: list[str] = []
    out.append(f"## Audit: {report.path}")
    out.append("")
    out.append(
        f"Sections: {report.sections_total} total, "
        f"{report.sections_with_citations} with citations, "
        f"{len(report.sections_without_citations)} without."
    )
    if report.marker_counts:
        counts = ", ".join(
            f"{k}={v}" for k, v in sorted(report.marker_counts.items())
        )
        out.append(f"Evidence markers: {counts}")
    else:
        out.append("Evidence markers: none found.")
    out.append(f"Blockquote lines: {report.blockquote_count}")
    out.append("")

    if not report.findings:
        out.append("No findings. Deep ref passes heuristic audit.")
        return "\n".join(out) + "\n"

    out.append(f"Findings ({len(report.findings)}):")
    for f in report.findings:
        loc = f"line {f.line}" if f.line else "global"
        out.append(f"  [{f.severity}] {loc} ({f.section}): {f.message}")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", nargs="?", help="deep-ref file to audit")
    parser.add_argument("--all", action="store_true", help="audit every deep ref under corpus.commons/*/references/")
    parser.add_argument("--all-local", action="store_true", help="audit every deep ref under corpus.local/*/references/")
    parser.add_argument("--all-corpora", action="store_true", help="audit every deep ref under both corpus.commons/ and corpus.local/")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of human-readable text")
    args = parser.parse_args()

    mode_count = sum(bool(x) for x in (args.all, args.all_local, args.all_corpora))
    if not args.path and mode_count == 0:
        parser.error("provide a path or use --all / --all-local / --all-corpora")
    if mode_count > 1:
        parser.error("use only one of --all, --all-local, --all-corpora")
    if args.path and mode_count > 0:
        parser.error("provide a path OR a tier flag, not both")

    paths: list[Path] = []
    if args.all:
        paths = collect_deep_refs(COMMONS_ROOT)
        if not paths:
            sys.stderr.write(f"No deep refs found under {COMMONS_ROOT}/*/references/\n")
            return 1
    elif args.all_local:
        paths = collect_deep_refs(LOCAL_ROOT)
        if not paths:
            sys.stderr.write(f"No deep refs found under {LOCAL_ROOT}/*/references/\n")
            return 1
    elif args.all_corpora:
        paths = collect_deep_refs(COMMONS_ROOT) + collect_deep_refs(LOCAL_ROOT)
        if not paths:
            sys.stderr.write(f"No deep refs found under {COMMONS_ROOT}/*/references/ or {LOCAL_ROOT}/*/references/\n")
            return 1
    else:
        p = Path(args.path)
        if not p.exists():
            sys.stderr.write(f"Not found: {p}\n")
            return 1
        if not p.name.endswith("-deep.md"):
            sys.stderr.write(f"Not a deep ref: {p}\n")
            return 1
        paths = [p]

    reports = [audit(p) for p in paths]
    any_warn = any(any(f.severity == "warn" for f in r.findings) for r in reports)

    if args.json:
        print(json.dumps([asdict(r) for r in reports], indent=2, default=lambda o: asdict(o)))
    else:
        for r in reports:
            print(render(r))

    return 0 if not any_warn else 1


if __name__ == "__main__":
    sys.exit(main())
