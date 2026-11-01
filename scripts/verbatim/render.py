#!/usr/bin/env python3
"""Render a verbatim-mode report folder to a self-contained page.

    uv run --python 3.12 --with pymupdf python scripts/verbatim/render.py <report-folder> \
        [--verbatim R] [--joins essay|minimal] [--context UNIT:N] [--ship]

Reads <report-folder>/report.json (the model's joins) and bundle.json (the resolver's
placed spans) and writes <report-folder>/preview.html from this folder's template.html.
Copies into the report folder everything the page opens, so the folder works zipped
and from file://: vendor/ (D3), originals/ (the source PDFs and EPUBs), converted/
(the converted text each span was placed from), figures/, and pages/ (the hit page and
two either side, pre-rendered as PNGs with highlight boxes, through PyMuPDF).

The flags set the page's opening state only; every one of them is also a control on
the page. No model call: the flags change what is shown, never what was placed.

Deterministic: no model in the loop. Without an arm64 PyMuPDF the pages are skipped
and the page's "see the page in the original" button greys out.
"""
import argparse, json, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def _norm(s):
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("ﬁ", "fi"), ("ﬂ", "fl")):
        s = s.replace(a, b)
    return " ".join(s.replace("|", " ").split())   # a converted table's cell rules are not on the page


def load_fitz():
    try:
        import pymupdf as fitz
        return fitz
    except ImportError:
        try:
            import fitz
            return fitz
        except ImportError:
            return None


def prerender_pages(out, sid, pdf, spans, fitz, window=2, zoom=1.6):
    """For each span: find its page in the PDF or EPUB, render that page and `window` either
    side to PNG, and record the highlight boxes as fractions of the page."""
    pages_dir = out / "pages"; pages_dir.mkdir(exist_ok=True)
    doc = fitz.open(str(pdf))
    is_epub = pdf.suffix.lower() == ".epub"
    if is_epub:
        doc.layout(width=500, height=720, fontsize=12)   # a fixed layout so the EPUB has pages to show
    rendered = 0
    texts = [_norm(doc[i].get_text()).lower() for i in range(doc.page_count)]
    for sp in spans:
        words = _norm(sp["text"].replace("---", "-").replace("--", "-")).split()
        probes = []
        # start at the span's first word, then a few words in, past a compound the book may break across lines
        for off, k in ((0, 12), (0, 8), (0, 6), (0, 5), (3, 6), (6, 6), (9, 5)):
            base = " ".join(words[off:off + k])
            if len(base.split()) < 4: continue
            # the converter wrote a dash as "-"; the book may set it as an em or en dash, spaced or not
            variants = [base, base.replace("-", "—"), base.replace("-", "–"), base.replace("-", " — "), base.replace("-", " - ")] if "-" in base else [base]
            # _norm folded apostrophes to straight; the book may set them curly
            probes += [x for v in variants for x in dict.fromkeys((v, v.replace("'", "’")))]
        start = (sp.get("page") or 1) - 1
        start = min(max(0, start), doc.page_count - 1)
        order = list(range(start, min(doc.page_count, start + 120))) + [i for i in range(doc.page_count) if i < start or i >= start + 120]
        hit, found_q = None, None
        # longest probe first, across the whole document, so a short prefix that recurs on an
        # earlier page cannot win over the page that holds more of the span
        for q in probes:
            nq = q.lower()
            for i in order:
                if nq in texts[i]:
                    hit, found_q = i, q; break
            if hit is not None: break
        if hit is None:   # text extraction can differ from search_for (dehyphenation, ligatures): ask PyMuPDF page by page
            for i in order:
                for q in probes:
                    if doc[i].search_for(q):
                        hit, found_q = i, q; break
                if hit is not None: break
        if hit is None:
            print(f"  {sid}: page not found for span starting {probes[0]!r}", file=sys.stderr); continue
        page = doc[hit]; rect = page.rect
        quads = page.search_for(_norm(sp["text"])) or page.search_for(" ".join(words[:12])) or page.search_for(found_q)
        boxes = [[(q.x0 - rect.x0) / rect.width, (q.y0 - rect.y0) / rect.height, (q.x1 - rect.x0) / rect.width, (q.y1 - rect.y0) / rect.height] for q in quads]
        sp["hit_page"] = hit + 1; sp["pages"] = []; sp["page_layout"] = "epub-reflow" if is_epub else "pdf"
        for i in range(max(0, hit - window), min(doc.page_count, hit + window + 1)):
            png = pages_dir / f"{sid}-{i + 1}.png"
            if True:   # always: a replaced original or a new layout must not show stale pages
                doc[i].get_pixmap(matrix=fitz.Matrix(zoom, zoom)).save(str(png)); rendered += 1
            txt = doc[i].get_text().strip().split("\n")
            folio = None
            for cand in (txt[:3] + txt[-3:]):
                cand = cand.rstrip()
                m = re.fullmatch(r"\s*(\d{1,4})\s*", cand) or re.match(r"^\s*(\d{1,4})\s{2,}\S", cand) or re.search(r"\S\s{2,}(\d{1,4})$", cand) or re.match(r"^\s*(\d{1,4})\s+\d+\s+•", cand) or re.search(r"•.*\s(\d{1,4})$", cand)
                if m and len(cand) < 120 and not is_epub:
                    n = int(m.group(1))
                    if i - 60 <= n <= i + 1:   # a printed folio never exceeds the PDF page index by more than the cover
                        folio = n; break
            sp["pages"].append({"n": i + 1, "png": f"pages/{png.name}", "boxes": boxes if i == hit else [], "folio": folio})
            if i == hit and folio is not None and not sp.get("page"):
                sp["page"], sp["page_via"] = folio, "the folio printed on the PDF page"
        print(f"  {sid}: span on {'EPUB' if is_epub else 'PDF'} page {hit + 1} (printed p. {sp.get('page')}), {len(boxes)} highlight boxes", file=sys.stderr)
    return rendered


