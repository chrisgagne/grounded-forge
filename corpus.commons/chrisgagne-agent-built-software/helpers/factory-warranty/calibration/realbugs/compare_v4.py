"""Score pre-registration v4 (PREREG-v4-false-stops.md): the round-two factory against the v3 factory.

Written and committed before any v4 trial was graded. Uses the replay's own per-trial scoring (`replay.outcome`) and
applies the pre-registered rule:

  Round two works if both hold:
  1. of the 24 good-change trials, the v4 arm stops at most half as many as the v3 arm (rounded down), and at most 5;
  2. of the 8 bug cases, the v4 arm catches on both trials at least as many as the v3 arm, less one.

Also reported, not judged: review legs that ran out of time per arm, the severity of each finding that stopped a good
change and whether it named a trigger, and the share of confirmed findings naming a standard, source or library row.

  .venv/bin/python calibration/realbugs/compare_v4.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from factory.replay import load_cases, outcome

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from compare_v3 import cites  # noqa: E402  (the same citation patterns as v3)

CASES = HERE / "v4-cases.json"
ARMS = {"v3": HERE / "results" / "v4-arm-v3", "v4": HERE / "results" / "v4-arm-v4"}
TRIALS = 2


def arm(out: Path, cases: dict) -> dict:
    per, confirmed, stops, timeouts = {}, [], [], 0
    for cid, case in cases.items():
        res = []
        for t in range(1, TRIALS + 1):
            p = out / "trials" / f"{cid}-t{t}.json"
            if not p.exists():
                continue
            rec = json.loads(p.read_text())
            gp = out / "grades" / f"{cid}-t{t}.json"
            o = outcome(case, rec, json.loads(gp.read_text()) if gp.exists() else None)
            res.append(o)
            confirmed += [f for f in rec.get("findings") or [] if f.get("verdict") == "confirmed"]
            timeouts += bool(rec.get("review_malfunction") and not rec.get("codex_tokens"))
            if case["kind"] == "control" and not o["ok"]:
                fs = {f["id"]: f for f in rec.get("findings") or []}
                stops.append({"trial": f"{cid}-t{t}", "stages": [s for s, v in rec["stage_blocks"].items() if v],
                              "findings": [{"raw": fs[b].get("raw_severity"), "sorted": fs[b].get("severity"),
                                            "evidence": (fs[b].get("evidence") or "")[:200]}
                                           for b in rec.get("blocking") or [] if b in fs]})
        per[cid] = res
    bugs = [c for c in cases if cases[c]["kind"] == "bug"]
    ctrl_trials = [r for c in cases if cases[c]["kind"] == "control" for r in per[c]]
    return {"bug_cases_caught_2of2": sorted(c for c in bugs if len(per[c]) == TRIALS and all(r["ok"] for r in per[c])),
            "control_trials_stopped": sum(not r["ok"] for r in ctrl_trials), "control_trials": len(ctrl_trials),
            "review_timeouts_or_no_codex": timeouts, "stops": stops,
            "confirmed_findings": len(confirmed), "confirmed_citing": sum(cites(f) for f in confirmed),
            "incomplete": sorted(c for c in cases if len(per[c]) < TRIALS),
            "errored_trials": sum(r["why"] == "errored" for rs in per.values() for r in rs)}


def main() -> None:
    cases = {c["id"]: c for c in load_cases(CASES)}
    a = {name: arm(out, cases) for name, out in ARMS.items()}
    old, new = a["v3"], a["v4"]
    stops_ok = new["control_trials_stopped"] <= old["control_trials_stopped"] // 2 and new["control_trials_stopped"] <= 5
    catches_ok = len(new["bug_cases_caught_2of2"]) >= len(old["bug_cases_caught_2of2"]) - 1
    print(json.dumps(a, indent=1))
    print(f"\ngood-change trials stopped: v3 {old['control_trials_stopped']}/{old['control_trials']}, "
          f"v4 {new['control_trials_stopped']}/{new['control_trials']} (the rule: at most "
          f"{old['control_trials_stopped'] // 2} and at most 5): {'met' if stops_ok else 'not met'}")
    print(f"bug cases caught 2 of 2: v3 {len(old['bug_cases_caught_2of2'])}/8, v4 {len(new['bug_cases_caught_2of2'])}/8 "
          f"(the rule: at least {len(old['bug_cases_caught_2of2']) - 1}): {'met' if catches_ok else 'not met'}")
    for name, x in a.items():
        share = x["confirmed_citing"] / x["confirmed_findings"] if x["confirmed_findings"] else 0
        print(f"{name}: review time-outs {x['review_timeouts_or_no_codex']}; {x['confirmed_citing']} of "
              f"{x['confirmed_findings']} confirmed findings cite ({share:.0%}); errored {x['errored_trials']}; "
              f"incomplete {x['incomplete']}")
    print(f"\nRound two: {'WORKS' if stops_ok and catches_ok else 'DOES NOT WORK'} (as pre-registered)")


if __name__ == "__main__":
    main()
