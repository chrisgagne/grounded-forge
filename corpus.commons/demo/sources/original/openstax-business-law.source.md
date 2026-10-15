---
title: Business Law I Essentials
author: OpenStax (Mirande Valbrune Esq., Renee De Assis, Suzanne Cardell et al.)
publisher: Rice University
publish_year: 2019
isbn: 978-1-947172-78-4
url: https://openstax.org/details/books/business-law-i-essentials
scope: open-nc
licence: CC BY-NC-SA 4.0
ingested: 2026-05-05
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: c56eef123fd5699ef7fac923394687c34cb46f349bad0b0f5f59b2106bc303bc
---

# Source: Business Law I Essentials (OpenStax)

PDF not shipped (download free from the URL above). The SHA256 above is of `business-law-i-essentials-WEB.pdf` (165 pages, 12,906,008 bytes), fetched from assets.openstax.org on 2026-10-16 and held in the gitignored `sources/original/`. Its printed folios match the converted text's running headers at one page offset. Text in the earlier converted markdown that is absent from this PDF is at the level of formatting noise, so this is the edition that was converted. Converted markdown is at
`../converted/openstax-business-law.md`; deep reference at
`../../references/openstax-business-law-deep.md`.

**Role in corpus.** The corpus's legal-framework axis: the four-tier ADR framework (negotiation / mediation / arbitration / litigation), TKI five negotiation modes, contract formation and remedies, UCC Article 2 sales contracts, tort doctrines (negligence / strict liability / product liability), IP (Lanham, patent, copyright, trade secret), employment law (Title VII, ADA, FMLA, at-will doctrine), consumer protection (FTC Act, COPPA, GDPR, CCPA), business-organisations primer, international-law primitives. The corpus's only treatment of legal-form primitives, load-bearing for any decision involving compliance, contracting, or jurisdictional concerns. Paired with `openstax-business-ethics-deep.md` for the law-ethics boundary work; the legal layer disciplines the ethics arguments rather than substituting for them.

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: all 4,720 of the PDF's text lines of 12 or more characters match line for line; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage and table rows it strung across cells. This restores what pymupdf4llm 0.2.9 dropped: about 0.7% of the longer lines in the chapters the deep reference covers, almost all table cells, in Ch 4, 6, 8 and 9 (e.g. Table 8.3, which the earlier conversion also damaged by dropping "fi" ligatures).

**Deep reference coverage.** The deep reference was read from the earlier pymupdf4llm 0.2.9 conversion, so it stays PARTIAL until Passes C–E cover the restored material (see its Coverage line).
