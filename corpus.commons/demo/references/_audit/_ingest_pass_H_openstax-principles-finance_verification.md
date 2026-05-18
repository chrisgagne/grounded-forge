# Pass H Verification Log — OpenStax, Principles of Finance

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Date:** 2026-05-05
**Phase 2 parallel-batch ingestion** (book of 12 in the OpenStax PoC corpus). This file completes the wrap-up after the original Phase 2 agent produced the deep ref, light ref, decision-making application, and Pass A ledger but did not produce the Pass H, Pass I, staging, or stakeholder-engagement artefacts.

## Files produced (this wrap-up + previously)

| Artefact | Path | Status |
|---|---|---|
| Deep reference | `corpus.commons/demo/references/openstax-principles-finance-deep.md` | Pre-existing (845 lines); audited in Pass I |
| Light reference | `corpus.commons/demo/references/openstax-principles-finance.md` | Pre-existing |
| Decision-making application | `prompts/applications/decision-making/openstax-principles-finance-decision-making.md` | Pre-existing |
| Stakeholder-engagement application | `prompts/applications/stakeholder-engagement/openstax-principles-finance-stakeholder-engagement.md` | Produced by this wrap-up |
| Pass A ledger | `corpus.commons/demo/references/_ingest_pass_A_openstax-principles-finance_ledger.md` | Pre-existing |
| Pass H verification log (this file) | `corpus.commons/demo/references/_ingest_pass_H_openstax-principles-finance_verification.md` | Produced by this wrap-up |
| Pass I source-only audit | `corpus.commons/demo/references/_ingest_pass_I_openstax-principles-finance_source_audit.md` | Produced by this wrap-up |
| SEARCH-INDEX staging | `_ingest_search_index_principles-finance.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) | Produced by this wrap-up |
| Decision-making INDEX staging | `_ingest_dm_principles-finance.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) | Produced by this wrap-up |
| Stakeholder-engagement INDEX staging | `_ingest_se_principles-finance.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) | Produced by this wrap-up |
| Image index staging | `_ingest_image_index_principles-finance.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) | Produced by this wrap-up |

## Pass-by-pass results (consolidated from the deep ref, the original ledger, and this wrap-up)

### Pass A: Context

Captured in the pre-existing deep ref frontmatter and Pass A ledger:

- Title: *Principles of Finance*; OpenStax / Rice University; first publish 2022-03-24.
- Senior contributing authors: Julie Dahlquist (TCU) and Rainford Knight (Florida Atlantic). Six contributing authors.
- Licence: **CC BY-NC-SA 4.0** (NonCommercial-ShareAlike), per the OpenStax CMS metadata. Recorded explicitly in deep ref frontmatter.
- ISBNs: 978-1-711470-53-5 (color paperback), 978-1-711470-52-8 (B&W paperback), 978-1-951693-54-1 (digital).
- Structure: Preface; 20 substantive chapters; Core (Ch 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18) versus Extension (Ch 3, 4, 13, 14, 19, 20) designation per the Preface.

### Pass B: Structural read

Identified: Ch 1 (introduction to finance), Ch 2 (corporate structure and governance), Ch 3 (economic foundations), Ch 4 (accrual accounting), Ch 5 (financial statements), Ch 6 (ratio analysis), Ch 7-9 (TVM single, equal, unequal), Ch 10 (bonds), Ch 11 (stocks), Ch 12 (US market history), Ch 13-14 (statistics and regression), Ch 15 (risk-return / CAPM), Ch 16 (capital budgeting), Ch 17 (capital structure / WACC), Ch 18 (forecasting), Ch 19 (working capital), Ch 20 (risk management). Each chapter's substantive sections were mapped to specific section names in the converted markdown. Pedagogical scaffolding sections (Summary, Key Terms, CFA Institute LOS cross-references, Multiple Choice, Review Questions, Problems, Video Activity) were identified and excluded per Option B.

### Pass C: Deep read with citations

