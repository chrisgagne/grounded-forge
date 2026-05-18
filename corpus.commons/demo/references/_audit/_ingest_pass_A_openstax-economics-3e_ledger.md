# Pass A Ledger — OpenStax, Principles of Economics 3e

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Phase 2 parallel batch:** Book of 11 (parallel ingestion).

## Source metadata

- **Title:** Principles of Economics 3e
- **Publisher:** OpenStax (Rice University), with print partnership via Kendall Hunt Publishing.
- **First published:** 2022-12-14. ©2026 Rice University reprint copyright in front matter.
- **Edition:** Third edition.
- **ISBNs:**
  - Color paperback: 978-1-711471-45-7
  - B&W paperback: 978-1-711471-46-4
  - Digital: 978-1-951693-63-3
- **URL:** https://openstax.org/details/books/principles-economics-3e
- **Licence:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (**CC BY-NC-SA 4.0**). Confirmed verbatim at source lines 19-20: "Textbook content produced by OpenStax is licensed under a Creative Commons Attribution Non-Commercial ShareAlike 4.0 International License (CC BY-NC-SA 4.0)" and again at lines 798-799.
- **Authors (10 contributors; lead Steven A. Greenlaw, University of Mary Washington):**
  - Lead: Steven A. Greenlaw, University of Mary Washington
  - Contributors: David Shapiro (Pennsylvania State University); Daniel MacDonald (California State University, San Bernardino); Eric Dodge (Hanover College); Cynthia Gamez (University of Texas at El Paso); Andres Jauregui (Columbus State University); Diane Keenan (Cerritos College); Amyaz Moledina (The College of Wooster); Craig Richardson (Winston-Salem State University); Ralph Sonenshine (American University)

## Source format and conversion path

- **PDF:** 995 pages, ~47 MB. At `corpus.commons/demo/sources/original/openstax-economics-3e.source.md`.
- **Conversion tool:** pymupdf4llm 0.2.9.
- **Converted markdown:** 57,917 lines, ~2.97 MB. At `corpus.commons/demo/sources/converted/openstax-economics-3e.md`.
- **Page anchors:** not preserved by pymupdf4llm. Citation style: `(Ch N, "Section name")`.

## Coverage scope (Option B — substantive content only)

**Included:**
- Chapter introduction (`###### **Introduction**`-style) including the Bring-It-Home opening narrative.
- All numbered substantive sections (`**N.M Section name**`).
- Appendices A-E (mathematical, indifference curves, present discounted value, expenditure-output, open-market operations) — included as substantive supporting content.

**Excluded per chapter (scaffolding):**
- `**Key Terms**`
- `**Self-Check Questions**`
- `**Review Questions**`
- `**Critical Thinking Questions**`
- `**Problems**` (where present)
- Chapter Summary (where formatted as a numbered chapter-summary section after sections close)

**Excluded back-matter:**
- ANSWER KEY (line 52101)
- REFERENCES (line 54778)
- INDEX (line 56762)

The deep ref's frontmatter and source-integrity-notes section both record this exclusion explicitly per the source-integrity rule.

## High-level structure (from converted markdown)

34 substantive chapters plus Appendices A-E. Both microeconomic foundations (Chs 1-18) and macroeconomic theory (Chs 19-34) are treated.

