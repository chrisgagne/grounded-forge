#!/usr/bin/env python3
"""Generate a verbatim-mode report: one model step, then deterministic placement and rendering.

    python3 scripts/verbatim/generate.py --question "…" --corpora aarbuddy,demo --out <folder>
        [--model opus] [--joins both|essay|minimal]
        [--verbatim R] [--context UNIT:N] [--ship] [--render-only]

1. Model step. One headless `claude -p` run from the repo root, with --add-dir for each
   corpus root and the tools Read, Grep, Glob, Bash and Write. It runs answer-from-corpus
   in project mode over the named corpora and writes <out>/report.json under
   scripts/verbatim/contract.md: model prose (joins) and placeholders (a source ID and an
   anchor copied from the converted text). The model never types a quotation.
2. Resolve (resolve.py): every anchor found in sources/converted/ and expanded to whole
   sentences. No model.
3. Repair, once: if any span was not found, one more `claude -p` run sees only the missing
   placeholders and their converted files and supplies a new anchor copied from the text;
   resolve again. A span still missing stays hatched and shows its paraphrase, never a quote.
4. Render (render.py, through uv for an arm64 PyMuPDF): <out>/preview.html, self-contained.

Render-time flags need no model call: --verbatim, --context, --ship and the page's own
controls change what is shown, never what was placed. --render-only re-resolves and
re-renders an existing report folder with no model call at all.

The model step appends to Claude Code's system prompt; it never replaces it.
"""
import argparse, json, re, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
from resolve import corpus_info  # noqa: E402

SYSTEM_APPEND = """You are the model step of grounded-forge's verbatim-mode generator. Your one output is a JSON file, report.json, written with the Write tool to the path the user gives, in the exact shape scripts/verbatim/contract.md sets out. A deterministic resolver then places the authors' words from the converted sources; you never type an author's words into your prose. Wherever you want the author's own words, you write a placeholder whose anchor is 8 to 12 consecutive words you copied, character for character, from a line of the converted text that you read in this run with Read or Grep. Copy anchors from sources/converted/ only, never from a reference, a distillation, or memory. Work autonomously; nobody will answer questions."""

MODEL_PROMPT = """Question: {question}

Corpora (project mode; bare names, roots from the repo root): {corpora_list}

Do this:

1. Read scripts/verbatim/contract.md in full. It is the output contract.
2. Read .claude/skills/answer-from-corpus/SKILL.md in full and run it in project mode over {corpora_names}: classify the shape, run the lens check, decompose into sub-claims, route through each corpus's concept-index.json (topics block first), triage light references, read the deep references of the authors doing real work. Project mode never reads a distillation or a task index.
3. For each claim you want in an author's words, open the converted source (the path is in the deep reference's header or the source's sidecar under sources/original/{{slug}}.source.md) and Grep or Read the passage. Copy an anchor of 8 to 12 consecutive words from the line you read, choose `sentences` so the placed span carries the claim, and write the paraphrase. Aim for 8 to 14 spans across 4 to 6 sections, spread across distinct authors, the most load-bearing ranked first.
4. Before writing, check every anchor with Grep against its converted file (fixed-string, case-insensitive, on a distinctive 5- or 6-word stretch of it). Replace any anchor that does not match.
5. Write the report with the Write tool to {out}/report.json. {joins_rule} Your joins state what follows from the spans for the question asked, in plain prose, and name the source by author; they never quote. The coverage note says plainly what the corpora lack for this question and names two or three ingestion candidates.
6. Run `python3 -c "import json;json.load(open('{out}/report.json'))"` to check the file parses. Then reply with one line: the number of spans and sections.
"""

