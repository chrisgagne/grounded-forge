#!/usr/bin/env python3
"""grounded-forge arm: one bare question through answer-from-corpus in project mode.

Each run gets a fresh copy of the demo corpus's reference tier (references,
converted sources, concept and reference indexes, lens index and specs) plus the
answer-from-corpus skill, outside this repo so no repo CLAUDE.md loads. No
distillations, task indexes or apps travel. claude -p runs isolated, as the
October round's Q10-on runs did: Opus 5.5 at effort high, project and local
settings only, auto-memory off, an empty MCP config, no Bash and no web.

    python3 run_gf.py template            # build the template once
    python3 run_gf.py K01B 1              # question id, run number

Writes RUNS/{qid}-{run}.out/: prompt.txt, stream.jsonl, answer.md, usage.json, tools.json.
RUNS defaults to /Users/Shared/aar-ab-runs/keyword-match (override with KM_RUNS).
"""
import json, os, shutil, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
GF = HERE.parents[3]
DEMO = GF / "corpus.commons/demo"
RUNS = Path(os.environ.get("KM_RUNS", "/Users/Shared/aar-ab-runs/keyword-match"))
EMPTY_MCP = RUNS / "empty-mcp.json"

CLAUDE_MD = """# demo corpus (project mode)

This folder holds the grounded-forge demo corpus: references in `references/`, converted sources in `sources/converted/`, and the concept and reference indexes.
For any substantive question, use the `answer-from-corpus` skill.
"""


def template():
    t = RUNS / "_template"
    if t.exists():
        return t
    t.mkdir(parents=True)
    shutil.copytree(DEMO / "references", t / "references", ignore=shutil.ignore_patterns("_audit", ".DS_Store"))
    (t / "sources").mkdir()
    shutil.copytree(DEMO / "sources/converted", t / "sources/converted", ignore=shutil.ignore_patterns(".DS_Store"))
    shutil.copytree(DEMO / "lenses", t / "lenses", ignore=shutil.ignore_patterns(".DS_Store"))
    for f in ["concept-index.json", "concept-index-deep.json", "reference-index.json", "lens-index.json"]:
        shutil.copy(DEMO / f, t / f)
    shutil.copytree(GF / ".claude/skills/answer-from-corpus", t / ".claude/skills/answer-from-corpus")
    (t / "CLAUDE.md").write_text(CLAUDE_MD)
    EMPTY_MCP.write_text('{"mcpServers": {}}\n')
    return t


def env():
    keep = {k: os.environ[k] for k in ("HOME", "USER", "LOGNAME", "LANG", "TERM", "TMPDIR") if k in os.environ}
    keep["PATH"] = f"/usr/bin:/bin:/usr/sbin:/sbin:{Path.home()}/.local/bin"
    keep["SHELL"] = "/bin/zsh"
    return keep


def question(qid):
    return next(q["question"] for q in json.loads((HERE / "questions.json").read_text()) if q["id"] == qid)


def run(qid, rep):
    t = template()
    d = RUNS / f"{qid}-{rep}"
    if d.exists():
        sys.exit(f"{d} exists")
    subprocess.run(["cp", "-cR", str(t), str(d)], check=True)
    out = RUNS / f"{qid}-{rep}.out"
    out.mkdir(exist_ok=True)
    p = question(qid)
    (out / "prompt.txt").write_text(p)
    flags = ["claude", "-p", p, "--output-format", "stream-json", "--verbose",
             "--model", "claude-opus-5-5", "--effort", "high",
             "--setting-sources", "project,local", "--settings", json.dumps({"autoMemoryEnabled": False}),
             "--strict-mcp-config", "--mcp-config", str(EMPTY_MCP),
             "--tools", "Read,Grep,Glob,Write,Skill,Agent", "--disallowedTools", "Bash,WebSearch,WebFetch",
             "--permission-mode", "acceptEdits", "--no-chrome"]
    t0 = time.time()
    with open(out / "stream.jsonl", "w") as log:
        r = subprocess.run(flags, cwd=d, env=env(), stdout=log, stderr=subprocess.PIPE, text=True, timeout=3600)
    wall = time.time() - t0
    result, usage, tools = None, None, []
    for line in open(out / "stream.jsonl"):
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("type") == "result":
            result = e.get("result")
            usage = {k: e.get(k) for k in ("total_cost_usd", "usage", "num_turns", "duration_ms", "is_error", "modelUsage")}
        if e.get("type") == "assistant":
            for c in e.get("message", {}).get("content", []):
                if c.get("type") == "tool_use":
                    tools.append({"tool": c["name"], "input": c.get("input")})
    (out / "answer.md").write_text(result or "")
    (out / "usage.json").write_text(json.dumps({"wall_s": round(wall), "rc": r.returncode, "stderr": r.stderr[-2000:], **(usage or {})}, indent=2))
    (out / "tools.json").write_text(json.dumps(tools, indent=1))
    new = subprocess.run(["find", str(d), "-newer", str(out / "prompt.txt"), "-type", "f"], capture_output=True, text=True).stdout.split("\n")
    for f in filter(None, new):
        (out / "written").mkdir(exist_ok=True)
        shutil.copy(f, out / "written" / Path(f).name)
    shutil.rmtree(d)  # what the run wrote is kept above; stream.jsonl keeps the trace
    print(qid, rep, "rc", r.returncode, "wall", round(wall), "cost", (usage or {}).get("total_cost_usd"))


if __name__ == "__main__":
    if sys.argv[1] == "template":
        print(template())
    else:
        run(sys.argv[1], sys.argv[2])
