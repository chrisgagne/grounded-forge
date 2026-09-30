"""Build blind judging packets: one folder per question with two unlabelled answers.

Trace footers are stripped (they name the index route and would unblind the
judge); X/Y order is random per question and recorded only in judge-key.json.
Usage: python3 build_packets.py
"""
import json
import random
import re
import shutil
from pathlib import Path

here = Path(__file__).parent
QUESTIONS = {
    "Q1": "Our leadership team keeps reopening decisions we already made: every meeting relitigates last month's choices. How do we make decisions stick without shutting down legitimate dissent?",
    "Q2": "What does the library say about making decisions under uncertainty and complexity?",
    "Q3": "What is the Agreement/Uncertainty Matrix, and when should I use it?",
    "Q4": "When a company makes a big decision, should it put shareholders first or weigh all stakeholders? Where do the sources disagree?",
}
RUBRIC = """# Rubric

Two answers to the same question, X and Y, written by an assistant answering from a
library of sources. The folder `distillations/` holds the source material both answers
drew on: every substantive claim should trace to it.

Score each answer 1 to 5 on:

- **Grounding.** Every substantive claim traces to the distillations; attributions name
  the right source; quoted text is really in the distillations. Check the claims that
  carry the answer, and list any you can't find support for.
- **Coverage.** Addresses every part of the question. For a question about disagreement,
  it names where the sources actually disagree.
- **Precision.** Stays on the question; the sources it uses are relevant; no padding.
- **Usefulness.** A practitioner asking this could act on it or learn from it.

Then pick the better answer overall, or call a tie if neither is clearly better.
Judge only what is on the page; length is not a virtue in itself.
"""


def strip_trace(text: str) -> str:
    lines = text.rstrip().splitlines()
    for i, line in enumerate(lines):
        if line.lstrip().startswith("*Trace") or line.lstrip().startswith("Trace ["):
            cut = i
            if cut > 0 and lines[cut - 1].strip() == "---":
                cut -= 1
            return "\n".join(lines[:cut]).rstrip() + "\n"
    return text


rng = random.Random(20260930)
key = {}
distillations = here / "arm-p/corpus.commons/demo/apps/decision/distillations/decision-making"
for q, question in QUESTIONS.items():
    answers = {arm: json.load(open(here / f"runs/arm-{arm}-{q}.json"))["answer"] for arm in ("p", "q")}
    order = ["p", "q"]
    rng.shuffle(order)
    key[q] = {"X": order[0], "Y": order[1]}
    out = here / f"judge/{q}"
    out.mkdir(parents=True, exist_ok=True)
    (out / "question.md").write_text(f"# Question\n\n{question}\n")
    (out / "rubric.md").write_text(RUBRIC)
    for label, arm in (("X", order[0]), ("Y", order[1])):
        body = strip_trace(answers[arm])
        if re.search(r"topic|t0\d\d|concept-index|schema", body, re.I):
            print(f"  note: {q} answer {label} mentions index mechanics in its body")
        (out / f"answer-{label}.md").write_text(f"# Answer {label}\n\n{body}")
    if not (out / "distillations").exists():
        shutil.copytree(distillations, out / "distillations")
json.dump(key, open(here / "judge-key.json", "w"), indent=1)
print("packets written for", ", ".join(QUESTIONS))
