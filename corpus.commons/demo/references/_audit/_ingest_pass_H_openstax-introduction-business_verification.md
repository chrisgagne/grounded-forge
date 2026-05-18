# Pass H Verification Log — OpenStax, Introduction to Business

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Phase 2 batch:** Book of 12 in the OpenStax PoC corpus. This wrap-up was completed by a separate Opus 4.7 sub-agent because the original parallel-batch run for *Introduction to Business* hit limits before Pass H, Pass I, and the four staging files were produced. Deep ref, light ref, both application files, and the Pass A ledger were already on disk and intact; this wrap-up did not redo them.

## Files produced

| Artefact | Path | Lines | Status |
|---|---|---|---|
| Deep reference | `corpus.commons/demo/references/openstax-introduction-business-deep.md` | 907 | Complete (post-Pass-I fixes) |
| Light reference | `corpus.commons/demo/references/openstax-introduction-business.md` | 143 | Pre-existing, not modified |
| Decision-making application | `prompts/applications/decision-making/openstax-introduction-business-decision-making.md` | 166 | Pre-existing, not modified |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-introduction-business-stakeholder-engagement.md` | 208 | Pre-existing, not modified |
| Pass A ledger | `corpus.commons/demo/references/_ingest_pass_A_openstax-introduction-business_ledger.md` | 96 | Pre-existing, not modified |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-introduction-business_verification.md` | (this file) | Complete |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-introduction-business_source_audit.md` | (Pass I artefact) | Complete |
| Staging: SEARCH-INDEX entries | `_ingest_search_index_introduction-business.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) | (staging) | Complete |
| Staging: DM-INDEX entries | `_ingest_dm_introduction-business.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) | (staging) | Complete |
| Staging: SE-INDEX entries | `_ingest_se_introduction-business.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) | (staging) | Complete |
| Staging: IMAGE-INDEX entries | `_ingest_image_index_introduction-business.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) | (staging) | Complete |

## Pass-by-pass results (recovered from on-disk artefacts plus this wrap-up's audit)

### Pass A: Context

Captured by the original ingestion run. Source: 7 senior contributing authors (lead Lawrence J. Gitman, San Diego State University Emeritus); CC BY 4.0 licence (the only book in the OpenStax Phase 2 PoC corpus genuinely licensed CC BY 4.0; all 11 others are CC BY-NC-SA 4.0); ISBNs 978-1-947172-54-8 print and 978-1-947172-55-5 PDF; 17 substantive chapters plus Appendix A; total source markdown 53,932 lines.

### Pass B: Structural read

Identified by the original ingestion run. 17 chapters covering: economic systems and the business environment (Ch 1); ethics, social responsibility, and stakeholders (Ch 2); global marketplace (Ch 3); forms of business ownership (Ch 4); entrepreneurship and small business (Ch 5); management and leadership (Ch 6); organisational structure (Ch 7); HR and labor relations (Ch 8); motivating employees (Ch 9); operations management (Ch 10); products and pricing (Ch 11); distribution and promotion (Ch 12); information technology (Ch 13); accounting (Ch 14); money and financial institutions (Ch 15); financial management and securities markets (Ch 16); career planning (Ch 17); plus Appendix A on the legal and tax environment.

Per-chapter scaffolding sections (Key Terms, Summary of Learning Outcomes, Preparing for Tomorrow's Workplace Skills, Ethics Activity, Working the Net, Critical Thinking Case, Hot Links Address Book) reliably identified for Option B exclusion. Back-matter `## References` (line 50151) and `## Index` (line 52139) excluded as standard back-matter.

### Pass C: Deep read with citations

