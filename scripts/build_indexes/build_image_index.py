#!/usr/bin/env python3
"""Assemble a corpus's IMAGE-INDEX.yaml from per-source staging files.

Image classification runs per source, in parallel, and each source agent
writes its result to ``docs/images/_ingest_image_index_{slug}.yaml``. The
corpus-level index is derived from those staging files once every per-source
step has completed — the same staging-then-assemble shape the reference and
concept indexes use, and for the same reason: parallel agents must not
read-modify-write one shared file.

Without this step the staging files are the only record, and the skill's rule
that "if an image is not in IMAGE-INDEX.yaml, it is not part of the library"
quietly makes every classified image invisible.

Staging files were authored before any schema was enforced, so four shapes
exist in the wild. All four are accepted and normalised:

  1. a bare list of entry mappings;
  2. ``{images: [...]}``;
  3. ``{substantive: [...], not_substantive: [...]}``;
  4. ``{substantive: [...], decorative_deleted: [...]}``.

Only substantive entries are indexed. Under shapes 3 and 4 the second key is
the classifier's record of what it rejected: counted, reported, not indexed.
A staging file with no substantive entries is not an error — a statute or a
vector-only PDF legitimately yields none — but it is reported, because the
difference between "inspected, found nothing" and "never inspected" is one
the operator needs to see.

Usage:
    python3 scripts/build_indexes/build_image_index.py --corpus demo
    python3 scripts/build_indexes/build_image_index.py --corpus demo --check
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("PyYAML required: pip install pyyaml\n")
    raise SystemExit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
STAGING_DIR = REPO_ROOT / "docs" / "images"
STAGING_GLOB = "_ingest_image_index_*.yaml"

# Keys holding substantive entries, and keys holding the classifier's record of
# what it rejected. Anything else in a staging mapping is a schema surprise and
# is reported rather than silently dropped.
SUBSTANTIVE_KEYS = ("images", "substantive")
REJECTED_KEYS = ("not_substantive", "decorative_deleted", "decorative")

HEADER = """\
# IMAGE-INDEX.yaml
#
# The persistent record of substantive images extracted from this corpus.
# Image files live alongside the converted markdown at
# {source-slug}-images/ and are gitignored; this index is the durable
# artefact that travels with the repo. Paths are relative to this file's
# directory ({corpus-root}/sources/converted/).
#
# Derived artefact: assembled by scripts/build_indexes/build_image_index.py
# from the per-source staging files at docs/images/_ingest_image_index_*.yaml.
# Never hand-edit it; edit the staging file and rebuild.
#
# Classification is SUBSTANTIVE (kept and indexed) or DECORATIVE (deleted,
# not indexed). Only SUBSTANTIVE entries appear here.
"""


def corpus_root(name: str) -> Path:
    for tier in ("corpus.commons", "corpus.local"):
        p = REPO_ROOT / tier / name
        if p.is_dir():
            return p
    sys.stderr.write(f"No corpus named {name!r} under corpus.commons/ or corpus.local/\n")
    raise SystemExit(1)


def load_staging(path: Path) -> tuple[list[dict], int, list[str]]:
    """Return (substantive entries, rejected count, notes) for one staging file."""
    notes: list[str] = []
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))

    if raw is None:
        return [], 0, ["file holds only comments"]

    if isinstance(raw, list):
        entries, rejected = raw, 0
    elif isinstance(raw, dict):
        entries = []
        for key in SUBSTANTIVE_KEYS:
            if isinstance(raw.get(key), list):
                entries.extend(raw[key])
        rejected = sum(
            len(raw[key]) for key in REJECTED_KEYS if isinstance(raw.get(key), list)
        )
        unknown = set(raw) - set(SUBSTANTIVE_KEYS) - set(REJECTED_KEYS)
        if unknown:
            notes.append(f"unrecognised top-level keys ignored: {sorted(unknown)}")
    else:
        return [], 0, [f"unusable shape {type(raw).__name__}"]

    kept = [e for e in entries if isinstance(e, dict)]
    if len(kept) != len(entries):
        notes.append(f"{len(entries) - len(kept)} non-mapping entries dropped")
    return kept, rejected, notes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--corpus", required=True, help="corpus name, e.g. demo")
    ap.add_argument("--check", action="store_true",
                    help="report what would be written without writing it")
    args = ap.parse_args()

    root = corpus_root(args.corpus)
    refs_dir = root / "references"
    converted = root / "sources" / "converted"
    if not converted.is_dir():
        sys.stderr.write(f"No converted/ directory at {converted}\n")
        return 1

    by_slug: dict[str, list[dict]] = {}
    rejected_total = 0
    foreign: list[str] = []
    unfinished: list[str] = []
    empty: list[str] = []
    problems: list[str] = []

    for path in sorted(STAGING_DIR.glob(STAGING_GLOB)):
        slug = path.name[len("_ingest_image_index_"):-len(".yaml")]
        # Staging is repo-wide, and a source is only indexable once it has a
        # deep reference. A staging file with no deep ref is either another
        # corpus's, or this corpus's ingestion stopped before Pass A — the
        # distinction matters, so the two are reported separately.
        if not (refs_dir / f"{slug}-deep.md").exists():
            if (converted / f"{slug}.md").exists():
                unfinished.append(slug)
            else:
                foreign.append(slug)
            continue
        entries, rejected, notes = load_staging(path)
        rejected_total += rejected
        for n in notes:
            problems.append(f"{slug}: {n}")
        if entries:
            by_slug[slug] = entries
        else:
            empty.append(slug)

    total = sum(len(v) for v in by_slug.values())
    missing_files = [
        e.get("file") for entries in by_slug.values() for e in entries
        if e.get("file") and not (converted / str(e["file"])).exists()
    ]

    print(f"corpus:            {args.corpus}")
    print(f"staging files:     {len(by_slug) + len(empty)} indexable for this corpus")
    if foreign:
        print(f"other corpora:     {len(foreign)} staging files skipped")
    if unfinished:
        print(f"NOT INDEXED:       {len(unfinished)} sources converted and image-classified "
              f"but with no deep reference — their ingestion never completed:")
        for s_ in sorted(unfinished):
            print(f"  {s_}")
    print(f"substantive:       {total} entries across {len(by_slug)} sources")
    print(f"rejected on disk:  {rejected_total} recorded as not-substantive")
    if empty:
        print(f"no substantive:    {len(empty)} sources — {', '.join(sorted(empty)[:4])}"
              + (" …" if len(empty) > 4 else ""))
    if missing_files:
        print(f"WARN image files absent from converted/: {len(missing_files)}")
        for f in missing_files[:5]:
            print(f"  {f}")
    for p in problems:
        print(f"WARN {p}")

    if args.check:
        return 0

    dest = converted / "IMAGE-INDEX.yaml"
    # Refuse to replace a populated index with an empty one. A corpus whose
    # staging files have been cleaned up, or a mistyped --corpus, would
    # otherwise silently delete a hand-curated index — and the images it
    # describes are gitignored, so the descriptions would be the only copy.
    if total == 0 and dest.exists() and "\n- file:" in dest.read_text(encoding="utf-8"):
        sys.stderr.write(
            f"\nRefusing to write: no staging entries found, but {dest.relative_to(REPO_ROOT)} "
            f"already holds entries.\nRebuilding from empty staging would delete them. Check "
            f"--corpus, or confirm the staging files under\n{STAGING_DIR.relative_to(REPO_ROOT)}/ "
            f"are present.\n")
        return 1

    out = [HEADER]
    for slug in sorted(by_slug):
        entries = by_slug[slug]
        out.append(f"\n# {'=' * 58}\n# {slug}\n# {len(entries)} substantive "
                   f"{'entry' if len(entries) == 1 else 'entries'}\n# {'=' * 58}\n")
        out.append(yaml.safe_dump(entries, sort_keys=False, allow_unicode=True,
                                  default_flow_style=False, width=88))

    dest.write_text("".join(out), encoding="utf-8")
    print(f"\nwrote {dest.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
