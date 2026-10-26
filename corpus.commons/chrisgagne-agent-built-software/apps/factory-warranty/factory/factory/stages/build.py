"""Stage 4, build: implement the change in the worktree under the guard, then commit it.

The builder's final message is stored as builder-summary.md and only ever
shown as asserted. On a rebuild the prompt carries the open review findings
and any return reason from the accountable human.
"""
from __future__ import annotations

import json
import re

from factory.hooks.guard import read_lock
from factory.ledger import num
from factory.stages import adapter_leg, brief, builder_command, check_commands


def open_items(change) -> list[str]:
    """Blocking review findings, and a return reason recorded since the last build with the findings it names spelled
    out (a reason like "fix F1" means nothing to a builder that can't read the review)."""
    last_build = change.outcome("build")
    since = num(last_build["id"]) if last_build else 0
    out = change.outcome("review")
    path = change.dir / "review" / "findings.json"
    findings = json.loads(path.read_text()) if out and num(out["id"]) > since and path.exists() else []
    wanted = list(out.get("blocking") or []) if findings else []
    returned = change.outcome("return")
    if returned and num(returned["id"]) > since:
        wanted += [i for i in re.findall(r"\bF\d+\b", returned["reason"]) if i not in wanted]
    items = [f"{f['id']} ({f['severity']}, {f['verdict']}) {f.get('file')}:{f.get('line')}: {f['claim']}"
             + (f" Review's reason: {f['reason']}" if f.get("reason") else "")
             for i in wanted for f in findings if f["id"] == i]
    if returned and num(returned["id"]) > since:
        items.append(returned["reason"])
    return items


def run(change) -> bool:
    change.start("build")
    lock = change.dir / "tests.lock"
    if not lock.exists():
        return change.finish("build", ["no tests.lock: tests must be written and locked before the build"],
                             ["Run `factory tests` first."])
    dirty = change.dirty_files()
    if dirty:  # whatever is lying in the worktree would be committed as the build's work
        return change.finish("build", [f"the worktree has uncommitted changes before the build: {', '.join(dirty[:10])}"],
                             [f"Discard them (`git -C {change.worktree} checkout -- . && git -C {change.worktree} clean -fd`), "
                              "then re-run `factory build`."])
    cfg = change.config
    before = change.head()
    items = open_items(change)
    commands = "\n".join(f"- {k}: `{v}`" for k, v in cfg["commands"].items() if v)
    names = [n for n, cmd in cfg["commands"].items() if cmd and n != "install"]  # install needs the network
    checks = None if builder_command(change, "build") else check_commands(change, "build", before, names)
    run_rule = ("Your shell runs one thing: the factory check. It scans what you've written so far (invisible "
                "characters, secrets, and semgrep on the lines you added) and runs one of the gate's commands only if "
                "the scans pass. Run these, exactly as written, before you finish, and fix what fails:\n"
                + "\n".join(f"  - `{c}`" for c in checks) + "\n  Any other shell command is blocked. Look at files "
                "with Read, Grep and Glob; change them with Edit and Write." if checks else
                "Run the test command (and typecheck and lint, if listed) before you finish, and fix what fails.")
    prompt = brief("build.md", story=(change.dir / "story.md").read_text(),
                   acceptance=(change.dir / "acceptance.md").read_text(),
                   locked="\n".join(f"- {f}" for f in read_lock(lock)), commands=commands,
                   open_items="\n".join(f"- {i}" for i in items) or "None.", run_rule=run_rule)
    res = adapter_leg(change, "build", prompt, bash_only=checks)
    change.path("builder-summary.md").write_text(res.get("result") or "(the builder left no final message)\n")
    change.record("build", "info", check="builder-summary", note="the builder's own account: asserted, not evidence",
                  artefacts=change.hashes("builder-summary.md"))
    if not res["ok"]:
        return change.finish("build", [f"the build leg failed: {res.get('error')}"], ["Re-run `factory build`."])
    change.commit_all(f"factory: build {change.id}", "build")
    changed = change.changed_files(before)
    if not changed:
        return change.finish("build", ["the build produced no changes"], ["Re-run `factory build`."])
    change.record("build", "info", check="commit", head=change.head(), files=changed)
    return change.finish("build", [])
