#!/usr/bin/env python3
"""Move image-index staging files out of docs/images/ into _planning/staging/.

Image-index staging lives at
``_planning/staging/{corpus}/images/_ingest_image_index_{slug}.yaml``.
``build_image_index.py`` reads nothing else, so a file in either older layout
is ignored until it is moved:

  ``docs/images/{corpus}/_ingest_image_index_{slug}.yaml``
      already filed by corpus; moved across as it is.
  ``docs/images/_ingest_image_index_{slug}.yaml``
      keyed by slug alone, and shared by every corpus that ingested the slug.

A flat file goes to the one corpus that holds its slug: the corpus with the
slug's deep reference, or, where none has one, its converted text. When several
corpora hold the slug, the file goes to the corpus whose IMAGE-INDEX.yaml
entries for the slug match the file's substantive entries exactly; the file
can't say whose it is, and only that corpus's index can vouch for it. A file
that matches none, or no corpus at all, stays where it is and is reported, as
does a file under a docs/images/ folder that names no corpus. A file already
present at the destination is never overwritten.

Dry run by default; ``--apply`` moves the files.

Usage:
    python3 scripts/migrate-image-staging.py
    python3 scripts/migrate-image-staging.py --apply
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
from scripts.build_indexes.build_image_index import (  # noqa: E402
    LEGACY_ROOT, STAGING_GLOB, load_staging, staging_dir)


def corpora() -> list[Path]:
    return sorted(p for tier in ("corpus.commons", "corpus.local")
                  for p in (REPO_ROOT / tier).glob("*") if p.is_dir())


def indexed(root: Path, slug: str) -> list[dict]:
    index = root / "sources" / "converted" / "IMAGE-INDEX.yaml"
    if not index.is_file():
        return []
    loaded = yaml.safe_load(index.read_text(encoding="utf-8")) or []
    return [e for e in loaded if isinstance(e, dict) and e.get("source_ref") == slug]


def same(a: list[dict], b: list[dict]) -> bool:
    key = lambda e: json.dumps(e, sort_keys=True, default=str)
    return Counter(map(key, a)) == Counter(map(key, b))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--apply", action="store_true", help="move the files (default: dry run)")
    args = ap.parse_args()

    roots = corpora()
    names = {r.name for r in roots}
    moves: list[tuple[Path, Path, str]] = []
    left: list[str] = []
    for path in sorted(LEGACY_ROOT.glob(f"*/{STAGING_GLOB}")):
        corpus = path.parent.name
        if corpus not in names:
            left.append(f"{path.relative_to(REPO_ROOT)}: no corpus named {corpus!r}")
            continue
        moves.append((path, staging_dir(corpus) / path.name, ""))
    for path in sorted(LEGACY_ROOT.glob(STAGING_GLOB)):
        slug = path.name[len("_ingest_image_index_"):-len(".yaml")]
        holders = ([r for r in roots if (r / "references" / f"{slug}-deep.md").exists()]
                   or [r for r in roots if (r / "sources" / "converted" / f"{slug}.md").exists()])
        entries = load_staging(path)[0]
        if not holders:
            left.append(f"{slug}: no corpus holds this slug")
            continue
        if len(holders) == 1:
            root = holders[0]
            note = "" if same(entries, indexed(root, slug)) else (
                "  (differs from the index; the next merge replaces its entries)")
        else:
            matches = [r for r in holders if same(entries, indexed(r, slug))]
            holding = ", ".join(r.name for r in holders)
            if len(matches) != 1:
                left.append(f"{slug}: in {holding}; the file matches "
                            + (f"{len(matches)} of their indexes" if matches else "none of their indexes"))
                continue
            root = matches[0]
            others = ", ".join(r.name for r in holders if r != root)
            note = f"  (also in {others}; matches {root.name}'s index)"
        moves.append((path, staging_dir(root.name) / path.name, note))

    # The per-corpus files come first, so a flat file bound for the same
    # destination is the one left behind.
    clear, taken = [], set()
    for src, dest, note in moves:
        if dest.exists() or dest in taken:
            left.append(f"{src.relative_to(REPO_ROOT)}: {dest.relative_to(REPO_ROOT)} "
                        f"already exists")
        else:
            clear.append((src, dest, note))
            taken.add(dest)
    moves = clear

    for src, dest, note in moves:
        print(f"{'moved' if args.apply else 'move '}  {src.relative_to(REPO_ROOT)} -> "
              f"{dest.relative_to(REPO_ROOT)}{note}")
        if args.apply:
            dest.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dest)
    if args.apply:
        for d in LEGACY_ROOT.glob("*/"):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
    for line in left:
        print(f"LEFT   {line}")
    print(f"\n{len(moves)} {'moved' if args.apply else 'to move'}, {len(left)} left in place"
          + ("" if args.apply or not moves else ". Rerun with --apply."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
