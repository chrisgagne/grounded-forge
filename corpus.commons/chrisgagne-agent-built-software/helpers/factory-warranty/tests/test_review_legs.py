"""Reviewer legs beyond the factory's own brief: Claude Code with a plain prompt (`claude-plain`) and OpenAI's own
`codex review` (`codex-review`). Their output is read into the factory's finding shape, `codex review` sees exactly
the change (a repository whose `base` is the baseline), and sorted items keep every reviewer's own finding."""
import json
import subprocess

from conftest import make_app

from factory import cli, legs
from factory.ledger import Change
from factory.stages import review

CODEX_OUT = """The change prints the name unquoted.

Review comment:

- [P1] Quote the name before echoing it — {root}/src/bye.sh:1-1
  `echo "Bye, $1"` passes the argument through unchanged, so a name with
  shell metacharacters is printed as given.
- [P3] Add a usage line — {root}/src/bye.sh:1-1
  Running it with no name prints "Bye, ".
"""


def test_codex_review_comments_become_findings(tmp_path):
    found = review.codex_review_findings(CODEX_OUT.format(root=tmp_path), tmp_path)
    assert [f["severity"] for f in found] == ["high", "low"]
    assert found[0]["file"] == "src/bye.sh" and found[0]["line"] == 1
    assert found[0]["claim"] == "Quote the name before echoing it"
    assert "shell metacharacters" in found[0]["evidence"]


def test_a_plain_review_keeps_every_readable_item():
    text = ('Here they are.\n[{"file":"a.js","start_line":3,"end_line":4,"severity":"high","message":"x breaks"},\n'
            '{"file":"b.js","start_line":1,"severity":low","message":"broken item"},\n'
            '{"file":"c.js","start_line":"7","severity":"odd","message":"y is slow"}]')
    found, unreadable = review.plain_findings(text)
    assert [(f["file"], f["line"], f["severity"]) for f in found] == [("a.js", 3, "high"), ("c.js", 7, "medium")]
    assert found[0]["claim"] == found[0]["evidence"] == "x breaks"
    assert unreadable == 1


def leg_result(log, result, family="claude"):
    log.write_text("")
    return {"ok": True, "exit": 0, "family": family, "cmd": f"{family} <prompt>", "started": "t", "finished": "t",
            "duration_s": 0.1, "cost_usd": 0.01 if family == "claude" else None, "tokens": 10 if family == "codex" else None,
            "model": "fake", "log_path": log, "result": result, "output_sha256": "0" * 64}


FINDING = {"severity": "high", "file": "src/bye.sh", "line": 1, "claim": "the name is echoed unquoted",
           "evidence": "src/bye.sh:1 is `echo \"Bye, $1\"`"}


def test_three_legs_run_blind_and_the_sort_keeps_each_reviewers_finding(tmp_path, monkeypatch, capsys):
    seen = {}

    def claude(prompt, cwd, log, **kw):
        stage, name = log.parent.name, log.name
        if stage == "spec":
            return leg_result(log, "## AC-1: bye says goodbye by name\ncheck: test/bye.test.sh :: says bye\n")
        if stage == "tests":
            (cwd / "test" / "bye.test.sh").write_text('# says bye\n[ "$(sh src/bye.sh Ann)" = "Bye, Ann" ]\n')
            return leg_result(log, "AC-1: test/bye.test.sh")
        if stage == "build":
            (cwd / "src" / "bye.sh").write_text('echo "Bye, $1"\n')
            return leg_result(log, "Done.")
        if name == "claude-log.jsonl":
            return leg_result(log, json.dumps([FINDING]))
        if name == "claude-plain-log.jsonl":
            seen["plain_prompt"] = prompt
            return leg_result(log, json.dumps([{"file": "src/bye.sh", "start_line": 1, "end_line": 1,
                                                "severity": "medium", "message": "No usage message"}]))
        if name == "sort-log.jsonl":
            seen["sort_packet"] = sorted(p.name for p in kw["add_dirs"][0].iterdir())
            return leg_result(log, json.dumps([
                {"sources": ["C1", "R1"], "verdict": "confirmed", "severity": "high", "reason": "src/bye.sh:1 echoes $1"},
                {"sources": ["P1", "R2"], "verdict": "disputed", "severity": "low", "reason": "a usage line is optional"}]))
        raise AssertionError(f"unexpected leg {log}")

    def codex_review(repo, log, *, base, **kw):
        seen["branches"] = subprocess.run(["git", "branch", "--format=%(refname:short)"], cwd=repo,
                                          capture_output=True, text=True).stdout.split()
        seen["diff"] = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], cwd=repo,
                                      capture_output=True, text=True).stdout.split()
        out = CODEX_OUT.format(root=repo)
        log.write_text(out)
        return {**leg_result(log, out, family="codex"), "result": out}

    monkeypatch.setattr(legs, "run_claude", claude)
    monkeypatch.setattr(legs, "run_codex_review", codex_review)
    app = make_app(tmp_path, review={"grounding": "none", "legs": ["claude", "claude-plain", "codex-review"]})
    story = tmp_path / "story.md"
    story.write_text("# Add a goodbye script\n\n`src/bye.sh NAME` prints Bye, NAME.\n")
    assert cli.main(["run", str(story), "--repo", str(app)]) == 1
    change = Change(app, capsys.readouterr().out.split("change ", 1)[1].split()[0])
    assert "base" in seen["branches"] and "src/bye.sh" in seen["diff"]  # codex review sees the change itself
    assert not any(p.startswith(".factory") for p in seen["diff"])
    assert "Add a goodbye script" in seen["plain_prompt"] and "diff.patch" in seen["plain_prompt"]
    assert {"findings-claude.json", "findings-claude-plain.json", "findings-codex-review.json"} <= set(seen["sort_packet"])
    items = json.loads((change.dir / "review" / "findings.json").read_text())
    assert [m["id"] for m in items[0]["members"]] == ["C1", "R1"] and items[0]["members"][1]["leg"] == "codex-review"
    assert change.outcome("review")["blocking"] == ["F1"]
