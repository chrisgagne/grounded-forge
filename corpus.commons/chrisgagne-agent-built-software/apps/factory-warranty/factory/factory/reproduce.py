"""Make a blocking finding show its work (PREREG-reproduce.md).

A Claude leg gets the finding and two copies of the project, `base/` (before the change) and `head/` (after), with no
network, and either writes a check in `check/` with the command that runs it, or says the finding can't be shown by
running code. The factory then runs that command itself, sandboxed and without network, on fresh copies of both
trees, and decides:

- shown: the check fails on head and passes on base (or fails on head where the leg says base can't run it);
- not shown: the check doesn't fail on head, or fails on both trees, or the leg found the problem doesn't happen;
- argued: the leg says the finding can't be shown by running code;
- unchecked: the leg gave no usable answer or the check couldn't run. Fails closed: the finding keeps blocking.

Shown, argued and unchecked findings keep blocking; a not-shown finding stops blocking.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from string import Template

from factory import isolation, legs

PROMPT = Path(__file__).parent / "prompts" / "reproducer.md"
KEEPS_BLOCKING = ("shown", "argued", "unchecked")
CHECK_TIMEOUT_S = 300


def describe(finding: dict) -> str:
    keys = ("severity", "file", "line", "claim", "evidence", "reason")
    return "\n".join(f"- **{k}:** {finding[k]}" for k in keys if finding.get(k))


def fresh(src: Path, dest: Path) -> None:
    """A copy of a pristine tree (an APFS clone where the filesystem allows it, so node_modules costs nothing)."""
    if dest.exists():
        shutil.rmtree(dest)
    r = subprocess.run(["cp", "-cR", str(src), str(dest)], capture_output=True)
    if r.returncode != 0:
        shutil.copytree(src, dest, symlinks=True)


def parse(text: str) -> dict | None:
    try:
        obj = json.loads(text[text.index("{"):text.rindex("}") + 1])
    except ValueError:
        return None
    return obj if isinstance(obj, dict) and obj.get("kind") in ("check", "not_shown", "argued") else None


def reproduce(finding: dict, base: Path, head: Path, work: Path, *, model: str = "opus",
              timeout_s: int = 1800) -> dict:
    """Run the step for one finding. `base` and `head` are pristine trees (dependencies installed) that are never
    touched; the leg and the checks work on copies under `work`."""
    work.mkdir(parents=True, exist_ok=True)
    for name, src in (("base", base), ("head", head)):
        fresh(src, work / name)
    (work / "check").mkdir(exist_ok=True)
    prompt = Template(PROMPT.read_text()).safe_substitute(finding=describe(finding))
    settings = work.parent / f"{work.name}-settings.json"
    settings.write_text(json.dumps(isolation.claude_sandbox([], [], []), indent=1))
    log = work.parent / f"{work.name}-leg.jsonl"
    res = legs.run_claude(prompt, work, log, model=model, timeout_s=timeout_s, settings=settings)
    answer = parse(res.get("result") or "")
    rec = {"finding": finding.get("id"), "leg": {k: res.get(k) for k in ("ok", "error", "cost_usd", "duration_s")},
           "answer": answer}
    if not answer:
        return {**rec, "outcome": "unchecked", "why": "the leg gave no usable answer"}
    if answer["kind"] == "argued":
        return {**rec, "outcome": "argued", "why": answer.get("because")}
    if answer["kind"] == "not_shown":
        return {**rec, "outcome": "not shown", "why": answer.get("because")}
    command = str(answer.get("command") or "")
    if "{tree}" not in command:
        return {**rec, "outcome": "unchecked", "why": "the check's command names no {tree}"}
    runs = {}
    for name, src in (("base", base), ("head", head)):
        fresh(src, work / name)  # the leg may have changed its copies while exploring
        policy = isolation.Policy(writable=[str(work.resolve())], network=False, label=f"reproduce-{name}")
        runs[name] = legs.run_command(command.replace("{tree}", name), work, work.parent / f"{work.name}-{name}.log",
                                      CHECK_TIMEOUT_S, policy=policy)
    rec["runs"] = {n: {k: r.get(k) for k in ("exit", "error", "sandbox", "output_tail")} for n, r in runs.items()}
    head_exit, base_exit = runs["head"].get("exit"), runs["base"].get("exit")
    if head_exit is None or (base_exit is None and not answer.get("base_cannot_run")):
        return {**rec, "outcome": "unchecked", "why": "the check couldn't run in the sandbox"}
    if head_exit == 0:
        return {**rec, "outcome": "not shown", "why": "the check passes on head"}
    if base_exit == 0:
        return {**rec, "outcome": "shown", "why": answer.get("because")}
    if answer.get("base_cannot_run"):
        return {**rec, "outcome": "shown", "head_only": True, "why": answer.get("because")}
    return {**rec, "outcome": "not shown", "why": "the check fails on base too, so it shows no change"}
