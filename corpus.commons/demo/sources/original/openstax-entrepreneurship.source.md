---
title: Entrepreneurship
author: OpenStax (Michael Laverty, Chris Littel et al.)
publisher: Rice University
publish_year: 2020
isbn: 978-1-947172-70-8
url: https://openstax.org/details/books/entrepreneurship
scope: open-nc
licence: CC BY-NC-SA 4.0
ingested: 2026-05-05
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: e2a29cee570f552360742956e9d27ef4df6aec35047d2cdc60b6b2cb24524613
---

# Source: Entrepreneurship (OpenStax)

PDF not shipped (download free from the URL above). The SHA256 above is of `Entrepreneurship-WEB.pdf` (631 pages, 129,375,799 bytes), fetched from assets.openstax.org on 2026-10-16 and held in the gitignored `sources/original/`. Its printed folios match the converted text's running headers at one page offset. Text in the earlier converted markdown that is absent from this PDF is at the level of formatting noise, so this is the edition that was converted. Converted markdown is at
`../converted/openstax-entrepreneurship.md`; deep reference at
`../../references/openstax-entrepreneurship-deep.md`.

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: 22,761 of the PDF's 23,091 text lines of 12 or more characters match line for line, and the other 330, mostly table rows and box text, have all their words on the same page with different line breaks; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage and table rows it strung across cells. This restores what pymupdf4llm 0.2.9 dropped: about 5.8% of the longer lines in the chapters the deep reference covers, mostly framed feature boxes (Link to Learning, Entrepreneur in Action, What Can You Do?, Are You Ready?, Work It Out), sometimes with the body text just before a box, in every chapter.

**Deep reference coverage.** The deep reference was read from the earlier pymupdf4llm 0.2.9 conversion, so it stays PARTIAL until Passes C–E cover the restored material (see its Coverage line).
