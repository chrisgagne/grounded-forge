#!/usr/bin/env python3
"""Build the upload folders for the two Gemini Notebook notebooks, from the original files.

The whole notebook is the October round's Q20 notebook (the original files behind
AAR Maker's 22 open sources: 26 files, SSDL as five briefs and the Open Practice
Library's pages joined into one Markdown file) plus the nine demo sources it
lacked, as their original PDFs. Nothing is converted.

add/    the nine PDFs added to the Q20 notebook for this round.
split/  the chunk-size control, which the round didn't run (the sources stayed as
        ingested): the same 35 files, except the six target sources over 20,000 words are cut
        into one PDF per chapter with qpdf, at the pages in PLAN (page ranges only;
        the pages themselves are unchanged).

PLAN gives each chapter's first page (1-based); a piece runs to the page before
the next entry. Page 1 is always a cut, so front matter rides with it. Pages were
found by each chapter's heading (CAIB: the page after each chapter's endnotes;
OpenStax: the PDF outline).

Usage: [GF_ORIGINALS=DIR] python3 split_pdfs.py Q20_DIR OUT_DIR
"""
import os, shutil, subprocess, sys
from pathlib import Path

# the originals are gitignored, so a worktree has none; point GF_ORIGINALS at a checkout that does
ORIG = Path(os.environ.get("GF_ORIGINALS", Path(__file__).resolve().parents[4] / "corpus.commons/demo/sources/original"))

ADD = {
    "openstax-accounting-vol1.pdf": ORIG,
    "openstax-accounting-vol2.pdf": ORIG,
    "openstax-business-law.pdf": ORIG,
    "openstax-economics-3e.pdf": ORIG,
    "openstax-entrepreneurship.pdf": ORIG,
    "openstax-introduction-business.pdf": ORIG,
    "openstax-principles-finance.pdf": ORIG,
    "openstax-principles-marketing.pdf": ORIG,
    # not in the repo's original/ folder; NIST SP 800-218 v1.1 as ingested
    "nist-ssdf-1-1.pdf": Path("/Users/Shared/gf-main-checkout-backup-2026-10-22/chrisgagne-agent-built-software/sources/original"),
}

PLAN = {
    # front matter + ch 1, then the page after each chapter's endnotes; ch 11 (recommendations) runs into the appendices
    "caib-report-vol1": [1, 28, 50, 86, 98, 121, 178, 196, 206, 214, 226],
    # front matter, chapters 1-4 (title pages), notes
    "mcdp1-warfighting": [1, 10, 30, 60, 78, 106],
    # front matter, Parts 1-13
    "lfuo-learning-review-guide-2024": [1, 8, 14, 17, 22, 23, 35, 44, 48, 53, 58, 64, 69, 83],
    # front matter, chapters 1-5
    "doe-hpi-handbook-vol1": [1, 9, 31, 81, 109, 143],
    # outline: front matter + ch 1, ch 2-16, references and index
    "openstax-psychology-2e": [1, 47, 83, 121, 157, 193, 225, 259, 291, 333, 371, 411, 457, 495, 547, 609, 645],
    # outline: front matter + ch 1, ch 2-19, appendices, references and index
    "openstax-organizational-behavior": [1, 45, 71, 99, 125, 159, 189, 231, 265, 295, 317, 341, 379, 407, 437, 469,
                                         497, 525, 557, 585],
}


def pages(pdf):
    out = subprocess.run(["qpdf", "--show-npages", str(pdf)], capture_output=True, text=True, check=True)
    return int(out.stdout)


def main():
    q20, out = Path(sys.argv[1]), Path(sys.argv[2])
    add, split = out / "add", out / "split"
    for d in (add, split):
        if d.exists():
            sys.exit(f"{d} exists")
        d.mkdir(parents=True)
    for name, src in ADD.items():
        shutil.copy(src / name, add / name)
        shutil.copy(src / name, split / name)
    q20_files = sorted(p for p in q20.iterdir() if p.suffix in (".pdf", ".md") and p.name != "INC-2291-AAR.md")
    assert len(q20_files) == 26, [p.name for p in q20_files]
    manifest = []
    for p in q20_files:
        if p.stem not in PLAN:
            shutil.copy(p, split / p.name)
            continue
        cuts = PLAN[p.stem] + [pages(p) + 1]
        for i, (a, b) in enumerate(zip(cuts, cuts[1:]), 1):
            name = f"{p.stem}-ch{i:02d}.pdf"
            subprocess.run(["qpdf", "--empty", "--pages", str(p), f"{a}-{b - 1}", "--", str(split / name)], check=True)
            manifest.append(f"{name}\tpages {a}-{b - 1}")
    (out / "split-manifest.tsv").write_text("file\tpages\n" + "\n".join(manifest) + "\n")
    print(len(list(add.iterdir())), "files in add/,", len(list(split.iterdir())), "in split/")


if __name__ == "__main__":
    main()
