"""Score pre-registration v7 (PREREG-v7-single-model.md). Written and committed before any v7 trial ran.

  .venv/bin/python calibration/realbugs/compare_v7.py --build   # split the runs into the four single-model arms
  .venv/bin/python calibration/realbugs/compare_v7.py

Arms: opus-factory (the factory's Claude reviewer, before the sort), opus-own (Claude Code, plain prompt), sol-factory
(the factory's Codex reviewer, before the sort), sol-own (`codex review`). Per model: overall, the v5 rule on grounded
precision and recall (5 points); serious, high-severity golden true findings found (3 or more apart).
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
RB = Path(os.environ.get("RB_ROOT", HERE.parents[2] / "ReviewBench"))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "runner-v5"))
from compare_v5 import better_a, metric  # noqa: E402

PAIRS = {"Opus": ("opus-factory", "opus-own"), "Sol": ("sol-factory", "sol-own")}


def build() -> None:
    import run_v5
    cases = {c["id"]: c for c in run_v5.part_d_cases()}
    for name in ("opus-factory", "opus-own", "sol-factory", "sol-own"):
        (RESULTS / f"v7-{name}" / "findings").mkdir(parents=True, exist_ok=True)
    for cid, case in cases.items():
        legs = {"claude": [], "codex": []}
        t = RESULTS / "v7-factory" / "trials" / f"{cid}-t1.json"
        for item in json.loads(t.read_text()).get("findings") or [] if t.exists() else []:
            for m in item.get("members") or []:
                line = m.get("line") if isinstance(m.get("line"), int) else 1
                legs.setdefault(m.get("leg"), []).append({
                    "file": str(m.get("file") or ""), "start_line": line, "end_line": line,
                    "message": " ".join(str(m.get(k) or "").strip() for k in ("claim", "evidence")).strip()})
        v = RESULTS / "v7-vendors" / "trials" / f"{cid}.json"
        own = json.loads(v.read_text())["findings"] if v.exists() else []
        sets = {"opus-factory": legs["claude"], "sol-factory": legs["codex"],
                "opus-own": [f for f in own if f["source"] == "claude"],
                "sol-own": [f for f in own if f["source"] == "codex"]}
        for name, fs in sets.items():
            rb = run_v5.rb_file(case, f"v7-{name}", fs, 0)
            (RESULTS / f"v7-{name}" / "findings" / f"{cid}.json").write_text(json.dumps(rb, indent=1))
    print("built four single-model arms for", len(cases), "pull requests")


def high_found(name: str) -> int:
    details = RESULTS / f"v7-{name}" / "scoring" / "results.details.json"
    found = set()
    for pr in json.loads(details.read_text()):
        golden = json.loads((RB / "golden" / f"{pr['pr_key']}.json").read_text())["findings"]
        high = {i for i, g in enumerate(golden) if g.get("tp_fp") == "tp" and g.get("severity") == "high"}
        for f in pr["candidate_findings"]:
            if f["status"] in ("matched_tp", "matched_fp"):
                cov = set(f.get("covered_golden_indices") or [f.get("matched_golden_index")])
                found |= {(pr["pr_key"], i) for i in cov & high}
    return len(found)


def arm(name: str) -> dict | None:
    p = RESULTS / f"v7-{name}" / "scoring" / "results.json"
    if not p.exists():
        return None
    r = json.loads(p.read_text())
    strata = ("severity", "category", "high", "medium", "low", "bycategory", "byseverity")
    files = sorted((RESULTS / f"v7-{name}" / "findings").glob("*.json"))
    return {"grounded_precision": metric(r, "grounded", "precision", avoid=strata),
            "grounded_recall": metric(r, "grounded", "recall", avoid=strata),
            "augmented_precision": metric(r, "augmented", "precision", avoid=strata),
            "augmented_recall": metric(r, "augmented", "recall", avoid=strata),
            "high_found": high_found(name),
            "findings_per_pr": round(sum(len(json.loads(f.read_text())["findings"]) for f in files) / len(files), 2)}


def main() -> None:
    if "--build" in sys.argv:
        build()
        return
    a = {n: arm(n) for pair in PAIRS.values() for n in pair}
    print(json.dumps(a, indent=1))
    for model, (fac, own) in PAIRS.items():
        x, y = a[fac], a[own]
        if not (x and y):
            print(f"\n{model}: not yet judged")
            continue
        overall = "factory brief did better" if better_a(x, y) else "own tool did better" if better_a(y, x) else "about the same"
        d = x["high_found"] - y["high_found"]
        serious = "factory brief found more" if d >= 3 else "own tool found more" if d <= -3 else "about the same"
        print(f"\n{model}: overall {overall}; serious findings {serious} ({x['high_found']} against {y['high_found']})")


if __name__ == "__main__":
    main()
