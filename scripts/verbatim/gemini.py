#!/usr/bin/env python3
"""Render a captured Gemini Notebook answer as gemini.html beside a verbatim-mode report.

    python3 scripts/verbatim/gemini.py <capture.md> <report-folder>

The capture is the markdown an eval round saves for the Gemini arm: setup notes, a line
holding only `---`, then `# Answer`, the question, the answer word for word with every
citation marker as `[n]`, and `## Citations`, where each `**[n]** source file` is followed
by the passage that marker's popup showed, as a blockquote.

The page shows the answer exactly as captured, in the same typography as the report page,
and a click on a marker shows its source file and the captured passage. It adds nothing
Gemini didn't show: no page numbers, no highlight inside a passage, no styling borrowed
from Google. A banner says it is a static copy made from a capture, and that the notebook
itself also opens the source at the cited passage, which this page can't. It links to the
report page, and render.py's --gemini flag links the report page back to it.

Deterministic: no model in the loop.
"""
import argparse, html, json, re, sys
from pathlib import Path


def parse(text):
    head, _, body = text.partition("\n---\n")
    if not body:
        raise SystemExit("capture: no line holding only --- between the setup notes and the answer")
    answer, _, cites = body.partition("\n## Citations")
    answer = answer.split("# Answer", 1)[-1].strip()
    question = ""
    m = re.match(r"Question:\s*(.+)\n", answer)
    if m:
        question, answer = m.group(1).strip(), answer[m.end():].strip()
    citations = {}
    for m in re.finditer(r"\*\*\[(\d+)\]\*\*\s*(.+?)\n\n((?:>.*(?:\n|$))+)", cites):
        paras = re.split(r"\n>\s*\n", m.group(3).strip())
        citations[m.group(1)] = {"source": m.group(2).strip(),
                                 "passage": [re.sub(r"^>\s?", "", p, flags=re.M).replace("\n", " ").strip() for p in paras if p.strip("> \n")]}
    return {"setup": head.strip(), "question": question, "answer": answer, "citations": citations}


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"\[(\d+)\]", r'<button class="cite" data-n="\1">\1</button>', s)


def blocks(md):
    out, items = [], []
    def flush():
        if items: out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>"); items.clear()
    for para in re.split(r"\n\s*\n", md):
        for line in para.strip().split("\n"):
            if line.startswith("- "):
                items.append(line[2:]); continue
            flush()
            if line.startswith("## "): out.append(f"<h2>{inline(line[3:])}</h2>")
            elif line.strip(): out.append(f"<p>{inline(line)}</p>")
        flush()
    return "\n".join(out)


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Gemini Notebook's answer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,400;0,500;0,600;1,400&family=Archivo+Narrow:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--g-ground:#FFFFFF;--g-ink:#1D2328;--g-secondary:#4A545E;--g-rule:#D5DAE0;--g-action:#1F4BB0;--g-tint:#F3F5F7;
  --font-body:"Archivo",Arial,sans-serif;--font-display:"Archivo Narrow","Arial Narrow",Arial,sans-serif;--measure:42rem}
