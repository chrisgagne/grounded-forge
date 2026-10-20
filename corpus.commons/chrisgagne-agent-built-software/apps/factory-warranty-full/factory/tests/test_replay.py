"""Real-bug replay: a bug case brings the buggy code back on a baseline without the fix's tests; a control applies the
commit's code; scoring follows the pass mark's rules."""
import json
import subprocess

import yaml

from factory import replay


def sh(cwd, *args):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def commit(repo, msg):
    sh(repo, "git", "add", "-A")
    sh(repo, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", msg)
    return sh(repo, "git", "rev-parse", "HEAD")


def project(tmp_path):
    repo = tmp_path / "repos" / "lib"
    (repo / "src").mkdir(parents=True)
    (repo / "test").mkdir()
    sh(repo, "git", "init", "-q", "-b", "main")
    (repo / "src" / "max.js").write_text("export const max = (a, b) => (a > b ? b : a);\n")
    (repo / "test" / "old.test.js").write_text("// old test\n")
    p = commit(repo, "base")
    (repo / "src" / "max.js").write_text("export const max = (a, b) => (a > b ? a : b);\n")
    (repo / "test" / "max.test.js").write_text("// max(2, 1) === 2\n")
    (repo / "test" / "old.test.js").write_text("// old test, extended\n")
    (repo / "CHANGELOG.md").write_text("- fix: max returned the smaller value\n")
    f = commit(repo, "fix max")
    return repo, p, f


def test_a_bug_case_reverts_the_code_on_a_baseline_without_the_fix_tests(tmp_path):
    repo, p, f = project(tmp_path)
    case = {"id": "rb01", "kind": "bug", "project": "lib", "commit": f, "parent": p,
            "code_files": ["src/max.js", "CHANGELOG.md"],
            "test_files": ["test/max.test.js", "test/old.test.js"], "ground_truth": "max returns the smaller"}
    d = replay.materialise(case, tmp_path / "repos", tmp_path / "case")
    app = d / "app"
    assert "(a > b ? a : b)" in (app / "src" / "max.js").read_text()  # the baseline holds the fix
    assert not (app / "test" / "max.test.js").exists()  # the regression test the fix added is gone
    assert (app / "test" / "old.test.js").read_text() == "// old test\n"  # and an edited test is back as it was
    assert not (app / "CHANGELOG.md").exists()  # the changelog line naming the fix is gone too
    patch = (d / "change.patch").read_text()
    assert "-export const max = (a, b) => (a > b ? a : b);" in patch and "test/" not in patch and "CHANGELOG" not in patch
    assert yaml.safe_load((d / "expect.yaml").read_text())["should_block"] is True
    assert yaml.safe_load((app / ".factory" / "config.yaml").read_text())["commands"]["test"] == replay.STUB_TEST
    sh(app, "git", "init", "-q")
    sh(app, "git", "apply", "--check", str(d / "change.patch"))


def test_a_control_applies_the_commit_code_on_its_parent(tmp_path):
    repo, p, f = project(tmp_path)
    case = {"id": "rb02", "kind": "control", "project": "lib", "commit": f, "parent": p,
            "code_files": ["src/max.js"], "test_files": ["test/max.test.js"], "ground_truth": "x"}
    d = replay.materialise(case, tmp_path / "repos", tmp_path / "case")
    assert "(a > b ? b : a)" in (d / "app" / "src" / "max.js").read_text()
    assert (d / "app" / "test" / "max.test.js").read_text() == "// max(2, 1) === 2\n"  # its tests, locked first
    assert "+export const max = (a, b) => (a > b ? a : b);" in (d / "change.patch").read_text()
    assert yaml.safe_load((d / "expect.yaml").read_text())["should_block"] is False


def test_a_benchmark_pull_request_reviews_its_whole_diff_with_its_own_title_and_body(tmp_path):
    repo, p, f = project(tmp_path)
    case = {"id": "pr01", "kind": "pr", "project": "lib", "base": p, "head": f,
            "title": "Fix max", "body": "max returned the smaller value."}
    d = replay.materialise(case, tmp_path / "repos", tmp_path / "case")
    assert "(a > b ? b : a)" in (d / "app" / "src" / "max.js").read_text()  # the base tree
    patch = (d / "change.patch").read_text()
    assert "src/max.js" in patch and "test/max.test.js" in patch and "CHANGELOG.md" in patch  # the whole diff
    assert (d / "story.md").read_text() == "# Fix max\n\nmax returned the smaller value.\n"
    sh(d / "app", "git", "init", "-q")
    sh(d / "app", "git", "apply", "--check", str(d / "change.patch"))


def test_scoring_counts_only_a_blocking_finding_the_grader_matched():
    bug = {"kind": "bug"}
    rec = {"stage_blocks": {"triage": [], "gate": [], "review": ["review"]}, "blocking": ["F2"],
           "findings": [{"id": "F1", "verdict": "confirmed"}, {"id": "F2", "verdict": "confirmed"}]}
    assert replay.outcome(bug, rec, {"matches": ["F2"]})["ok"] is True
    missed = replay.outcome(bug, rec, {"matches": ["F1"]})
    assert missed["ok"] is False and missed["surfaced"] is True
    assert replay.outcome(bug, {"error": "boom"}, None)["why"] == "errored"
    control = {"kind": "control"}
    assert replay.outcome(control, rec, None)["ok"] is False
    clean = {"stage_blocks": {"triage": [], "gate": [], "review": []}}
    assert replay.outcome(control, clean, None)["ok"] is True


def test_report_measures_and_pass_mark(tmp_path):
    cases = [{"id": "rb01", "kind": "bug", "project": "lib"}, {"id": "rb02", "kind": "control", "project": "lib"}]
    cf = tmp_path / "cases.json"
    cf.write_text(json.dumps(cases))
    out = tmp_path / "out"
    (out / "trials").mkdir(parents=True)
    (out / "grades").mkdir()
    blocked = {"triage": [], "gate": [], "review": ["review"]}
    for t in (1, 2):
        (out / "trials" / f"rb01-t{t}.json").write_text(json.dumps(
            {"id": "rb01", "trial": t, "kind": "bug", "stage_blocks": blocked, "blocking": ["F1"],
             "findings": [{"id": "F1", "verdict": "confirmed"}]}))
        (out / "grades" / f"rb01-t{t}.json").write_text(json.dumps({"matches": ["F1"] if t == 1 else []}))
        (out / "trials" / f"rb02-t{t}.json").write_text(json.dumps(
            {"id": "rb02", "trial": t, "kind": "control", "stage_blocks": {"triage": [], "gate": [], "review": []}}))
    pm = tmp_path / "pm.yaml"
    pm.write_text(yaml.safe_dump({"measures": [{"measure": "bug_trials_caught", "min": 0.5, "status": "PROPOSED"}]}))
    text = replay.report(cf, out, pm).read_text()
    m = json.loads((out / "measures.json").read_text())
    assert m["bug_trials_caught"] == [1, 2] and m["bug_cases_pass_hat_k"] == [0, 1] and m["bug_cases_pass_at_k"] == [1, 1]
    assert m["control_cases_pass_hat_k"] == [1, 1]
    assert "| bug_trials_caught | >= 50% (PROPOSED) | 50% | yes |" in text
