"""Stage 8, release (v0 stub): refuse without a valid signature; attest it for the merge check; run the preview and
smoke commands.

A signature is valid when it is the latest sign event, its seal matches its
fields, it signed the pack as it is now (same sha256), nothing was returned
after it, no stage ran after it, and (for release) the worktree is still at the
commit and tree it signed with nothing uncommitted.

The merge into the target repo's main happens outside the harness. So release
attaches an attestation to the signed commit as a git note (`refs/notes/factory`):
the signature's sealed fields plus the pack itself. `factory verify-merge --tree
SHA` is the check a target repo's CI runs: it passes only when a valid
attestation, or a valid signature in the local ledger, names that exact tree.
There is no signing key, so an attestation is tamper-evident, not unforgeable:
someone who can push notes and knows the format can write a new one.
"""
from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

from factory.ledger import WORK_STAGES, Change, LedgerError, git, num, sha256_file
from factory.stages.warrant import SEALED, seal

NOTES_REF = "refs/notes/factory"
ATTESTATION_FORMAT = "factory-attestation/1"


def signature_problem(change, at_worktree: bool = True) -> str | None:
    """Why the change has no valid signature, or None. `at_worktree=False` skips the check that the worktree is
    still at the signed commit (the merge check, which compares trees itself)."""
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
    return change.code_problem(s, "the signature") if at_worktree else None


def latest_signature(change) -> dict:
    return [e for e in change.ledger.events() if e["stage"] == "sign"][-1]


def attestation(change) -> dict:
    """The portable record of the latest signature: its sealed fields, its seal and the pack it signed."""
    s = latest_signature(change)
    return {"format": ATTESTATION_FORMAT, **{k: s.get(k) for k in SEALED}, "seal": s["seal"], "sign_event": s["id"],
            "pack": (change.dir / "warranty.md").read_bytes().decode("utf-8")}


def attest(change) -> dict:
    """Attach the attestation to the signed commit as a git note, and record that in the ledger."""
    record = attestation(change)
    data = json.dumps(record, sort_keys=True)
    folder = change.tmpdir("attest-")
    try:
        (folder / "attestation.json").write_text(data)
        change.git("notes", "--ref", NOTES_REF, "add", "-f", "-F", str(folder / "attestation.json"), record["commit"])
    finally:
        shutil.rmtree(folder, ignore_errors=True)
    return change.record("release", "pass", check="attestation", notes_ref=NOTES_REF, commit=record["commit"],
                         tree=record["tree"], sign_event=record["sign_event"],
                         attestation_sha256=hashlib.sha256(data.encode()).hexdigest())


def attestation_problem(repo: Path, record: dict, noted_commit: str | None) -> str | None:
    """Why an attestation doesn't vouch for its tree, or None. `noted_commit` is the commit the note sits on."""
    if not isinstance(record, dict) or record.get("format") != ATTESTATION_FORMAT:
        return "not a factory attestation"
    missing = [k for k in (*SEALED, "seal", "pack") if not record.get(k)]
    if missing:
        return f"the attestation lacks {', '.join(missing)}"
    if record["seal"] != seal(record):
        return "the attestation doesn't match its own seal: its pack, commit, tree, signer or time was edited"
    if not isinstance(record["pack"], str) or \
            hashlib.sha256(record["pack"].encode("utf-8")).hexdigest() != record["pack_sha256"]:
        return "the pack in the attestation is not the pack that was signed"
    if noted_commit is not None and noted_commit != record["commit"]:
        return f"the attestation for {record['commit'][:12]} sits on another commit ({noted_commit[:12]})"
    actual = git(repo, "rev-parse", "--verify", "--quiet", f"{record['commit']}^{{tree}}", check=False)
    if actual != record["tree"]:
        return (f"commit {record['commit'][:12]} has tree {actual[:12] or '(not in this clone)'}, not the signed "
                f"tree {record['tree'][:12]}")
    return None


def noted_attestations(repo: Path) -> list[tuple[str, dict | None]]:
    """(commit, record) for every note under the factory's notes ref; record is None when the note isn't JSON."""
    out = []
    for line in git(repo, "notes", "--ref", NOTES_REF, "list", check=False).splitlines():
        blob, _, commit = line.partition(" ")
        try:
            out.append((commit, json.loads(git(repo, "cat-file", "-p", blob))))
        except (json.JSONDecodeError, RuntimeError):
            out.append((commit, None))
    return out


def local_signatures(repo: Path) -> list[tuple[dict | None, str | None]]:
    """(signature, problem) for every change in the repo's local ledger folder."""
    out = []
    for cj in sorted((Path(repo) / ".factory" / "changes").glob("*/change.json")):
        try:
            change = Change(Path(repo), cj.parent.name)
            problem = signature_problem(change, at_worktree=False)
            out.append((latest_signature(change) if problem is None else None, problem))
        except (LedgerError, RuntimeError, OSError, KeyError, ValueError) as e:
            out.append((None, f"change {cj.parent.name}: {e}"))
    return out


def find_signed(repo: Path, tree: str) -> tuple[dict | None, list[str]]:
    """The first valid attestation or local signature naming `tree`, and the problems with those that name it but
    don't count."""
    problems = []
    for commit, record in noted_attestations(repo):
        if record is None:
            problems.append(f"the note on {commit[:12]} is not JSON")
            continue
        if record.get("tree") != tree:
            continue
        problem = attestation_problem(repo, record, commit)
        if problem is None:
            return record, problems
        problems.append(problem)
    for sig, problem in local_signatures(repo):
        if sig and sig.get("tree") == tree:
            if git(repo, "rev-parse", "--verify", "--quiet", f"{sig['commit']}^{{tree}}", check=False) == tree:
                return sig, problems
            problems.append(f"signature {sig['id']} names commit {sig['commit'][:12]}, whose tree isn't {tree[:12]}")
    return None, problems


def verify_merge(repo: Path, tree: str) -> str | None:
    """None when a valid signed pack names exactly `tree`; otherwise why the merge must not land."""
    repo = Path(repo)
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", tree or ""):
        return f"--tree must be a full tree id (git rev-parse HEAD^{{tree}}), not {tree!r}"
    found, problems = find_signed(repo, tree)
    if found:
        return None
    why = f"no valid signed pack names tree {tree}"
    return why + (": " + "; ".join(problems) if problems else
                  f" (fetch the attestations first: git fetch origin '{NOTES_REF}:{NOTES_REF}')")


def run(change) -> bool:
    change.start("release")
    problem = signature_problem(change)
    if problem:
        return change.finish("release", [problem], ["The accountable human signs with `factory sign` after reading the pack."])
    ev = attest(change)
    print(f"attestation attached to {ev['commit'][:12]} under {NOTES_REF}; push it with "
          f"`git push origin {NOTES_REF}` so the target repo's merge check can find it")
    for check in ("deploy_preview", "smoke"):
        cmd = change.config["commands"].get(check)
        ev = change.run_check("release", check, cmd) if cmd else \
            change.record("release", "skipped", check=check, reason=f"commands.{check} is not configured")
        if ev["status"] == "fail":
            return change.finish("release", [f"release:{check} failed (event {ev['id']})"], ["Fix it and re-run `factory release`."])
    return change.finish("release", [])