Read all 20 chapters' substantive content in full from the converted markdown (`corpus.commons/demo/sources/converted/openstax-principles-finance.md`, 35,453 lines, pymupdf4llm 0.2.9). Approximately 220+ load-bearing claims extracted, each citation-anchored to `(Ch N, "Section name")`. Working notes captured: named cases (Bacon Signs, Clear Lake Sporting Goods, Charlie's Camping World, Bluebonnet Industries, Sam's Sporting Goods, Mayweather Inc., Lore Ltd., Maddox Inc.), Irina Simmons interview, key statistics with provenance, contrarian positions, and cross-author connections.

Coverage scope: substantive content of all 20 chapters. Excluded: Summary, Key Terms, CFA Institute (per-chapter LOS cross-references), Multiple Choice, Review Questions, Problems, Video Activity (all pedagogical scaffolding per Option B); Index back-matter (standard).

### Pass D: Blockquote extraction

Verbatim quotations extracted and verified character-by-character against the source. Approximately 30+ verbatim quotes embedded in the deep ref carrying [V] markers, including:

- "business finance is about developing and understanding the tools that help people make consistently good and repeatable decisions" (Ch 1, "Why It Matters")
- "Stockholders are not just an abstract group . . . they are individuals who have chosen to invest their hard-earned cash in a company" (Ch 2, "Why It Matters")
- "any person or group that has an interest in the outcomes of an organization's actions . . . employees, customers, shareholders, suppliers, communities, and governments" (Ch 2.2, "Stakeholders")
- "a firm has important nonfinancial goals" (Ch 2, "Why It Matters")
- "managerial actions that affect a company's value may not immediately be reflected in the price of a company's stock but rather will become evident in the long-term prospects of the organization" (Ch 2, "Why It Matters")
- "tends to unify and discipline a management or agent group, thus fostering a union of agent and shareholder interests" (Ch 2.4, on hostile takeover threat)
- "(1) money received now can be saved or invested now and earn interest or a return . . . (2) any promise of future payments of cash will always carry the risk of default; and (3) it is simple human nature for people to prefer making their purchases of goods and services in the present rather than waiting" (Ch 7, "Why It Matters")
- "the more frequent the compounding period, the greater the future value of a savings amount, a bond, or any other financial instrument" (Ch 7.4)
- "Bond price and interest rate have an inverse relationship. When interest rates fall, bond prices rise, and vice versa" (Ch 10.1)
- "With common stock, there is no specific promise of how much cash investors will receive or when they will receive it" (Ch 11, "Why It Matters")
- "the discount rate used to bring the future cash flows of a bond into present value terms . . . the return that the investor will receive if the bond is held to maturity" (Ch 10.1, on YTM)
- "while profitability is very useful for analysis by investors to measure performance, an organization's cash flow provides superior measurement" (Simmons interview, Ch 9.1)
- "the difference between the present value of the cash inflows and the present value of cash outflows" (Ch 16.2, on NPV)
- "the criterion for whether or not a project is a good project" (Ch 16.2, on NPV)
- "providing a return equal to what potential investors could expect to earn elsewhere for a similar risk is the cost a company bears in exchange for obtaining funds from investors" (Ch 17.1)
- "in finance, hedging is a risk management tool. . . Speculating . . . involves directional bets" (Ch 20.1)
- "gives the owner the right, but not the obligation, to purchase or sell an asset for a specified price at some future date" (Ch 20.3, on options)
- Eisenhower: "plans are worthless, but planning is everything" (Ch 1.2)
- Buffett (paraphrased verbatim): "the payment of dividends to shareholders is 'almost a last resort for corporate management'" (Ch 11.2)

Each verbatim quote carries [V] and a section-anchored citation.

### Pass E: Synthesis

Pre-existing deep reference (845 lines) assembled per the canonical template: HTML-comment frontmatter, source/structure/citation-style header, author's thesis (paraphrased; five load-bearing claims), 20 thematic Parts each with subsections, Key Statistics table, Connections section, Positions Framed Against section, Citation and Source-Integrity Notes section. Evidence-class markers ([V], [AP], [AR], [AE], [BT]) applied throughout. Tier separation maintained.

