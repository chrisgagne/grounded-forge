#!/usr/bin/env python3
"""Merge per-source staging files into a corpus's IMAGE-INDEX.yaml.

Image classification runs per source, in parallel, and each source agent
writes its result to ``docs/images/_ingest_image_index_{slug}.yaml``. The
corpus-level index is merged from those staging files once every per-source
step has completed — the same staging-then-assemble shape the reference and
concept indexes use, and for the same reason: parallel agents must not
read-modify-write one shared file.

The index is merged, not rebuilt. A source with a staging file has its entries
replaced by the staging file's; every other entry already in the index is
carried forward unchanged. The index is the durable copy: ``docs/images/`` is
gitignored, so staging files are missing on a fresh clone, and some corpora
hold entries that never had one (ported from an older image library, or
curated by hand). A rebuild from staging alone would delete those. Removing a
source's entries is therefore explicit: ``--drop SLUG``.

The merge edits the file's text rather than re-dumping it, so carried entries
keep their formatting and the comments around them (demo's schema notes and
per-source provenance lines). The result is parsed back and checked against the
expected entries before anything is written, and a merge that changes nothing
writes nothing.

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
    python3 scripts/build_indexes/build_image_index.py --corpus demo --drop SLUG [--drop SLUG ...]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
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

PROVENANCE = """\
# Written by scripts/build_indexes/build_image_index.py. Each run replaces
# the entries of every source that has a staging file at
# docs/images/_ingest_image_index_{slug}.yaml and carries every other entry
# forward, so this file, not the staging, is the record. To change a source's
# entries, edit its staging file and rerun; to remove them, rerun with
# --drop {slug}.
"""

HEADER = """\
# IMAGE-INDEX.yaml
#
# The persistent record of substantive images extracted from this corpus.
# Image files live alongside the converted markdown at
# {source-slug}-images/ and are gitignored; this index is the durable
# artefact that travels with the repo. Paths are relative to this file's
# directory ({corpus-root}/sources/converted/).
#
""" + PROVENANCE + """\
#
# Classification is SUBSTANTIVE (kept and indexed) or DECORATIVE (deleted,
# not indexed). Only SUBSTANTIVE entries appear here.
"""

# Indexes written before the merge carry this claim in their preamble; it is
# swapped for the current wording so the file stops saying it is rebuildable.
WHOLLY_DERIVED = """\
# Derived artefact: assembled by scripts/build_indexes/build_image_index.py
# from the per-source staging files at docs/images/_ingest_image_index_*.yaml.
# Never hand-edit it; edit the staging file and rebuild.
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


def dump(entries: list[dict]) -> str:
    return yaml.safe_dump(entries, sort_keys=False, allow_unicode=True,
                          default_flow_style=False, width=88)


def section(slug: str, entries: list[dict]) -> str:
    return (f"\n# {'=' * 58}\n# {slug}\n# {len(entries)} substantive "
            f"{'entry' if len(entries) == 1 else 'entries'}\n# {'=' * 58}\n" + dump(entries))


