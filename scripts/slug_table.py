"""Slug-to-ID table generator and integrity check.

A slug table is a per-corpus mapping from a stable short ID (3-character
base-36, e.g. ``001``..``zzz``; capacity ~46k) to the deep-reference slug
that the ID represents. The table is the compression source for the
runtime ``concept-index.json`` and ``reference-index.json``: the index
references sources by ID, not by filename, which cuts ~35% of the index
file size on the current demo corpus.

Discipline:
  * IDs are append-only: once an ID is assigned to a slug, it stays.
  * Renames update the slug for the existing ID (not in scope yet;
    operators can hand-edit the JSON; the script just verifies integrity).
  * Deletions leave a tombstone (``"007": null``) so future ID assignment
    does not reuse the slot.
  * Alphabetical assignment on first build for determinism. Subsequent
    runs preserve existing IDs and append new ones in the order they
    appear in the corpus.

Usage:

    python3 scripts/slug_table.py generate --corpus corpus.commons/demo
    python3 scripts/slug_table.py check --corpus corpus.commons/demo

The table is written to ``{corpus}/references/slug-table.json`` so it
sits next to the deep refs it indexes.
"""

from __future__ import annotations

import argparse
import json
import string
import sys
from datetime import date
from pathlib import Path

_ALPHABET = string.digits + string.ascii_lowercase  # base-36
_ID_WIDTH = 3
_MAX_ID = len(_ALPHABET) ** _ID_WIDTH  # 36^3 = 46,656


def _to_base36(n: int) -> str:
    if n < 0:
        raise ValueError("ID must be non-negative")
    if n >= _MAX_ID:
        raise ValueError(f"ID overflow: {n} ≥ {_MAX_ID} (3-char base-36 capacity)")
    digits = []
    for _ in range(_ID_WIDTH):
        n, r = divmod(n, len(_ALPHABET))
        digits.append(_ALPHABET[r])
    return "".join(reversed(digits))


def _from_base36(s: str) -> int:
    if len(s) != _ID_WIDTH:
        raise ValueError(f"expected {_ID_WIDTH}-char ID, got {s!r}")
    n = 0
    for ch in s:
        idx = _ALPHABET.index(ch)
        n = n * len(_ALPHABET) + idx
    return n


def discover_slugs(corpus_root: Path) -> list[str]:
    """Return sorted unique slugs found as ``{slug}-deep.md`` files under
    ``{corpus_root}/references/``.
    """
    ref_dir = corpus_root / "references"
    if not ref_dir.is_dir():
        raise FileNotFoundError(f"references dir not found: {ref_dir}")
    slugs: set[str] = set()
    for path in ref_dir.glob("*-deep.md"):
        slug = path.stem[: -len("-deep")]
        if slug:
            slugs.add(slug)
    return sorted(slugs)


def _load_table(path: Path) -> dict:
    if not path.is_file():
        return {
            "schema_version": 1,
            "corpus": None,
            "generated": None,
            "next_id": 0,
            "slugs": {},
        }
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _save_table(path: Path, table: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(table, f, indent=2, ensure_ascii=False)
        f.write("\n")


def generate(corpus_root: Path) -> tuple[dict, list[str], list[str]]:
    """Read the corpus, update the slug table append-only, return
    ``(table, added, missing)`` where ``added`` is new slugs assigned an ID
    and ``missing`` is slugs in the table but no longer present in the
    references dir (kept as tombstone candidates, *not* deleted by this
    function).
    """
    table_path = corpus_root / "references" / "slug-table.json"
    table = _load_table(table_path)

    if table.get("corpus") is None:
        table["corpus"] = corpus_root.name
    elif table["corpus"] != corpus_root.name:
        raise ValueError(
            f"slug-table.json belongs to corpus {table['corpus']!r}; cannot reuse for {corpus_root.name!r}"
        )

    slugs = discover_slugs(corpus_root)
    existing_inverse = {v: k for k, v in table["slugs"].items() if v is not None}

    added: list[str] = []
    for slug in slugs:
        if slug in existing_inverse:
            continue
        new_id = _to_base36(table["next_id"])
        table["slugs"][new_id] = slug
        table["next_id"] += 1
        added.append(slug)

    table["generated"] = date.today().isoformat()
    _save_table(table_path, table)

    present = set(slugs)
    missing = sorted(s for s in existing_inverse if s not in present)
    return table, added, missing


def check(corpus_root: Path) -> list[str]:
    """Verify slug-table integrity. Returns a list of complaint strings;
    empty list means a clean table.
    """
    table_path = corpus_root / "references" / "slug-table.json"
    if not table_path.is_file():
        return [f"missing slug-table at {table_path}"]
    table = _load_table(table_path)
    complaints: list[str] = []

    if table.get("schema_version") != 1:
        complaints.append(f"unexpected schema_version: {table.get('schema_version')!r}")

    ids = sorted(table["slugs"].keys())
    seen_slugs: dict[str, str] = {}
    for id_ in ids:
        try:
            _from_base36(id_)
        except ValueError as e:
            complaints.append(f"malformed ID {id_!r}: {e}")
            continue
        slug = table["slugs"][id_]
        if slug is None:
            continue  # tombstone, fine
        if slug in seen_slugs:
            complaints.append(f"duplicate slug {slug!r} on IDs {seen_slugs[slug]} and {id_}")
        seen_slugs[slug] = id_

    expected_next = max((_from_base36(i) for i in ids), default=-1) + 1
    if table.get("next_id", 0) < expected_next:
        complaints.append(
            f"next_id={table.get('next_id')} below highest-assigned + 1 ({expected_next}): append-only invariant broken"
        )

    present = set(discover_slugs(corpus_root))
    missing = sorted(s for s in seen_slugs if s not in present)
    if missing:
        complaints.append(
            f"slug-table references {len(missing)} slug(s) not present in {corpus_root}/references/: "
            + ", ".join(missing[:5])
            + ("..." if len(missing) > 5 else "")
        )

    untracked = sorted(present - set(seen_slugs))
    if untracked:
        complaints.append(
            f"{len(untracked)} deep-ref slug(s) untracked by slug-table: "
            + ", ".join(untracked[:5])
            + ("..." if len(untracked) > 5 else "")
        )

    return complaints


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Slug-to-ID table tool")
    parser.add_argument("command", choices=["generate", "check"])
    parser.add_argument("--corpus", required=True, help="Corpus root directory")
    args = parser.parse_args(argv)

    corpus_root = Path(args.corpus).expanduser().resolve()
    if not corpus_root.is_dir():
        print(f"ERROR: corpus directory not found: {corpus_root}", file=sys.stderr)
        return 2

    if args.command == "generate":
        table, added, missing = generate(corpus_root)
        print(
            f"slug-table for {corpus_root.name}: "
            f"{len(table['slugs'])} entries, next_id={table['next_id']}"
        )
        if added:
            print(f"added {len(added)} slug(s): {', '.join(added[:5])}{'...' if len(added) > 5 else ''}")
        if missing:
            print(
                f"WARNING: {len(missing)} slug(s) in table but no longer in references/: "
                + ", ".join(missing[:5])
                + ("..." if len(missing) > 5 else "")
            )
            print("  Leave tombstones in place (set value to null) rather than deleting; IDs are append-only.")
        return 0

    complaints = check(corpus_root)
    if not complaints:
        print(f"slug-table for {corpus_root.name}: OK")
        return 0
    for c in complaints:
        print(f"  - {c}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
