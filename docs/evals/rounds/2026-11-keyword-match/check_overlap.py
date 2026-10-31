#!/usr/bin/env python3
"""List the content words a question shares with its target passage.

Reads targets.json (passage locations) and questions.json (the A and B
questions), and for every question prints the content words it shares with
its passage. A (B) question passes only when that list is empty.

Matching is deliberately loose, so it errs towards finding overlap:
- text is lowercased, line-break hyphens are joined ("fric-\\ntion" -> "friction"),
  and hyphenated or slashed words are split;
- function words (STOP below) are dropped; every other word counts as content;
- each word is reduced by stripping common English suffixes;
- two words match when their reduced forms are equal, or when both are at
  least 5 letters and share their first 5 letters ("deviation" ~ "deviance").

It also lists, for information only, the words each question shares with the
whole target section (the unit a citation is scored against). That list doesn't
gate anything: a section of hundreds of lines shares some words with almost any
question.

Usage: python3 check_overlap.py [--passages]   (--passages also prints each passage)
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CONVERTED = ROOT / "corpus.commons/demo/sources/converted"

STOP = set("""
a about above after again against all also am an and any are as at be because been before being below
between both but by can could did do does doing down during each either else ever every few for from
further had has have having he her here hers herself him himself his how i if in into is it its itself
just me might more most must my myself neither no nor not now of off often on once only or other our
ours ourselves out over own per quite rather really same shall she should so some such than that the
their theirs them themselves then there these they this those through thus to too under until up upon
us very was we were what when where whether which while who whom whose why will with within without
would yet you your yours yourself yourselves s t d ll m re ve don doesn didn isn aren wasn weren won
wouldn couldn shouldn hasn haven hadn can't let's one's
""".split())

SUFFIXES = ["ational", "ization", "isation", "fulness", "iveness", "ousness", "ments", "ement", "ment",
            "ness", "ings", "ing", "ions", "ion", "ities", "ity", "ally", "ies", "ied", "ers", "er",
            "ed", "es", "ly", "s"]


def reduce(w):
    for suf in SUFFIXES:
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: -len(suf)]
    return w


def words(text):
    text = re.sub(r"-\s*\n\s*", "", text.lower())
    text = text.replace("’", "'").replace("‘", "'")
    toks = re.findall(r"[a-z]+(?:'[a-z]+)?", text)
    out = []
    for t in toks:
        t = t.split("'")[0] if t.endswith(("'s", "'t", "'re", "'ve", "'ll", "'d", "'m")) else t
        if t and t not in STOP and len(t) > 1:
            out.append(t)
    return out


def match(a, b):
    ra, rb = reduce(a), reduce(b)
    if ra == rb:
        return True
    return len(a) >= 5 and len(b) >= 5 and a[:5] == b[:5]


def shared(question, passage):
    pw = sorted(set(words(passage)))
    hits = {}
    for q in sorted(set(words(question))):
        m = [p for p in pw if match(q, p)]
        if m:
            hits[q] = m
    return hits


def section_text(t):
    lines = (CONVERTED / f"{t['slug']}.md").read_text().split("\n")
    return "\n".join(lines[t["section"]["start"] - 1 : t["section"]["end"]])


def passage_text(t):
    # split on "\n" only, so line numbers match grep -n and sed (splitlines also breaks on \f and  )
    lines = (CONVERTED / f"{t['slug']}.md").read_text().split("\n")
    return "\n".join(lines[t["start"] - 1 : t["end"]])


def main():
    targets = {t["id"]: t for t in json.loads((HERE / "targets.json").read_text())}
    questions = json.loads((HERE / "questions.json").read_text())
    fails = 0
    for q in questions:
        t = targets[q["target"]]
        ptxt = passage_text(t)
        if "--passages" in sys.argv and q["form"] == "A":
            print(f"\n----- {t['id']} {t['slug']}.md:{t['start']}-{t['end']}\n{ptxt}\n-----")
        hits = shared(q["question"], ptxt)
        verdict = "-" if q["form"] == "A" else ("PASS" if not hits else "FAIL")
        if q["form"] == "B" and hits:
            fails += 1
        listed = "; ".join(f"{k} ~ {','.join(v)}" for k, v in hits.items()) or "(none)"
        sec = shared(q["question"], section_text(t))
        print(f"{q['id']:6} {verdict:4}  shared: {listed}")
        print(f"{'':11} section ({t['section']['end'] - t['section']['start'] + 1} lines), informational: "
              f"{', '.join(sorted(sec)) or '(none)'}")
    print(f"\n(B) questions with shared content words: {fails}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
