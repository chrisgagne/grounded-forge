"""Pooled coverage per arm: ideas each answer carries, and how many the library supports.

    python3 tally.py FAMILY
"""
import json, os, sys, collections
GF = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
L = json.load(open(f"{GF}/corpus.local/aarbuddy/projects/case-citations-private/pooled-labels.json"))
fam = sys.argv[1]
BASES = {"demo": (f"{os.path.dirname(os.path.abspath(__file__))}/work", ("C1", "C2")),
         "aarbuddy": (f"{GF}/corpus.local/aarbuddy/projects/case-citations-private/pooled-private", ("C1", "C2", "C3"))}
for corpus, (base, cases) in BASES.items():
    tot = collections.defaultdict(collections.Counter)
    for case in cases:
        p = f"{base}/{case}/{fam}/pool.json"
        if not os.path.exists(p): print(corpus, case, "no pool yet"); continue
        ideas = json.load(open(p))["ideas"]
        print(f"[{fam} {corpus} {case}] {len(ideas)} ideas, library {dict(collections.Counter(i['library'] for i in ideas))}")
        for k, v in L.items():
            c, cs, lab = k.split("-")
            if c != corpus or cs != case: continue
            mine = [i for i in ideas if lab in i["answers"]]
            t = tot[v["arm"]]
            t["answers"] += 1; t["words"] += v["words"]; t["ideas"] += len(mine)
            for g in ("supported", "partly", "unsupported"): t[g] += sum(i["library"] == g for i in mine)
    for a, t in sorted(tot.items()):
        n = t["answers"]
        print(f"  {corpus:8} {a:22} n={n:2} ideas {t['ideas']/n:5.1f}  supported {t['supported']/n:5.1f}  partly {t['partly']/n:4.1f}  unsupported {t['unsupported']/n:4.1f}  words {t['words']/n:5.0f}  supported/1k words {1000*t['supported']/t['words']:4.1f}")
