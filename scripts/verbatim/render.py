#!/usr/bin/env python3
"""Render a verbatim-mode report folder to a self-contained page.

    uv run --python 3.12 --with pymupdf python scripts/verbatim/render.py <report-folder> \
        [--verbatim R] [--joins essay|minimal] [--context UNIT:N] [--ship] [--pages-only]

Reads <report-folder>/report.json (the model's joins) and bundle.json (the resolver's
placed spans) and writes <report-folder>/preview.html from this folder's template.html,
and answer.md, the same report as plain prose with its pointers (flatten.py).
Copies into the report folder everything the page opens, so the folder works zipped
and from file://: vendor/ (D3), originals/ (the source PDFs and EPUBs), converted/
(the converted text each span was placed from), figures/, and pages/ (the hit page and
two either side, pre-rendered as PNGs through PyMuPDF, the passage highlighted on the hit page).
--pages-only leaves the original files out of the folder: the page images are still drawn
from them, and any copy an earlier render left in originals/ is removed. --gemini CAPTURE
writes gemini.html beside the page from a captured Gemini Notebook answer (gemini.py), and
links the two pages to each other.

The flags set the page's opening state only; every one of them is also a control on
the page. No model call: the flags change what is shown, never what was placed.

Deterministic: no model in the loop. Without an arm64 PyMuPDF the pages are skipped
and the page's "see the page in the original" button greys out.
"""
import argparse, difflib, json, re, shutil, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


