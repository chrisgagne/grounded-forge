"""Score pre-registration v9 (PREREG-v9-plain-and-built-in.md). Written and committed before any v9 trial ran.

  .venv/bin/python calibration/realbugs/compare_v9.py

The rule (as v5 to v8): an arm did better than another only if its grounded precision and grounded recall (the judge's
per-pull-request averages) are each at least as high and one is higher by at least 5 points. Primary: sol-factory
against sol-plain, and opus-plain against each /code-review level. Every other pair reported under the same rule.
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
from compare_v6 import high_found  # noqa: E402

# arm name -> results folder (the v7 arms are reused as judged there)
ARMS = {"sol-factory": "v7-sol-factory", "sol-own": "v7-sol-own", "opus-factory": "v7-opus-factory",
        "opus-plain": "v7-opus-own", "sol-plain": "v9-sol-plain", "sol-plain-high": "v9-sol-plain-high",
        "cc-review": "v9-cc-review", "cc-review-high": "v9-cc-review-high", "cc-review-xhigh": "v9-cc-review-xhigh",
        "codex-review-high": "v9-codex-review-high"}  # the last added by Amendment 1
PRIMARY = [("sol-factory", "sol-plain"), ("opus-plain", "cc-review"), ("opus-plain", "cc-review-high"),
           ("opus-plain", "cc-review-xhigh"),
           # Amendment 1 (2026-10-21): codex review at "high" against Sol's other arms
           ("codex-review-high", "sol-own"), ("codex-review-high", "sol-plain-high"), ("codex-review-high", "sol-factory")]


def arm(folder: str) -> dict | None:
    p = RESULTS / folder / "scoring" / "results.json"
    if not p.exists():
        return None
    r = json.loads(p.read_text())
    strata = ("severity", "category", "high", "medium", "low", "bycategory", "byseverity")
    files = sorted((RESULTS / folder / "findings").glob("*.json"))
    out = {"grounded_precision": metric(r, "grounded", "precision", avoid=strata),
           "grounded_recall": metric(r, "grounded", "recall", avoid=strata),
           "high_found": high_found(p.with_name("results.details.json")),
           "pull_requests": len(files),
           "findings_per_pr": round(sum(len(json.loads(f.read_text())["findings"]) for f in files) / len(files), 2)}
    metas = [json.loads(t.read_text())["meta"] for t in sorted((RESULTS / folder / "trials").glob("*.json"))]
    if metas:
        out["cost_usd"] = round(sum(m.get("cost_usd") or 0 for m in metas), 2)
        out["codex_tokens"] = sum(m.get("tokens") or 0 for m in metas)
        out["failed"] = sum(bool(m.get("timed_out") or m.get("unreadable")) for m in metas)
        for key in ("level", "reasoning_effort"):
            seen = [m.get(key) for m in metas if key in m]
            if seen:
                out[key] = {str(v): seen.count(v) for v in sorted(set(map(str, seen)))}
    return out


def verdict(a: dict | None, b: dict | None, x: str, y: str) -> str:
    if not (a and b):
        return "not yet judged"
    return f"{x} did better" if better_a(a, b) else f"{y} did better" if better_a(b, a) else "about the same on these pull requests"


def main() -> None:
    a = {n: arm(f) for n, f in ARMS.items()}
    print(json.dumps({"arms": a}, indent=1))
    for x, y in PRIMARY:
        print(f"\nPrimary: {x} against {y}: {verdict(a[x], a[y], x, y)}")
    print()
    for x, y in itertools.permutations(ARMS, 2):
        if a[x] and a[y] and better_a(a[x], a[y]):
            print(f"  {x} did better than {y}")


if __name__ == "__main__":
    main()