REPAIR_PROMPT = """The verbatim-mode resolver could not find these anchors in their converted sources. For each one, open the converted file named, find the passage that carries what the paraphrase says, and copy a new anchor of 8 to 12 consecutive words from a line you read with Read or Grep. Check it with a fixed-string, case-insensitive Grep on a distinctive 5- or 6-word stretch before you use it. If the source does not contain the passage, give an empty anchor; never invent one.

{items}

Write {out}/repair.json as {{"span-id": {{"anchor": "…", "sentences": N}}, …}} with the Write tool, one entry per span above, then reply with one line: how many anchors you replaced.
"""


def run_claude(prompt, add_dirs, model, log_path, max_turns):
    cmd = ["claude", "-p", prompt, "--model", model, "--output-format", "json", "--max-turns", str(max_turns),
           "--append-system-prompt", SYSTEM_APPEND, "--allowedTools", "Read", "Grep", "Glob", "Bash", "Write"]
    for d in add_dirs:
        cmd += ["--add-dir", str(d)]
    t0 = time.time()
    p = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    log = {"cmd": cmd[:2] + ["<prompt>"] + cmd[3:], "returncode": p.returncode, "seconds": round(time.time() - t0)}
    try:
        res = json.loads(p.stdout)
        log.update({k: res.get(k) for k in ("result", "num_turns", "total_cost_usd", "is_error", "subtype", "modelUsage")})
    except json.JSONDecodeError:
        log["stdout"] = p.stdout[-4000:]
    log["stderr"] = p.stderr[-4000:]
    log_path.write_text(json.dumps(log, indent=1, ensure_ascii=False))
    print(f"  claude -p: {log['seconds']} s, {log.get('num_turns')} turns, ${log.get('total_cost_usd')} of allowance, exit {p.returncode}", file=sys.stderr)
    if p.returncode != 0 or log.get("is_error"):
        tail = (log.get("result") or log.get("stderr") or "")[-600:]
        if re.search(r"usage limit|rate limit|limit reached", tail, re.I):
            raise SystemExit(f"usage limit: {tail}")
        print(f"  model step reported an error: {tail}", file=sys.stderr)
    return log


def placeholders(report):
    for sec in report.get("sections", []):
        for j in sec.get("joins", []):
            if isinstance(j, dict): yield j


def lint(report):
    """Contract checks the resolver does not make. Returns a list of problems; none blocks resolution."""
    out = []
    ids = [j.get("span") for j in placeholders(report)]
    if len(ids) != len(set(ids)): out.append("duplicate span IDs")
    for j in placeholders(report):
        n = len(str(j.get("anchor", "")).split())
        if not 8 <= n <= 12: out.append(f"{j.get('span')}: anchor has {n} words")
        if j.get("source") not in report.get("sources", {}): out.append(f"{j.get('span')}: source {j.get('source')} not in sources")
        if not j.get("paraphrase"): out.append(f"{j.get('span')}: no paraphrase")
    if sorted(report.get("rank", [])) != sorted(ids): out.append("rank does not list every span exactly once")
    sub = {s for c in report.get("subclaims", []) for s in c.get("spans", [])}
    if set(ids) - sub: out.append(f"spans in no subclaim: {sorted(set(ids) - sub)}")
    for sec in report.get("sections", []):
        for form in ("joins", "joins_min"):
            for j in sec.get(form, []) or []:
                if isinstance(j, str):
                    for q in re.findall(r"[\"“]([^\"”]{12,})[\"”]", j):
                        if len(q.split()) >= 4: out.append(f"{form} in {sec.get('heading', '')[:30]!r} carries a quoted run: {q[:60]!r}")
        if sec.get("joins_min") is not None:
            a = [j["span"] for j in sec["joins"] if isinstance(j, dict)]
            b = [j.get("span") for j in sec["joins_min"] if isinstance(j, dict)]
            if a != b: out.append(f"joins_min in {sec.get('heading', '')[:30]!r} does not carry the same spans in order")
    return out


