---
title: Handbook of Software Engineering Methods
author: Lara Letaw
publisher: Oregon State University, Open Educational Resources (OER) Unit
publish_year: 2024
isbn: not stated in source front-matter
url: https://open.oregonstate.education/setextbook/
scope: open-nc
licence: CC BY-NC 4.0
ingested: 2026-05-13
original_format: pdf
converted_via: 'PyMuPDF 1.28.2 text blocks in content-stream order (page.get_text("blocks", sort=False)), one block per paragraph, pages split by form feed'
checksum_sha256: a1abd674f74bcea0bfd2717ef38365180ba2a9b9798d1055edf6381c6fc14673
---

# Source: Handbook of Software Engineering Methods (Lara Letaw)

Second edition (2024) of an Oregon State University open textbook covering eight
software-engineering methods: Agile/Scrum, project management and teamwork,
requirements, UML class and sequence diagrams, monolith versus microservice
architectures, paper prototyping, Inclusivity Heuristics, and code smells and
refactoring. PDF was downloaded from the canonical URL above (Pressbooks "Digital PDF", 115
pages; the SHA256 above was checked against it on 2026-10-16) . PDF binary is not redistributed (defensively gitignored); the converted
markdown lives at `../converted/letaw-handbook-sweng-methods.md`. Deep reference
at `../../references/letaw-handbook-sweng-methods-deep.md`. The source's editor
of record is Ashleigh McKown; the work is published by the OSU OER Unit.

**Conversion.** Re-converted on 2026-10-16 with PyMuPDF 1.28.2: each page's text blocks in content-stream order (`page.get_text("blocks", sort=False)`), one block per paragraph, trailing spaces removed, pages separated by form feeds, nothing added or edited. Each page's folio and running header come first in its text. Checked against pdftotext of the original: 2,460 of the PDF's 2,464 text lines of 12 or more characters match line for line, and the other four are present with different line breaks; a page-by-page word comparison finds no word pdftotext reads that the new text lacks, and every line of the earlier pymupdf4llm conversion is present apart from its ligature damage ("Defning", "hufpost") and soft hyphens it left inside bold markers. This restores what pymupdf4llm 0.2.9 dropped, the text of framed callout and example boxes: the Agile Manifesto values (PDF p. 18), the CHAOS report findings (p. 17), the example use case and user stories (pp. 46–47), the acceptance-criteria examples (p. 49), the Inclusivity Heuristics design recommendations (pp. 84–90) and the coding-style tip boxes (pp. 95–100).

**Deep reference coverage.** The deep reference was read from the earlier pymupdf4llm 0.2.9 conversion, so it stays PARTIAL until Passes C–E cover the restored boxes (see its Coverage line).
