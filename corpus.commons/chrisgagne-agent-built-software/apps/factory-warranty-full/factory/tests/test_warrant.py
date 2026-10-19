import json

from factory.stages import gate, triage, warrant
from factory.stages.tests import write_lock


def passing_run(change):
    """Ledger events for a change that passed every stage, with real command runs."""
    change.start("spec")
    (change.dir / "acceptance.md").write_text("## AC-1: greets by name\ncheck: test/greet.test.sh :: greets\n")
    change.finish("spec", [])
    change.start("tests")
    change.run_check("tests", "baseline-tests", "sh test/run.sh")
    write_lock(change)
    change.finish("tests", [])
    change.start("build")
    (change.dir / "builder-summary.md").write_text("Done. All tests pass and it is production ready.\n")
    change.record("build", "info", check="builder-summary", artefacts=change.hashes("builder-summary.md"))
    (change.worktree / "src" / "greet.sh").write_text('echo "Hello, $1"  # polite\n')
    change.commit_all("build")
    change.finish("build", [])
    triage.run(change)
    change.start("gate")
    change.run_check("gate", "tests", "sh test/run.sh")
    gate.locked_tests(change)
    change.record("gate", "skipped", check="perf", reason="commands.perf is not configured")
    change.finish("gate", [])
    change.start("review")
    (change.dir / "review").mkdir(exist_ok=True)
    (change.dir / "review" / "findings.json").write_text(json.dumps([]))
    change.finish("review", [])


def section(pack: str, title: str) -> str:
    return pack.split(f"## {title}", 1)[1].split("\n## ", 1)[0]


def test_pack_separates_demonstrated_from_asserted(change):
    passing_run(change)
    assert warrant.run(change) is True
    pack = (change.dir / "warranty.md").read_text()
    assert "READY TO SIGN" in pack
    demonstrated = section(pack, "Demonstrated")
    assert "`sh test/run.sh` exit 0" in demonstrated and "output sha256" in demonstrated
    assert "locked-test hash check: **pass**" in demonstrated
    assert "production ready" not in demonstrated
    assert "production ready" in section(pack, "Asserted, not evidence")
    assert "gate:perf skipped" in section(pack, "Residual risks")
    assert "Accountable person:" in section(pack, "Sign-off")


def test_confirmed_findings_below_the_bar_are_residual_risks(change):
    passing_run(change)
    found = [{"id": "F1", "severity": "medium", "verdict": "confirmed", "file": "src/greet.sh", "line": 1,
              "claim": "a stale id can delete a newer record", "reason": "ids are reused", "sources": ["C1"]},
             {"id": "F2", "severity": "low", "verdict": "noise", "file": "src/greet.sh", "line": 1,
              "claim": "style", "reason": "not a defect", "sources": ["X1"]}]
    (change.dir / "review" / "findings.json").write_text(json.dumps(found))
    assert warrant.run(change) is True
    residual = section((change.dir / "warranty.md").read_text(), "Residual risks")
    assert "F1 confirmed (medium)" in residual and "F2" not in residual


def test_a_return_that_names_a_finding_hands_the_builder_its_claim(change):
    from factory.stages import build
    passing_run(change)
    found = [{"id": "F1", "severity": "medium", "verdict": "confirmed", "file": "src/greet.sh", "line": 1,
              "claim": "a stale id can delete a newer record", "reason": "ids are reused", "sources": ["C1"]}]
    (change.dir / "review" / "findings.json").write_text(json.dumps(found))
    warrant.run(change)
    warrant.return_(change, "fix F1", "Chris")
    items = build.open_items(change)
    assert any("F1 (medium, confirmed) src/greet.sh:1: a stale id can delete a newer record" in i
               and "ids are reused" in i for i in items)
    assert any("fix F1" in i for i in items)


def test_assessor_lines_must_cite_real_events():
    kept, dropped = warrant.filter_cited(
        "- The suite passed after the build [e012].\n- It is safe to ship.\n- Scans ran clean [e099].\n"
        "- Mixed cites [e012] [e100].\n\n", {"e012"})
    assert kept == ["- The suite passed after the build [e012]."]
    assert len(dropped) == 3


def test_sign_needs_an_unchanged_pack(change):
    passing_run(change)
    warrant.run(change)
    pack = change.dir / "warranty.md"
    pack.write_text(pack.read_text().replace("NOT READY", "READY") + "\nextra line\n")
    ok, msg = warrant.sign(change, "Chris")
    assert not ok and "changed since it was assembled" in msg
    warrant.run(change)
    ok, msg = warrant.sign(change, "Chris")
    assert ok, msg
    sig = [e for e in change.ledger.events() if e["stage"] == "sign"][-1]
    assert sig["by"] == "Chris" and sig["pack_sha256"] == change.outcome("warrant")["pack_sha256"]


def test_sign_refuses_a_pack_that_is_not_ready_or_stale(change):
    passing_run(change)
    change.record("gate", "blocked", check="outcome", reason="gate:tests failed")
    warrant.run(change)
    ok, msg = warrant.sign(change, "Chris")
    assert not ok and "not ready" in msg
    change.record("gate", "pass", check="outcome")
    ok, msg = warrant.sign(change, "Chris")
    assert not ok and "after the pack was assembled" in msg


