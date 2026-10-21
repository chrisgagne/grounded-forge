import json

from conftest import make_app, sh

from factory.ledger import Change
from factory.stages import gate, warrant
from factory.stages.gate import count_findings
from factory.stages.tests import write_lock


def lint(n: int) -> str:
    return json.dumps([{"filePath": "src/greet.sh", "messages": [{"ruleId": "r", "severity": 1}] * n}])


def test_count_findings_shapes():
    assert count_findings('{"results": [1, 2, 3], "errors": []}')[0] == 3  # semgrep
    assert count_findings(lint(2))[:2] == (2, ["src/greet.sh"])  # ESLint
    assert count_findings("[1, 2]")[0] == 2
    assert count_findings('{"count": 7}')[0] == 7
    for bad in ("not json", '{"count": -1}', '{"count": true}', '{"count": "3"}', '{"other": 1}'):
        assert count_findings(bad)[0] is None and count_findings(bad)[2], bad


def test_ratchet_rise_fails_the_gate_until_the_human_accepts_it(tmp_path):
    app = make_app(tmp_path, ratchet={"lint_warnings": {"command": "cat lint.json", "mode": "absolute"}},
                   theory_doc="docs/THEORY.md")
    (app / "lint.json").write_text(lint(1))
    (app / "docs").mkdir()
    (app / "docs" / "THEORY.md").write_text("Greetings are polite.\n")
    sh(app, "git", "add", "-A")
    sh(app, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "lint baseline")
    story = tmp_path / "story.md"
    story.write_text("# Greet\n")
    change = Change.create(app, story, change_id="r1")
    write_lock(change)
    (change.worktree / "lint.json").write_text(lint(2))
    change.commit_all("one more warning")

    assert gate.run(change) is False
    ev = [e for e in change.last_run("gate") if e["check"] == "ratchet:lint_warnings"][-1]
    assert (ev["status"], ev["before"], ev["after"]) == ("fail", 1, 2)
    assert "rose from 1 at baseline to 2" in ev["reason"]
    out = change.outcome("gate")
    assert out["blocking"] == ["ratchet:lint_warnings"] and out["acceptable"] is True
    theory = [e for e in change.last_run("gate") if e["check"] == "theory-doc"][-1]
    assert theory["exists"] is True and theory["changed"] is False

    ok, msg = warrant.accept(change, "gate:tests", "no", "Chris")
    assert not ok
    ok, msg = warrant.accept(change, "ratchet:lint_warnings", "new lint rule; cleanup is ticket 12", "Chris")
    assert ok, msg
    assert change.stage_ready("gate")[0] is True


def test_ratchet_holds_when_count_does_not_rise(tmp_path):
    app = make_app(tmp_path, ratchet={"lint_warnings": {"command": "cat lint.json", "mode": "absolute"}})
    (app / "lint.json").write_text(lint(2))
    sh(app, "git", "add", "-A")
    sh(app, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "lint baseline")
    story = tmp_path / "story.md"
    story.write_text("# Greet\n")
    change = Change.create(app, story, change_id="r2")
    write_lock(change)
    (change.worktree / "lint.json").write_text(lint(1))
    change.commit_all("one fewer warning")
    assert gate.run(change) is True
    ev = [e for e in change.last_run("gate") if e["check"] == "ratchet:lint_warnings"][-1]
    assert (ev["status"], ev["before"], ev["after"]) == ("pass", 2, 1)
