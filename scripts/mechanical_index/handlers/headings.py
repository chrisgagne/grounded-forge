"""Heading-tree extraction.

Handles four heading conventions seen in the corpus:

  1. Native markdown: lines starting with ``#``..``######``.
  2. Pandoc-attribute headings: ``## Title {#anchor}``.
  3. Plaintext ALL-CAPS section labels (calibre-noise / sparse conversions).
     Recognised conservatively: a line ≥ 8 chars, mostly uppercase letters
     (≥ 0.7 ratio of A-Z chars in the alphabetic-character subset), no
     trailing prose punctuation, surrounded by blank lines or fenced-div
     markers.
  4. Numbered plaintext section headings (journal-article shape):
     ``1. Introduction`` / ``2.1. Polysaccharides and dietary fibers`` /
     ``5.1.1. Beverages``. PDF-to-markdown converters (markitdown,
     pymupdf4llm) drop heading typography on two-column article layouts, so
     a paper's entire section spine arrives as ordinary body lines and the
     first three conventions see nothing. Recognised only when the numbering
     corroborates *across the whole document* — see ``_spine_corroborated``.

The output is a list of ``{level, title, line, anchor}`` records. Level 0 is
reserved for plaintext ALL-CAPS labels (we can't infer a real depth without
the source's typography); numbered plaintext headings take their level from
the depth of the number (``2.1.`` → level 2).
"""

from __future__ import annotations

import re
from typing import Iterable