| Ch | Chapter title | Source line (open) |
|---|---|---|
| 1 | Welcome to Economics! | 1262 |
| 2 | Choice in a World of Scarcity | 2346 |
| 3 | Demand and Supply | 3443 |
| 4 | Labor and Financial Markets | 5595 |
| 5 | Elasticity | 6896 |
| 6 | Consumer Choices | 8200 |
| 7 | Production, Costs, and Industry Structure | 9342 |
| 8 | Perfect Competition | 11170 |
| 9 | Monopoly | 12658 |
| 10 | Monopolistic Competition and Oligopoly | 13867 |
| 11 | Monopoly and Antitrust Policy | 15052 |
| 12 | Environmental Protection and Negative Externalities | 16308 |
| 13 | Positive Externalities and Public Goods | 17854 |
| 14 | Labor Markets and Income | 18978 |
| 15 | Poverty and Economic Inequality | 20902 |
| 16 | Information, Risk, and Insurance | 22472 |
| 17 | Financial Markets | 23732 |
| 18 | Public Economy | 25372 |
| 19 | The Macroeconomic Perspective | 26275 |
| 20 | Economic Growth | 27848 |
| 21 | Unemployment | 29318 |
| 22 | Inflation | 30922 |
| 23 | The International Trade and Capital Flows | 32464 |
| 24 | The Aggregate Demand/Aggregate Supply Model | 33949 |
| 25 | The Keynesian Perspective | 35594 |
| 26 | The Neoclassical Perspective | 36557 |
| 27 | Money and Banking | 37602 |
| 28 | Monetary Policy and Bank Regulation | 38806 |
| 29 | Exchange Rates and International Capital Flows | 40545 |
| 30 | Government Budgets and Fiscal Policy | 42111 |
| 31 | The Impacts of Government Borrowing | 43683 |
| 32 | Macroeconomic Policy Around the World | 44740 |
| 33 | International Trade | 46076 |
| 34 | Globalization and Protectionism | 47407 |

Appendix A (The Use of Mathematics, line 49257), Appendix B (Indifference Curves, line 50006), Appendix C (Present Discounted Value, line 50695), Appendix D (Expenditure-Output Model, line 50860), and Appendix E (Open Market Operations and Balance Sheets, line 52061) are included as substantive supporting content. Answer Key (52101), References (54778), Index (56762) are excluded as back-matter.

## Citation style decision

`(Ch N, "Section name")` — pymupdf4llm did not preserve page anchors. Section names from the converted markdown are used. Where chapter names span multiple pdf-extracted lines (e.g., chapters 7, 10, 11, 12, 13, 23, 24, 28, 29, 30, 31, 32 have multi-line titles in the converted markdown), the canonical chapter title from the contents listing (lines 183-740) is used.

## Pre-flight gates

1. **Completeness.** Confirmed: 34 chapters present, each with the full Introduction + numbered sections + scaffolding sections, plus 5 appendices and back-matter. No mid-paragraph truncation visible. TOC structure (chapter heading + numbered section bold + standard exclusion blocks) holds across all 34 chapters.
2. **Citation style.** No page anchors in converted markdown; cite as `(Ch N, "Section name")`.
3. **Model identity.** Confirmed Opus 4.7 (claude-opus-4-7[1m], 1M context) running this ingestion.

## Outputs anticipated

- `corpus.commons/demo/references/openstax-economics-3e-deep.md`
- `corpus.commons/demo/references/openstax-economics-3e.md`
- `prompts/applications/decision-making/openstax-economics-3e-decision-making.md` (pending Pass G.0)
- `prompts/applications/stakeholder-engagement/openstax-economics-3e-stakeholder-engagement.md` (pending Pass G.0; weak-applicability watch flagged)
- Pass H verification log + Pass I source-only audit + this Pass A ledger.
- Staging files for SEARCH-INDEX, DECISION-MAKING-INDEX, STAKEHOLDER-ENGAGEMENT-INDEX, IMAGE-INDEX (parent agent merges).

## Pass G.0 preliminary read

- **Decision-making.** Strong applicability anticipated. Economics is fundamentally about choice under scarcity (Ch 1 definition: "the study of how humans make decisions in the face of scarcity"). The book provides foundational decision-theoretic concepts: opportunity cost, marginal analysis, budget constraints, production possibilities frontier (Chs 1-2), consumer choice and utility maximisation (Ch 6), firm cost curves and profit maximisation (Ch 7-10), expected value and risk (Ch 16), and government decision-making frameworks (Ch 18). High likelihood of clear-yes after deep read.
- **Stakeholder-engagement.** Borderline. Most economics framing is at the system / market level rather than interpersonal. However, several chapters carry stakeholder content: labour markets and unionisation (Ch 14), positive externalities and public goods (Ch 13), negative externalities and environmental policy (Ch 12), poverty and inequality (Ch 15), public economy and voting (Ch 18), and globalization debates (Ch 34). Final Pass G.0 decision deferred until deep read confirms how interpersonal/stakeholder-engagement content is actually framed by the source.
