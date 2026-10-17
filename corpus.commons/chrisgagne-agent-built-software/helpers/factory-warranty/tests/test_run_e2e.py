"""`factory run` end to end with faked legs: the stage glue, the block, the human's acceptance, sign, release."""
import json

import pytest
from conftest import make_app

from factory import cli, legs
from factory.ledger import Change
from factory.stages import warrant

FINDING = {"severity": "high", "file": "src/bye.sh", "line": 1, "claim": "the name is echoed unquoted",
           "evidence": "src/bye.sh:1 is `echo \"Bye, $1\"`"}


def leg_result(log, result, family="claude"):
    log.write_text("")
    return {"ok": True, "exit": 0, "family": family, "cmd": f"{family} <prompt>", "started": "t", "finished": "t",
            "duration_s": 0.1, "cost_usd": 0.01 if family == "claude" else None, "tokens": 10 if family == "codex" else None,
            "model": "fake", "log_path": log, "result": result, "output_sha256": "0" * 64}


def fake_claude(prompt, cwd, log, **kw):
    stage, name = log.parent.name, log.name
    if stage == "spec":
        return leg_result(log, "## AC-1: bye says goodbye by name\ncheck: test/bye.test.sh :: says bye\n")
    if stage == "tests":
        (cwd / "test" / "bye.test.sh").write_text('# says bye\n[ "$(sh src/bye.sh Ann)" = "Bye, Ann" ]\n')
        return leg_result(log, "AC-1: test/bye.test.sh")
    if stage == "build":
        (cwd / "src" / "bye.sh").write_text('echo "Bye, $1"\n')
        return leg_result(log, "Done. All tests pass.")
    if name == "claude-log.jsonl":
        return leg_result(log, json.dumps([FINDING]))
    if name == "sort-log.jsonl":
        return leg_result(log, json.dumps([{"sources": ["C1", "X1"], "verdict": "confirmed", "severity": "high",
                                            "reason": "src/bye.sh:1 echoes $1 as given"}]))
    raise AssertionError(f"unexpected leg {log}")


def fake_codex(prompt, cwd, log, out, **kw):
    out.write_text(json.dumps([{**FINDING, "severity": "medium"}]))
    return leg_result(log, out.read_text(), family="codex")


@pytest.fixture
def faked(monkeypatch):
    monkeypatch.setattr(legs, "run_claude", fake_claude)
    monkeypatch.setattr(legs, "run_codex", fake_codex)


def test_run_blocks_on_a_confirmed_finding_then_signs_after_acceptance(tmp_path, faked, capsys):
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n\n`src/bye.sh NAME` prints Bye, NAME.\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 1
    change_id = capsys.readouterr().out.split("change ", 1)[1].split()[0]
    change = Change(app, change_id)
    assert change.outcome("review")["blocking"] == ["F1"]
    assert "F1 confirmed high" in (change.dir / "decisions-needed.md").read_text()
    assert (change.dir / "tests.lock").read_text().count("test/bye.test.sh") == 1
    red = [e for e in change.ledger.events() if e.get("check") == "new-tests"][-1]
    assert red["status"] == "fail"  # the new test was red before the build

    assert cli.main(["accept", "--repo", str(app), "--change", change_id, "--item", "F1",
                     "--reason", "names come from our own CLI; tracked as ticket 7", "--by", "Chris"]) == 0
    assert cli.main(["run", "--repo", str(app), "--change", change_id]) == 0
    pack = (change.dir / "warranty.md").read_text()
    assert "READY TO SIGN" in pack and "accepted by Chris" in pack
    assert "Done. All tests pass." in pack.split("## Asserted, not evidence")[1].split("## Gates")[0]

    assert cli.main(["release", "--repo", str(app), "--change", change_id]) == 1  # not signed yet
    ok, msg = warrant.sign(change, "Chris")
    assert ok, msg
    assert cli.main(["release", "--repo", str(app), "--change", change_id]) == 0


def test_builder_command_adapter(tmp_path, faked):
    app = make_app(tmp_path, builder={"kind": "command", "command": {
        "tests": "printf '# says bye\\n[ \"$(sh src/bye.sh Ann)\" = \"Bye, Ann\" ]\\n' > test/bye.test.sh && echo \"wrote tests for $FACTORY_STAGE\"",
        "build": "printf 'echo \"Bye, $1\"\\n' > src/bye.sh && echo built"}})
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n")
    change = Change.create(app, story, change_id="cmd1")
    for stage in ("spec", "triage", "tests", "build", "triage", "gate"):
        assert cli.run_stage(change, stage, None), stage
    legs_run = {e["leg"]: e for e in change.ledger.events() if e.get("check", "").startswith("leg:")}
    assert legs_run["builder-command"]["family"] == "command"
    assert (change.dir / "tests-summary.md").read_text().strip() == "wrote tests for tests"
    assert (change.dir / "builder-summary.md").read_text().strip() == "built"
    assert not (change.worktree / ".claude" / "settings.local.json").exists()


