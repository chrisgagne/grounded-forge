"""Generate the Codex twins of the substrate agents.

Every ``.claude/agents/{name}.md`` at the repo root gets a Codex custom agent
at ``.codex/agents/{name}.toml``. The ``.md`` is the one source of truth: the
twin carries its name, description and body, and nothing else is authored by
hand.

``model`` and ``model_reasoning_effort`` are left out of the twin, so Codex
runs the agent on the parent session's model. The Claude form pins its model
in frontmatter; the Codex equivalent is the profile the operator runs under
(see AGENTS.md, "Codex-native surfaces").

Usage:

    python3 scripts/sync-codex-agents.py           # write the twins
    python3 scripts/sync-codex-agents.py --check   # exit 1 if any twin is missing or stale
"""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLAUDE_DIR = ROOT / ".claude" / "agents"
CODEX_DIR = ROOT / ".codex" / "agents"

PREAMBLE = (
    "Tool names below are Claude Code's (Read, Grep, Glob, Bash, Write). "
    "Use your own equivalents: read files in full, search with rg, write with "
    "your file-editing tool.\n\n"
)


def _parse(md: Path) -> tuple[dict[str, str], str]:
    text = md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SystemExit(f"{md}: no frontmatter")
    head, body = text[4:].split("\n---\n", 1)
    meta = {}
    for line in head.splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    return meta, body.lstrip("\n")


def _render(md: Path) -> str:
    meta, body = _parse(md)
    instructions = PREAMBLE + body
    if "'''" in instructions:
        raise SystemExit(f"{md}: body contains ''' and cannot become a TOML literal string")
    out = (
        f"# Codex custom agent, generated from .claude/agents/{md.name} by\n"
        "# scripts/sync-codex-agents.py. Edit the .md and re-run the script; the\n"
        "# pre-push hook fails while this file is stale.\n"
        "#\n"
        "# model and model_reasoning_effort are left out, so the agent runs on the\n"
        "# Codex session's model. Pick that model with a profile (see AGENTS.md).\n\n"
        f"name = {json.dumps(meta['name'], ensure_ascii=False)}\n\n"
        f"description = {json.dumps(meta['description'], ensure_ascii=False)}\n\n"
        'sandbox_mode = "workspace-write"\n\n'
        f"developer_instructions = '''\n{instructions}'''\n"
    )
    parsed = tomllib.loads(out)
    assert parsed["name"] == meta["name"] and parsed["developer_instructions"] == instructions
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    stale = []
    for md in sorted(CLAUDE_DIR.glob("*.md")):
        twin = CODEX_DIR / f"{md.stem}.toml"
        want = _render(md)
        have = twin.read_text(encoding="utf-8") if twin.exists() else None
        if have == want:
            continue
        stale.append(twin.relative_to(ROOT))
        if not args.check:
            CODEX_DIR.mkdir(parents=True, exist_ok=True)
            twin.write_text(want, encoding="utf-8")

    if args.check:
        for path in stale:
            print(f"stale or missing: {path} (run python3 scripts/sync-codex-agents.py)")
        return 1 if stale else 0
    for path in stale:
        print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
