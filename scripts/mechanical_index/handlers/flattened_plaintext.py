"""Flattened-plaintext index extractor.

Operates on a back-matter index whose locators are printed page numbers, not
anchors. Each entry has the shape ``concept text, N`` or ``concept text, N,
M-O`` and may span multiple paragraphs; sub-entries are concept-only lines
followed by page-bearing sub-bullets.

The handler is conservative on purpose:

  * It only extracts entries inside the supplied ``line_range``.
  * It treats a line as an entry if and only if the trailing tokens parse as
    a page-locator list (one or more page-numbers or page-ranges, comma-
    separated, optionally with Roman-numeral front-matter pages).
  * It surfaces the *parent* concept text but does not try to merge multi-
    paragraph hierarchies; that is a semantic-pass responsibility.
  * Page-number → line-range resolution is deferred to the dispatcher, which
    threads the ``page_markers`` map in when one is available.
"""

from __future__ import annotations

import re

_ROMAN = "ivxlcdm"

# A single locator is either a print-page number (digits) or a Roman-numeral
# (front-matter), optionally followed by ``-N`` or ``-M-N`` for a range, and
# optionally followed by a single suffix letter (``f`` figure, ``n`` note,
# ``t`` table).
_LOC_TOKEN = re.compile(
    r"(?:(?:[0-9]+|[" + _ROMAN + r"]+)(?:[-–](?:[0-9]+|[" + _ROMAN + r"]+))?[fnt]?)",
    re.IGNORECASE,
)

# The trailing locator list: 1+ locator tokens separated by commas and
# whitespace, anchored to end-of-line.
_TRAILING_LOCATORS = re.compile(
    r"(?:^|,\s*)(" + _LOC_TOKEN.pattern + r"(?:\s*,\s*" + _LOC_TOKEN.pattern + r")*)\s*$",
    re.IGNORECASE,
)

# A single-letter paragraph (alphabetical section divider).
_LETTER_DIVIDER = re.compile(r"^[A-Z]$")

# "See" and "See also" prose cross-refs.
_SEE_CROSSREF = re.compile(r"^(.+?)\.\s+\*?See(?:\s+also)?\*?\s+(.+)$", re.IGNORECASE)

# Structural sub-headers that appear inside Forsgren-style indexes
# (correlated with: / negatively correlated with: / not correlated with:).
_STRUCT_HEADER = re.compile(r"^[a-z][a-z\s-]+:\s*$", re.IGNORECASE)


def _parse_locators(text: str) -> list[dict]:
    out: list[dict] = []
    for tok in text.split(","):
        tok = tok.strip()
        if not tok:
            continue
        suffix = None
        if tok and tok[-1].lower() in "fnt" and len(tok) > 1 and not tok[-2].isalpha():
            suffix = tok[-1].lower()
            tok = tok[:-1]
        if "-" in tok or "–" in tok:
            parts = re.split(r"[-–]", tok)
            if len(parts) == 2:
                out.append(
                    {
                        "kind": "range",
                        "start": parts[0].strip(),
                        "end": parts[1].strip(),
                        "suffix": suffix,
                    }
                )
                continue
        out.append({"kind": "single", "page": tok, "suffix": suffix})
    return out


def _strip_styling(line: str) -> str:
    """Drop pandoc/calibre attribute spans so the matcher sees clean text."""
    s = re.sub(r"\[([^\]]*?)\]\{[^}]*\}", r"\1", line)
    s = re.sub(r"\{#[A-Za-z0-9._:-]+\}", "", s)
    s = re.sub(r"\{\.[A-Za-z0-9._-]+\}", "", s)
    return s.strip()


def _is_fence_noise(line: str) -> bool:
    """Pandoc/Calibre fenced-div boundaries and bare section labels."""
    s = line.strip()
    if not s:
        return True
    if s.startswith(":") or s.endswith(":::") or s.startswith("```"):
        return True
    if s in ("INDEX", "Index"):
        return True
    if re.fullmatch(r":{2,}.*", s):
        return True
    return False


def extract(
    lines: list[str],
    line_range: tuple[int, int],
    region_name: str = "back-matter-index",
) -> list[dict]:
    start, end = line_range
    end = min(end, len(lines))

    entries: list[dict] = []
    current_letter: str | None = None
    pending_parent: str | None = None  # concept line awaiting sub-entries

    for i in range(start - 1, end):
        raw = _strip_styling(lines[i])
        if not raw:
            continue
        if _is_fence_noise(raw):
            continue

        if _LETTER_DIVIDER.match(raw):
            current_letter = raw
            pending_parent = None
            continue

        # Bare-concept lines clear any previous parent before we test
        # locator continuations below.
        # (Don't clear here — fall through; the "bare concept" branch will
        # set a new pending_parent and the cleanup happens implicitly.)

        # See / See also cross-references.
        m = _SEE_CROSSREF.match(raw)
        if m:
            entries.append(
                {
                    "kind": "cross-reference",
                    "concept_text": m.group(1).strip(),
                    "see": m.group(2).strip(),
                    "line": i + 1,
                    "letter_section": current_letter,
                    "region": region_name,
                }
            )
            pending_parent = None
            continue

        # Structural sub-headers ("correlated with:" etc.).
        if _STRUCT_HEADER.match(raw):
            entries.append(
                {
                    "kind": "structural-header",
                    "header": raw.rstrip(":").strip(),
                    "line": i + 1,
                    "letter_section": current_letter,
                    "parent": pending_parent,
                    "region": region_name,
                }
            )
            continue

        # Trailing-locator entries (the canonical case).
        m = _TRAILING_LOCATORS.search(raw)
        if m:
            locator_text = m.group(1)
            concept_text = raw[: m.start()].rstrip(", ").strip()
            if not concept_text:
                continue
            looks_like_continuation = (
                pending_parent is not None
                and (
                    concept_text[0].islower()
                    or concept_text.split()[0].lower()
                    in {"and", "the", "in", "for", "of", "with", "as", "by", "on", "to", "see"}
                )
            )
            parent = pending_parent if looks_like_continuation else None
            if not looks_like_continuation:
                pending_parent = None
            entries.append(
                {
                    "kind": "entry",
                    "concept_text": concept_text,
                    "locators": _parse_locators(locator_text),
                    "line": i + 1,
                    "letter_section": current_letter,
                    "parent": parent,
                    "region": region_name,
                }
            )
            continue

        # Bare concept line (no locator) — likely a parent of indented
        # sub-entries below it. Record it as a parent so the dispatcher's
        # semantic-pass instruction set can stitch hierarchy if it wants.
        if 2 < len(raw) < 80 and not raw.endswith(":"):
            pending_parent = raw
            entries.append(
                {
                    "kind": "parent",
                    "concept_text": raw,
                    "line": i + 1,
                    "letter_section": current_letter,
                    "region": region_name,
                }
            )

    return entries
