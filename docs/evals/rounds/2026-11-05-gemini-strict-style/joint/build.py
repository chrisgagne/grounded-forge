import json, glob, collections, os, re, random, sys
random.seed(7)
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
FAM = sys.argv[1] if len(sys.argv) > 1 else "sol"
BRIEF = open(os.path.join(HERE, "brief.md")).read()
manifest = {}
for f in sorted(glob.glob(f"{ROOT}/work/{FAM}/gemini-*/gemini-*.score.json")):
    aid = os.path.basename(f)[:-11]
    j = json.load(open(f)); cits = j.get("citations", [])
    if not cits: continue
    pk = None
    for d in ("packets",):
        p = f"{ROOT}/{d}/{aid}.md"
        if os.path.exists(p): pk = open(p).read(); break
    answer = pk.split("## Chat answer", 1)[1].split("## Citation legend", 1)[0]
    leg_txt = pk.split("## Citation legend (full chunk text per marker)", 1)[1].split("## Quotation locations", 1)[0]
    legend = {}
    for m in re.finditer(r"^\[(\d+)\] ([^\n]*)\n(.*?)(?=^\[\d+\] |\Z)", leg_txt, re.S | re.M):
        legend[m.group(1)] = (m.group(2), m.group(3).strip())
    by = collections.OrderedDict()
    for c in cits: by.setdefault(c["claim"].strip(), []).append(c)
    items, mid, ctrl = [], [], []
    for claim, cs in by.items():
        s = [c["support"] for c in cs]
        if "supports" not in s and len(cs) > 1 and "partial" in s: mid.append(claim)
        elif len(cs) == 1 and s[0] in ("supports", "partial"): ctrl.append(claim)
    ctrl = random.sample(ctrl, min(6, len(ctrl)))
    keep = [c for c in by if c in mid or c in ctrl]
    out = []
    for i, claim in enumerate(keep, 1):
        ns = [c["n"] for c in by[claim]]
        block = f"### S{i}\n\nSentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers {', '.join('['+n+']' for n in ns)}):\n> {claim}\n\nMarkers on it:\n"
        for n in ns:
            slug, chunk = legend.get(n, ("", "(no chunk captured)"))
            block += f"\n[{n}] source: {slug or '(none)'}\n{chunk or '(empty chunk)'}\n"
        out.append(block)
        manifest[f"{aid}#S{i}"] = {"claim": claim, "markers": ns, "set": "stacked" if claim in mid else "control", "per_marker": [c["support"] for c in by[claim]]}
    wd = f"{HERE}/{FAM}-base/{aid}"; os.makedirs(wd, exist_ok=True)
    open(f"{wd}/brief.md", "w").write(BRIEF)
    open(f"{wd}/packet.md", "w").write(f"# {aid}\n\n## The whole answer, for context\n{answer}\n## Sentences to grade\n\n" + "\n".join(out))
    print(aid, len(keep), "sentences", f"({len(mid)} stacked, {len(ctrl)} control)")
json.dump(manifest, open(f"{HERE}/manifest-{FAM}.json", "w"), indent=1)
