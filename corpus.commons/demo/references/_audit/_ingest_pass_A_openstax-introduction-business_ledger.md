# Pass A Ledger — OpenStax, Introduction to Business

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Parallel batch:** Phase 2 of OpenStax 12-book PoC corpus.

## Source metadata

- **Title:** Introduction to Business
- **Publisher:** OpenStax (Rice University)
- **Original publication year:** 2018 (per front-matter Revision Number: IB-2018-000(09/18)-BKB)
- **Publish date:** 2018-09-19 (per the spawn prompt)
- **Edition:** First edition (current OpenStax release)
- **ISBNs:**
  - Print Book ISBN-10: 1-947172-54-9; ISBN-13: 978-1-947172-54-8
  - PDF Version ISBN-10: 1-947172-55-7; ISBN-13: 978-1-947172-55-5
- **URL:** https://openstax.org/details/books/introduction-business
- **Licence:** Creative Commons Attribution 4.0 International (**CC BY 4.0**). Confirmed verbatim in front matter (lines 22-23 of the converted markdown): "Textbook content produced by OpenStax is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0)." This book is the **only** book in the 12-book PoC corpus genuinely licensed CC BY 4.0; the other 11 are CC BY-NC-SA 4.0.
- **Authors (7 senior contributing authors; OpenStax `display_at_top: true` flags lead):**
  - Lead: Lawrence J. Gitman (San Diego State University - Emeritus)
  - Contributors: Carl McDaniel (University of Texas, Arlington); Amit Shah (Frostburg State University); Monique Reece; Linda Koffel (Houston Community College); Bethann Talsma (Davenport University and Grand Rapids Community College); James C. Hyatt (University of The Cumberlands)

## Source format and conversion path

- **PDF:** 744 pages, 53 MB. At `corpus.commons/demo/sources/original/openstax-introduction-business.source.md`.
- **Conversion tool:** pymupdf4llm 0.2.9 (per Phase 2 batch standard).
- **Converted markdown:** 53,932 lines, 1.9 MB. At `corpus.commons/demo/sources/converted/openstax-introduction-business.md`.
- **Page anchors:** not preserved by pymupdf4llm. Citation style: `(Ch N, "Section name")`.

## Coverage scope (Option B — substantive content only)

**Included:** chapter introductions and all numbered substantive sections (1.1 through 17.6); Appendix A (Understanding the Legal and Tax Environment) is included because it grounds the legal-environment framing the chapters reference.

**Excluded** per Option B: per-chapter scaffolding sections —

- `### Key Terms`
- `### Summary of Learning Outcomes`
- `### Preparing for Tomorrow's Workplace Skills`
- `### Ethics Activity`
- `### Working the Net`
- `### Critical Thinking Case`
- `### Hot Links Address Book`

Also excluded: the back-matter `## References` section (line 50151) and `## Index` section (line 52139) as standard back-matter.

The deep ref's frontmatter and source-integrity-notes section both record this exclusion explicitly per the source-integrity rule.

## High-level structure (from converted markdown)

17 substantive chapters plus Appendix A.

| Ch | Chapter title | Section count | Source line (open) |
|---|---|---|---|
| 1 | Understanding Economic Systems and Business | 8 | 907 |
| 2 | Making Ethical Decisions and Managing a Socially Responsible Business | 5 | 4718 |
| 3 | Competing in the Global Marketplace | 9 | 6499 |
| 4 | Forms of Business Ownership | 7 | 9475 |
| 5 | Entrepreneurship: Starting and Managing Your Own Business | 8 | 12420 |
| 6 | Management and Leadership in Today's Organizations | 8 | 15087 |
| 7 | Designing Organizational Structures | 8 | 17707 |
| 8 | Managing Human Resources and Labor Relations | 10 | 20401 |
| 9 | Motivating Employees | 8 | 23745 |
| 10 | Achieving World-Class Operations Management | 8 | 26217 |
| 11 | Creating Products and Pricing Strategies to Meet Customers' Needs | 10 | 29336 |
| 12 | Distributing and Promoting Products and Services | 11 | 33094 |
| 13 | Using Technology to Manage Information | 6 | 35985 |
| 14 | Using Financial Information and Accounting | 8 | 38729 |
| 15 | Understanding Money and Financial Institutions | 6 | 41689 |
| 16 | Understanding Financial Management and Securities Markets | 8 | 43945 |
| 17 | Your Career in Business | 6 | 47068 |
| App A | Understanding the Legal and Tax Environment | 3 | 49107 |

## Front-matter framing

The Preface (lines 290-906) introduces the survey textbook as a freshman/sophomore-level overview, contributed by seven specialists in different disciplines. The book speaks with multiple authorial voices unified by editorial process. The chapter authorship is distributed: Reece's marketing background shows in Chs 11-12; Gitman's finance expertise grounds Chs 14-16; Shah likely owns the operations and management chapters; etc.

The book's organising premise is that effective business activity requires integrating perspectives across functional areas (economics, ethics, global trade, ownership forms, entrepreneurship, management, organisational design, HR, motivation, operations, marketing, distribution, technology, accounting, finance, securities markets, careers, and legal/tax environment). Unlike a deep specialist text in any single area, the book aims to give a non-specialist reader "the right" basic vocabulary in each functional area to participate in business conversations and to choose a major.

## Citation style decision

`(Ch N, "Section name")` — pymupdf4llm did not preserve page anchors. Recorded in the deep ref's source-integrity-notes block. Appendix A is cited as `(App A, "Section name")`.

## Pre-flight gates

1. **Completeness.** Confirmed: 17 chapters + Appendix A present, each with the full Introduction + numbered sections + standard scaffolding sections. No mid-paragraph truncation. TOC structure (chapter heading + numbered sections + standard exclusion blocks) holds across all 17 chapters.
2. **Citation style.** No page anchors in converted markdown; cite as `(Ch N, "Section name")`.
3. **Model identity.** Confirmed Opus 4.7 (claude-opus-4-7[1m], 1M context) running this ingestion.

## Outputs anticipated

- `corpus.commons/demo/references/openstax-introduction-business-deep.md`
- `corpus.commons/demo/references/openstax-introduction-business.md`
- `prompts/applications/decision-making/openstax-introduction-business-decision-making.md` (pending Pass G.0)
- `prompts/applications/stakeholder-engagement/openstax-introduction-business-stakeholder-engagement.md` (pending Pass G.0)
- Pass H verification log + Pass I source-only audit + this Pass A ledger.
- Staging files: SEARCH-INDEX entries, DECISION-MAKING-INDEX entries, STAKEHOLDER-ENGAGEMENT-INDEX entries, IMAGE-INDEX entries.
