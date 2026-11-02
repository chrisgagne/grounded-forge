#!/usr/bin/env python3
"""Compare Sol's score files against Opus's for the same packets.

    python3 compare_sol.py scores/sol scores PRIVATE_SCORES_DIR

SOL_DIR holds Sol's *.score.json (public ones in scores/sol/; private ones stay
outside the repo beside the private Opus scores). Per packet: each scorer's none/partial/supports shares and wrong-book count; then,
aligned by marker number and claim prefix where both graded the same citation,
per-citation agreement on support and on the none grade.
"""
import collections, json, sys
from pathlib import Path


def load(p):
    return json.loads(Path(p).read_text())


def shares(s):
    c = s["citations"]; n = len(c); k = collections.Counter(x["support"] for x in c)
    wb = sum(x["wrong_book"] == "yes" for x in c)
    return n, k, wb


def key(x):
    return (str(x.get("n", "")), " ".join(str(x.get("claim", "")).split())[:40].lower())


def main():
    sol, pub, priv = map(Path, sys.argv[1:4])
    print("packet\tscorer\tcitations\tnone\tpartial\tsupports\twrong book\tideas present/credited\tsources")
    tot = collections.Counter()
    for f in sorted(sol.glob("*.score.json")):
        d = f.with_name(f.name[: -len(".score.json")])
        a = load(f)
        o = next((p / f.name for p in (pub, priv) if (p / f.name).exists()), None)
        if o is None:
            print(f"{d.name}\topus\tMISSING"); continue
        b = load(o)
        for name, s in (("sol", a), ("opus", b)):
            n, k, wb = shares(s)
            ideas = s.get("ideas", [])
            ip = sum(i.get("present") == "yes" for i in ideas); ic = sum(i.get("credited_ok") == "yes" for i in ideas)
            pc = lambda v: f"{v} ({v / n:.0%})" if n else "-"
            print(f"{d.name}\t{name}\t{n}\t{pc(k['none'])}\t{pc(k['partial'])}\t{pc(k['supports'])}\t{wb}\t{ip}/{ic} of {len(ideas) or '-'}\t{s.get('sources_cited')}")
        # per-citation agreement
        ka = {key(x): x for x in a["citations"]}; kb = {key(x): x for x in b["citations"]}
        both = [k for k in ka if k in kb]
        if not both and len(a["citations"]) == len(b["citations"]):
            pairs = list(zip(a["citations"], b["citations"])); how = "by order"
        else:
            pairs = [(ka[k], kb[k]) for k in both]; how = "by marker+claim"
        agree = sum(x["support"] == y["support"] for x, y in pairs)
        none_agree = sum((x["support"] == "none") == (y["support"] == "none") for x, y in pairs)
        sol_stricter = sum(("none", "partial", "supports").index(x["support"]) < ("none", "partial", "supports").index(y["support"]) for x, y in pairs)
        opus_stricter = sum(("none", "partial", "supports").index(x["support"]) > ("none", "partial", "supports").index(y["support"]) for x, y in pairs)
        print(f"{d.name}\taligned {how}: {len(pairs)} pairs; support agreement {agree}/{len(pairs)}; none-vs-not agreement {none_agree}/{len(pairs)}; sol stricter {sol_stricter}, opus stricter {opus_stricter}")
        tot.update(pairs=len(pairs), agree=agree, none_agree=none_agree, sol_stricter=sol_stricter, opus_stricter=opus_stricter)
    print(f"\nALL: {tot['pairs']} pairs; support agreement {tot['agree']} ({tot['agree'] / max(tot['pairs'], 1):.0%}); none-vs-not agreement {tot['none_agree']} ({tot['none_agree'] / max(tot['pairs'], 1):.0%}); sol stricter {tot['sol_stricter']}, opus stricter {tot['opus_stricter']}")


if __name__ == "__main__":
    main()
