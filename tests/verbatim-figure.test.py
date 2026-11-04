#!/usr/bin/env python3
"""Verbatim mode: a passage that names a figure gets the source's own figure.

Two rules, both in code rather than the model:

- the resolver attaches a figure the placed passage itself names ("As Exhibit 4.4 shows"),
  through `FIGURE_NAME` in `scripts/verbatim/resolve.py`;
- where the image index files images by PDF page rather than by figure name (OpenStax), the
  render step finds the PDF page carrying the figure's caption and takes the index's one entry
  for that page (`figure_by_page` in `scripts/verbatim/render.py`).

The page lookup needs PyMuPDF; without it, the test re-runs itself under uv.
"""
import os, subprocess, sys, tempfile
from pathlib import Path

try:
    import pymupdf as fitz
except ImportError:
    try:
        import fitz
    except ImportError:
        if os.environ.get("GF_FIGURE_TEST_REEXEC"):
            sys.exit("PyMuPDF unavailable even under uv")
        env = dict(os.environ, GF_FIGURE_TEST_REEXEC="1")
        sys.exit(subprocess.call(["uv", "run", "-q", "--python", "3.12", "--with", "pymupdf", "python", __file__], env=env))

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts" / "verbatim"))
from resolve import FIGURE_NAME, Source   # noqa: E402
from render import figure_by_page   # noqa: E402

fails = []


def check(name, got, want):
    if got != want:
        fails.append(f"{name}: got {got!r}, want {want!r}")


# Which sentences name a figure.
for text, want in [
    ("As Exhibit 4.4 shows, these organizational forms work best in unstable environments.", "Exhibit 4.4"),
    ("The curve in Figure 12 bends early.", "Figure 12"),
    ("See Fig. 23 for the doubling times.", "Fig. 23"),
    ("Exhibits of this kind are common in figure skating.", None),
    ("Table 17.2 lists the goals.", None),   # a table is already text in the conversion
]:
    m = FIGURE_NAME.search(text)
    check(f"name in {text[:30]!r}", m.group(0) if m else None, want)

with tempfile.TemporaryDirectory() as d:
    root = Path(d)
    conv = root / "sources" / "converted"; conv.mkdir(parents=True)
    orig = root / "sources" / "original"; orig.mkdir(parents=True)
    (conv / "book.md").write_text("\n".join([
        "Some text before the exhibit, on the first page.",
        "",
        "Exhibit 4.4 Company Industry Fit Adapted from: Duncan, R. (1972).",
        "American Science Quarterly, 17; Daft, R. Organizational Theory and Design.",
        "",
        "As Exhibit 4.4 shows, these organizational forms work best in unstable, complex, changing environments.",
    ]))
    # A three-page PDF; the caption is on page 2, and the index files that page's image.
    doc = fitz.open()
    for body in ("Some text before the exhibit, on the first page.",
                 "Exhibit 4.4 Company Industry Fit Adapted from: Duncan, R. (1972).",
                 "As Exhibit 4.4 shows, these organizational forms work best."):
        doc.new_page().insert_text((72, 72), body)
    doc.save(str(orig / "book.pdf"))
    (conv / "IMAGE-INDEX.yaml").write_text("\n".join([
        "- file: book-images/p0001-1.png",
        "  source_ref: book",
        "  page: 1",
        "- file: book-images/p0002-1.png",
        "  source_ref: book",
        "  page: 2",
        "- file: other-images/p0002-1.png",
        "  source_ref: other",
        "  page: 2",
        "",
    ]))

    src = Source("x", {"corpus": "c", "slug": "book", "converted": "sources/converted/book.md"}, {"c": {"root": str(root)}})
    fig = src.figure("Exhibit 4.4")
    check("caption line", fig and fig["line"], 3)
    check("no image by name", fig and fig["image"], None)
    check("wrapped caption kept whole", fig and fig["caption"],
          "Exhibit 4.4 Company Industry Fit Adapted from: Duncan, R. (1972). American Science Quarterly, 17; Daft, R. Organizational Theory and Design.")

    source = {"slug": "book", "original": "sources/original/book.pdf"}
    found = figure_by_page(root, source, fig["caption"], fitz)
    check("image by caption page", found and found[0], "sources/converted/book-images/p0002-1.png")
    check("no image for a caption not in the PDF", figure_by_page(root, source, "Exhibit 9.9 Nowhere in this book", fitz), None)

if fails:
    print("\n".join(fails))
    sys.exit(1)
print("ok: verbatim figures")
