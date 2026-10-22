#!/usr/bin/env python3
"""Check an answer's author quotations before it goes out.

Every quotation the answer attributes to a named author or work must be the author's
own words. The failure this catches: wording from a summary layer (a reference's or a
distillation's paraphrase) put in quote marks as if the author wrote it. In the
Gemini Notebook evaluation (October 2026) every Claude configuration did this at
least once.

Where it looks, by mode (detected from the folder, or set with --root):

  project mode (references/ and sources/converted/ present)
    ok        found in a converted source
    LAYER     found only in a light or deep reference: the reference's wording, not
              the author's. Fix: quote the source's own words, or paraphrase.
  app mode (distillations/ present, no references/)
    ok        found on a distillation line marked [V] or in a blockquote, which the
              build checked word for word against the source
    LAYER     found only in a distillation's unmarked prose: the distillation's
              wording. Fix: paraphrase with attribution, or quote a [V] passage.
  both
    input     found in a file passed with --input (the user's own material)
    MISSING   not found anywhere: reworded, shortened without an ellipsis, or
              invented. The closest opening run is shown.

Only quotations of four or more words whose sentence names a known author or work
are checked; the rest are counted as unattributed (often the answer's own suggested
lines). Matching sets aside typography: case, curly and straight quote marks, dash
styles, Markdown emphasis, line-end hyphens and whitespace. An ellipsis or a
bracketed insertion splits the quote into pieces that must appear in order. For the
full ladder used at ingestion, see scripts/check-verbatim.py in the grounded-forge
repo. A hyphen at a line end is read as joining the word, as at ingestion, so a true
compound split across a line ("self-\naware") reads as one word.

Usage:
    python3 .claude/skills/answer-from-corpus/check_quotes.py ANSWER.md [--input CASE.txt ...] [--root DIR]
    python3 .claude/skills/answer-from-corpus/check_quotes.py - < ANSWER.md
Exit status: 1 if any LAYER or MISSING, else 0.
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"}
# A quote opens after a space, an opening bracket or a line start, and closes before a space or punctuation,
# so two quoted phrases on one line don't pair across the text between them.
QUOTE_RE = re.compile(r'(?:(?<=^)|(?<=[\s(\[]))(?:"([^"\n]{12,600}?)"|“([^”\n]{12,600}?)”)(?=[\s.,;:!?)\]]|$)', re.M)
STOP = {"the", "and", "that", "with", "this", "from", "have", "they", "their", "what", "which", "when", "where",
        "there", "about", "would", "could", "should", "into", "than", "then", "them", "were", "been", "your"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for k, v in LIGATURES.items():
        s = s.replace(k, v)
    s = re.sub(r"[​‌‍﻿]", "", s)
    s = re.sub(r"(?i)<br\s*/?>", " ", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)            # links: keep the text
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)               # line-end hyphen
    s = s.translate(str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "—": "-", "–": "-", "‐": "-"}))
    s = re.sub(r"[*_`#>]", "", s)
    s = s.replace('"', "").replace("'", "")
    s = re.sub(r"\s*-\s*", "-", s)                             # dashes set open or closed
    s = re.sub(r"\s+([,.;:!?)])", r"\1", s)
    return re.sub(r"\s+", " ", s).lower().strip()


def pieces(quote: str) -> list[str]:
    parts = re.split(r"\.\.\.|…|\[[^\]]*\]", quote)
    out = [norm(p).strip(" ,.;:") for p in parts]
    return [p for p in out if len(p.split()) >= 2]


def found_in(ps: list[str], text: str) -> bool:
    pos = 0
    for i, p in enumerate(ps):
        j = text.find(p, pos)
        if j < 0 or (i and j - pos > 4000):
            return False
        pos = j + len(p)
    return True


def keywords(quote: str) -> list[str]:
    """Long words from the quote as typed, skipping any with an apostrophe (the source may spell it differently)."""
    words = [w.lower() for w in re.findall(r"[A-Za-z’']+", quote) if "'" not in w and "’" not in w and len(w) >= 5]
    return sorted(set(w for w in words if w not in STOP), key=len, reverse=True)[:3]


def bigrams(quote: str) -> list[str]:
    """Pairs of adjacent plain words, the cheapest reliable filter on raw text."""
    toks = re.findall(r"[A-Za-z’'-]+|[^\sA-Za-z]", quote)
    out = []
    for a, b in zip(toks, toks[1:]):
        if a.isalpha() and b.isalpha() and len(a) + len(b) >= 8 and not ({a.lower(), b.lower()} <= STOP):
            out.append(f"{a.lower()} {b.lower()}")
    return sorted(set(out), key=len, reverse=True)[:2]


class Layer:
    """A set of files searched lazily: raw lowercase text as a prefilter, normalised text on demand."""

    def __init__(self, files):
        self.files = list(files)
        self.raw, self.normd = {}, {}

    def _raw(self, f):
        if f not in self.raw:
            t = re.sub(r"(\w)-[ \t]*\n\s*(\w)", r"\1\2", f.read_text(errors="ignore").lower())  # line-end hyphen, as norm()
            self.raw[f] = re.sub(r"\s+", " ", t)
        return self.raw[f]

    def candidates(self, quote):
        kws, bgs = keywords(quote), bigrams(quote)
        hits = [f for f in self.files if bgs and all(b in self._raw(f) for b in bgs)]
        return hits or [f for f in self.files if kws and all(k in self._raw(f) for k in kws)]

    def search(self, quote, ps):
        """Normalise only windows around the quote's rarest word, not whole books (a book takes about a second)."""
        kws = keywords(quote)
        for f in self.candidates(quote):
            raw = self._raw(f)
            if f in self.normd or not kws:
                if f not in self.normd:
                    self.normd[f] = norm(raw)
                if found_in(ps, self.normd[f]):
                    return f
                continue
            span = 2500 + len(quote) * 4
            starts = [m.start() for m in re.finditer(re.escape(kws[0]), raw)][:400]
            merged = []
            for i in starts:
                a, b = max(0, i - span), i + span
                if merged and a <= merged[-1][1]:
                    merged[-1][1] = b
                else:
                    merged.append([a, b])
            if any(found_in(ps, norm(raw[a:b])) for a, b in merged):
                return f
        return None

    def closest(self, quote):
        """The file holding the longest opening run of the quote's words, searched in windows around its keywords."""
        ws = norm(quote).split()
        kws = keywords(quote) or ws[:1]
        best = (0, None)
        for f in self.files:
            raw = self._raw(f)
            if not any(k in raw for k in kws):
                continue
            starts = [m.start() for k in kws for m in re.finditer(re.escape(k), raw)][:200]
            t = " ".join(norm(raw[max(0, i - 1500):i + 1500]) for i in starts)
            k = len(ws)
            while k > best[0] and k >= 3 and " ".join(ws[:k]) not in t:
                k -= 1
            if k > best[0] and k >= 3:
                best = (k, f)
        return best


