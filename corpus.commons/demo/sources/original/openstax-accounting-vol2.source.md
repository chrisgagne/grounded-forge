---
title: Principles of Accounting, Volume 2 — Managerial Accounting
author: OpenStax (Mitchell Franklin, Patty Graybeal, Dixon Cooper et al.)
publisher: Rice University
publish_year: 2019
isbn: 978-1-947172-59-3
url: https://openstax.org/details/books/principles-managerial-accounting
scope: open-nc
licence: CC BY-NC-SA 4.0
ingested: 2026-05-05
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: 233b94100de54a5ed9fd6b9cf419a2b165aa2b5975ae06c9ac7bcba556a7bc26
---

# Source: Principles of Accounting, Vol 2 — Managerial Accounting (OpenStax)

PDF not shipped (download free from the URL above). The SHA256 above is of `principles-managerial-accounting_-_WEB.pdf` (677 pages, 89,822,467 bytes), fetched from assets.openstax.org on 2026-10-16 and held in the gitignored `sources/original/`. Its printed folios match the converted text's running headers at one page offset. Text in the earlier converted markdown that is absent from this PDF is at the level of formatting noise, so this is the edition that was converted. Converted markdown is at
`../converted/openstax-accounting-vol2.md`; deep reference at
`../../references/openstax-accounting-vol2-deep.md`.

**Role in corpus.** The corpus's managerial-accounting axis: cost classification (variable / fixed / relevant / sunk / opportunity), job-order and process costing, CVP, contribution margin, master and flexible budgets, standard costs and variances, responsibility accounting, relevant-cost analysis, capital budgeting (NPV / IRR / payback), the five-step Theory of Constraints, the four-perspective balanced scorecard, GRI / SASB / IIRC sustainability reporting. Paired with `openstax-accounting-vol1-deep.md` for the financial-vs-managerial split. Treats cost as decision-relative rather than as an inherent attribute: the load-bearing distinction the rest of the volume builds on.

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: 20,117 of the PDF's 20,202 text lines of 12 or more characters match line for line, and the other 85, mostly table rows, have all their words on the same page with different line breaks; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage and table rows it strung across cells. This restores what pymupdf4llm 0.2.9 dropped: about 4.2% of the longer lines in the chapters the deep reference covers, mostly framed feature boxes (Link to Learning, Concepts in Practice, Your Turn, Think It Through, Ethical Considerations), sometimes with the body text just before a box, in every chapter.

**Deep reference coverage.** The deep reference was first read from the earlier pymupdf4llm 0.2.9 conversion. On 2026-10-17 every span this re-conversion restored was read in full and added (see its Coverage line), with a single-family Pass I and no cross-family leg.
