import json, glob, os, collections, sys
H = os.path.dirname(os.path.abspath(__file__))
for fam in ("opus", "sol"):
    c = collections.Counter(); wb = 0
    for f in sorted(glob.glob(f"{H}/work/{fam}/*/score.json")):
        t = open(f).read(); j = json.loads(t[t.find("{"): t.rfind("}") + 1])
        for s in j["sentences"]:
            c[s["support"]] += 1; wb += s.get("wrong_book") == "yes"
    n = sum(c.values())
    if n: print(fam, n, "cited sentences:", {k: f"{v} ({100*v/n:.0f}%)" for k, v in c.items()}, "wrong_book", wb)