def splice(text: str, existing: list[dict], staged: dict[str, list[dict]],
           drop: set[str]) -> str:
    """Rewrite the index text: replace staged sources' entries, cut dropped ones.

    Each top-level ``- `` line starts an entry (nested lists and block scalars
    are always indented). The comment and blank lines that end a chunk are the
    lead-in to the next entry, usually a source's section header, so they travel
    with that entry: kept when it stays, kept ahead of the replacement for a
    staged source's first entry, cut when it goes. A staged source whose
    entries already match the index keeps its text as it is.
    """
    preamble, *chunks = re.split(r"(?m)^(?=- )", text)
    if len(chunks) != len(existing):
        raise ValueError(f"{len(chunks)} top-level entries in the text, "
                         f"{len(existing)} parsed")
    preamble = preamble.replace(WHOLLY_DERIVED, PROVENANCE)

    lead, bodies = [], []
    pending = ""
    for chunk in chunks:
        lines = chunk.splitlines(keepends=True)
        cut = len(lines)
        while cut > 1 and (not lines[cut - 1].strip() or lines[cut - 1].startswith("#")):
            cut -= 1
        lead.append(pending)
        bodies.append("".join(lines[:cut]))
        pending = "".join(lines[cut:])
    trailer = pending

    indexed: dict[str | None, list[dict]] = {}
    for e in existing:
        indexed.setdefault(e.get("source_ref") or None, []).append(e)
    staged = {s: v for s, v in staged.items() if v != indexed.get(s)}

    out, placed = [preamble], set()
    for entry, before, body in zip(existing, lead, bodies):
        slug = entry.get("source_ref") or None
        if slug in drop:
            continue
        if slug in staged:
            if slug not in placed:
                placed.add(slug)
                if staged[slug]:
                    out += [before, dump(staged[slug])]
            continue
        out += [before, body]
    out.append(trailer)
    new = [section(s, staged[s]) for s in sorted(staged) if s not in placed and staged[s]]
    if new and not "".join(out).endswith("\n"):
        out.append("\n")
    return "".join(out + new)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--corpus", required=True, help="corpus name, e.g. demo")
    ap.add_argument("--check", action="store_true",
                    help="report what would be written without writing it")
    ap.add_argument("--drop", action="append", default=[], metavar="SLUG",
                    help="remove every entry whose source_ref is SLUG (repeatable)")
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
        # An empty staging file still replaces its source's entries: the
        # source was inspected and nothing in it is substantive.
        by_slug[slug] = entries
        if not entries:
            empty.append(slug)

    dest = converted / "IMAGE-INDEX.yaml"
    existing: list[dict] = []
    if dest.exists():
        loaded = yaml.safe_load(dest.read_text(encoding="utf-8"))
        if loaded is not None and not (isinstance(loaded, list)
                                       and all(isinstance(e, dict) for e in loaded)):
            sys.stderr.write(f"{dest.relative_to(REPO_ROOT)} is not a list of entries; "
                             f"refusing to merge into it.\n")
            return 1
        existing = loaded or []

    # Group what is already indexed by source. Entries with no source_ref can't
    # be matched to a staging file, so they always carry forward, under None.
    indexed: dict[str | None, list[dict]] = {}
    for e in existing:
        indexed.setdefault(e.get("source_ref") or None, []).append(e)

    drop = set(args.drop)
    staged = {s: v for s, v in by_slug.items() if s not in drop}
    carried = {s: v for s, v in indexed.items()
               if s not in by_slug and s not in drop}
    merged: dict[str | None, list[dict]] = {**carried, **staged}

    total = sum(len(v) for v in merged.values())
    missing_files = [
        e.get("file") for entries in merged.values() for e in entries
        if e.get("file") and not (converted / str(e["file"])).exists()
    ]

    print(f"corpus:            {args.corpus}")
    print(f"staging files:     {len(by_slug)} indexable for this corpus")
    if foreign:
        print(f"other corpora:     {len(foreign)} staging files skipped")
    if unfinished:
        print(f"NOT INDEXED:       {len(unfinished)} sources converted and image-classified "
              f"but with no deep reference — their ingestion never completed:")
        for s_ in sorted(unfinished):
            print(f"  {s_}")
    print(f"substantive:       {sum(len(v) for v in staged.values())} staged entries "
          f"across {sum(1 for v in staged.values() if v)} sources")
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

    # Every replacement is reported. A staging file that holds fewer entries
    # than the index had deletes the difference, and a truncated staging file
    # looks the same as a reclassification. Staging is keyed by slug alone, so a
    # slug ingested into two corpora shares one staging file, which may hold the
    # other corpus's descriptions.
    for slug in sorted(staged):
        before = indexed.get(slug, [])
        if staged[slug] == before:
            continue
        print(f"replaced:          {slug}: {len(before)} entries in the index, "
              f"{len(staged[slug])} in staging" if before else
              f"added:             {slug}: {len(staged[slug])} entries")
        if len(staged[slug]) < len(before):
            print(f"WARN {slug}: {len(before) - len(staged[slug])} entries will go")
        others = sorted(p.parent.parent.name for p in REPO_ROOT.glob(
            f"corpus.*/*/references/{slug}-deep.md") if p.parent.parent != root)
        if before and others:
            print(f"WARN {slug}: also ingested in {', '.join(others)}; its staging file may "
                  f"describe that corpus's copy, so check the diff before committing")

    if carried:
        print(f"carried forward:   {sum(len(v) for v in carried.values())} entries across "
              f"{len(carried)} sources with no staging file")
        for slug in sorted(carried, key=lambda s: (s is None, s or "")):
            # A carried source with no deep reference may have been removed
            # without --drop; flagged so the operator can tell.
            flag = ("  (no source_ref)" if slug is None
                    else "" if (refs_dir / f"{slug}-deep.md").exists() else "  (no deep reference)")
            print(f"  {len(carried[slug]):5d}  {slug or '-'}{flag}")

    for slug in sorted(drop):
        print(f"dropped:           {slug}: {len(indexed.get(slug, []))} entries"
              + ("" if slug in indexed else " (none in the index; check the slug)"))
        if (STAGING_DIR / f"_ingest_image_index_{slug}.yaml").exists():
            print(f"WARN --drop {slug}: its staging file still exists; the next run without "
                  f"--drop {slug} will index it again")

    print(f"index:             {len(existing)} entries before, {total} after")

    old_text = dest.read_text(encoding="utf-8") if dest.exists() else ""
    try:
        text = splice(old_text, existing, staged, drop) if existing else HEADER + "".join(
            section(s, staged[s]) for s in sorted(staged) if staged[s])
    except ValueError as exc:
        sys.stderr.write(f"\nRefusing to write: can't split {dest.relative_to(REPO_ROOT)} "
                         f"into entries ({exc}).\n")
        return 1

    # The written file must hold exactly the merged entries, whatever the text
    # edit did; anything else leaves the index as it was.
    key = lambda e: json.dumps(e, sort_keys=True, default=str)
    written = yaml.safe_load(text) or []
    if Counter(map(key, written)) != Counter(key(e) for v in merged.values() for e in v):
        sys.stderr.write(f"\nRefusing to write: the merged text of "
                         f"{dest.relative_to(REPO_ROOT)} doesn't parse back to the "
                         f"{total} expected entries.\n")
        return 1

    if text == old_text:
        print(f"\nunchanged: {dest.relative_to(REPO_ROOT)}")
        return 0
    if args.check:
        print(f"\nwould rewrite {dest.relative_to(REPO_ROOT)}")
        return 0
    dest.write_text(text, encoding="utf-8")
    print(f"\nwrote {dest.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
