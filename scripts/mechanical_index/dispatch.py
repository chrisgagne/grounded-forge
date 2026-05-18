"""Tier-aware handler dispatch.

Reads a discovery JSON, decides which handlers to fire, and runs them against
the converted-markdown source. Returns a single dict ready to be serialised
as ``_planning/extracted/{slug}.json``.

The dispatcher reads ``book_index.shape``, ``page_markers.present``, and
``headings.quality`` directly. It does **not** trust
``pass_h_tier_recommendation``; the discovery scan showed ~57% drift on
that field. A source can be multi-tier: Forsgren has an anchor-linked
Lists-of-Figures, a plaintext Quick Reference, and a flattened-plaintext
back-matter index all in the same file. Every applicable handler runs.
"""

from __future__ import annotations

import re
from typing import Any

from .handlers import (
    anchor_linked,
    enumerated_methods,
    flattened_plaintext,
    headings,
    page_markers,
    toc,
)


def _shape_value(discovery: dict, *path: str) -> Any:
    cur: Any = discovery
    for p in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(p)
    return cur


def _normalise_shape(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return value.strip().lower()


def _shape_is_anchor_linked(shape: str) -> bool:
    return "anchor" in shape and "link" in shape


def _shape_is_flattened_plaintext(shape: str) -> bool:
    return (
        ("flattened" in shape and "plaintext" in shape)
        or "two-column" in shape
        or "letter-grouped" in shape
        or "letter-section" in shape
        or "alphabetical" in shape  # broadest catch — also covers OCR-style two-column collapses
        or "single-column" in shape
        or "multi-level" in shape
        or "flat" in shape
    )


def _coerce_line_range(value: Any) -> tuple[int, int] | None:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        return None
    try:
        start = int(value[0])
        end = int(value[1])
    except (TypeError, ValueError):
        return None
    return (start, end) if start <= end else None


def _coerce_present(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        return bool(value.get("present"))
    if isinstance(value, str):
        s = value.strip().lower()
        if not s or s in ("absent", "none", "false", "no"):
            return False
        if s in ("true", "yes", "present"):
            return True
        return "absent" not in s and "no " not in s and s != "n/a"
    return bool(value)


def run(source_lines: list[str], discovery: dict) -> dict:
    """Run all applicable handlers and return the merged extraction record."""
    anchor_map = anchor_linked.build_anchor_map(source_lines)
    page_map = page_markers.build(source_lines)

    heading_tree = headings.extract(source_lines)

    out: dict[str, Any] = {
        "schema_version": 1,
        "slug": discovery.get("slug"),
        "source_total_lines": len(source_lines),
        "derived_tier": [],
        "handler_log": [],
        "anchor_map_size": len(anchor_map),
        "page_marker_map": page_map,
        "headings": heading_tree,
        "front_matter_toc": [],
        "book_index_entries": [],
        "enumerated_methods": [],
    }

    bi_shape = _normalise_shape(_shape_value(discovery, "book_index", "shape"))
    bi_present = _coerce_present(_shape_value(discovery, "book_index", "present"))
    bi_range = _coerce_line_range(_shape_value(discovery, "book_index", "location_line_range"))
    pm_present = _coerce_present(_shape_value(discovery, "page_markers", "present"))

    # 1. Front-matter TOC — almost universally applicable when the source has
    #    *any* markdown links resolving to in-file anchors.
    if anchor_map:
        toc_entries = toc.extract(source_lines, anchor_map=anchor_map)
        out["front_matter_toc"] = toc_entries
        if toc_entries:
            out["derived_tier"].append("toc-anchor-linked")
            out["handler_log"].append(
                {
                    "handler": "toc",
                    "entries": len(toc_entries),
                    "resolved": sum(1 for e in toc_entries if e["resolved"]),
                }
            )

    # 2. Back-matter book index — handler chosen by shape.
    if bi_present and bi_range:
        if _shape_is_anchor_linked(bi_shape):
            entries = anchor_linked.extract(
                source_lines,
                line_range=bi_range,
                region_name="back-matter-index",
                anchor_map=anchor_map,
            )
            out["book_index_entries"] = entries
            out["derived_tier"].append("anchor-linked")
            out["handler_log"].append(
                {
                    "handler": "anchor_linked",
                    "region": "back-matter-index",
                    "entries": len(entries),
                    "resolved": sum(1 for e in entries if e["resolved"]),
                }
            )
        elif _shape_is_flattened_plaintext(bi_shape):
            entries = flattened_plaintext.extract(
                source_lines,
                line_range=bi_range,
                region_name="back-matter-index",
            )
            out["book_index_entries"] = entries
            tier = "page-marker-resolved" if pm_present and page_map else "flattened-plaintext"
            out["derived_tier"].append(tier)
            out["handler_log"].append(
                {
                    "handler": "flattened_plaintext",
                    "region": "back-matter-index",
                    "entries": len(entries),
                    "page_markers_available": bool(page_map),
                }
            )
        else:
            # Unknown shape — log it and surface raw line range so the
            # semantic pass can decide what to do.
            out["handler_log"].append(
                {
                    "handler": "skip",
                    "reason": f"unknown book_index.shape: {bi_shape!r}",
                    "line_range": bi_range,
                }
            )

    # 3. Enumerated named methods — discovery JSON carries the list.
    examples = _shape_value(discovery, "enumerated_named_methods", "examples_seen") or []
    if isinstance(examples, list) and examples:
        em_records = enumerated_methods.extract(examples, source_lines, anchor_map)
        out["enumerated_methods"] = em_records
        out["derived_tier"].append("enumerated-methods")
        out["handler_log"].append(
            {
                "handler": "enumerated_methods",
                "entries": len(em_records),
                "located": sum(1 for r in em_records if r["located"]),
            }
        )

    # 4. Inference-only fallback signal.
    if not out["book_index_entries"] and not out["front_matter_toc"] and not out["enumerated_methods"]:
        out["derived_tier"].append("inference-only")
        out["handler_log"].append(
            {
                "handler": "inference_only",
                "reason": "no mechanically-extractable artefacts found",
            }
        )

    return out
