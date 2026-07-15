#!/usr/bin/env python3
"""PreToolUse hook (Claude Code adapter): structural validation for deep references.

Fires before a Write or Edit against any deep reference under
`corpus.commons/{any-corpus}/references/*-deep.md` or
`corpus.local/{any-corpus}/references/*-deep.md`. Performs the
deterministic, false-positive-free checks that the 9-pass protocol
requires every deep reference to satisfy. The Pass I source-only audit
runs at the model level and catches drift from the source; this hook runs
at write time and catches drift from the *protocol's structural contract*.

This file is a THIN ADAPTER. The validation logic lives in
`scripts/validate/deep_ref_core.py` (runtime-agnostic). This adapter owns
only the Claude-specific parts: parsing the PreToolUse stdin JSON, mapping
Claude's `Write`/`Edit` tool_input to a predicted post-write string, and the
exit-code-2 convention Claude uses to surface stderr to the model. A Codex or
CI adapter imports the same core with a different front end.

Why PreToolUse not PostToolUse: PostToolUse would let a malformed file land
before the check fires, leaving a broken file on disk if the next step
fails. PreToolUse predicts the post-write state from the tool input and
blocks the call entirely if validation fails, so the file on disk never
gets corrupted. This is a fast-feedback convenience, not the only guard:
the git pre-push audit and build-time validation hold the same floor for
any agent, in any runtime, that reaches this repo.

Reads JSON from stdin per the Claude Code hook spec; uses exit codes:
  0 → check passed, write proceeds.
  2 → check failed, write is blocked, stderr surfaces to the model so the
       next turn can repair the content. Use exit 2 (not 1) because the
       model only sees stderr on exit 2.

Run standalone against an existing file (delegates to the core's runner):
    python3 .claude/hooks/validate-deep-ref.py --file corpus.commons/demo/references/foo-deep.md
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Locate the runtime-agnostic core relative to this file: repo-root/scripts/validate.
_REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO_ROOT / "scripts" / "validate"))

from deep_ref_core import check_file, check_text, is_deep_ref_path  # noqa: E402


def predict_write_result(tool_name: str, tool_input: dict, file_path: Path) -> str | None:
    """Predict what the file contents will be after a Claude tool call.

    Claude-specific: understands the `Write` and `Edit` tool_input shapes.
    Returns the predicted content, or None if we can't predict (caller
    should skip validation in that case).
    """
    if tool_name == "Write":
        return tool_input.get("content", "")

    if tool_name == "Edit":
        old_string = tool_input.get("old_string", "")
        new_string = tool_input.get("new_string", "")
        replace_all = tool_input.get("replace_all", False)
        try:
            current = file_path.read_text(encoding="utf-8") if file_path.exists() else ""
        except OSError:
            return None
        if replace_all:
            return current.replace(old_string, new_string)
        # Edit semantics: must be unique. If not unique we can't reliably
        # predict; fall back to None and let the tool surface its own error.
        if current.count(old_string) != 1:
            return None
        return current.replace(old_string, new_string, 1)

    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--file",
        type=Path,
        help="check a specific file on disk (standalone mode, bypasses stdin)",
    )
    args = parser.parse_args()

    if args.file:
        if not is_deep_ref_path(args.file):
            print(f"Not a deep-ref path: {args.file}")
            return 0
        exit_code, messages = check_file(args.file)
        if exit_code != 0:
            sys.stderr.write(f"Deep-ref validation failed: {args.file}\n")
            for m in messages:
                sys.stderr.write(f"  - {m}\n")
            return exit_code
        print(f"OK: {args.file}")
        return 0

    # Hook mode: read the Claude Code PreToolUse payload from stdin.
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {})
    file_path_str = tool_input.get("file_path", "")
    if not file_path_str:
        return 0

    path = Path(file_path_str)
    if not is_deep_ref_path(path):
        return 0

    predicted = predict_write_result(tool_name, tool_input, path)
    if predicted is None:
        # Either an unsupported tool or a non-unique Edit; let the tool
        # itself handle the error rather than blocking pre-emptively.
        return 0

    violations = check_text(predicted)
    if violations:
        sys.stderr.write(
            f"Deep-ref structural validation failed for {path.name}.\n"
            "The 9-pass protocol requires every deep reference to satisfy these checks:\n"
        )
        for v in violations:
            sys.stderr.write(f"  - {v}\n")
        sys.stderr.write(
            "\nFix the content and retry, or run "
            "`python3 .claude/hooks/validate-deep-ref.py --file <path>` standalone "
            "to validate an existing file.\n"
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