def marked_text(path: Path) -> str:
    """The [V]-marked lines and blockquotes of a distillation, i.e. the build-checked verbatim text."""
    keep = [ln for ln in path.read_text(errors="ignore").splitlines() if "[V]" in ln or ln.lstrip().startswith(">")]
    return "\n".join(keep)


def names(root: Path, mode: str) -> set[str]:
    out = set()
    idx = root / "reference-index.json"
    if idx.exists():
        refs = json.loads(idx.read_text()).get("refs", {})
        for r in (refs.values() if isinstance(refs, dict) else refs):
            for person in re.split(r"[;&]| and ", r.get("author") or ""):
                surname = person.split(",")[0].strip()
                if len(surname) > 2:
                    out.add(surname.split()[-1])
            title = re.split(r"[:(]| -- ", r.get("title") or "")[0].strip()
            if len(title) > 6:
                out.add(title)
    if mode == "app":
        for f in (root / "distillations").glob("*/*.md"):
            head = f.read_text(errors="ignore")[:1500]
            m = re.search(r"\*\*Source(?: Framework)?:\*\*\s*([^\n]+)", head)
            if not m:
                continue
            line = m.group(1)
            for t in re.findall(r"\*([^*\n]{6,80})\*", line):        # the work's title, in italics
                out.add(re.split(r"[:(]", t)[0].strip())
            people = re.split(r"\(\d{4}|\.\s+\*|\*", line)[0]       # names come before the year or the title
            for person in re.split(r"[;&,]| and ", people):
                w = re.findall(r"[A-Z][\w'’-]+", person)
                if w and len(w[-1]) > 2:
                    out.add(w[-1])
    for f in (root / "references").glob("*.md") if (root / "references").exists() else []:
        first = f.name.split("-")[0]
        if len(first) > 3:
            out.add(first.capitalize())
    return {n for n in out if n and n.lower() not in STOP}


