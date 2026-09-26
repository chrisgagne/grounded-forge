# SSDF v1.1 ingestion coverage and figure ledger

Producer: GPT-6 (Codex). Date: 2026-09-25. Image scope: full, explicitly requested by the operator. Status: A–E complete; independent Pass I pending. Target: corpus.commons/demo, scope open.

## Source integrity

- Official 36-page PDF SHA-256: `617746e553a9e2da49bfbd4eef0dfc3094758a39b869314e4173ac36605cde22`.
- Markitdown initial conversion: 15,589 whitespace-delimited words, 36 page segments. It contains the repeated rotated margin notice as isolated letters and less convenient table reading order.
- Poppler 26.08.0 `pdftotext -raw`: 14,227 words, 36 page segments plus final form feed. Raw word count differs partly because the margin notice remains a line, and some authority-page words run together.
- Final tape: 14,891 words, 2,298 lines. First three pages use markitdown; pages 4–36 use Poppler raw output, with editorial page/section headings. Every selected page segment is included verbatim before adding navigation.
- Full read: raw.txt lines 1–2017 read in contiguous tool outputs (overlapping ranges); first three markitdown pages also read in full. No unread chapter or appendix. Source has text-heavy landscape tables; word count is plausible for 36 pages including covers, extensive mappings and two near-empty continuations.
- Quotes: both blockquotes mechanically match the final tape after joining PDF line wrapping with spaces.

## Complete source structure and inspection

| PDF pages | Printed pages | Content | Read and visual inspection |
|---|---|---|---|
| 1–3 | Unnumbered | Covers, title, author affiliations, Authority, publication notices | Full converted text; page contact sheet for layout/logos |
| 4 | ii | ITL reports, abstract, keywords, trademarks | Full text; contact sheet |
| 5–6 | iii–iv | Acknowledgments, Audience, Note to Readers | Full text; contact sheet |
| 7 | v | Patent Disclosure Notice | Full text; contact sheet |
| 8 | vi | Executive Summary | Full text; contact sheet |
| 9 | vii | Contents and List of Tables | Full text; contact sheet; compared with actual sections |
| 10–12 | 1–3 | Introduction and footnotes 1–4 | Full text; contact sheet |
| 13 | 4 | Framework groups and interpretation of practices/tasks/examples/references | Full text; contact sheet |
| 14–28 | 5–19 | Table 1, every task and example, mappings and footnotes 5–9 | Full text; every page visually inspected individually at 1800-pixel scale |
| 29–32 | 20–23 | All bibliography entries | Full text; contact sheet |
| 33 | 24 | Appendix A, EO 14028 explanation and Table 2 | Full text; full page inspected individually at 1800-pixel scale |
| 34–35 | 25–26 | Appendix B, all acronym entries | Full text; contact sheet |
| 36 | 27 | Appendix C, all final/draft changes | Full text; contact sheet |

## Image reconciliation

Repository extractor executed with `/usr/local/bin/python3` (PyMuPDF 1.27.2.3) because Homebrew ARM Python could not load the installed x86 PyMuPDF library. It extracted three bitmap images. Each was visually inspected: `p0033-1.png` says “Appendix A—”; `p0034-1.png` says “Appendix B—”; `p0036-1.png` says “Appendix C—”. These are heading typography, not conceptual illustrations. All three were classified decorative and removed after preserving their labels as editorial tape navigation.

The extractor does not capture vector/text tables. All 36 page renders were inspected to cover that blind spot. Table 1 is one substantive table spread across 15 pages; Table 2 is one substantive table on one page. Their 16 full-page PNG panels are retained, preserving table continuations and footnotes. No numbered diagrams/figures are present. Cover logo/seal and ornamental heading bars are decorative and are not indexed.

| Image retained | Printed page | Content |
|---|---|---|
| p0014-table.png | 5 | Table 1: PO.1.1–PO.1.3, requirements and third parties |
| p0015-table.png | 6 | Table 1: PO.1.3 continuation; PO.2.1–PO.2.2; provenance footnote |
| p0016-table.png | 7 | Table 1: PO.2.3; PO.3.1–PO.3.3; artefact/evidence footnote |
| p0017-table.png | 8 | Table 1: PO.3.3 continuation; PO.4.1–PO.4.2; PO.5.1 |
| p0018-table.png | 9 | Table 1: PO.5.1 continuation; PO.5.2; PS.1.1; zero-trust/code-signing footnotes |
| p0019-table.png | 10 | Table 1: PS.2.1; PS.3.1–PS.3.2 |
| p0020-table.png | 11 | Table 1: PW.1.1–PW.1.3 |
| p0021-table.png | 12 | Table 1: PW.2.1; retired PW.3; PW.4.1–PW.4.2; retired PW.4.3 |
| p0022-table.png | 13 | Table 1: PW.4.4; retired PW.4.5; PW.5.1; retired PW.5.2 |
| p0023-table.png | 14 | Table 1: PW.6.1–PW.6.2; PW.7.1–PW.7.2 |
| p0024-table.png | 15 | Table 1: PW.7.2 continuation; PW.8.1–PW.8.2 |
| p0025-table.png | 16 | Table 1: PW.9.1–PW.9.2; RV.1.1–RV.1.2; NVD footnote |
| p0026-table.png | 17 | Table 1: RV.1.2 continuation; RV.1.3; RV.2.1 |
| p0027-table.png | 18 | Table 1: RV.2.2; RV.3.1–RV.3.4 |
| p0028-table.png | 19 | Table 1: RV.3.4 reference mappings continued |
| p0033-table.png | 24 | Table 2: all 15 EO Section 4e subsection mappings, with Appendix A context |

Reconciliation: 3 embedded assets extracted = 0 substantive embedded assets + 3 decorative deleted. Supplemental vector/text page captures: 16 substantive retained. Total substantive index entries: 16, representing 2 complete tables. No figure classification remains pending.
