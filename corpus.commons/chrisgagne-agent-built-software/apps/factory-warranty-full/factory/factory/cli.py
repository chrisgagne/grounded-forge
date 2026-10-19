"""factory: run a change through the harness and hand the accountable human a warranty pack.

  factory run STORY.md --repo PATH        new change, stages 1-7, stop at the first block
  factory run --change ID --repo PATH     resume at the first stage that isn't ready
  factory new STORY.md --repo PATH        create a change without running it
  factory spec|triage|tests|build|gate|review|warrant|release --change ID
  factory spec|tests --change ID --recheck   re-check without running the leg
  factory accept --change ID --item F1|class:NAME|ratchet:NAME --reason ... --by NAME
  factory sign --change ID --by NAME      the accountable human, at a terminal
  factory return --change ID --reason ...
  factory status [--change ID]
  factory calibrate [--grounding none|seeds|distillations] [--only NN-name]
  factory replay run|grade|report --cases FILE --out DIR [--repos DIR]   real-bug replay
"""
from __future__ import annotations

import argparse
import signal
import sys
from pathlib import Path

from factory.ledger import READY_ORDER, Change, LedgerError, num
from factory.text import inert
from factory.stages import build, gate, release, review, spec, tests, triage, warrant

SEQUENCE = ["spec", "triage", "tests", "build", "triage", "gate", "review", "warrant"]
RESUME_AT = {"spec": 0, "tests": 1, "build": 3, "triage": 4, "gate": 5, "review": 6, "warrant": 7}
STAGES = {"spec": spec, "triage": triage, "tests": tests, "build": build, "gate": gate, "review": review,
          "warrant": warrant, "release": release}


# The stage each stage command follows. It must be ready (passed, or blocked with every item accepted) before the
# command runs, so order is a precondition checked before execution, not only at sign-off (OWASP LLM07:2026 #3).
# Calibration and replay call the stages directly: a measurement runs every stage on purpose.
AFTER = {"triage": "spec", "tests": "spec", "build": "tests", "gate": "triage", "review": "gate"}


def precondition(change: Change, name: str) -> str | None:
    built, specced = change.outcome("build"), change.outcome("spec")
    after_build = built and not (specced and num(specced["id"]) > num(built["id"]))
    need = "build" if name == "triage" and after_build else AFTER.get(name)
    if not need:
        return None
    ok, why = change.stage_ready(need)
    return None if ok else f"{name} runs only after {need} is ready ({why})"


def run_stage(change: Change, name: str, args) -> bool:
    problem = precondition(change, name)
    if problem:
        change.record(name, "blocked", check="order", reason=problem)
        print(f"{name}: NOT RUN: {inert(problem)}")
        return False
    if name == "spec":
        ok = spec.run(change, recheck=getattr(args, "recheck", False))
    elif name == "tests":
        ok = tests.run(change, recheck=getattr(args, "recheck", False))
    elif name == "warrant":
        ok = warrant.run(change, assessor=getattr(args, "assessor", False))
    else:
        ok = STAGES[name].run(change)
    out = change.outcome(name)
    detail = f" ({out['id']})" if out else ""
    if ok:
        print(f"{name}: pass{detail}")
    else:
        print(f"{name}: BLOCKED{detail}: {inert(out.get('reason') or '') if out else ''}")
        print(f"  see {change.dir / 'decisions-needed.md'}")
    return ok


def resume_point(change: Change) -> int:
    for stage in READY_ORDER:
        if not change.stage_ready(stage)[0]:
            return RESUME_AT[stage]
    return RESUME_AT["warrant"]


def cmd_run(args) -> int:
    repo = Path(args.repo)
    if args.change:
        change = Change(repo, args.change)
        start = RESUME_AT[args.from_stage] if args.from_stage else resume_point(change)
    else:
        if not args.story:
            sys.exit("factory run needs STORY.md, or --change ID to resume")
        change = Change.create(repo, Path(args.story))
        print(f"change {change.id}\n  folder   {change.dir}\n  worktree {change.worktree}")
        start = 0
    with change.exclusive():
        for name in SEQUENCE[start:]:
            if not run_stage(change, name, args):
                return 1
    print(f"warranty pack: {change.dir / 'warranty.md'}\n"
          f"Read it, then: factory sign --change {change.id} --by NAME   or   factory return --change {change.id} --reason ...")
    return 0


def cmd_sign(args) -> int:
    change = Change(Path(args.repo), args.change)
    _, problem = warrant.pack_state(change)
    if problem:
        print(f"cannot sign: {problem}")
        return 1
    if not sys.stdin.isatty():
        print("factory sign needs the accountable person at a terminal; it does not run headless.")
        return 2
    pack = (change.dir / "warranty.md").read_text()
    if "## Your decision" in pack:  # the page written for the signer comes first, in the terminal too
        print(pack.split("## Your decision", 1)[1].split("# The evidence", 1)[0].strip(), "\n")
    print(f"Pack, with the evidence: {change.dir / 'warranty.md'}")
    typed = input(f"You are signing as {args.by}. Type the change id ({change.id}) to sign: ").strip()
    if typed != change.id:
        print("not signed: the id didn't match")
        return 1
    with change.exclusive():
        ok, msg = warrant.sign(change, args.by)
    print(msg if ok else f"cannot sign: {msg}")
    return 0 if ok else 1


