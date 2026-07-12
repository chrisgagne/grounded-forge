"""Mechanical baseline discovery scan.

Walks every ``{slug}-deep.md`` (and the corresponding ``sources/converted/{slug}.md``
when available) in a corpus and emits a minimum-viable
``_planning/discovery/{slug}.json`` for the mechanical preprocessor.

What this script captures:

- ``slug``, ``source_file`` — identity.
- ``headings.quality`` — heuristic from the converted markdown's heading
  distribution. (The preprocessor's ``headings.extract`` handler runs
  unconditionally regardless, so this field is only diagnostic.)
- ``book_index.present`` — heuristic: does the converted markdown have a
  back-matter region matching a standard book-index shape?
  ``book_index.shape``, ``book_index.location_line_range`` — when present.
- ``page_markers.present`` — does the converted markdown contain
  ``{page-N}`` markers or recurring numeric-only lines suggesting page
  boundaries?
- ``enumerated_named_methods.examples_seen`` — left empty; this is the
  one field where LLM judgement materially helps, and is handled by the
  separate LLM-augmented scanner.

What this script does NOT capture:

- Author-curated enumerated method names (Five Dysfunctions, Seven Habits, etc.).
- Distinguishing between "no back-matter index" and "back-matter index in
  an unusual shape we didn't pattern-match." False negatives are possible.

Run order:

    1. python -m scripts.mechanical_index.discovery_scan_mechanical \\
           --corpus corpus.local/aarbuddy

    2. (Optional) LLM-augmented scan on book-shaped sources to fill
       ``enumerated_named_methods.examples_seen`` and refine
       ``book_index.shape``.

    3. python -m scripts.mechanical_index.preprocess --source ... --discovery ...
       (per source — driven by the orchestrator)

The mechanical scanner is intentionally noisy-but-cheap; the preprocessor
already tolerates partial discovery records (`_load_discovery` does not
require every field).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


_INDEX_HEADING_RX = re.compile(
    r"^#+\s*(?:\*\*)?(index|subject\s+index|name\s+index|topic\s+index|general\s+index)(?:\*\*)?\s*$",
    re.IGNORECASE,
)
_PAGE_MARKER_RX = re.compile(r"\{page[-_:\s]*\d+\}|^\s*\d{1,4}\s*$")


def _find_back_matter_index(lines: list[str]) -> dict | None:
    """Locate a back-matter book index region.

    Returns ``{present, shape, location_line_range}`` or None.
    """
    for i, line in enumerate(lines):
        if _INDEX_HEADING_RX.match(line.strip()):
            # The index starts at i; ends at EOF or at next top-level heading
            # at the same/higher level. Greedy: take rest of file.
            end = len(lines) - 1
            # Trim trailing blank lines
            while end > i and not lines[end].strip():
                end -= 1
            # Heuristic: is the region long enough to be a real index?
            region_lines = end - i
            if region_lines < 20:
                return None
            # Detect shape: do lines have anchor links?
            anchor_count = sum(1 for L in lines[i:end] if "](" in L and "#" in L)
            if anchor_count > region_lines * 0.3:
                shape = "anchor-linked"
            else:
                shape = "flattened-plaintext"
            return {
                "present": True,
                "shape": shape,
                "location_line_range": [i + 1, end + 1],  # 1-indexed
            }
    return None


def _detect_page_markers(lines: list[str]) -> bool:
    hits = 0
    for line in lines[: min(2000, len(lines))]:
        if _PAGE_MARKER_RX.search(line):
            hits += 1
            if hits >= 5:
                return True
    return False


def _heading_quality(lines: list[str]) -> str:
    """Crude rating: counts # / ## / ### densities."""
    h1 = sum(1 for L in lines if L.startswith("# "))
    h2 = sum(1 for L in lines if L.startswith("## "))
    h3 = sum(1 for L in lines if L.startswith("### "))
    total = h1 + h2 + h3
    if total < 3:
        return "sparse"
    if h2 + h3 < 5:
        return "shallow"
    return "good"


def scan_one(slug: str, source_path: Path) -> dict:
    with source_path.open("r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    bi = _find_back_matter_index(lines) or {"present": False}
    pm_present = _detect_page_markers(lines)
    hq = _heading_quality(lines)

    return {
        "schema_version": 1,
        "slug": slug,
        "source_file": str(source_path),
        "source_total_lines": len(lines),
        "book_index": bi,
        "page_markers": {"present": pm_present},
        "headings": {"quality": hq},
        "enumerated_named_methods": {"examples_seen": []},
        "scan_kind": "mechanical-baseline",
    }


def discover_sources(corpus_root: Path) -> list[tuple[str, Path]]:
    """Return [(slug, source_path), ...] for every converted source we can find.

    Preference: ``sources/converted/{slug}.md`` (the canonical mechanical-extraction
    input). Fallback: the deep ref itself, when there is no converted source.
    """
    out: list[tuple[str, Path]] = []
    refs_dir = corpus_root / "references"
    converted_dir = corpus_root / "sources" / "converted"
    deeps = sorted(refs_dir.glob("*-deep.md"))
    seen: set[str] = set()
    for deep in deeps:
        slug = deep.stem[: -len("-deep")]
        if slug in seen:
            continue
        seen.add(slug)
        # Prefer converted markdown if it exists
        converted = converted_dir / f"{slug}.md"
        if converted.is_file():
            out.append((slug, converted))
        else:
            out.append((slug, deep))
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Mechanical baseline discovery scan")
    parser.add_argument("--corpus", required=True, help="Path to corpus root (e.g. corpus.local/aarbuddy)")
    parser.add_argument("--output-dir", default=None, help="Override output dir (default: _planning/discovery/)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing discovery files")
    parser.add_argument("--limit", type=int, default=None, help="Scan only the first N sources (for testing)")
    args = parser.parse_args(argv)

    corpus_root = Path(args.corpus).expanduser()
    if not corpus_root.is_dir():
        print(f"ERROR: corpus root not found: {corpus_root}", file=sys.stderr)
        return 2

    out_dir = Path(args.output_dir).expanduser() if args.output_dir else Path("_planning/discovery")
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = discover_sources(corpus_root)
    if args.limit:
        sources = sources[: args.limit]

    written = 0
    skipped = 0
    with_index = 0
    for slug, src in sources:
        out_path = out_dir / f"{slug}.json"
        if out_path.is_file() and not args.force:
            skipped += 1
            continue
        record = scan_one(slug, src)
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
            f.write("\n")
        if record["book_index"].get("present"):
            with_index += 1
        written += 1

    print(f"Scanned {len(sources)} sources")
    print(f"  Wrote: {written}; skipped (existing): {skipped}")
    print(f"  With back-matter index detected: {with_index}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
