"""Assemble ``reference-index.json`` from Sonnet-extracted per-source records
plus mechanical fields read from the deep-ref frontmatter and slug-table.

Inputs:
- ``_planning/staging/{corpus}/refs/{slug}.json``: one per source, written by
  the Sonnet semantic-extraction sub-agents. Schema (per source):

      {
        "slug": "openstax-organizational-behavior",
        "author": "OpenStax / J. Stewart Black et al.",
        "year": 2019,
        "title": "Organizational Behavior",
        "primary_topic": "Organisational behaviour: individual differences, ...",
        "concept_tags": ["motivation", "decision-making", "leadership", ...]
      }

- ``corpus.commons/{corpus}/references/slug-table.json`` (Phase 2).
- ``corpus.commons/{corpus}/references/{slug}-deep.md`` (for Scope + line
  counts; ``{slug}.md`` for light line counts).

Output:
- ``corpus.commons/{corpus}/reference-index.json`` (Phase 3 deliverable).

Usage:

    python -m scripts.build_indexes.build_reference_index --corpus demo

The script fails loudly if the staging directory is missing entries for any
slug in the slug-table; that is the safety net that catches a dispatch
that did not complete.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .common import (
    count_lines,
    deep_ref_path,
    index_output_dir,
    light_ref_path,
    load_slug_table,
    read_scope,
    staging_dir,
)


def _load_staged_record(corpus: str, slug: str) -> dict | None:
    path = staging_dir(corpus, "refs") / f"{slug}.json"
    if not path.is_file():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build(corpus: str) -> dict:
    slug_table = load_slug_table(corpus)
    refs: dict[str, dict] = {}
    missing: list[str] = []

    for rid, slug in sorted(slug_table["slugs"].items()):
        if slug is None:
            continue  # tombstone

        staged = _load_staged_record(corpus, slug)
        if staged is None:
            missing.append(slug)
            continue

        deep_path = deep_ref_path(corpus, slug)
        light_path = light_ref_path(corpus, slug)
        scope = read_scope(deep_path)

        record = {
            "slug": slug,
            "author": staged.get("author"),
            "year": staged.get("year"),
            "title": staged.get("title"),
            "primary_topic": staged.get("primary_topic"),
            "concept_tags": staged.get("concept_tags", []),
            "lines_light": count_lines(light_path),
            "lines_deep": count_lines(deep_path),
            "scope": scope,
        }
        refs[rid] = record

    if missing:
        raise SystemExit(
            "ERROR: staging records missing for slugs:\n  - "
            + "\n  - ".join(missing)
            + f"\n\nExpected at: _planning/staging/{corpus}/refs/{{slug}}.json"
        )

    return {
        "schema_version": 1,
        "corpus": corpus,
        "generated_from": "frontmatter+slug-table",
        "refs": refs,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build reference-index.json")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--output", default=None)
    args = parser.parse_args(argv)

    out = build(args.corpus)

    output_path = (
        Path(args.output).expanduser()
        if args.output
        else index_output_dir(args.corpus) / "reference-index.json"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    size = output_path.stat().st_size
    print(f"wrote {output_path} ({len(out['refs'])} refs, {size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
