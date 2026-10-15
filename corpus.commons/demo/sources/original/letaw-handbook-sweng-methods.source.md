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
converted_via: pymupdf4llm 0.2.9
checksum_sha256: a1abd674f74bcea0bfd2717ef38365180ba2a9b9798d1055edf6381c6fc14673
---

# Source: Handbook of Software Engineering Methods (Lara Letaw)

Second edition (2024) of an Oregon State University open textbook covering eight
software-engineering methods: Agile/Scrum, project management and teamwork,
requirements, UML class and sequence diagrams, monolith versus microservice
architectures, paper prototyping, Inclusivity Heuristics, and code smells and
refactoring. PDF was downloaded from the canonical URL above (Pressbooks "Digital PDF", 115
pages; the SHA256 above was checked against it on 2026-10-16) and converted to
markdown with pymupdf4llm 0.2.9 (preserving section structure but not page
anchors). PDF binary is not redistributed (defensively gitignored); the converted
markdown lives at `../converted/letaw-handbook-sweng-methods.md`. Deep reference
at `../../references/letaw-handbook-sweng-methods-deep.md`. The source's editor
of record is Ashleigh McKown; the work is published by the OSU OER Unit.

**Known gaps, not repaired.** Compared line by line with pdftotext of the original on 2026-10-16, the converted text lacks 122 of the PDF's 1,857 longer text lines (6.6%); 101 (5.4%) once reference-list URLs and three ligature-damaged lines ("Defning", "hufpost") are set aside. pymupdf4llm 0.2.9 dropped the text of framed callout and example boxes: the Agile Manifesto values (PDF p. 18), the CHAOS report findings (p. 17), the example use case and user stories (pp. 46–47), the acceptance-criteria examples (p. 49), the Inclusivity Heuristics design recommendations (pp. 84–90) and the coding-style tip boxes (pp. 95–100). Example: PDF p. 18 (printed p. 10), the Agile Manifesto box ("We are uncovering better ways of developing software…" and its four values), checked against the page render. A re-conversion is needed before this text can be called complete.
