#!/usr/bin/env python3
"""Package a verbatim-mode report for a blind judge.

    python3 package_forge.py <report-folder> <out.md>

Writes the report as plain prose, essay joins, every placed span in quotation marks with
a bracketed number, and under each paragraph a pointer block per span: source, section,
printed page, converted file and line, the paragraph around the span, and the page images
pre-rendered for it. A span the resolver could not place is given as the model's
paraphrase, marked as such. Nothing names the tool that made the answer.

The output quotes the sources, so it belongs beside the report under corpus.local/.
"""
import json, sys
from pathlib import Path

folder, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
report = json.loads((folder / "report.json").read_text())
bundle = json.loads((folder / "bundle.json").read_text())
srcs = bundle["sources"]
n = 0
lines = [f"# Answer\n\nQuestion: {report['question']}\n", report.get("coverage_note", "") + "\n"]
for sec in report["sections"]:
    para, notes = [], []
    for j in sec["joins"]:
        if isinstance(j, str):
            para.append(j); continue
        n += 1
        sp = bundle["spans"].get(j["span"], {})
        src = srcs.get(j["source"], {})
        who = f"{src.get('author', '')}, {src.get('title', '')} ({src.get('year', '')})"
        if not sp.get("verified"):
            para.append(f"{j['paraphrase']} [{n}, paraphrase]")
            notes.append(f"[{n}] {who}. Paraphrase by the answer's author; no passage is pointed to.")
            continue
        para.append(f"“{sp['text']}” [{n}]")
        pages = ", ".join(str(folder / p["png"]) for p in sp.get("pages", []))
        hit = next((p for p in sp.get("pages", []) if p["n"] == sp.get("hit_page")), None)
        ctx = " ".join(x for x in (sp["context"].get("lead", ""), "«" + sp["text"] + "»", sp["context"].get("tail", "")) if x.strip())
        notes.append("\n".join([
            f"[{n}] {who}",
            f"    section: {sp.get('locator') or 'not recorded'}; printed page: {sp.get('page') or 'not kept by the converter'}",
            f"    original file: {folder / src['served'] if src.get('served') else 'not held'}" + (f", {'EPUB laid out at a fixed size, page' if sp.get('page_layout') == 'epub-reflow' else 'PDF page'} {sp['hit_page']}" if sp.get("hit_page") else ""),
            f"    converted text: {folder / src['converted_local']}, line {sp['line']}",
            f"    page images: {pages or 'none'}" + (f" (the passage is boxed on {folder / hit['png']})" if hit else ""),
            f"    paragraph: {ctx}",
        ]))
    lines.append(f"## {sec['heading']}\n\n{''.join(para).strip()}\n\nPointers:\n\n" + "\n\n".join(notes) + "\n")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(lines))
print(f"wrote {out}: {n} spans")
