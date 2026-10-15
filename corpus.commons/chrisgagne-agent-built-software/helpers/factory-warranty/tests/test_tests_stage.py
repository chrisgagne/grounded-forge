"""Stage 3: red must be a completed run that mentions the tests, every check names a real test, and existing
tests are kept."""
import pytest
from conftest import make_app

from factory import legs
from factory.ledger import Change
from factory.stages import tests

AC = "## AC-1: bye says goodbye by name\ncheck: test/bye.test.sh :: says bye\n"


def leg(writes):
    def fake(prompt, cwd, log, **kw):
        for rel, text in writes.items():
            (cwd / rel).write_text(text)
        log.write_text("")
        return {"ok": True, "exit": 0, "family": "claude", "cmd": "claude", "started": "t", "finished": "t",
                "duration_s": 0, "log_path": log, "result": "wrote tests", "output_sha256": "0" * 64}
    return fake


def ready(tmp_path, monkeypatch, writes, acceptance=AC, **cfg) -> Change:
    app = make_app(tmp_path, **cfg)
    story = tmp_path / "s.md"
    story.write_text("# Add a goodbye script\n")
    change = Change.create(app, story, change_id="t1")
    (change.dir / "acceptance.md").write_text(acceptance)
    monkeypatch.setattr(legs, "run_claude", leg(writes))
    return change


GOOD = '# says bye\n[ "$(sh src/bye.sh Ann)" = "Bye, Ann" ]\n'


def test_a_good_red_run_locks(tmp_path, monkeypatch):
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": GOOD})
    assert tests.run(change) is True, change.outcome("tests")["reason"]


def test_a_timeout_is_not_red(tmp_path, monkeypatch):
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": "# says bye\nsleep 30\n"},
                   gate={"timeout_minutes": 0.05})
    assert tests.run(change) is False
    assert "didn't complete" in change.outcome("tests")["reason"]
    assert not (change.dir / "tests.lock").exists()


def test_a_check_line_naming_a_test_that_isnt_there_blocks(tmp_path, monkeypatch):
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": '[ "$(sh src/bye.sh Ann)" = "Bye, Ann" ]\n'})
    assert tests.run(change) is False
    assert "no test named 'says bye'" in change.outcome("tests")["reason"]


def test_a_test_name_with_an_escaped_quote_counts(tmp_path, monkeypatch):
    acceptance = "## AC-1: bye works\ncheck: test/bye.test.sh :: says bye to Ann's dog\n"
    source = "# says bye to Ann\\'s dog\n" + GOOD.split("\n", 1)[1]
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": source}, acceptance=acceptance)
    assert tests.run(change) is True, change.outcome("tests")["reason"]


def test_recheck_locks_the_committed_tests_without_a_leg(tmp_path, monkeypatch):
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": GOOD},
                   acceptance="## AC-1: bye works\ncheck: test/bye.test.sh :: says goodbye\n")
    assert tests.run(change) is False and "no test named" in change.outcome("tests")["reason"]
    (change.dir / "acceptance.md").write_text(AC)

    def no_leg(*a, **kw):
        raise AssertionError("recheck ran a leg")

    monkeypatch.setattr(legs, "run_claude", no_leg)
    assert tests.run(change, recheck=True) is True, change.outcome("tests")["reason"]
    assert (change.dir / "tests.lock").exists()


def test_recheck_refuses_code_committed_since_the_baseline(tmp_path, monkeypatch):
    change = ready(tmp_path, monkeypatch, {})
    (change.worktree / "test" / "bye.test.sh").write_text(GOOD)
    (change.worktree / "src" / "bye.sh").write_text('echo "Bye, $1"\n')
    change.commit_all("tests and code together")
    assert tests.run(change, recheck=True) is False
    assert "not tests: src/bye.sh" in change.outcome("tests")["reason"]


def test_red_output_must_mention_each_criterions_test(tmp_path, monkeypatch):
    acceptance = "## AC-1: bye works\ncheck: test/bye.spec.sh :: says bye\n"  # a file the runner never runs
    change = ready(tmp_path, monkeypatch, {"test/bye.spec.sh": GOOD, "test/other.test.sh": "false\n"},
                   acceptance=acceptance)
    assert tests.run(change) is False
    assert "never mentions" in change.outcome("tests")["reason"]


@pytest.mark.parametrize("edit", ["true\n", None])
def test_the_tests_leg_may_not_change_or_delete_existing_tests(tmp_path, monkeypatch, edit):
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": GOOD})
    original = leg({"test/bye.test.sh": GOOD})

    def weaken(prompt, cwd, log, **kw):
        res = original(prompt, cwd, log, **kw)
        if edit is None:
            (cwd / "test" / "greet.test.sh").unlink()
        else:
            (cwd / "test" / "greet.test.sh").write_text(edit)
        return res

    monkeypatch.setattr(legs, "run_claude", weaken)
    head = change.head()
    assert tests.run(change) is False
    assert "existing tests" in change.outcome("tests")["reason"] and change.head() == head


def test_adding_a_test_to_an_existing_file_is_fine(tmp_path, monkeypatch):
    acceptance = "## AC-1: bye works\ncheck: test/greet.test.sh :: says bye\n"
    change = ready(tmp_path, monkeypatch, {}, acceptance=acceptance)
    greet = change.worktree / "test" / "greet.test.sh"
    monkeypatch.setattr(legs, "run_claude", leg({"test/greet.test.sh": greet.read_text() + "# says bye\n"
                                                 '[ "$(sh src/bye.sh Ann)" = "Bye, Ann" ]\n'}))
    assert tests.run(change) is True, change.outcome("tests")["reason"]


def test_the_claude_tests_leg_may_run_only_the_check(tmp_path, monkeypatch):
    import json
    import shlex
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": GOOD})
    seen = {}
    inner = legs.run_claude

    def spy(prompt, cwd, log, *, settings=None, add_dirs=(), **kw):
        seen["hook"] = json.loads(settings.read_text())["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
        seen["brief"] = (add_dirs[0] / "brief.md").read_text()
        return inner(prompt, cwd, log, **kw)

    monkeypatch.setattr(legs, "run_claude", spy)
    start = change.head()
    assert tests.run(change) is True, change.outcome("tests")["reason"]
    words = shlex.split(seen["hook"])
    allowed = [words[i + 1] for i, w in enumerate(words) if w == "--bash-only"]
    assert len(allowed) == 1 and shlex.split(allowed[0]) == [str(change.dir / "tests" / "check"), "test"]
    assert allowed[0] in seen["brief"]
    assert json.loads((change.dir / "tests" / "check.json").read_text())["baseline"] == start


def test_the_driver_scans_the_new_tests_before_it_runs_them(tmp_path, monkeypatch):
    change = ready(tmp_path, monkeypatch, {"test/bye.test.sh": "# says bye\n# ‮\n" + GOOD})
    assert tests.run(change) is False
    assert "fails a scan" in change.outcome("tests")["reason"]
    assert not [e for e in change.ledger.events() if e.get("check") == "new-tests"]  # never run
