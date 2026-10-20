"""factory calibrate: run the seeded-defect fixtures and report what each stage caught.

For each fixture in `calibration/defects/{NN-name}/` (story.md, change.patch,
expect.yaml), against a fresh copy of `calibration/sample-app/`:

  1. copy the app to a temp folder, git init, commit the baseline, create the
     change, run install, lock the baseline's test files (stages 1 and 3 are
     simulated: story.md is the story, the baseline's tests are the locked
     acceptance tests)
  2. apply change.patch and commit it (stage 4 simulated)
  3. run triage, gate and review for real, then warrant
  4. record the first stage that blocked, every check that blocked, and
     compare with expect.yaml

Every stage runs even after an earlier one blocks, so the report shows each
stage's catches and the review A/B (--grounding none, seeds or distillations)
covers every fixture. Work folders are kept under a temp root named in the report.
"""
from __future__ import annotations

import datetime as dt
import shutil
import tempfile
from pathlib import Path

import yaml

from factory.ledger import Change, git
from factory.stages import gate, review, tests, triage, warrant

CALIBRATION = Path(__file__).resolve().parent.parent / "calibration"
CHECKED = ("triage", "gate", "review")


def simulate(change: Change, patch: Path) -> None:
    """Stages 1, 3 and 4 as calibration defines them."""
    change.start("spec")
    change.path("acceptance.md").write_text(  # no file names here: triage reads this text for keywords
        "# Acceptance (calibration)\n\nstory.md is the spec. The baseline's tests are the locked acceptance tests; "
        "tests.lock lists them.\n")
    change.record("spec", "skipped", check="outcome", reason="calibration: simulated; story.md is the spec",
                  artefacts=change.hashes("acceptance.md"))
    triage.run(change)
    change.start("tests")
    install = change.config["commands"].get("install")
    if install and change.run_check("tests", "install", install)["status"] == "fail":
        raise RuntimeError("install failed on the baseline")
    tests.write_lock(change)
    change.record("tests", "skipped", check="outcome",
                  reason="calibration: simulated; the baseline's tests are the locked acceptance tests")
    change.start("build")
    change.git("apply", "--whitespace=nowarn", str(patch))
    change.path("builder-summary.md").write_text("Calibration: change.patch was applied in place of a build leg.\n")
    change.record("build", "info", check="builder-summary", artefacts=change.hashes("builder-summary.md"))
    change.commit_all(f"calibration: apply {patch.parent.name}/change.patch")
    change.record("build", "skipped", check="outcome", reason="calibration: simulated by applying change.patch",
                  head=change.head(), files=change.changed_files())


def catchers(change: Change, stage: str) -> list[str]:
    out = change.outcome(stage)
    if not out or out["status"] != "blocked":
        return []
    if stage == "gate":
        return [f"gate:{e['check']}" for e in change.last_run("gate") if e["status"] == "fail"]
    if stage == "review" and not any(e.get("check") == "sorted" for e in change.last_run("review")):
        # Blocked before findings were sorted: a leg failed or returned an invalid list. The review failed closed,
        # which protects the operator but detected nothing, so it isn't a catch (and on the control it's a false alarm).
        return ["review:malfunction"]
    return [stage]


def run_fixture(fx: Path, sample: Path, work: Path, grounding: str | None, review_on: bool) -> dict:
    expect = yaml.safe_load((fx / "expect.yaml").read_text()) or {}
    row = {"fixture": fx.name, "expect": expect, "work": str(work)}
    app = work / "app"
    shutil.copytree(sample, app, ignore=shutil.ignore_patterns("node_modules", ".git"))
    git(app, "init", "-q", "-b", "main")
    # The baseline is committed byte for byte: the project's own .gitignore and line-ending attributes would otherwise
    # drop tracked files or rewrite them, and the change's diff would no longer apply.
    (app / ".git" / "info").mkdir(parents=True, exist_ok=True)
    (app / ".git" / "info" / "attributes").write_text("* -text\n")
    git(app, "add", "-A", "-f")
    if (app / ".factory").exists():  # a project whose .gitignore is an allowlist would leave the config out
        git(app, "add", "-f", ".factory")
    git(app, "commit", "-q", "-m", "calibration baseline")
    overrides = {"worktree_root": str(work / "worktrees")}
    if grounding:
        overrides["review"] = {"grounding": grounding}
    try:
        change = Change.create(app, fx / "story.md", change_id=fx.name, overrides=overrides)
        row["grounding"] = change.config["review"]["grounding"]
        simulate(change, fx / "change.patch")
        triage.run(change)
        gate.run(change)
        if review_on:
            review.run(change)
        warrant.run(change)
    except (Exception, SystemExit) as e:  # a broken fixture is reported, not hidden
        row["error"] = f"{type(e).__name__}: {e}"
        return row
    found = {s: catchers(change, s) for s in CHECKED}
    every = [c for s in CHECKED for c in found[s]]
    row.update(first=next((s for s in CHECKED if found[s]), "passed"), blocks=every,
               review_caught=found["review"] == ["review"], change_dir=str(change.dir))
    legs_run = [e for e in change.last_run("review") if e.get("check", "").startswith("leg:")]
    row["cost_usd"] = round(sum(e.get("cost_usd") or 0 for e in legs_run), 4)
    row["codex_tokens"] = sum(e.get("tokens") or 0 for e in legs_run)
    if expect.get("should_block", True):
        row["ok"] = any(c in (expect.get("caught_by") or []) for c in every)
        # With review off, a fixture only review is expected to catch can't be judged: reported, not failed.
        row["na"] = not review_on and set(expect.get("caught_by") or []) <= {"review"} and not row["ok"]
    else:
        row["ok"] = not every
    return row


