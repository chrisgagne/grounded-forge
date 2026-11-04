#!/usr/bin/env python3
"""Verbatim-mode page locator: `Source.page` in `scripts/verbatim/resolve.py`.

The sidenote shows the printed page the resolver reads from the converted text. Two
conversions put the page number on opposite sides of the text it names:

- a Pandoc EPUB page-break anchor opens its page, so the nearest anchor above a span names it;
- the PDF converter writes an OpenStax running head after its page's body text, so the
  nearest head below a span names its page, and the head above names the page before.

The OpenStax cases are spans from the published Marines example
(`docs/examples/marines-verbatim/`), with the printed page each sits on in the original PDF.
"""
import sys, tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts" / "verbatim"))
from resolve import Source   # noqa: E402

fails = []


def check(name, got, want):
    if got != want:
        fails.append(f"{name}: got p.{got}, want p.{want}")


def source(root, converted):
    return Source("x", {"corpus": "c", "slug": Path(converted).stem, "converted": converted},
                  {"c": {"root": str(root)}})


# Real conversion: OpenStax Principles of Management, (1-based line, printed page in the PDF).
pom = source(REPO / "corpus.commons" / "demo", "sources/converted/openstax-principles-management.md")
for line, want in [(12669, 250), (25032, 500), (4527, 84), (1675, 29), (2670, 46)]:
    check(f"openstax line {line}", pom.page(line - 1), want)

with tempfile.TemporaryDirectory() as d:
    d = Path(d)
    # Synthetic OpenStax: page 8's head closes page 8; the span after it is on page 9.
    (d / "os.md").write_text("\n".join([
        "Body text on page eight, long enough to be ordinary prose in the book.",
        "",
        "8     1 • Managing and Performing",
        "",
        "The span sits here, on page nine, before page nine's own running head.",
        "",
        "1.2 • The Roles Managers Play     9",
        "",
    ]))
    check("synthetic openstax", source(d, "os.md").page(4), 9)
    # Synthetic EPUB: the anchor above the span opens its page.
    (d / "ep.md").write_text("\n".join([
        "[]{#page_11}Text on page eleven.",
        "",
        "[]{#page_12}The span sits here, on page twelve.",
        "",
        "More text on page twelve.",
        "",
        "[]{#page_13}Text on page thirteen.",
    ]))
    check("synthetic epub", source(d, "ep.md").page(4), 12)

if fails:
    print("\n".join(fails))
    sys.exit(1)
print("ok: verbatim page locator")
