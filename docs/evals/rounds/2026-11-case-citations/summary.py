#!/usr/bin/env python3
"""Rebuild the README's numbers from the committed score files.

    python3 summary.py [SCORES_DIR]

Reads every *.score.json (default: scores/) and prints, per arm, corpus and
case, pooled over runs: citations graded, the share graded none (U, the
pre-registered reading's number), partial and supports; wrong-book citations;
quotations exact; expected ideas present and credited to a source that carries
them; distinct sources cited per answer.
"""
import collections, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def pct(a, b):
    return f"{a / b:.0%}" if b else "-"


def main():
    d = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "scores"
    groups = collections.defaultdict(list)
    for f in sorted(d.glob("*.score.json")):
        s = json.loads(f.read_text())
        arm, corpus, case, run = s["id"].split("-")
        groups[(arm, corpus, case)].append(s)
    print("arm\tcorpus\tcase\truns\tcitations\tnone (U)\tpartial\tsupports\twrong book\tquotes exact/with\tideas present\tideas credited ok\tsources/answer")
    for (arm, corpus, case), runs in sorted(groups.items()):
        c = [x for s in runs for x in s["citations"]]
        n = len(c)
        sup = collections.Counter(x["support"] for x in c)
        wb = sum(x["wrong_book"] == "yes" for x in c)
        q = [x for x in c if x.get("quote_exact")]
        qe = sum(x["quote_exact"] == "yes" for x in q)
        ideas = [i for s in runs for i in s.get("ideas", [])]
        ip = sum(i["present"] == "yes" for i in ideas)
        ic = sum(i["credited_ok"] == "yes" for i in ideas)
        src = sum(s["sources_cited"] for s in runs) / len(runs)
        print(f"{arm}\t{corpus}\t{case}\t{len(runs)}\t{n}\t{sup['none']} ({pct(sup['none'], n)})\t{sup['partial']} ({pct(sup['partial'], n)})"
              f"\t{sup['supports']} ({pct(sup['supports'], n)})\t{wb}\t{qe}/{len(q)}\t{ip}/{len(ideas) or '-'}\t{ic}/{len(ideas) or '-'}\t{src:.1f}")


if __name__ == "__main__":
    main()
