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
    the previous evidence marker; a full stop that closes an abbreviation
    ("U.S.", "e.g.", "p.m.") ends no sentence. When that sentence is only a
    citation (`"…the end." (Ch 1, p. 5) [V]`, "(¶12)", "(same section)"),
    the segment is the sentence before it, the one the citation cites. In a
    table it is the marker's cell, or the whole row when the cell holds no
    quote. Quoted titles inside citation parentheticals are skipped: they
    cite, they don't quote. A parenthetical inside a quotation is the
    author's own and stays part of the quote.
  - A `[V]` before a colon ("Five benefits of UML (Ch 4.4) [V]:") also
    covers what the colon introduces: the rest of the line up to the next
    marker, or, when the colon ends the line, the list below it (items and
    their continuation lines, up to a heading or a paragraph). A list item
    with its own marker is that marker's.
  - Every quoted span in a blockquote (`>` lines), marker or not.

In a "Citation and Source-Integrity Notes" section a `[V]` with no quoted span
names the marker ("carries [V] markers") and is neither reported nor counted;
a quoted span there is checked as anywhere else.

Each quote is looked for at a ladder of levels and reported at the first level
that finds it:

  exact     Found once conversion noise is set aside on both sides: whitespace
            collapsed, Markdown emphasis and link syntax dropped, Pandoc's
            Markdown read as its text (`[text]{.italic}` spans, `[]{#…}`
            anchors, endnote links with their attribute blocks, a note
            number linked to its note and glued to a word dropped, backslash
            escapes, `---` and `--` as em and en dash, but not a command-line
            option's `--`), ligatures
            expanded (ﬂ → fl), zero-width characters and `<br>` dropped, a
            hyphen at a line end read as the quote spells the word (rejoined
            for a word split across the line, kept for a true compound, each
            hyphen on its own), running headers and folios between two pages
            dropped (see below), no space before punctuation, an en or em dash
            set open or closed. Double quote marks
            read as single: inside a quotation the nesting convention turns the
            source's "x" into 'x'. Trailing
            `,` `.` `;` `:` inside the closing quote mark are the quoting
            convention, not the author, and are ignored. An ellipsis (`...`,
            `…`) is an elision: each piece must appear, in order, within a few
            thousand characters. A bracketed insertion (`[the manager]`)
            stands for a short run of source text; `[sic]` is dropped.
            Nothing is reported.
  joined    As exact, and a hyphen the quote sets between two words may match
            nothing in the source, where both words, two letters or more, stand
            on their own elsewhere in the source: a compound the converter
            joined ("one-month" against "onemonth", "on-the-spot" against
            "onthe-spot"). A hyphen after a prefix the source never sets alone
            ("co-operate" against "cooperate") is no joined compound and still
            fails; nor is an en or em dash the converter dropped, even once
            the glyph level folds it to a hyphen. Read up to, not including,
            near. Not failing, and not exact either: a line-end hyphen leaves
            its mark in the source, so the exact rule knows a hyphen stood
            there; a joined compound leaves none, and an author who closed the
            compound ("email", "coworker") reads the same, so the count is
            shown.
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
  ligature  Found once every ligature (ff, fi, fl, ffi, ffl) is read as "f",
            on both sides. That covers the three ways a converter damages a
            ligature glyph: it keeps the first letter and drops the rest
            ("confrms"), it splits the ligature from its word ("fi rst",
            "fl ow"), or it writes a punctuation mark in its place ("e"ort",
            "o#ce", "signi%cant", "work!ows"). Converter damage, not the
            author's change; not failing.
  interrupted
            Found as up to four runs of the quote's words, each within a few
            hundred characters of the last. The text in each gap is shown: a
            dropped clause is a quote shortened without an ellipsis (fixture
            09's failure mode); a page header the furniture rule below missed
            is conversion noise.
  missing   Not found at any level: reworded, credited to the wrong source, or
            invented. The source text matching the quote's longest opening run
            of words is shown.
  cross-source
            Not in this file's source, but in another converted source in the
            corpus (up to the near level) that the line names (by slug, title or author): a
            distillation quoting a second source with attribution. Or in a
            second conversion of this source (the note says so): a corpus can
            hold two conversions of one book, and the one the slug resolves to
            may have lost a passage the other kept. Two files are conversions
            of one book when each holds at least a third of the other's runs
            of six words (a book that quotes another whole holds few of its
            own runs in the other), and the second is no source in its own
            right: no source card names it and no slug resolves to it. A
            paper and the thesis chapter it grew from are two sources. Not
            failing.
  wrong-source
            In another source the line doesn't name: credited to the
            wrong source, or attributed too vaguely to check.
  no-quote  A `[V]` segment with neither a quoted span nor a figure: the marker
            sits on a paraphrase (fixture 07's failure mode). A segment with
            figures and no quote is a figure claim, which the protocol's stats
            table marks `[V]`; those are counted, not checked.

Numbers at a quote's ends. At every level, a quote (or an elided piece of one)
that starts or ends on a digit matches only where the source's number starts or
ends there too: not where the source runs on into another digit, or into a `.`
or `,` and a digit. "rose by 3." against "rose by 3.5 points", "rose by 3"
against "rose by 30 points" and "hired 2," against "hired 2,500 people" are
not matches, so a figure cut short can't pass. One run-on is a note number,
not decimals: a figure that ends a sentence with a note glued after the full
stop ("as late as 2119.27 These"). It is read as a note only on the source's
own evidence, all of it: one to three digits with no leading zero, then a line
end or a word that isn't lowercase; the note before or after it (26 or 28) set
as a glued marker within a few thousand characters ("slowly.26"); and a note
entry for it opening a line ("27. Josh Horwitz"). "rose by 6." against "6.5
points" fails whatever the notes say, and so does a decimal before a capital
with no note beside it in sequence.

Running headers and folios. A page break in a converted PDF leaves page
furniture in the text: the folio at the foot of one page and the running header
at the top of the next ("87", "Warfighting", "MCDP 1"). A short line (eight
words or fewer, numbers and bullets not counted) is a running header when its
text, with digits read as one placeholder, recurs at least five times in the
source; a line one or two characters from a header (an OCR slip, "MCD? 1")
counts when it sits beside one. In a source paged with form feeds, a line among
the last three before a page break or the first two after one is a header too,
however long its title and however rarely it recurs, when the number at its
start or end runs with the page count: at least five such lines share one
offset from the page index (OpenStax's "56     2 • Introduction to Financial
Statements" and "2.6 • Personal Values and Ethics     43"). A run of header,
folio and blank lines is dropped only where it shows a page break: a form feed,
a folio line, a header whose number at its start or end changes from page to
page while a chapter or section number beside it stays ("87 Warfighting", "48 5
• Criminal Liability", "8.1 • Entrepreneurial Marketing 267"), or a header whose
folio runs with the page count. A recurring line whose numbers never change
stays in the text. A quote is looked for with the furniture in place first, so
a quote of a header's own words still matches; one that matches only once the
furniture is dropped has every other word in place.

Exit status is 1 when any finding other than `joined`, `apostrophe`, `initial`,
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

  - `references/{slug}-deep.md`, `references/{slug}.md` and
    `distillations/{task}/{slug}-{task}.md` → the slug's converted source:
    `sources/converted/{slug}.md`; else the converted file the source card
    (`sources/original/{slug}.source.md`) links to; else, for a converted
    file kept under a title-based name, the converted file that holds the
    slug's quotations: of those six words or more long, across its
    references and distillations, at least three, and at least three
    quarters of them. A slug that none of these finds is reported, with the
    closest file by content.
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
import functools
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
# A `[V]` that introduces what follows: stacked markers and a citation, then a colon.
LEAD_IN_RE = re.compile(r"(?:\s*\[(?:V|AP|AR|AE|BT)\])*\s*(?:\([^()]*\))?\s*:")
LIST_ITEM_RE = re.compile(r"\s*(?:[-*+]|\d{1,3}[.)])\s")
HEADING_RE = re.compile(r"(#{1,6})\s+(.*)")
# The section where a file describes its own evidence markers.
NOTES_HEADING_RE = re.compile(r"[*_]*citation and source-integrity notes\b", re.I)
FRONTMATTER_SEED_RE = re.compile(r"^seed_source:\s*(\S+)\s*$", re.M)
ELLIPSIS_RE = re.compile(r"\s*(?:\.\s?\.\s?\.|…)\s*")
BRACKET_RE = re.compile(r"\[[^\]]*\]")
SIC_RE = re.compile(r"\s*\[sic\]", re.I)
DIGIT_RE = re.compile(r"\d")

ELISION_WINDOW = 3000  # max characters between the pieces of an elided quote
INSERTION_WINDOW = 80  # max source characters a bracketed insertion stands for
MIN_PIECE_WORDS = 2  # elided pieces shorter than this are not located on their own

LEVELS = ("exact", "joined", "apostrophe", "glyph", "initial", "near", "page", "ligature")
FAILING_KINDS = {"glyph", "near", "page", "interrupted", "wrong-source", "missing", "no-quote"}  # not joined, apostrophe, initial, ligature or cross-source
GAP_WINDOW = 400  # max source characters between the runs of an interrupted quote
MAX_RUNS = 4  # an interrupted quote may be found in at most this many runs
MIN_RUN_WORDS = 3
MIN_CROSS_SOURCE_WORDS = 5
FURNITURE_MIN_REPEATS = 5  # a running header recurs on at least this many pages
FURNITURE_MAX_WORDS = 8
FURNITURE_MAX_CHARS = 60
FOLIO_HEADER_MAX_CHARS = 120  # a header carrying a folio that runs with the page count


# ---------------------------------------------------------------------------
# Normalisation: a pipeline of regex substitutions that keeps a map from each
# output character back to its offset in the original text, so a match can be
# shown as the source's own characters.

# Characters a converter leaves in that no reader sees: soft hyphen, zero-width
# space and joiners, word joiner, byte-order mark.
INVISIBLE = "".join(chr(c) for c in (0x00AD, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF))
LIGATURES = {"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st"}

# Pandoc's Markdown, which an EPUB conversion leaves in the text: a span with an
# attribute block ("[text]{.italic}", "[D]{.dropcap}rop"), an empty anchor
# ("[]{#ch02.html_page_17}"), or a link carrying one (an endnote link,
# "[the same plan](#notes.html_n4){#ch02.html_n4ref .calibre3}"). Each reads as
# its text. Spans nest, so the innermost is unwrapped first. A note number
# linked to its note and glued to the word before it ("badly.[3](notes.htm#n3)",
# "Writer[^1^](#note_1){#ref_1}") is the converter's, not the sentence's, and
# is dropped.
NOTE_LINK_RE = re.compile(r"(?<=\S)\[\^?\d{1,3}\^?\]\([^)\s]*#[^)\s]*\)(?:\{[^{}\n]*\})?")
PANDOC_SPAN_RE = re.compile(r"\[((?:\\.|[^\[\]\\\n])*)\](?:\([^)\s]*\))?\{[^{}\n]*\}")
PANDOC_SPAN_DEPTH = 4
ESCAPE_RE = re.compile(r"\\([!-/:-@\[-`{-~])")
BASE_STEPS = [
    (re.compile(r"\[([^\]\n]*)\]\([^)\s]*\)"), 1),  # Markdown link → its text
    # Pandoc's dashes: "---" an em dash, "--" an en dash, but not a
    # command-line option ("--all", a "--" at a word's start before a
    # letter) or an HTML comment's "<!--" and "-->".
    (re.compile(r"(?<!-)---(?!-)"), "—"),
    (re.compile(r"(?<=[^\s(\[{\"'“‘`<!\-])--(?![->])|(?<![-<!])--(?![-A-Za-z>])"), "–"),
    # A backslash escape ("don\'t", "\$5", "\[sic\]") → the character. After
    # the dashes, so an escaped "\-\-" stays two hyphens.
    (ESCAPE_RE, 1),
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
# In the source, a hyphen at a line end becomes this mark, which a quote's
# pattern reads as nothing (a word split across the line) or as a hyphen (a true
# compound), by the quote's own spelling at that point. A private-use character
# no converted text holds.
HYPHEN_MARK = "\ue000"
TAIL_STEPS = [
    (re.compile(r"\s+"), " "),
    (re.compile(r" (?=[.,;:!?)\]])"), ""),
    (re.compile(r"(?<=[(\[]) "), ""),
    (re.compile(r" ?([–—]) ?"), 1),  # an en or em dash set open or closed
]
APOSTROPHE_STEP = (re.compile("[‘’‚‛′`']"), "'")
DASH_STEP = (re.compile(r"\s*(?:[–—‐‑−]|--+)\s*|\s+-\s+"), "-")
FOOTNOTE_RE = re.compile(r"(?<=[A-Za-z.,;:')])\d{1,3}(?= |$)")
PUNCT_RE = re.compile(r"[^\w" + HYPHEN_MARK + r"]+")
LIGATURE_LOSS_RE = re.compile(r"f(?:f[il]?|[il])")  # ffi, ffl, ff, fi, fl → f
# A mark some converters write in place of a ligature glyph, inside a word
# ("e"ort", "o#ce", "signi%cant", "work!ows") or opening one ("!ow"). Double
# quotes already read as a straight single quote here, so a word-internal one is
# taken as a ligature on both sides; an apostrophe in "don't" turns to "f" in
# the quotation and the source alike, so a true match still holds.
LIGATURE_MARK_RE = re.compile(r"(?<=[a-z])['#%!](?=[a-z])|(?<![a-z'])[#%!](?=[a-z])")
LIGATURE_SPLIT_RE = re.compile(r"(?<=f) (?=[a-z])")  # "f rst" once "fi rst" reads as "f rst"
PAGE_RE = re.compile(r"(?<![^ ])\d{1,4} ")
# A number running on past a quote's end or before its start, in the source's
# own characters: a digit, or a decimal point or thousands separator and a
# digit. Emphasis marks between are read through.
NUMBER_AFTER_RE = re.compile(r"[*_]*[.,]?[*_]*\d")
NUMBER_BEFORE_RE = re.compile(r"\d[*_]*[.,]?[*_]*$")
# A note number glued to a figure that ends a sentence ("as late as 2119.27
# These"): a full stop, one to three digits with no leading zero, then a line
# end or a space and no lowercase word.
GLUED_NOTE_RE = re.compile(r"\.([1-9]\d{0,2})(?:\s+(?=[^\sa-z])|\s*\Z)")
# A note number glued to a word, as the source's other notes are set
# ("Red Bull.11", "variability11", "existence.”23"). The digit before a
# decimal point is no letter, so a decimal is never taken for one.
NOTE_MARKER_RE = re.compile(
    r"(?:(?<=[a-z])|(?<=[a-z][.,;:)'’”\]])|(?<=[a-z][.,;:)'’”\]][.,;:)'’”\]]))([1-9]\d{0,2})(?=\s|$)")
NOTE_SEQUENCE_WINDOW = 10000  # max characters to the next or previous note number


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


def _drop(text: str, idx: list[int], spans: list[tuple[int, int]]) -> tuple[str, list[int]]:
    """Replace each (start, end) span of `text` with a line break, carrying the
    offset map. Spans are sorted and don't overlap."""
    out: list[str] = []
    oidx: list[int] = []
    last = 0
    for a, b in spans:
        out.append(text[last:a] + "\n")
        oidx.extend(idx[last:a])
        oidx.append(idx[a])
        last = b
    out.append(text[last:])
    oidx.extend(idx[last:])
    return "".join(out), oidx


def normalise(text: str, level: str, hyphen: str = "join",
              drop: list[tuple[int, int]] | None = None) -> tuple[str, list[int]]:
    """Normalise `text` for one rung of the ladder. `hyphen` is "join" (rejoin
    a word split across a line) or "mark" (leave HYPHEN_MARK, for a quote's
    pattern to resolve). `drop` lists spans of page furniture to set aside."""
    rank = LEVELS.index(level)
    s, idx = text, list(range(len(text)))
    if drop:
        s, idx = _drop(s, idx, drop)
    s, idx = _sub(s, idx, NOTE_LINK_RE, "")
    for _ in range(PANDOC_SPAN_DEPTH):
        if not PANDOC_SPAN_RE.search(s):
            break
        s, idx = _sub(s, idx, PANDOC_SPAN_RE, 1)
    for pat, repl in BASE_STEPS:
        s, idx = _sub(s, idx, pat, repl)
    s, idx = _sub(s, idx, HYPHEN_RE, "" if hyphen == "join" else HYPHEN_MARK)
    for pat, repl in TAIL_STEPS:
        s, idx = _sub(s, idx, pat, repl)
    if rank >= LEVELS.index("apostrophe"):
        s, idx = _sub(s, idx, *APOSTROPHE_STEP)
    if rank >= LEVELS.index("glyph"):
        s, idx = _sub(s, idx, *DASH_STEP)
    if rank >= LEVELS.index("near"):
        s, idx = _sub(s, idx, FOOTNOTE_RE, "")
        s, idx = _lower(s, idx)
        if rank >= LEVELS.index("ligature"):
            s, idx = _sub(s, idx, LIGATURE_MARK_RE, "f")
        s, idx = _sub(s, idx, PUNCT_RE, " ")
    if rank >= LEVELS.index("page"):
        s, idx = _sub(s, idx, PAGE_RE, "")
    if rank >= LEVELS.index("ligature"):
        s, idx = _sub(s, idx, LIGATURE_LOSS_RE, "f")
        s, idx = _sub(s, idx, LIGATURE_SPLIT_RE, "")
    return s, idx


FOLIO_LINE_RE = re.compile(r"\d{1,4}")
SENTENCE_END_RE = re.compile(r"[.?!;:,]$")


def _furniture_key(line: str) -> str:
    """A line's text for spotting a running header: emphasis dropped, case
    folded, every number read as one placeholder."""
    return re.sub(r"\s+", " ", re.sub(r"\d+", "#", re.sub(r"[*_]+", "", line).strip().lower()))


def _within(a: str, b: str, limit: int) -> bool:
    """Levenshtein distance between a and b is at most `limit`."""
    if abs(len(a) - len(b)) > limit:
        return False
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        if min(cur) > limit:
            return False
        prev = cur
    return prev[-1] <= limit


FOLIO_START_RE = re.compile(r"(\d{1,4})\s")
FOLIO_END_RE = re.compile(r"\s(\d{1,4})$")


def _folio_headers(raw: str, lines: list[tuple[int, int, str, bool]]) -> set[int]:
    """Indices of the lines that are a page's header or footer carrying its
    folio, in a source paged with form feeds (see the module docstring): among
    the last three lines before a page break or the first two after one, a
    line whose number at its start or end runs with the page count. However
    long its title, and however rarely it recurs."""
    breaks = [m.start() for m in re.finditer(r"\f+", raw)]
    if len(breaks) < FURNITURE_MIN_REPEATS:
        return set()
    pages: list[list[int]] = [[] for _ in range(len(breaks) + 1)]
    b = 0
    for n, (start, _, text, _) in enumerate(lines):
        while b < len(breaks) and breaks[b] < start:
            b += 1
        if text.strip():
            pages[b].append(n)
    candidates: list[tuple[int, int]] = []  # (line index, folio minus page index)
    for p, members in enumerate(pages):
        edge = (members[:2] if p > 0 else []) + (members[-3:] if p < len(breaks) else [])
        for n in dict.fromkeys(edge):
            t = re.sub(r"[*_]+", "", lines[n][2]).strip()
            if (not t or len(t) > FOLIO_HEADER_MAX_CHARS or t[0] in "#|" or re.search(r"[.,;:]$", t)
                    or len(re.findall(r"[A-Za-z]", t)) < 2):
                continue
            for m in (FOLIO_START_RE.match(t), FOLIO_END_RE.search(t)):
                if m:
                    candidates.append((n, int(m.group(1)) - p))
    support: dict[int, int] = {}
    for _, off in candidates:
        support[off] = support.get(off, 0) + 1
    return {n for n, off in candidates if support[off] >= FURNITURE_MIN_REPEATS}


def furniture_spans(raw: str) -> list[tuple[int, int]]:
    """Spans of running headers and folios at page breaks (see the module
    docstring): each a run of header, folio and blank lines that shows a page
    break, from its first non-blank line to its last."""
    lines = []  # (start, end, text, after a form feed)
    for m in re.finditer(r"[^\n\f]*", raw):
        if m.start() == m.end() and m.start() > 0 and raw[m.start() - 1] not in "\n\f":
            continue
        lines.append((m.start(), m.end(), m.group(0), m.start() > 0 and raw[m.start() - 1] == "\f"))

    def short(text: str) -> bool:
        """A line a running header could be: short (words with letters
        counted, not numbers or bullets; emphasis marks not counted), two
        letters or more, not a sentence end, a Markdown heading or a table row."""
        t = text.strip()
        return (0 < len(re.sub(r"[*_]+", "", t)) <= FURNITURE_MAX_CHARS
                and sum(bool(re.search(r"[A-Za-z]", w)) for w in t.split()) <= FURNITURE_MAX_WORDS
                and len(re.findall(r"[A-Za-z]", t)) >= 2 and not SENTENCE_END_RE.search(t)
                and t[0] not in "#|")

    counts: dict[str, int] = {}
    edges: dict[str, tuple[set[str], set[str]]] = {}
    for _, _, text, _ in lines:
        if short(text):
            k = _furniture_key(text)
            counts[k] = counts.get(k, 0) + 1
            nums = re.findall(r"\d+", text)
            first, last = edges.setdefault(k, (set(), set()))
            first.add(nums[0] if nums else "")
            last.add(nums[-1] if nums else "")
    headers = {k for k, n in counts.items() if n >= FURNITURE_MIN_REPEATS}
    folio_headers = _folio_headers(raw, lines)
    if not headers and not folio_headers:
        return []
    # A header carrying the folio: a number at the start or the end that
    # changes from page to page ("87 Warfighting", "48 5 • Criminal
    # Liability", not "Table 3.2"). A chapter or section number beside it
    # stays the same.
    numbered = {k for k in headers
                if (k.startswith("# ") and len(edges[k][0]) > 1) or (k.endswith(" #") and len(edges[k][1]) > 1)}
    near: dict[str, bool] = {}

    def kind(text: str) -> str:
        t = text.strip()
        if not t:
            return "blank"
        if FOLIO_LINE_RE.fullmatch(t):
            return "folio"
        if short(t):
            k = _furniture_key(t)
            if k in headers:
                return "numbered" if k in numbered else "header"
            if k not in near:
                near[k] = len(k) >= 4 and any(_within(k, h, 2 if len(h) >= 6 else 1) for h in headers)
            if near[k]:
                return "near-header"
        return "text"

    kinds_of = ["numbered" if n in folio_headers and kind(ln[2]) != "folio" else kind(ln[2])
                for n, ln in enumerate(lines)]
    spans: list[tuple[int, int]] = []
    i = 0
    while i < len(lines):
        if kinds_of[i] == "text":
            i += 1
            continue
        j = i
        while j < len(lines) and kinds_of[j] != "text":
            j += 1
        run = list(zip(lines[i:j], kinds_of[i:j]))
        kinds = set(kinds_of[i:j])
        # A near-header counts only beside a true header, and a page break must show.
        has_header = kinds & {"header", "numbered"}
        page_break = "folio" in kinds or "numbered" in kinds or any(ln[3] for ln, _ in run)
        if has_header and page_break:
            body = [ln for ln, k in run if k != "blank"]
            spans.append((body[0][0], body[-1][1]))
        i = j
    return spans


class Source:
    """A converted source, normalised lazily per (level, hyphen, furniture) rung."""

    def __init__(self, path: Path):
        self.path = path
        self.raw = path.read_text(encoding="utf-8", errors="replace")
        self.furniture = furniture_spans(self.raw)
        self._forms: dict[tuple[str, str, bool], tuple[str, list[int]]] = {}
        self._notes: list[tuple[int, int]] | None = None
        self._words: set[str] | None = None
        self._runs: set[int] | None = None

    def same_text(self, other: Source) -> bool:
        """`other` is another conversion of this source: each holds at least
        COPY_MIN_SHARE of the other's runs of RUN_WORDS words. Two conversions
        of one book share most of their runs; a book that quotes another, or a
        later edition's new chapters, shares few of the larger file's."""
        a, b = self.runs(), other.runs()
        shared = len(a & b)
        return bool(a and b) and shared >= COPY_MIN_SHARE * len(a) and shared >= COPY_MIN_SHARE * len(b)

    def runs(self) -> set[int]:
        if self._runs is None:
            self._runs = word_runs(self.raw)
        return self._runs

    def words(self) -> set[str]:
        """The source's words, lowercased, with a word split across a line rejoined."""
        if self._words is None:
            self._words = set(re.findall(r"[^\W\d_]+", self.form("exact", "join")[0].lower()))
        return self._words

    def form(self, level: str, hyphen: str, furniture: bool = False) -> tuple[str, list[int]]:
        """With `furniture`, page furniture is dropped first."""
        key = (level, hyphen, furniture)
        if key not in self._forms:
            self._forms[key] = normalise(self.raw, level, hyphen, self.furniture if furniture else None)
        return self._forms[key]

    def furniture_modes(self) -> tuple[bool, ...]:
        return (False, True) if self.furniture else (False,)

    def number_intact(self, idx: list[int], start: int, end: int, lead: bool, tail: bool) -> bool:
        """The match text[start:end] doesn't cut a number short: with `lead`
        (the quote starts on a digit) the source's number doesn't run on before
        it; with `tail` (it ends on one), not after it."""
        if tail:
            a = idx[end - 1] + 1
            if NUMBER_AFTER_RE.match(self.raw, a, a + 8) and not self.glued_note(a):
                return False
        if lead:
            a = idx[start]
            if NUMBER_BEFORE_RE.search(self.raw[max(0, a - 8) : a]):
                return False
        return True

    def glued_note(self, a: int) -> bool:
        """What runs on at raw[a] is a note number glued to the figure, not
        its decimals: a full stop and a note number closing the sentence
        (GLUED_NOTE_RE), the note before or after it set as a glued marker
        nearby, and an entry for it in the notes."""
        m = GLUED_NOTE_RE.match(self.raw, a)
        if not m:
            return False
        n = int(m.group(1))
        if self._notes is None:
            self._notes = [(x.start(), int(x.group(1))) for x in NOTE_MARKER_RE.finditer(self.raw)]
        in_sequence = any((k == n - 1 and a - NOTE_SEQUENCE_WINDOW <= pos < a)
                          or (k == n + 1 and a < pos <= a + NOTE_SEQUENCE_WINDOW)
                          for pos, k in self._notes)
        # A note entry opens a line: "27. Josh Horwitz", "27 . John", "11 Ken".
        entry = re.search(rf"(?m)^[*_]*{n}[*_]*(?: ?\.[ \t]+| )(?=[A-Z“\"‘'(])", self.raw)
        return in_sequence and entry is not None

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


def citation_parens(segment: str) -> list[tuple[int, int]]:
    """Spans of the citation parentheticals outside quoted spans. A
    parenthetical a quotation holds whole is the author's own words."""
    quotes = [m.span() for m in QUOTE_RE.finditer(segment)]
    return [m.span() for m in CITATION_PAREN_RE.finditer(segment)
            if not any(a < m.start() and m.end() <= b for a, b in quotes)]


def _inside(pos: int, spans: list[tuple[int, int]]) -> bool:
    return any(a <= pos < b for a, b in spans)


def quoted_spans(segment: str) -> list[str]:
    """Quoted spans, less quoted titles inside a citation parenthetical. A
    span that runs into one pairs a stray quote mark (a quotation opened on an
    earlier line) with a title's, and is no quotation either."""
    parens = citation_parens(segment)
    return [(m.group(1) or m.group(2)).strip() for m in QUOTE_RE.finditer(segment)
            if not _inside(m.start(), parens) and not any(m.start() < a < m.end() for a, _ in parens)]


def without_citations(segment: str) -> str:
    parens = citation_parens(segment)
    return "".join(" " if _inside(i, parens) else c for i, c in enumerate(segment))


# A full stop that closes an abbreviation ends no sentence: a dotted initialism
# ("U.S.", "e.g.", "i.e.", "p.m.") or a short title ("Dr.", "vs."). "etc." often
# does end one, so it is left out.
ABBREVIATION_RE = re.compile(r"(?:(?<![A-Za-z.])(?:[A-Za-z]\.){2,}|\b(?:Mr|Mrs|Ms|Dr|vs|cf)\.)$")


# What a citation leaves once its parentheticals are gone: spaces, emphasis
# marks, punctuation.
CITATION_RESIDUE_RE = re.compile(r"[\s*_.,;:—–-]*")
PAREN_RE = re.compile(r"\([^()]*\)")


def citation_only(text: str) -> bool:
    """`text` is nothing but parentheticals: a quotation's citation or locator
    standing after its sentence ("(Ch 1, p. 5)", "(¶12)", "(same section)")."""
    return bool(PAREN_RE.search(text)) and CITATION_RESIDUE_RE.fullmatch(PAREN_RE.sub("", text)) is not None


def sentence_tail(segment: str) -> str:
    """The last sentence of a segment: the text after the last sentence end
    that sits outside quotation marks and citation parentheticals ("p. 22").
    A `[V]` covers the sentence it closes, not an illustrative phrase quoted a
    sentence earlier. When that last sentence is only a citation, the
    quotation it cites ends the sentence before ("…the end." (Ch 1, p. 5)
    [V]), and the `[V]` covers that one."""
    in_quote, starts = False, [0]
    parens = citation_parens(segment)
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
        if c == "." and ABBREVIATION_RE.search(segment, 0, i + 1):
            ends = False
        if ends and not _inside(i, parens):
            rest = segment[i + 1 :].lstrip("*_)")
            # A sentence end with nothing after it is the end of the sentence
            # the [V] closes, not the start of a new one.
            if rest[:1].isspace() and rest.strip():
                starts.append(i + 1)
    if len(starts) > 1 and citation_only(segment[starts[-1] :]):
        return segment[starts[-2] :]
    return segment[starts[-1] :]


def lead_in_list(lines: list[str], i: int) -> list[tuple[int, str, bool]]:
    """The list after a lead-in line `lines[i]`, as (index, text, marked)
    triples: past any blank lines, list items and their indented continuation
    lines until a heading or a paragraph. `marked` is set on the lines of an
    item that carries its own evidence marker."""
    items: list[tuple[int, str, bool]] = []
    started = marked = False
    for k in range(i + 1, len(lines)):
        ln = lines[k]
        if not ln.strip():
            continue
        if LIST_ITEM_RE.match(ln):
            started, marked = True, bool(MARKER_RE.search(INLINE_CODE_RE.sub(" ", ln)))
        elif not (ln[:1].isspace() and started):
            break
        items.append((k, INLINE_CODE_RE.sub(" ", ln), marked))
    return items


def extract(text: str) -> Extracted:
    lines = text.split("\n")
    ex = Extracted()
    in_code = False
    notes_level = 0  # the heading level of the notes section we're in, or 0
    for i in range(body_start(lines), len(lines)):
        raw = lines[i]
        stripped = raw.lstrip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code or stripped.startswith("<!--"):
            continue
        heading = HEADING_RE.match(raw)
        if heading:
            level = len(heading.group(1))
            if NOTES_HEADING_RE.match(heading.group(2)):
                notes_level = level
            elif level <= notes_level:
                notes_level = 0
        lineno = i + 1
        line = INLINE_CODE_RE.sub(" ", raw)
        if stripped.startswith(">"):
            ex.spans.extend(Span(lineno, q, "blockquote", raw) for q in quoted_spans(line.lstrip()[1:]))
            continue
        is_row = stripped.startswith("|")
        prev_end = 0
        seen: set[tuple[int, str]] = set()
        markers = list(MARKER_RE.finditer(line))
        for n, m in enumerate(markers):
            if m.group(1) == "V":
                if is_row:
                    # The marker's own cell, or the whole row when the cell holds no quote.
                    cell = line[line.rfind("|", 0, m.start()) + 1 : m.start()]
                    segment = cell if quoted_spans(cell) else line[: m.start()]
                else:
                    # Drop the previous marker's trailing citation.
                    segment = re.sub(r"^\s*\([^()]*\)[.,;]?", "", line[prev_end : m.start()])
                    segment = sentence_tail(segment)
                found = [(lineno, q, raw) for q in quoted_spans(segment)]
                covered, quoted = segment, False
                lead = None if is_row else LEAD_IN_RE.match(line, m.end())
                if lead:
                    # A `[V]` before a colon covers what the colon introduces:
                    # the rest of the line up to the next marker, or the list
                    # on the lines below when the colon ends the line. An item
                    # with its own marker is that marker's to check.
                    stop = next((x.start() for x in markers[n + 1 :] if x.start() >= lead.end()), len(line))
                    after = line[lead.end() : stop]
                    if after.strip():
                        covered += after
                        found += [(lineno, q, raw) for q in quoted_spans(after)]
                    else:
                        for k, item, marked in lead_in_list(lines, i):
                            covered += item
                            quotes = quoted_spans(item)
                            quoted = quoted or bool(quotes)
                            if not marked:
                                found += [(k + 1, q, lines[k]) for q in quotes]
                quoted = quoted or bool(found)
                # A quote the lead-in and the next marker's segment both take is checked once.
                ex.spans.extend(Span(ln, q, "V", lt) for ln, q, lt in found if (ln, q) not in seen)
                seen.update((ln, q) for ln, q, _ in found)
                # In the notes section a `[V]` with no quote names the marker
                # ("carries [V] markers"): neither a quotation nor a figure.
                if not quoted and not notes_level:
                    if DIGIT_RE.search(without_citations(covered)):
                        ex.figures += 1
                    else:
                        ex.no_quote.append(lineno)
            prev_end = m.end()
    return ex


# ---------------------------------------------------------------------------
# Matching


def _literal(lit: str, level: str, any_initial: bool) -> str:
    """A pattern for one literal run of a quote. A hyphen mark in the source
    may sit between any two letters, where it reads as nothing, or stand for a
    hyphen the quote sets between two letters (a space, once punctuation is
    folded), where it reads as that compound's hyphen. A joined-compound mark
    (the joined level) reads as a hyphen, a hyphen mark or nothing."""
    out: list[str] = []
    mark = re.escape(HYPHEN_MARK)
    hyphens = "- " if LEVELS.index(level) >= LEVELS.index("near") else "-"
    for i, c in enumerate(lit):
        prev, nxt = lit[i - 1 : i], lit[i + 1 : i + 2]
        if c == JOINED_MARK:
            out.append(f"[-{mark}]?")
            continue
        if c in hyphens and prev.isalpha() and nxt.isalpha():
            out.append(f"[{re.escape(c)}{mark}]")
            continue
        if i == 0 and any_initial and c.isalpha():
            out.append(f"[{re.escape(c.lower())}{re.escape(c.upper())}]")
        else:
            out.append(re.escape(c))
        if c.isalpha() and nxt.isalpha():
            out.append(mark + "?")
    return "".join(out)


# A hyphen between two letters in the quote as written, before dashes are
# folded: an en or em dash is never a joined compound's hyphen.
COMPOUND_HYPHEN_RE = re.compile(r"(?<=[^\W\d_])-(?=[^\W\d_])")
# A quote's hyphen that may read as nothing in the source (see the joined
# level). A private-use character no quotation holds.
JOINED_MARK = "\ue001"


def mark_joined(piece: str, words: set[str]) -> str:
    """Mark each hyphen in `piece` that joins two words of two letters or more
    the source uses on their own ("one-month", "dead-end"), not a prefix
    ("co-", "re-") the source never sets alone."""
    def repl(m: re.Match) -> str:
        left = re.search(r"[^\W\d_]+$", piece[: m.start()]).group(0).lower()
        right = re.match(r"[^\W\d_]+", piece[m.end() :]).group(0).lower()
        ok = len(left) >= 2 and len(right) >= 2 and left in words and right in words
        return JOINED_MARK if ok else "-"
    return COMPOUND_HYPHEN_RE.sub(repl, piece)


def _piece_pattern(piece: str, level: str, any_initial: bool) -> tuple[re.Pattern, int] | None:
    """A pattern for one elided piece, and the most source text it can span;
    bracketed insertions become a short wildcard. With `any_initial`, the first
    letter matches either case."""
    lits = [normalise(p, level)[0].strip() for p in BRACKET_RE.split(piece)]
    if not "".join(lits):
        return None
    esc = [_literal(x, level, any_initial and k == 0) for k, x in enumerate(lits)]
    reach = sum(map(len, lits)) + INSERTION_WINDOW * (len(lits) - 1)
    return re.compile((r".{0,%d}?" % INSERTION_WINDOW).join(esc), re.S), reach


def _pieces(quote: str) -> list[str]:
    # A quote copied from Pandoc's Markdown can keep its escapes ("\[W\]e");
    # unescaped first, its brackets read as the bracket rules say.
    quote = SIC_RE.sub("", ESCAPE_RE.sub(r"\1", quote)).rstrip(",.;: ")
    pieces = [p for p in ELLIPSIS_RE.split(quote) if p.strip()]
    return [p for p in pieces if len(p.split()) >= MIN_PIECE_WORDS] or pieces


def locate(quote: str, src: Source, level: str) -> tuple[int, int, list[int]] | None:
    pieces = _pieces(quote)
    if not pieces:
        return None
    any_initial = level == "initial"
    norm_level = {"initial": "glyph", "joined": "exact"}.get(level, level)
    rank = LEVELS.index(level)
    # Joined compounds are read from the joined level up to, not including,
    # near: there a hyphen and a space are one, and a dropped space is no
    # joined compound.
    if LEVELS.index("joined") <= rank < LEVELS.index("near"):
        pieces = [mark_joined(p, src.words()) for p in pieces]
    pats = []  # (pattern, reach, starts on a digit, ends on a digit)
    for k, piece in enumerate(pieces):
        pat = _piece_pattern(piece, norm_level, any_initial and k == 0)
        if pat is not None:
            lit = normalise(piece, norm_level)[0].strip()
            pats.append((*pat, lit[:1].isdigit(), lit[-1:].isdigit()))
    if not pats:
        return None
    for furniture in src.furniture_modes():
        text, idx = src.form(norm_level, "mark", furniture)
        first, _, lead, tail = pats[0]
        for m in first.finditer(text):
            if not src.number_intact(idx, m.start(), m.end(), lead, tail):
                continue
            end, ok = m.end(), True
            for p, reach, p_lead, p_tail in pats[1:]:
                nxt = next((n for n in p.finditer(text, end, end + ELISION_WINDOW + reach)
                            if src.number_intact(idx, n.start(), n.end(), p_lead, p_tail)), None)
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
    text, idx = src.form("page", "join", furniture=True)
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
    text, idx = src.form("page", "join", furniture=True)
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


def classify(span: Span, src: Source, others: list[Path], cache: dict,
             sources: CorpusSources | None = None) -> Finding | None:
    """The span's level, or None at exact. `sources` tells a second
    conversion of this source from a source in its own right."""
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
            if not (sources and sources.is_own_source(other)) and src.same_text(cache[other]):
                return Finding("", span.line, "cross-source", span.text, "",
                               f"found in {other.stem}, another conversion of this source")
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


def slug_of(path: Path) -> str:
    """The source slug a reference or distillation is named for."""
    name = path.stem
    if path.parent.parent.name == "distillations":
        task = path.parent.name
        if name.endswith(f"-{task}"):
            name = name[: -len(task) - 1]
    elif name.endswith("-deep"):
        name = name[: -len("-deep")]
    return name


@functools.lru_cache(maxsize=None)
def inode(p: Path) -> tuple[int, int]:
    """A file's identity: a path the filesystem matches without regard to
    case names the same file as the path that matches it exactly."""
    st = p.stat()
    return st.st_dev, st.st_ino


CARD_LINK_RE = re.compile(r"\]\((\.\./converted/[^)]+\.md)\)")
WORD_RE = re.compile(r"[^\W_]+")
RUN_WORDS = 6  # a run of this many words seldom recurs in an unrelated text
CONTENT_MIN_QUOTES = 3
CONTENT_MIN_SHARE = 0.75
COPY_MIN_SHARE = 1 / 3


def word_runs(text: str) -> set[int]:
    """Hashes of every run of RUN_WORDS words in `text`, lowercased."""
    w = WORD_RE.findall(text.lower())
    return {hash(t) for t in zip(*(w[i:] for i in range(RUN_WORDS)))}


class CorpusSources:
    """Which converted source each slug's files quote, in one corpus.

    By name first: `sources/converted/{slug}.md`, then the converted-text link
    on the source card (`sources/original/{slug}.source.md`). A conversion
    made before that convention can keep a title-based filename ("A Book
    Title -- Writer, A. -- 2011 -- Publisher.md") and have no card, so a slug
    that neither names is found by content: the converted file that holds the
    most of the slug's quotations (in its references and distillations, those
    of RUN_WORDS words or more), when it holds at least CONTENT_MIN_QUOTES of
    them and at least CONTENT_MIN_SHARE. A file found so is the slug's source
    as if it bore the slug's name. A slug whose files quote too few words, or
    quote no one file enough, stays without a source and is reported."""

    def __init__(self, root: Path):
        self.root = root
        self.converted = sorted((root / "sources" / "converted").glob("*.md"))
        files: dict[str, list[Path]] = {}
        for f in collect_corpus(root):
            files.setdefault(slug_of(f), []).append(f)
        self.files = files
        by_inode = {inode(p): p for p in self.converted}
        self.named: dict[str, Path] = {}
        for slug in files:
            p = self._by_name(slug)
            if p is not None and inode(p) in by_inode:
                self.named[slug] = by_inode[inode(p)]
        # The converted files named as sources in their own right by a slug
        # or a source card, whether by the card's own name or its link.
        self.own_sources = set(self.named.values())
        for card in sorted((root / "sources" / "original").glob("*.source.md")):
            p = self._by_name(card.name[: -len(".source.md")])
            if p is not None and inode(p) in by_inode:
                self.own_sources.add(by_inode[inode(p)])
        self._content: dict[str, tuple[Path | None, str]] | None = None

    def _by_name(self, slug: str) -> Path | None:
        direct = self.root / "sources" / "converted" / f"{slug}.md"
        if direct.is_file():
            return direct
        card = self.root / "sources" / "original" / f"{slug}.source.md"
        if card.is_file():
            m = CARD_LINK_RE.search(card.read_text(encoding="utf-8", errors="replace"))
            if m and (card.parent / m.group(1)).is_file():
                return card.parent / m.group(1)
        return None

    def resolve(self, slug: str) -> tuple[Path | None, str]:
        """The slug's converted source, or None and why."""
        if slug in self.named:
            return self.named[slug], ""
        return self.by_content().get(slug, (None, ""))

    def is_own_source(self, p: Path) -> bool:
        """`p` is a source in its own right: a source card names it or a slug
        resolves to it. Any other converted file is a conversion no one
        named, and may be a second conversion of a named source."""
        return p in self.own_sources or any(p == q for q, _ in self.by_content().values())

    def by_content(self) -> dict[str, tuple[Path | None, str]]:
        if self._content is None:
            self._content = self._by_content()
        return self._content

    def _by_content(self) -> dict[str, tuple[Path | None, str]]:
        quotes: dict[str, list[set[int]]] = {}
        for slug, paths in self.files.items():
            if slug in self.named:
                continue
            spans = {s.text for p in paths for s in extract(p.read_text(encoding="utf-8")).spans}
            quotes[slug] = [r for r in map(word_runs, sorted(spans)) if r]
        wanted = set().union(*(r for qs in quotes.values() for r in qs))
        held = {p: word_runs(p.read_text(encoding="utf-8", errors="replace")) & wanted for p in self.converted}
        out: dict[str, tuple[Path | None, str]] = {}
        for slug, qs in quotes.items():
            ranked = sorted(((sum(1 for q in qs if q & runs), p) for p, runs in held.items()), key=lambda x: (-x[0], x[1]))
            if not qs or not ranked or not ranked[0][0]:
                out[slug] = (None, "")
                continue
            hits, best = ranked[0]
            if hits >= CONTENT_MIN_QUOTES and hits >= CONTENT_MIN_SHARE * len(qs):
                out[slug] = (best, "")
            else:
                out[slug] = (None, f"the closest by content, {best.name}, holds {hits} of {len(qs)} quotations")
        return out


SOURCES: dict[Path, CorpusSources] = {}


def corpus_sources(root: Path) -> CorpusSources:
    if root not in SOURCES:
        SOURCES[root] = CorpusSources(root)
    return SOURCES[root]


def resolve_source(path: Path, text: str) -> tuple[Path | None, str]:
    """The converted source a file quotes, or None and why."""
    seed = FRONTMATTER_SEED_RE.search(text[:2000])
    if seed and seed.group(1) != "synthetic":
        return find_seed_source(seed.group(1)), ""
    root = corpus_root_of(path)
    if root is None:
        return None, ""
    return corpus_sources(root).resolve(slug_of(path))


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
    src_path, why = (source_override, "") if source_override else resolve_source(path, text)
    if src_path is None:
        return findings, ex.figures, f"{rel}: no converted source found (pass --source)" + (f"; {why}" if why else "")
    src = cache.get(src_path)
    if src is None:
        src = cache[src_path] = Source(src_path)
    others: list[Path] = []
    sources = None
    if search_corpus:
        root = corpus_root_of(src_path)
        if root:
            others = [p for p in sorted((root / "sources" / "converted").glob("*.md")) if inode(p) != inode(src_path)]
            sources = corpus_sources(root)
    for span in ex.spans:
        f = classify(span, src, others, cache, sources)
        if f:
            f.file = rel
            if span.context == "blockquote":
                f.note = "; ".join(x for x in ("blockquote", f.note) if x)
            findings.append(f)
    findings.sort(key=lambda f: f.line)
    return findings, ex.figures, None


def collect_corpus(corpus: Path) -> list[Path]:
    files = sorted((corpus / "references").glob("*.md")) + sorted((corpus / "distillations").glob("*/*.md"))
    return [f for f in files if f.name != "README.md" and "INDEX" not in f.name]


def collect(tiers: list[Path]) -> list[Path]:
    files: list[Path] = []
    for tier in tiers:
        if not tier.exists():
            continue
        for corpus in sorted(p for p in tier.iterdir() if p.is_dir()):
            files += collect_corpus(corpus)
    return files


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
