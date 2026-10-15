"""factory replay: run real-bug cases (reverted fixes and clean controls from open-source history) through triage,
gate, review and warrant, k independent trials each, and grade the catches with a model of the other family.

A case (one entry of a cases file, chosen by someone other than the operator) names a project clone, a commit and its
parent, the commit's code files and test files, and a ground truth:

  bug      from a fix commit F: the baseline is F's tree with the fix's test-file changes undone; the change is the
           reverse of F's code-file changes, so the buggy code comes back
  control  from a non-fix commit C: the baseline is C's parent plus C's own test changes (the factory writes and locks
           tests before the build); the change is C's code-file changes

A bug case's fix tests never reach the factory, so it can't give itself away; a control's tests are already in place,
as they would be in the factory, so a correct change doesn't look like it breaks them. Each project's own suite is not run
(old commits need old toolchains, and the bug cases' suites no longer hold the regression test by construction):
commands.test is a stub that says so, and the replay measures triage, the gate's scanners and review.

  factory replay run   --cases FILE --repos DIR --out DIR [--trials 3] [--jobs 3] [--only rb01,rb02]
  factory replay grade --cases FILE --repos DIR --out DIR      a blind Codex grader: does a finding describe the defect?
  factory replay report --cases FILE --out DIR [--pass-mark FILE]

`run` prints only case ids and states, so it can run a half the operator must not read.
"""
from __future__ import annotations

import concurrent.futures as cf
import io
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

import yaml

from factory import legs
from factory.calibrate import CHECKED, catchers, run_fixture

STUB_TEST = "echo 'replay: the project suite is not run; see factory/replay.py' && exit 0"
TEST_GLOBS = ["test/**", "tests/**", "spec/**", "__tests__/**", "**/__tests__/**", "**/*.test.*", "**/*.spec.*",
              "**/test/**", "**/tests/**"]
SAMPLE_CONFIG = Path(__file__).resolve().parent.parent / "calibration" / "sample-app" / ".factory" / "config.yaml"


def load_cases(path: Path) -> list[dict]:
    data = json.loads(Path(path).read_text())
    return data if isinstance(data, list) else data["cases"]


def gitc(repo: Path, *args: str, binary: bool = False):
    r = subprocess.run(["git", "-c", "core.hooksPath=/dev/null", *args], cwd=repo, capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "surrogateescape")


