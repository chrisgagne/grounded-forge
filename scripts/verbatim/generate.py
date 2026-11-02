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
4. Credits, once: every join sentence that credits a source ("MCDP 1 ranks…", "the textbook
   says…", "Both sources…") must be a placeholder, so it carries a pointer. If any is not,
   one more `claude -p` run turns each into a pointed paraphrase (or cuts the credit), and
   resolve runs again. A credit still without a pointer stops the run.
5. Render (render.py, through uv for an arm64 PyMuPDF): <out>/preview.html and answer.md,
   with every quotation checked word for word against its page in the original.

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
5. Write the report with the Write tool to {out}/report.json. {joins_rule} Your joins state what follows from the spans for the question asked, in plain prose; they never quote, and they never credit. Every sentence that says what a source says, holds, found or recommends is a placeholder: a quotation, or a pointed paraphrase (`"show": "paraphrase"`, your sentence in `paraphrase`, with an anchor to the passage it rests on). A sentence comparing two sources is one pointed paraphrase per source. A join names an author only in a lead-in that runs straight into the placeholder after it. The coverage note says plainly what the corpora lack for this question and names two or three ingestion candidates.
6. Run `python3 -c "import json;json.load(open('{out}/report.json'))"` to check the file parses. Then reply with one line: the number of spans and sections.
"""

REPAIR_PROMPT = """The verbatim-mode resolver could not find these anchors in their converted sources. For each one, open the converted file named, find the passage that carries what the paraphrase says, and copy a new anchor of 8 to 12 consecutive words from a line you read with Read or Grep. Check it with a fixed-string, case-insensitive Grep on a distinctive 5- or 6-word stretch before you use it. If the source does not contain the passage, give an empty anchor; never invent one.

{items}

Write {out}/repair.json as {{"span-id": {{"anchor": "…", "sentences": N}}, …}} with the Write tool, one entry per span above, then reply with one line: how many anchors you replaced.
"""

CREDIT_PROMPT = """In the verbatim-mode report at {out}/report.json, these sentences in the model's own prose (the joins) say what a source says, holds or found, but carry no pointer to a passage:

{items}

Read scripts/verbatim/contract.md ("The rules that matter" and the placeholder table), then fix each sentence in report.json:

- If one passage in one source carries it: replace the sentence in that section's `joins` with a pointed paraphrase placeholder, {{"span": "…", "source": "…", "anchor": "…", "sentences": N, "paraphrase": "…", "show": "paraphrase"}}. The paraphrase is the sentence itself, reworded only as far as the passage needs. Copy the anchor, 8 to 12 consecutive words, from a line of the converted source you read with Read or Grep, and check it with a fixed-string, case-insensitive Grep on a distinctive 5- or 6-word stretch. Put the same span in `joins_min` at the same place, and in a subclaim. Leave it out of `rank`.
- If it compares two sources: one pointed paraphrase per source, joined by your own words.
- If no passage carries it: cut the credit. Rewrite it as your own reasoning with no source named, or drop it.
- If it is not a credit at all (for example "the board" meaning a company's board): leave it, and list it in {out}/credits-reviewed.json as [{{"sentence": "…", "why": "…"}}].

Change nothing else in the report. Write report.json back with the Write tool, check it parses with `python3 -c "import json;json.load(open('{out}/report.json'))"`, then reply with one line: how many sentences you made into placeholders, cut, and left.
"""

ORG = re.compile(r"\b(?:Corps|Department|Board|Service|Agency|Institute|University|OpenStax|Commission|Administration|Committee|Office|Cent(?:er|re)|Foundation|Council|Association|Press|NASA|Navy|Army|Marine|Forest|Health|Energy|Rice|Collective|Team|Group|NHS|Improvement)\b")
SOURCE_REF = re.compile(r"\b(?:the|this|both|either|each|neither|all|these|those|its|his|her|their)\s+(?:[\w'’-]+\s+){0,2}?(?:textbook|text|book|doctrine|manual|report|guide|handbook|study|studies|source|sources|author|authors|board|paper|article|chapter|framework|literature|tradition|teachers?|teachings?|pamphlet|publication|research|findings?)\b", re.I)


def source_names(report, bundle):
    """The words a join would use to credit a source of the run's corpora: personal surnames from
    the corpora's reference indexes and the run's sources, and each cited source's short name."""
    authors = [s.get("author", "") for s in bundle.get("sources", {}).values()]
    for c in bundle.get("corpora", {}).values():
        ri = REPO / c["root"] / "reference-index.json"
        if ri.exists():
            authors += [r.get("author") or "" for r in json.loads(ri.read_text()).get("refs", {}).values()]
    names = {s.get("short", "").strip() for s in report.get("sources", {}).values()} - {""}
    for a in authors:
        if not a or ORG.search(a): continue
        for person in re.split(r";|&|\band\b", a):
            person = person.strip()
            surname = person.split(",")[0].strip() if "," in person else (person.split()[-1] if person.split() else "")
            surname = re.sub(r"[^\w'’-]", "", surname)
            if len(surname) >= 3 and surname[0].isupper() and not surname.isupper(): names.add(surname)
    return names


def credits(report, bundle):
    """Join sentences that credit a source without being a placeholder: they name a source, or
    refer to one ("the textbook", "both sources"), and are not a lead-in running straight into
    the placeholder after them."""
    names = source_names(report, bundle)
    named = re.compile(r"(?<![\w-])(?:" + "|".join(sorted(map(re.escape, names), key=len, reverse=True)) + r")(?![\w-])") if names else None
    found = []
    for sec in report.get("sections", []):
        for form in ("joins", "joins_min"):
            js = sec.get(form) or []
            for i, j in enumerate(js):
                if not isinstance(j, str): continue
                parts = [p for p in re.split(r"(?<=[.!?])\s+", j.strip()) if p]
                for k, sent in enumerate(parts):
                    lead_in = k == len(parts) - 1 and i + 1 < len(js) and isinstance(js[i + 1], dict) and not re.search(r"[.!?][\"”’')]*$", sent)
                    if lead_in: continue
                    if (named and named.search(sent)) or SOURCE_REF.search(sent):
                        found.append({"section": sec.get("heading", ""), "form": form, "sentence": sent})
    return found


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
        raise SystemExit(f"the model step failed (exit {p.returncode}); see {log_path}: {tail}")
    return log


def placeholders(report):
    for sec in report.get("sections", []):
        for j in sec.get("joins", []):
            if isinstance(j, dict): yield j


QUOTED = re.compile(r"[\"“‘]([^\"”’]{12,}?)[\"”’](?!\w)")


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
    for j in placeholders(report):
        if j.get("show", "quote") not in ("quote", "paraphrase"): out.append(f"{j.get('span')}: show must be quote or paraphrase")
    quotes = [j.get("span") for j in placeholders(report) if j.get("show") != "paraphrase"]
    if sorted(report.get("rank", [])) != sorted(quotes): out.append("rank does not list every quotation placeholder exactly once (pointed paraphrases are left out)")
    sub = {s for c in report.get("subclaims", []) for s in c.get("spans", [])}
    if set(ids) - sub: out.append(f"spans in no subclaim: {sorted(set(ids) - sub)}")
    for sec in report.get("sections", []):
        for form in ("joins", "joins_min"):
            for j in sec.get(form, []) or []:
                text = j if isinstance(j, str) else (j.get("paraphrase", "") if form == "joins" else "")
                for q in QUOTED.findall(text):
                    if len(q.split()) >= 4: out.append(f"QUOTE: {form} in {sec.get('heading', '')[:30]!r} carries a quoted run: {q[:60]!r}")
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
    if args.passages: cmd += ["--passages"]
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
            if sp.get("verified") and sp.get("show") != "paraphrase": own += len(sp["text"].split())
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
    ap.add_argument("--passages", action="store_true", help="render-time, no model call: open with pointed paraphrases shown as the author's passages")
    ap.add_argument("--allow-join-quotes", action="store_true", help="render even though the model's prose carries quotation marks (check each first)")
    ap.add_argument("--allow-unpointed-credits", action="store_true", help="render even though join sentences still credit a source with no pointer (check each first)")
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
        for stale in ("report.json", "repair.json", "bundle.json", "summary.json"):
            (out / stale).unlink(missing_ok=True)   # a failed step must not leave an old answer to render
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
    quoted = [p for p in problems if p.startswith("QUOTE:")]
    if quoted and not args.allow_join_quotes:
        raise SystemExit("the model's own prose carries quotation marks around four or more words; a quotation reaches the page only "
                         "through a placeholder. Fix report.json (paraphrase it, or make it a span) and rerun with --render-only, "
                         "or pass --allow-join-quotes after checking each one is not a source's words:\n  " + "\n  ".join(quoted))
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
        (out / "repair.json").unlink(missing_ok=True)
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

    found = credits(report, bundle)
    reviewed = json.loads((out / "credits-reviewed.json").read_text()) if (out / "credits-reviewed.json").exists() else []
    found = [c for c in found if c["sentence"] not in {r.get("sentence") for r in reviewed}]
    if found and not args.render_only:
        items = "\n".join(f"- section {c['section']!r} ({c['form']}): {c['sentence']}" for c in found)
        print(f"credit pass for {len(found)} join sentences …", file=sys.stderr)
        log = run_claude(CREDIT_PROMPT.format(items=items, out=out), [REPO / bundle["corpora"][c]["root"] for c in bundle["corpora"]] + [out], args.model, out / "credit-step.json", 80)
        summary["credit_step"] = {k: log.get(k) for k in ("seconds", "num_turns", "total_cost_usd")}
        summary["credits_before_repair"] = len(found)
        report = json.loads((out / "report.json").read_text())
        problems = lint(report)
        for p in problems: print("  contract:", p, file=sys.stderr)
        summary["contract_problems"] = problems
        quoted = [p for p in problems if p.startswith("QUOTE:")]
        if quoted and not args.allow_join_quotes:
            raise SystemExit("the credit pass left quotation marks in the model's prose:\n  " + "\n  ".join(quoted))
        bundle = resolve(out)
        missing = [k for k, s in bundle["spans"].items() if not s.get("verified")]
        reviewed = json.loads((out / "credits-reviewed.json").read_text()) if (out / "credits-reviewed.json").exists() else []
        found = [c for c in credits(report, bundle) if c["sentence"] not in {r.get("sentence") for r in reviewed}]
    summary["credits_reviewed_not_credits"] = reviewed
    summary["unpointed_credits"] = found
    if found:
        for c in found: print(f"  unpointed credit in {c['section'][:30]!r}: {c['sentence'][:100]}", file=sys.stderr)
        if not args.render_only and not args.allow_unpointed_credits:
            (out / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
            raise SystemExit(f"{len(found)} join sentences still credit a source with no pointer (listed above and in summary.json). Make each "
                             "a pointed paraphrase in report.json and rerun with --render-only, or pass --allow-unpointed-credits after checking each.")
    summary["pointed_paraphrases"] = sum(1 for j in placeholders(report) if j.get("show") == "paraphrase")

    summary["spans"] = len(bundle["spans"]); summary["placed"] = len(bundle["spans"]) - len(missing); summary["missing"] = missing
    summary["charts"] = bundle.get("charts", [])
    summary["source_problems"] = bundle.get("source_problems", [])
    summary["render"] = render(out, args)
    rendered = json.loads((out / "bundle.json").read_text())
    pcs = [s.get("page_check") for s in rendered["spans"].values() if s.get("show") != "paraphrase" and s.get("verified")]
    summary["page_check"] = {"quotations": len(pcs), "checked": sum(1 for p in pcs if p and p.get("checked")),
                             "match": sum(1 for p in pcs if p and p.get("checked") and not [d for d in p.get("differences", []) if not d.get("corrected")]),
                             "split_words_set_from_page": sum(1 for p in pcs if p for d in p.get("differences", []) if d.get("corrected")),
                             "differ": {k: [d for d in s["page_check"]["differences"] if not d.get("corrected")] for k, s in rendered["spans"].items()
                                        if s.get("page_check", {}).get("differences") and [d for d in s["page_check"]["differences"] if not d.get("corrected")]}}
    summary["own_share_minimal_v1"] = round(own_share(report, bundle, "minimal"), 3)
    summary["own_share_essay_v1"] = round(own_share(report, bundle, "essay"), 3)
    (out / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
    print(f"\nspans placed {summary['placed']} of {summary['spans']}, missing {len(missing)}"
          f"{' (' + ', '.join(missing) + ')' if missing else ''}; pages pre-rendered for {summary['render'].get('spans_with_pages')} spans"
          f"; authors' words {100 * summary['own_share_minimal_v1']:.0f}% at --joins minimal, {100 * summary['own_share_essay_v1']:.0f}% essay"
          f"; {summary['pointed_paraphrases']} pointed paraphrases, {len(summary['unpointed_credits'])} credits without a pointer"
          f"; {summary['page_check']['match']} of {summary['page_check']['quotations']} quotations match the printed page\n{out / 'preview.html'}")


if __name__ == "__main__":
    main()
