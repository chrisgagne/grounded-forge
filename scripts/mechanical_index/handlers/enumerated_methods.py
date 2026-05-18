"""Enumerated-named-method extractor.

Surfaces author-curated routing structures of the form "Seven Lean Principles
/ Twenty-Two Thinking Tools / Five Core Properties of Kanban / 24 Capabilities
..." that appear repeatedly across the corpus.

The handler does *not* try to invent these; they come from the discovery
JSON's ``enumerated_named_methods.examples_seen`` field. Each entry in that
field is a one-sentence description that may include a chapter pointer
("Chapter 7, Figure 7.1") or an anchor identifier
("anchor #dummy_split_012.html_filepos93841"). The handler:

  1. Pulls the example list from the discovery JSON.
  2. Tries to bind each example to a line range in the converted source by
     searching for a verbatim heading match or an anchor match.
  3. Emits one record per example, with the location-binding success flag so
     the downstream pass can decide whether to trust the routing.

This is the smallest of the handlers; most of the work is the discovery
scan, which the LLM already did once. We just lift the result into structured
form.
"""

from __future__ import annotations

import re
from typing import Iterable


_ANCHOR_HINT = re.compile(r"#([A-Za-z0-9._:-]+)")
_LINE_HINT = re.compile(r"\bline[s]?\s*~?\s*([0-9]+)\b", re.IGNORECASE)


def _try_locate(line_text: str, anchor_map: dict[str, int], lines: list[str]) -> int | None:
    m = _LINE_HINT.search(line_text)
    if m:
        return int(m.group(1))

    m = _ANCHOR_HINT.search(line_text)
    if m and m.group(1) in anchor_map:
        return anchor_map[m.group(1)]

    # Fall back to a simple verbatim-text search for the named method.
    head = re.split(r"[—-]\s|\(", line_text, 1)[0].strip().strip("\"'")
    if 4 < len(head) < 80:
        needle = re.escape(head)
        rx = re.compile(needle, re.IGNORECASE)
        for i, raw in enumerate(lines):
            if rx.search(raw):
                return i + 1
    return None


def extract(
    examples: Iterable[str],
    lines: list[str],
    anchor_map: dict[str, int],
) -> list[dict]:
    out: list[dict] = []
    for ex in examples:
        if not isinstance(ex, str) or not ex.strip():
            continue
        located = _try_locate(ex, anchor_map, lines)
        out.append(
            {
                "method_description": ex.strip(),
                "located_line": located,
                "located": located is not None,
            }
        )
    return out
