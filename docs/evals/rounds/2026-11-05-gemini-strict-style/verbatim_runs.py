#!/usr/bin/env python3
"""How much of an answer is the sources' own words, quoted or not.

    python3 verbatim_runs.py ANSWER.txt

Splits the answer's prose into sentences (headings, source chips and "My inference:"
sentences set aside), and for each sentence of 8 words or more finds the longest run of
consecutive words that also appears in one converted demo source, after normalising case,
punctuation, quotation marks, dashes and line-break hyphens. A sentence counts as copied
when that run covers 90% or more of its words. Prints counts, split by whether the sentence
sits inside quotation marks.
"""
import re, sys, glob, os

HERE = os.path.dirname(os.path.abspath(__file__))
CONV = os.path.join(HERE, "../../../../corpus.commons/demo/sources/converted")


def words(t):
    t = t.replace("­", "")
    t = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", t)
    t = t.lower().replace("’", "'").replace("‘", "'")
    return re.findall(r"[a-z0-9']+", t)


sources = {}
for p in glob.glob(os.path.join(CONV, "*.md")):
    w = words(open(p, encoding="utf-8", errors="ignore").read())
    sources[os.path.basename(p)[:-3]] = " " + " ".join(w) + " "


def copied_from(ws):
    """The source holding a run of at least 90% of the sentence's words, or None."""
    m = -(-9 * len(ws) // 10)
    for i in range(len(ws) - m + 1):
        frag = " " + " ".join(ws[i:i + m]) + " "
        for name, txt in sources.items():
            if frag in txt:
                return name
    return None


text = open(sys.argv[1], encoding="utf-8").read()
text = re.sub(r"\[CHIP:[^\]]*\]", "\n", text)
paras = [p for p in text.split("\n") if len(p.split()) >= 12]
sents = []
for p in paras:
    for s in re.split(r"(?<=[.!?])[”\"']?\s+(?=[A-Z“\"])", p):
        if len(s.split()) >= 8 and not s.startswith("My inference"):
            sents.append(s)
copied = {"quoted": 0, "unquoted": 0}
total = {"quoted": 0, "unquoted": 0}
examples = []
for s in sents:
    ws = words(s)
    if len(ws) < 8:
        continue
    kind = "quoted" if re.search(r"[“\"][^”\"]{20,}[”\"]", s) else "unquoted"
    src = copied_from(ws)
    total[kind] += 1
    if src:
        copied[kind] += 1
        if kind == "unquoted" and len(examples) < 5:
            examples.append((src, s[:110]))
n = sum(total.values())
print(f"sentences of 8+ words (inferences set aside): {n}")
for k in ("unquoted", "quoted"):
    print(f"  {k}: {total[k]}, of which copied word for word from a source (90%+ of words): {copied[k]}")
for src, s in examples:
    print(f"  e.g. [{src}] {s}")

quotes = [q for q in re.findall(r"[“\"]([^”\"]{20,})[”\"]", text) if len(words(q)) >= 5]
found = sum(1 for q in quotes if (" " + " ".join(words(q)) + " ") in "".join(sources.values()))
print(f"quotations of 5+ words: {len(quotes)}, found word for word in a source: {found}")