def sentence_at(text: str, start: int, end: int) -> str:
    a = max(text.rfind(c, 0, start) for c in (". ", "\n", "! ", "? "))
    b_candidates = [i for i in (text.find(c, end) for c in (". ", "\n")) if i >= 0]
    b = min(b_candidates) if b_candidates else len(text)
    return text[a + 1:b]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("answer", help="the answer file, or - for stdin")
    ap.add_argument("--input", action="append", default=[], help="the user's own material (case notes, transcript): quotes from it are fine")
    ap.add_argument("--root", type=Path, default=Path.cwd(), help="corpus root or app folder (default: the current folder)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = sys.stdin.read() if a.answer == "-" else Path(a.answer).read_text(errors="ignore")
    root = a.root
    if (root / "references").exists() and (root / "sources/converted").exists():
        mode = "project"
        good = Layer(sorted((root / "sources/converted").glob("*.md")))
        layer = Layer(sorted((root / "references").glob("*.md")))
    elif (root / "distillations").exists():
        mode = "app"
        dists = sorted((root / "distillations").glob("*/*.md"))
        tmp = {f: marked_text(f) for f in dists}
        good = Layer(dists)
        good.raw = {f: re.sub(r"\s+", " ", t.lower()) for f, t in tmp.items()}
        good.normd = {f: norm(t) for f, t in tmp.items()}
        layer = Layer(dists)
    else:
        print("check_quotes: no references/ and sources/converted/ (project mode) or distillations/ (app mode) under", root, file=sys.stderr)
        return 2
    inputs = Layer([Path(p) for p in a.input])
    known = names(root, mode)
    name_re = re.compile(r"\b(" + "|".join(sorted((re.escape(n) for n in known), key=len, reverse=True)) + r")\b") if known else None

    results, unattributed = [], 0
    for m in QUOTE_RE.finditer(text):
        quote = (m.group(1) or m.group(2)).strip()
        if len(quote.split()) < 4:
            continue
        caps = [w for w in quote.split() if w[:1].isalpha()]
        if len(caps) <= 8 and sum(w[0].isupper() for w in caps) >= max(3, len(caps) - 1):
            continue                                                  # a title or heading, not a quotation
        ps = pieces(quote)
        if not ps:
            continue
        sent = sentence_at(text, m.start(), m.end())
        who = name_re.findall(sent) if name_re else []
        line = text.count("\n", 0, m.start()) + 1
        if inputs.files and inputs.search(quote, ps):
            results.append({"line": line, "quote": quote, "status": "input", "attributed": who})
            continue
        if not who:
            unattributed += 1
            continue
        f = good.search(quote, ps)
        if f:
            results.append({"line": line, "quote": quote, "status": "ok", "attributed": who, "where": f.name})
            continue
        f = layer.search(quote, ps)
        if f:
            results.append({"line": line, "quote": quote, "status": "LAYER", "attributed": who, "where": f.name,
                            "fix": "paraphrase with attribution, or quote the author's own words"})
            continue
        k, cf = good.closest(quote)
        results.append({"line": line, "quote": quote, "status": "MISSING", "attributed": who,
                        "closest": f"{k} opening words match in {cf.name}" if cf else "no opening run of 3+ words found"})

    bad = [r for r in results if r["status"] in ("LAYER", "MISSING")]
    if a.json:
        print(json.dumps({"mode": mode, "checked": len(results), "unattributed": unattributed, "failures": len(bad), "results": results}, indent=1))
    else:
        print(f"check_quotes ({mode} mode): {len(results)} attributed quotation(s) checked, {len(bad)} to fix; {unattributed} unattributed, not checked.")
        for r in results:
            if r["status"] in ("LAYER", "MISSING"):
                print(f"  {r['status']:7s} line {r['line']}: \"{r['quote'][:90]}\" ({', '.join(r['attributed'][:2])})")
                print(f"          {r.get('where') or r.get('closest')}; {r.get('fix', 'reword as paraphrase, or find the passage and quote it exactly')}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
