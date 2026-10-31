#!/usr/bin/env python3
"""Build the upload folders for the two Gemini Notebook notebooks.

whole/  one file per demo source, as the October private round and the
        gemini-notebook-arm protocol upload them: the converted Markdown, except
        doe-hpi-handbook-vol2, whose original PDF is a single redistributed file.
split/  the same, except the six target sources over 20,000 words are replaced
        by one file per chapter, cut at the lines in PLAN. The other four targets
        (Scrum Guide, Org Topologies primer, SSDL briefs, Liberating Structures)
        are already chapter-sized and go in whole, as do the 21 non-target sources.

Each PLAN entry is the first line of a chapter in the converted file (1-based,
as grep -n counts). The chapter runs to the line before the next entry. Line 1
is always a cut, so front matter rides with the first chapter.

Usage: python3 split_sources.py OUT_DIR
"""
import shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
DEMO = ROOT / "corpus.commons/demo/sources"

PLAN = {
    # first numbered section of each chapter (2.1, 3.1 ...), CHAPTER 2's own heading, then Appendix A's endnotes
    "caib-report-vol1": [1, 1946, 4237, 8472, 9796, 12966, 17685, 19583, 20855, 21296, 23538],
    # chapter title pages after the table of contents, then the endnotes
    "mcdp1-warfighting": [1, 177, 771, 1687, 2224, 3161],
    # Parts 1 to 13
    "lfuo-learning-review-guide-2024": [1, 361, 691, 848, 1156, 1221, 1901, 2438, 2666, 2934, 3195, 3557, 3830, 4401],
    # "Chapter N <title>" headings in the body
    "doe-hpi-handbook-vol1": [1, 445, 1805, 5696, 7905, 10693],
    # first "N.1" section heading of chapters 1 to 16
    "openstax-psychology-2e": [1, 935, 2207, 3909, 5583, 7407, 8904, 10410, 12061, 13526, 15747, 17315, 19233,
                               21526, 23380, 25742, 28871],
    # first "N.1" section heading of chapters 1 to 19
    "openstax-organizational-behavior": [1, 817, 1949, 3218, 4727, 6023, 7826, 9389, 11503, 13463, 15058, 16161,
                                         17268, 19125, 20570, 22283, 23475, 24857, 26352, 28038],
}

ORIGINALS = {"doe-hpi-handbook-vol2": DEMO / "original/doe-hpi-handbook-vol2.pdf"}


def sources():
    return sorted(p for p in (DEMO / "converted").glob("*.md") if p.name != "IMAGES-README.md")


def place(src, dest):
    slug = src.stem
    if slug in ORIGINALS:
        shutil.copy(ORIGINALS[slug], dest / ORIGINALS[slug].name)
    else:
        shutil.copy(src, dest / src.name)


def main():
    out = Path(sys.argv[1])
    whole, split = out / "whole", out / "split"
    for d in (whole, split):
        if d.exists():
            sys.exit(f"{d} exists")
        d.mkdir(parents=True)
    manifest = []
    for src in sources():
        place(src, whole)
        if src.stem not in PLAN:
            place(src, split)
            continue
        lines = src.read_text().split("\n")
        cuts = PLAN[src.stem] + [len(lines) + 1]
        for i, (a, b) in enumerate(zip(cuts, cuts[1:]), 1):
            name = f"{src.stem}-ch{i:02d}.md"
            (split / name).write_text("\n".join(lines[a - 1 : b - 1]) + "\n")
            manifest.append(f"{name}\t{a}-{b - 1}\t{lines[a - 1].strip()[:70]}")
    (out / "split-manifest.tsv").write_text("file\tlines\tfirst line\n" + "\n".join(manifest) + "\n")
    print(len(list(whole.iterdir())), "files in whole/,", len(list(split.iterdir())), "in split/")


if __name__ == "__main__":
    main()
