"""CLI for the mechanical-index deterministic preprocessor.

Usage:

    python -m scripts.mechanical_index.preprocess \
        --source path/to/source.md \
        --discovery _planning/discovery/{slug}.json \
        --output _planning/extracted/{slug}.json

When ``--output`` is omitted the result is written to
``_planning/extracted/{slug}.json`` next to the discovery JSON's slug.

The script is deliberately self-contained: it makes no network calls, no LLM
calls, no Chroma calls. Pure regex + dict manipulation. If a discovery JSON
is malformed (the discovery scan showed schema-field type drift), the
preprocessor logs and emits the partial record rather than failing; the
semantic pass will inspect ``handler_log`` to decide whether the extraction
is trustworthy.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from .dispatch import run


def _load_lines(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as f:
        return f.readlines()


def _load_discovery(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _default_output(discovery: dict, repo_root: Path) -> Path:
    slug = discovery.get("slug") or "unknown.md"
    stem = Path(slug).stem
    return repo_root / "_planning" / "extracted" / f"{stem}.json"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Mechanical index preprocessor")
    parser.add_argument("--source", required=True, help="Path to converted markdown source")
    parser.add_argument("--discovery", required=True, help="Path to discovery JSON")
    parser.add_argument("--output", default=None, help="Output JSON path (defaults to _planning/extracted/{slug}.json)")
    parser.add_argument("--repo-root", default=None, help="Repo root (defaults to two parents up from this script)")
    parser.add_argument("--print-summary", action="store_true", help="Print a one-line summary of the extraction to stdout")
    args = parser.parse_args(argv)

    source_path = Path(args.source).expanduser()
    discovery_path = Path(args.discovery).expanduser()

    if not source_path.is_file():
        print(f"ERROR: source file not found: {source_path}", file=sys.stderr)
        return 2
    if not discovery_path.is_file():
        print(f"ERROR: discovery file not found: {discovery_path}", file=sys.stderr)
        return 2

    repo_root = Path(args.repo_root).expanduser() if args.repo_root else Path(__file__).resolve().parents[2]

    source_lines = _load_lines(source_path)
    discovery = _load_discovery(discovery_path)

    record = run(source_lines, discovery)
    record["source_path"] = str(source_path)
    record["discovery_path"] = str(discovery_path)

    output_path = Path(args.output).expanduser() if args.output else _default_output(discovery, repo_root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, ensure_ascii=False)

    if args.print_summary:
        toc_n = len(record["front_matter_toc"])
        bi_n = len(record["book_index_entries"])
        em_n = len(record["enumerated_methods"])
        tiers = ",".join(record["derived_tier"]) or "(none)"
        print(
            f"{discovery.get('slug')}: toc={toc_n} book_index={bi_n} enum_methods={em_n} tiers={tiers} → {output_path}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