def exists_at(repo: Path, commit: str, path: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{commit}:{path}"], cwd=repo, capture_output=True).returncode == 0


def case_config() -> dict:
    sample = yaml.safe_load(SAMPLE_CONFIG.read_text())
    return {"commands": {"test": STUB_TEST}, "test_globs": TEST_GLOBS, "risk_paths": {},
            # A run names the corpus it reads explicitly: the sample's relative paths depend on where the factory sits.
            "axis_spec": os.environ.get("FACTORY_AXIS_SPEC") or sample.get("axis_spec"),
            "axis_index": os.environ.get("FACTORY_AXIS_INDEX") or sample.get("axis_index"),
            "builder": {"kind": "claude", "command": None}, "ratchet": {"semgrep_findings": True},
            "theory_doc": None, "review": dict(sample.get("review") or {})}


DOC = re.compile(r"(\.md|\.markdown|\.txt|\.rst)$|(^|/)docs?/|(^|/)(CHANGELOG|HISTORY|README|AUTHORS)", re.I)


def split_files(case: dict) -> tuple[list[str], list[str]]:
    """(code, undone): docs ride with the tests. A changelog line naming the fix would give a bug case away, so a
    case's doc changes, like its test changes, never reach the factory."""
    docs = [f for f in case["code_files"] if DOC.search(f)]
    return [f for f in case["code_files"] if f not in docs], list(case.get("test_files") or []) + docs


def materialise(case: dict, repos: Path, dest: Path) -> Path:
    """dest/{app/, story.md, change.patch, expect.yaml} for one case; returns dest."""
    repo = repos / case["project"]
    bug = case["kind"] == "bug"
    code, undone = split_files(case)
    if not code:
        raise ValueError(f"{case['id']}: no code files once docs and tests are set aside")
    base = case["commit"] if bug else case["parent"]
    if dest.exists():
        shutil.rmtree(dest)
    app = dest / "app"
    app.mkdir(parents=True)
    with tarfile.open(fileobj=io.BytesIO(gitc(repo, "archive", "--format=tar", base, binary=True))) as t:
        t.extractall(app, filter="data")
    if not bug:  # the commit's own test updates come first, as the factory's tests stage would write and lock them
        for f in case.get("test_files") or []:
            target = app / f
            if exists_at(repo, case["commit"], f):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(gitc(repo, "show", f"{case['commit']}:{f}", binary=True))
            elif target.exists():
                target.unlink()
    if bug:  # undo the fix's test-file and doc changes in the baseline
        for f in undone:
            target = app / f
            if exists_at(repo, case["parent"], f):
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(gitc(repo, "show", f"{case['parent']}:{f}", binary=True))
            elif target.exists():
                target.unlink()
    a, b = (case["commit"], case["parent"]) if bug else (case["parent"], case["commit"])
    patch = gitc(repo, "diff", "--no-color", "--no-ext-diff", "--binary", a, b, "--", *code)
    if not patch.strip():
        raise ValueError(f"{case['id']}: the code files give an empty change")
    (dest / "change.patch").write_text(patch)
    (app / ".factory").mkdir(exist_ok=True)
    (app / ".factory" / "config.yaml").write_text(yaml.safe_dump(case_config(), sort_keys=False))
    name = case["project"]
    (dest / "story.md").write_text(f"# A contributor's change to {name}\n\n"
                                   f"A contributor's change to {name}. Review it before it merges.\n")
    expect = {"should_block": bug, "caught_by": ["review"] if bug else []}
    (dest / "expect.yaml").write_text(yaml.safe_dump(expect))
    return dest


def findings_of(change_dir: Path) -> list[dict]:
    p = change_dir / "review" / "findings.json"
    return json.loads(p.read_text()) if p.exists() else []


def one_trial(case: dict, repos: Path, out: Path, trial: int, grounding: str | None) -> dict:
    key = f"{case['id']}-t{trial}"
    work = Path(tempfile.mkdtemp(prefix=f"replay-{key}-"))
    fx = materialise(case, repos, work / case["id"])
    row = run_fixture(fx, fx / "app", work / "run", grounding, True)
    rec = {"id": case["id"], "trial": trial, "kind": case["kind"], "error": row.get("error"),
           "blocks": row.get("blocks", []), "first": row.get("first"), "cost_usd": row.get("cost_usd"),
           "codex_tokens": row.get("codex_tokens"), "work": str(work)}
    if row.get("change_dir"):
        cdir = Path(row["change_dir"])
        rec["findings"] = findings_of(cdir)
        from factory.ledger import Change  # the outcome names which findings blocked
        change = Change(Path(row["work"]) / "app", case["id"])
        review_out = change.outcome("review") or {}
        rec["blocking"] = review_out.get("blocking") or []
        rec["review_malfunction"] = "review:malfunction" in catchers(change, "review")
        rec["stage_blocks"] = {s: catchers(change, s) for s in CHECKED}
    (out / "trials").mkdir(parents=True, exist_ok=True)
    (out / "trials" / f"{key}.json").write_text(json.dumps(rec, indent=1))
    return rec


INFRA = ("usage limit", "429 Too Many Requests", "model is at capacity", "waiting for network",
         "failed to refresh available models: request timed out", "Could not resolve host", "ENOTFOUND")


def infra_failure(rec: dict) -> str | None:
    """The marker, when a trial's review failed closed because a model service or the network was unavailable. Read
    from the legs' own logs, never from the result, so it applies to bug and control cases alike."""
    if not rec.get("review_malfunction") or not rec.get("work"):
        return None
    logs = Path(rec["work"]) / "run" / "app" / ".factory" / "changes" / rec["id"] / "review"
    text = " ".join(p.read_text(errors="replace") for p in logs.glob("*log*") if p.is_file())
    return next((m for m in INFRA if m in text), None)


def run(cases_file: Path, repos: Path, out: Path, trials: int = 3, jobs: int = 3, only: str | None = None,
        grounding: str | None = None) -> None:
    cases = load_cases(cases_file)
    if only:
        wanted = set(only.split(","))
        cases = [c for c in cases if c["id"] in wanted]
    out.mkdir(parents=True, exist_ok=True)
    todo = [(c, t) for t in range(1, trials + 1) for c in cases
            if not (out / "trials" / f"{c['id']}-t{t}.json").exists()]
    print(f"{len(cases)} cases x {trials} trials: {len(todo)} to run", flush=True)
    with cf.ThreadPoolExecutor(max_workers=jobs) as pool:
        futs = {pool.submit(one_trial, c, repos, out, t, grounding): f"{c['id']}-t{t}" for c, t in todo}
        for f in cf.as_completed(futs):
            try:
                rec = f.result()
                print(f"{futs[f]}: {'error' if rec.get('error') else 'done'}", flush=True)
            except Exception as e:  # reported by id only; the content stays unread
                print(f"{futs[f]}: harness error {type(e).__name__}", flush=True)
                (out / "harness-errors.txt").open("a").write(f"{futs[f]}: {type(e).__name__}: {e}\n")
    # Amendment of 2026-10-12, before the held-out run (PASS-MARK.md): a trial that failed closed on an outage is
    # kept in infra-failures/ and re-run once; the report gives the score both ways.
    retry = []
    for p in sorted((out / "trials").glob("*.json")):
        rec = json.loads(p.read_text())
        marker = infra_failure(rec)
        if marker and not (out / "infra-failures" / p.name).exists():
            (out / "infra-failures").mkdir(exist_ok=True)
            rec["infra_marker"] = marker
            (out / "infra-failures" / p.name).write_text(json.dumps(rec, indent=1))
            p.unlink()
            retry.append((next(c for c in cases if c["id"] == rec["id"]), rec["trial"]))
    for c, t in retry:
        rec = one_trial(c, repos, out, t, grounding)
        print(f"{c['id']}-t{t}: re-run after an outage: {'error' if rec.get('error') else 'done'}", flush=True)


GRADER = """You grade whether an automated code review found one specific, known defect. You are not reviewing the code.

The change under review re-introduced a real bug from an open-source project's history. What the bug does (taken from the
fix commit and its regression test):

{ground_truth}

The diff that later fixed it (buggy code on the minus side, fixed code on the plus side):

{fix_diff}

The review's findings (id, file, line, claim, and the review's reason):

{findings}

For each finding, decide whether it describes THIS defect: the same wrong behaviour from the same code, in any words, or
a symptom that only this defect causes. A finding about something else in the same code does not count; a vague finding
("this could have edge cases") does not count. Your final message is ONLY JSON, no prose and no code fence:
{{"matches": ["F1", ...], "reason": "one sentence"}}"""


def fix_diff(case: dict, repos: Path) -> str:
    return gitc(repos / case["project"], "diff", "--no-color", "--no-ext-diff", case["parent"], case["commit"], "--",
                *split_files(case)[0])


def grade_one(case: dict, rec: dict, repos: Path, out: Path) -> dict:
    key = f"{rec['id']}-t{rec['trial']}"
    found = [{k: f.get(k) for k in ("id", "file", "line", "claim", "reason")} for f in rec.get("findings") or []]
    if not found:
        return {"matches": [], "reason": "no findings"}
    gdir = out / "grades"
    gdir.mkdir(parents=True, exist_ok=True)
    prompt = GRADER.format(ground_truth=case["ground_truth"], fix_diff=fix_diff(case, repos)[:20000],
                           findings=json.dumps(found, indent=1))
    res = legs.run_codex(prompt, gdir, gdir / f"{key}.log", gdir / f"{key}.out.md", model="gpt-6.1-sol",
                         timeout_s=900)
    try:
        text = (gdir / f"{key}.out.md").read_text().strip()
        g = json.loads(text[text.index("{"):text.rindex("}") + 1])
        g["matches"] = [m for m in g.get("matches") or [] if any(m == f["id"] for f in found)]
    except Exception as e:
        g = {"matches": [], "reason": f"grader output unreadable: {type(e).__name__}", "grader_error": True}
    g["grader_ok"] = bool(res.get("ok")) and not g.get("grader_error")
    return g


def grade(cases_file: Path, repos: Path, out: Path, jobs: int = 3) -> None:
    out, repos = Path(out).resolve(), Path(repos).resolve()  # the Codex leg runs in its own working folder
    cases = {c["id"]: c for c in load_cases(cases_file)}
    recs = [json.loads(p.read_text()) for p in sorted((out / "trials").glob("*.json"))]
    todo = [r for r in recs if cases[r["id"]]["kind"] == "bug" and not (out / "grades" / f"{r['id']}-t{r['trial']}.json").exists()]
    print(f"{len(todo)} bug trials to grade", flush=True)
    def work(r):
        g = grade_one(cases[r["id"]], r, repos, out)
        (out / "grades").mkdir(parents=True, exist_ok=True)
        (out / "grades" / f"{r['id']}-t{r['trial']}.json").write_text(json.dumps(g, indent=1))
        return f"{r['id']}-t{r['trial']}: {'graded' if g.get('grader_ok', True) else 'GRADER ERROR'}"
    with cf.ThreadPoolExecutor(max_workers=jobs) as pool:
        for line in pool.map(work, todo):
            print(line, flush=True)


def outcome(case: dict, rec: dict, g: dict | None) -> dict:
    """One trial, scored by the rules in the pass mark."""
    if rec.get("error") or "stage_blocks" not in rec:
        return {"ok": False, "why": "errored"}
    blocked = [c for s in CHECKED for c in rec["stage_blocks"][s]]
    if case["kind"] == "control":
        return {"ok": not blocked, "why": "false alarm: " + ", ".join(blocked) if blocked else "passed clean",
                "review_alarm": bool(rec["stage_blocks"]["review"])}
    matches = set((g or {}).get("matches") or [])
    confirmed = {f["id"] for f in rec.get("findings") or [] if f.get("verdict") == "confirmed"}
    caught = bool(matches & set(rec.get("blocking") or []))
    return {"ok": caught, "surfaced": bool(matches & confirmed), "mentioned": bool(matches),
            "why": "caught (blocked on the defect)" if caught else
                   "surfaced to the signer, not blocked" if matches & confirmed else
                   "mentioned, not confirmed" if matches else "missed"}


def report(cases_file: Path, out: Path, pass_mark: Path | None = None, title: str = "") -> Path:
    cases = {c["id"]: c for c in load_cases(cases_file)}
    recs = {}
    for p in sorted((out / "trials").glob("*.json")):
        r = json.loads(p.read_text())
        recs.setdefault(r["id"], {})[r["trial"]] = r
    rows, per = [], {}
    for cid, case in sorted(cases.items()):
        trials = recs.get(cid, {})
        res = []
        for t in sorted(trials):
            gp = out / "grades" / f"{cid}-t{t}.json"
            res.append(outcome(case, trials[t], json.loads(gp.read_text()) if gp.exists() else None))
        per[cid] = res
        rows.append(f"| {cid} | {case['kind']} | {case['project']} | "
                    + " / ".join(r["why"] for r in res) + " |")
    def rate(kind, fn):
        vals = [fn(r) for cid, rs in per.items() if cases[cid]["kind"] == kind for r in rs]
        return (sum(vals), len(vals))
    def cases_rate(kind, fn):
        vals = [fn(rs) for cid, rs in per.items() if cases[cid]["kind"] == kind and rs]
        return (sum(vals), len(vals))
    k = max((len(rs) for rs in per.values()), default=0)
    m = {
        "bug_trials_caught": rate("bug", lambda r: r["ok"]),
        "bug_trials_surfaced": rate("bug", lambda r: r.get("ok") or r.get("surfaced", False)),
        "bug_cases_pass_hat_k": cases_rate("bug", lambda rs: len(rs) == k and all(r["ok"] for r in rs)),
        "bug_cases_pass_at_k": cases_rate("bug", lambda rs: any(r["ok"] for r in rs)),
        "control_trials_false_alarm": rate("control", lambda r: not r["ok"]),
        "control_trials_review_alarm": rate("control", lambda r: r.get("review_alarm", False)),
        "control_cases_pass_hat_k": cases_rate("control", lambda rs: len(rs) == k and all(r["ok"] for r in rs)),
        "errored_trials": (sum(r["why"] == "errored" for rs in per.values() for r in rs),
                           sum(len(rs) for rs in per.values())),
        "grader_errors": (sum(1 for p in (out / "grades").glob("*.json") if json.loads(p.read_text()).get("grader_error")),
                          len(list((out / "grades").glob("*.json"))) if (out / "grades").exists() else 0),
    }
    infra = sorted(p.stem for p in (out / "infra-failures").glob("*.json")) if (out / "infra-failures").exists() else []
    if infra:  # the original rule: each outage trial counts as a failure for its case
        lost_bugs = sum(1 for k in infra if cases[k.split("-t")[0]]["kind"] == "bug")
        lost_ctrl = len(infra) - lost_bugs
        n, d = m["bug_trials_caught"]
        f, fd = m["control_trials_false_alarm"]
        m["infra_reruns"] = (len(infra), sum(len(rs) for rs in per.values()))
        m["bug_trials_caught_original_rule"] = (n - min(n, lost_bugs), d)
        m["control_trials_false_alarm_original_rule"] = (min(fd, f + lost_ctrl), fd)
    costs = [r.get("cost_usd") or 0 for ts in recs.values() for r in ts.values()]
    tokens = [r.get("codex_tokens") or 0 for ts in recs.values() for r in ts.values()]
    lines = [f"# Real-bug replay{': ' + title if title else ''}", "",
             f"Cases: `{cases_file.name}` ({len(cases)}), trials per case: {k}. Claude review legs ${sum(costs):.2f}; "
             f"Codex review tokens {sum(tokens):,}.", "", "## Measures", "", "| Measure | Value |", "|---|---|"]
    for name, (n, d) in m.items():
        lines.append(f"| {name} | {n}/{d}" + (f" ({100 * n / d:.0f}%)" if d else "") + " |")
    if pass_mark and pass_mark.exists():
        lines += ["", "## Against the pass mark", "", "| Measure | Pass mark | Result | Meets |", "|---|---|---|---|"]
        for item in yaml.safe_load(pass_mark.read_text())["measures"]:
            n, d = m[item["measure"]]
            val = n / d if d else None
            ok = None if val is None else (val >= item["min"] if "min" in item else val <= item["max"])
            bound = f">= {item['min']:.0%}" if "min" in item else f"<= {item['max']:.0%}"
            lines.append(f"| {item['measure']} | {bound} ({item['status']}) | "
                         + (f"{val:.0%}" if val is not None else "n/a") + f" | {'yes' if ok else 'no' if ok is False else 'n/a'} |")
    if infra:
        lines += ["", f"Re-run once after an outage (originals in `infra-failures/`): {', '.join(infra)}."]
    lines += ["", "## Per case", "", "| Case | Kind | Project | Trials |", "|---|---|---|---|", *rows, ""]
    path = out / "report.md"
    path.write_text("\n".join(lines))
    (out / "measures.json").write_text(json.dumps(m, indent=1))
    return path
