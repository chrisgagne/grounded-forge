---
title: Principles of Management
author: OpenStax (David S. Bright, Anastasia H. Cortes, Donald G. Gardner et al.)
publisher: Rice University
publish_year: 2019
isbn: 978-0-9986257-7-5
url: https://openstax.org/details/books/principles-management
scope: open-nc
licence: CC BY-NC-SA 4.0
ingested: 2026-05-05
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: 59ea3ea149d631f57c26279d5ac71f588121ebc56c1a25eb6c76f011c9765b6d
---

# Source: Principles of Management (OpenStax)

PDF not shipped (download free from the URL above). The SHA256 above is of `principles-management_-_WEB.pdf` (605 pages, 65,629,502 bytes), fetched from assets.openstax.org on 2026-10-16 and held in the gitignored `sources/original/`. Its printed folios match the converted text's running headers at one page offset. Text in the earlier converted markdown that is absent from this PDF is at the level of formatting noise, so this is the edition that was converted. Converted markdown is at
`../converted/openstax-principles-management.md`; deep reference at
`../../references/openstax-principles-management-deep.md`.

**Role in corpus.** The corpus's general-management axis: the strategic-management cycle, ethics / CSR (seven principles, eight-question stakeholder analysis, FCPA), international management (Hofstede, GLOBE), leadership (LMX, French-Raven, servant), motivation (Maslow, Herzberg, ERG, McClelland, SDT), teams (Tuckman, Follett), organisational design (Mintzberg six structures), control (PDCA, MBO, balanced scorecard). The corpus's only substantive treatment of *tacit knowledge* (Ch 18.6, Nonaka-Takeuchi), load-bearing for any decision involving expertise transfer, succession planning, or knowledge-management design. Paired with `openstax-organizational-behavior-deep.md` (people-at-work focus) and `openstax-introduction-business-deep.md` (functional-area-of-business focus).

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: 22,038 of the PDF's 22,043 text lines of 12 or more characters match line for line, and the other 5 are present with different line breaks; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage and table rows it strung across cells. This restores what pymupdf4llm 0.2.9 dropped: about 9.8% of the longer lines in the chapters the deep reference covers, mostly framed feature boxes (Ethics in Practice, Managing Change, Concept Check, Exploring Managerial Careers, Catching the Entrepreneurial Spirit), sometimes with the body text just before a box, in every chapter.

**Deep reference coverage.** The deep reference was first read from the earlier pymupdf4llm 0.2.9 conversion. On 2026-10-17 every span this re-conversion restored was read in full and added (see its Coverage line), with a single-family Pass I and no cross-family leg.
