"""Score pre-registration v3 (PREREG-v3-grounding.md): the corpus arm against the no-corpus arm.

Written and committed before any v3 trial was graded. Uses the replay's own per-trial scoring (`replay.outcome`), so
a catch means what the pass mark says it means, then applies the pre-registered rule:

  Criterion (a) is met if the `distillations` arm catches every time (2 of 2 trials) at least 3 more of the 17 bug
  cases than the `none` arm, and at most 1 more control case has a false alarm in any trial.

Secondary, descriptive: the share of confirmed findings in each arm that name a standard, a corpus source or an axis
row. A finding counts when it carries an `axis_row`, or its claim or reason names a corpus slug or a standard's
identifier (patterns below, fixed before grading).

  .venv/bin/python calibration/realbugs/compare_v3.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from factory.replay import load_cases, outcome

HERE = Path(__file__).resolve().parent
CASES = HERE / "v3-cases.json"
ARMS = {"none": HERE / "results" / "v3-none", "distillations": HERE / "results" / "v3-distillations"}
TRIALS = 2

SLUGS = ["nist-ssdf-1-1", "nist-sp-800-218a", "cisa-secure-software-attestation-form", "owasp-asvs-5-0",
         "owasp-llm-top10-2026", "owasp-agentic-top10-2026", "owasp-agentic-threats-mitigations",
         "becker-metr-ai-developer-productivity-2025", "he-cursor-velocity-complexity-2025", "jimenez-swe-bench",
         "why-language-models-hallucinate-kalai", "dora-ai-assisted-swdev-2025", "egashira-testsuitebench-2026",
         "cucumber-bdd-gherkin", "microsoft-code-with-engineering-playbook", "uk-duck-book-qa-of-code",
         "uk-aqua-book-2025", "openssf-finding-fixing-vulnerabilities-ai"]
STANDARD = re.compile(r"\b(ASVS|SSDF|SP 800-218A?|OWASP|CWE-\d+|ASI\d{2}|LLM\d{2}|[PR][OSWV]\.\d+(\.\d+)?|NIST|CISA|"
                      r"AQuA|Duck Book|OpenSSF)\b")


def cites(f: dict) -> bool:
    text = f"{f.get('claim') or ''} {f.get('reason') or ''}"
    return bool(f.get("axis_row")) or any(s in text for s in SLUGS) or bool(STANDARD.search(text))


def arm(out: Path, cases: dict) -> dict:
    per, confirmed = {}, []
    for cid, case in cases.items():
        res = []
        for t in range(1, TRIALS + 1):
            p = out / "trials" / f"{cid}-t{t}.json"
            if not p.exists():
                continue
            rec = json.loads(p.read_text())
            gp = out / "grades" / f"{cid}-t{t}.json"
            res.append(outcome(case, rec, json.loads(gp.read_text()) if gp.exists() else None))
            confirmed += [f for f in rec.get("findings") or [] if f.get("verdict") == "confirmed"]
        per[cid] = res
    bugs = [c for c in cases if cases[c]["kind"] == "bug"]
    ctrls = [c for c in cases if cases[c]["kind"] == "control"]
    caught_every = sorted(c for c in bugs if len(per[c]) == TRIALS and all(r["ok"] for r in per[c]))
    alarmed = sorted(c for c in ctrls if any(not r["ok"] for r in per[c]))
    incomplete = sorted(c for c in cases if len(per[c]) < TRIALS)
    return {"bug_cases_caught_2of2": caught_every, "control_cases_false_alarm": alarmed, "incomplete": incomplete,
            "confirmed_findings": len(confirmed), "confirmed_citing": sum(cites(f) for f in confirmed),
            "errored_trials": sum(r["why"] == "errored" for rs in per.values() for r in rs)}


def main() -> None:
    cases = {c["id"]: c for c in load_cases(CASES)}
    a = {name: arm(out, cases) for name, out in ARMS.items()}
    n, d = a["none"], a["distillations"]
    more_caught = len(d["bug_cases_caught_2of2"]) - len(n["bug_cases_caught_2of2"])
    more_alarms = len(d["control_cases_false_alarm"]) - len(n["control_cases_false_alarm"])
    met = more_caught >= 3 and more_alarms <= 1
    print(json.dumps(a, indent=1))
    print(f"\nbug cases caught 2 of 2: none {len(n['bug_cases_caught_2of2'])}/17, "
          f"distillations {len(d['bug_cases_caught_2of2'])}/17 (difference {more_caught:+d}; the rule needs +3)")
    print(f"control cases with a false alarm: none {len(n['control_cases_false_alarm'])}/8, "
          f"distillations {len(d['control_cases_false_alarm'])}/8 (difference {more_alarms:+d}; the rule allows +1)")
    for name, x in a.items():
        share = x["confirmed_citing"] / x["confirmed_findings"] if x["confirmed_findings"] else 0
        print(f"{name}: {x['confirmed_citing']} of {x['confirmed_findings']} confirmed findings cite a standard, "
              f"corpus source or axis row ({share:.0%}); errored trials {x['errored_trials']}; incomplete {x['incomplete']}")
    print(f"\nCriterion (a): {'MET' if met else 'NOT MET'}")


if __name__ == "__main__":
    main()
