#!/usr/bin/env python3
"""Remove all corpus content matching a given prefix.

Use: python3 scripts/remove-corpus.py {prefix}
Or:  npm run remove-corpus -- {prefix}

Removes:
- corpus.commons/demo/references/{prefix}-*.md (light + deep references)
- corpus.commons/demo/references/_audit/_ingest_pass_*_{prefix}-*.md (Pass artefacts)
- corpus.commons/demo/distillations/{task}/{prefix}-*.md (distillations)
- corpus.commons/demo/sources/original/{prefix}-*.* (binaries + .source.md sidecars)
- corpus.commons/demo/sources/converted/{prefix}-*.md (converted markdown)
- corpus.commons/demo/sources/converted/{md-slug}-images/ (image dirs; gitignored)
- Lines containing {prefix}- in REFERENCE-INDEX.md and per-task distillation indexes
- IMAGE-INDEX.yaml entries whose source_ref starts with {prefix}-

Designed for the OpenStax PoC corpus removal. Forks running their own corpus can use the same script with a different prefix.

Requires Python 3.9+ (uses PEP 585 generic syntax: set[str], list[str]).
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_ROOT = REPO_ROOT / "corpus.commons" / "demo"


def affected_md_slugs(prefix: str) -> set[str]:
    """Find every converted-md slug starting with {prefix}-."""
    slugs = set()
    converted_dir = CORPUS_ROOT / "sources" / "converted"
    if not converted_dir.is_dir():
        return slugs
    for f in converted_dir.glob(f"{prefix}-*.md"):
        slugs.add(f.stem)
    return slugs


def remove_files(prefix: str, dry_run: bool = False) -> int:
    """Delete reference, distillation, source, and pass-artefact files matching the prefix."""
    targets = [
        CORPUS_ROOT / "references",
        CORPUS_ROOT / "sources" / "original",
        CORPUS_ROOT / "sources" / "converted",
    ]
    # plus every distillation task subdir
    distillations_root = CORPUS_ROOT / "distillations"
    if distillations_root.is_dir():
        targets.extend(d for d in distillations_root.iterdir() if d.is_dir())
    count = 0
    for d in targets:
        if not d.is_dir():
            continue
        for f in list(d.glob(f"{prefix}-*")):
            if f.is_file():
                if dry_run:
                    print(f"  would delete: {f.relative_to(REPO_ROOT)}")
                else:
                    f.unlink()
                count += 1
    # Pass artefacts have prefix in middle of name
    audit_dir = CORPUS_ROOT / "references" / "_audit"
    if audit_dir.exists():
        for f in list(audit_dir.glob(f"_ingest_pass_*_{prefix}-*.md")):
            if dry_run:
                print(f"  would delete: {f.relative_to(REPO_ROOT)}")
            else:
                f.unlink()
            count += 1
    return count


def remove_directories(md_slugs: set[str], dry_run: bool = False) -> int:
    """Delete image directories inline with the converted markdown. Gitignored but on disk."""
    count = 0
    converted_dir = CORPUS_ROOT / "sources" / "converted"
    for md_slug in md_slugs:
        d = converted_dir / f"{md_slug}-images"
        if d.is_dir():
            if dry_run:
                print(f"  would delete dir: {d.relative_to(REPO_ROOT)}")
            else:
                shutil.rmtree(d)
            count += 1
    return count


def filter_index_lines(prefix: str, dry_run: bool = False) -> int:
    """Remove lines containing {prefix}- from the markdown indexes."""
    indexes = [CORPUS_ROOT / "references" / "REFERENCE-INDEX.md"]
    distillations_root = CORPUS_ROOT / "distillations"
    if distillations_root.is_dir():
        for task_dir in distillations_root.iterdir():
            if task_dir.is_dir():
                indexes.extend(task_dir.glob("*-DISTILLATION-INDEX.md"))
    needle = f"{prefix}-"
    edited = 0
    for path in indexes:
        if not path.is_file():
            continue
        original = path.read_text().splitlines(keepends=True)
        kept = [line for line in original if needle not in line]
        # Collapse runs of >2 blank lines (artefact of removing entries)
        collapsed: list[str] = []
        blank_run = 0
        for line in kept:
            if line.strip() == "":
                blank_run += 1
                if blank_run <= 2:
                    collapsed.append(line)
            else:
                blank_run = 0
                collapsed.append(line)
        if collapsed != original:
            if dry_run:
                print(f"  would edit: {path.relative_to(REPO_ROOT)}")
            else:
                path.write_text("".join(collapsed))
            edited += 1
    return edited


def filter_image_index(prefix: str, dry_run: bool = False) -> int:
    """Remove YAML entries whose source_ref starts with {prefix}-. Block-aware filter (handles indented entries spanning multiple lines)."""
    path = CORPUS_ROOT / "sources" / "converted" / "IMAGE-INDEX.yaml"
    if not path.is_file():
        return 0
    text = path.read_text()
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    removed_blocks = 0
    while i < len(lines):
        line = lines[i]
        # Each entry starts with "- file:" at column 0 indentation
        if line.startswith("- "):
            # Look ahead at the entry's source_ref field
            block = [line]
            j = i + 1
            while j < len(lines) and not lines[j].startswith("- ") and not lines[j].startswith("# ----"):
                block.append(lines[j])
                j += 1
            # Check whether any line in block has source_ref pointing at the prefix
            block_text = "".join(block)
            if re.search(rf"source_ref:\s*[\"']?{re.escape(prefix)}-", block_text):
                removed_blocks += 1
            else:
                out.extend(block)
            i = j
        else:
            out.append(line)
            i += 1
    if removed_blocks > 0 and not dry_run:
        path.write_text("".join(out))
    return removed_blocks


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="remove-corpus.py",
        description=(
            "Remove all corpus content matching a given prefix. "
            "Deletes references, distillations, source binaries, converted markdown, "
            "audit artefacts, image directories, and any matching lines in the markdown "
            "indexes and IMAGE-INDEX.yaml. Destructive; use --dry-run to preview."
        ),
        epilog="Example: python3 scripts/remove-corpus.py openstax --dry-run",
    )
    parser.add_argument(
        "prefix",
        help="The slug prefix to remove (lowercase, hyphen-separated). E.g. 'openstax'.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be deleted without touching disk.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Skip the confirmation prompt. Required for non-interactive use.",
    )
    args = parser.parse_args()

    prefix = args.prefix.rstrip("-")
    if not re.match(r"^[a-z0-9][a-z0-9-]*$", prefix):
        print(f"Invalid prefix: {prefix!r}. Use lowercase, hyphen-separated.", file=sys.stderr)
        return 2

    mode = "DRY-RUN" if args.dry_run else "REMOVING"
    print(f"{mode} corpus prefix: {prefix}")
    print(f"Repo root: {REPO_ROOT}")
    print()

    md_slugs = affected_md_slugs(prefix)
    print(f"Identified {len(md_slugs)} affected converted-md slug(s):")
    for s in sorted(md_slugs):
        print(f"  - {s}")
    print()

    if not args.dry_run and not args.yes and sys.stdin.isatty():
        reply = input(f"Proceed with deleting all '{prefix}-*' corpus content? [y/N] ").strip().lower()
        if reply not in ("y", "yes"):
            print("Aborted.")
            return 1

    n_files = remove_files(prefix, dry_run=args.dry_run)
    print(f"{'Would delete' if args.dry_run else 'Deleted'} {n_files} source/reference/distillation/pass-artefact file(s).")

    n_dirs = remove_directories(md_slugs, dry_run=args.dry_run)
    print(f"{'Would delete' if args.dry_run else 'Deleted'} {n_dirs} image director(ies) (gitignored, were on local disk).")

    n_indexes = filter_index_lines(prefix, dry_run=args.dry_run)
    print(f"{'Would filter' if args.dry_run else 'Filtered'} {n_indexes} markdown index file(s).")

    n_yaml = filter_image_index(prefix, dry_run=args.dry_run)
    print(f"{'Would remove' if args.dry_run else 'Removed'} {n_yaml} YAML entr(ies) from IMAGE-INDEX.yaml.")

    print()
    if args.dry_run:
        print("Dry run only. Re-run without --dry-run to apply.")
    else:
        print("Done. Run `npm run build` to verify the build still passes.")
        print("Re-ingest your own sources with the `ingesting-resources` skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
