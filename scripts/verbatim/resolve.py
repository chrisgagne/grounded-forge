#!/usr/bin/env python3
"""Deterministic resolver for verbatim mode.

    python3 scripts/verbatim/resolve.py <report-folder>

Reads <report-folder>/report.json (the model's joins, each placeholder carrying a
source ID and an anchor of 8 to 12 words), finds every anchor in the source's
converted text, expands the hit to sentence boundaries, and writes
<report-folder>/bundle.json: the span's exact text, its line, locator, page marker,
context, the provenance layers (deep ref with marker, light ref, distillations) and
the source's figure where the passage names one.

No model in the loop. A span whose anchor is not found is recorded with status
"not-found" and never rendered as a quotation. The contract the report must meet is
scripts/verbatim/contract.md.
"""
import argparse, bisect, datetime, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
TIERS = (("corpus.commons", "open-nc"), ("corpus.local", "copyrighted"))
ABBR = {"u.s", "e.g", "i.e", "dr", "mr", "mrs", "ms", "vs", "no", "p", "pp", "fig", "st", "jr", "sr", "etc", "cf", "ch", "vol", "inc", "co", "ed", "eds", "al", "prof", "gen", "gov", "sen", "rep", "lt", "col", "capt", "sgt", "mt", "ft", "approx", "dept", "fig", "figs", "op", "ibid"}
PARA_BREAK = re.compile(r"\n[ \t]*\n")
SOFT_PARA_WORDS = 300   # a blank-line block longer than this is checked for paragraph ends the conversion lost
TERMINAL = re.compile(r"[.!?][\"”’')\]]*(?=\s|$)")


def corpus_info(name):
    """A corpus by bare name: corpus.commons/{name} (ceiling open-nc), else corpus.local/{name}."""
    for tier, ceiling in TIERS:
        root = REPO / tier / name
        if root.is_dir():
            return {"root": f"{tier}/{name}", "tier": tier, "ceiling": ceiling}
    raise SystemExit(f"corpus {name!r} not found under corpus.commons/ or corpus.local/")


# ---------- text cleaning (Pandoc span noise) ----------
def clean(line: str) -> str:
    s = line
    s = re.sub(r"\[\]\{#[^}]*\}", "", s)                     # []{#anchor}
    s = re.sub(r"\[\(\d+\)\]\(#[^)]*\)", "", s)              # [(3)](#note)
    s = re.sub(r"\[([^\[\]]*?)\]\{\.[^}]*\}", r"\1", s)       # [text]{.class}
    s = re.sub(r"\[([^\[\]]*?)\]\{\.[^}]*\}", r"\1", s)       # nested once more
    s = re.sub(r"\{[#.][^}]*\}", "", s)                        # stray {.class} and {#id}
    s = re.sub(r"\[([^\[\]]*?)\]\(#[^)]*\)", r"\1", s)        # [text](#link)
    s = re.sub(r"(?<!!)\[([^\[\]]+?)\]\((?:https?:|mailto:|www\.)[^)]*\)", r"\1", s)   # [text](https://…)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)                # images
    s = re.sub(r"(?<!\w)[*_]{1,3}(?=\S)", "", s); s = re.sub(r"(?<=\S)[*_]{1,3}(?!\w)", "", s)  # emphasis
    s = s.replace("\\", "")
    return s


