"""PREREG-reproduce's offline test: put every recorded blocking finding through the reproduction step and score the
two pre-registered rules.

  .venv/bin/python calibration/realbugs/reproduce_offline.py --dry-run            # counts, prepares nothing
  .venv/bin/python calibration/realbugs/reproduce_offline.py [--jobs 3] [--runs v4-arm-v4,...]
  .venv/bin/python calibration/realbugs/reproduce_offline.py --score

Trees: each case's base and head, rebuilt with the replay's own materialise, with dependencies installed by the
operator (`npm ci --ignore-scripts`, or `npm install --ignore-scripts` without a lockfile; the network is used here,
never by the leg), kept under REPRO_TREES. Records: results/repro/{run}/{trial}-{finding}.json.

Scoring, as registered: a caught bug trial keeps its catch if any blocking finding the grader matched to the bug comes
out shown, argued or unchecked; a review-stopped control is cleared if it had blocking findings and every one comes out
not shown. A control stopped only by a review malfunction has no finding to test and counts as not cleared.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from factory.replay import load_cases, materialise, outcome
from factory.reproduce import KEEPS_BLOCKING, reproduce

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
OUT = RESULTS / "repro"
REPOS = Path(os.environ.get("FACTORY_REPLAY_REPOS", HERE.parents[2] / "realbugs-repos"))
TREES = Path(os.environ.get("REPRO_TREES", HERE.parents[2] / "realbugs-work" / "repro-trees"))
WORK = Path(os.environ.get("REPRO_WORK", HERE.parents[2] / "realbugs-work" / "repro-work"))
RUNS = {"v3-distillations": "v3-cases.json", "v4-arm-v3": "v4-cases.json", "v4-arm-v4": "v4-cases.json",
        "v5-b-factory": "v5-controls.json"}


def items(runs: list[str]) -> list[dict]:
    """(run, trial, kind, finding) for every blocking finding the test covers."""
    out = []
    for run in runs:
        base = RESULTS / run
        if not (base / "trials").exists():
            continue
        cases = {c["id"]: c for c in load_cases(HERE / RUNS[run])}
        for p in sorted((base / "trials").glob("*.json")):
            rec = json.loads(p.read_text())
            case = cases[rec["id"]]
            g = base / "grades" / p.name
            grade = json.loads(g.read_text()) if g.exists() else None
            blocking = rec.get("blocking") or []
            findings = {f["id"]: f for f in rec.get("findings") or []}
            if case["kind"] == "bug" and outcome(case, rec, grade)["ok"]:
                ids = [b for b in blocking if b in set((grade or {}).get("matches") or [])]
            elif case["kind"] == "control" and (rec.get("stage_blocks") or {}).get("review"):
                ids = list(blocking)
                if not ids:
                    out.append({"run": run, "trial": p.stem, "case": case, "kind": "control", "finding": None})
            else:
                continue
            out += [{"run": run, "trial": p.stem, "case": case, "kind": case["kind"], "finding": findings[i]}
                    for i in ids if i in findings]
    return out


def trees(case: dict) -> tuple[Path, Path]:
    """Pristine base and head trees for a case, dependencies installed once."""
    root = TREES / case["id"]
    base, head = root / "base", root / "head"
    if (root / ".ready").exists():
        return base, head
    shutil.rmtree(root, ignore_errors=True)
    fx = materialise(case, REPOS, Path(tempfile.mkdtemp()) / case["id"])
    shutil.copytree(fx / "app", base, symlinks=True)
    shutil.rmtree(base / ".factory", ignore_errors=True)
    if (base / "package.json").exists():
        cmd = ["npm", "ci"] if (base / "package-lock.json").exists() else ["npm", "install"]
        subprocess.run(cmd + ["--ignore-scripts", "--no-audit", "--no-fund", "--loglevel=error"], cwd=base,
                       capture_output=True, timeout=1200)
    subprocess.run(["cp", "-cR", str(base), str(head)], check=True)
    subprocess.run(["git", "apply", str(fx / "change.patch")], cwd=head, check=True, capture_output=True)
    (root / ".ready").write_text("ok\n")
    return base, head


def one(item: dict) -> str:
    f = item["finding"]
    rec_path = OUT / item["run"] / f"{item['trial']}-{f['id']}.json"
    if rec_path.exists():
        return f"{item['run']}/{item['trial']}-{f['id']}: done before"
    base, head = trees(item["case"])
    res = reproduce(f, base, head, WORK / item["run"] / f"{item['trial']}-{f['id']}")
    res.update(run=item["run"], trial=item["trial"], kind=item["kind"])
    rec_path.parent.mkdir(parents=True, exist_ok=True)
    rec_path.write_text(json.dumps(res, indent=1))
    return f"{item['run']}/{item['trial']}-{f['id']}: {res['outcome']}"


def score(runs: list[str]) -> dict:
    trials = {}
    for it in items(runs):
        t = trials.setdefault((it["run"], it["trial"]), {"kind": it["kind"], "outcomes": []})
        if it["finding"] is None:
            continue
        p = OUT / it["run"] / f"{it['trial']}-{it['finding']['id']}.json"
        t["outcomes"].append(json.loads(p.read_text())["outcome"] if p.exists() else "missing")
    bugs = [t for t in trials.values() if t["kind"] == "bug"]
    ctrls = [t for t in trials.values() if t["kind"] == "control"]
    kept = sum(any(o in KEEPS_BLOCKING for o in t["outcomes"]) for t in bugs)
    cleared = sum(bool(t["outcomes"]) and all(o == "not shown" for o in t["outcomes"]) for t in ctrls)
    every = [o for t in trials.values() for o in t["outcomes"]]
    by_kind = {k: {o: sum(x == o for t in trials.values() if t["kind"] == k for x in t["outcomes"])
                   for o in ("shown", "not shown", "argued", "unchecked", "missing")} for k in ("bug", "control")}
    s = {"bug_trials": len(bugs), "catches_kept": kept, "control_trials": len(ctrls), "controls_cleared": cleared,
         "outcomes": by_kind, "missing": every.count("missing"),
         "rule_1_catches_kept_90pct": kept >= 0.9 * len(bugs), "rule_2_half_cleared": cleared >= len(ctrls) / 2}
    s["verdict"] = "GOES IN" if s["rule_1_catches_kept_90pct"] and s["rule_2_half_cleared"] and not s["missing"] \
        else "DOES NOT GO IN" if not s["missing"] else "INCOMPLETE"
    return s


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default=",".join(RUNS))
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--score", action="store_true")
    args = ap.parse_args()
    runs = args.runs.split(",")
    if args.score:
        s = score(runs)
        (OUT / "summary.json").parent.mkdir(parents=True, exist_ok=True)
        (OUT / "summary.json").write_text(json.dumps(s, indent=1))
        print(json.dumps(s, indent=1))
        return
    todo = [it for it in items(runs) if it["finding"] is not None]
    print(f"{len(todo)} findings across {len({(i['run'], i['trial']) for i in todo})} trials")
    if args.dry_run:
        return
    for case in {it["case"]["id"]: it["case"] for it in todo}.values():  # trees first, one at a time (npm)
        trees(case)
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for line in pool.map(one, todo):
            print(line, flush=True)


if __name__ == "__main__":
    main()
