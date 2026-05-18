"""Anchor-linked index extractor.

Pulls every ``[concept text](#target)`` markdown link in a given line range
and resolves the ``#target`` to the line where that anchor is defined.

Anchor definitions can take three shapes:
  * Markdown heading with trailing ``{#anchor}``.
  * Standalone ``[]{#anchor}`` paragraph landmark.
  * Inline ``[]{#anchor}`` span dropped at the page-break point inside a
    paragraph (Pandoc from EPUB / Calibre).

This is the gold-standard handler: the source is doing the routing work for
us; we just lift it.
"""

from __future__ import annotations

import re
from collections import defaultdict
from typing import Iterable

_LINK = re.compile(r"\[([^\]]+?)\]\(#([A-Za-z0-9._:-]+)\)")
# Pandoc/Calibre anchor definitions:
#   {#anchor}                 — bare anchor, span landmark
#   {#anchor .class1 .class2} — heading with id + classes
#   {#anchor key=value}       — heading with key-value pair
# Only the id (the first ``#token``) is significant for our lookup.
_ANCHOR_DEF = re.compile(r"\{#([A-Za-z0-9._:-]+)(?:[\s}])")
_ATTR_SPAN = re.compile(r"\[([^\[\]]*?)\]\{[^}]*\}")


def _flatten_attr_spans(text: str) -> str:
    """Collapse pandoc/calibre ``[Text]{.class}`` spans to plain ``Text``.

    Run iteratively until no spans remain; the Calibre output nests up to
    three levels (``[[[Text]{.underline}]{.calibre6}]``).
    """
    prev = None
    cur = text
    while prev != cur:
        prev = cur
        cur = _ATTR_SPAN.sub(r"\1", cur)
    return cur


def build_anchor_map(lines: list[str]) -> dict[str, int]:
    """Map anchor-id → 1-based line number of its definition.

    The whole file is scanned so the map covers cross-section references.
    First definition wins (anchors should be unique; if duplicates appear we
    treat the earliest as the binding site).
    """
    anchors: dict[str, int] = {}
    for i, raw in enumerate(lines):
        for m in _ANCHOR_DEF.finditer(raw):
            anchor_id = m.group(1)
            if anchor_id not in anchors:
                anchors[anchor_id] = i + 1
    return anchors


def extract(
    lines: list[str],
    line_range: tuple[int, int] | None = None,
    region_name: str | None = None,
    anchor_map: dict[str, int] | None = None,
) -> list[dict]:
    """Extract anchor-linked entries from ``lines[line_range[0]-1:line_range[1]]``.

    If ``line_range`` is ``None`` the whole file is scanned. ``anchor_map`` is
    optional; when omitted it is built from the same source on the fly (slower
    if you're calling this repeatedly).
    """
    if anchor_map is None:
        anchor_map = build_anchor_map(lines)

    if line_range is None:
        start, end = 1, len(lines)
    else:
        start, end = line_range

    entries: list[dict] = []
    for i in range(start - 1, min(end, len(lines))):
        line = _flatten_attr_spans(lines[i])
        for m in _LINK.finditer(line):
            text = m.group(1).strip()
            target = m.group(2)
            target_line = anchor_map.get(target)
            entries.append(
                {
                    "kind": "entry",
                    "concept_text": text,
                    "anchor_target": target,
                    "line": i + 1,
                    "resolved_line": target_line,
                    "resolved": target_line is not None,
                    "region": region_name,
                }
            )
    return entries


def group_by_concept(entries: Iterable[dict]) -> dict[str, list[dict]]:
    """Group anchor entries by ``concept_text``."""
    out: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        out[e["concept_text"]].append(e)
    return dict(out)
