# Pass A Ledger — OpenStax, Organizational Behavior

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Pilot run:** Book 1 of 12 in the OpenStax PoC corpus.

## Source metadata

- **Title:** Organizational Behavior
- **Publisher:** OpenStax (Rice University), with print partnership via Kendall Hunt Publishing.
- **First published:** 2019-04-15. Latest publish date 2019-06-05. Reprint copyright in front matter dated 2026.
- **Edition:** First edition (current OpenStax release; no later edition exists).
- **ISBNs:**
  - Color paperback: 978-1-947172-71-5
  - B&W paperback: 978-1-59399-877-6
  - Digital: 978-1-947172-72-2
- **URL:** https://openstax.org/details/books/organizational-behavior
- **Licence:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (**CC BY-NC-SA 4.0**). Confirmed verbatim in front matter, lines 387-390 of the converted markdown: "Organizational Behavior is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY NC-SA) license".
- **Authors (12 contributors; OpenStax `display_at_top: true` flags lead):**
  - Lead: J. Stewart Black, INSEAD
  - Contributors: David S. Bright (Wright State), Donald G. Gardner (UCCS), Eva Hartmann (Richmond), Jason Lambert (Texas Woman's), Laura M. Leduc (James Madison), Joy Leopold (Webster), James S. O'Rourke (Notre Dame), Jon L. Pierce (Minnesota-Duluth), Richard M. Steers (Oregon), Siri Terjesen (American), Joseph Weiss (Bentley)

## Source format and conversion path

- **PDF:** 631 pages, 44 MB, version 1.7. At `corpus.commons/demo/sources/original/openstax-organizational-behavior.source.md`.
- **Conversion tool:** pymupdf4llm 0.2.9 (after markitdown 0.1.5 import-failed on numpy/numexpr ABI mismatch — see phase2 log).
- **Converted markdown:** 32,852 lines, 1.9 MB. At `corpus.commons/demo/sources/converted/openstax-organizational-behavior.md`.
- **Page anchors:** not preserved by pymupdf4llm. Citation style: `(Ch N, "Section name")`.

## Coverage scope (Option B — substantive content only)

Per global decision Q2 in the planning log, the deep ref covers:

**Included:** chapter introduction (`### **Introduction**`), all numbered substantive sections (`### **N.M Section name**`), and the chapter-overview text under the chapter title before sections start.

**Excluded:** per-chapter pedagogical scaffolding —
- `### **Key Terms**`
- `### **Summary of Learning Outcomes**`
- `### **Chapter Review Questions**`
- `### **Critical Thinking Case**`
- `### **Management Skills Application Exercises**`
- `### **Managerial Decision Exercises**`

The deep ref's frontmatter and source-integrity-notes section both record this exclusion explicitly per the source-integrity rule.

## High-level structure (from converted markdown)

19 substantive chapters plus appendices.

| Ch | Chapter title | Section count | Source line (open) |
|---|---|---|---|
| 1 | Management and Organizational Behavior | 4 | 671 |
| 2 | Individual and Cultural Differences | 7 | 1848 |
| 3 | Perception and Job Attitudes | 5 | 3178 |
| 4 | Learning and Reinforcement | 4 | 4668 |
| 5 | Diversity in Organizations | 7 | 6036 |
| 6 | Perception and Managerial Decision Making | 6 | 7856 |
| 7 | Work Motivation for Performance | 4 | 9309 |
| 8 | Performance Appraisal and Rewards | 5 | 11654 |
| 9 | Group and Intergroup Relations | 4 | 13394 |
| 10 | Understanding and Managing Work Teams | 6 | 15023 |
| 11 | Communication | 5 | 16211 |
| 12 | Leadership | 9 | 17458 |
| 13 | Organizational Power and Politics | 4 | 19469 |
| 14 | Conflict and Negotiations | 4 | 20845 |
| 15 | External and Internal Organizational Environments and Corporate Culture | 6 | 22382 |
| 16 | Organizational Structure and Change | 3 | 23851 |
| 17 | Human Resource Management | 6 | 25416 |
| 18 | Stress and Well Being | 4 | 26911 |
| 19 | Entrepreneurship | 6 | 28552 |

Appendix A (Theory Building / Scientific Method in OB Research, lines 29919-30323) is included in the deep ref because it grounds the book's empirical framing. Appendix B (Scoring keys for self-assessment exercises) is excluded as scaffolding. The References (line 30631) and Index (line 32198) sections are excluded as standard back-matter.

## Front-matter framing

The Preface (lines 370-669) and the chapter-opening "Exploring Managerial Careers" profiles serve as orientation. The Preface declares:

- The book "was designed to address two main themes": (1) the variables that affect how/when/where/why managers perform their jobs, and (2) the theories and techniques used by successful managers to achieve and exceed objectives (Preface, "About Organizational Behavior", lines 437-444).
- The chapter authorship is distributed: "specialists in a variety of areas have authored individual chapters" (lines 446-447). This bears on attribution for borderline-cited claims — the book speaks with multiple authorial voices but presents itself as a single integrated text.

## Citation style decision

`(Ch N, "Section name")` — pymupdf4llm did not preserve page anchors. Recorded in the deep ref's source-integrity-notes block.

## Pre-flight gates

1. **Completeness.** Confirmed: 19 chapters present, each with the full Introduction + numbered sections + standard scaffolding sections. No mid-paragraph truncation. TOC structure (chapter heading + numbered sections + standard exclusion blocks) holds across all 19 chapters.
2. **Citation style.** No page anchors in converted markdown; cite as `(Ch N, "Section name")`.
3. **Model identity.** Confirmed Opus 4.7 (claude-opus-4-7[1m], 1M context) running this ingestion.

## Outputs anticipated

- `corpus.commons/demo/references/openstax-organizational-behavior-deep.md`
- `corpus.commons/demo/references/openstax-organizational-behavior.md`
- `prompts/applications/decision-making/openstax-organizational-behavior-decision-making.md` (pending Pass G.0)
- `prompts/applications/stakeholder-engagement/openstax-organizational-behavior-stakeholder-engagement.md` (pending Pass G.0)
- Pass H verification log + Pass I source-only audit + this Pass A ledger.
- Index updates to SEARCH-INDEX.md, DECISION-MAKING-INDEX.md, STAKEHOLDER-ENGAGEMENT-INDEX.md.
- Image index entries (substantive subset of 189 extracted images).