class Result:
    """The report path, and whether every fixture ran and met its expectation."""

    def __init__(self, report: Path, rows: list[dict]):
        self.report, self.rows = report, rows
        self.ok = all("error" not in r and (r.get("ok") or r.get("na")) for r in rows)

    def __fspath__(self) -> str:
        return str(self.report)


def write_report(cal_dir: Path, rows: list[dict], root: Path, review_on: bool) -> Path:
    mode = next((r["grounding"] for r in rows if r.get("grounding")), "config")
    # Errored fixtures stay in the denominators: a fixture that didn't run caught nothing.
    defects = [r for r in rows if r["expect"].get("should_block", True)]
    controls = [r for r in rows if not r["expect"].get("should_block", True)]
    lines = [f"# Calibration report {dt.date.today().isoformat()}", "",
             f"Grounding: **{mode}** · review legs: {'on' if review_on else 'off'} · fixtures: {len(rows)} · "
             f"work folders: `{root}`", "",
             "| Fixture | Defect | Expected | First block | All blocks | Result | Review cost |",
             "|---|---|---|---|---|---|---|"]
    for r in rows:
        exp = r["expect"]
        expected = ", ".join(exp.get("caught_by") or []) if exp.get("should_block", True) else "pass (control)"
        if "error" in r:
            lines.append(f"| {r['fixture']} | {exp.get('defect', '')} | {expected} | error | {r['error']} | ERROR | - |")
            continue
        cost = f"${r['cost_usd']:.2f} + {r['codex_tokens']} Codex tokens" if review_on else "-"
        verdict = "ok" if r["ok"] else "n/a (review off)" if r.get("na") else "MISS"
        lines.append(f"| {r['fixture']} | {exp.get('defect', '')} | {expected} | {r['first']} | "
                     f"{', '.join(r['blocks']) or '-'} | {verdict} | {cost} |")
    caught = [r for r in defects if r.get("blocks")]
    fp = [r["fixture"] for r in controls if r.get("blocks") or "error" in r]
    lines += ["",
              f"- **Catch rate (any stage):** {len(caught)}/{len(defects)} seeded defects",
              f"- **Caught by an expected check:** {sum(bool(r.get('ok')) for r in defects)}/{len(defects)}",
              f"- **Caught by review:** {sum(bool(r.get('review_caught')) for r in defects)}/{len(defects)}"
              + (f" (review malfunctioned on {', '.join(m)})" if (m := [r['fixture'] for r in rows
                                                                       if 'review:malfunction' in r.get('blocks', [])])
                 else ""),
              f"- **False positives on the control:** {len(fp)}/{len(controls)}" + (f" ({', '.join(fp)})" if fp else "")
              + (" (a control that errored counts as a false positive)" if any("error" in r for r in controls) else ""),
              f"- **Review cost:** ${sum(r.get('cost_usd', 0) for r in rows):.2f} Claude, "
              f"{sum(r.get('codex_tokens', 0) for r in rows)} Codex tokens",
              f"- **Fixture errors:** {sum('error' in r for r in rows)} (counted as misses)",
              f"- **Result:** {'PASS' if all('error' not in r and (r.get('ok') or r.get('na')) for r in rows) else 'FAIL'} "
              "(every fixture ran and met its expectation"
              + (f"; {sum(bool(r.get('na')) for r in rows)} review-only fixtures not judged with review off)"
                 if any(r.get("na") for r in rows) else ")"), "",
              "Stages 1, 3 and 4 are simulated (spec, tests and build are recorded as skipped), so a control that "
              "passes here shows the gates and review raise no false alarm; it doesn't show a signable pack.", ""]
    report = cal_dir / f"report-{dt.date.today().isoformat()}-{mode}.md"
    report.write_text("\n".join(lines))
    return report


def run(cal_dir: Path | None, grounding: str | None, only: str | None, review_on: bool = True) -> Result:
    cal_dir = Path(cal_dir or CALIBRATION).resolve()
    sample = cal_dir / "sample-app"
    fixtures = sorted(p for p in (cal_dir / "defects").iterdir() if p.is_dir()) if (cal_dir / "defects").exists() else []
    if only:
        fixtures = [f for f in fixtures if f.name == only]
    if not sample.exists() or not fixtures:
        raise SystemExit(f"nothing to calibrate: need {sample} and fixtures in {cal_dir / 'defects'}")
    root = Path(tempfile.mkdtemp(prefix="factory-calibrate-"))
    rows = []
    for fx in fixtures:
        print(f"{fx.name} ...", flush=True)
        rows.append(run_fixture(fx, sample, root / fx.name, grounding, review_on))
        r = rows[-1]
        print(f"  {r.get('error') or ('ok' if r['ok'] else 'n/a (review off)' if r.get('na') else 'MISS') + ': first block ' + r['first']}",
              flush=True)
    return Result(write_report(cal_dir, rows, root, review_on), rows)
