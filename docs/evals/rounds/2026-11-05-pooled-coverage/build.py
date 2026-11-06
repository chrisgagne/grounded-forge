"""Blind-label every answer to a case, from every arm, for pooled coverage.

    python3 build.py OUT_DIR LABELS_JSON demo|aarbuddy

Arms: Gemini chat at default style, Gemini chat under the strict style, Gemini as asked
(a Studio report or a chat answer), grounded-forge answer-from-corpus, and verbatim mode
rounds 3 and 3b. Citation markers and pointer blocks are stripped; labels are shuffled.
"""
import json, re, random, os, sys
GF = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
CC = f"{GF}/docs/evals/rounds/2026-11-case-citations"
CCP = f"{GF}/corpus.local/aarbuddy/projects/case-citations-private"
VB = f"{GF}/corpus.local/aarbuddy/projects/verbatim-reports"
out, labels_path, corpus = sys.argv[1:4]
CASES = {"demo": ("C1", "C2"), "aarbuddy": ("C1", "C2", "C3")}[corpus]
def strip_markers(t): return re.sub(r"\s*\[\d+(?::[^\]]*)?\]", "", t).replace("Thoughts\nexpand_more\n", "").strip()
def verbatim(p):
    t = open(p).read().split("\n", 1)[1]
    t = re.sub(r"^Question:.*?\n\n", "", t, count=1, flags=re.S)
    t = re.sub(r"\nPointers:\n.*?(?=\n## |\n[^\s\[].*\n\nPointers:|\Z)", "\n", t, flags=re.S)
    t = re.sub(r"\nPointers:\n(?:(?:    |\[).*\n?|\n)*", "\n", t)
    return re.sub(r"\s*\[\d+\]", "", t).strip()
def gem_packet(p):
    t = open(p).read().split("## Chat answer", 1)[1].split("## Citation legend", 1)[0]
    if "### Studio report" in t:
        t = "\n\n".join(re.sub(r"^.*?\n\n\(citation markers in the report: [^)]*\)\n\n", "", s, flags=re.S) for s in t.split("### Studio report: ")[1:])
    return strip_markers(t)
def gem_json(p):
    j = json.load(open(p)); rep = "\n\n".join(r["text"] for r in j.get("reports", []))
    return strip_markers(rep or j["text"])
cases = {c["id"]: c["prompt"] for c in json.load(open(f"{CC}/cases.json"))}
conv = f"{GF}/corpus.commons/demo/sources/converted" if corpus == "demo" else f"{GF}/corpus.local/aarbuddy/sources/converted"
labels = json.load(open(labels_path)) if os.path.exists(labels_path) else {}
brief = open(os.path.join(os.path.dirname(__file__), "brief.md")).read()
for case in CASES:
    items = []
    for run in ("1", "2"):
        if corpus == "demo":
            items.append(("gemini-default-chat", run, gem_json(f"{CC}/runs/gemini/demo-{case}-{run}-chat.json")))
            items.append(("gemini-strict-chat", run, gem_json(f"{GF}/docs/evals/rounds/2026-11-05-gemini-strict-style/runs/gf-cc-demo-{case}-{run}-strict.json")))
            items.append(("gemini-as-asked", run, gem_json(f"{CC}/runs/gemini/demo-{case}-{run}.json")))
        else:
            items.append(("gemini-default-chat", run, gem_packet(f"{CCP}/cc-packets-private/gemini-aarbuddy-{case}-{run}-chat.md")))
            items.append(("gemini-strict-chat", run, gem_json(f"{CCP}/strict-private/runs/gf-cc-aarbuddy-{case}-{run}-strict.json")))
            items.append(("gemini-as-asked", run, gem_packet(f"{CCP}/cc-packets-private/gemini-aarbuddy-{case}-{run}.md")))
        pk = open(f"{CCP}/cc-packets/gf-{corpus}-{case}-{run}.md").read().split("## Answer", 1)[1].split("## Quotation locations", 1)[0]
        items.append(("gf-answer-from-corpus", run, pk.strip()))
        for rnd, arm in (("round3", "gf-verbatim-r3"), ("round3b", "gf-verbatim-r3b")):
            p = f"{VB}/{rnd}/{corpus}-{case}-{run}/answer.md"
            if os.path.exists(p): items.append((arm, run, verbatim(p)))
    random.seed(f"pool2-{corpus}-{case}"); random.shuffle(items)
    d = f"{out}/{case}"; os.makedirs(f"{d}/answers", exist_ok=True)
    letters = [chr(65 + i) for i in range(len(items))]
    for lab, (arm, run, text) in zip(letters, items):
        open(f"{d}/answers/{lab}.md", "w").write(f"# Answer {lab}\n\n{text}\n")
        labels[f"{corpus}-{case}-{lab}"] = {"arm": arm, "run": run, "words": len(text.split())}
    open(f"{d}/question.md", "w").write(f"# Question\n\n{cases[case]}\n\nConverted sources: {conv}\n")
    open(f"{d}/brief.md", "w").write(brief.replace("ten answers to it (`answers/A.md` to `answers/J.md`)", f"{len(items)} answers to it (`answers/A.md` to `answers/{letters[-1]}.md`)").replace("all ten answers", "all the answers"))
    print(corpus, case, len(items), "answers")
json.dump(labels, open(labels_path, "w"), indent=1)
