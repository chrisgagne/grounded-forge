#!/usr/bin/env python3
"""Flatten a rendered verbatim-mode report to plain prose, for a reader with no browser or a judge.

    python3 scripts/verbatim/flatten.py <report-folder> [--out FILE] [--base PATH]

Writes the report with its essay joins, every placed span in quotation marks with a bracketed
number, and under each section a pointer block per span: source, section, printed page, the
original file and the page within it, converted file and line, the span's own paragraph, and
the page images (the hit page shows the passage highlighted). A span the resolver could not
place is given as the model's paraphrase, marked as such. Nothing names the tool that made it.

render.py calls this at the end of every render, writing <report-folder>/answer.md from the
same bundle as the page, so the two never disagree. File paths are relative to the report
folder unless --base gives the path a reader will reach the folder by (a judge's neutral path).

The output quotes the sources, so it stays beside the report.
"""
import argparse, json
from pathlib import Path


def flatten(folder, base=None):
    report = json.loads((folder / "report.json").read_text())
    bundle = json.loads((folder / "bundle.json").read_text())
    at = (lambda p: f"{base}/{p}") if base else (lambda p: p)
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
            pages = ", ".join(at(p["png"]) for p in sp.get("pages", []))
            hit = next((p for p in sp.get("pages", []) if p["boxes"]), None)
            ctx = " ".join(x for x in (sp["context"].get("lead", ""), "«" + sp["text"] + "»", sp["context"].get("tail", "")) if x.strip())
            layout = "EPUB laid out at a fixed size, page" if sp.get("page_layout") == "epub-reflow" else "PDF page"
            notes.append("\n".join([
                f"[{n}] {who}",
                f"    section: {sp.get('locator') or 'not recorded'}; printed page: {sp.get('page') or 'not kept by the converter'}",
                f"    original file: {at(src['served']) if src.get('served') else 'not held'}" + (f", {layout} {sp['hit_page']}" if sp.get("hit_page") else ""),
                f"    converted text: {at(src['converted_local'])}, line {sp['line']}",
                f"    page images: {pages or 'none'}" + (f" (the passage is highlighted on {at(hit['png'])})" if hit else ""),
                f"    paragraph: {ctx}",
            ]))
        lines.append(f"## {sec['heading']}\n\n{''.join(para).strip()}\n\nPointers:\n\n" + "\n\n".join(notes) + "\n")
    return "\n".join(lines), n


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path)
    ap.add_argument("--out", type=Path, default=None, help="default <report-folder>/answer.md")
    ap.add_argument("--base", default=None, help="the path a reader will reach the report folder by; default: paths relative to it")
    args = ap.parse_args()
    folder = args.folder.resolve()
    text, n = flatten(folder, args.base.rstrip("/") if args.base else None)
    out = args.out or folder / "answer.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(f"wrote {out}: {n} spans")


if __name__ == "__main__":
    main()
