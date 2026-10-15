---
title: Principles of Finance
author: OpenStax (Julie Dahlquist, Rainford Knight et al.)
publisher: Rice University
publish_year: 2022
isbn: 978-1-951693-54-1
url: https://openstax.org/details/books/principles-finance
scope: open-nc
licence: CC BY-NC-SA 4.0
ingested: 2026-05-05
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: d9dc9bc96cb6e3128a38aabf00609cc72d5e7721565fa3b5a672a41352f4a22c
---

# Source: Principles of Finance (OpenStax)

PDF not shipped (download free from the URL above). The SHA256 above is of `principles-finance_-_WEB.pdf` (629 pages, 31,916,668 bytes), fetched from assets.openstax.org on 2026-10-16 and held in the gitignored `sources/original/`. Its printed folios match the converted text's running headers at one page offset. Text in the earlier converted markdown that is absent from this PDF is at the level of formatting noise, so this is the edition that was converted. Converted markdown is at
`../converted/openstax-principles-finance.md`; deep reference at
`../../references/openstax-principles-finance-deep.md`.

**Role in corpus.** The corpus's time-value-of-money axis: present and future value, annuities and perpetuities, NPV / IRR / MIRR / PI / payback, the cost-of-capital toolkit (WACC, Modigliani-Miller), CAPM and the security-market line, systematic vs unsystematic risk, the dividend-discount model, working-capital and cash-conversion-cycle, short-term financing (commercial paper, line of credit, factoring). The corpus's only treatment of the TVM apparatus, load-bearing for any deliberation involving capital allocation, project ranking, or cost-of-capital arguments. Paired with `openstax-accounting-vol2-deep.md` for the managerial-vs-financial-modelling distinction; finance ranks projects, accounting accounts for them.

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: 19,853 of the PDF's 19,973 text lines of 12 or more characters match line for line, and the other 120, mostly table and equation rows, have all their words on the same page with different line breaks; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage and table rows it strung across cells. This restores what pymupdf4llm 0.2.9 dropped: about 7.7% of the longer lines in the chapters the deep reference covers, mostly framed feature boxes (Link to Learning, Think It Through, Concepts in Practice), sometimes with the body text just before a box, in every chapter.

**Deep reference coverage.** The deep reference was read from the earlier pymupdf4llm 0.2.9 conversion, so it stays PARTIAL until Passes C–E cover the restored material (see its Coverage line).