Performed by the original ingestion run. All 17 substantive chapters plus Appendix A read in full from the converted source markdown. Approximately 220+ load-bearing claims extracted with `(Ch N, "Section name")` citations. Working notes (visible in the deep ref): named cases (Ben & Jerry's seven-times rule, Sony-Apple, Walmart, Disney, Sandberg, Drucker, Mary Parker Follett, Pinchot intrapreneur coinage, McGregor Theory X/Y, Maslow, Mayo Hawthorne, Herzberg motivator-hygiene, Ouchi Theory Z, Adler-Gunderson, Deming TQM, Six Sigma, P&G four pillars, Cisco virtual corporation, Wegmans, Apple, Amazon, IBM, McDonald's Hurricane Katrina response, Norfolk Southern McCracken empowerment, Marriott Hurricane Maria contingency, Ethan Allen Interiors, Pixar process departmentalization, Unilever matrix exit), key statistics (CSR philanthropy ~$19B; socially-responsible investing >$7T; corporate share of profit 58%; franchise output $890B; small business 80% no employees; ESOP ~6,717 firms ~14M participants; 2017 women's pay 80.5% of men; mutual fund ~94M holders ~$40T global; ETFs >$3.5T; bond market ~$88T; asbestos lawsuits >$70B), contrarian positions (managers as adapters not change agents; strict Maslow not empirically supported; canned sales obsolete; matrix structures hinder accountability; cost-only competitive advantage erodes; autocratic style on its way out), and cross-author connections.

### Pass D: Blockquote extraction

Performed by the original ingestion run; verified during this wrap-up. Approximately 40+ verbatim quotes embedded in the deep ref carry [V] markers. Spot-checked verbatim against source for accuracy in this wrap-up's Pass I; one verbatim slip was found and corrected (stakeholder-list quote rephrased to match source word for word). All other [V] quotes verified character-by-character.

### Pass E: Synthesis

Performed by the original ingestion run. Deep reference assembled (907 lines) per the canonical template: HTML-comment frontmatter, source/structure/citation-style/coverage block, author's thesis (paraphrased, four paragraphs), 17 thematic Parts plus Appendix A each with subsections, Key Statistics table (44 rows), Connections section, Positions Framed Against section (10 explicit positions), Citation and Source-Integrity Notes section. Evidence-class markers throughout. Tier separation maintained.

### Pass F: Light-reference derivation

Performed by the original ingestion run. Light ref totals 143 lines.

### Pass G: Application file projection

Performed by the original ingestion run. Sub-pass G.0 — Applicability decisions:

- **Decision-making**: CLEAR YES. Ch 6.6 dedicates a section to managerial decision-making with the five-step process (Exhibit 6.7), the programmed-vs-non-programmed distinction, and named cases (Norfolk Southern post-Katrina, Oreck Hurricane Katrina). Ch 1.7 addresses competitive structure for market-entry decisions; Ch 2 supplies the four-philosophy ethics frame plus the CSR pyramid for ethical decisions; Ch 3.6 supplies the six-mode global-entry decision; Ch 4 supplies the ownership-form decision; Ch 5.4 supplies the start-business decision; Ch 7 supplies the structural decision space; Ch 9 supplies the motivation-design decisions. The book is fundamentally a decision-making frame.
- **Stakeholder engagement**: CLEAR YES. Ch 2.4 is dedicated to stakeholder responsibilities with explicit treatment of employees, customers, society (Benefit Corporations and corporate philanthropy), and investors (socially responsible investing). Ch 8 addresses employee engagement specifically (HR, labor relations, four-aspect social contract). Ch 11-12 address customer engagement (marketing concept, customer-relationship management). The book provides a survey-level, plural-stakeholder lens.

Sub-pass G.1, G.2, G.3 (project, phase-organise, cross-check) all completed in the original run. Both application files contain zero verbatim blockquotes (regex `^>\s*"` returns nothing — verified during this wrap-up).

### Pass H: Cross-reference (this pass)

Per the parallel-batch instructions, canonical indexes are not modified by this wrap-up. Staging files instead:

- `_ingest_search_index_introduction-business.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) — light-ref + deep-ref table rows + Concept-A-Z entries.
- `_ingest_dm_introduction-business.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) — quick-start rows and phase-by-phase additions for the decision-making axis.
- `_ingest_se_introduction-business.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) — quick-start rows and phase-by-phase additions for the stakeholder-engagement axis.
- `_ingest_image_index_introduction-business.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) — 51 substantive image entries; 107 decorative images deleted from disk.

