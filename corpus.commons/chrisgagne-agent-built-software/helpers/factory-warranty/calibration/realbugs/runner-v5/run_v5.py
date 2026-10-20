"""PREREG-v5 runner: each arm reviews each case once, and its findings land in ReviewBench's judging format (part A) or
as a stop/no-stop record (part B).

  python run_v5.py a factory|vendors|pr-agent [--only rb01,rb02]
  python run_v5.py b factory|vendors|pr-agent [--only x01]

Paths come from the environment (defaults in brackets):
  RB_ROOT         the ReviewBench clone at 12e9d1a                    [<repos>/ReviewBench]
  RB_REPOS        clones of the review-bench mirrors                  [<repos>/reviewbench-repos]
  REALBUGS_REPOS  clones of the part B projects                       [<repos>/realbugs-repos]
  FACTORY_AXIS_INDEX  the open build's distillation index (factory arm)
  ANTHROPIC_ENV   a file with ANTHROPIC_API_KEY=... (pr-agent arm)    [<repos>/grounded-forge/_evals/anthropic.env]

Each arm, as committed here before the first trial:

- factory: `factory replay run` on the case file (the factory at this repo's HEAD, recorded in results/v5-factory.commit),
  grounded in the open build. Reported findings: the ones the warranty sheet shows (the sort's confirmed and disputed;
  "noise" is left out, as the sheet leaves it out). Part B stop: the replay's own outcome for a control (any blocking
  finding or gate failure).
- vendors: OpenAI's `codex review --base base` (model gpt-6.1-sol, a neutral CODEX_HOME holding only the sign-in, so no
  personal config or instructions) and Claude Code with the plain prompt below, under the same isolation as the
  factory's own Claude reviewer (no session persistence, strict MCP config, project settings only, read-only tools),
  Claude Code's default model (recorded). Findings pooled. Part B stop: any Codex P0 or P1, or any Claude critical or
  high.
- pr-agent: PR-Agent 0.48.0 `review`, plain-diff mode (it sees the diff only; that mode has no title or body),
  model anthropic/claude-opus-5-5 through the Anthropic API. Two settings beyond the model, because PR-Agent doesn't
  know this model yet: its context size (200,000 tokens; PR-Agent otherwise assumes 32,000 and cuts large diffs) and a
  600-second API timeout. Part B stop: any key issue to review, or a security concern other than "No".
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REALBUGS = HERE.parent
FACTORY = REALBUGS.parent.parent
REPOS_ROOT = FACTORY.parent
RB_ROOT = Path(os.environ.get("RB_ROOT", REPOS_ROOT / "ReviewBench"))
RB_REPOS = Path(os.environ.get("RB_REPOS", REPOS_ROOT / "reviewbench-repos"))
REALBUGS_REPOS = Path(os.environ.get("REALBUGS_REPOS", REPOS_ROOT / "realbugs-repos"))
ANTHROPIC_ENV = Path(os.environ.get("ANTHROPIC_ENV", REPOS_ROOT / "grounded-forge" / "_evals" / "anthropic.env"))
PR_AGENT_PY = Path(os.environ.get("PR_AGENT_PY", REPOS_ROOT / "realbugs-work" / "pr-agent-venv" / "bin" / "python"))
CODEX = os.environ.get("CODEX_BIN", "/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex")
CODEX_MODEL = "gpt-6.1-sol"
PR_AGENT_MODEL = "anthropic/claude-opus-5-5"
TIMEOUT_S = 60 * 60  # what the factory gives its own review legs
NEUTRAL_STORY = "A contributor's change to {project}. Review it before it merges."

CLAUDE_PROMPT = """You are reviewing a change before it merges. The repository is checked out at the change's head; the \
branch `base` is where the change started, and the whole change is in {diff} (`git diff base...HEAD`).

What the author says about it:
{story}

Review it as a careful senior engineer and report every issue worth raising. Your final message is ONLY a JSON array, \
no prose and no code fence, one object per issue:
{{"file": "path from the repository root", "start_line": 1, "end_line": 1, "severity": "critical|high|medium|low", \
"message": "what is wrong and why it matters"}}
An empty array if you find nothing."""


# ---------------------------------------------------------------------------------------------------------- cases

def part_a_cases() -> list[dict]:
    tests = json.loads((RB_ROOT / "corpus" / "test" / "test.json").read_text())
    return [{"id": f"rb{i:02d}", "kind": "pr", "project": t["nwo"].replace("/", "_"), "repo": t["repo"],
             "pr_number": int(t["pr_number"]), "base": t["base"], "head": t["head"], "title": t["title"],
             "body": t.get("body") or ""} for i, t in enumerate(tests, 1)]


def part_c_cases() -> list[dict]:
    """PREREG-v6's sample (pick_v6.py)."""
    return json.loads((REALBUGS / "v6-cases.json").read_text())["cases"]


