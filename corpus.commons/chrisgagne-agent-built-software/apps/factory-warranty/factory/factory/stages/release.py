"""Stage 8, release (v0 stub): refuse without a valid signature; run the preview and smoke commands.

A signature is valid when it is the latest sign event, its seal matches its
fields, it signed the pack as it is now (same sha256), the worktree is still at
the commit and tree it signed with nothing uncommitted, nothing was returned
after it, and no stage ran after it.
"""
from __future__ import annotations

from factory.ledger import WORK_STAGES, num, sha256_file
from factory.stages.warrant import seal


def signature_problem(change) -> str | None:
    events = change.ledger.events()  # checks the chain and the anchor
    signs = [e for e in events if e["stage"] == "sign"]
    if not signs:
        return "the warranty pack is not signed"
    s = signs[-1]
    if s.get("seal") != seal(s):
        return f"the signature {s['id']} doesn't match its own seal: its pack, commit, signer or time was edited"
    w = next((e for e in events if e["id"] == s.get("warrant_event")), None)
    if not w or w.get("pack_sha256") != s["pack_sha256"] or (w.get("commit"), w.get("tree")) != (s["commit"], s["tree"]):
        return f"the signature {s['id']} doesn't match the pack it names ({s.get('warrant_event')})"
    pack = change.dir / "warranty.md"
    if not pack.exists() or sha256_file(pack) != s["pack_sha256"]:
        return f"warranty.md changed after it was signed in {s['id']}"
    later = [e for e in events if num(e["id"]) > num(s["id"]) and (e["stage"] in WORK_STAGES + ("return", "warrant"))]
    if later:
        return f"{later[0]['stage']} ran after the signature ({later[0]['id']}); the pack must be re-warranted and re-signed"
    return change.code_problem(s, "the signature")


def run(change) -> bool:
    change.start("release")
    problem = signature_problem(change)
    if problem:
        return change.finish("release", [problem], ["The accountable human signs with `factory sign` after reading the pack."])
    for check in ("deploy_preview", "smoke"):
        cmd = change.config["commands"].get(check)
        ev = change.run_check("release", check, cmd) if cmd else \
            change.record("release", "skipped", check=check, reason=f"commands.{check} is not configured")
        if ev["status"] == "fail":
            return change.finish("release", [f"release:{check} failed (event {ev['id']})"], ["Fix it and re-run `factory release`."])
    return change.finish("release", [])
