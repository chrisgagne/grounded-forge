"""Front-matter table-of-contents extractor.

Most converted sources have a TOC in the first 10% of the file: markdown
links resolving to in-file anchors. The TOC is a high-value routing surface
even when no back-matter index survived (typical for calibre-from-EPUB).

This handler reuses ``anchor_linked.extract`` but biases the search to the
front-matter region: by default the first 12% of the file or the first
``max_lines`` lines, whichever is shorter. The bound is set generously
because long-form books have long TOCs (Poppendieck's 22-tool TOC runs
~500 lines).
"""

from __future__ import annotations

from . import anchor_linked


def extract(
    lines: list[str],
    max_lines: int = 600,
    front_matter_fraction: float = 0.12,
    anchor_map: dict[str, int] | None = None,
) -> list[dict]:
    bound = min(max_lines, max(50, int(len(lines) * front_matter_fraction)))
    return anchor_linked.extract(
        lines,
        line_range=(1, bound),
        region_name="front-matter-toc",
        anchor_map=anchor_map,
    )
