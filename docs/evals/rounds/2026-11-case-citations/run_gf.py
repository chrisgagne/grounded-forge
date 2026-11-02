#!/usr/bin/env python3
"""grounded-forge arm: one case prompt through answer-from-corpus in project mode, over a named corpus.

Each run gets a fresh copy of the corpus's reference tier (references, converted
sources, concept and reference indexes, lens index and specs) plus the
answer-from-corpus skill, outside this repo so no repo CLAUDE.md loads. No
distillations, task indexes or apps travel. claude -p runs isolated, as the
October and keyword-match rounds did: Opus 5.5 at effort high, project and
local settings only, auto-memory off, an empty MCP config, no Bash and no web.

    python3 run_gf.py template demo|aarbuddy      # build that corpus's template once
    python3 run_gf.py demo C1 1                   # corpus, case id, run number

Writes RUNS/{corpus}-{case}-{run}.out/: prompt.txt, stream.jsonl, answer.md,
usage.json, tools.json, and written/ for any file the run wrote. RUNS defaults
to /Users/Shared/aar-ab-runs/case-citations (override with CC_RUNS).
"""
import json, os, shutil, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
GF = HERE.parents[3]
# corpus.local is gitignored, so a worktree has none; fall back to the main checkout three levels up
MAIN = GF.parents[2] if (GF.parents[2] / "corpus.local/aarbuddy").exists() else GF
CORPORA = {"demo": GF / "corpus.commons/demo", "aarbuddy": MAIN / "corpus.local/aarbuddy"}
RUNS = Path(os.environ.get("CC_RUNS", "/Users/Shared/aar-ab-runs/case-citations"))
EMPTY_MCP = RUNS / "empty-mcp.json"

CLAUDE_MD = """# {corpus} corpus (project mode)

This folder holds the grounded-forge {corpus} corpus: references in `references/`, converted sources in `sources/converted/`, and the concept and reference indexes.
For any substantive question, use the `answer-from-corpus` skill.
"""


def template(corpus):
    t = RUNS / f"_template-{corpus}"
    if t.exists():
        return t
    src = CORPORA[corpus]
    t.mkdir(parents=True)
    # cp -c clones on APFS, so a 1 GB corpus costs no space and no time
    subprocess.run(["cp", "-cR", str(src / "references"), str(t / "references")], check=True)
    shutil.rmtree(t / "references/_audit", ignore_errors=True)
    (t / "sources").mkdir()
    subprocess.run(["cp", "-cR", str(src / "sources/converted"), str(t / "sources/converted")], check=True)
    subprocess.run(["cp", "-cR", str(src / "lenses"), str(t / "lenses")], check=True)
    for f in ["concept-index.json", "concept-index-deep.json", "reference-index.json", "lens-index.json"]:
        if (src / f).exists():
            shutil.copy(src / f, t / f)
    shutil.copytree(GF / ".claude/skills/answer-from-corpus", t / ".claude/skills/answer-from-corpus")
    (t / "CLAUDE.md").write_text(CLAUDE_MD.format(corpus=corpus))
    EMPTY_MCP.write_text('{"mcpServers": {}}\n')
    return t


def env():
    keep = {k: os.environ[k] for k in ("HOME", "USER", "LOGNAME", "LANG", "TERM", "TMPDIR") if k in os.environ}
    keep["PATH"] = f"/usr/bin:/bin:/usr/sbin:/sbin:{Path.home()}/.local/bin"
    keep["SHELL"] = "/bin/zsh"
    return keep


def prompt(case):
    return next(c["prompt"] for c in json.loads((HERE / "cases.json").read_text()) if c["id"] == case)


def run(corpus, case, rep):
    t = template(corpus)
    d = RUNS / f"{corpus}-{case}-{rep}"
    if d.exists():
        sys.exit(f"{d} exists")
    subprocess.run(["cp", "-cR", str(t), str(d)], check=True)
    out = RUNS / f"{corpus}-{case}-{rep}.out"
    out.mkdir(exist_ok=True)
    p = prompt(case)
    (out / "prompt.txt").write_text(p)
    flags = ["claude", "-p", p, "--output-format", "stream-json", "--verbose",
             "--model", "claude-opus-5-5", "--effort", "high",
             "--setting-sources", "project,local", "--settings", json.dumps({"autoMemoryEnabled": False}),
             "--strict-mcp-config", "--mcp-config", str(EMPTY_MCP),
             "--tools", "Read,Grep,Glob,Write,Skill,Agent", "--disallowedTools", "Bash,WebSearch,WebFetch",
             "--permission-mode", "acceptEdits", "--no-chrome"]
    t0 = time.time()
    with open(out / "stream.jsonl", "w") as log:
        r = subprocess.run(flags, cwd=d, env=env(), stdout=log, stderr=subprocess.PIPE, text=True, timeout=5400)
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
    shutil.rmtree(d)
    print(corpus, case, rep, "rc", r.returncode, "wall", round(wall), "cost", (usage or {}).get("total_cost_usd"))


if __name__ == "__main__":
    if sys.argv[1] == "template":
        print(template(sys.argv[2]))
    else:
        run(sys.argv[1], sys.argv[2], sys.argv[3])
