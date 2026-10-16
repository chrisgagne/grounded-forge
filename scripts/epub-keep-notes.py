#!/usr/bin/env python3
"""Convert an EPUB to markdown with pandoc, keeping its footnote and endnote text.

pandoc's EPUB reader treats any element whose `epub:type` or `role` names a
note container (`footnote`, `rearnote`, `endnotes`, `doc-endnotes`, ...) as a
note definition. It pulls a note's text into the flow only when a link marked
`epub:type="noteref"` points at it, and otherwise drops it silently. Many
publishers' EPUBs carry plain links, so the note numbers survive in the body
and the notes themselves vanish: 6,000 to 28,000 words per book in the
private corpus.

This script copies the EPUB with every such attribute renamed to
`data-note-type` (`noteref` attributes are left alone), then runs
`pandoc -t markdown --wrap=none` on the copy. The body converts exactly as it
would from the original; the notes stay where the EPUB puts them, usually at
the end of each chapter or in a closing Notes section.

Usage:
    python3 scripts/epub-keep-notes.py BOOK.epub OUT.md

Then gate the result with scripts/check-epub-coverage.py.
"""

import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ATTR = re.compile(r'\b(epub:type|role)="([^"]*)"')


def rename(m: re.Match) -> str:
    value = m.group(2).lower()
    if 'note' in value and 'noteref' not in value:
        return f'data-note-type="{m.group(2)}"'
    return m.group(0)


def keep_notes_copy(src: Path, dst: Path) -> int:
    renamed = 0
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, 'w') as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename.lower().endswith(('.xhtml', '.html', '.htm')):
                text = data.decode('utf-8')
                renamed += sum(1 for _, v in ATTR.findall(text) if 'note' in v.lower() and 'noteref' not in v.lower())
                data = ATTR.sub(rename, text).encode('utf-8')
            # the EPUB spec requires `mimetype` first and uncompressed
            method = zipfile.ZIP_STORED if info.filename == 'mimetype' else zipfile.ZIP_DEFLATED
            zout.writestr(info, data, compress_type=method)
    return renamed


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip().split('\n\n')[-2], file=sys.stderr)
        return 2
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    with tempfile.TemporaryDirectory() as tmp:
        copy = Path(tmp) / 'keep-notes.epub'
        renamed = keep_notes_copy(src, copy)
        subprocess.run(['pandoc', str(copy), '-t', 'markdown', '--wrap=none', '-o', str(out)], check=True)
    version = subprocess.run(['pandoc', '--version'], capture_output=True, text=True).stdout.split('\n')[0]
    print(f'{out}: {version}; {renamed} note-container attribute(s) renamed')
    return 0


if __name__ == '__main__':
    sys.exit(main())
