"""Assemble ``lens-index.json`` from the curated ``LENS-INDEX.md`` table.

Lenses don't go through the 9-pass; they're authored directly via the
``creating-lenses`` skill, and the curated ``LENS-INDEX.md`` table is the
single source of truth for per-lens purpose, reach-for-when, and the
native-vocabulary-and-salience signature. This builder parses that table
and emits the JSON runtime artefact.

The *Native vocabulary & salience* column has a stable three-part shape:

    Notices first: <comma-separated phrases>. Recedes: <comma-separated phrases>.
    Native: *<comma-separated italicised phrases>.*

The builder splits these into ``salience.notices_first``,
``salience.recedes``, and ``salience.native_vocabulary`` (a list of
phrases stripped of italics) so runtime retrieval can pattern-match
against the lens's signature cheaper than re-parsing the prose every time.

Inputs:
- ``corpus.commons/{corpus}/lenses/LENS-INDEX.md``: operator-curated table.
- ``corpus.commons/{corpus}/lenses/{slug}.md``: referenced for existence
  check; the per-spec content is reached for at runtime, not embedded.

Output:
- ``corpus.commons/{corpus}/lens-index.json``.

Usage:

    python -m scripts.build_indexes.build_lens_index --corpus demo

Fails loudly if a row's slug points at a file that does not exist, or if
the *Native vocabulary & salience* prose breaks the expected three-part
shape (a regression-protection gate: adding a new lens that doesn't
follow the structure should surface in the build, not at runtime).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from .common import corpus_root, index_output_dir, repo_root


def _lenses_dir(corpus: str) -> Path:
    return corpus_root(corpus) / "lenses"


def _read_index_md(corpus: str) -> str:
    path = _lenses_dir(corpus) / "LENS-INDEX.md"
    if not path.is_file():
        raise SystemExit(f"ERROR: lens index not found: {path}")
    return path.read_text(encoding="utf-8")


def _extract_table_rows(text: str) -> list[list[str]]:
    """Return the body rows of the first markdown pipe-table in the text.

    Header and separator rows are skipped. Each row is returned as a list
    of trimmed cell strings (leading/trailing pipes removed)."""
    rows: list[list[str]] = []
    in_table = False
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                break  # table ended
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        # Detect header (Kind / Slug / ...) and separator (---) rows; skip both.
        if not in_table:
            if cells and cells[0].lower() == "kind":
                in_table = True
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue  # separator
        rows.append(cells)
    return rows


SLUG_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _parse_slug_cell(cell: str) -> tuple[str, str]:
    """Return ``(slug, link_target)`` from a ``[slug](link)`` markdown cell."""
    match = SLUG_LINK_RE.match(cell)
    if not match:
        raise SystemExit(
            f"ERROR: lens slug cell does not match `[slug](link)` shape: {cell!r}"
        )
    return match.group(1), match.group(2)


SALIENCE_RE = re.compile(
    r"^Notices first:\s*(?P<notices>.+?)\.\s*"
    r"Recedes:\s*(?P<recedes>.+?)\.\s*"
    r"Native:\s*\*(?P<native>.+?)\.\*\s*$",
    re.DOTALL,
)


def _split_native_vocabulary(native_prose: str) -> list[str]:
    """Split the ``Native:`` italicised prose into a list of phrases.

    The italics block is comma-separated; each phrase is trimmed and
    de-duplicated while preserving first-seen order."""
    seen: dict[str, None] = {}
    for raw in native_prose.split(","):
        phrase = raw.strip()
        # Strip stray surrounding asterisks if the regex captured a fragment.
        phrase = phrase.strip("*").strip()
        if not phrase:
            continue
        if phrase not in seen:
            seen[phrase] = None
    return list(seen.keys())


def _parse_salience(prose: str, slug: str) -> dict:
    """Split the three-part ``Native vocabulary & salience`` cell."""
    match = SALIENCE_RE.match(prose.strip())
    if not match:
        raise SystemExit(
            f"ERROR: lens {slug!r} salience prose does not match the "
            f"`Notices first: ... Recedes: ... Native: *...*` shape. "
            f"Got:\n  {prose!r}"
        )
    return {
        "notices_first": match.group("notices").strip(),
        "recedes": match.group("recedes").strip(),
        "native_vocabulary": _split_native_vocabulary(match.group("native")),
    }


def build(corpus: str) -> dict:
    text = _read_index_md(corpus)
    rows = _extract_table_rows(text)
    if not rows:
        raise SystemExit(
            f"ERROR: no lens rows found in LENS-INDEX.md for corpus {corpus!r}"
        )

    lenses_dir = _lenses_dir(corpus)
    lenses: dict[str, dict] = {}
    kinds_seen: list[str] = []

    for row in rows:
        if len(row) < 5:
            raise SystemExit(
                f"ERROR: lens row has {len(row)} cells, expected 5: {row!r}"
            )
        kind, slug_cell, purpose, reach_for_when, salience_prose = row[:5]

        slug, link_target = _parse_slug_cell(slug_cell)
        spec_path = (lenses_dir / link_target).resolve()
        if not spec_path.is_file():
            raise SystemExit(
                f"ERROR: lens spec missing for slug {slug!r}: {spec_path}"
            )

        record = {
            "kind": kind.strip(),
            "spec_path": f"lenses/{link_target}",
            "purpose": purpose.strip(),
            "reach_for_when": reach_for_when.strip(),
            "salience": _parse_salience(salience_prose, slug),
        }
        lenses[slug] = record
        if record["kind"] not in kinds_seen:
            kinds_seen.append(record["kind"])

    return {
        "schema_version": 1,
        "corpus": corpus,
        "generated_from": "LENS-INDEX.md",
        "kinds": kinds_seen,
        "lenses": lenses,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build lens-index.json")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", default=None)
    args = parser.parse_args(argv)

    out = build(args.corpus)

    output_path = (
        Path(args.output).expanduser()
        if args.output
        else index_output_dir(args.corpus) / "lens-index.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    size = output_path.stat().st_size
    print(f"wrote {output_path} ({len(out['lenses'])} lenses, {size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
