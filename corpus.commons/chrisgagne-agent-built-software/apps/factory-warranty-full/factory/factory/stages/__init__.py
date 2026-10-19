"""Helpers shared by the stages: prompt filling, guard wiring, adapter legs, JSON from model output.

Stages 1, 3 and 4 (spec, tests, build) are adapters. With `builder.kind:
claude` each runs a thin `claude -p` leg. With `builder.kind: command` each
runs the configured command in the worktree; a string runs for all three
stages with FACTORY_STAGE set, a mapping names a command per stage (stages it
leaves out fall back to the claude leg). The command's stdout is the leg's
artefact (acceptance.md for spec; a summary, filed as asserted, otherwise).
Either way the deterministic checks after the leg are the same.
"""
from __future__ import annotations

import json
import re
import shlex
import shutil
import sys
from pathlib import Path
from string import Template

from factory import isolation, legs

PROMPTS = Path(__file__).resolve().parent.parent / "prompts"
GUARD = Path(__file__).resolve().parent.parent / "hooks" / "guard.py"
GUARDED_TOOLS = "Edit|Write|MultiEdit|NotebookEdit|Bash|Read|Grep|Glob"


def brief(name: str, **values) -> str:
    return Template((PROMPTS / name).read_text()).safe_substitute({k: str(v) for k, v in values.items()})


def guard_hook(change, stage: str, allow_only: list[str] | None = None, worktree: Path | None = None,
               deny_read: list[str] = (), bash_only: list[str] | None = None) -> dict:
    """The PreToolUse hook entry that runs the guard for this leg."""
    wt = worktree or change.worktree
    cmd = [sys.executable, str(GUARD), "--worktree", str(wt), "--log", str(change.path(f"{stage}/guard.jsonl"))]
    for p in change.protected():
        cmd += ["--protect", p]
    for p in isolation.secret_paths():
        cmd += ["--secret", p]
    for p in deny_read:
        cmd += ["--deny-read", p]
    if (change.dir / "tests.lock").exists():
        cmd += ["--lock", str(change.dir / "tests.lock")]
    for g in allow_only or []:
        cmd += ["--allow-only", g]
    for c in bash_only or []:
        cmd += ["--bash-only", c]
    # onFailure: a hook that crashes or times out blocks the call. Claude Code 2.1.288 accepts the key but still
    # treats a failed hook as non-blocking (checked 2026-10-11), so the guard itself exits 2 on any error.
    return {"type": "command", "command": shlex.join(cmd), "timeout": 60, "onFailure": "block"}


def leg_settings(change, stage: str, allow_only: list[str] | None = None, worktree: Path | None = None,
                 deny_read: list = (), bash_only: list[str] | None = None) -> dict:
    """Claude Code settings for a leg: the guard as a PreToolUse hook (the first line) and Claude Code's own
    sandbox (the boundary). Bash and everything it starts may write only the worktree, never git metadata, the
    change folder, the factory config, Claude settings or a locked test; no secret path is readable; the network
    is limited to `isolation.allowed_domains` (none by default)."""
    locked, _ = change.locked_paths()
    deny_read = [isolation.expand(p) for p in deny_read]
    settings = isolation.claude_sandbox(change.protected() + locked,
                                        change.config["isolation"].get("allowed_domains") or [], deny_read)
    settings["hooks"] = {"PreToolUse": [{"matcher": GUARDED_TOOLS,
                                         "hooks": [guard_hook(change, stage, allow_only, worktree, deny_read,
                                                              bash_only)]}]}
    return settings


def settings_file(change, stage: str, name: str, worktree: Path | None = None, deny_read: list = ()) -> Path:
    """Write leg_settings for a read-only leg (reviewers, sort, assessor) and return the file. `deny_read` names
    folders this leg may not read (a reviewer may not read the change folder or the other reviewer's folders)."""
    f = change.path(f"{stage}/{name}-settings.json")
    f.write_text(json.dumps(leg_settings(change, stage, worktree=worktree, deny_read=deny_read), indent=1))
    return f


def leg_files(change, stage: str, prompt: str, settings: dict, name: str = "brief.md") -> tuple[Path, Path, Path]:
    """Write the brief and settings as evidence in the change folder, and copy the brief to a private folder the
    leg may read (an `--add-dir` is writable to the leg, so it is never the change folder).
    Returns (brief evidence copy, leg-readable folder, settings file)."""
    prompt_file = change.path(f"{stage}/{name}")
    prompt_file.write_text(prompt)
    settings_file = change.path(f"{stage}/settings.json")
    settings_file.write_text(json.dumps(settings, indent=1))
    share = change.tmpdir(f"{stage}-brief-")
    shutil.copy(prompt_file, share / name)
    return prompt_file, share, settings_file