def test_pack_not_ready_when_an_artefact_changed_after_recording(change):
    passing_run(change)
    (change.dir / "builder-summary.md").write_text("edited later\n")
    assert warrant.run(change) is False
    assert "builder-summary.md no longer matches" in (change.dir / "warranty.md").read_text()


def test_pack_not_ready_when_a_command_log_changed_after_recording(change):
    passing_run(change)
    log = change.dir / "gate" / "tests.log"
    assert log.exists()
    log.write_text("all green, trust me\n")
    assert warrant.run(change) is False
    assert "gate/tests.log no longer matches" in (change.dir / "warranty.md").read_text()


def test_the_assessor_summary_is_filed_as_asserted(change, monkeypatch):
    from factory import legs
    passing_run(change)

    def assessor(prompt, cwd, log, **kw):
        log.write_text("")
        return {"ok": True, "exit": 0, "family": "claude", "cmd": "claude", "started": "t", "finished": "t",
                "duration_s": 0, "log_path": log, "result": "- Rollback was rehearsed and all scans passed [e001].",
                "output_sha256": "0" * 64}

    monkeypatch.setattr(legs, "run_claude", assessor)
    warrant.run(change, assessor=True)
    pack = (change.dir / "warranty.md").read_text()
    summary = section(pack, "Assessor's summary (asserted, not evidence)")
    assert "[e001]" in summary and "did not check that those events support" in summary


def test_the_pack_opens_with_a_decision_page_in_plain_words(change):
    passing_run(change)
    assert warrant.run(change) is True
    pack = (change.dir / "warranty.md").read_text()
    page = pack.split("## Your decision", 1)[1].split("# The evidence", 1)[0]
    assert pack.index("## Your decision") < pack.index("## Story")
    assert "> # " not in page and "Greetings should say Hello." in page  # what was asked, from the story
    assert "AC-1: greets by name" in page and "written by an AI" in page
    assert "All the project's tests pass, the new ones included: yes" in page
    assert "The tests written before the build weren't changed afterwards: yes" in page
    assert "no such command: perf" in page
    assert "Does this need someone else?" in page and "No: nothing in it reaches personal data" in page
    assert "Undo: revert this change" in page and "PROPOSED" in page
    assert f"factory sign --change {change.id}" in page and f"factory return --change {change.id}" in page


def test_the_decision_page_names_a_second_person_for_personal_data(change):
    passing_run(change)
    risk = json.loads((change.dir / "risk.json").read_text())
    risk["classes"]["personal-data"] = {"evidence": [{"rule": "path", "source": "diff", "match": "src/users/x.js"}],
                                        "strength": "path or pattern", "required_gates": [], "review_focus": "x"}
    (change.dir / "risk.json").write_text(json.dumps(risk))
    page = "\n".join(warrant.decision_page(change, risk["classes"], change.last_run("gate"), change.last_run("tests"),
                                           [], [], []))
    assert "penetration test" in page and "No: nothing in it reaches" not in page


def test_a_finding_that_blocks_is_the_decision_not_a_leftover(change):
    passing_run(change)
    finding = {"id": "F1", "severity": "medium", "raw_severity": "high", "verdict": "confirmed", "file": "a", "line": 1,
               "claim": "flags fixed strings", "reason": "r", "evidence": "e", "breaks": "AC-1"}
    (change.dir / "review" / "findings.json").write_text(json.dumps([finding]))
    change.start("review")
    change.finish("review", ["F1"], blocking=["F1"], acceptable=True)
    warrant.run(change)
    page = (change.dir / "warranty.md").read_text().split("# The evidence")[0]
    sub = lambda title: page.split(f"### {title}", 1)[1].split("\n### ", 1)[0]
    decide = sub("What you must decide first")
    assert "F1" in decide and "rated it serious" in decide and "flags fixed strings" in decide
    assert 'misses AC-1: "greets by name"' in decide
    assert "flags fixed strings" not in sub("What's left over")
    assert "a reviewer rated 1 point(s) serious: F1" in page
    assert "--item F1" in sub("Your choices") and "factory sign" not in sub("Your choices")


def test_a_moderate_stop_says_why_the_bar_dropped(change):
    passing_run(change)
    risk = json.loads((change.dir / "risk.json").read_text())
    risk["classes"]["irreversible"] = {"evidence": [{"rule": "keyword", "source": "story/acceptance", "match": "drop"}],
                                       "strength": "keyword only", "required_gates": [], "review_focus": "x"}
    (change.dir / "risk.json").write_text(json.dumps(risk))
    finding = {"id": "F2", "severity": "low", "raw_severity": "medium", "verdict": "confirmed", "file": "a", "line": 1,
               "claim": "a contrived false block", "reason": "r", "evidence": "e"}
    (change.dir / "review" / "findings.json").write_text(json.dumps([finding]))
    change.start("review")
    change.finish("review", ["F2"], blocking=["F2"], acceptable=True)
    page = "\n".join(warrant.decision_page(change, risk["classes"], change.last_run("gate"), change.last_run("tests"),
                                           [finding], [], [], ["F2"]))
    decide = page.split("### What you must decide first", 1)[1].split("\n### ", 1)[0]
    assert "F2 stopped the change at moderate" in decide
    assert 'a step that can\'t be undone, because the story or its behaviours mention "drop"' in decide
    assert "If the change doesn't do that, accept the point" in decide
