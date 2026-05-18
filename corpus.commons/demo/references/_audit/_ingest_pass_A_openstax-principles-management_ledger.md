# Pass A Ledger — OpenStax, Principles of Management

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Parallel-batch run:** Phase 2 ingestion, Book 11 of 12 in the OpenStax PoC corpus.

## Source metadata

- **Title:** Principles of Management
- **Publisher:** OpenStax (Rice University), 2019.
- **First published:** 2019-03-20.
- **Edition:** First edition.
- **ISBNs (front matter, lines 54-56 of source markdown):**
  - Color paperback: 978-0-9986257-6-8
  - B&W paperback: 978-1-59399-876-9
  - Digital: 978-0-9986257-7-5
- **URL:** https://openstax.org/details/books/principles-management
- **Licence:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (**CC BY-NC-SA 4.0**). Confirmed verbatim in front matter at lines 14-15 ("©2026 Rice University. Textbook content produced by OpenStax is licensed under a Creative Commons Attribution Non-Commercial ShareAlike 4.0 International License (CC BY-NC-SA 4.0)") and at lines 386-389 ("Principles of Management is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY NC-SA) license").
- **Lead author (per spawn prompt and front matter):** David S. Bright (Wright State University).
- **Contributing authors (15 total per front matter, lines 601-617):** Anastasia H. Cortes (Virginia Tech University); Donald G. Gardner (University of Colorado-Colorado Springs); Eva Hartmann (University of Richmond); Jason Lambert (Texas Woman's University); Laura M. Leduc (James Madison University); Joy Leopold (Webster University); Jeffrey Muldoon (Emporia State University); James S. O'Rourke (University of Notre Dame); K. Praveen Parboteeah (University of Wisconsin-Whitewater); Jon L. Pierce (University of Minnesota-Duluth); Monique Reece; Amit Shah (Frostburg State University); Siri Terjesen (American University); Joseph Weiss (Bentley University); Margaret A. White (Oklahoma State University).

## Source format and conversion path

- **PDF:** 605 pages (per spawn prompt). At `corpus.commons/demo/sources/original/openstax-principles-management.source.md`.
- **Conversion tool:** pymupdf4llm 0.2.9 (per Phase 2 batch standard).
- **Converted markdown:** 31,465 lines. At `corpus.commons/demo/sources/converted/openstax-principles-management.md`.
- **Page anchors:** not preserved by pymupdf4llm. Citation style: `(Ch N, "Section name")`.

## Coverage scope (Option B — substantive content only)

**Included:** chapter introductions (`### **Introduction**`), all numbered substantive sections (`### **N.M Section name**`), and the chapter-overview text under chapter titles before sections start.

**Excluded:** per-chapter pedagogical scaffolding, including:

- `### **Key Terms**`
- `### **Summary of Learning Outcomes**`
- `### **Chapter Review Questions**`
- `### **Management Skills Application Exercises**`
- `### **Managerial Decision Exercises**`
- `### **Critical Thinking Case**`

The deep ref's frontmatter and source-integrity-notes section both record this exclusion explicitly per the source-integrity rule.

## High-level structure (from converted markdown)

18 substantive chapters; no separate appendix.

| Ch | Chapter title | Section count | Source line (open) |
|---|---|---|---|
| 1 | Managing and Performing | 3 | 664 |
| 2 | Managerial Decision-Making | 6 | 1293 |
| 3 | The History of Management | 7 | 2746 |
| 4 | External and Internal Organizational Environments and Corporate Culture | 6 | 4109 |
| 5 | Ethics, Corporate Responsibility, and Sustainability | 8 | 5578 |
| 6 | International Management | 7 | 7389 |
| 7 | Entrepreneurship | 8 | 9700 |
| 8 | Strategic Analysis: Understanding a Firm's Competitive Environment | 7 | 11461 |
| 9 | The Strategic Management Process: Achieving and Sustaining Competitive Advantage | 6 | 12820 |
| 10 | Organizational Structure and Change | 3 | 13973 |
| 11 | Human Resource Management | 6 | 15540 |
| 12 | Diversity in Organizations | 7 | 17037 |
| 13 | Leadership | 9 | 18858 |
| 14 | Work Motivation for Performance | 4 | 20869 |
| 15 | Managing Teams | 6 | 23216 |
| 16 | Managerial Communication | 5 | 24402 |
| 17 | Organizational Planning and Controlling | 8 | 25645 |
| 18 | Management of Technology and Innovation | 7 | 27719 |

## Front-matter framing

The Preface (lines 369-662) describes the book's design intent:

- "Principles of Management is designed to meet the scope and sequence requirements of the introductory course on management. This is a traditional approach to management using the leading, planning, organizing, and controlling approach" (Preface, "About Principles of Management", line 429-430).
- The book's two main themes: (1) "What are the variables that affect how, when, where, and why managers perform their jobs?" and (2) "What theories and techniques are used by successful managers at a variety of organizational levels to achieve and exceed objectives effectively and efficiently throughout their careers?" (line 437-439).
- Authorship is distributed: "an additional benefit of this text is that specialists in a variety of areas have authored individual chapters" (line 442-443).
- Pedagogy: gender alternation across chapters (line 444-446), Exploring Managerial Careers profiles, Concept Checks, and applied features (Ethics in Practice, Managing Change, Catching the Entrepreneurial Spirit, Managerial Leadership, Sustainability and Responsible Management).

## Citation style decision

`(Ch N, "Section name")` — pymupdf4llm did not preserve page anchors. Recorded in deep ref source-integrity-notes block.

## Pre-flight gates

1. **Completeness.** Confirmed: 18 chapters present, each with the full Introduction + numbered sections + standard scaffolding sections. No mid-paragraph truncation. TOC structure (chapter heading + numbered sections + standard exclusion blocks) holds across all 18 chapters.
2. **Citation style.** No page anchors in converted markdown; cite as `(Ch N, "Section name")`.
3. **Model identity.** Confirmed Opus 4.7 (claude-opus-4-7[1m], 1M context) running this ingestion.

## Outputs anticipated

- `corpus.commons/demo/references/openstax-principles-management-deep.md`
- `corpus.commons/demo/references/openstax-principles-management.md`
- `prompts/applications/decision-making/openstax-principles-management-decision-making.md` (pending Pass G.0)
- `prompts/applications/stakeholder-engagement/openstax-principles-management-stakeholder-engagement.md` (pending Pass G.0)
- Pass H verification log + Pass I source-only audit + this Pass A ledger.
- Staging files for SEARCH-INDEX, DECISION-MAKING-INDEX, STAKEHOLDER-ENGAGEMENT-INDEX merges.
- Image index staging entries for substantive subset of 186 extracted images.

## Pre-Pass-B notes on substantive content (initial scan)

Chapter 2 (Managerial Decision-Making) is the most concentrated decision-making chapter in the OpenStax management corpus, mirroring the OpenStax Organizational Behavior Ch 6 framing closely (reflective vs reactive systems, programmed vs non-programmed decisions, six-step process, six barriers, group decision-making with groupthink and devil's advocate). It cites the same Darlow & Sloman neuropsychology research and the same Rest four-component ethical decision-making model. Several chapters cross-reference OB content closely (Ch 4 on environments and culture mirrors OB Ch 15; Ch 10 on structure and change mirrors OB Ch 16; Ch 11 on HR mirrors OB Ch 17; Ch 12 on diversity mirrors OB Ch 5; Ch 13 on leadership mirrors OB Ch 12; Ch 14 on motivation mirrors OB Ch 7; Ch 15 on teams mirrors OB Ch 10; Ch 16 on communication mirrors OB Ch 11). Distinct content includes Ch 3 (history of management — Sumer, Hammurabi, Renaissance, Industrial Revolution, Taylor, Fayol, Weber, Mayo, Barnard, Follett, Woodward); Ch 5 (ethics, CSR, sustainability — including normative ethical principles, terminal/instrumental values, Schein's culture definition, stakeholder theory, FCPA, UN Global Compact, triple bottom line); Ch 8 and Ch 9 (strategic analysis and strategic management — SWOT, PESTEL, Porter's Five Forces, VRIO, value chain, generic strategies, BCG matrix, vision/mission, SMART goals, planning levels); Ch 17 (organizational planning and controlling — Koontz/O'Donnell five-step planning process, goal vs domain vs hybrid planning, Drucker's eight-area goal hierarchy, Deming/Shewhart cycle, MBO, hierarchical/frequency/time-frame plans); and Ch 18 (management of technology and innovation — explicit vs tacit knowledge, internal vs external creation methods, leadership/followship, value proposition, lean start-up).
