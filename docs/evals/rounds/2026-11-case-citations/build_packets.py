#!/usr/bin/env python3
"""Build one scorer packet per answer.

    python3 build_packets.py RUNS_DIR CAPTURES_DIR OUT_DIR [ID_PREFIX ...]

With prefixes, only answers whose id starts with one of them are built.

RUNS_DIR holds the grounded-forge runs ({corpus}-{case}-{run}.out/answer.md);
CAPTURES_DIR the Gemini captures (gf-cc-{corpus}-{case}-{run}.json, with the
.located.json and .annotated.md that locate_chunks.py writes beside them).
Each packet carries the question, the answer (Gemini's with [n:slug] markers),
the citation legend with every chunk in full, the quotation locations from the
keyword-match round's quotes.py, and the path of the corpus's converted text.
"""
import json, os, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
KM = HERE.parent / "2026-11-keyword-match"
GF = HERE.parents[3]
MAIN = GF.parents[2] if (GF.parents[2] / "corpus.local/aarbuddy").exists() else GF
CONVERTED = {"demo": GF / "corpus.commons/demo/sources/converted", "aarbuddy": MAIN / "corpus.local/aarbuddy/sources/converted"}


def quotes(corpus, text_path):
    """Locate the answer's quotations. demo: quotes_free.py (whole-corpus, normalised). aarbuddy: the
    corpus is 1.2 GB, so each quotation's first six words are grepped as a line-break-tolerant regex."""
    if corpus == "demo":
        env = dict(os.environ, GF_CONVERTED=str(CONVERTED[corpus]))
        return subprocess.run([sys.executable, str(KM / "quotes_free.py"), str(text_path)], capture_output=True, text=True, env=env).stdout
    sys.path.insert(0, str(KM))
    from quotes import quotations  # noqa: E402
    rows = []
    for part in quotations(Path(text_path).read_text()):
        words = re.findall(r"[A-Za-z0-9']+", part)[:6]
        pat = r"\W+".join(re.escape(w) for w in words)
        hits = subprocess.run(["grep", "-rlizE", pat, str(CONVERTED[corpus])], capture_output=True, text=True).stdout.split("\n")
        hits = [Path(h).stem for h in hits if h.endswith(".md")][:3]
        rows.append(f"  {'found' if hits else 'MISSING':8} {', '.join(hits):45} {part[:100]}")
    return f"{len(rows)} quotations, {sum('found' in r[:10] for r in rows)} found (first six words, grep)\n" + "\n".join(rows) + "\n"


def main():
    runs, caps, out = map(Path, sys.argv[1:4])
    only = sys.argv[4:]
    wanted = lambda i: not only or any(i.startswith(p) for p in only)
    out.mkdir(parents=True, exist_ok=True)
    cases = {c["id"]: c["prompt"] for c in json.loads((HERE / "cases.json").read_text())}
    n = 0
    for f in sorted(caps.glob("gf-cc-*.json")):
        if f.name.endswith((".located.json", ".report.json")):
            continue
        cap = json.loads(f.read_text())
        if not wanted(cap["id"]):
            continue
        corpus, case, run = cap["id"].split("-")[:3]
        loc = json.loads(f.with_suffix(".located.json").read_text())
        ann = f.with_suffix(".annotated.md").read_text().split("\n", 4)[-1]
        reports = "\n\n".join(f"### Studio report: {r['title']}\n\n(citation markers in the report: {r['markers']})\n\n{r['text']}" for r in cap.get("reports", []))
        tmp = out / f"_{cap['id']}.txt"
        tmp.write_text(cap["text"] + "\n\n" + "\n\n".join(r["text"] for r in cap.get("reports", [])))
        legend = "\n".join(f"[{k}] {loc[k]['slug']}:{loc[k]['line']}\n{v['chunk']}\n" for k, v in cap["legend"].items())
        cond = cap.get("condition", "as-asked")
        (out / f"gemini-{cap['id']}.md").write_text(
            f"# gemini-{cap['id']}\n\nCondition: {cond}. Converted sources: {CONVERTED[corpus]}\n\n## Question\n\n{cases[case]}\n\n"
            f"## Chat answer\n\n{ann}\n\n{reports}\n\n## Citation legend (full chunk text per marker)\n\n{legend}\n## Quotation locations\n\n{quotes(corpus, tmp)}\n")
        tmp.unlink()
        n += 1
    for d in sorted(runs.glob("*-C?-?.out")):
        corpus, case, run = d.name[:-4].split("-")
        if not wanted(d.name[:-4]):
            continue
        ans = (d / "answer.md").read_text()
        (out / f"gf-{corpus}-{case}-{run}.md").write_text(
            f"# gf-{corpus}-{case}-{run}\n\nConverted sources: {CONVERTED[corpus]}\n\n## Question\n\n{cases[case]}\n\n## Answer\n\n{ans}\n\n"
            f"## Quotation locations\n\n{quotes(corpus, d / 'answer.md')}\n")
        n += 1
    print(n, "packets in", out)


if __name__ == "__main__":
    main()
