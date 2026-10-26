#!/usr/bin/env python3
"""Remove every source whose slug starts with a given prefix.

Use: python3 scripts/remove-corpus.py {prefix} [--corpus demo] [--dry-run] [--yes]
Or:  npm run remove-corpus -- {prefix}

Runs scripts/remove-source.py once per matching slug in the corpus's slug
table, so each source is retired, deleted, taken off every index and its ID
retired exactly as the `removing-resources` skill does for one source. Built
for clearing the OpenStax set from the demo corpus (`npm run
remove-corpus:openstax`); forks can pass their own prefix.

The script does the mechanical half only. Surviving sources' distillations,
task specs and profiles that cited a removed source are listed in each
source's report under `_planning/removals/{corpus}/`; work through them with
the `removing-resources` skill's rewrite step before building.
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.build_indexes.common import corpus_root  # noqa: E402

_spec = importlib.util.spec_from_file_location("remove_source", REPO_ROOT / "scripts" / "remove-source.py")
remove_source = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(remove_source)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="remove-corpus.py",
        description="Remove every source whose slug starts with {prefix}-, one remove-source.py run each.",
        epilog="Example: python3 scripts/remove-corpus.py openstax --dry-run",
    )
    parser.add_argument("prefix", help="The slug prefix to remove (lowercase, hyphen-separated). E.g. 'openstax'.")
    parser.add_argument("--corpus", default="demo", help="bare corpus name (default: demo)")
    parser.add_argument("--reason", default="", help="stamped on each retired sidecar")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without touching disk.")
    parser.add_argument("--yes", action="store_true", help="Skip the confirmation prompt. Required for non-interactive use.")
    args = parser.parse_args()

    prefix = args.prefix.rstrip("-")
    if not re.match(r"^[a-z0-9][a-z0-9-]*$", prefix):
        print(f"Invalid prefix: {prefix!r}. Use lowercase, hyphen-separated.", file=sys.stderr)
        return 2
    table = json.loads((corpus_root(args.corpus) / "references" / "slug-table.json").read_text(encoding="utf-8"))
    slugs = sorted(s for s in table["slugs"].values() if s and s.startswith(f"{prefix}-"))
    print(f"{'DRY-RUN' if args.dry_run else 'REMOVING'} {len(slugs)} source(s) matching '{prefix}-' in {args.corpus}:")
    for s in slugs:
        print(f"  - {s}")
    if not slugs:
        return 0

    if not args.dry_run and not args.yes and sys.stdin.isatty():
        reply = input(f"Proceed with removing all {len(slugs)} sources? [y/N] ").strip().lower()
        if reply not in ("y", "yes"):
            print("Aborted.")
            return 1

    failed = 0
    for slug in slugs:
        print()
        failed += remove_source.Removal(args.corpus, slug, args.reason, not args.dry_run, []).run() != 0

    print()
    if args.dry_run:
        print("Dry run only. Re-run without --dry-run to apply.")
    else:
        print(f"Done. Reports: _planning/removals/{args.corpus}/. Rewrite the surviving files they list "
              "(the removing-resources skill's rewrite step), then `npm run build`.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