def check_commands(change, stage: str, start: str, names: list[str]) -> list[str]:
    """Write a leg's check (factory/check.py) into the change folder, which the leg can read and run but not write,
    and return the exact commands the leg may run with it, one per gate command in `names`. The scans cover what the
    leg changes from `start`, the commit its stage begins at. Python starts isolated (-I), so a `factory` folder in
    the worktree can't stand in for the check."""
    from factory.stages.gate import PINNED_RULES
    cfg = change.config
    rules = cfg["gate"]["semgrep_config"]
    spec = {"worktree": str(change.worktree), "baseline": start,
            "commands": {n: cfg["commands"][n] for n in names},
            "semgrep_configs": [c for c in (rules,) if Path(c).exists()] + [str(PINNED_RULES)]}
    path = change.path(f"{stage}/check.json")
    path.write_text(json.dumps(spec, indent=1))
    script = change.path(f"{stage}/check")
    script.write_text(f"#!/bin/sh\nexec {shlex.quote(sys.executable)} -I -m factory.check {shlex.quote(str(path))} \"$@\"\n")
    script.chmod(0o755)
    change.record(stage, "info", check="check-command", names=names,
                  artefacts=change.hashes(f"{stage}/check.json", f"{stage}/check"))
    return [f"{shlex.quote(str(script))} {n}" for n in names]


def builder_command(change, stage: str) -> str | None:
    b = change.config["builder"]
    if b.get("kind") != "command":
        return None
    cmd = b.get("command")
    return cmd.get(stage) if isinstance(cmd, dict) else cmd


def adapter_leg(change, stage: str, prompt: str, *, read_only: bool = False,
                allow_only: list[str] | None = None, bash_only: list[str] | None = None) -> dict:
    """Run stage 1, 3 or 4's leg (claude -p or the builder command), record it, return the result. `bash_only`
    limits a claude leg's shell to those commands; a builder command keeps its own shell, under sandbox-exec."""
    guard_log = change.dir / stage / "guard.jsonl"
    earlier = guard_log.exists() or any(change.rel(guard_log) in (e.get("artefacts") or {})
                                         for e in change.ledger.events())
    guard_log.unlink(missing_ok=True)
    command = builder_command(change, stage)
    settings = leg_settings(change, stage, allow_only, bash_only=None if command else bash_only)
    prompt_file, share, settings_file = leg_files(change, stage, prompt, settings)
    lc = change.config["legs"]
    try:
        res = _adapter_run(change, stage, command, settings, settings_file, prompt_file, share, read_only, lc)
    finally:
        shutil.rmtree(share, ignore_errors=True)
    change.record_leg(stage, "builder-command" if command else stage, res, prompt_file)
    if guard_log.exists() or earlier:
        # A rerun replaces the earlier leg's log, so record this one even when the guard blocked nothing: the
        # ledger's last hash for the path has to match the file on disk, or the pack reads it as tampered with.
        guard_log.touch()
        blocks = [json.loads(ln) for ln in guard_log.read_text().splitlines() if ln.strip()]
        change.record(stage, "info", check="guard", blocked_calls=len(blocks),
                      reasons=sorted({b["reason"][:160] for b in blocks}), evidence=[change.rel(guard_log)],
                      artefacts=change.hashes(change.rel(guard_log)))
    return res


def _adapter_run(change, stage, command, settings, settings_file, prompt_file, share, read_only, lc) -> dict:
    if command:
        # Any Claude session the command starts in the worktree loads local settings, so the guard applies there.
        local = change.worktree / ".claude" / "settings.local.json"
        local.parent.mkdir(exist_ok=True)
        saved = local.read_text() if local.exists() else None
        local.write_text(json.dumps(settings, indent=1))
        env = {"FACTORY_STAGE": stage, "FACTORY_STORY": str(change.dir / "story.md"),
               "FACTORY_ACCEPTANCE": str(change.dir / "acceptance.md"), "FACTORY_BRIEF": str(prompt_file),
               "FACTORY_TESTS_LOCK": str(change.dir / "tests.lock"),
               "FACTORY_TEST_COMMAND": change.config["commands"]["test"],
               "FACTORY_TEST_GLOBS": json.dumps(change.config["test_globs"])}
        try:
            # The adapter runs under sandbox-exec: the spec adapter may write nothing, the others only the worktree.
            res = legs.run_builder_command(command, change.worktree, change.path(f"{stage}/command-log.txt"),
                                           change.timeout(), env, policy=change.policy("adapter", writable=not read_only),
                                           os_sandbox=change.os_sandbox(),
                                           env_names=tuple(change.config["isolation"].get("env") or ()),
                                           tmp_root=change.worktree.parent / ".factory-tmp")
        finally:
            local.write_text(saved) if saved is not None else local.unlink(missing_ok=True)
        return res
    return legs.run_claude(
        f"Read {share / prompt_file.name} in full and do the work it describes. Your final message is the output it "
        "asks for.", change.worktree, change.path(f"{stage}/leg-log.jsonl"), model=lc["claude_model"],
        timeout_s=change.timeout(), read_only=read_only, permission_mode=lc["permission_mode"], effort=lc.get("effort"),
        settings=settings_file, add_dirs=(share,), setting_sources=lc.get("setting_sources"))


def strip_fences(text: str) -> str:
    m = re.match(r"^\s*```[\w-]*\n(.*?)\n```\s*$", text, re.S)
    return (m.group(1) if m else text).strip() + "\n"


def parse_json(text: str):
    """JSON from a model's final message: bare, fenced, or the first [..] / {..} span in it."""
    text = text.strip()
    for candidate in (text, strip_fences(text)):
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            pass
    for open_, close in (("[", "]"), ("{", "}")):
        i, j = text.find(open_), text.rfind(close)
        if 0 <= i < j:
            try:
                return json.loads(text[i:j + 1])
            except json.JSONDecodeError:
                continue
    raise ValueError("no JSON found in the leg's final message")