def test_no_findings_skips_the_sort_and_the_pack_still_assembles(tmp_path, monkeypatch):
    def quiet_claude(prompt, cwd, log, **kw):
        return leg_result(log, "[]") if log.name == "claude-log.jsonl" else fake_claude(prompt, cwd, log, **kw)

    def quiet_codex(prompt, cwd, log, out, **kw):
        out.write_text("[]")
        return leg_result(log, "[]", family="codex")

    monkeypatch.setattr(legs, "run_claude", quiet_claude)
    monkeypatch.setattr(legs, "run_codex", quiet_codex)
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 0
    change = Change(app, sorted((app / ".factory" / "changes").iterdir())[0].name)
    pack = (change.dir / "warranty.md").read_text()
    assert "sort: skipped (neither reviewer reported a finding)" in pack and "READY TO SIGN" in pack


def test_a_send_back_goes_through_spec_and_tests_before_the_rebuild(tmp_path, monkeypatch):
    """The human sends a ready pack back asking for more. Spec adds a criterion (the old one stays word for word),
    tests writes and locks a red test for it alone, then the build makes it pass: the builder adds no tests of its own."""
    calls = []

    def claude(prompt, cwd, log, **kw):
        stage = log.parent.name
        calls.append(stage)
        brief = next(iter(kw.get("add_dirs") or ()), None)
        text = (brief / "brief.md").read_text() if brief and (brief / "brief.md").exists() else ""
        if stage == "spec" and "sent it back" in text:
            assert "and say goodnight" in text and "review's findings" in text
            return leg_result(log, "## AC-1: bye says goodbye by name\ncheck: test/bye.test.sh :: says bye\n\n"
                                   "## AC-2: bye says goodnight too\ncheck: test/night.test.sh :: says goodnight\n")
        if stage == "tests" and "Write tests only for AC-2" in text:
            (cwd / "test" / "night.test.sh").write_text('# says goodnight\n[ "$(sh src/night.sh)" = "Goodnight" ]\n')
            return leg_result(log, "AC-2: test/night.test.sh")
        if stage == "build" and "goodnight" in text:
            (cwd / "src" / "night.sh").write_text('echo "Goodnight"\n')
            return leg_result(log, "Done.")
        if stage == "build":  # the first build tries something the guard stops; the rebuild doesn't
            (log.parent / "guard.jsonl").write_text(json.dumps({"reason": "outside the worktree"}) + "\n")
        if log.name == "claude-log.jsonl":
            return leg_result(log, "[]")
        return fake_claude(prompt, cwd, log, **kw)

    def codex(prompt, cwd, log, out, **kw):
        out.write_text("[]")
        return leg_result(log, "[]", family="codex")

    monkeypatch.setattr(legs, "run_claude", claude)
    monkeypatch.setattr(legs, "run_codex", codex)
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 0
    change = Change(app, sorted((app / ".factory" / "changes").iterdir())[0].name)
    ok, _ = warrant.return_(change, "and say goodnight", "Chris")
    assert ok and change.stage_ready("spec")[0] is False
    assert cli.main(["build", "--repo", str(app), "--change", change.id]) == 1  # not before spec and tests
    calls.clear()
    assert cli.main(["run", "--repo", str(app), "--change", change.id]) == 0
    assert [c for c in calls if c in ("spec", "tests", "build")] == ["spec", "tests", "build"]
    events = change.ledger.events()
    amend = [e for e in events if e.get("check") == "amend"][-1]
    assert amend["added"] == ["AC-2"]
    assert "test/night.test.sh" in (change.dir / "tests.lock").read_text()
    red = [e for e in events if e.get("check") == "new-tests"][-1]
    assert red["status"] == "fail"  # the new test failed before the rebuild
    added = [e for e in events if e.get("check") == "added-tests"][-1]
    assert added["status"] == "pass"
    guards = [e for e in events if e["stage"] == "build" and e.get("check") == "guard"]
    assert [g["blocked_calls"] for g in guards] == [1, 0]  # the rebuild's empty log replaces the first build's
    pack = (change.dir / "warranty.md").read_text()
    assert "READY TO SIGN" in pack and "AC-2: bye says goodnight too" in pack


def test_a_send_back_that_changes_a_locked_criterion_blocks(tmp_path, monkeypatch):
    def claude(prompt, cwd, log, **kw):
        brief = next(iter(kw.get("add_dirs") or ()), None)
        text = (brief / "brief.md").read_text() if brief and (brief / "brief.md").exists() else ""
        if log.parent.name == "spec" and "sent it back" in text:
            return leg_result(log, "## AC-1: bye says goodbye politely\ncheck: test/bye.test.sh :: says bye\n")
        return leg_result(log, "[]") if log.name == "claude-log.jsonl" else fake_claude(prompt, cwd, log, **kw)

    monkeypatch.setattr(legs, "run_claude", claude)
    monkeypatch.setattr(legs, "run_codex", lambda prompt, cwd, log, out, **kw: (out.write_text("[]"),
                                                                                leg_result(log, "[]", "codex"))[1])
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 0
    change = Change(app, sorted((app / ".factory" / "changes").iterdir())[0].name)
    warrant.return_(change, "be more polite", "Chris")
    assert cli.main(["run", "--repo", str(app), "--change", change.id]) == 1
    assert "changed or removed a criterion whose tests are locked" in change.outcome("spec")["reason"]


