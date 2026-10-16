---
title: Psychology 2e
author: OpenStax (Rose M. Spielman, William J. Jenkins, Marilyn D. Lovett et al.)
publisher: Rice University
publish_year: 2020
isbn: 978-1-951693-23-7
url: https://openstax.org/details/books/psychology-2e
scope: open-nc
licence: CC BY-NC-SA 4.0
ingested: 2026-05-05
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: 2f08113c78127bc684922ad6a819db22bd4705ce9fcf28a07f36a2041b1474e2
---

# Source: Psychology 2e (OpenStax)

PDF not shipped (download free from the URL above). The SHA256 above is of `Psychology2e_WEB.pdf` (755 pages, 57,739,919 bytes), fetched from assets.openstax.org on 2026-10-16 and held in the gitignored `sources/original/`. Its printed folios match the converted text's running headers at one page offset. Text in the earlier converted markdown that is absent from this PDF is at the level of formatting noise, so this is the edition that was converted. Converted markdown is at
`../converted/openstax-psychology-2e.md`; deep reference at
`../../references/openstax-psychology-2e-deep.md`.

**Role in corpus.** The corpus's applied-cognition axis: biopsychology, sensation and perception, learning (classical and operant conditioning, observational), cognition (concepts, prototypes, problem-solving, language), memory (Atkinson-Shiffrin, encoding, retrieval, forgetting), developmental (Piaget, Erikson, Kohlberg, Bronfenbrenner, Vygotsky, Baumrind), motivation (drive-reduction, Maslow, SDT, the overjustification effect), emotion (James-Lange, Cannon-Bard, Schachter-Singer), personality (Big Five / OCEAN), social psychology (Asch, Milgram, attribution, persuasion), industrial-organisational, stress and health. The corpus's general cognitive grounding, narrow in applicability to business-task work via the cognitive-load and dual-process threads. **Chapters 15–16 (therapy / clinical) deliberately excluded from the concept index**: the corpus uses this source for general cognitive grounding, not for clinical recommendation; deliberation that turns on therapy or diagnosis should reach for primary clinical sources, not this volume.

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: 26,392 of the PDF's 26,408 text lines of 12 or more characters match line for line, and the other 16 are present with different line breaks; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage and table rows it strung across cells. This restores what pymupdf4llm 0.2.9 dropped: about 1.1% of the longer lines in the chapters the deep reference covers, mostly framed feature boxes (Dig Deeper, Everyday Connection, Link to Learning), sometimes with the body text just before a box, in Ch 1, 2, 4 and 6–15.

**Deep reference coverage.** The deep reference was first read from the earlier pymupdf4llm 0.2.9 conversion. On 2026-10-17 every span this re-conversion restored was read in full and added (see its Coverage line), with a single-family Pass I and no cross-family leg.