def part_d_cases() -> list[dict]:
    """PREREG-v7's sample (pick_v7.py)."""
    return json.loads((REALBUGS / "v7-cases.json").read_text())["cases"]


def part_b_cases() -> list[dict]:
    return json.loads((REALBUGS / "v5-controls.json").read_text())["cases"]


def ensure_mirror(case: dict) -> Path:
    repo = RB_REPOS / case["project"]
    if repo.exists():
        return repo
    RB_REPOS.mkdir(parents=True, exist_ok=True)
    partial = RB_REPOS / f"{case['project']}.partial"  # only a finished clone takes the real name
    for attempt in range(3):
        shutil.rmtree(partial, ignore_errors=True)
        r = subprocess.run(["git", "clone", "-q", f"https://github.com/review-bench/{case['project']}.git", str(partial)])
        if r.returncode == 0:
            partial.rename(repo)
            return repo
        time.sleep(30 * (attempt + 1))
    raise RuntimeError(f"could not clone the {case['project']} mirror")


def has(repo: Path, sha: str) -> bool:
    return subprocess.run(["git", "cat-file", "-e", f"{sha}^{{commit}}"], cwd=repo, capture_output=True).returncode == 0


def ensure_commits(case: dict, repo: Path) -> None:
    """A pull request's base and head can sit outside the mirror's branches. Fetch them as ReviewBench's own
    try-agent.sh does: from the mirror, then from the upstream repository's pull request ref."""
    if has(repo, case["base"]) and has(repo, case["head"]):
        return
    fetch = lambda *a: subprocess.run(["git", "fetch", "-q", *a], cwd=repo, capture_output=True,
                                      env=dict(os.environ, GIT_LFS_SKIP_SMUDGE="1"))
    fetch("origin", case["base"], case["head"])
    if not (has(repo, case["base"]) and has(repo, case["head"])):
        fetch(case["repo"], case["base"], f"pull/{case['pr_number']}/head")
    if not (has(repo, case["base"]) and has(repo, case["head"])):
        fetch(case["repo"], case["base"], case["head"])
    if not (has(repo, case["base"]) and has(repo, case["head"])):
        raise RuntimeError(f"{case['id']}: could not fetch base and head")


def checkout(case: dict, part: str, dest: Path) -> tuple[Path, str]:
    """A git repository at dest with branch `base` at the change's start and HEAD at its end; returns (repo, story)."""
    git = lambda *a, cwd=dest: subprocess.run(["git", "-c", "core.hooksPath=/dev/null", *a], cwd=cwd, check=True,
                                              capture_output=True)
    if part in ("a", "c", "d"):
        mirror = ensure_mirror(case)
        ensure_commits(case, mirror)
        subprocess.run(["git", "clone", "-q", "--shared", "--no-checkout", str(mirror), str(dest)], check=True)
        git("checkout", "-q", case["head"])
        git("branch", "-f", "base", case["base"])
        return dest, f"{case['title']}\n\n{case['body']}".strip()
    sys.path.insert(0, str(FACTORY))
    from factory.replay import materialise
    fx = materialise(case, REALBUGS_REPOS, Path(tempfile.mkdtemp()) / case["id"])
    shutil.copytree(fx / "app", dest)
    git("init", "-q", "-b", "main")
    git("add", "-A")
    git("-c", "user.name=v5", "-c", "user.email=v5@local", "commit", "-q", "-m", "base")
    git("branch", "base")
    git("apply", str(fx / "change.patch"))
    git("add", "-A")
    git("-c", "user.name=v5", "-c", "user.email=v5@local", "commit", "-q", "-m", "change")
    return dest, NEUTRAL_STORY.format(project=case["project"])


def rel(path: str, repo: Path) -> str:
    """A reviewer's path, relative to the repository root (macOS reports temp folders both with and without /private)."""
    p = path.strip()
    real = os.path.realpath(repo)
    for root in {real, real.removeprefix("/private"), str(repo)}:
        if p.startswith(root + "/"):
            return p[len(root) + 1:]
    return p.removeprefix("./")


# ----------------------------------------------------------------------------------------------------------- arms

def codex_home() -> Path:
    home = REPOS_ROOT / "realbugs-work" / "codex-home-neutral"
    home.mkdir(parents=True, exist_ok=True)
    link = home / "auth.json"
    if not link.exists():
        link.symlink_to(Path.home() / ".codex" / "auth.json")
    return home


