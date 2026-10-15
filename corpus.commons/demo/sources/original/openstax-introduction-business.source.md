---
title: Introduction to Business
author: OpenStax (Lawrence J. Gitman, Carl McDaniel, Amit Shah et al.)
publisher: Rice University
publish_year: 2018
isbn: 978-1-947172-55-5
url: https://openstax.org/details/books/introduction-business
scope: open
licence: CC BY 4.0
ingested: 2026-05-05
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: 2395bd23185badbe637b06878ebb2b8d9e9c9e85a49a77b0be6f0904bb312dcd
---

# Source: Introduction to Business (OpenStax)

The only OpenStax book in the demo corpus under genuinely-permissive CC BY 4.0
(the other 11 are CC BY-NC-SA 4.0). PDF not shipped (download free from the URL above). The SHA256 above is of `IntroductionToBusiness-OP.pdf` (743 pages, 53,432,925 bytes), fetched from assets.openstax.org on 2026-10-16 and held in the gitignored `sources/original/`. Its revision number (IB-2018-000(09/18)-BKB) and table-of-contents folios match the converted text. Its revision number (IB-2018-000(09/18)-BKB) and table-of-contents folios match the converted text, and its body text matches word for word, but it is not the identical file: the earlier conversion's front matter carried a web-view promotional page and the citation URL `…/Introduction-Business`, which this file lacks (it reads `…/Introduction-to-Business`). OpenStax has deprecated this first edition and its API no longer links a PDF, so this assets.openstax.org file is the closest available; the re-conversion below is from it. Converted markdown at `../converted/openstax-introduction-business.md`;
deep reference at `../../references/openstax-introduction-business-deep.md`.

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: 24,447 of the PDF's 25,009 text lines of 12 or more characters match line for line, and the other 562, mostly glossary entries and table rows, have all their words on the same page with different line breaks; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage and table rows it strung across cells. This restores what pymupdf4llm 0.2.9 dropped: about 10.8% of the longer lines in the chapters the deep reference covers, mostly framed feature boxes (Managing Change, Concept Check, Ethics in Practice, Catching the Entrepreneurial Spirit, Expanding Around the Globe, Customer Satisfaction and Quality), sometimes with the body text just before a box, in every chapter.

**Deep reference coverage.** The deep reference was read from the earlier pymupdf4llm 0.2.9 conversion, so it stays PARTIAL until Passes C–E cover the restored material (see its Coverage line).
