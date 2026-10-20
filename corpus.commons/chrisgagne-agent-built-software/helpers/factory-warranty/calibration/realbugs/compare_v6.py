"""Score pre-registration v6 (PREREG-v6-review-legs.md). Written and committed before any v6 trial ran.

  .venv/bin/python calibration/realbugs/compare_v6.py --build-control   # v6-control = vendors + a second Claude review
  .venv/bin/python calibration/realbugs/compare_v6.py

The rule (as v5): an arm did better than another only if its grounded precision and grounded recall (the judge's
per-pull-request averages) are each at least as high and one is higher by at least 5 points. Primary: factory against
vendors; also factory against control and control against vendors. Reported, not judged: high-severity golden
findings found, findings per pull request, and each factory leg alone (from the judge's per-finding decisions).
"""
from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
sys.path.insert(0, str(HERE))
from compare_v5 import better_a, metric  # noqa: E402  (the same reading of the judge's output, the same rule)

ARMS = ("factory", "vendors", "control", "pr-agent")


def build_control() -> None:
    out = RESULTS / "v6-control" / "findings"
    out.mkdir(parents=True, exist_ok=True)
    for p in sorted((RESULTS / "v6-vendors" / "findings").glob("*.json")):
        again = RESULTS / "v6-claude-again" / "findings" / p.name
        if not again.exists():
            raise SystemExit(f"no second Claude review for {p.stem}")
        a, b = json.loads(p.read_text()), json.loads(again.read_text())
        out.joinpath(p.name).write_text(json.dumps({**a, "agent": "v6-control",
                                                    "findings": a["findings"] + b["findings"]}, indent=1))
    print("control built for", len(list(out.glob("*.json"))), "pull requests")


def high_found(details: Path, keep=lambda f: True) -> int:
    s = set()
    for pr in json.loads(details.read_text()):
        for f in pr["candidate_findings"]:
            if keep(f) and f["status"] == "matched_tp" and f.get("golden_severity") == "high":
                s |= {(pr["pr_key"], g) for g in (f.get("covered_golden_indices") or [f.get("matched_golden_index")])}
    return len(s)


def arm(name: str) -> dict | None:
    p = RESULTS / f"v6-{name}" / "scoring" / "results.json"
    if not p.exists():
        return None
    r = json.loads(p.read_text())
    strata = ("severity", "category", "high", "medium", "low", "bycategory", "byseverity")
    files = sorted((RESULTS / f"v6-{name}" / "findings").glob("*.json"))
    return {"grounded_precision": metric(r, "grounded", "precision", avoid=strata),
            "grounded_recall": metric(r, "grounded", "recall", avoid=strata),
            "augmented_precision": metric(r, "augmented", "precision", avoid=strata),
            "augmented_recall": metric(r, "augmented", "recall", avoid=strata),
            "high_found": high_found(p.with_name("results.details.json")),
            "pull_requests": len(files),
            "findings_per_pr": round(sum(len(json.loads(f.read_text())["findings"]) for f in files) / len(files), 2)}


def factory_legs() -> dict:
    """Each factory leg alone: its share of the factory arm's judged findings."""
    leg_of = {}
    for t in (RESULTS / "v6-factory" / "trials").glob("*.json"):
        for item in json.loads(t.read_text()).get("findings") or []:
            for m in item.get("members") or []:
                msg = " ".join(str(m.get(k) or "").strip() for k in ("claim", "evidence")).strip()
                leg_of[(str(m.get("file") or ""), msg[:200])] = m.get("leg")
    details = RESULTS / "v6-factory" / "scoring" / "results.details.json"
    if not details.exists():
        return {}
    return {leg: high_found(details, lambda f, leg=leg: leg_of.get((f["file"], f["message"][:200])) == leg)
            for leg in ("claude", "claude-plain", "codex-review")}


def main() -> None:
    if "--build-control" in sys.argv:
        build_control()
        return
    a = {n: arm(n) for n in ARMS}
    print(json.dumps({"arms": a, "factory_legs_high_found": factory_legs()}, indent=1))
    print("\nPrimary: factory against vendors:",
          "factory did better" if a["factory"] and a["vendors"] and better_a(a["factory"], a["vendors"]) else
          "vendors did better" if a["factory"] and a["vendors"] and better_a(a["vendors"], a["factory"]) else
          "about the same on these pull requests (or not yet judged)")
    for x, y in itertools.permutations(ARMS, 2):
        if a[x] and a[y] and better_a(a[x], a[y]):
            print(f"  {x} did better than {y}")


if __name__ == "__main__":
    main()