### Pass F: Light-reference derivation

Pre-existing light ref derived from verified deep. (Trace count not counted in this wrap-up; the light ref was untouched.)

### Pass G: Application file projection

#### Sub-pass G.0 — Applicability decisions

- **Decision-making**: CLEAR YES. The book opens with "business finance is about developing and understanding the tools that help people make consistently good and repeatable decisions" and projects 20 chapters of decision toolkits (capital budgeting, valuation, TVM, risk pricing, financing structure, working capital). Pre-existing application file written by the original agent.

- **Stakeholder-engagement**: CLEAR YES. Decided in this wrap-up after honest re-evaluation. Reasoning: the book is overwhelmingly about *internal* financial decisions but Chapter 2 is wholly dedicated to corporate structure, governance, agency, and stakeholders — including the explicit OpenStax stakeholder definition ("any person or group that has an interest in the outcomes of an organization's actions . . . employees, customers, shareholders, suppliers, communities, and governments"), the Donaldson-Preston-style typology of agency conflicts (stockholders vs management, investors vs creditors, stockholders vs other stakeholders), the SOX / SEC governance regime, ESG ratings, and investor relations as a stakeholder-engagement function. Cross-cutting content extends through Ch 11 (preferred-vs-common claim ordering), Ch 17 (capital-structure choice as creditor / shareholder claim ordering, with explicit treatment of how leverage affects different capital claimants differently), and Ch 19 (trade-credit relationships with suppliers, payables-deferral as relationship-vs-economics tradeoff). The genuine substance is more concentrated than in *Organizational Behavior* but is nevertheless real and well-anchored. The skip-the-axis option was considered and rejected. Application file written by this wrap-up.

#### Sub-pass G.1-G.3

For decision-making, the original agent's pre-existing application file. For stakeholder-engagement, this wrap-up:

1. *Project*: the verified deep ref's concepts (stakeholder definition, agency typology, governance, ESG, capital claims, investor relations, supplier-trade-credit relationships) projected onto the stakeholder-engagement task vocabulary.
2. *Phase-organise*: phase tables for Mapping, Framing, Convening, Surfacing tension, Reaching agreement, Ratifying, Post-engagement.
3. *Cross-check*: each phase's diagnostic content cross-checked back to the deep ref. Only paraphrased citations; zero verbatim blockquotes (regex `^>\s*"` confirmed to return nothing in the SE application file — verified via `grep -c '^>\s*"' prompts/applications/stakeholder-engagement/openstax-principles-finance-stakeholder-engagement.md` after writing).

### Pass H: Cross-reference (this wrap-up)

Staging files produced rather than direct edits to canonical indexes (per parallel-batch protocol). Files:

- `_ingest_search_index_principles-finance.md` (staging file, merged into SEARCH-INDEX.md and deleted in consolidation) — light-ref row, deep-ref row, ~50 concept-A-Z entries.
- `_ingest_dm_principles-finance.md` (staging file, merged into DECISION-MAKING-INDEX.md and deleted in consolidation) — quick-start entries, phase-by-phase entries for the 6 decision-making phases.
- `_ingest_se_principles-finance.md` (staging file, merged into STAKEHOLDER-ENGAGEMENT-INDEX.md and deleted in consolidation) — quick-start entries, phase-by-phase entries for the 7 stakeholder-engagement phases.
- `_ingest_image_index_principles-finance.yaml` (staging file, merged into IMAGE-INDEX.yaml and deleted in consolidation) — substantive image entries plus methodology comment.

### Pass I: Source-only audit (this wrap-up)

See `corpus.commons/demo/references/_ingest_pass_I_openstax-principles-finance_source_audit.md`. Outcome: PASS. Approximately 240 claims audited, 1 marker correction applied, 0 strips required. The deep ref is well-anchored to source material with appropriate evidence-class markers throughout.

