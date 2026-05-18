"""Page-marker scanner.

Builds a ``{page_number: line_number}`` map for sources where the converter
preserved print-page boundaries as anchors or sentinels.

Recognised marker shapes (Forsgren, Poppendieck, devops-handbook patterns):

  ``<<page_N>>``                          plaintext sentinel (markitdown)
  ``{#page_N}`` or ``{#page-N}``           pandoc anchor on a heading or paragraph
  ``{#chXX.html_page_N}``                  pandoc-from-EPUB anchor
  ``[]{#page_N}``                          empty-span anchor landmark

Only ``page_N`` style page references are resolved here; ``page_xxiv`` and
similar Roman-numeral front-matter markers are noted but kept as strings so
the flattened-plaintext handler can still cite them.
"""

from __future__ import annotations

import re

_MARKERS = [
    re.compile(r"<<page_([0-9]+)>>"),
    re.compile(r"\{#page[-_]([0-9]+)\}"),
    re.compile(r"\{#[A-Za-z0-9._-]*?page[-_]([0-9]+)\}"),
    re.compile(r"\[\]\{#page[-_]([0-9]+)\}"),
]


def build(lines: list[str]) -> dict[int, int]:
    """Return ``{print_page_number: line_number}`` from the converted source.

    First-seen wins (some converters leave duplicate markers; the binding
    site is the earliest occurrence).
    """
    page_to_line: dict[int, int] = {}
    for i, raw in enumerate(lines):
        for pat in _MARKERS:
            for m in pat.finditer(raw):
                page = int(m.group(1))
                if page not in page_to_line:
                    page_to_line[page] = i + 1
    return page_to_line


def resolve_range(page_to_line: dict[int, int], page: int) -> int | None:
    """Resolve a single page number to a line number, falling back to the
    nearest *preceding* marker when the exact page wasn't anchored.
    """
    if page in page_to_line:
        return page_to_line[page]
    candidates = [p for p in page_to_line if p <= page]
    if not candidates:
        return None
    return page_to_line[max(candidates)]