CODEX_FINDING = re.compile(r"^- \[P(\d)\] (.+?) — (.+?):(\d+)(?:-(\d+))?\s*$\n((?:^  .*\n?)*)", re.M)


def run_codex_review(repo: Path, story_title: str, log: Path) -> tuple[list[dict], dict]:
    env = dict(os.environ, CODEX_HOME=str(codex_home()))
    t0 = time.time()
    try:
        r = subprocess.run([CODEX, "review", "--base", "base", "--title", story_title[:200], "-c", f'model="{CODEX_MODEL}"'],
                           cwd=repo, env=env, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        log.write_text("timed out\n")
        return [], {"timed_out": True, "seconds": TIMEOUT_S}
    log.write_text(f"exit {r.returncode}\n--- stdout\n{r.stdout}\n--- stderr\n{r.stderr}")
    out = []
    for m in CODEX_FINDING.finditer(r.stdout):
        start = int(m.group(4))
        out.append({"source": "codex", "priority": int(m.group(1)), "file": rel(m.group(3), repo), "start_line": start,
                    "end_line": int(m.group(5) or start),
                    "message": f"{m.group(2).strip()}. {' '.join(l.strip() for l in m.group(6).splitlines())}".strip()})
    return out, {"exit": r.returncode, "seconds": round(time.time() - t0), "outage": "usage limit" in r.stderr}


def json_items(text: str) -> tuple[list, int]:
    """The objects in a reviewer's JSON array, read one at a time, so one malformed item (a reviewer once wrote
    `"severity":low"`) costs that item, not the whole review. Returns (items, how many couldn't be read)."""
    if "[" not in text:
        return [], 0
    body = text[text.index("[") + 1:text.rindex("]") if "]" in text else len(text)]
    dec, items, broken, i = json.JSONDecoder(), [], 0, 0
    while True:
        start = body.find("{", i)
        if start < 0:
            return items, broken
        try:
            obj, end = dec.raw_decode(body, start)
            items.append(obj)
            i = end
        except ValueError:
            broken += 1
            nxt = body.find("},", start)  # skip to the next item
            if nxt < 0:
                return items, broken
            i = nxt + 2


def run_claude_review(repo: Path, story: str, log: Path) -> tuple[list[dict], dict]:
    diff = repo.parent / "change.diff"
    diff.write_bytes(subprocess.run(["git", "diff", "--no-color", "base...HEAD"], cwd=repo, capture_output=True,
                                    check=True).stdout)
    prompt = CLAUDE_PROMPT.format(diff=diff, story=story)
    t0 = time.time()
    try:
        r = subprocess.run(["claude", "-p", prompt, "--output-format", "json", "--no-session-persistence",
                            "--strict-mcp-config", "--setting-sources", "project", "--tools", "Read,Grep,Glob",
                            "--allowedTools", "Read,Grep,Glob", "--permission-mode", "dontAsk", "--add-dir",
                            str(diff.parent)],
                           cwd=repo, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        log.write_text("timed out\n")
        return [], {"timed_out": True, "seconds": TIMEOUT_S}
    log.write_text(f"exit {r.returncode}\n--- stdout\n{r.stdout}\n--- stderr\n{r.stderr[-4000:]}")
    meta = {"exit": r.returncode, "seconds": round(time.time() - t0)}
    try:
        res = json.loads(r.stdout)
        meta.update(cost_usd=res.get("total_cost_usd"), models=list((res.get("modelUsage") or {}).keys()))
    except ValueError as e:
        meta["unreadable"] = f"{type(e).__name__}"
        return [], meta
    items, broken = json_items(res.get("result") or "")
    if broken:
        meta["items_unreadable"] = broken
    out = []
    for it in items:
        if not isinstance(it, dict) or not it.get("file"):
            continue
        start = int(it.get("start_line") or 1)
        out.append({"source": "claude", "severity": str(it.get("severity") or "").lower(), "file": rel(it["file"], repo),
                    "start_line": start, "end_line": int(it.get("end_line") or start),
                    "message": str(it.get("message") or "").strip()})
    return out, meta


def anthropic_key() -> str:
    for line in ANTHROPIC_ENV.read_text().splitlines():
        m = re.match(r"^\s*(?:export\s+)?ANTHROPIC_API_KEY\s*=\s*(.*)$", line)
        if m:
            return m.group(1).strip().strip("\"'")
    raise SystemExit(f"ANTHROPIC_API_KEY not found in {ANTHROPIC_ENV}")


def run_pr_agent(repo: Path, log: Path) -> tuple[list[dict], dict]:
    diff = repo.parent / "change.diff"
    diff.write_bytes(subprocess.run(["git", "diff", "--no-color", "base...HEAD"], cwd=repo, capture_output=True,
                                    check=True).stdout)
    out_json = repo.parent / "pr-agent.json"
    key = anthropic_key()
    env = dict(os.environ, ANTHROPIC_API_KEY=key, ANTHROPIC__KEY=key, CONFIG__MODEL=PR_AGENT_MODEL,
               CONFIG__FALLBACK_MODELS=json.dumps([PR_AGENT_MODEL]), CONFIG__CUSTOM_MODEL_MAX_TOKENS="200000",
               CONFIG__AI_TIMEOUT="600")
    t0 = time.time()
    try:
        r = subprocess.run([str(PR_AGENT_PY), "-m", "pr_agent.cli", "--diff-file", str(diff), "--json-output",
                            str(out_json), "review"], cwd=repo.parent, env=env, stdin=subprocess.DEVNULL,
                           capture_output=True, text=True, timeout=TIMEOUT_S)
    except subprocess.TimeoutExpired:
        log.write_text("timed out\n")
        return [], {"timed_out": True, "seconds": TIMEOUT_S}
    log.write_text((f"exit {r.returncode}\n--- stdout\n{r.stdout[-6000:]}\n--- stderr\n{r.stderr[-6000:]}").replace(key, "<key>"))
    meta = {"exit": r.returncode, "seconds": round(time.time() - t0)}
    if not out_json.exists():
        meta["unreadable"] = "no json output"
        return [], meta
    data = json.loads(out_json.read_text())
    review, usage = data.get("review") or {}, data.get("usage") or {}
    meta["usage"] = usage
    out = []
    for it in review.get("key_issues_to_review") or []:
        start = int(it.get("start_line") or 1)
        out.append({"source": "pr-agent", "kind": "key_issue", "file": rel(str(it.get("relevant_file") or ""), repo),
                    "start_line": start, "end_line": int(it.get("end_line") or start),
                    "message": f"{str(it.get('issue_header') or '').strip()}. {str(it.get('issue_content') or '').strip()}"})
    sec = str(review.get("security_concerns") or "").strip()
    meta["security_concern"] = bool(sec) and not sec.lower().startswith("no")
    if meta["security_concern"]:
        out.append({"source": "pr-agent", "kind": "security", "file": out[0]["file"] if out else "", "start_line": 1,
                    "end_line": 1, "message": sec})
    return out, meta


# -------------------------------------------------------------------------------------------------------- outputs

def rb_file(case: dict, agent: str, findings: list[dict], seconds: int) -> dict:
    return {"pr": {"repo": case["repo"], "pr_number": case["pr_number"], "base": case["base"], "head": case["head"]},
            "agent": agent,
            "findings": [{"producer": agent, "file": f["file"], "start_line": f["start_line"],
                          "end_line": max(f["end_line"], f["start_line"]), "message": f["message"]}
                         for f in findings if f["file"] and f["message"]],
            "usage": {"time_in_ms": seconds * 1000}}


def stop(arm: str, findings: list[dict], meta: dict) -> bool:
    if arm == "vendors":
        return any((f["source"] == "codex" and f.get("priority", 9) <= 1) or
                   (f["source"] == "claude" and f.get("severity") in ("critical", "high")) for f in findings)
    if arm == "pr-agent":
        return any(f.get("kind") == "key_issue" for f in findings) or bool(meta.get("security_concern"))
    raise ValueError(arm)


def run_external(part: str, arm: str, cases: list[dict], out: Path, jobs: int = 2) -> None:
    todo = [c for c in cases if not (out / "trials" / f"{c['id']}.json").exists()]
    outage = False
    with cf.ThreadPoolExecutor(max_workers=jobs) as pool:
        for line in pool.map(lambda c: one_external(part, arm, c, out), todo):
            print(line, flush=True)
            outage |= "usage limit" in line
    if outage:  # exit 3: the driver waits for Codex and runs the cases left over
        raise SystemExit(3)


def one_external(part: str, arm: str, case: dict, out: Path) -> str:
    rec_path = out / "trials" / f"{case['id']}.json"
    work = Path(tempfile.mkdtemp(prefix=f"v5-{part}-{arm}-{case['id']}-"))
    repo, story = checkout(case, part, work / "repo")
    (out / "logs").mkdir(parents=True, exist_ok=True)
    findings, meta = [], {}
    if arm == "claude-again":  # PREREG-v6's control: a second, separate plain Claude Code review
        findings, meta = run_claude_review(repo, story, out / "logs" / f"{case['id']}-claude.log")
    elif arm == "vendors":
        title = case.get("title") or story.splitlines()[0]
        with cf.ThreadPoolExecutor(max_workers=2) as two:
            cx = two.submit(run_codex_review, repo, title, out / "logs" / f"{case['id']}-codex.log")
            cc = two.submit(run_claude_review, repo, story, out / "logs" / f"{case['id']}-claude.log")
            (fx, mx), (fc, mc) = cx.result(), cc.result()
        findings, meta = fx + fc, {"codex": mx, "claude": mc, "seconds": max(mx["seconds"], mc["seconds"])}
        if mx.get("outage"):  # not recorded: re-run once Codex answers again
            shutil.rmtree(work, ignore_errors=True)
            return f"{case['id']}: codex usage limit; left for the next pass"
    else:
        findings, meta = run_pr_agent(repo, out / "logs" / f"{case['id']}-pr-agent.log")
    rec = {"id": case["id"], "arm": arm, "findings": findings, "meta": meta}
    if part == "b":
        rec["stopped"] = stop(arm, findings, meta)
    rec_path.parent.mkdir(parents=True, exist_ok=True)
    rec_path.write_text(json.dumps(rec, indent=1))
    if part in ("a", "c", "d"):
        (out / "findings").mkdir(exist_ok=True)
        (out / "findings" / f"{case['id']}.json").write_text(
            json.dumps(rb_file(case, f"v5-{arm}", findings, meta.get("seconds", 0)), indent=1))
    shutil.rmtree(work, ignore_errors=True)
    return f"{case['id']}: {len(findings)} findings" + (f", stopped={rec['stopped']}" if part == "b" else "")


def factory_to_rb(cases: list[dict], out: Path) -> None:
    """The factory arm's part A findings, in ReviewBench's format: what the warranty sheet shows."""
    (out / "findings").mkdir(parents=True, exist_ok=True)
    for case in cases:
        p = out / "trials" / f"{case['id']}-t1.json"
        if not p.exists():
            continue
        rec = json.loads(p.read_text())
        if os.environ.get("V5_REPORT") == "members":  # every reviewer's own finding, whatever the sort's verdict
            shown = [m for f in rec.get("findings") or [] for m in f.get("members") or [f]]
        else:
            shown = [f for f in rec.get("findings") or [] if f.get("verdict") in ("confirmed", "disputed")]
        findings = []
        for f in shown:
            line = int(re.match(r"\d+", str(f.get("line") or "1")).group()) if re.match(r"\d+", str(f.get("line") or "1")) else 1
            message = " ".join(str(f.get(k) or "").strip() for k in ("claim", "evidence")).strip()
            findings.append({"file": str(f.get("file") or ""), "start_line": line, "end_line": line, "message": message})
        (out / "findings" / f"{case['id']}.json").write_text(json.dumps(rb_file(case, "v5-factory", findings, 0), indent=1))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("part", choices=["a", "b", "c", "d"], help="c is PREREG-v6's sample, d PREREG-v7's")
    ap.add_argument("arm", choices=["factory", "vendors", "pr-agent", "claude-again"])
    ap.add_argument("--only")
    ap.add_argument("--to-rb", action="store_true", help="factory arm: convert its trials to ReviewBench files only")
    args = ap.parse_args()
    cases = {"a": part_a_cases, "b": part_b_cases, "c": part_c_cases, "d": part_d_cases}[args.part]()
    if args.only:
        wanted = set(args.only.split(","))
        cases = [c for c in cases if c["id"] in wanted]
    out = REALBUGS / "results" / ({"c": f"v6-{args.arm}", "d": f"v7-{args.arm}"}.get(args.part)
                                  or f"v5-{args.part}-{args.arm}")
    out.mkdir(parents=True, exist_ok=True)
    if args.arm == "factory":
        cases_file = out / "cases.json"
        cases_file.write_text(json.dumps({"cases": cases}, indent=1))
        if args.part in ("a", "c", "d"):
            for c in cases:
                ensure_commits(c, ensure_mirror(c))
        if not args.to_rb:
            subprocess.run([sys.executable, "-m", "factory.cli", "replay", "run", "--cases", str(cases_file),
                            "--repos", str(REALBUGS_REPOS if args.part == "b" else RB_REPOS), "--out", str(out),
                            "--trials", "1", "--jobs", "1", "--grounding", "distillations"], cwd=FACTORY, check=True)
        if args.part in ("a", "c", "d"):
            factory_to_rb(cases, out)
        return
    run_external(args.part, args.arm, cases, out)


if __name__ == "__main__":
    main()
