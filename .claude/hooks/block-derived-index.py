#!/usr/bin/env python3
"""PreToolUse hook (Claude Code adapter): block hand-edits of derived JSON indexes.

The runtime JSON indexes (`task-index.json`, `concept-index.json`,
`reference-index.json`, `lens-index.json`, `slug-table.json`) are derived
artefacts written only by `scripts/build_indexes/` and `build.js` from their
staging artefacts and operator-view markdowns. A hand-edit desyncs the JSON
from its authoring source silently: the next rebuild overwrites the edit, and
until then downstream consumers read state no authoring artefact records.
CLAUDE.md states the rule ("never hand-edit them"); this hook enforces it at
the tool boundary, matched by basename so corpus-level and compiled-app copies
are both covered.

Reads JSON from stdin per the Claude Code hook spec; uses exit codes:
  0 → not a derived index, write proceeds.
  2 → derived index, write is blocked, stderr surfaces to the model with the
       regeneration path. Use exit 2 (not 1) because the model only sees
       stderr on exit 2.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

DERIVED_BASENAMES = {
    "task-index.json",
    "concept-index.json",
    "reference-index.json",
    "lens-index.json",
    "slug-table.json",
}


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    file_path = payload.get("tool_input", {}).get("file_path", "")
    name = Path(file_path).name
    if name in DERIVED_BASENAMES:
        print(
            f"Blocked: {name} is a derived artefact. Regenerate it via "
            "scripts/build_indexes/ (or node build.js); see CLAUDE.md "
            "'Retrieval pattern'.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