def cmd_status(args) -> int:
    repo = Path(args.repo).resolve()
    if not args.change:
        changes = sorted((repo / ".factory" / "changes").glob("*/change.json"))
        print("\n".join(p.parent.name for p in changes) or "no changes")
        return 0
    change = Change(repo, args.change)
    for stage in READY_ORDER:
        ok, why = change.stage_ready(stage)
        print(f"{stage:8} {'ready' if ok else 'not ready'}: {why}")
    for stage in ("warrant", "sign", "return", "release"):
        out = change.outcome(stage) if stage != "sign" else next(
            (e for e in reversed(change.ledger.events()) if e["stage"] == "sign"), None)
        if out:
            print(f"{stage:8} {out['status']} ({out['id']}) {out.get('reason') or out.get('by') or ''}".rstrip())
    return 0


def main(argv: list[str] | None = None) -> int:
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(143))  # so running legs are stopped too (legs._spawn)
    ap = argparse.ArgumentParser(prog="factory", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add(name: str, needs_change: bool = True, **kw):
        p = sub.add_parser(name, **kw)
        p.add_argument("--repo", default=".", help="the target repo (default: current folder)")
        if needs_change:
            p.add_argument("--change", required=True, help="change id")
        return p

    p = add("run", needs_change=False, help="run stages 1-7, stopping at the first block")
    p.add_argument("story", nargs="?")
    p.add_argument("--change", help="resume this change")
    p.add_argument("--from", dest="from_stage", choices=list(RESUME_AT), help="resume at this stage")
    p.add_argument("--assessor", action="store_true", help="add the assessor's cited summary to the pack")
    p = add("new", needs_change=False, help="create a change without running it")
    p.add_argument("story")
    for name in STAGES:
        p = add(name, help=f"run the {name} stage")
        if name == "spec":
            p.add_argument("--recheck", action="store_true", help="only re-check the existing acceptance.md")
        if name == "tests":
            p.add_argument("--recheck", action="store_true", help="no leg: re-check the tests already committed")
        if name == "warrant":
            p.add_argument("--assessor", action="store_true")
    p = add("sign", help="sign the warranty pack (the accountable human)")
    p.add_argument("--by", required=True)
    p = add("return", help="return the pack with a reason")
    p.add_argument("--reason", required=True)
    p.add_argument("--by")
    p = add("accept", help="accept a blocking finding, class or ratchet rise, with a reason")
    p.add_argument("--item", required=True)
    p.add_argument("--reason", required=True)
    p.add_argument("--by", required=True)
    p = add("status", needs_change=False, help="show where a change stands")
    p.add_argument("--change")
    p = sub.add_parser("calibrate", help="run the seeded-defect fixtures and write a report")
    p.add_argument("--grounding", choices=["none", "seeds", "distillations"])
    p.add_argument("--only", help="run one fixture, e.g. 03-locked-test-edit")
    p.add_argument("--dir", help="calibration folder (default: calibration/ in this repo)")
    p.add_argument("--no-review", action="store_true", help="skip the review legs (no model spend)")

    p = sub.add_parser("replay", help="real-bug replay: run, grade or report a cases file")
    p.add_argument("action", choices=["run", "grade", "report"])
    p.add_argument("--cases", required=True, help="cases JSON (a list, or an object with a cases list)")
    p.add_argument("--repos", help="folder holding the project clones the cases name")
    p.add_argument("--out", required=True, help="results folder")
    p.add_argument("--trials", type=int, default=3)
    p.add_argument("--jobs", type=int, default=3)
    p.add_argument("--only", help="comma-separated case ids")
    p.add_argument("--grounding", choices=["none", "seeds", "distillations"])
    p.add_argument("--pass-mark", help="pass-mark YAML to report against")
    p.add_argument("--title", default="")

    args = ap.parse_args(argv)
    try:
        return dispatch(args)
    except LedgerError as e:  # a ledger that fails its checks stops everything: fail closed, say why
        print(f"factory: the ledger failed its integrity check: {e}", file=sys.stderr)
        return 3


def dispatch(args) -> int:
    if args.cmd == "replay":
        from factory import replay
        if args.action == "run":
            replay.run(Path(args.cases), Path(args.repos), Path(args.out), args.trials, args.jobs, args.only, args.grounding)
        elif args.action == "grade":
            replay.grade(Path(args.cases), Path(args.repos), Path(args.out), args.jobs)
        else:
            print(replay.report(Path(args.cases), Path(args.out), Path(args.pass_mark) if args.pass_mark else None,
                                args.title))
        return 0
    if args.cmd == "run":
        return cmd_run(args)
    if args.cmd == "new":
        change = Change.create(Path(args.repo), Path(args.story))
        print(change.id)
        return 0
    if args.cmd in STAGES:
        with Change(Path(args.repo), args.change).exclusive() as change:
            return 0 if run_stage(change, args.cmd, args) else 1
    if args.cmd == "sign":
        return cmd_sign(args)
    if args.cmd == "return":
        with Change(Path(args.repo), args.change).exclusive() as change:
            ok, msg = warrant.return_(change, args.reason, args.by)
        print(msg)
        return 0 if ok else 1
    if args.cmd == "accept":
        with Change(Path(args.repo), args.change).exclusive() as change:
            ok, msg = warrant.accept(change, args.item, args.reason, args.by)
        print(msg)
        return 0 if ok else 1
    if args.cmd == "status":
        return cmd_status(args)
    if args.cmd == "calibrate":
        from factory import calibrate
        result = calibrate.run(Path(args.dir) if args.dir else None, args.grounding, args.only, not args.no_review)
        print(f"report: {result.report}")
        if not result.ok:
            print("calibration FAILED: a fixture errored or missed its expectation (see the report)")
        return 0 if result.ok else 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