# Native markdown heading: leading hashes + space + title, optional {#anchor}.
_MD_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*(?:\{#([A-Za-z0-9._:-]+)\})?\s*$")

# Pandoc anchor-only line — a structural landmark on a line of its own.
_ANCHOR_ONLY = re.compile(r"^\[\]\{#([A-Za-z0-9._:-]+)\}\s*$")

# Numbered plaintext section heading, two accepted forms.
#
# The trailing dot after the number is required for a single-level heading
# (``1. Introduction``). Without it the shape collides with wrapped body prose
# (``20 cones terminating the second cycle were observed...``), running page
# headers (``1440 G. Gastaminza et al``) and author affiliations (``1
# Department of Orthopedics...``). A multi-level number (``2.1 Animal
# Procedures``) is distinctive enough on its own, so the dot is optional there.
_NUMBERED_HEADING = re.compile(r"^(\d{1,2}(?:\.\d{1,2}){0,3})\.\s+(\S.*?)\s*$")
_NUMBERED_HEADING_NODOT = re.compile(r"^(\d{1,2}(?:\.\d{1,2}){1,3})\s+(\S.*?)\s*$")

# Section titles are short noun phrases, not sentences.
_TITLE_MAX_CHARS = 100
_TITLE_MAX_WORDS = 16
_TITLE_WORD = re.compile(r"[A-Za-z]{3,}")

# Reference-list entries are the dangerous look-alike: ``12. Smith, J. (2019).
# Title. Journal, 4(2), 1-10.`` shares the leading-number shape exactly.
_REFERENCE_TELL = re.compile(
    r"(?:https?://|\bdoi[:.]|\bet\s+al\b|\bpp?\.\s*\d|\(\s*(?:1[6-9]|20)\d{2}[a-z]?\s*\))",
    re.IGNORECASE,
)

# ``Addison S, Armstrong C`` / ``Smith, J.`` author-list openings. Case-
# sensitive on purpose — the capitalisation *is* the signal.
_AUTHOR_LIST = re.compile(r"^[A-Z][A-Za-z'’-]+,?\s+(?:[A-Z]\.|[A-Z]{1,3}\b,)")

# Numbered prose enumerations in body text ("1. First, ... 2. Second, ...")
# open with a sequence adverb and a comma. Section titles do not; the comma is
# what separates ``Second, the matrix invites...`` from ``Third Party Risk``.
_DISCOURSE_OPENER = re.compile(
    r"^(?:First|Second|Third|Fourth|Fifth|Sixth|Next|Then|Finally|Lastly|Also|"
    r"Additionally|Moreover|Furthermore|However|Therefore|Thus|Conversely)\s*[,:]\s",
    re.IGNORECASE,
)

# Back-matter boundary. Everything past it is reference-list territory.
_REFERENCE_SECTION = {
    "references",
    "reference",
    "bibliography",
    "literature cited",
    "works cited",
    "references cited",
}

# Corroboration thresholds for the numbered-section spine.
_SPINE_MIN_HEADINGS = 4
_SPINE_MIN_TOP_LEVELS = 3
_SPINE_MIN_TOP_LEVELS_FLAT = 4  # no subsections anywhere → demand a longer spine
_SPINE_MAX_TOP_LEVEL = 12
_SPINE_MIN_SPREAD = 0.4
_SPINE_MIN_SPAN_LINES = 100
_SPINE_MIN_MONOTONIC = 0.6
_SPINE_MIN_UNIQUE = 0.9


def _is_allcaps_label(line: str) -> bool:
    s = line.strip()
    if len(s) < 8:
        return False
    if s.startswith(("#", ">", "-", "*", "|", ":", "[", "`")):
        return False
    if s.endswith((".", ",", ";", "?", "!")):
        return False
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 6:
        return False
    upper = sum(1 for c in letters if c.isupper())
    return upper / len(letters) >= 0.7


def _is_section_title(title: str) -> bool:
    """Does the text after the number look like a section title?

    Rejects sentences, table cells, unit-bearing measurement rows, citation
    entries and author lists. Deliberately strict: a wrong section pointer
    routes the runtime to the wrong passage, which is worse than no pointer.
    """
    probe = title.strip("*_ ‘’\"")
    if not (3 <= len(probe) <= _TITLE_MAX_CHARS):
        return False
    if not probe[0].isalpha() or not probe[0].isupper():
        return False
    if probe[-1] in ".,;:?!":
        return False
    if "=" in probe:  # numbered formula list, not a section
        return False
    if len(probe.split()) > _TITLE_MAX_WORDS:
        return False
    if _REFERENCE_TELL.search(probe) or _AUTHOR_LIST.match(probe):
        return False
    if _DISCOURSE_OPENER.match(probe):
        return False
    dense = [c for c in probe if not c.isspace()]
    letters = [c for c in dense if c.isalpha()]
    if not dense or len(letters) / len(dense) < 0.6:
        return False
    return bool(_TITLE_WORD.search(probe))


def _numbered_candidate(line: str, lineno: int) -> dict | None:
    """Shape test for one line. Document-level corroboration comes later."""
    if not line[:1].isdigit():
        return None
    m = _NUMBERED_HEADING.match(line) or _NUMBERED_HEADING_NODOT.match(line)
    if not m:
        return None
    number, title = m.group(1), m.group(2)
    if not _is_section_title(title):
        return None
    parts = tuple(int(p) for p in number.split("."))
    return {
        "level": len(parts),
        "title": line.strip(),
        "line": lineno,
        "anchor": None,
        "kind": "numbered-plaintext",
        "_number": parts,
    }


def _reference_region_start(lines: list[str]) -> int | None:
    """Line number where the back-matter reference list begins, if any.

    Takes the *last* bare reference-section label in the back half of the
    file: two-column conversions scatter stray ``References`` lines through
    the body (figure-caption fragments), and only the final one is the real
    boundary.
    """
    found: int | None = None
    for i, raw in enumerate(lines):
        if i < len(lines) // 2:
            continue
        s = re.sub(r"[*_#`\s]+", " ", raw).strip().rstrip(".").lower()
        if s in _REFERENCE_SECTION:
            found = i + 1
    return found


def _spine_corroborated(candidates: list[dict], total_lines: int) -> bool:
    """Does the candidate set actually look like a document's section spine?

    A single ``4. Wall disruption`` is indistinguishable from the fourth step
    of a numbered procedure, so the decision is taken over the whole set:

      * enough of them to be a spine at all;
      * top-level numbers starting at 0 or 1, near-contiguous, and bounded —
        papers do not have 40 top-level sections, reference lists do;
      * numbers used once each — a spine never repeats ``3.``, whereas a
        document carrying several enumerated lists restarts at 1 every time;
      * spread across the document, in both absolute and relative terms —
        enumerated lists inside Methods, diagram-label lists and numbered
        table rows cluster locally, section spines do not;
      * numbering mostly ascending in reading order. Only *mostly*, and the
        bar is deliberately low: two-column PDF conversions interleave the
        columns, so a real spine arrives partly out of order (one two-column review emits
        ``3.4`` before ``3.1`` and ``4.`` before ``3.8``, scoring 0.92).
        Strict monotonicity would reject the very sources this convention
        exists for, and ordering is the weakest of the five signals anyway —
        the four above already account for every look-alike we have seen.
    """
    if len(candidates) < _SPINE_MIN_HEADINGS or total_lines <= 0:
        return False

    numbers = [c["_number"] for c in candidates]
    if len(set(numbers)) / len(numbers) < _SPINE_MIN_UNIQUE:
        return False

    tops = sorted({n[0] for n in numbers})
    if tops[0] not in (0, 1) or tops[-1] > _SPINE_MAX_TOP_LEVEL:
        return False
    if len(tops) < tops[-1] - tops[0]:  # at most one missing top-level section
        return False

    has_subsections = any(len(n) > 1 for n in numbers)
    min_tops = _SPINE_MIN_TOP_LEVELS if has_subsections else _SPINE_MIN_TOP_LEVELS_FLAT
    if len(tops) < min_tops:
        return False

    span = candidates[-1]["line"] - candidates[0]["line"]
    if span < _SPINE_MIN_SPAN_LINES or span / total_lines < _SPINE_MIN_SPREAD:
        return False

    pairs = list(zip(numbers, numbers[1:]))
    ascending = sum(1 for a, b in pairs if b >= a)
    return ascending / len(pairs) >= _SPINE_MIN_MONOTONIC


def _numbered_plaintext(lines: list[str], claimed: set[int]) -> list[dict]:
    """Convention 4 end to end: collect candidates, then accept or reject
    the set as a whole. ``claimed`` holds lines another convention already
    took, so a numbered ALL-CAPS label isn't emitted twice.
    """
    cutoff = _reference_region_start(lines)
    candidates: list[dict] = []
    for i, raw in enumerate(lines):
        lineno = i + 1
        if lineno in claimed:
            continue
        if cutoff is not None and lineno >= cutoff:
            break
        cand = _numbered_candidate(raw.rstrip("\n"), lineno)
        if cand:
            candidates.append(cand)

    if not _spine_corroborated(candidates, len(lines)):
        return []
    for c in candidates:
        del c["_number"]
    return candidates


def extract(lines: list[str]) -> list[dict]:
    out: list[dict] = []
    n = len(lines)
    for i, raw in enumerate(lines):
        line = raw.rstrip("\n")

        m = _MD_HEADING.match(line)
        if m:
            hashes, title, anchor = m.group(1), m.group(2).strip(), m.group(3)
            out.append(
                {
                    "level": len(hashes),
                    "title": title,
                    "line": i + 1,
                    "anchor": anchor,
                    "kind": "markdown",
                }
            )
            continue

        m = _ANCHOR_ONLY.match(line)
        if m:
            out.append(
                {
                    "level": None,
                    "title": None,
                    "line": i + 1,
                    "anchor": m.group(1),
                    "kind": "anchor-only",
                }
            )
            continue

        if _is_allcaps_label(line):
            prev_blank = i == 0 or lines[i - 1].strip() == "" or lines[i - 1].strip().startswith(":")
            next_blank = i + 1 >= n or lines[i + 1].strip() == "" or lines[i + 1].strip().startswith(":")
            if prev_blank and next_blank:
                out.append(
                    {
                        "level": 0,
                        "title": line.strip(),
                        "line": i + 1,
                        "anchor": None,
                        "kind": "allcaps",
                    }
                )

    numbered = _numbered_plaintext(lines, {h["line"] for h in out})
    if numbered:
        out.extend(numbered)
        out.sort(key=lambda h: h["line"])
    return out


def first_anchor_after(headings: Iterable[dict], line: int) -> str | None:
    """Find the nearest anchor-only landmark at or after ``line``.

    Used by the anchor-linked extractor to bind ALL-CAPS section labels to a
    Pandoc fenced-div identifier.
    """
    for h in headings:
        if h["kind"] == "anchor-only" and h["line"] >= line:
            return h["anchor"]
    return None