### Pass I: Source-only audit (this pass)

See `_ingest_pass_I_openstax-introduction-business_source_audit.md`. Summary numbers:

- N audited: ~230 (body claims with citations or evidence markers).
- N source-anchored without modification: ~227.
- N marker corrections: 1 (grapevine 47%/57% claim was [V] but is paraphrase; corrected to [AP]).
- N verbatim slips fixed: 1 (stakeholder-list quote "the employees, its customers..." -> "the stakeholders of a business are its employees, its customers...").
- N strips: 0.
- N image-classification corrections (deep ref text): 1 (note that the pilot PNG-substantive heuristic proved unreliable for this book and the substantive-image numbers updated in the deep ref's source-integrity-notes block).
- Pass I outcome: PASS after fixes.

## Image classification (this wrap-up)

The pilot Phase 2 heuristic (PNG = substantive, JPEG = decorative) is **unreliable** for Introduction to Business. The wrap-up subagent visually inspected every PNG and every JPEG.

- **Total images extracted from PDF**: 158 (144 JPEG, 14 PNG).
- **Substantive (kept and indexed)**: 51 (8 PNG + 43 JPEG).
  - PNGs: p0051-1, p0051-2, p0052-1, p0053-1 (Ch 1 demand/supply/equilibrium/shift); p0155-1 (Ch 4 corporate governance); p0280-1 (Ch 7 flat vs tall); p0403-1 (Ch 10 Gantt chart); p0477-1 (Ch 12 marketing intermediary).
  - JPEGs: 43 framework diagrams across Chs 1-16 covering environmental forces, circular flow, factors of production, federal budget, decision-making process, consumer behaviour, CSR pyramid, departmentalization, line-and-staff org, matrix structure, new-product development, HR planning, employee selection, training cycle, performance management, managerial pyramid, grievance procedure, collective bargaining, motivation model, Maslow hierarchy, product life cycle, control process, expectancy theory, HR functions, production layouts, marketing channels, traditional-vs-targeted marketing, supply chain, personal selling, product layers, accounting cycle, VPN, MIS hierarchy, bank assets, ASP topology, Federal Reserve districts, financial intermediaries, accounting-types split, cash management, secondary markets.
- **Decorative (deleted from disk)**: 107 (6 PNG + 101 JPEG).
  - PNGs: p0006-1 (photograph overlay), p0006-3 (monitor frame), p0006-4 (OpenStax Study Guide screenshot), p0006-6, p0006-7, p0006-8 (dark monitor / abstract frame shapes).
  - JPEGs: 101 photographs (executives, consumer products, sports figures, stadiums, urban scenery, military, university, retail stores, transportation) and chapter-opener illustrations.

**Heuristic refinement for the parallel batch:** always visually inspect every image; do not rely on PNG vs JPEG. File-size correlation is weak (small JPEGs are sometimes framework diagrams; large JPEGs are sometimes diagrams; small PNGs can be decorative monitor frames; large PNGs can be background photo overlays).

## Per-pass effort estimates (this wrap-up)

- Pass H (staging files + image YAML): heavy (158 image visual inspections + 51 image YAML entries + 3 staging markdown files)
- Pass I (source audit + fixes): medium

## Notes for parent agent consolidation

1. **CC BY 4.0 licence** on this book is genuine (verified verbatim from source front matter). Distinct from all other Phase 2 books.
2. **Author attribution** of seven contributors with Gitman as lead is correct.
3. **Image classification** required full visual inspection — pilot PNG/JPEG heuristic is unreliable. Decoratives have already been deleted from `docs/images/introduction-business/`.
4. **Application files** for both axes were already complete on disk; the wrap-up did not modify them. Both contain zero verbatim blockquotes (regex check passed).
5. **Pass G.0 decisions:** CLEAR YES for both decision-making and stakeholder-engagement.
6. **Two fixes applied to deep ref during Pass I:** stakeholder-list verbatim slip; grapevine survey marker correction. See Pass I audit log for details.
