"""The reproduction step: a blocking finding is shown only by a check that fails on head and passes on base, run by the
factory itself; a check that doesn't fail on head, or fails on both, shows nothing; no usable answer fails closed."""
import json

import pytest

from factory import isolation, legs, reproduce


def trees(tmp_path):
    base, head = tmp_path / "base", tmp_path / "head"
    for d, body in ((base, "a > b ? a : b"), (head, "a > b ? b : a")):
        d.mkdir()
        (d / "max.js").write_text(f"exports.max = (a, b) => ({body});\n")
    return base, head


def leg_answers(monkeypatch, answer, check_body=None):
    def fake(prompt, cwd, log, **kw):
        if check_body is not None:
            (cwd / "check" / "t.js").write_text(check_body)
        log.write_text("")
        return {"ok": True, "result": json.dumps(answer), "cost_usd": 0.01, "duration_s": 1}
    monkeypatch.setattr(legs, "run_claude", fake)


CHECK = "const {max} = require(require('path').resolve(process.argv[2], 'max.js')); process.exit(max(2, 3) === 3 ? 0 : 1);\n"
needs_sandbox = pytest.mark.skipif(not isolation.available()[0], reason="sandbox-exec unavailable")


@needs_sandbox
def test_a_check_that_fails_on_head_and_passes_on_base_shows_the_finding(tmp_path, monkeypatch):
    base, head = trees(tmp_path)
    leg_answers(monkeypatch, {"kind": "check", "command": "node check/t.js {tree}", "because": "max(2,3) is 2"}, CHECK)
    r = reproduce.reproduce({"id": "F1", "claim": "max returns the smaller"}, base, head, tmp_path / "w")
    assert r["outcome"] == "shown" and r["runs"]["head"]["exit"] == 1 and r["runs"]["base"]["exit"] == 0


@needs_sandbox
def test_a_check_that_passes_on_head_shows_nothing(tmp_path, monkeypatch):
    base, head = trees(tmp_path)
    leg_answers(monkeypatch, {"kind": "check", "command": "node check/t.js {tree}", "because": "x"},
                "process.exit(0);\n")
    assert reproduce.reproduce({"id": "F1"}, base, head, tmp_path / "w")["outcome"] == "not shown"


@needs_sandbox
def test_a_check_that_fails_on_both_trees_shows_no_change(tmp_path, monkeypatch):
    base, head = trees(tmp_path)
    leg_answers(monkeypatch, {"kind": "check", "command": "node check/t.js {tree}", "because": "x"},
                "process.exit(1);\n")
    assert reproduce.reproduce({"id": "F1"}, base, head, tmp_path / "w")["outcome"] == "not shown"


def test_argued_and_unreadable_answers_keep_the_finding_blocking(tmp_path, monkeypatch):
    base, head = trees(tmp_path)
    leg_answers(monkeypatch, {"kind": "argued", "because": "a removed auth check"})
    assert reproduce.reproduce({"id": "F1"}, base, head, tmp_path / "w1")["outcome"] == "argued"
    monkeypatch.setattr(legs, "run_claude", lambda *a, **k: {"ok": False, "result": "no json here"})
    out = reproduce.reproduce({"id": "F1"}, base, head, tmp_path / "w2")["outcome"]
    assert out == "unchecked" and out in reproduce.KEEPS_BLOCKING


def test_the_leg_cannot_change_the_trees_the_check_runs_on(tmp_path, monkeypatch):
    base, head = trees(tmp_path)
    def fake(prompt, cwd, log, **kw):
        (cwd / "head" / "max.js").write_text("exports.max = (a, b) => 3;\n")  # tampering with its copy
        return {"ok": True, "result": json.dumps({"kind": "not_shown", "because": "x"})}
    monkeypatch.setattr(legs, "run_claude", fake)
    reproduce.reproduce({"id": "F1"}, base, head, tmp_path / "w")
    assert "b ? b : a" in (head / "max.js").read_text()  # the pristine tree is untouched