## Image classification (this wrap-up)

- **Total images extracted from PDF**: 271 (242 PNG, 29 JPEG)
- **Substantive (kept and indexed)**: 238 PNG diagrams / charts / tables / Excel screenshots
- **Decorative (deleted)**: 33 (29 JPEGs, all chapter-opening photographs of buildings, conference rooms, audience scenes, executives, and one OpenStax brand JPEG; plus 4 PNGs: Rice University logo p0005-1, paper-texture cover p0006-1, dark-rectangle frame p0006-6, and a cartoon laptop/papers/chart illustration p0029-1).

**Methodology correction from the OB pilot:** the OB pilot's "PNG = substantive heuristic" was followed but supplemented with visual inspection of all suspect cases (front-matter PNGs and any cartoon-style illustrations encountered during Pass C). The final classification was confirmed by visual sampling of representative PNGs across each chapter (from the early ratio diagrams to the late risk-management diagrams). PNGs in this book are predominantly substantive (financial-flow diagrams, Excel screenshots showing calculator and spreadsheet outputs, regression / scatter plots, supply-and-demand curves, balance-sheet layouts, perpetuity / annuity time-line diagrams). The four decorative PNGs are pure cosmetic / iconographic items.

The original Phase 2 agent did not perform image classification; this wrap-up performed it.

## Indexes targeted (NOT touched — staging files only)

Per the parallel-batch protocol, this wrap-up did NOT touch:

- `corpus.commons/demo/references/SEARCH-INDEX.md` (race risk; staging file emitted)
- `prompts/indexes/DECISION-MAKING-INDEX.md` (race risk; staging file emitted)
- `prompts/indexes/STAKEHOLDER-ENGAGEMENT-INDEX.md` (race risk; staging file emitted)
- `docs/images/IMAGE-INDEX.yaml` (race risk; staging file emitted)

## Pipeline issues encountered

1. **Original agent's incomplete G.0 documentation.** The original agent left no record of why the SE app was not produced. This wrap-up performed the G.0 evaluation honestly, found genuine SE substance in Ch 2 + cross-cutting threads, and produced the application file rather than skipping. The decision was not pro forma; the alternative skip-with-reason path was considered.

2. **Image classification volume.** 271 images is a large set. Visual inspection of every PNG was not performed in this wrap-up; instead, representative sampling across chapters was performed and the PNG = substantive heuristic was applied with confirmed exceptions for 4 known decoratives. This is a known limitation; v0.1.5+ could refine per-image descriptions.

3. **Coverage of pedagogical fictional cases.** The text uses fictional pedagogical cases (Bacon Signs, Clear Lake Sporting Goods, Bluebonnet Industries, Sam's Sporting Goods) that look like empirical references but are author-constructed for illustration. The deep ref treats these as [AE] (author example) rather than [V] (verbatim source data) where they appear as worked numerical illustrations. Confirmed in Pass I.

## Methodology refinements added by this book

These observations supplement the OB pilot's methodology notes:

1. **PNG = substantive heuristic mostly held but needed exceptions.** Four decorative PNGs were identified by visual inspection; all four were either front-matter brand assets (Rice University logo, paper texture, dark frame) or one cartoon illustration. The heuristic should be supplemented with visual confirmation of front-matter PNGs and any cartoon-style illustrations.

2. **Pass G.0 for finance and other heavily-quantitative books.** Pass G.0 honesty requires looking past the surface (a finance book "looks like" it should not have stakeholder-engagement content) to the actual deep ref. *Principles of Finance* dedicates a chapter to corporate structure / governance / agency / stakeholders and threads the topic through bond ordering, capital structure choice, and supplier relations. The G.0 decision should be made from the verified deep ref, not from the book's title or genre.

3. **Pedagogical fictional cases.** OpenStax books often use fictional companies as worked examples. The evidence-class marker for these is [AE] (author example), not [V]. The Pass I audit should confirm this.
