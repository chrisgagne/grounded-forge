"""Per-question mechanics for both arms: tokens, distillations read, overlap."""
import json
from pathlib import Path

here = Path(__file__).parent
tokens = json.load(open(here / "tokens.json"))
arms = {"p": "schema 2 (today)", "q": "schema 3 (topics)"}
print(f"{'Q':3s} {'arm':18s} {'tokens':>8s} {'distillations':>14s}")
totals = {"p": 0, "q": 0}
for q in ("Q1", "Q2", "Q3", "Q4"):
    read = {}
    for arm in ("p", "q"):
        rec = json.load(open(here / f"runs/arm-{arm}-{q}.json"))
        dist = {Path(d).name for d in rec.get("distillations_read", [])}
        read[arm] = dist
        t = tokens[f"arm-{arm}-{q}"]
        totals[arm] += t
        print(f"{q:3s} {arms[arm]:18s} {t:8d} {len(dist):14d}")
    both, only_p, only_q = read["p"] & read["q"], read["p"] - read["q"], read["q"] - read["p"]
    print(f"    shared {len(both)} | only today: {sorted(d.split('-decision-making')[0] for d in only_p)}"
          f" | only topics: {sorted(d.split('-decision-making')[0] for d in only_q)}")
print(f"total tokens: today {totals['p']}, topics {totals['q']} ({100 * (totals['q'] - totals['p']) / totals['p']:+.0f}%)")
