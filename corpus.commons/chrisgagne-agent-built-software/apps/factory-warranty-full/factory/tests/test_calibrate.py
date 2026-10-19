"""calibrate end to end against throwaway fixtures (review legs off, so no model spend)."""
import shutil

import yaml
from conftest import make_app, sh

from factory import calibrate


def patch_from(app, edit) -> str:
    edit(app)
    sh(app, "git", "add", "-A")
    patch = sh(app, "git", "diff", "--cached")
    sh(app, "git", "reset", "-q", "--hard")
    return patch


def fixture(cal, name, story, patch, expect):
    d = cal / "defects" / name
    d.mkdir(parents=True)
    (d / "story.md").write_text(story)
    (d / "change.patch").write_text(patch)
    (d / "expect.yaml").write_text(yaml.safe_dump(expect))


def test_calibrate_catches_a_locked_test_edit_and_passes_the_control(tmp_path):
    app = make_app(tmp_path / "src")
    cal = tmp_path / "cal"
    shutil.copytree(app, cal / "sample-app", ignore=shutil.ignore_patterns(".git"))
    tamper = patch_from(app, lambda a: (a / "test" / "greet.test.sh").write_text("true\n"))
    control = patch_from(app, lambda a: (a / "src" / "bye.sh").write_text('echo "Bye, $1"\n'))
    fixture(cal, "01-locked-test-edit", "# Make greetings friendlier\n", tamper,
            {"should_block": True, "caught_by": ["gate:locked-tests"], "defect": "edits a locked test"})
    fixture(cal, "02-control", "# Add a goodbye script\n", control,
            {"should_block": False, "caught_by": [], "defect": "none (clean control)"})

    result = calibrate.run(cal, None, None, review_on=False)
    assert result.ok
    report = result.report.read_text()
    rows = {ln.split("|")[1].strip(): ln for ln in report.splitlines() if ln.startswith("| 0")}
    assert "gate:locked-tests" in rows["01-locked-test-edit"] and "| ok |" in rows["01-locked-test-edit"]
    assert "| passed |" in rows["02-control"] and "| ok |" in rows["02-control"]
    assert "**Catch rate (any stage):** 1/1" in report
    assert "**False positives on the control:** 0/1" in report


def test_a_miss_or_a_broken_fixture_fails_calibration_and_stays_in_the_rates(tmp_path):
    from factory import cli
    app = make_app(tmp_path / "src")
    cal = tmp_path / "cal"
    shutil.copytree(app, cal / "sample-app", ignore=shutil.ignore_patterns(".git"))
    harmless = patch_from(app, lambda a: (a / "src" / "bye.sh").write_text('echo "Bye, $1"\n'))
    fixture(cal, "01-missed", "# Add bye\n", harmless,
            {"should_block": True, "caught_by": ["gate:secrets"], "defect": "nothing a gate can see"})
    fixture(cal, "02-broken", "# Broken\n", "not a patch\n",
            {"should_block": True, "caught_by": ["gate:tests"], "defect": "patch doesn't apply"})
    result = calibrate.run(cal, None, None, review_on=False)
    report = result.report.read_text()
    assert not result.ok
    assert "**Catch rate (any stage):** 0/2" in report and "**Result:** FAIL" in report
    assert cli.main(["calibrate", "--dir", str(cal), "--no-review"]) == 1


def fake_legs(monkeypatch, reviewer_text):
    """Claude reviewer returns reviewer_text; Codex finds nothing; the sort confirms everything."""
    import json
    from test_run_e2e import leg_result
    from factory import legs
    from factory.stages import review
    seen = []

    def claude(prompt, cwd, log, **kw):
        seen.append(kw.get("json_schema"))
        if kw.get("json_schema") is review.SORT_SCHEMA:
            return leg_result(log, json.dumps({"items": [{"sources": ["C1"], "verdict": "confirmed", "reason": "r"}]}))
        return leg_result(log, reviewer_text)

    def codex(prompt, cwd, log, out, **kw):
        out.write_text("[]")
        return leg_result(log, "[]", family="codex")

    monkeypatch.setattr(legs, "run_claude", claude)
    monkeypatch.setattr(legs, "run_codex", codex)
    return seen


def review_fixtures(tmp_path):
    app = make_app(tmp_path / "src")
    cal = tmp_path / "cal"
    shutil.copytree(app, cal / "sample-app", ignore=shutil.ignore_patterns(".git"))
    bye = patch_from(app, lambda a: (a / "src" / "bye.sh").write_text('echo "Bye, $1"\n'))
    fixture(cal, "01-review-only", "# Add bye\n", bye, {"should_block": True, "caught_by": ["review"], "defect": "d"})
    fixture(cal, "02-control", "# Add bye\n", bye, {"should_block": False})
    return cal


def test_a_review_that_fails_closed_is_a_malfunction_not_a_catch(tmp_path, monkeypatch):
    cal = review_fixtures(tmp_path)
    fake_legs(monkeypatch, 'Writing up the findings now.\n\n[{"severity": "high", "claim": "c", "evidence": "e"}]')
    result = calibrate.run(cal, None, None, review_on=True)
    report = result.report.read_text()
    rows = {ln.split("|")[1].strip(): ln for ln in report.splitlines() if ln.startswith("| 0")}
    assert not result.ok and "review:malfunction" in rows["01-review-only"] and "| MISS |" in rows["01-review-only"]
    assert "**Caught by review:** 0/1 (review malfunctioned on 01-review-only, 02-control)" in report
    assert "**False positives on the control:** 1/1 (02-control)" in report


def test_a_schema_held_confirmed_finding_is_a_review_catch(tmp_path, monkeypatch):
    from factory.stages import review
    cal = review_fixtures(tmp_path)
    seen = fake_legs(monkeypatch, '{"findings": [{"severity": "high", "claim": "c", "evidence": "e"}]}')
    result = calibrate.run(cal, None, "01-review-only", review_on=True)
    report = result.report.read_text()
    assert result.ok and "**Caught by review:** 1/1" in report
    assert review.FINDINGS_SCHEMA in seen and review.SORT_SCHEMA in seen