def resolve(out):
    p = subprocess.run([sys.executable, str(HERE / "resolve.py"), str(out)], capture_output=True, text=True)
    (out / "resolve.log").write_text(p.stderr)
    if p.returncode != 0:
        raise SystemExit(f"resolve failed:\n{p.stderr[-2000:]}")
    return json.loads((out / "bundle.json").read_text())


def render(out, args):
    cmd = ["uv", "run", "--python", "3.12", "--with", "pymupdf", "python", str(HERE / "render.py"), str(out)]
    if args.verbatim is not None: cmd += ["--verbatim", str(args.verbatim)]
    if args.context: cmd += ["--context", args.context]
    if args.ship: cmd += ["--ship"]
    if args.joins in ("essay", "minimal"): cmd += ["--joins", args.joins]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:   # no uv: render without page images
        p = subprocess.run([sys.executable] + cmd[cmd.index(str(HERE / "render.py")):], capture_output=True, text=True)
    (out / "render.log").write_text(p.stderr)
    if p.returncode != 0:
        raise SystemExit(f"render failed:\n{p.stderr[-2000:]}")
    m = re.search(r"(\d+) of (\d+) spans have pre-rendered pages \((\d+) new PNGs\)", p.stderr)
    return {"spans_with_pages": int(m.group(1)), "new_pngs": int(m.group(3))} if m else {}


