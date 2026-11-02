#!/usr/bin/env python3
"""Rebuild the README's numbers from the committed run records and scores.

    python3 summary.py

Mechanical: for Gemini, from runs/gemini/*.located.json (each citation chunk
located in the converted text); for grounded-forge, from scores/gf-quotes.txt
(quotes.py: quotations found inside the target section). Judged: from
scores/gemini.json and scores/gf.json (the scoring brief's strict and lenient
readings).
"""
import collections, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = [f"K{k:02d}{form}-{r}" for k in range(1, 11) for form in "AB" for r in (1, 2)]


def both(pred, form):
    return sum(pred(f"K{k:02d}{form}-1") and pred(f"K{k:02d}{form}-2") for k in range(1, 11))


def main():
    loc = {i: [c["verdict"] for c in json.loads((HERE / f"runs/gemini/{i}.located.json").read_text()).values()]
           for i in RUNS}
    gfq = {}
    for line in (HERE / "scores/gf-quotes.txt").read_text().splitlines():
        m = re.match(r"(K\d\d[AB]-\d)\.out/answer\.md: (\d+) quotations, (\d+) exact, (\d+) in target section", line)
        gfq[m.group(1)] = int(m.group(4))
    gfq["K09A-2"] = max(gfq["K09A-2"], 1)  # its two blockquotes carry no quote marks; the first is the target passage itself (1169-1173)

    print("## Mechanical: target section cited anywhere in the answer")
    for form in "AB":
        ids = [i for i in RUNS if i[3] == form]
        g = sum("IN" in loc[i] for i in ids)
        f = sum(gfq[i] > 0 for i in ids)
        print(f"{form}: Gemini {g}/20 runs, {both(lambda i: 'IN' in loc[i], form)}/10 targets both runs; "
              f"grounded-forge {f}/20 runs, {both(lambda i: gfq[i] > 0, form)}/10")

    print("\n## Gemini citation mix")
    for form in "AB":
        ids = [i for i in RUNS if i[3] == form]
        c = collections.Counter(v for i in ids for v in loc[i])
        n = sum(c.values())
        print(f"{form}: {n} citations, {n / 20:.1f} per answer; " + ", ".join(f"{k} {v} ({v / n:.0%})" for k, v in c.most_common()))
    for grp, ks in (("small files (K04 K05 K09 K10)", (4, 5, 9, 10)), ("large files (K01 K02 K03 K06 K07 K08)", (1, 2, 3, 6, 7, 8))):
        for form in "AB":
            ids = [f"K{k:02d}{form}-{r}" for k in ks for r in (1, 2)]
            c = collections.Counter(v for i in ids for v in loc[i])
            n = sum(c.values())
            print(f"{grp} {form}: IN {c['IN'] / n:.0%}, OTHER {c['OTHER'] / n:.0%}")

    print("\n## Judged")
    for arm, f in (("Gemini", "gemini"), ("grounded-forge", "gf")):
        d = {x["id"]: x for x in json.loads((HERE / f"scores/{f}.json").read_text())}
        for form in "AB":
            ids = [i for i in RUNS if i[3] == form]
            yes = lambda k: (lambda i: d[i][k] == "yes")
            print(f"{arm} {form}: strict s1 {sum(map(yes('s1'), ids))}/20 ({both(yes('s1'), form)}/10 both runs); "
                  f"s2 {sum(map(yes('s2'), ids))}/20; lenient s1 {sum(map(yes('s1_lenient'), ids))}/20 "
                  f"({both(yes('s1_lenient'), form)}/10); s4 key hit {sum(map(yes('s4'), ids))}/20; "
                  f"wrong-book credits on key sentence {sum(d[i]['s3'] for i in ids)}; "
                  f"no key sentence {sum(d[i]['key_sentence'] is None for i in ids)}; "
                  f"quotations exact {sum(d[i]['quotes_exact'] for i in ids)}, inexact {sum(d[i]['quotes_inexact'] for i in ids)}")


if __name__ == "__main__":
    main()
