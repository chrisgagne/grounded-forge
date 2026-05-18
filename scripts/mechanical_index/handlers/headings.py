"""Heading-tree extraction.

Handles three heading conventions seen in the corpus:

  1. Native markdown: lines starting with ``#``..``######``.
  2. Pandoc-attribute headings: ``## Title {#anchor}``.
  3. Plaintext ALL-CAPS section labels (calibre-noise / sparse conversions).
     Recognised conservatively: a line ≥ 8 chars, mostly uppercase letters
     (≥ 0.7 ratio of A-Z chars in the alphabetic-character subset), no
     trailing prose punctuation, surrounded by blank lines or fenced-div
     markers.

The output is a list of ``{level, title, line, anchor}`` records. Level 0 is
reserved for plaintext ALL-CAPS labels (we can't infer a real depth without
the source's typography).
"""

from __future__ import annotations

import re
from typing import Iterable

# Native markdown heading: leading hashes + space + title, optional {#anchor}.
_MD_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*(?:\{#([A-Za-z0-9._:-]+)\})?\s*$")

# Pandoc anchor-only line — a structural landmark on a line of its own.
_ANCHOR_ONLY = re.compile(r"^\[\]\{#([A-Za-z0-9._:-]+)\}\s*$")


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
