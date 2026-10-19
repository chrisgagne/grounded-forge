"""Stage 1, spec: the story becomes acceptance.md, and the driver checks its shape.

Each criterion is a heading `## AC-N: ...` followed by a `check:` line naming
the test file (and test) that will prove it. Anything else blocks.
"""
from __future__ import annotations

import json
import re

from factory.ledger import num
from factory.text import inert
from factory.stages import adapter_leg, brief, strip_fences

CRITERION = re.compile(r"^#{2,4}\s+(AC-\d+)\s*[:.\-–—]\s*(.+?)\s*$")
CHECK = re.compile(r"^\s*[-*]?\s*check:\s*(.+?)\s*$", re.I)


def check_file(check: str) -> str:
    """The test file a check line names: the part before `::`, without quotes or backticks."""
    return check.split("::")[0].strip().strip("`'\" ")


def check_name(check: str) -> str:
    """The test a check line names: the part after `::`, without quotes or backticks ('' when there is none)."""
    return check.split("::", 1)[1].strip().strip("`'\" ") if "::" in check else ""


def parse_acceptance(text: str) -> tuple[list[dict], list[str]]:
    criteria, current = [], None
    for line in text.splitlines():
        m = CRITERION.match(line)
        if m:
            current = {"id": m.group(1), "text": m.group(2), "check": None}
            criteria.append(current)
            continue
        c = CHECK.match(line)
        if c and current and current["check"] is None:
            current["check"] = c.group(1)
    problems = [] if criteria else ["no criteria found: each needs a heading like `## AC-1: ...`"]
    seen = set()
    for cr in criteria:
        if cr["id"] in seen:
            problems.append(f"{cr['id']} appears twice")
        seen.add(cr["id"])
        if not cr["check"]:
            problems.append(f"{cr['id']} has no `check:` line")
        elif not check_file(cr["check"]):
            problems.append(f"{cr['id']}'s check line names no test file")
    return criteria, problems


def send_back(change) -> dict | None:
    """The open send-back this spec run answers: a return with no tests locked since, when criteria already exist."""
    returned, tests = change.outcome("return"), change.outcome("tests")
    if not returned or not (change.dir / "acceptance.md").exists():
        return None
    if tests and num(tests["id"]) > num(returned["id"]) and tests["status"] == "pass":
        return None
    return returned


def locked_acceptance(change) -> str:
    """The criteria as they were when the tests were last locked: the base a send-back may only add to."""
    saved = change.dir / "tests" / "acceptance-locked.md"
    if saved.exists():
        return saved.read_text()
    from factory.hooks.guard import read_lock
    from factory.stages.tests import covered  # here: the tests stage imports this module
    locked = set(read_lock(change.dir / "tests.lock")) if (change.dir / "tests.lock").exists() else set()
    current = parse_acceptance((change.dir / "acceptance.md").read_text())[0]
    return "".join(f"## {c['id']}: {c['text']}\ncheck: {c['check']}\n\n" for c in current
                   if c["check"] and covered(change, c["check"], locked))


def review_findings(change) -> str:
    """The findings of the review the pack was sent back from, one line each, for a reason that refers to them."""
    path = change.dir / "review" / "findings.json"
    items = json.loads(path.read_text()) if path.exists() and change.outcome("review") else []
    return "\n".join(f"- {f['id']} ({f['severity']}, {f['verdict']}) {f.get('file')}:{f.get('line')}: {inert(f['claim'])}"
                     for f in items) or "None."


def run(change, recheck: bool = False) -> bool:
    change.start("spec")
    acceptance = change.dir / "acceptance.md"
    if not recheck:
        cfg = change.config
        returned = send_back(change)
        base = locked_acceptance(change) if returned else ""
        before = parse_acceptance(base)[0] if returned else []
        prompt = (brief("spec-amend.md", reason=returned.get("request") or returned["reason"], acceptance=base,
                        findings=review_findings(change),
                        story=(change.dir / "story.md").read_text(), worktree=change.worktree,
                        test_globs=", ".join(cfg["test_globs"]), test_command=cfg["commands"]["test"]) if returned else
                  brief("spec.md", story=(change.dir / "story.md").read_text(), worktree=change.worktree,
                        test_globs=", ".join(cfg["test_globs"]), test_command=cfg["commands"]["test"]))
        res = adapter_leg(change, "spec", prompt, read_only=True)
        if not res["ok"]:
            return change.finish("spec", [f"the spec leg failed: {res.get('error')}"],
                                 ["Re-run `factory spec`, or write acceptance.md by hand and run `factory spec --recheck`."])
        acceptance.write_text(strip_fences(res["result"]))
        if returned:  # the locked criteria stay word for word; the send-back may only add
            after = parse_acceptance(acceptance.read_text())[0]
            if after[:len(before)] != before:
                change.record("spec", "fail", check="amend", reason="the spec leg changed or removed a locked criterion")
                return change.finish("spec", ["the spec leg changed or removed a criterion whose tests are locked"],
                                     ["Re-run `factory spec`; a send-back may only add criteria."])
            from factory.hooks.guard import read_lock
            locked = set(read_lock(change.dir / "tests.lock")) if (change.dir / "tests.lock").exists() else set()
            into_locked = [c["id"] for c in after[len(before):] if c["check"] and check_file(c["check"]) in locked]
            if into_locked:
                change.record("spec", "fail", check="amend", reason=f"new criteria name locked test files: {into_locked}")
                return change.finish("spec", [f"{', '.join(into_locked)} name a locked test file, which nobody may edit, "
                                              "so no test could be added there"],
                                     ["Re-run `factory spec`; new criteria name new test files."])
            change.record("spec", "info", check="amend", answers=returned["id"],
                          added=[c["id"] for c in after[len(before):]] or None,
                          note=None if len(after) > len(before) else "the send-back asks for nothing a test could show")
        dirty = change.dirty_files()
        if dirty:  # the spec leg is read-only; anything it left behind is not the spec's to commit
            change.record("spec", "fail", check="read-only", touched=dirty, reason="the spec leg changed the worktree")
            return change.finish("spec", [f"the spec leg changed files it may only read: {', '.join(dirty)}"],
                                 ["Discard the changes in the worktree, then re-run `factory spec`."])
    if not acceptance.exists():
        return change.finish("spec", ["acceptance.md does not exist"], ["Run `factory spec` without --recheck."])
    criteria, problems = parse_acceptance(acceptance.read_text())
    change.record("spec", "fail" if problems else "pass", check="criteria", criteria=len(criteria),
                  problems=problems or None, artefacts=change.hashes("acceptance.md"),
                  reason="; ".join(problems) or None)
    return change.finish("spec", problems, [
        "Edit acceptance.md so every criterion is a `## AC-N: ...` heading followed by a `check: <test file> :: <test name>` "
        "line, then run `factory spec --recheck`; or re-run `factory spec`."])
