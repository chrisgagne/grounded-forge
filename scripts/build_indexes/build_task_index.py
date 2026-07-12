"""Assemble per-axis ``task-index.json`` files from the per-task
DISTILLATION-INDEX.md files.

The task-axis indexes are situation routers, partitioned by phase or
situation, each row mapping a need to a reference + a distillation file.
The current `.md` shape is operator-authored markdown tables; this script
parses those tables mechanically and emits one JSON file per task axis.

One file per axis, not one bundled file: the runtime only loads the
axis it needs, so bundling would charge every query the full task-axis
token cost regardless of which axis applies. Co-locates each JSON next
to the .md it replaces.

Phase 3 contract: JSON ships alongside the .md indexes. Phase 4 switches
the runtime skills to read JSON.

Inputs:
- ``corpus.commons/{corpus}/distillations/{task}/{TASK}-DISTILLATION-INDEX.md``
- ``corpus.commons/{corpus}/references/slug-table.json``

Outputs:
- ``corpus.commons/{corpus}/distillations/{task}/task-index.json`` (per axis)

The parser is intentionally simple: it walks the markdown line by line,
collects rows from every pipe-table it finds, and groups them under the
section heading they appeared in. Tables with 3 columns are treated as
quick-start rows ``(situation, reference, distillation)``; tables with 4
columns as phase-by-phase rows ``(need, reference, distillation, when)``.
Tables with other shapes are recorded as-is in a ``raw_rows`` list so the
operator can see what was skipped.

Distillation references are matched back to source slugs via filename
suffix-stripping (``openstax-foo-decision-making.md`` → ``openstax-foo``).

Usage:

    python -m scripts.build_indexes.build_task_index --corpus demo
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from .common import corpus_root, index_output_dir, load_slug_table, repo_root, slug_to_id


_TABLE_DIVIDER = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$")
_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_BACKTICK_FILE = re.compile(r"`([^`]+\.md)`")
# A distillation-filename token, backticked or bare. Anchored on a
# word-boundary-ish left edge so it doesn't grab mid-word; the ``-{task}.md``
# tail is checked in ``_slug_from_distillation_filename``.
_FILENAME_TOKEN = re.compile(r"`?([A-Za-z0-9][A-Za-z0-9-]*\.md)`?")


def _parse_pipe_row(line: str) -> list[str] | None:
    """Parse a single markdown pipe-table row. Returns None if the line is
    not a pipe-table row.
    """
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    inner = stripped.strip("|")
    cells = [c.strip() for c in inner.split("|")]
    return cells


def _slug_from_distillation_filename(filename: str, task: str) -> str | None:
    base = filename.rsplit("/", 1)[-1].removesuffix(".md")
    suffix = f"-{task}"
    if base.endswith(suffix):
        return base[: -len(suffix)]
    return None


def _extract_distillation_filename(cell: str) -> str | None:
    m = _BACKTICK_FILE.search(cell)
    return m.group(1) if m else None


def _ids_from_row(cells: list[str], task: str, slug_id: dict[str, str]) -> list[str]:
    """Scan every cell of a row for ``{slug}-{task}.md`` distillation
    filenames and return the resolved slug-IDs in order, de-duplicated.

    Cell order varies across the corpus's DISTILLATION-INDEX.md views
    (filenames land in different columns, and some are un-backticked), so
    routing is cell-order-agnostic: any cell may carry the filenames. Both
    backticked and bare filename tokens are matched.
    """
    ids: list[str] = []
    for cell in cells:
        for fp in _FILENAME_TOKEN.findall(cell):
            slug = _slug_from_distillation_filename(fp, task)
            rid = slug_id.get(slug) if slug else None
            if rid is not None and rid not in ids:
                ids.append(rid)
    return ids


def _section_title(line: str) -> tuple[int, str] | None:
    m = _HEADING.match(line.rstrip())
    if not m:
        return None
    return len(m.group(1)), m.group(2).strip()


def _parse_index_file(path: Path, task: str, slug_id: dict[str, str]) -> dict:
    """Walk one DISTILLATION-INDEX.md, emit a structured task entry."""
    sections: list[dict] = []
    current_section_stack: list[tuple[int, str]] = []  # (level, title)

    in_table = False
    pending_header: list[str] | None = None
    current_rows: list[dict] = []
    current_table_shape: int | None = None

    def flush_table() -> None:
        nonlocal current_rows, current_table_shape, pending_header, in_table
        if current_rows:
            section_path = [t for _, t in current_section_stack]
            # Skip the in-document "Format" example tables — they document
            # the table shape, not routing rows. Identified by section
            # title and by the single-cell ellipsis row.
            first = current_rows[0]
            first_cells = first if isinstance(first, list) else list(first.values())
            is_format_example = (
                any("format" == t.lower() for t in section_path)
                and len(current_rows) == 1
                and all(
                    (c == "..." or c == "" or c is None or c == [])
                    for c in first_cells
                )
            )
            # "Quick start / quick lookup" tables are sometimes a redundant
            # view of a routing surface other tables already cover, and
            # sometimes the *primary* routing surface (some corpora carry no
            # 4-column phase tables at all). Tag them here and drop only the
            # genuinely-redundant ones in a second pass below, once every
            # section's ids are known. Never drop eagerly on the title alone.
            is_quick = current_table_shape == 3 and (
                section_path
                and "quick" in section_path[-1].lower()
            )
            if not is_format_example:
                columns = (
                    ["need", "id", "when"]
                    if current_table_shape == 4
                    else ["situation", "ids"]
                    if current_table_shape == 3
                    else None
                )
                sections.append(
                    {
                        "section": section_path[-1] if section_path else None,
                        "columns": columns,
                        "rows": current_rows,
                        "_quick": is_quick,
                    }
                )
        current_rows = []
        current_table_shape = None
        pending_header = None
        in_table = False

    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    for idx, raw in enumerate(lines):
        heading = _section_title(raw)
        if heading is not None:
            flush_table()
            level, title = heading
            current_section_stack = [
                (l, t) for (l, t) in current_section_stack if l < level
            ]
            current_section_stack.append((level, title))
            continue

        cells = _parse_pipe_row(raw)
        if cells is None:
            flush_table()
            continue

        # divider line — confirm the header row
        if _TABLE_DIVIDER.match(raw.strip()):
            if pending_header is None:
                pending_header = []
            in_table = True
            continue

        if not in_table:
            pending_header = cells
            continue

        if current_table_shape is None:
            current_table_shape = len(cells)

        row_record: list | dict
        # Filenames may sit in any column and may be backticked or bare, so
        # scan the whole row rather than a fixed cell. The first cell is the
        # human-facing need/situation label; the last is the when/phase note.
        ids = _ids_from_row(cells, task, slug_id)
        if len(cells) == 4:
            need, when = cells[0], cells[3]
            # Flat triple: [need, slug-id, when]. Field names live once in
            # the section header (``columns``) below, not per-row. The
            # spec's "drop redundant prose" lever — re-paying field names
            # 1,100 times for the same shape is exactly the kind of
            # markdown-scaffolding waste this migration removes.
            row_record = [need, ids[0] if ids else None, when]
        elif len(cells) == 3:
            row_record = [cells[0], ids]
        else:
            row_record = {"cells": cells}

        current_rows.append(row_record)

    flush_table()

    # Second pass: drop a "quick" table only when it is genuinely redundant —
    # every slug-ID it routes already appears in a non-quick section. A quick
    # table that is the primary (or only) routing surface is kept.
    def _section_ids(sec: dict) -> set[str]:
        out: set[str] = set()
        for row in sec["rows"]:
            if not isinstance(row, list):
                continue
            if len(row) == 3 and row[1]:  # [need, id, when]
                out.add(row[1])
            elif len(row) == 2 and isinstance(row[1], list):  # [situation, ids]
                out.update(row[1])
        return out

    non_quick_ids: set[str] = set()
    for sec in sections:
        if not sec.get("_quick"):
            non_quick_ids |= _section_ids(sec)

    kept: list[dict] = []
    for sec in sections:
        if sec.pop("_quick", False):
            if _section_ids(sec) - non_quick_ids:
                kept.append(sec)  # routes something no other table covers
        else:
            kept.append(sec)

    return {
        "task": task,
        "source_file": str(path.relative_to(repo_root())),
        "sections": kept,
    }


def build(corpus: str) -> list[dict]:
    """Build one task-index payload per task axis. Returns a list of
    ``{task, sections, output_path}`` records.
    """
    slug_table = load_slug_table(corpus)
    slug_id = slug_to_id(slug_table)

    distillations_root = corpus_root(corpus) / "distillations"
    if not distillations_root.is_dir():
        raise SystemExit(f"ERROR: distillations dir not found: {distillations_root}")

    payloads: list[dict] = []
    for task_dir in sorted(distillations_root.iterdir()):
        if not task_dir.is_dir():
            continue
        task = task_dir.name
        index_candidates = list(task_dir.glob("*-DISTILLATION-INDEX.md"))
        if not index_candidates:
            continue
        if len(index_candidates) > 1:
            raise SystemExit(
                f"ERROR: multiple DISTILLATION-INDEX.md files in {task_dir}"
            )
        parsed = _parse_index_file(index_candidates[0], task, slug_id)
        payload = {
            "schema_version": 1,
            "corpus": corpus,
            "task": task,
            "generated_from": "distillation-index-markdown",
            "source_file": parsed["source_file"],
            "sections": parsed["sections"],
        }
        payloads.append({"task": task, "output_dir": task_dir, "payload": payload})
    return payloads


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build per-axis task-index.json files"
    )
    parser.add_argument("--corpus", required=True)
    args = parser.parse_args(argv)

    payloads = build(args.corpus)

    if not payloads:
        print(f"no task axes found for corpus {args.corpus!r}")
        return 0

    total_bytes = 0
    for record in payloads:
        out_path = record["output_dir"] / "task-index.json"
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(record["payload"], f, indent=2, ensure_ascii=False)
        size = out_path.stat().st_size
        total_bytes += size
        rows = sum(len(s["rows"]) for s in record["payload"]["sections"])
        print(f"  {record['task']}: {rows} rows, {size:,} bytes → {out_path}")
    print(f"wrote {len(payloads)} per-axis task indexes ({total_bytes:,} bytes total)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
