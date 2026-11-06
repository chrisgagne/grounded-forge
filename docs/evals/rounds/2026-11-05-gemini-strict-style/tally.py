"""Strict-style round against the default-style public chat runs, same method as the joint re-grade:
per marker (Sol first pass), per sentence by best single marker (Sol first pass), and per sentence with
stacked-partial sentences re-graded jointly (Sol and Opus)."""
import os as _os
GFROOT = _os.path.abspath(_os.path.join(_os.path.dirname(__file__), '../../../..'))
import json, glob, os, collections, sys
H = os.path.dirname(os.path.abspath(__file__))
DEF = GFROOT + "/corpus.local/aarbuddy/projects/case-citations-private"
def load(path):
    t = open(path).read(); t = t[t.find("{"): t.rfind("}") + 1]
    return {g["s"]: g["joint"] for g in json.loads(t)["grades"]}
def arm(score_files, manifest, jointdir, jointname):
    pm = collections.Counter(); best = collections.Counter(); joint = collections.Counter(); n_sent = 0
    for f in score_files:
        aid = os.path.basename(f)[:-11]
        cits = json.load(open(f)).get("citations", [])
        by = collections.OrderedDict()
        for c in cits: pm[c["support"]] += 1; by.setdefault(c["claim"].strip(), []).append(c["support"])
        res = load(f"{jointdir}/{aid}/{jointname}") if os.path.exists(f"{jointdir}/{aid}/{jointname}") else {}
        keys = {v["claim"]: k.split("#")[1] for k, v in manifest.items() if k.startswith(aid + "#") and v["set"] == "stacked"}
        for claim, s in by.items():
            b = "supports" if "supports" in s else "partial" if "partial" in s else "none"
            best[b] += 1; n_sent += 1
            joint[res.get(keys[claim], b) if claim in keys else b] += 1
    p = lambda c: f"{100 * c['supports'] / sum(c.values()):.0f}%"
    return {"markers": sum(pm.values()), "per_marker": p(pm), "sentences": n_sent, "best_marker": p(best), "joint": p(joint), "joint_n": joint["supports"]}
dman = json.load(open(f"{DEF}/joint/manifest.json"))
dfiles = sorted(glob.glob(f"{DEF}/sol-all/gemini-demo-C*-chat.score.json"))
sman = json.load(open(f"{H}/joint/manifest-sol.json"))
sfiles = sorted(glob.glob(f"{H}/work/sol/gemini-*/gemini-*.score.json"))
for fam, jn in (("sol", "result.json"), ("opus", "result-claude.json")):
    print("default", fam, arm(dfiles, dman, f"{DEF}/joint", jn))
    print("strict ", fam, arm(sfiles, sman, f"{H}/joint/sol-base", jn))