FOLD = {"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", "­": "", "ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "\u00a0": " ", "\u200b": ""}


def build_norm(text: str, loose=False):
    """Normalised string plus maps from each normalised index to the original start and end.

    exact: quotes, dashes, ligatures, soft hyphens and whitespace folded, case folded.
    loose: as exact, and a hyphen at a line end between two letters rejoins the word, and
           every character that is not a letter or digit becomes a space, except a sign
           written against a number (-5, +5), which is kept.
    The same function normalises the source and the anchor, so the two always agree.
    """
    out, starts, ends = [], [], []
    i, n = 0, len(text)
    prev_space = True
    def emit(ch, a, b):
        nonlocal prev_space
        if ch == " ":
            if not prev_space:
                out.append(" "); starts.append(a); ends.append(b)
            prev_space = True
        else:
            out.append(ch); starts.append(a); ends.append(b); prev_space = False
    while i < n:
        if loose and text[i] in "-\u00ad" and i > 0 and text[i - 1].isalpha():
            j = i + 1
            while j < n and text[j] in " \t": j += 1
            if j < n and text[j] == "\n":
                j += 1
                while j < n and text[j] in " \t": j += 1
                if j < n and text[j].isalpha() and (text[j].islower() or text[i - 1].isupper()):
                    i = j; continue
        if text.startswith("---", i): c, step = "-", 3
        elif text.startswith("--", i): c, step = "-", 2
        else: c, step = FOLD.get(text[i], text[i]), 1
        if loose and c in "-+" and i + step < n and text[i + step].isdigit():
            emit(c, i, i + step); i += step; continue
        for ch in c.lower():
            if ch.isspace() or (loose and not ch.isalnum()): emit(" ", i, i + step)
            else: emit(ch, i, i + step)
        i += step
    while out and out[-1] == " ": out.pop(); starts.pop(); ends.pop()
    return "".join(out), starts, ends


def norm_query(q: str, loose=False) -> str:
    return build_norm(q.strip(), loose)[0].strip()


# ---------- a converted source ----------
class Source:
    def __init__(self, sid, meta, corpora):
        self.id = sid; self.meta = meta
        self.corpus = meta["corpus"]; self.root = REPO / corpora[self.corpus]["root"]
        self.slug = meta["slug"]
        self.converted = meta["converted"]
        self.raw_lines = (self.root / self.converted).read_text(encoding="utf-8", errors="replace").split("\n")
        self.lines = [clean(l) for l in self.raw_lines]
        nonempty = sorted(len(l) for l in self.lines if l.strip())
        self.line_is_para = (nonempty[len(nonempty) // 2] if nonempty else 0) > 180   # one paragraph per line
        self.joined = "\n".join(self.lines)
        self.line_starts = []; pos = 0
        for l in self.lines:
            self.line_starts.append(pos); pos += len(l) + 1
        self.norm, self.nmap, self.nend = build_norm(self.joined)
        self._loose = None
        self.words = sum(len(l.split()) for l in self.lines)

    def line_of(self, off): return bisect.bisect_right(self.line_starts, off) - 1

    @staticmethod
    def _hits(norm, q):
        """Every match of q in norm that starts and ends on a word boundary, overlaps included."""
        out, at = [], norm.find(q)
        while at >= 0:
            before = norm[at - 1] if at else " "
            after = norm[at + len(q)] if at + len(q) < len(norm) else " "
            if not (before.isalnum() and q[0].isalnum()) and not (after.isalnum() and q[-1].isalnum()):
                out.append(at)
            at = norm.find(q, at + 1)
        return out

    def find(self, anchor):
        """(start, end, level, hits) of the first boundary-valid hit, or None. Levels: exact, then loose.
        hits counts every boundary-valid occurrence; more than one means the anchor is ambiguous."""
        q = norm_query(anchor)
        hits = self._hits(self.norm, q) if q else []
        if hits:
            at = hits[0]
            return self.nmap[at], self.nend[at + len(q) - 1], "exact", len(hits)
        if self._loose is None:
            self._loose = build_norm(self.joined, loose=True)
        lnorm, lmap, lend = self._loose
        q = norm_query(anchor, loose=True)
        if len(q.split()) < 6:      # too short to place loosely without a false hit
            return None
        hits = self._hits(lnorm, q)
        if not hits:
            return None
        at = hits[0]
        return lmap[at], lend[at + len(q) - 1], "loose", len(hits)

    def para_bounds(self, start, end):
        if self.line_is_para:
            ls, le = self.line_of(start), self.line_of(end - 1)
            return self.line_starts[ls], self.line_starts[le] + len(self.lines[le])
        breaks = [m.end() for m in PARA_BREAK.finditer(self.joined, 0, start)]
        a = breaks[-1] if breaks else 0
        m = PARA_BREAK.search(self.joined, end)
        b = m.start() if m else len(self.joined)
        if len(self.joined[a:b].split()) > SOFT_PARA_WORDS:
            a, b = self.soft_para(a, b, start, end)
        return a, b

    def soft_para(self, a, b, start, end):
        """Some PDF conversions keep the printed lines but drop the blank line between paragraphs,
        so a chapter reads as one block. Inside such a block a paragraph still ends on a short line
        that closes a sentence and is followed by a capitalised line: narrow [a, b) to that one."""
        first, last = self.line_of(a), self.line_of(b - 1)
        widths = sorted(len(self.lines[i].rstrip()) for i in range(first, last + 1) if self.lines[i].strip())
        width = widths[len(widths) // 2]
        ends = [i for i in range(first, last)
                if len(self.lines[i].rstrip()) < 0.8 * width
                and re.search(r"[.!?:][\"”’')\]]*$", self.lines[i].rstrip())
                and re.match(r"\s*[\"“‘'(]?[A-Z0-9]", self.lines[i + 1])]
        s_line, e_line = self.line_of(start), self.line_of(end - 1)
        before = [i for i in ends if i < s_line]
        after = [i for i in ends if i >= e_line]
        na = self.line_starts[before[-1] + 1] if before else a
        nb = self.line_starts[after[0]] + len(self.lines[after[0]]) if after else b
        return max(a, na), min(b, nb)

    def sentence_span(self, start, end, sentences=1):
        """Expand [start, end) to whole sentences inside its paragraph: back to the start of
        the sentence holding `start`, forward through `sentences` sentence ends counted from
        the sentence holding the anchor's last character."""
        pa, pb = self.para_bounds(start, end)
        text = self.joined
        s = pa
        for m in re.finditer(r"[.!?][\"”’')\]]*\s+", text[pa:start]):
            if not self._abbr(text, pa + m.start()):
                s = pa + m.end()
        e = end; count = 0
        tail = re.search(r"[.!?][\"”’')\]]*$", text[max(start, end - 4):end])
        if tail and not self._abbr(text, max(start, end - 4) + tail.start()):
            count = 1
        while count < sentences:
            m = TERMINAL.search(text, e, pb)
            if not m: e = pb; break
            e = m.end()
            if self._abbr(text, m.start()):
                continue
            count += 1
            if count >= sentences: break
        return s, min(e, pb)

    def _abbr(self, text, dot):
        if text[dot] != ".": return False
        w = re.search(r"(\S+)$", text[max(0, dot - 12):dot])
        if not w: return False
        tok = w.group(1).lower().strip("(\"'“‘[")
        if tok in ABBR or re.fullmatch(r"[a-z]", tok): return True
        # a decimal or a list number ("3.5", "1."), not a number that ends a sentence ("in 1984.")
        return bool(re.fullmatch(r"\d+", tok)) and dot + 1 < len(text) and text[dot + 1].isdigit()

    def paragraphs(self, start, end, k=2):
        """k paragraphs before and after the span's paragraph."""
        if self.line_is_para:
            ls, le = self.line_of(start), self.line_of(end - 1)
            before = [l for l in self.lines[max(0, ls - 12):ls] if l.strip()][-k:]
            after = [l for l in self.lines[le + 1:le + 13] if l.strip()][:k]
            return "\n\n".join(before), "\n\n".join(after)
        pa, pb = self.para_bounds(start, end)
        text = self.joined; before, after = [], []
        # step one paragraph at a time through para_bounds, so breaks the conversion lost count too
        a = pa
        for _ in range(k):
            p = len(text[:a].rstrip()) - 1
            if p < 0: break
            a, z = self.para_bounds(p, p + 1)
            before.insert(0, text[a:z])
        z = pb
        for _ in range(k):
            q = len(text) - len(text[z:].lstrip())
            if q >= len(text): break
            a, z = self.para_bounds(q, q + 1)
            after.append(text[a:z])
        soft = lambda p: re.sub(r"\s*\n\s*", " ", p.strip())
        return "\n\n".join(soft(p) for p in before), "\n\n".join(soft(p) for p in after)

    def own_paragraph(self, s, e):
        """The rest of the span's own paragraph, before and after the span."""
        pa, pb = self.para_bounds(s, e)
        soft = lambda p: re.sub(r"\s*\n\s*", " ", p).strip()
        return soft(self.joined[pa:s]), soft(self.joined[e:pb])

    def locator(self, line):
        for i in range(line, max(-1, line - 400), -1):
            l = self.lines[i].strip()
            m = re.match(r"^#{1,6}\s+(.+)", l)
            if m: return m.group(1).strip()
            m = re.match(r"^(\d+\.\d+)\s+•\s+(.+?)\s{2,}\d+\s*$", l) or re.match(r"^\d+\s{2,}(\d+)\s+•\s+(.+)$", l)
            if m: return f"Ch {m.group(1)} • {m.group(2).strip()}" if "." in m.group(1) else f"Ch {m.group(1)}, {m.group(2).strip()}"
        # a report or textbook PDF: the nearest numbered all-caps section heading
        if not self.line_is_para:
            for i in range(line, max(-1, line - 2500), -1):
                l = self.lines[i].strip()
                m = re.match(r"^(\d+(?:\.\d+)?)\s+([A-Z][A-Z0-9 \-:,'’]{4,60})$", l)
                if m and not re.search(r"\b(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\b", l):
                    return f"{m.group(1)} {m.group(2).title()}"
        # EPUB conversions without markdown headings: a styled chapter title, else the nearest short title-like line
        for i in range(line, max(-1, line - 400), -1):
            m = re.search(r"\[([^\]]{3,90})\]\{\.(?:chapter-title|h\d|heading|title)[^}]*\}", self.raw_lines[i])
            if m: return m.group(1).strip()
        # a short all-caps line is a heading; one the book wraps over two lines is joined
        caps = lambda t: len(re.findall(r"[A-Za-z]", t)) >= 6 and len(t) < 70 and sum(c.isupper() for c in t if c.isalpha()) >= 0.9 * len(re.findall(r"[A-Za-z]", t))
        for i in range(line, max(-1, line - 120), -1):
            l = self.lines[i].strip()
            if i < line and caps(l):
                above, below = self.lines[i - 1].strip() if i else "", self.lines[i + 1].strip()
                return f"{above} {l}" if caps(above) else (f"{l} {below}" if caps(below) else l)
            isolated = (i + 1 >= len(self.lines) or not self.lines[i + 1].strip()) and (i == 0 or not self.lines[i - 1].strip())
            if 2 < len(l) < 70 and re.search(r"[A-Za-z]{3}", l) and not re.search(r"[.!?:;,]$", l) and not re.match(r"^(Fig\.|Figure|Table|---|:::|\[|!|>|\d)", l) and l.lower() not in ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten") and len(l.split()) <= 9 and (isolated or (self.line_is_para and not re.search(r"[.!?]\s", l))):
                if l[0].islower() and i > 0 and 0 < len(self.lines[i - 1].strip()) < 70:   # a heading wrapped onto two lines
                    l = self.lines[i - 1].strip() + " " + l
                return l
        return ""

    def page(self, line, text=None):
        """The printed page the converter kept, if any: a Pandoc EPUB page-break anchor
        ({#page_12}, {#ch3.xhtml_page_101 .pagebreak}; not {#homepage_12}), an epub:type
        pagebreak, or an OpenStax running header. A bare number on a line is not trusted (it may
        be a footnote, a list number, or the folio of the page before), so for a PDF the renderer
        reads the printed page off the PDF page it finds the span on instead."""
        marker = re.compile(r"\{#(?:[^}\s]*[_.])?(?:page|pg)[_-]?(\d+)\b[^}]*\}|pagebreak[^>]*?(?:title|aria-label)=\"(\d+)\"", re.I)
        for i in range(line, max(-1, line - 120), -1):
            raw = self.raw_lines[i]
            found = list(marker.finditer(raw))
            if i == line and text and found:   # on the span's own line, a marker after the span starts the next page
                at = raw.find(" ".join(text.split()[:4]))
                if at >= 0:
                    found = [m for m in found if m.start() < at]
            if found:
                m = found[-1]
                return int(m.group(1) or m.group(2))
            l = self.lines[i].strip()
            m = re.match(r"^\d+\.\d+\s+•\s+.+?\s{2,}(\d+)\s*$", l) or re.match(r"^(\d+)\s{2,}\d+\s+•\s+", l)
            if m: return int(m.group(1))
        return None

    def chapters(self):
        out = []
        for i, l in enumerate(self.lines):
            m = re.match(r"^#{1,2}\s+(.+)", l.strip())
            if m: out.append({"title": m.group(1).strip()[:60], "line": i + 1})
        if not out:
            for i, l in enumerate(self.lines):
                if re.match(r"^(CHAPTER|Chapter)\s+\d+\b", l.strip()): out.append({"title": l.strip()[:60], "line": i + 1})
        if len(out) > 40:
            out = [c for c in out if not re.match(r"^\d+\.\d+", c["title"])] or out
        return out[:40]

    def grep_layer(self, relpath, keywords):
        p = self.root / relpath
        if not p.exists(): return None
        lines = p.read_text(encoding="utf-8", errors="replace").split("\n")
        for need in (len(keywords), max(2, len(keywords) - 1), 1):
            for i, l in enumerate(lines):
                low = l.lower()
                if sum(1 for k in keywords if k in low) >= need and len(l.strip()) > 20:
                    m = re.search(r"\[(V|AP|AR|AE|BT)\]", l)
                    return {"path": relpath, "line": i + 1, "text": re.sub(r"\s+", " ", l.strip())[:420], "marker": m.group(1) if m else None, "match": f"{need} of {len(keywords)} keywords"}
        return None

    def figure(self, name):
        """A figure the passage names: its caption line and, through the image index, its file."""
        cap = None
        for i, l in enumerate(self.lines):
            if re.match(rf"^\s*{re.escape(name)}\b", l.strip()) and not l.strip().endswith("shows"):
                cap = {"line": i + 1, "caption": l.strip()[:300]}; break
        img = None
        for idx in (self.root / "sources/converted/IMAGE-INDEX.yaml", REPO / "docs/images" / f"_ingest_image_index_{self.slug}.yaml"):
            if not idx.exists(): continue
            txt = idx.read_text(encoding="utf-8", errors="replace")
            for block in re.split(r"\n(?=- )", txt):
                if self.slug in block and re.search(rf"\b{re.escape(name)}\b", block, re.I):
                    m = re.search(r"(sources/converted/\S+?\.(?:png|jpe?g))", block) or re.search(r"(path|file|image):\s*(\S+)", block)
                    if m: img = m.group(1) if m.lastindex == 1 else m.group(2); break
            if img: break
        if cap is None and img is None: return None
        return {"name": name, "image": img, "caption": cap["caption"] if cap else None, "line": cap["line"] if cap else None}


_REFINDEX = {}


def sidecar(root, slug):
    """Title, author, year, scope and licence from the source's sidecar, with the corpus's
    reference-index.json filling any the sidecar lacks."""
    if root not in _REFINDEX:
        ri = root / "reference-index.json"
        _REFINDEX[root] = {v["slug"]: v for v in json.loads(ri.read_text()).get("refs", {}).values()} if ri.exists() else {}
    meta = {k: v for k, v in (("title", _REFINDEX[root].get(slug, {}).get("title")), ("author", _REFINDEX[root].get(slug, {}).get("author")),
                              ("publish_year", _REFINDEX[root].get(slug, {}).get("year")), ("scope", _REFINDEX[root].get(slug, {}).get("scope"))) if v}
    p = root / "sources/original" / f"{slug}.source.md"
    if p.exists():
        m = re.match(r"^---\n(.*?)\n---", p.read_text(encoding="utf-8", errors="replace"), re.S)
        if m:
            for l in m.group(1).split("\n"):
                mm = re.match(r"^(\w+):\s*(.*)$", l)
                if mm: meta[mm.group(1)] = mm.group(2).strip().strip("'\"")
    return meta


def find_converted(root, slug):
    """The converted file for a slug when the report did not name one that exists."""
    direct = root / "sources/converted" / f"{slug}.md"
    if direct.exists(): return str(direct.relative_to(root))
    for p in (root / "sources/original" / f"{slug}.source.md", root / "references" / f"{slug}-deep.md"):
        if p.exists():
            m = re.search(r"(sources/converted/[^)`\]\n]+?\.md)", p.read_text(encoding="utf-8", errors="replace"))
            if m and (root / m.group(1)).exists(): return m.group(1)
    return None


def find_original(root, slug, converted, sc):
    """The redistributable or held original for a source: named after the converted file or the
    slug, else the one PDF or EPUB whose file name carries the author's surname and two words of
    the title (originals keep their download names). None when no single file matches."""
    files = [p for p in (root / "sources/original").glob("*") if p.suffix.lower() in (".pdf", ".epub")]
    stem = Path(converted).stem
    for p in files:
        if p.stem in (stem, slug): return str(p.relative_to(root)), "file name"
    surname = re.split(r"[,;]", sc.get("author", ""))[0].strip().split(" ")[-1].lower()
    words = [w for w in re.findall(r"[a-z]{4,}", sc.get("title", "").lower()) if w not in {"with", "from", "that", "this", "their", "what", "into"}][:4]
    if not surname or len(words) < 2: return None, None
    fold = lambda t: t.lower().replace("ö", "o").replace("ü", "u").replace("ä", "a")
    hits = [p for p in files if fold(surname) in fold(p.name) and sum(w in fold(p.name) for w in words) >= min(2, len(words))]
    return (str(hits[0].relative_to(root)), "author and title in the file name") if len(hits) == 1 else (None, None)


def keywords(anchor):
    ws = [w.strip(".,;:'\"()[]-").lower() for w in anchor.split()]
    ws = [w for w in ws if len(w) >= 6 and w not in {"because", "through", "between", "without", "another", "against", "something"}]
    ws.sort(key=len, reverse=True)
    return ws[:3] or [w for w in anchor.lower().split() if len(w) >= 4][:3]


def placeholders(report):
    for sec in report["sections"]:
        for j in sec["joins"]:
            if not isinstance(j, str): yield j


def check_sources(report, corpora):
    """Each source ID must be that slug's ID in its corpus's slug table, and its converted file must exist."""
    problems = []
    tables = {}
    for sid, meta in report["sources"].items():
        c = meta.get("corpus")
        if c not in corpora:
            problems.append(f"{sid}: corpus {c!r} is not one of {sorted(corpora)}"); continue
        root = REPO / corpora[c]["root"]
        if c not in tables:
            tables[c] = json.loads((root / "references/slug-table.json").read_text())["slugs"]
        if tables[c].get(sid) != meta.get("slug"):
            want = next((k for k, v in tables[c].items() if v == meta.get("slug")), None)
            problems.append(f"{sid}: slug-table says {tables[c].get(sid)!r}, report says {meta.get('slug')!r}" + (f" (that slug is {want})" if want else ""))
        conv, canon = meta.get("converted"), find_converted(root, meta.get("slug", ""))
        inside = bool(conv) and (root / conv).resolve().is_relative_to((root / "sources/converted").resolve()) and (root / conv).is_file()
        if canon and conv != canon:
            if conv: problems.append(f"{sid}: converted path {conv!r} is not the slug's own; using {canon!r}")
            meta["converted"] = canon
        elif not canon and not inside:
            problems.append(f"{sid}: converted file not found ({conv!r})")
        elif not canon:
            meta["converted_unconfirmed"] = True   # inside sources/converted/, but nothing names it as this slug's
    return problems


def check_chart(chart, spans):
    """A chart may only draw numbers its span states: every series value, and every number
    in a series label, must appear in the span's placed text."""
    sp = spans.get(chart.get("span"))
    if not sp or not sp.get("verified"):
        return f"its span {chart.get('span')!r} was not placed"
    if chart.get("kind") not in ("growth", "bars"):
        return f"unknown chart kind {chart.get('kind')!r}"
    nums = {f"{float(n):g}" for n in re.findall(r"\d+(?:\.\d+)?", sp["text"].replace(",", ""))}
    drawn = []
    for s in chart.get("series", []):
        drawn.append(s.get("value"))
        drawn += re.findall(r"\d+(?:\.\d+)?", str(s.get("label", "")))
    if not drawn: return "it draws no numbers"
    missing = [str(v) for v in drawn if v is None or f"{float(v):g}" not in nums]
    if missing: return "numbers not in the passage: " + ", ".join(missing)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path, help="report folder holding report.json")
    args = ap.parse_args()
    folder = args.folder.resolve()
    report = json.loads((folder / "report.json").read_text())
    corpora = {c: corpus_info(c) for c in sorted({m["corpus"] for m in report["sources"].values()} | set(report.get("mode", {}).get("corpora", [])))}
    ids = [j["span"] for j in placeholders(report)]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    if dupes:
        raise SystemExit(f"duplicate span IDs: {', '.join(dupes)}; every placeholder needs its own")
    problems = check_sources(report, corpora)
    for p in problems: print("SOURCE", p, file=sys.stderr)
    bad = {p.split(":")[0] for p in problems if "converted file not found" in p or "is not one of" in p}
    sources = {sid: Source(sid, m, corpora) for sid, m in report["sources"].items() if sid not in bad}
    out_sources, out_spans = {}, {}
    for sid, src in sources.items():
        sc = sidecar(src.root, src.slug)
        refs = {"deep": f"references/{src.slug}-deep.md", "light": f"references/{src.slug}.md", "distillations": {}}
        for d in sorted((src.root / "distillations").glob(f"*/{src.slug}-*.md")):
            refs["distillations"][d.parent.name] = str(d.relative_to(src.root))
        for k in ("deep", "light"):
            if not (src.root / refs[k]).exists(): refs[k] = None
        original, via = src.meta.get("original"), "report"
        if original and not (src.root / original).exists(): original = None
        if original is None:
            original, via = find_original(src.root, src.slug, src.converted, sc)
        out_sources[sid] = {"slug": src.slug, "corpus": src.corpus, "short": src.meta.get("short", ""), "title": sc.get("title", src.meta.get("title", src.slug)), "author": sc.get("author", src.meta.get("author", "")),
                            "year": int(re.sub(r"\D", "", str(sc.get("publish_year", src.meta.get("year", 0)))) or 0), "scope": sc.get("scope", src.meta.get("scope", "copyrighted")), "licence": sc.get("licence", src.meta.get("licence", "")),
                            "original": original, "original_via": via if original else None, "converted": src.converted, "lines": len(src.lines), "words": src.words, "chapters": src.chapters(), "refs": refs}
    for j in placeholders(report):
        sid = j["source"]; span_id = j["span"]
        if sid not in sources:
            out_spans[span_id] = {"source": sid, "corpus": report["sources"].get(sid, {}).get("corpus"), "status": "not-found", "verified": False, "anchor": j["anchor"], "note": f"source {sid} could not be opened"}
            print(f"NOT FOUND {span_id}: source {sid} unavailable", file=sys.stderr); continue
        src = sources[sid]
        hit = src.find(j["anchor"])
        if not hit:
            out_spans[span_id] = {"source": sid, "corpus": src.corpus, "status": "not-found", "verified": False, "anchor": j["anchor"], "note": f"anchor not found in {src.converted}"}
            print(f"NOT FOUND {span_id}: {j['anchor']!r}", file=sys.stderr); continue
        a, b, level, hits = hit
        s, e = src.sentence_span(a, b, sentences=max(1, min(4, int(j.get("sentences", 1)))))
        text = re.sub(r"\s*\n\s*", " ", src.joined[s:e]).strip()
        line = src.line_of(s) + 1
        before, after = src.paragraphs(s, e)
        own_b, own_a = src.own_paragraph(s, e)
        kws = keywords(j["anchor"])
        refs = out_sources[sid]["refs"]
        layers = {"deep": src.grep_layer(refs["deep"], kws) if refs["deep"] else None, "light": src.grep_layer(refs["light"], kws) if refs["light"] else None, "distillations": []}
        for task, path in refs["distillations"].items():
            g = src.grep_layer(path, kws)
            if g: g["task"] = task; layers["distillations"].append(g)
        fig = None
        if j.get("figure"):
            f = j["figure"]
            fig = src.figure(f["name"] if isinstance(f, dict) else f)
            if isinstance(f, dict) and f.get("image"):
                fig = fig or {"name": f["name"], "caption": None, "line": None}
                fig["image"] = f["image"] if (src.root / f["image"]).exists() else None
                fig["via"] = f.get("via")
        out_spans[span_id] = {"source": sid, "corpus": src.corpus, "status": level, "verified": True, "hits": hits, "text": text, "anchor": j["anchor"], "line": line,
                              "locator": src.locator(line - 1), "page": src.page(line - 1, text),
                              "context": {"before": before, "after": after, "lead": own_b, "tail": own_a},
                              "layers": layers, "figure": fig}
        print(f"ok {span_id}: {level}, line {line}, {len(text.split())} words, p.{out_spans[span_id]['page']}, {out_spans[span_id]['locator'][:50]!r}", file=sys.stderr)
    charts = []
    for c in report.get("charts", []):
        why = check_chart(c, out_spans)
        charts.append({"span": c.get("span"), "ok": why is None, "why": why})
        print(f"chart after {c.get('span')}: {'ok' if why is None else 'withdrawn, ' + why}", file=sys.stderr)
    bundle = {"question": report["question"], "generated": datetime.date.today().isoformat(), "corpora": corpora, "sources": out_sources, "spans": out_spans, "charts": charts, "source_problems": problems}
    (folder / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=1))
    placed = sum(1 for s in out_spans.values() if s["verified"])
    print(f"wrote {folder / 'bundle.json'}: {len(out_spans)} spans, {placed} placed, {len(out_spans) - placed} missing", file=sys.stderr)


if __name__ == "__main__":
    main()
