"""Score pre-registration v8 (PREREG-v8-other-reviewers.md). Written and committed before any v8 trial ran.

  .venv/bin/python calibration/realbugs/compare_v8.py --build   # v8-factory-claude and v8-plain, from v6's trials
  .venv/bin/python calibration/realbugs/compare_v8.py

The rule (as v5 to v7): an arm did better than another only if its grounded precision and grounded recall (the judge's
per-pull-request averages) are each at least as high and one is higher by at least 5 points. Primary: factory-claude
against brooks and against cc-review; every other pair reported under the same rule. Reported, not judged:
high-severity golden findings found, findings per pull request, cost, /code-review's effort level, fallback files.
"""
from __future__ import annotations

import itertools
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "runner-v5"))
from compare_v5 import better_a, metric  # noqa: E402  (the same reading of the judge's output, the same rule)
from compare_v6 import high_found  # noqa: E402

ARMS = ("factory-claude", "brooks", "cc-review", "plain")


def build() -> None:
    from run_v5 import part_e_cases, rb_file
    cases = {c["id"]: c for c in part_e_cases()}
    fc = RESULTS / "v8-factory-claude" / "findings"
    fc.mkdir(parents=True, exist_ok=True)
    for cid, case in cases.items():
        rec = json.loads((RESULTS / "v6-factory" / "trials" / f"{cid}-t1.json").read_text())
        mine = [m for f in rec.get("findings") or [] for m in f.get("members") or [f] if m.get("leg") == "claude"]
        findings = []
        for f in mine:
            n = re.match(r"\d+", str(f.get("line") or "1"))
            line = int(n.group()) if n else 1
            message = " ".join(str(f.get(k) or "").strip() for k in ("claim", "evidence")).strip()
            findings.append({"file": str(f.get("file") or ""), "start_line": line, "end_line": line, "message": message})
        fc.joinpath(f"{cid}.json").write_text(json.dumps(rb_file(case, "v8-factory-claude", findings, 0), indent=1))
    plain = RESULTS / "v8-plain" / "findings"
    plain.mkdir(parents=True, exist_ok=True)
    for cid in cases:
        a = json.loads((RESULTS / "v6-claude-again" / "findings" / f"{cid}.json").read_text())
        plain.joinpath(f"{cid}.json").write_text(json.dumps({**a, "agent": "v8-plain",
                                                             "findings": [{**f, "producer": "v8-plain"}
                                                                          for f in a["findings"]]}, indent=1))
    print("built factory-claude and plain for", len(cases), "pull requests")


def arm(name: str) -> dict | None:
    p = RESULTS / f"v8-{name}" / "scoring" / "results.json"
    if not p.exists():
        return None
    r = json.loads(p.read_text())
    strata = ("severity", "category", "high", "medium", "low", "bycategory", "byseverity")
    files = sorted((RESULTS / f"v8-{name}" / "findings").glob("*.json"))
    out = {"grounded_precision": metric(r, "grounded", "precision", avoid=strata),
           "grounded_recall": metric(r, "grounded", "recall", avoid=strata),
           "augmented_precision": metric(r, "augmented", "precision", avoid=strata),
           "augmented_recall": metric(r, "augmented", "recall", avoid=strata),
           "high_found": high_found(p.with_name("results.details.json")),
           "pull_requests": len(files),
           "findings_per_pr": round(sum(len(json.loads(f.read_text())["findings"]) for f in files) / len(files), 2)}
    trials = sorted((RESULTS / f"v8-{name}" / "trials").glob("*.json"))
    if trials:
        metas = [json.loads(t.read_text())["meta"] for t in trials]
        out["cost_usd"] = round(sum(m.get("cost_usd") or 0 for m in metas), 2)
        out["fallback_file"] = sum(m.get("fallback_file") or 0 for m in metas)
        out["timed_out_or_unreadable"] = sum(bool(m.get("timed_out") or m.get("unreadable")) for m in metas)
        if name == "cc-review":
            out["levels"] = {lv: sum(m.get("level") == lv for m in metas) for lv in {m.get("level") for m in metas}}
            out["no_report_findings"] = sum(bool(m.get("no_report_findings")) for m in metas)
    return out


def main() -> None:
    if "--build" in sys.argv:
        build()
        return
    a = {n: arm(n) for n in ARMS}
    print(json.dumps({"arms": a}, indent=1, default=str))
    for other in ("brooks", "cc-review"):
        x, y = a["factory-claude"], a[other]
        print(f"\nPrimary: factory-claude against {other}:",
              "factory-claude did better" if x and y and better_a(x, y) else
              f"{other} did better" if x and y and better_a(y, x) else
              "about the same on these pull requests (or not yet judged)")
    for x, y in itertools.permutations(ARMS, 2):
        if a[x] and a[y] and better_a(a[x], a[y]):
            print(f"  {x} did better than {y}")


if __name__ == "__main__":
    main()