def ready_change(tmp_path, monkeypatch, spec_reply, tests_writes=True):
    """A change run to READY with faked legs, then sent back; the amend's spec reply and whether the tests leg writes."""
    def claude(prompt, cwd, log, **kw):
        brief = next(iter(kw.get("add_dirs") or ()), None)
        text = (brief / "brief.md").read_text() if brief and (brief / "brief.md").exists() else ""
        if log.parent.name == "spec" and "sent it back" in text:
            return leg_result(log, spec_reply)
        if log.parent.name == "tests" and "Write tests only for" in text:
            if tests_writes:
                (cwd / "test" / "night.test.sh").write_text('# says goodnight\n[ "$(sh src/night.sh)" = "Goodnight" ]\n')
            return leg_result(log, "done")
        return leg_result(log, "[]") if log.name == "claude-log.jsonl" else fake_claude(prompt, cwd, log, **kw)

    monkeypatch.setattr(legs, "run_claude", claude)
    monkeypatch.setattr(legs, "run_codex", lambda prompt, cwd, log, out, **kw: (out.write_text("[]"),
                                                                                leg_result(log, "[]", "codex"))[1])
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 0
    change = Change(app, sorted((app / ".factory" / "changes").iterdir())[0].name)
    warrant.return_(change, "and say goodnight", "Chris")
    return app, change


OLD = "## AC-1: bye says goodbye by name\ncheck: test/bye.test.sh :: says bye\n\n"


def test_a_new_criterion_may_not_name_a_locked_test_file(tmp_path, monkeypatch):
    app, change = ready_change(tmp_path, monkeypatch, OLD + "## AC-2: says goodnight\ncheck: test/bye.test.sh :: says goodnight\n")
    assert cli.main(["run", "--repo", str(app), "--change", change.id]) == 1
    assert "name a locked test file" in change.outcome("spec")["reason"]


def test_a_send_back_stays_open_until_its_tests_are_locked(tmp_path, monkeypatch):
    app, change = ready_change(tmp_path, monkeypatch, OLD + "## AC-2: says goodnight\ncheck: test/night.test.sh :: says goodnight\n",
                               tests_writes=False)
    assert cli.main(["run", "--repo", str(app), "--change", change.id]) == 1
    assert "wrote no test files" in change.outcome("tests")["reason"]
    assert cli.main(["spec", "--repo", str(app), "--change", change.id]) == 0  # amends again, from the locked base
    amends = [e for e in change.ledger.events() if e.get("check") == "amend"]
    assert len(amends) == 2 and amends[-1]["added"] == ["AC-2"]
    assert (change.dir / "tests" / "acceptance-locked.md").exists()


def run_with_codex_timeouts(tmp_path, monkeypatch, capsys, timeouts):
    """A run whose Codex reviewer runs out of time on its first `timeouts` attempts."""
    calls = {"n": 0}

    def codex(prompt, cwd, log, out, **kw):
        calls["n"] += 1
        if calls["n"] <= timeouts:
            log.write_text("exec\n... still reading ...\n")
            return {"ok": False, "exit": None, "timed_out": True, "error": "killed after 60 min", "family": "codex",
                    "cmd": "codex <prompt>", "started": "t", "finished": "t", "duration_s": 3600, "log_path": log,
                    "result": "", "output_sha256": "0" * 64, "tokens": None, "model": "fake", "cost_usd": None}
        return fake_codex(prompt, cwd, log, out, **kw)

    monkeypatch.setattr(legs, "run_claude", fake_claude)
    monkeypatch.setattr(legs, "run_codex", codex)
    app = make_app(tmp_path)
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n\n`src/bye.sh NAME` prints Bye, NAME.\n")
    cli.main(["run", str(story), "--repo", str(app)])
    change = Change(app, capsys.readouterr().out.split("change ", 1)[1].split()[0])
    return change, calls["n"]


def test_a_reviewer_that_runs_out_of_time_is_retried_once(tmp_path, monkeypatch, capsys):
    change, attempts = run_with_codex_timeouts(tmp_path, monkeypatch, capsys, timeouts=1)
    assert attempts == 2
    timed = [e for e in change.ledger.events() if e.get("check") == "timed-out:codex"]
    assert len(timed) == 1 and timed[0]["retried"] and timed[0]["evidence"] == ["review/codex-timed-out-1.log"]
    assert change.outcome("review")["blocking"] == ["F1"]  # the retry's findings count as usual


def test_a_reviewer_out_of_time_twice_stops_the_change_and_says_so(tmp_path, monkeypatch, capsys):
    change, attempts = run_with_codex_timeouts(tmp_path, monkeypatch, capsys, timeouts=2)
    assert attempts == 2
    out = change.outcome("review")
    assert out["status"] == "blocked"
    assert "the codex reviewer ran out of time (2 attempts of 60 min) and named no finding" in out["reason"]
