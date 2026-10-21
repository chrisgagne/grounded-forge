"""Score pre-registration v5 (PREREG-v5-head-to-head.md and its Amendment 1).

Written and committed before any arm's findings were judged. It reads ReviewBench's judge output for part A and the
arms' trial records for part B, and applies the pre-registered rules:

  Part A: one arm did better than another only if its grounded precision and grounded recall are each at least as
          high, and one of them higher by at least 5 points (one trial per arm, so "in every trial" is that trial).
  Part B: one arm stopped fewer good changes only if at least 3 fewer of the 15.
  Otherwise: "about the same".

Also reported, not judged: augmented precision and recall, high-severity recall where the judge reports it, findings
and minutes per review, cost.

  .venv/bin/python calibration/realbugs/compare_v5.py
"""
from __future__ import annotations

import itertools
import json
import re
from pathlib import Path

from factory.replay import load_cases, outcome

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
ARMS = ("factory", "vendors", "pr-agent")


def leaves(d, path=()):
    """Every numeric leaf of a nested dict, with its key path."""
    if isinstance(d, dict):
        for k, v in d.items():
            yield from leaves(v, path + (str(k),))
    elif isinstance(d, (int, float)) and not isinstance(d, bool):
        yield path, d


def metric(results: dict, *words: str, avoid: tuple[str, ...] = ()) -> float | None:
    """The one numeric leaf whose key path names every word (and none of `avoid`), shortest path first; ReviewBench's
    results.json is read by name, not by a layout assumed in advance."""
    norm = lambda p: re.sub(r"[^a-z]", "", ".".join(p).lower())
    hits = sorted(((p, v) for p, v in leaves(results) if all(w in norm(p) for w in words)
                   and not any(a in norm(p) for a in avoid)), key=lambda pv: len(pv[0]))
    return hits[0][1] if hits else None


def part_a() -> dict:
    out = {}
    for arm in ARMS:
        p = RESULTS / f"v5-a-{arm}" / "scoring" / "results.json"
        if not p.exists():
            out[arm] = None
            continue
        r = json.loads(p.read_text())
        strata = ("severity", "category", "high", "medium", "low", "bycategory", "byseverity")
        row = {"grounded_precision": metric(r, "grounded", "precision", avoid=strata),
               "grounded_recall": metric(r, "grounded", "recall", avoid=strata),
               "augmented_precision": metric(r, "augmented", "precision", avoid=strata),
               "augmented_recall": metric(r, "augmented", "recall", avoid=strata),
               "high_severity_grounded_recall": metric(r, "high", "grounded", "recall")}
        files = sorted((RESULTS / f"v5-a-{arm}" / "findings").glob("*.json"))
        row["pull_requests"] = len(files)
        row["findings_per_pr"] = round(sum(len(json.loads(f.read_text())["findings"]) for f in files) / len(files), 2) \
            if files else None
        out[arm] = row
    return out


def better_a(x: dict, y: dict) -> bool:
    px, rx, py, ry = x["grounded_precision"], x["grounded_recall"], y["grounded_precision"], y["grounded_recall"]
    if None in (px, rx, py, ry):
        return False
    scale = 100 if max(px, rx, py, ry) <= 1 else 1  # points, whether the judge reports fractions or percentages
    return px >= py and rx >= ry and max(px - py, rx - ry) * scale >= 5


def part_b() -> dict:
    cases = {c["id"]: c for c in load_cases(HERE / "v5-controls.json")}
    out = {}
    for arm in ARMS:
        base = RESULTS / f"v5-b-{arm}" / "trials"
        stopped, done = 0, 0
        for cid, case in cases.items():
            p = base / (f"{cid}-t1.json" if arm == "factory" else f"{cid}.json")
            if not p.exists():
                continue
            rec = json.loads(p.read_text())
            done += 1
            stopped += (not outcome(case, rec, None)["ok"]) if arm == "factory" else bool(rec.get("stopped"))
        out[arm] = {"good_changes_stopped": stopped, "of": done, "missing": len(cases) - done}
    return out


def main() -> None:
    a, b = part_a(), part_b()
    print(json.dumps({"part_a": a, "part_b": b}, indent=1))
    print("\nPart A (ReviewBench test set, offline, judged by Claude Sonnet 5):")
    for x, y in itertools.permutations(ARMS, 2):
        if a.get(x) and a.get(y) and better_a(a[x], a[y]):
            print(f"  {x} did better than {y}")
    print("  (any pair not listed: about the same on these pull requests, or not yet judged)")
    print("Part B (15 good changes, one trial per arm):")
    for x, y in itertools.permutations(ARMS, 2):
        if b[x]["of"] == b[y]["of"] == 15 and b[y]["good_changes_stopped"] - b[x]["good_changes_stopped"] >= 3:
            print(f"  {x} stopped fewer good changes than {y}")
    print("  (any pair not listed: about the same on these changes, or not yet complete)")


if __name__ == "__main__":
    main()
