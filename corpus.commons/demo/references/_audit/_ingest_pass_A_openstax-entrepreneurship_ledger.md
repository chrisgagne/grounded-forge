# Pass A Ledger — OpenStax, Entrepreneurship

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Run:** Phase 2 batch ingestion (one of 11 books).

## Source metadata

- **Title:** Entrepreneurship
- **Publisher:** OpenStax (Rice University), with print partnership via Kendall Hunt Publishing.
- **Original publication year:** 2020. Print copyright in front matter dated 2026.
- **ISBNs:**
  - B&W paperback: 978-1-975076-34-4
  - Digital: 978-1-947172-70-8
- **URL:** https://openstax.org/details/books/entrepreneurship
- **Licence:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (**CC BY-NC-SA 4.0**). Confirmed in front matter (lines 17-22 of the converted markdown): "Textbook content produced by OpenStax is licensed under a Creative Commons Attribution Non-Commercial ShareAlike 4.0 International License (CC BY-NC-SA 4.0)".
- **Senior contributing authors:**
  - Michael Laverty, Colorado State University Global
  - Chris Littel, North Carolina State University
- **Contributing authors (19):** Chandra D. Arthur (Cuyahoga Community College); Martin S. Bressler (Southeastern Oklahoma State University); Stephen M. Byars (USC Marshall School of Business); Bryan Coleman (Assumption College); Mehran C. Ferdowsian (Wilkes University); Geoffrey Graybeal (Georgia State University); Wm. David Hawkins (Northwestern Oklahoma State University); Jennifer Herrera (Capella University); Lyzona Marshall (Seton Hill University); Angela Mitchell (Wilmington College); William Nantz (Houston Community College); Denisse Olivas (University of Texas at El Paso); Karli Peterson (Colorado State University Global); Mark A. Poepsel (Southern Illinois University Edwardsville); Kevin Raiford (College of Southern Nevada); Jeffrey J. Sabolish (University of Michigan-Flint); Sally Sledge (Norfolk State University); Kurt Stanberry (University of Houston-Downtown).

## Source format and conversion path

- **PDF:** 631 pages, 124 MB. At `corpus.commons/demo/sources/original/openstax-entrepreneurship.source.md`.
- **Conversion tool:** pymupdf4llm 0.2.9.
- **Converted markdown:** 36,579 lines, 1.9 MB. At `corpus.commons/demo/sources/converted/openstax-entrepreneurship.md`.
- **Page anchors:** not preserved by pymupdf4llm. Citation style: `(Ch N, "Section name")`.

## Coverage scope (Option B — substantive content only)

Per global decision Q2, the deep ref covers:

**Included:** chapter introduction (`### **Introduction**`), all numbered substantive sections (`### **N.M Section name**`), and the chapter-overview text under the chapter title before sections start.

**Excluded:** per-chapter pedagogical scaffolding —
- `### **Key Terms**`
- `### **Summary**`
- `### **Review Questions**`
- `### **Discussion Questions**`
- `### **Case Questions**`
- `### **Suggested Resources**`

Appendix A ("Suggested Resources") is excluded as a back-matter reading list, not substantive content. The Index is excluded as standard back-matter.

The deep ref's frontmatter and source-integrity-notes section both record this exclusion explicitly per the source-integrity rule.

## High-level structure (from converted markdown)

15 substantive chapters. Section counts and source-line openings:

| Ch | Chapter title | Section count | Source line (open) |
|---|---|---|---|
| 1 | The Entrepreneurial Perspective | 3 | 697 |
| 2 | The Entrepreneurial Journey and Pathways | 4 | 2366 |
| 3 | The Ethical and Social Responsibilities of Entrepreneurs | 3 | 4932 |
| 4 | Creativity, Innovation, and Invention | 3 | 7670 |
| 5 | Identifying Entrepreneurial Opportunity | 3 | 9277 |
| 6 | Problem Solving and Need Recognition Techniques | 4 | 10889 |
| 7 | Telling Your Entrepreneurial Story and Pitching the Idea | 5 | 12577 |
| 8 | Entrepreneurial Marketing and Sales | 6 | 14963 |
| 9 | Entrepreneurial Finance and Accounting | 4 | 18128 |
| 10 | Launch for Growth to Success | 5 | 20049 |
| 11 | Business Model and Plan | 4 | 22571 |
| 12 | Building Networks and Foundations | 3 | 25275 |
| 13 | Business Structure Options: Legal, Tax, and Risk Issues | 7 | 28154 |
| 14 | Fundamentals of Resource Planning | 3 | 30218 |
| 15 | Next Steps | 5 | 32521 |

Appendix A (Suggested Resources, line 34176) and Index (line 34629) are excluded as back-matter.

## Front-matter framing

The Preface (lines 315-695) declares the book is "designed to meet the course needs of a one-semester undergraduate course on the subject" and that it "will cover the key principles of entrepreneurship alongside the concepts, strategies, and tools needed to succeed as a small business owner, franchisee, founder, or other entrepreneurial professional" (Preface, "About Entrepreneurship", lines 374-377).

The book is organised around the entrepreneurial journey: perspective and mindset (Ch 1), pathways and life cycle (Ch 2), ethics and social responsibility (Ch 3), creativity through opportunity recognition (Ch 4-6), pitching and marketing (Ch 7-8), finance and launch (Ch 9-10), business model and planning (Ch 11), networks and structure (Ch 12-13), resource planning (Ch 14), and next steps after harvest (Ch 15). Multiple-author authorship — the Preface acknowledges 19 contributing authors plus 2 senior contributors, with chapters reflecting different authorial voices integrated into a single text.

## Pre-flight gates

- **Completeness:** converted markdown opens with title page, preface, and proceeds through all 15 chapters plus appendix and index. No truncation observed.
- **Citation style:** `(Ch N, "Section name")` chosen because pymupdf4llm does not preserve PDF page anchors.
- **Model identity:** confirmed Opus 4.7 per spawn-prompt Step 0.
- **Licence:** CC BY-NC-SA 4.0 confirmed verbatim in front matter.