def _norm(s):
    for a, b in (("‘", "'"), ("’", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"), ("ﬁ", "fi"), ("ﬂ", "fl")):
        s = s.replace(a, b)
    return " ".join(s.replace("|", " ").split())   # a converted table's cell rules are not on the page


WORD = re.compile(r"[a-z0-9]+(?:'[a-z]+)*")


def _words(s):
    s = re.sub(r"(?<=[a-z])\d+\b", "", _norm(s).lower())   # a footnote call set against its word
    s = re.sub(r"(?<=[a-z])-(?=[a-z])", "", s)              # a compound compares as one word, as the page's dehyphenated text has it
    return WORD.findall(s)


def page_check(doc, hit, text, fitz, vocab):
    """Compare a placed quotation with the words printed on its page (and the next, for a span that
    runs over), and list every word of the quotation the page has differently or not at all: an
    OCR slip or a conversion error. Words the page has and the quotation lacks (a running head,
    a footnote call) are not counted."""
    flags = getattr(fitz, "TEXT_DEHYPHENATE", 0)
    page = " ".join(doc[i].get_text("text", flags=flags) for i in range(hit, min(doc.page_count, hit + 2)))
    a, b = _words(text), _words(page)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    if sum(m.size for m in sm.get_matching_blocks()) < 0.6 * len(a):
        return {"checked": False, "why": "the page's text does not line up with the quotation"}
    diffs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace" and (j2 - j1) <= 2 * (i2 - i1) + 2:
            q, pg = a[i1:i2], b[j1:j2]
            # the same letters spaced differently: the page's text layer glued two real words ("theart"),
            # unless the quotation's pieces are not words this source uses ("bet ter", a word the conversion split)
            if "".join(q) == "".join(pg) and len(q) > len(pg) and all(vocab.get(w, 0) >= 3 for w in q):
                continue
            diffs.append({"quote": " ".join(q), "page": " ".join(pg)})
        elif tag in ("replace", "delete"):
            q = a[i1:i2]
            near = b[max(0, j1 - 3):j2 + 3]   # the alignment can lose a split word's place: look for it whole close by
            whole = "".join(q)
            found = whole if len(q) > 1 and whole in near else None
            edge = "start" if i1 == 0 else "end" if i2 == len(a) else None
            diffs.append({"quote": " ".join(q), "page": found, **({"edge": edge} if edge and not found else {})})
    return {"checked": True, "differences": diffs}


def trim_edges(sp, most=6):
    """Words at a quotation's start or end that its printed page doesn't have are converter debris
    (a column label, a running head, a heading run into the paragraph): trim them, and record it."""
    for d in sp["page_check"].get("differences", []):
        if not d.get("edge") or len(d["quote"].split()) > most: continue
        words = r"[^\w]+".join(re.escape(w).replace("'", "['’]") for w in d["quote"].split())
        pat = (r"(?i)^\W*" + words + r"\W*") if d["edge"] == "start" else (r"(?i)\W*" + words + r"\W*$")
        new = re.sub(pat, "", sp["text"], count=1).strip()
        if new and new != sp["text"]:
            sp["text"] = new[0].upper() + new[1:] if d["edge"] == "start" else new
            d["trimmed"] = True


def heal_splits(sp):
    """Where the conversion split a word the printed page has whole ("bet ter" for "better"), set
    the quotation to the page's word and record it. Nothing else in a quotation is ever changed."""
    for d in sp["page_check"].get("differences", []):
        q, pg = d["quote"].split(), (d["page"] or "").split()
        if not pg or "".join(q) != "".join(pg) or len(q) <= len(pg): continue
        pat = r"(?i)(?<!\w)" + r"[\s\-]+".join(re.escape(w).replace("'", "['’]") for w in q) + r"(?!\w)"
        # "bet ter" was one word on the page; "self- motivated" keeps its hyphen and loses only the space
        new = re.sub(pat, lambda m: re.sub(r"\s+", "", m.group(0)), sp["text"], count=1)
        if new != sp["text"]:
            sp["text"] = new; d["corrected"] = True


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


def _toks(s):
    return re.findall(r"[a-z0-9]+", _norm(s).lower())


def span_boxes(page, text, fitz, cont=False):
    """One box per printed line of the span on this page, whether it runs past the page, and how
    many of its words the page held. Finds where the span's opening words start in the page's own
    word list and where its closing words end, and boxes every word between, so a line-end hyphen
    or a curly quote inside the span cannot cut the highlight short. A span that runs on past the
    page is boxed to the page's last word; `cont` boxes its rest on the next page, past the
    running head."""
    pw = page.get_text("words")   # (x0, y0, x1, y1, word, block, line, word_no), in reading order
    flat = [(t, wi) for wi, w in enumerate(pw) for t in _toks(w[4])]
    toks, st = [t for t, _ in flat], _toks(text)
    if len(st) < 4 or not toks:
        return [], False, 0

    def find(seq, lo=0):
        for i in range(lo, len(toks) - len(seq) + 1):
            if toks[i:i + len(seq)] == seq:
                return i
        return None

    offs = range(0, 16) if cont else (0, 1, 2, 3)
    start = next(((i if cont else max(0, i - off)) for off in offs if (i := find(st[off:off + 4])) is not None), None)
    if start is None:
        return [], False, 0
    end = None
    for off in (0, 1, 2, 3, 5, 8):
        seq = st[len(st) - 4 - off:len(st) - off]
        if len(seq) < 4:
            break
        i = find(seq, start)
        if i is not None and i - start <= len(st) + 20:
            end = i + 3 + off; break
    past = end is None and start + len(st) > len(toks)
    end = min(len(toks) - 1, end if end is not None else start + len(st) - 1)
    lines = {}
    for wi in sorted({flat[k][1] for k in range(start, end + 1)}):
        x0, y0, x1, y1, _, b, ln, _ = pw[wi]
        r = lines.get((b, ln))
        lines[(b, ln)] = [x0, y0, x1, y1] if r is None else [min(r[0], x0), min(r[1], y0), max(r[2], x1), max(r[3], y1)]
    return [fitz.Rect(*r) for r in lines.values()], past, end - start + 1


def page_pixmap(doc, i, quads, fitz, zoom, tint=(1.0, 0.85, 0.35)):
    """Page i as a pixmap, with the passage highlighted in the image itself (each box multiplied
    by a highlighter tint), so the PNG shows it wherever it is opened. Works the same for a PDF
    and an EPUB, and never touches the original."""
    pix = doc[i].get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    if not quads:
        return pix
    w, h, n = pix.width, pix.height, pix.n
    buf = bytearray(pix.samples)
    for q in quads:
        r = fitz.Rect(q) * fitz.Matrix(zoom, zoom)
        x0, x1 = max(0, int(r.x0)), min(w, int(r.x1) + 1)
        for y in range(max(0, int(r.y0)), min(h, int(r.y1) + 1)):
            row = y * pix.stride
            for c in range(min(n, 3)):
                seg = slice(row + x0 * n + c, row + x1 * n + c, n)
                buf[seg] = bytes(int(v * tint[c]) for v in buf[seg])
    return fitz.Pixmap(pix.colorspace, w, h, bytes(buf), False)


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
    conv = out / "converted" / f"{sid}.md"
    vocab = Counter(_words(conv.read_text(encoding="utf-8", errors="replace"))) if conv.exists() else Counter()
    for span_id, sp in spans:
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
        quads, past, held = span_boxes(page, sp["text"], fitz)
        # a span that runs over the page break is lit on the next page too
        next_quads = span_boxes(doc[hit + 1], " ".join(_toks(sp["text"])[held:]), fitz, cont=True)[0] if past and hit + 1 < doc.page_count else []
        quads = quads or page.search_for(_norm(sp["text"])) or page.search_for(" ".join(words[:12])) or page.search_for(found_q)
        if not quads:   # the page sets the span differently from the extraction (hyphens, ligatures): box it in five-word pieces
            for k in range(0, len(words), 5):
                piece = " ".join(words[k:k + 5])
                quads += page.search_for(piece) or page.search_for(piece.replace("'", "’"))
        frac = lambda qs, r: [[(q.x0 - r.x0) / r.width, (q.y0 - r.y0) / r.height, (q.x1 - r.x0) / r.width, (q.y1 - r.y0) / r.height] for q in qs]
        boxes = frac(quads, rect)
        sp["hit_page"] = hit + 1; sp["pages"] = []; sp["page_layout"] = "epub-reflow" if is_epub else "pdf"
        if sp.get("show") != "paraphrase":
            sp["page_check"] = page_check(doc, hit, sp["text"], fitz, vocab)
            heal_splits(sp)
            trim_edges(sp)
        for i in range(max(0, hit - window), min(doc.page_count, hit + window + 1)):
            # a page carrying this span's highlight is the span's own file; the pages either side are shared
            lit = quads if i == hit else next_quads if i == hit + 1 else []
            png = pages_dir / (f"{sid}-{i + 1}-{span_id}.png" if lit else f"{sid}-{i + 1}.png")
            if True:   # always: a replaced original or a new layout must not show stale pages
                page_pixmap(doc, i, lit, fitz, zoom).save(str(png)); rendered += 1
            txt = doc[i].get_text().strip().split("\n")
            folio = None
            for cand in (txt[:3] + txt[-3:]):
                cand = cand.rstrip()
                m = re.fullmatch(r"\s*(\d{1,4})\s*", cand) or re.match(r"^\s*(\d{1,4})\s{2,}\S", cand) or re.search(r"\S\s{2,}(\d{1,4})$", cand) or re.match(r"^\s*(\d{1,4})\s+\d+\s+•", cand) or re.search(r"•.*\s(\d{1,4})$", cand)
                if m and len(cand) < 120 and not is_epub:
                    n = int(m.group(1))
                    if i - 60 <= n <= i + 1:   # a printed folio never exceeds the PDF page index by more than the cover
                        folio = n; break
            sp["pages"].append({"n": i + 1, "png": f"pages/{png.name}", "boxes": frac(lit, doc[i].rect) if lit else [], "folio": folio})
            if i == hit and folio is not None and not sp.get("page"):
                sp["page"], sp["page_via"] = folio, "the folio printed on the PDF page"
        print(f"  {sid}: span on {'EPUB' if is_epub else 'PDF'} page {hit + 1} (printed p. {sp.get('page')}), {len(boxes)} highlight boxes{f', {len(next_quads)} more on the next page' if next_quads else ''}", file=sys.stderr)
    return rendered


def figure_by_page(root, source, caption, fitz):
    """The image for a figure the image index files by PDF page rather than by name: find the
    page of the original that carries the caption, and take the one index entry for that page."""
    pdf = root / (source.get("original") or "")
    idx = root / "sources/converted/IMAGE-INDEX.yaml"
    if not (pdf.is_file() and pdf.suffix.lower() == ".pdf" and idx.exists()):
        return None
    probe = _norm(" ".join(caption.split()[:8])).lower()
    doc = fitz.open(str(pdf))
    hits = [i for i in range(doc.page_count) if probe in _norm(doc[i].get_text()).lower()]
    if len(hits) != 1:
        return None
    entries = []
    for block in re.split(r"\n(?=- )", idx.read_text(encoding="utf-8", errors="replace")):
        ref = re.search(r"^\s*source_ref:\s*(\S+)", block, re.M)
        page = re.search(r"^\s*page:\s*(\d+)\s*$", block, re.M)
        file = re.search(r"^-?\s*file:\s*(\S+)", block, re.M)
        if ref and page and file and ref.group(1) == source["slug"] and int(page.group(1)) == hits[0] + 1:
            entries.append(file.group(1))
    if len(entries) != 1:
        return None
    return f"sources/converted/{entries[0]}", f"caption on PDF page {hits[0] + 1}; the image index's one entry for that page"


def copy_if_changed(src, dst):
    if not dst.exists() or dst.stat().st_size != src.stat().st_size or dst.stat().st_mtime < src.stat().st_mtime:
        shutil.copyfile(src, dst)


def render(out, init, pages_only=False, gemini=None):
    report = json.loads((out / "report.json").read_text())
    bundle = json.loads((out / "bundle.json").read_text())
    root_of = lambda corpus: REPO / bundle["corpora"][corpus]["root"]

    vdir = out / "vendor"; vdir.mkdir(exist_ok=True)
    for f in (HERE / "vendor").iterdir():
        copy_if_changed(f, vdir / f.name)

    fitz = load_fitz()
    figdir = out / "figures"; figdir.mkdir(exist_ok=True)
    for sid, span in bundle.get("spans", {}).items():
        fig = span.get("figure")
        if fig and not fig.get("image") and fig.get("caption") and fitz is not None:
            source = bundle["sources"][span["source"]]
            found = figure_by_page(root_of(source["corpus"]), source, fig["caption"], fitz)
            if found:
                fig["image"], fig["via"] = found
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
        src["original_omitted"] = pages_only
        if not src.get("original"):
            continue
        f = root_of(src["corpus"]) / src["original"]
        if f.exists() and f.suffix.lower() in (".pdf", ".epub"):
            dst = odir / f"{sid}{f.suffix.lower()}"
            if pages_only:
                dst.unlink(missing_ok=True)
            else:
                copy_if_changed(f, dst)
                src["served"] = f"originals/{dst.name}"
            if fitz is not None:
                pages += prerender_pages(out, sid, f, [(k, s) for k, s in bundle["spans"].items() if s.get("source") == sid and s.get("verified")], fitz)
        else:
            print(f"original not servable: {f}", file=sys.stderr)
    if not any(odir.iterdir()):
        odir.rmdir()

    if gemini:
        cap = out / "gemini-capture.md"
        if Path(gemini).resolve() != cap.resolve():
            shutil.copyfile(gemini, cap)
        from gemini import write as write_gemini
        g = write_gemini(cap, out)
        init = {**init, "gemini": "gemini.html"}
        print(f"wrote {out / 'gemini.html'}: {g['markers']} markers, {g['citations']} citations" + (f"; no passage captured for {g['uncaptured']}" if g["uncaptured"] else ""), file=sys.stderr)
    (out / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=1))   # with the served files and page images, for anything that reads the folder
    html = (HERE / "template.html").read_text()
    for marker, value in (("/*__REPORT__*/", report), ("/*__BUNDLE__*/", bundle), ("/*__INIT__*/", init)):
        html = html.replace(marker, json.dumps(value, ensure_ascii=False).replace("</", "<\\/"))
    (out / "preview.html").write_text(html)
    from flatten import flatten   # the plain-prose answer, from the same bundle as the page
    (out / "answer.md").write_text(flatten(out)[0])
    with_pages = sum(1 for s in bundle["spans"].values() if s.get("pages"))
    for k, sp in bundle["spans"].items():
        d = sp.get("page_check", {}).get("differences", [])
        if d:
            print(f"  page check {k}: " + "; ".join(f"{x['quote']!r} on the page {x['page']!r}" + (" (corrected)" if x.get("corrected") else "") if x["page"] else f"{x['quote']!r} not on the page" for x in d), file=sys.stderr)
    print(f"wrote {out / 'preview.html'}: {with_pages} of {len(bundle['spans'])} spans have pre-rendered pages ({pages} new PNGs)", file=sys.stderr)
    return {"spans_with_pages": with_pages, "new_pngs": pages}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path, help="report folder holding report.json and bundle.json")
    ap.add_argument("--verbatim", type=float, default=None, help="opening share of ranked spans shown as the author's words, 0..1 (default 1)")
    ap.add_argument("--joins", choices=("essay", "minimal"), default=None, help="opening join form (default: the report's mode.joins, else essay)")
    ap.add_argument("--context", default=None, choices=("paras:0", "paras:1", "paras:2"), help="opening context for a clicked span: its paragraph, and 0, 1 or 2 paragraphs either side (default paras:1)")
    ap.add_argument("--ship", action="store_true", help="open as it would ship: copyrighted sources paraphrased under max_visibility open-nc")
    ap.add_argument("--passages", action="store_true", help="open with each pointed paraphrase shown as the author's passage it rests on")
    ap.add_argument("--pages-only", action="store_true", help="leave the original PDFs and EPUBs out of the folder; keep the page images (the hit page and two either side)")
    ap.add_argument("--gemini", type=Path, default=None, metavar="CAPTURE", help="a captured Gemini Notebook answer to the same question (markdown, see gemini.py): write gemini.html beside the page and link the two")
    args = ap.parse_args()
    out = args.folder.resolve()
    report = json.loads((out / "report.json").read_text())
    init = {"verbatim": args.verbatim if args.verbatim is not None else 1.0,
            "joins": args.joins or report.get("mode", {}).get("joins", "essay"),
            "ctx": args.context or "paras:1", "ship": args.ship, "passages": args.passages}
    if init["joins"] not in ("essay", "minimal"):
        init["joins"] = "essay"
    render(out, init, args.pages_only, args.gemini)


if __name__ == "__main__":
    main()
