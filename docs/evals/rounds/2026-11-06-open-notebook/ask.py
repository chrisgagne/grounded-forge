#!/usr/bin/env python3
"""Ask Open Notebook the case-citations public cases in Ask mode, Opus 5.5 for every model role.

    python3 ask.py NOTEBOOK_ID MODEL_ID [CASE-RUN ...]

The strict style is pasted at the top of each question, as it was for Gemini 4 Argon.
Writes runs/demo-{case}-{run}.json with the question, the answer and the timing.
"""
import json, os, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
CC = os.path.join(HERE, "../2026-11-case-citations/cases.json")
STYLE = open(os.path.join(HERE, "../2026-11-05-gemini-strict-style/style.txt")).read().strip()
nb, model = sys.argv[1:3]
which = sys.argv[3:] or ["C1-1", "C1-2", "C2-1", "C2-2"]
cases = {c["id"]: c["prompt"] for c in json.load(open(CC))}
for cr in which:
    case = cr.split("-")[0]
    q = "Instructions for this answer: " + STYLE + "\n\n" + cases[case] + "\n\nAnswer here in the chat."
    body = json.dumps({"notebook_id": nb, "question": q, "strategy_model": model, "answer_model": model, "final_answer_model": model}).encode()
    t = time.time()
    req = urllib.request.Request("http://127.0.0.1:5055/api/search/ask/simple", body, {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=1800))
    out = {"id": f"opennotebook-demo-{cr}", "question": q, "answer": r.get("answer"), "seconds": round(time.time() - t), "notebook": nb, "model": model}
    json.dump(out, open(os.path.join(HERE, "runs", f"demo-{cr}.json"), "w"), indent=1)
    print(cr, out["seconds"], "s,", len((out["answer"] or "").split()), "words", flush=True)
