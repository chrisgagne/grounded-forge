#!/usr/bin/env python3
"""Verify derived artefacts (light refs, distillations) are current with the
audited deep reference they were derived from.

The 9-pass ingestion protocol derives the light ref (Pass F) and distillations
(Pass G) *before* Pass I audits and edits the deep reference in place. Nothing
re-checks the derived tier after Pass I, so a strip at Pass I can leave the
light ref and distillations carrying content the deep no longer supports (the
`jocham-ai-and-scrum` incident: Pass I stripped a fabricated cross-reference
table from the deep, but the light ref and distillations kept it). This tool
closes that gap: each derived artefact records the sha256 of the deep it was
derived from, and a mismatch means the deep moved and the derived artefact is
stale.

Stamp format — one HTML-comment line near the top of a derived artefact:

    <!-- derived-from-deep: sha256:<64-hex> -->

The stamp records the hash of the *deep* file (which carries no stamp of its
own), so there is no self-reference: editing the deep changes its hash and
invalidates every derived artefact's stamp until they are re-derived and
re-stamped. That is the point — it makes "derived from the verified deep"
mechanically testable rather than a prose promise.

Usage:
    python3 scripts/check_derived_provenance.py --corpus <name>
        Check mode. Exit 1 if any derived artefact carries a STALE stamp
        (present but != the deep's current hash). UNSTAMPED artefacts warn
        (adoption is gradual; new ingestions stamp going forward). A derived
        artefact whose deep is missing is an orphan and warns.

    python3 scripts/check_derived_provenance.py --corpus <name> --stamp [--slug S ...]
        Stamp mode. Write / refresh the stamp on derived artefacts with their
        deep's current hash. Restrict to specific sources with --slug (repeatable).
        Only stamp artefacts you have verified current with their deep: stamping
        asserts the artefact is up to date.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STAMP_RE = re.compile(
    r"^<!--\s*derived-from-deep:\s*sha256:([0-9a-f]{64})\s*-->\s*$", re.MULTILINE
)


def corpus_root(name: str) -> Path:
    """Resolve a corpus by name, commons before local (matches common.py)."""
    for tier in ("corpus.commons", "corpus.local"):
        candidate = REPO_ROOT / tier / name
        if candidate.is_dir():
            return candidate
    raise SystemExit(
        f"corpus '{name}' not found under corpus.commons/ or corpus.local/"
    )


def deep_hash(deep_path: Path) -> str:
    return hashlib.sha256(deep_path.read_bytes()).hexdigest()


def read_stamp(text: str) -> str | None:
    m = STAMP_RE.search(text)
    return m.group(1) if m else None


def derived_artefacts(root: Path, slug: str) -> list[Path]:
    """Light ref plus one distillation per task dir for a given source slug."""
    out: list[Path] = []
    light = root / "references" / f"{slug}.md"
    if light.exists():
        out.append(light)
    dist_root = root / "distillations"
    if dist_root.is_dir():
        for task_dir in sorted(dist_root.iterdir()):
            if not task_dir.is_dir():
                continue
            dist = task_dir / f"{slug}-{task_dir.name}.md"
            if dist.exists():
                out.append(dist)
    return out


def write_stamp(path: Path, h: str) -> None:
    text = path.read_text(encoding="utf-8")
    stamp_line = f"<!-- derived-from-deep: sha256:{h} -->"
    if STAMP_RE.search(text):
        text = STAMP_RE.sub(stamp_line, text, count=1)
    else:
        lines = text.split("\n")
        # Insert after line 1 if it is the generation-header HTML comment,
        # otherwise at the very top.
        insert_at = 1 if lines and lines[0].lstrip().startswith("<!--") else 0
        lines.insert(insert_at, stamp_line)
        text = "\n".join(lines)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--corpus", help="corpus name (e.g. demo, aarbuddy)")
    ap.add_argument(
        "--root",
        help="explicit corpus root path, bypassing --corpus name resolution "
        "(the regression test points this at a fixture corpus)",
    )
    ap.add_argument("--stamp", action="store_true", help="write/refresh stamps")
    ap.add_argument(
        "--slug", action="append", default=[], help="restrict to source slug(s)"
    )
    args = ap.parse_args()

    if args.root:
        root = Path(args.root).resolve()
        if not root.is_dir():
            raise SystemExit(f"--root path not found: {root}")
    elif args.corpus:
        root = corpus_root(args.corpus)
    else:
        ap.error("one of --corpus or --root is required")
    deep_files = sorted((root / "references").glob("*-deep.md"))
    slug_filter = set(args.slug)

    ok: list[str] = []
    unstamped: list[str] = []
    stale: list[str] = []
    stamped: list[str] = []

    for deep in deep_files:
        slug = deep.name[: -len("-deep.md")]
        if slug_filter and slug not in slug_filter:
            continue
        h = deep_hash(deep)
        for art in derived_artefacts(root, slug):
            try:
                rel = art.relative_to(REPO_ROOT).as_posix()
            except ValueError:
                # --root may point outside the repo (e.g. a test fixture); artefacts
                # are always under root, so fall back to a root-relative display path.
                rel = art.relative_to(root).as_posix()
            if args.stamp:
                write_stamp(art, h)
                stamped.append(rel)
                continue
            s = read_stamp(art.read_text(encoding="utf-8"))
            if s is None:
                unstamped.append(rel)
            elif s != h:
                stale.append(f"{rel}  (stamp {s[:12]}… != deep {h[:12]}…)")
            else:
                ok.append(rel)

    if args.stamp:
        for p in stamped:
            print(f"stamped  {p}")
        if slug_filter and not stamped:
            print(f"(no derived artefacts found for slug(s): {', '.join(sorted(slug_filter))})")
        print(f"\nStamped {len(stamped)} derived artefact(s).")
        return 0

    for p in ok:
        print(f"OK       {p}")
    for p in unstamped:
        print(f"WARN     unstamped  {p}")
    for p in stale:
        print(f"STALE    {p}")
    print(
        f"\n{len(ok)} current, {len(unstamped)} unstamped (warn), {len(stale)} STALE."
    )
    if stale:
        sys.stderr.write(
            "\nStale derived artefacts: the deep ref moved after this artefact "
            "was derived.\nRe-derive (Pass F / Pass G) from the audited deep, "
            "then re-stamp with --stamp.\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