html{background:var(--g-ground)}
body{margin:0;color:var(--g-ink);font-family:var(--font-body);font-size:19px;line-height:1.64;background:var(--g-ground)}
main{max-width:var(--measure);margin:0 auto;padding:32px 16px 80px}
a{color:var(--g-action)}
header{border-top:3px solid var(--g-ink);padding-top:14px;margin-bottom:24px}
.kicker{font-family:var(--font-display);font-size:16px;letter-spacing:.02em;color:var(--g-secondary);text-transform:uppercase}
h1{font-family:var(--font-display);font-weight:600;font-size:clamp(30px,5vw,48px);line-height:1.1;margin:6px 0 14px}
h2{font-family:var(--font-display);font-weight:600;font-size:26px;line-height:1.2;margin:34px 0 8px}
.banner{font-size:16px;line-height:1.5;color:var(--g-secondary);border-top:1px solid var(--g-rule);border-bottom:1px solid var(--g-rule);padding:12px 0}
.banner b{color:var(--g-ink);font-weight:600}
details{font-size:15px;line-height:1.5;color:var(--g-secondary);margin:8px 0 0}
details summary{cursor:pointer;color:var(--g-action)}
details pre{white-space:pre-wrap;font-family:var(--font-body);font-size:15px;margin:8px 0 0}
ul{padding-left:1.2em}
button.cite{font:500 13px/1 var(--font-body);color:var(--g-ink);background:var(--g-tint);border:1px solid var(--g-rule);border-radius:999px;padding:3px 7px;margin:0 1px;cursor:pointer;vertical-align:2px}
button.cite:hover,button.cite.on{border-color:var(--g-action);color:var(--g-action)}
.pop{font-size:16px;line-height:1.55;background:var(--g-tint);border-left:3px solid var(--g-action);padding:12px 16px;margin:10px 0 16px;position:relative}
.pop .src{font-weight:600;padding-right:28px;overflow-wrap:anywhere}
.pop .note{font-size:14px;color:var(--g-secondary);margin-top:8px}
.pop p{margin:8px 0 0}
.pop .close{position:absolute;top:6px;right:8px;border:0;background:none;font-size:22px;cursor:pointer;color:var(--g-secondary)}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--g-ground:#14181C;--g-ink:#E6E9EC;--g-secondary:#A9B2BB;--g-rule:#333B43;--g-action:#8FB0FF;--g-tint:#1E242A}}
:root[data-theme="dark"]{--g-ground:#14181C;--g-ink:#E6E9EC;--g-secondary:#A9B2BB;--g-rule:#333B43;--g-action:#8FB0FF;--g-tint:#1E242A}
</style></head><body><main>
<header><div class="kicker">Gemini Notebook · the same question</div><h1>__QUESTION__</h1>
<div class="banner"><b>A static copy, made from a capture.</b> This is Gemini Notebook's answer to the same question, captured __WHEN__: the answer word for word, and for each citation marker the source it names and the passage its popup showed, in full. Click a marker to see it. Gemini gives no page number and marks nothing inside the passage, so neither does this page. In the notebook itself, clicking a citation also opens the source at that passage, which a static copy can't do. The page uses the report's typography, not Google's. __BACK__</div>
<details><summary>How this was captured</summary><pre>__SETUP__</pre></details>
</header>
<article id="answer">
__ANSWER__
</article>
</main>
<script>
const CITES = __CITES__;
const esc = s => s.replace(/[&<>]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
let open = null;
function close(){ if(open){ open.pop.remove(); open.btn.classList.remove("on"); open = null; } }
document.getElementById("answer").addEventListener("click", e => {
  const b = e.target.closest("button.cite"); if(!b) return;
  const same = open && open.btn === b; close(); if(same) return;
  const c = CITES[b.dataset.n];
  const pop = document.createElement("div"); pop.className = "pop";
  pop.innerHTML = `<button class="close" title="close">×</button><div class="src">[${b.dataset.n}] ${esc(c ? c.source : "not captured")}</div>` +
    (c ? c.passage.map(p => `<p>${esc(p)}</p>`).join("") : "") +
    `<div class="note">The passage this marker's popup showed, as captured. No page number; no span marked inside it.</div>`;
  pop.querySelector(".close").addEventListener("click", close);
  b.closest("p,li").after(pop); b.classList.add("on"); open = {btn: b, pop};
});
</script></body></html>
"""


def write(capture, folder, report_page="preview.html"):
    cap = parse(Path(capture).read_text())
    when = re.search(r"Captured ([^,.]+(?:, [^,.(]+)?)", cap["setup"])
    back = f'<a href="{report_page}">See grounded-forge\'s answer to the same question</a>.'
    page = (PAGE.replace("__QUESTION__", html.escape(cap["question"] or "Gemini Notebook's answer"))
                .replace("__WHEN__", html.escape(when.group(1)) if when else "as recorded below")
                .replace("__BACK__", back)
                .replace("__SETUP__", html.escape(cap["setup"]))
                .replace("__ANSWER__", blocks(cap["answer"]))
                .replace("__CITES__", json.dumps(cap["citations"], ensure_ascii=False).replace("</", "<\\/")))
    (Path(folder) / "gemini.html").write_text(page)
    markers = set(re.findall(r"\[(\d+)\]", cap["answer"]))
    missing = sorted(markers - set(cap["citations"]), key=int)
    return {"citations": len(cap["citations"]), "markers": len(re.findall(r"\[(\d+)\]", cap["answer"])), "uncaptured": missing}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("capture", type=Path)
    ap.add_argument("folder", type=Path)
    args = ap.parse_args()
    r = write(args.capture, args.folder)
    print(f"wrote {args.folder / 'gemini.html'}: {r['markers']} markers, {r['citations']} citations" + (f"; no passage captured for {r['uncaptured']}" if r["uncaptured"] else ""), file=sys.stderr)


if __name__ == "__main__":
    main()
