#!/usr/bin/env python3
"""Deterministic check that verbatim quotations match the converted source.

A `[V]` marker promises the author's own words, character-exact. Pass D
blockquotes promise the same. This script checks both against
`sources/converted/{slug}.md`, so an auditor gets every mismatch in one run
instead of tracing quotes one grep at a time. It reports candidates and edits
nothing: the auditor still decides the fix, which is to correct the quote to the
source's words or to paraphrase it and change the marker.

What it checks, per file:

  - Every quoted span ("..." or curly “...”) in a segment that ends in a `[V]`
    marker. A segment is the sentence the `[V]` closes, back no further than
    the previous evidence marker; in a table it is the marker's cell, or the
    whole row when the cell holds no quote. Quoted titles inside citation
    parentheticals are skipped: they cite, they don't quote.
  - Every quoted span in a blockquote (`>` lines), marker or not.

Each quote is looked for at a ladder of levels and reported at the first level
that finds it:

  exact     Found once conversion noise is set aside on both sides: whitespace
            collapsed, Markdown emphasis and link syntax dropped, ligatures
            expanded (ﬂ → fl), zero-width characters and `<br>` dropped, a word
            hyphenated across a line rejoined (or kept, for a true compound),
            no space before punctuation, an en or em dash set open or closed. Double quote marks
            read as single: inside a quotation the nesting convention turns the
            source's "x" into 'x'. Trailing
            `,` `.` `;` `:` inside the closing quote mark are the quoting
            convention, not the author, and are ignored. An ellipsis (`...`,
            `…`) is an elision: each piece must appear, in order, within a few
            thousand characters. A bracketed insertion (`[the manager]`)
            stands for a short run of source text; `[sic]` is dropped.
            Nothing is reported.
  apostrophe
            Found once apostrophes and single quote marks are folded, straight
            and curly. That is typography, not the author's words: reported so
            the count is visible, never failing (fixture 05 is the control).
  glyph     As apostrophe, and dashes folded too: hyphen, en and em. The words
            are the author's; a dash is not.
  initial   As glyph, but the first letter's case differs: the quotation
            starts mid-sentence in the source, or the reverse.
  near      The same words in the same order, but case or punctuation differs,
            or a footnote number glued to a word is dropped. Fixture 06's
            capitalisation tidy lands here, as does a bulleted list quoted
            inline with semicolons.
  page      Found only once standalone numbers are dropped: a page number or
            folio sits inside the passage in the converted text. Usually a
            conversion artefact; a changed figure in the quote would also land
            here, so it is shown.
  ligature  Found once "fi" and "fl" are read as "f": the converter kept the
            first letter of a ligature glyph and dropped the rest ("confrms").
            Converter damage, not the author's change; not failing.
  interrupted
            Found as up to four runs of the quote's words, each within a few
            hundred characters of the last. The text in each gap is shown: a
            running header or folio ("87 Warfighting MCDP1") is conversion
            noise; a dropped clause is a quote shortened without an ellipsis
            (fixture 09's failure mode).
  missing   Not found at any level: reworded, credited to the wrong source, or
            invented. The source text matching the quote's longest opening run
            of words is shown.
  cross-source
            Not in this file's source, but in another converted source in the
            corpus (up to the near level) that the line names (by slug, title or author): a
            distillation quoting a second source with attribution. Not failing.
  wrong-source
            In another source the line doesn't name: credited to the
            wrong source, or attributed too vaguely to check.
  no-quote  A `[V]` segment with neither a quoted span nor a figure: the marker
            sits on a paraphrase (fixture 07's failure mode). A segment with
            figures and no quote is a figure claim, which the protocol's stats
            table marks `[V]`; those are counted, not checked.

Exit status is 1 when any finding other than `apostrophe`, `initial`,
`ligature` or `cross-source` is reported, 2 when a file's source cannot be found, else 0.

Limits, by design:

  - An OCR'd two-column source can hold a passage word for word yet never as
    one run, so `missing` there may mean scrambled reading order. The
    protocol's rule applies: check the page image or reclassify to `[AP]`.
  - A translation can never carry `[V]`; this script cannot tell a gloss from
    the source's own language. Pass I can.
  - A match proves the words are in the source, not that the source's author
    wrote them: a passage the source quotes from someone else still matches.

Files and their sources:

  - `references/{slug}-deep.md` and `references/{slug}.md` → `sources/converted/{slug}.md`
  - `distillations/{task}/{slug}-{task}.md` → `sources/converted/{slug}.md`
  - A file with a `seed_source:` frontmatter field (the Pass I audit
    fixtures) → that slug's converted source, looked up across corpora.
  - `--source PATH` overrides the lookup for a single file.

Usage:
    python3 scripts/check-verbatim.py corpus.commons/demo/references/foo-deep.md
    python3 scripts/check-verbatim.py corpus.commons/demo/distillations/aar/foo-aar.md --json
    python3 scripts/check-verbatim.py tests/audit-fixtures/06-verbatim-capitalisation-tidy.md
    python3 scripts/check-verbatim.py --all
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TIER_ROOTS = {"commons": REPO_ROOT / "corpus.commons", "local": REPO_ROOT / "corpus.local"}

MARKER_RE = re.compile(r"(?<![A-Za-z0-9])\[(V|AP|AR|AE|BT)\](?=[\s,.;:)\]]|$)")
QUOTE_RE = re.compile(r'"([^"\n]+?)"|“([^”\n]+?)”')
# A citation parenthetical holds a digit or a citation keyword. Quoted section
# titles inside one are citations, not quotations.
CITATION_PAREN_RE = re.compile(
    r"\((?=[^()]*(?:\d|\bCh\b|\bChapter\b|\bPart\b|\bSection\b|§|\bp\.|\bpp\.|\bciting\b))[^()]*\)"
)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
FRONTMATTER_SEED_RE = re.compile(r"^seed_source:\s*(\S+)\s*$", re.M)
ELLIPSIS_RE = re.compile(r"\s*(?:\.\s?\.\s?\.|…)\s*")
BRACKET_RE = re.compile(r"\[[^\]]*\]")
SIC_RE = re.compile(r"\s*\[sic\]", re.I)
DIGIT_RE = re.compile(r"\d")

ELISION_WINDOW = 3000  # max characters between the pieces of an elided quote
INSERTION_WINDOW = 80  # max source characters a bracketed insertion stands for
MIN_PIECE_WORDS = 2  # elided pieces shorter than this are not located on their own

LEVELS = ("exact", "apostrophe", "glyph", "initial", "near", "page", "ligature")
FAILING_KINDS = {"glyph", "near", "page", "interrupted", "wrong-source", "missing", "no-quote"}  # not apostrophe, initial, ligature or cross-source
GAP_WINDOW = 400  # max source characters between the runs of an interrupted quote
MAX_RUNS = 4  # an interrupted quote may be found in at most this many runs
MIN_RUN_WORDS = 3
MIN_CROSS_SOURCE_WORDS = 5


# ---------------------------------------------------------------------------
# Normalisation: a pipeline of regex substitutions that keeps a map from each
# output character back to its offset in the original text, so a match can be
# shown as the source's own characters.

# Characters a converter leaves in that no reader sees: soft hyphen, zero-width
# space and joiners, word joiner, byte-order mark.
INVISIBLE = "".join(chr(c) for c in (0x00AD, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF))
LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st"}

BASE_STEPS = [
    (re.compile(r"\[([^\]\n]*)\]\([^)\s]*\)"), 1),  # Markdown link → its text
    (re.compile(chr(0x00AD) + r"\s*"), ""),  # a soft hyphen can still carry its line break
    (re.compile("[" + INVISIBLE + "]"), ""),
    (re.compile("[" + "".join(LIGATURES) + "]"), lambda m: LIGATURES[m.group(0)]),
    (re.compile(r"[*_]+"), ""),  # emphasis
    (re.compile(r"<br\s*/?>", re.I), " "),  # line break inside a table cell
    # A double quote inside a quotation becomes single by the nesting
    # convention, so every double quote mark reads as a straight single.
    (re.compile("[\"“”„‟″]"), "'"),
]
HYPHEN_RE = re.compile(r"(?<=[A-Za-z])-\s+(?=[a-z])")  # "organi-\nzation", "in- ward"
TAIL_STEPS = [
    (re.compile(r"\s+"), " "),
    (re.compile(r" (?=[.,;:!?)\]])"), ""),
    (re.compile(r"(?<=[(\[]) "), ""),
    (re.compile(r" ?([–—]) ?"), 1),  # an en or em dash set open or closed
]
APOSTROPHE_STEP = (re.compile("[‘’‚‛′`']"), "'")
DASH_STEP = (re.compile(r"\s*(?:[–—‐‑−]|--+)\s*|\s+-\s+"), "-")
FOOTNOTE_RE = re.compile(r"(?<=[A-Za-z.,;:')])\d{1,3}(?= |$)")
PUNCT_RE = re.compile(r"\W+")
LIGATURE_LOSS_RE = re.compile(r"f[il]")
PAGE_RE = re.compile(r"(?<![^ ])\d{1,4} ")


def _sub(text: str, idx: list[int], pattern: re.Pattern, repl) -> tuple[str, list[int]]:
    """Apply one substitution, carrying the offset map. `repl` is a string, a
    function of the match, or an int naming the group to keep in place."""
    out: list[str] = []
    oidx: list[int] = []
    last = 0
    for m in pattern.finditer(text):
        out.append(text[last : m.start()])
        oidx.extend(idx[last : m.start()])
        if isinstance(repl, int):
            g0, g1 = m.span(repl)
            out.append(text[g0:g1])
            oidx.extend(idx[g0:g1])
        else:
            r = repl(m) if callable(repl) else repl
            out.append(r)
            oidx.extend([idx[m.start()]] * len(r))
        last = m.end()
    out.append(text[last:])
    oidx.extend(idx[last:])
    return "".join(out), oidx


def _lower(text: str, idx: list[int]) -> tuple[str, list[int]]:
    low = text.lower()
    if len(low) == len(text):
        return low, idx
    return "".join(c.lower()[:1] for c in text), idx


def normalise(text: str, level: str, hyphen: str = "join") -> tuple[str, list[int]]:
    """Normalise `text` for one rung of the ladder. `hyphen` is "join" (rejoin
    a word split across a line) or "keep" (a true compound broken at its hyphen)."""
    rank = LEVELS.index(level)
    s, idx = text, list(range(len(text)))
    for pat, repl in BASE_STEPS:
        s, idx = _sub(s, idx, pat, repl)
    s, idx = _sub(s, idx, HYPHEN_RE, "" if hyphen == "join" else "-")
    for pat, repl in TAIL_STEPS:
        s, idx = _sub(s, idx, pat, repl)
    if rank >= LEVELS.index("apostrophe"):
        s, idx = _sub(s, idx, *APOSTROPHE_STEP)
    if rank >= LEVELS.index("glyph"):
        s, idx = _sub(s, idx, *DASH_STEP)
    if rank >= LEVELS.index("near"):
        s, idx = _sub(s, idx, FOOTNOTE_RE, "")
        s, idx = _lower(s, idx)
        s, idx = _sub(s, idx, PUNCT_RE, " ")
    if rank >= LEVELS.index("page"):
        s, idx = _sub(s, idx, PAGE_RE, "")
    if rank >= LEVELS.index("ligature"):
        s, idx = _sub(s, idx, LIGATURE_LOSS_RE, "f")
    return s, idx


class Source:
    """A converted source, normalised lazily per (level, hyphen) rung."""

    def __init__(self, path: Path):
        self.path = path
        self.raw = path.read_text(encoding="utf-8", errors="replace")
        self._forms: dict[tuple[str, str], tuple[str, list[int]]] = {}

    def form(self, level: str, hyphen: str) -> tuple[str, list[int]]:
        key = (level, hyphen)
        if key not in self._forms:
            self._forms[key] = normalise(self.raw, level, hyphen)
        return self._forms[key]

    def original(self, idx: list[int], start: int, end: int) -> str:
        if not idx or start >= len(idx):
            return ""
        a = idx[start]
        b = idx[min(len(idx) - 1, max(start, end - 1))] + 1
        return re.sub(r"\s+", " ", self.raw[a:b]).strip()


# ---------------------------------------------------------------------------
# Extraction


@dataclass
class Span:
    line: int
    text: str
    context: str  # "V" (a [V] segment) or "blockquote"
    line_text: str = ""


@dataclass
class Finding:
    file: str
    line: int
    kind: str
    quote: str = ""
    source_text: str = ""
    note: str = ""


@dataclass
class Extracted:
    spans: list[Span] = field(default_factory=list)
    no_quote: list[int] = field(default_factory=list)
    figures: int = 0


def body_start(lines: list[str]) -> int:
    """Index of the first body line, past any YAML frontmatter."""
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return i + 1
    return 0


def quoted_spans(segment: str) -> list[str]:
    segment = CITATION_PAREN_RE.sub(" ", segment)
    return [(m.group(1) or m.group(2)).strip() for m in QUOTE_RE.finditer(segment)]


def sentence_tail(segment: str) -> str:
    """The last sentence of a segment: the text after the last sentence end
    that sits outside quotation marks. A `[V]` covers the sentence it closes,
    not an illustrative phrase quoted a sentence earlier."""
    in_quote, start = False, 0
    for i, c in enumerate(segment):
        closing = (c == '"' and in_quote) or c == "”"
        if c == '"':
            in_quote = not in_quote
        elif c == "“":
            in_quote = True
        elif c == "”":
            in_quote = False
        # A sentence ends at . ? ! outside quotation marks, or just inside a
        # closing one ("...out of time." Diagnosis:).
        ends = (c in ".?!" and not in_quote) or (closing and i > 0 and segment[i - 1] in ".?!")
        if ends:
            rest = segment[i + 1 :].lstrip("*_)")
            # A sentence end with nothing after it is the end of the sentence
            # the [V] closes, not the start of a new one.
            if rest[:1].isspace() and rest.strip():
                start = i + 1
    return segment[start:]


def extract(text: str) -> Extracted:
    lines = text.split("\n")
    ex = Extracted()
    in_code = False
    for i in range(body_start(lines), len(lines)):
        raw = lines[i]
        stripped = raw.lstrip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or stripped.startswith("<!--"):
            continue
        lineno = i + 1
        line = INLINE_CODE_RE.sub(" ", raw)
        if stripped.startswith(">"):
            ex.spans.extend(Span(lineno, q, "blockquote", raw) for q in quoted_spans(line.lstrip()[1:]))
            continue
        is_row = stripped.startswith("|")
        prev_end = 0
        for m in MARKER_RE.finditer(line):
            if m.group(1) == "V":
                if is_row:
                    # The marker's own cell, or the whole row when the cell holds no quote.
                    cell = line[line.rfind("|", 0, m.start()) + 1 : m.start()]
                    segment = cell if quoted_spans(cell) else line[: m.start()]
                else:
                    # Drop the previous marker's trailing citation.
                    segment = re.sub(r"^\s*\([^()]*\)[.,;]?", "", line[prev_end : m.start()])
                    segment = sentence_tail(segment)
                found = quoted_spans(segment)
                if found:
                    ex.spans.extend(Span(lineno, q, "V", raw) for q in found)
                elif DIGIT_RE.search(CITATION_PAREN_RE.sub(" ", segment)):
                    ex.figures += 1
                else:
                    ex.no_quote.append(lineno)
            prev_end = m.end()
    return ex


# ---------------------------------------------------------------------------
# Matching


def _piece_pattern(piece: str, level: str, any_initial: bool) -> re.Pattern | None:
    """A literal pattern for one elided piece; bracketed insertions become a
    short wildcard. With `any_initial`, the first letter matches either case."""
    lits = [normalise(p, level)[0].strip() for p in BRACKET_RE.split(piece)]
    if not "".join(lits):
        return None
    esc = [re.escape(x) for x in lits]
    if any_initial and lits[0][:1].isalpha():
        c = lits[0][0]
        esc[0] = f"[{re.escape(c.lower())}{re.escape(c.upper())}]" + re.escape(lits[0][1:])
    return re.compile((r".{0,%d}?" % INSERTION_WINDOW).join(esc), re.S)


def _pieces(quote: str) -> list[str]:
    quote = SIC_RE.sub("", quote).rstrip(",.;: ")
    pieces = [p for p in ELLIPSIS_RE.split(quote) if p.strip()]
    return [p for p in pieces if len(p.split()) >= MIN_PIECE_WORDS] or pieces


def locate(quote: str, src: Source, level: str) -> tuple[int, int, list[int]] | None:
    pieces = _pieces(quote)
    if not pieces:
        return None
    any_initial = level == "initial"
    norm_level = "glyph" if level == "initial" else level
    for hyphen in ("join", "keep"):
        text, idx = src.form(norm_level, hyphen)
        pats = [_piece_pattern(p, norm_level, any_initial and k == 0) for k, p in enumerate(pieces)]
        pats = [p for p in pats if p is not None]
        if not pats:
            return None
        for m in pats[0].finditer(text):
            end, ok = m.end(), True
            for p in pats[1:]:
                nxt = p.search(text, end, end + ELISION_WINDOW + len(p.pattern))
                if not nxt:
                    ok = False
                    break
                end = nxt.end()
            if ok:
                return m.start(), end, idx
    return None


def locate_interrupted(quote: str, src: Source) -> list[str] | None:
    """Find a quote as up to MAX_RUNS runs of its words, each starting within
    GAP_WINDOW characters of the last, at the most permissive level. Return
    the source text in each gap, or None."""
    text, idx = src.form("page", "join")
    words = normalise(ELLIPSIS_RE.sub(" ", SIC_RE.sub("", quote)).rstrip(",.;: "), "page")[0].split()
    words = [w for w in words if not BRACKET_RE.fullmatch(w)]
    if len(words) < 2 * MIN_RUN_WORDS:
        return None

    def longest_run(i: int, lo: int, hi: int) -> tuple[int, int, int]:
        """Longest run words[i:j] found in text[lo:hi]; returns (j, start, end)."""
        best = (i, -1, -1)
        a, b = i + 1, len(words)
        while a <= b:
            mid = (a + b) // 2
            needle = " ".join(words[i:mid])
            at = text.find(needle, lo, hi)
            if at >= 0:
                best, a = (mid, at, at + len(needle)), mid + 1
            else:
                b = mid - 1
        return best

    first = " ".join(words[:MIN_RUN_WORDS])
    for m in re.finditer(re.escape(first), text):
        i, end, gaps = 0, m.start(), []
        j, at, stop = longest_run(0, m.start(), m.start() + len(" ".join(words)) + 1)
        if at != m.start():
            continue
        i, end = j, stop
        while i < len(words) and len(gaps) < MAX_RUNS - 1:
            j, at, stop = longest_run(i, end, end + GAP_WINDOW + len(" ".join(words[i:])))
            if j - i < min(MIN_RUN_WORDS, len(words) - i) or at - end > GAP_WINDOW:
                break
            gaps.append(src.original(idx, end, at) if at > end else "")
            i, end = j, stop
        if i == len(words) and gaps:
            return gaps
    return None


def closest(quote: str, src: Source) -> str:
    """The source text that matches the longest opening run of the quote's
    words, at the most permissive level, so the fix needs no further search."""
    text, idx = src.form("page", "join")
    words = normalise(ELLIPSIS_RE.sub(" ", SIC_RE.sub("", quote)), "page")[0].split()
    lo, hi, best = 1, len(words), None
    while lo <= hi:
        mid = (lo + hi) // 2
        at = text.find(" ".join(words[:mid]))
        if at >= 0:
            best, lo = (mid, at), mid + 1
        else:
            hi = mid - 1
    if best is None or best[0] < MIN_RUN_WORDS:
        return ""
    n, at = best
    shown = src.original(idx, at, min(len(idx), at + len(" ".join(words)) + 40))
    return f"first {n} of {len(words)} words found; source reads: {shown[:240]}"


def _diff_note(quote: str, found: str) -> str:
    q = re.sub(r"\s+", " ", SIC_RE.sub("", quote)).rstrip(",.;: ")
    f = found.rstrip(",.;: ")
    if len(q) == len(f):
        pairs = sorted({f"{a}→{b}" for a, b in zip(q, f) if a != b})
        if pairs:
            return "quote→source: " + ", ".join(pairs[:6])
    return ""


def classify(span: Span, src: Source, others: list[Path], cache: dict) -> Finding | None:
    for level in LEVELS:
        hit = locate(span.text, src, level)
        if hit is None:
            continue
        if level == "exact":
            return None
        start, end, idx = hit
        found = src.original(idx, start, end)
        return Finding("", span.line, level, span.text, found, _diff_note(span.text, found))
    gaps = locate_interrupted(span.text, src)
    if gaps:
        shown = " | ".join((g[:70] + "…") if len(g) > 70 else g for g in gaps if g) or "punctuation only"
        return Finding("", span.line, "interrupted", span.text, "", f"source text in the gap: {shown}")
    # Sources the line names are searched for a quote of any length. A short
    # phrase turns up in other books by chance, so only a longer quote is
    # searched for in sources the line doesn't name.
    named = [o for o in others if names_source(span.line_text, o)]
    unnamed = [o for o in others if o not in named] if len(span.text.split()) >= MIN_CROSS_SOURCE_WORDS else []
    for other in named + unnamed:
        if other not in cache:
            try:
                cache[other] = Source(other)
            except OSError:
                continue
        if locate(span.text, cache[other], "near"):
            if other in named:
                return Finding("", span.line, "cross-source", span.text, "", f"quoted from {other.stem}, which the line names")
            return Finding("", span.line, "wrong-source", span.text, "",
                           f"found in {other.stem}, which the line doesn't name")
    return Finding("", span.line, "missing", span.text, "", closest(span.text, src))


GENERIC_NAME_TOKENS = {"open", "openstax", "the", "guide", "handbook", "principles", "introduction", "a", "an"}


def _compact(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def source_names(converted: Path) -> set[str]:
    """Ways a line may name a source: its slug, the slug's distinctive leading
    tokens, its sidecar title (whole and before any colon) and author surnames."""
    slug = converted.stem
    toks = slug.split("-")
    names = {slug, "-".join(toks[:2])}
    if toks[0] not in GENERIC_NAME_TOKENS:
        names.add(toks[0])
    sidecar = converted.parent.parent / "original" / f"{slug}.source.md"
    if sidecar.exists():
        head = sidecar.read_text(encoding="utf-8", errors="replace")[:3000]
        for key in ("title", "author"):
            m = re.search(rf"^{key}:\s*['\"]?(.+?)['\"]?\s*$", head, re.M)
            if not m:
                continue
            val = m.group(1)
            if key == "title":
                names.update({val, val.split(":")[0], val.split(" — ")[0]})
                initials = "".join(w[0] for w in re.findall(r"[A-Z][A-Za-z]{2,}", val.split(":")[0]))
                if len(initials) >= 3:
                    names.add(initials)
            else:
                for person in re.split(r",|;|&|\band\b|\(|\)", val):
                    words = [w for w in person.split() if w[:1].isupper() and len(w) > 2]
                    if words:
                        names.add(words[-1])
    return {c for c in map(_compact, names) if len(c) >= 3}


def names_source(line: str, converted: Path) -> bool:
    line_c = _compact(line)
    words = {_compact(w) for w in line.split()}
    # A three-letter name (an acronym such as OPL) must stand as its own word.
    return any((n in words) if len(n) == 3 else (n in line_c) for n in source_names(converted))


# ---------------------------------------------------------------------------
# File → source resolution


def corpus_root_of(path: Path) -> Path | None:
    for parent in path.resolve().parents:
        if parent.parent in TIER_ROOTS.values():
            return parent
    return None


def find_seed_source(slug: str) -> Path | None:
    for tier in TIER_ROOTS.values():
        for cand in sorted(tier.glob(f"*/sources/converted/{slug}.md")):
            return cand
    return None


def resolve_source(path: Path, text: str) -> Path | None:
    seed = FRONTMATTER_SEED_RE.search(text[:2000])
    if seed and seed.group(1) != "synthetic":
        return find_seed_source(seed.group(1))
    root = corpus_root_of(path)
    if root is None:
        return None
    name = path.stem
    if path.parent.parent.name == "distillations":
        task = path.parent.name
        if name.endswith(f"-{task}"):
            name = name[: -len(task) - 1]
    elif name.endswith("-deep"):
        name = name[: -len("-deep")]
    cand = root / "sources" / "converted" / f"{name}.md"
    return cand if cand.exists() else None


def _rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def check_file(path: Path, source_override: Path | None, search_corpus: bool, cache: dict) -> tuple[list[Finding], int, str | None]:
    text = path.read_text(encoding="utf-8")
    ex = extract(text)
    rel = _rel(path)
    findings = [Finding(rel, ln, "no-quote", note="[V] segment carries no quoted span or figure") for ln in ex.no_quote]
    if not ex.spans:
        return findings, ex.figures, None
    src_path = source_override or resolve_source(path, text)
    if src_path is None:
        return findings, ex.figures, f"{rel}: no converted source found (pass --source)"
    src = cache.get(src_path)
    if src is None:
        src = cache[src_path] = Source(src_path)
    others: list[Path] = []
    if search_corpus:
        root = corpus_root_of(src_path)
        if root:
            others = [p for p in sorted((root / "sources" / "converted").glob("*.md")) if p != src_path]
    for span in ex.spans:
        f = classify(span, src, others, cache)
        if f:
            f.file = rel
            if span.context == "blockquote":
                f.note = "; ".join(x for x in ("blockquote", f.note) if x)
            findings.append(f)
    findings.sort(key=lambda f: f.line)
    return findings, ex.figures, None


def collect(tiers: list[Path]) -> list[Path]:
    files: list[Path] = []
    for tier in tiers:
        if not tier.exists():
            continue
        for corpus in sorted(p for p in tier.iterdir() if p.is_dir()):
            files += sorted((corpus / "references").glob("*.md"))
            files += sorted((corpus / "distillations").glob("*/*.md"))
    return [f for f in files if f.name != "README.md" and "INDEX" not in f.name]


# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("paths", nargs="*", type=Path, help="deep refs, light refs, distillations or audit fixtures")
    parser.add_argument("--source", type=Path, help="converted source to check against (single file only)")
    parser.add_argument("--all", action="store_true", help="check every reference and distillation under corpus.commons/")
    parser.add_argument("--all-local", action="store_true", help="check every reference and distillation under corpus.local/")
    parser.add_argument("--all-corpora", action="store_true", help="check both corpus.commons/ and corpus.local/")
    parser.add_argument("--no-corpus-search", action="store_true", help="don't look for missing quotes in the corpus's other sources")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of human-readable text")
    args = parser.parse_args()

    files = list(args.paths)
    if args.all or args.all_corpora:
        files += collect([TIER_ROOTS["commons"]])
    if args.all_local or args.all_corpora:
        files += collect([TIER_ROOTS["local"]])
    if not files:
        parser.error("name at least one file, or pass --all / --all-local / --all-corpora")
    if args.source and len(files) != 1:
        parser.error("--source applies to a single file")

    cache: dict = {}
    findings: list[Finding] = []
    errors: list[str] = []
    figures = 0
    for f in files:
        got, figs, err = check_file(f, args.source, not args.no_corpus_search, cache)
        findings += got
        figures += figs
        if err:
            errors.append(err)

    counts: dict[str, int] = {}
    for f in findings:
        counts[f.kind] = counts.get(f.kind, 0) + 1
    if args.json:
        print(json.dumps({"findings": [asdict(f) for f in findings], "counts": counts,
                          "figure_claims_unchecked": figures, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"{f.file}:{f.line}: {f.kind}" + (f" ({f.note})" if f.note else ""))
            if f.quote:
                print(f"    quote:  {f.quote}")
            if f.source_text:
                print(f"    source: {f.source_text}")
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        summary = ", ".join(f"{counts[k]} {k}" for k in (*LEVELS[1:], "interrupted", "cross-source", "wrong-source", "missing", "no-quote") if k in counts) or "no findings"
        print(f"\n{len(files)} file(s) checked: {summary}; {figures} figure claim(s) not checked"
              + (f"; {len(errors)} without a source" if errors else ""))

    if errors:
        return 2
    return 1 if any(f.kind in FAILING_KINDS for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
