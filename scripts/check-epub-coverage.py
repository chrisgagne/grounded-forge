#!/usr/bin/env python3
"""Gate an EPUB conversion: find text the EPUB holds that the converted markdown lacks.

The reference is the EPUB's own XHTML, read in spine order with a plain HTML
parser (script, style and head skipped), so it doesn't share any converter's
blind spots. A converter can't be checked against its own output: pandoc
compared with pandoc can't see what pandoc drops.

Every reference word is marked covered when a 6-word window containing it
occurs in the markdown (words are runs of letters, lowercased; markdown
attribute spans and link targets are stripped first). A gap is a run of 25 or
more uncovered words. Gaps are reported with their spine document and the
first words of the missing text.

Exit status: 0 when no gap lies outside the EPUB's navigation document,
1 otherwise. Contents pages that aren't the nav document, title and copyright
pages, and reflowed tables can show up as gaps; read each one and record any
you accept on the source card. A gap inside chapter text, notes or sidebars is
lost content: re-convert. For pandoc, use scripts/epub-keep-notes.py, which
keeps the footnote and endnote text pandoc otherwise drops.

Usage:
    python3 scripts/check-epub-coverage.py BOOK.epub CONVERTED.md [--min-gap 25]
"""

import argparse
import posixpath
import re
import sys
import unicodedata
import zipfile
from html.parser import HTMLParser
from urllib.parse import unquote

K = 6
BLOCK = {'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr', 'td', 'th', 'br',
         'blockquote', 'section', 'aside', 'dt', 'dd', 'figcaption', 'caption', 'pre'}


def words(text: str) -> list[str]:
    text = unicodedata.normalize('NFKD', text.replace('­', '')).lower()
    return re.findall(r'[a-z]+', text)


class TextOf(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ('head', 'script', 'style'):
            self.skip += 1
        if tag in BLOCK:
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('head', 'script', 'style'):
            self.skip -= 1
        if tag in BLOCK:
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def spine_documents(epub: zipfile.ZipFile):
    container = epub.read('META-INF/container.xml').decode('utf-8', 'replace')
    opf_path = re.search(r'full-path="([^"]+)"', container).group(1)
    base = posixpath.dirname(opf_path)
    opf = epub.read(opf_path).decode('utf-8', 'replace')
    items, nav = {}, set()
    for tag in re.findall(r'<(?:\w+:)?item\b[^>]*>', opf):
        attr = dict(re.findall(r'([\w:-]+)="([^"]*)"', tag))
        if 'id' in attr and 'href' in attr:
            path = posixpath.normpath(posixpath.join(base, unquote(attr['href'])))
            items[attr['id']] = path
            if 'nav' in attr.get('properties', '').split():
                nav.add(path)
    for idref in re.findall(r'<(?:\w+:)?itemref\b[^>]*idref="([^"]+)"', opf):
        path = items.get(idref)
        if path and path in epub.namelist():
            yield path, path in nav


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('epub')
    ap.add_argument('markdown')
    ap.add_argument('--min-gap', type=int, default=25)
    args = ap.parse_args()

    md = open(args.markdown, encoding='utf-8', errors='replace').read()
    md = re.sub(r'\{[#.][^}]*\}', ' ', md)          # pandoc attribute spans
    md = re.sub(r'\]\((?:#|https?:|mailto:)[^)\s]*\)', ']', md)  # link targets
    md = re.sub(r'<[^>]{1,40}>', ' ', md)
    mw = words(md)
    windows = {tuple(mw[i:i + K]) for i in range(len(mw) - K + 1)}

    seq, doc_of, is_nav = [], [], []
    with zipfile.ZipFile(args.epub) as epub:
        for path, nav in spine_documents(epub):
            parser = TextOf()
            parser.feed(epub.read(path).decode('utf-8', 'replace'))
            w = words(''.join(parser.parts))
            seq += w
            doc_of += [path] * len(w)
            is_nav += [nav] * len(w)

    covered = [False] * len(seq)
    for i in range(len(seq) - K + 1):
        if tuple(seq[i:i + K]) in windows:
            for j in range(i, i + K):
                covered[j] = True

    gaps, i = [], 0
    while i < len(seq):
        if covered[i]:
            i += 1
            continue
        j = i
        while j < len(seq) and not covered[j]:
            j += 1
        if j - i >= args.min_gap:
            gaps.append((i, j))
        i = j

    blocking = [(i, j) for i, j in gaps if not is_nav[i]]
    lost = sum(j - i for i, j in blocking)
    print(f'{args.markdown}: {len(seq)} EPUB words; {len(gaps)} gap(s) of {args.min_gap}+ words, '
          f'{len(blocking)} outside the nav document ({lost} words, {100 * lost / max(len(seq), 1):.2f}%)')
    for i, j in sorted(gaps, key=lambda g: g[0] - g[1]):
        tag = 'nav ' if is_nav[i] else ''
        print(f'  {tag}{doc_of[i]}: {j - i} words: {" ".join(seq[i:min(j, i + 18)])} ...')
    return 1 if blocking else 0


if __name__ == '__main__':
    sys.exit(main())