def copy_if_changed(src, dst):
    if not dst.exists() or dst.stat().st_size != src.stat().st_size or dst.stat().st_mtime < src.stat().st_mtime:
        shutil.copyfile(src, dst)


def render(out, init):
    report = json.loads((out / "report.json").read_text())
    bundle = json.loads((out / "bundle.json").read_text())
    root_of = lambda corpus: REPO / bundle["corpora"][corpus]["root"]

    vdir = out / "vendor"; vdir.mkdir(exist_ok=True)
    for f in (HERE / "vendor").iterdir():
        copy_if_changed(f, vdir / f.name)

    figdir = out / "figures"; figdir.mkdir(exist_ok=True)
    for sid, span in bundle.get("spans", {}).items():
        fig = span.get("figure")
        if not fig or not fig.get("image"):
            continue
        src = root_of(span.get("corpus") or bundle["sources"][span["source"]]["corpus"]) / fig["image"]
        if not src.exists():
            src = REPO / fig["image"]
        if src.exists():
            dst = figdir / f"{sid}{src.suffix}"
            shutil.copyfile(src, dst)
            fig["local"] = f"figures/{dst.name}"
        else:
            fig["local"] = None
            print(f"figure missing on disk: {src}", file=sys.stderr)

    fitz = load_fitz()
    if fitz is None:
        print("no PyMuPDF: skipping page pre-render (run through uv: uv run --python 3.12 --with pymupdf python render.py ...)", file=sys.stderr)
    cdir = out / "converted"; cdir.mkdir(exist_ok=True)
    odir = out / "originals"; odir.mkdir(exist_ok=True)
    pages = 0
    for sid, src in bundle.get("sources", {}).items():
        conv = root_of(src["corpus"]) / src["converted"]
        copy_if_changed(conv, cdir / f"{sid}.md")
        src["converted_local"] = f"converted/{sid}.md"
        src["served"] = None
        if not src.get("original"):
            continue
        f = root_of(src["corpus"]) / src["original"]
        if f.exists() and f.suffix.lower() in (".pdf", ".epub"):
            dst = odir / f"{sid}{f.suffix.lower()}"
            copy_if_changed(f, dst)
            src["served"] = f"originals/{dst.name}"
            if fitz is not None:
                pages += prerender_pages(out, sid, f, [s for s in bundle["spans"].values() if s.get("source") == sid and s.get("verified")], fitz)
        else:
            print(f"original not servable: {f}", file=sys.stderr)

    (out / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=1))   # with the served files and page images, for anything that reads the folder
    html = (HERE / "template.html").read_text()
    for marker, value in (("/*__REPORT__*/", report), ("/*__BUNDLE__*/", bundle), ("/*__INIT__*/", init)):
        html = html.replace(marker, json.dumps(value, ensure_ascii=False).replace("</", "<\\/"))
    (out / "preview.html").write_text(html)
    with_pages = sum(1 for s in bundle["spans"].values() if s.get("pages"))
    print(f"wrote {out / 'preview.html'}: {with_pages} of {len(bundle['spans'])} spans have pre-rendered pages ({pages} new PNGs)", file=sys.stderr)
    return {"spans_with_pages": with_pages, "new_pngs": pages}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path, help="report folder holding report.json and bundle.json")
    ap.add_argument("--verbatim", type=float, default=None, help="opening share of ranked spans shown as the author's words, 0..1 (default 1)")
    ap.add_argument("--joins", choices=("essay", "minimal"), default=None, help="opening join form (default: the report's mode.joins, else essay)")
    ap.add_argument("--context", default=None, choices=("paras:1", "chars:600", "words:120", "pages:1"), help="opening context window for a clicked span (default paras:1)")
    ap.add_argument("--ship", action="store_true", help="open as it would ship: copyrighted sources paraphrased under max_visibility open-nc")
    args = ap.parse_args()
    out = args.folder.resolve()
    report = json.loads((out / "report.json").read_text())
    init = {"verbatim": args.verbatim if args.verbatim is not None else 1.0,
            "joins": args.joins or report.get("mode", {}).get("joins", "essay"),
            "ctx": args.context or "paras:1", "ship": args.ship}
    if init["joins"] not in ("essay", "minimal"):
        init["joins"] = "essay"
    render(out, init)


if __name__ == "__main__":
    main()