def own_share(report, bundle, joins="minimal"):
    """Share of the page's words that are the authors' own, at --verbatim 1, as the page counts it."""
    own = model = 0
    ph = {j["span"]: j for j in placeholders(report)}
    for sec in report["sections"]:
        form = sec.get("joins_min") if joins == "minimal" and sec.get("joins_min") else sec["joins"]
        for j in form:
            if isinstance(j, str): model += len(j.split()); continue
            sp = bundle["spans"].get(j["span"], {})
            if sp.get("verified"): own += len(sp["text"].split())
            else: model += len(ph.get(j["span"], {}).get("paraphrase", "").split())
    return own / max(1, own + model)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--question")
    ap.add_argument("--corpora", help="comma-separated bare corpus names, e.g. aarbuddy,demo")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--model", default="opus")
    ap.add_argument("--joins", default="both", choices=("both", "essay", "minimal"), help="join forms the model writes (both: essay and terse); also the page's opening form")
    ap.add_argument("--max-turns", type=int, default=150)
    ap.add_argument("--verbatim", type=float, help="render-time, no model call: opening --verbatim share, 0..1")
    ap.add_argument("--context", help="render-time, no model call: paras:1, chars:600, words:120 or pages:1")
    ap.add_argument("--ship", action="store_true", help="render-time, no model call: open under the open-nc shipping gate")
    ap.add_argument("--render-only", action="store_true", help="no model call: resolve and render an existing report.json")
    args = ap.parse_args()
    out = args.out.resolve(); out.mkdir(parents=True, exist_ok=True)
    summary = {"out": str(out)}

    if not args.render_only:
        if not (args.question and args.corpora):
            ap.error("--question and --corpora are required unless --render-only")
        names = [c.strip() for c in args.corpora.split(",") if c.strip()]
        infos = {c: corpus_info(c) for c in names}
        corpora_list = "; ".join(f"{c} at {i['root']}/ (ceiling {i['ceiling']})" for c, i in infos.items())
        joins_rule = {"both": "Write both `joins` (the essay form) and `joins_min` (the terse form, no lead-ins) for every section.",
                      "essay": "Write `joins` (the essay form) only; leave `joins_min` out.",
                      "minimal": "Write `joins` in the terse form (no lead-ins; the source mark names the source) and leave `joins_min` out."}[args.joins]
        prompt = MODEL_PROMPT.format(question=args.question, corpora_list=corpora_list, corpora_names=", ".join(names), out=out, joins_rule=joins_rule)
        print(f"model step ({args.model}) over {', '.join(names)} …", file=sys.stderr)
        log = run_claude(prompt, [REPO / i["root"] for i in infos.values()] + [out], args.model, out / "model-step.json", args.max_turns)
        summary["model_step"] = {k: log.get(k) for k in ("seconds", "num_turns", "total_cost_usd")}
        if not (out / "report.json").exists():
            raise SystemExit(f"the model step wrote no report.json; see {out / 'model-step.json'}")
        report = json.loads((out / "report.json").read_text())
        if report.get("question") != args.question:
            report["question"] = args.question
        report.setdefault("mode", {})["corpora"] = names
        report["mode"]["joins"] = "minimal" if args.joins == "minimal" else "essay"
        (out / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1))

    report = json.loads((out / "report.json").read_text())
    problems = lint(report)
    for p in problems: print("  contract:", p, file=sys.stderr)
    summary["contract_problems"] = problems
    bundle = resolve(out)
    missing = [k for k, s in bundle["spans"].items() if not s.get("verified")]
    summary["first_pass"] = {"spans": len(bundle["spans"]), "placed": len(bundle["spans"]) - len(missing), "missing": list(missing), "loose": [k for k, s in bundle["spans"].items() if s.get("status") == "loose"]}
    print(f"resolve: {summary['first_pass']['placed']} of {len(bundle['spans'])} placed", file=sys.stderr)

    if missing and not args.render_only:
        ph = {j["span"]: j for j in placeholders(report)}
        items = []
        for k in missing:
            j = ph[k]; src = report["sources"].get(j["source"], {})
            conv = bundle["sources"].get(j["source"], {}).get("converted") or src.get("converted")
            root = bundle["corpora"].get(src.get("corpus"), {}).get("root", "")
            items.append(f"- span {k}: source {j['source']} ({src.get('slug')}), converted file {root}/{conv}\n  old anchor (not found): {j['anchor']!r}\n  paraphrase: {j.get('paraphrase', '')}")
        print(f"repair pass for {len(missing)} spans …", file=sys.stderr)
        log = run_claude(REPAIR_PROMPT.format(items="\n".join(items), out=out), [REPO / bundle["corpora"][c]["root"] for c in bundle["corpora"]] + [out], args.model, out / "repair-step.json", 60)
        summary["repair_step"] = {k: log.get(k) for k in ("seconds", "num_turns", "total_cost_usd")}
        fixes = json.loads((out / "repair.json").read_text()) if (out / "repair.json").exists() else {}
        for sec in report["sections"]:
            for j in sec["joins"]:
                if isinstance(j, dict) and j["span"] in fixes and fixes[j["span"]].get("anchor"):
                    j["repaired_from"] = j["anchor"]
                    j["anchor"] = fixes[j["span"]]["anchor"]
                    j["sentences"] = int(fixes[j["span"]].get("sentences", j.get("sentences", 1)))
        (out / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1))
        bundle = resolve(out)
        missing = [k for k, s in bundle["spans"].items() if not s.get("verified")]

    summary["spans"] = len(bundle["spans"]); summary["placed"] = len(bundle["spans"]) - len(missing); summary["missing"] = missing
    summary["charts"] = bundle.get("charts", [])
    summary["source_problems"] = bundle.get("source_problems", [])
    summary["render"] = render(out, args)
    summary["own_share_minimal_v1"] = round(own_share(report, bundle, "minimal"), 3)
    summary["own_share_essay_v1"] = round(own_share(report, bundle, "essay"), 3)
    (out / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
    print(f"\nspans placed {summary['placed']} of {summary['spans']}, missing {len(missing)}"
          f"{' (' + ', '.join(missing) + ')' if missing else ''}; pages pre-rendered for {summary['render'].get('spans_with_pages')} spans"
          f"; authors' words {100 * summary['own_share_minimal_v1']:.0f}% at --joins minimal, {100 * summary['own_share_essay_v1']:.0f}% essay\n{out / 'preview.html'}")


if __name__ == "__main__":
    main()
