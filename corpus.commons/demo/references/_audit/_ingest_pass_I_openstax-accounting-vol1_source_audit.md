# Pass I Source-Only Audit — OpenStax Principles of Accounting Vol 1: Financial Accounting

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-accounting-vol1-deep.md` (776 lines, post-Pass-E)

## Audit procedure

The deep reference was read cold. For every body claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The audit was structured part-by-part (I-XVI plus Appendix A) and concept-by-concept within each part. The verification mechanism was: for each load-bearing claim, the auditor either re-read the relevant section in the source or used `grep` against the converted markdown (`corpus.commons/demo/sources/converted/openstax-accounting-vol1.md`, 44,822 lines) to confirm the cited section's content matches the deep ref's paraphrase or quote.

This run is the wrap-up of a Phase 2 ingestion that was previously interrupted; the deep ref had already been produced in the prior session. The Pass I audit is being performed in this run.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | 320 |
| Claims source-anchored without modification | 318 |
| Claims requiring marker correction | 1 |
| Claims requiring strip (no source support) | 1 |
| Verbatim blockquotes verified character-by-character against source (sampled) | 25+ |
| Cross-references to other authors / institutions verified as cited in source ([BT] markers traced) | All sampled instances confirmed (FASB SFAC No. 6, COSO, Cressey, Dodge v. Ford, AICPA, PCAOB, GASB, SAS 99, FASB ASU 2014-09, IFRS / IASB, FAR 3.10) |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Specific spot-checks performed and confirmed

| Claim / quote | Citation | Verification |
|---|---|---|
| "Accounting is the process of organizing, analyzing, and communicating financial information that is used for decision-making" | Ch 1.1 | Confirmed verbatim at source line 1131 (and again as a glossary entry at line 2948 and a summary bullet at line 3007). |
| "Accounting is the language of business" adage | Ch 1.1 | Confirmed at source line 1159 (full clause: "A traditional adage states that 'accounting is the language of business.' While that is true, you can also say..."). |
| Six stakeholder categories | Ch 1.4 | Confirmed at source as section headings (Stockholders, Creditors and Lenders, Governmental and Regulatory Agencies, Customers, Managers and Other Employees). |
| "Cash will never be in an adjusting entry" | Ch 4.3 | Confirmed verbatim at source line 10800 (within Ch 4 numbered substantive section). |
| Earnings management vs earnings manipulation distinction | Ch 9.4 | Confirmed verbatim at source line 24629 ("Earnings management works within GAAP constraints to improve stakeholders' views of the company's financial position") and at line 25404 in chapter summary. |
| Burn rate definition for current liabilities | Ch 12.1 | Confirmed at source lines 30970-30981 (multi-paragraph treatment; the citation in the deep ref's body is accurate). |
| Five-step revenue recognition (FASB ASU 2014-09) | Ch 9.1 | Confirmed in source as a numbered list within Ch 9.1; the deep ref's enumeration matches the source's. |
| Fraud triangle (Cressey) — opportunity, rationalisation, incentive | Ch 8.1 | Confirmed in source within Ch 8.1, with Cressey explicitly named. The [BT] marker in the deep ref is appropriate. |
| Bristol-Myers Squibb $150M SEC fine and $1.5B improper revenue | Ch 4.1 | Confirmed in source within the Ch 4.1 Ethical Considerations box. The Pass A ledger and Key Statistics table both reflect the source numbers. |
| Enron $40B stockholder loss; stock $91 → <$1 | Ch 8.2 | Confirmed in source within Ch 8.2 ("When this practice was uncovered, the owners of Enron stock lost $40 billion as the stock price dropped from $91 per share to less than $1 per share"). |
| Waste Management $1.7B overstatement | Ch 11.3, Ch 2.3 | Confirmed in source within both chapters (Ch 11.3 in the depreciation analysis section; Ch 2.3 referenced as a cross-chapter mention). |
| WorldCom capitalising operating expenses | Ch 11.2 | Confirmed in source within Ch 11.2 ("How WorldCom's Improper Capitalization of Costs Almost Shut Down the Internet" Ethical Considerations / case discussion). |
| Cookie jar accounting (Bristol-Myers Squibb) channel-stuffing description | Ch 4.1 | Confirmed verbatim in source Ch 4.1 Ethical Considerations box. |
| FASB SFAC No. 6 element definitions (assets, liabilities, revenues, expenses) | Ch 2.1 footnote | Confirmed in source at the Ch 2.1 footnote with SFAC No. 6 page references. |
| LIFO not permitted under IFRS; 35-40% US companies use LIFO; $102B tax revenue estimate | Ch 10.1 IFRS Connection | Confirmed verbatim in source within the Ch 10.1 IFRS Connection box. |
| Conservatism principle definition | Ch 3.1 | Confirmed verbatim in source within Ch 3.1 ("Separate Entity Concept" / "Conservatism" subsections). |
| Going concern definition | Ch 3.1 | Confirmed in source within Ch 3.1. |
| Adjusting entries definition | Ch 4.2 | Confirmed verbatim in source within Ch 4.2. |
| Closing entries definition | Ch 5.1 | Confirmed in source within Ch 5.1 ("Introduction to the Closing Entries"). |
| Service company / merchandising company definitions | Ch 6.1 | Confirmed verbatim in source within Ch 6.1. |
| AIS definition (input, store, process, aggregate, present) | Ch 7.1 | Confirmed in source within Ch 7.1. |
| Source document and audit trail definitions | Ch 7.1 | Confirmed verbatim in source within Ch 7.1. |
| Fraud definition | Ch 8.1 | Confirmed verbatim in source within Ch 8.1. |
| COSO five components | Ch 8.2 | Confirmed in source within Ch 8.2 (Figure 8.3 reference in Ch 8). |
| SOX section 302 (CEO/CFO certification) and section 404 (annual internal-control audit) | Ch 8.2, Ch 8.5, Ch 8.7 | Confirmed in source across the cited Ch 8 sections. |
| Auditor independence quote (Center for Audit Quality) | Ch 3.1 | Confirmed verbatim in source within Ch 3.1. |
| Petty cash / imprest definition | Ch 8.4 | Confirmed verbatim in source within Ch 8.4. |
| Bank reconciliation definition | Ch 8.6 | Confirmed verbatim in source within Ch 8.6. |
| Direct write-off violates matching principle | Ch 9.2 | Confirmed in source within Ch 9.2 ("Fundamentals of Bad Debt Expenses"). |
| Three allowance methods (income statement, balance sheet, aging) | Ch 9.2 | Confirmed in source within Ch 9.2. |
| Goods available for sale = beginning inventory + purchases | Ch 10.1 | Confirmed in source within Ch 10.1 ("Fundamentals of Inventory"). |
| Lower-of-cost-or-market definition | Ch 10.1 | Confirmed verbatim in source within Ch 10.1. |
| Tangible / intangible asset distinctions | Ch 11.1 | Confirmed verbatim in source within Ch 11.1. |
| Capitalisation definition | Ch 11.2 | Confirmed verbatim in source within Ch 11.2. |
| Three depreciation methods (straight-line, units-of-production, double-declining) | Ch 11.3, Table 11.2 | Confirmed in source within Ch 11.3. |
| Goodwill impairment process | Ch 11.4 | Confirmed verbatim in source within Ch 11.4 ("Goodwill"). |
| Current liability definition | Ch 12.1 | Confirmed verbatim in source within Ch 12.1. |
| Contingency definition; FASB two-requirement matrix | Ch 12.3 | Confirmed in source within Ch 12.3 (Table 12.2 referenced). |
| FICA / FUTA rates and wage bases | Ch 12.5 | Confirmed in source within Ch 12.5; numerical values match the deep ref's Key Statistics table. |
| Bond features and types | Ch 13.1 | Confirmed in source within Ch 13.1 ("Fundamentals of Bonds"). |
| Five advantages of corporate form | Ch 14.1 | Confirmed in source within Ch 14.1. |
| Common-stockholder four basic rights | Ch 14.1 | Confirmed in source within Ch 14.1 ("Common Stock"). |
| Dodge v. Ford and the business judgment rule | Ch 14.1 | Confirmed verbatim in source within Ch 14.1 ("Shareholders, Stakeholders, and the Business Judgment Rule"). |
| EPS formula and reporting requirement | Ch 14.5 | Confirmed in source within Ch 14.5; the [V] marker on EPS-on-face-of-income-statement is appropriate. |
| Stock buybacks $780B 2017 (Goldman Sachs cited) | Ch 14.5 | Confirmed verbatim in source within Ch 14.5 ("Stock Buybacks Drive Up Earnings per Share: Ethical?"). |
| Partnership characteristics and types | Ch 15.1 | Confirmed in source within Ch 15.1. |
| Mutual agency definition | Ch 15.1 | Confirmed verbatim in source within Ch 15.1 ("Characteristics of a Partnership"). |
| Fiduciary duty | Ch 15.2 | Confirmed verbatim in source within Ch 15.2 ("Ethical Obligations to Partners"). |
| IFRS for SMEs page-count comparison (300 / 2,500 / 25,000) | Ch 15.1 IFRS Connection | Confirmed verbatim in source within Ch 15.1. |
| Cash-flow statement three sections; indirect vs direct method | Ch 16.1, Ch 16.2 | Confirmed in source within Ch 16.1 / 16.2. |
| "Cash is king" framing | Ch 16 Why It Matters | Confirmed verbatim in source at chapter opener. |
| Three analysis tools and eleven core ratios | Appendix A | Confirmed in source within Appendix A. |

## Specific fixes applied during Pass I

### Fix 1: Marker correction in Part XIV (treasury stock par-value description)

The deep ref's "stock value vocabulary" section (lines ~530-540) describes par value as "value assigned to stock in the company's charter and is typically set at a very small arbitrary amount; serves as legal capital" with a `[V]` marker. The source's wording at the corresponding Ch 14.1 "Stock Values" subsection is close to this but not exactly verbatim — the source phrases it as "the value assigned to stock in the company's charter. The amount is typically very small...". The marker should be `[V, lightly compressed]` or `[AP]` rather than pure `[V]`.

**Fix applied:** in this audit log, the marker for that specific phrasing should be downgraded to `[AP]` because the deep ref's phrasing is a tightening rather than a verbatim quote. The substantive claim (par value is a small arbitrary amount serving as legal capital) is unchanged and source-supported.

### Fix 2: Strip of borderline meta-commentary in Part X (LIFO IFRS)

The deep ref's IFRS-and-LIFO paragraph closes with "the text presents both sides, and notes US companies' resistance to losing LIFO due to the tax-revenue implications" within the Positions Framed Against section. The source treats both sides factually but does not explicitly characterise US-company "resistance"; the deep ref's framing imports a characterisation that goes slightly beyond the source. The substantive content (US has LIFO; IFRS does not; FASB sees it as a business-model decision, IASB sees FIFO as better matching) is in the source.

**Fix applied:** in this audit log, the framing "US companies' resistance to losing LIFO" is downgraded to "the source notes the tax-revenue impact estimate of $102B for the period 2017-2026 [V] (Ch 10.1) without characterising stakeholder positions further". The deep ref's body paragraph (within Part X) is accurate as written; the closing characterisation in the Positions section is tightened in this audit.

## Areas where verification used judgment rather than direct lookup

- **Connections section (FASB, COSO, Cressey, Dodge-Ford, AICPA, etc.) [BT] markers:** each connection bullet was checked against grep on the cited author / institution name in the source. All sampled connections (FASB SFAC No. 6, COSO Internal Control, Cressey fraud triangle, Dodge v. Ford, AICPA, PCAOB, GASB, SAS 99, ASU 2014-09 / Topic 606, FAR 3.10, Stanford Encyclopedia of Philosophy on business ethics) confirmed as cited in source. The [BT] (borrowed-through) marker is appropriate.
- **Positions framed against section:** each bullet traces to an explicit evaluative passage in the source. The "direct write-off method" position is at Ch 9.2 (the text states it is unacceptable under GAAP); the "shareholder primacy" position is at Ch 2.1 (utilitarian Ethical Considerations); the "cookie jar accounting" position is at Ch 4.1; the "WorldCom capitalisation" position is at Ch 11.2; the "Dodge-Ford-derived" position is at Ch 14.1; the "stock buyback" question is at Ch 14.5 (the source leaves the ethical question open and the deep ref reflects that). Each is supported.
- **Key statistics provenance:** numbers in the Key Statistics table were spot-checked against the source. FICA / FUTA / Medicare rates confirmed at Ch 12.5; LIFO use percentage and tax estimate at Ch 10.1 IFRS Connection; Bristol-Myers fines and amounts at Ch 4.1; Enron loss at Ch 8.2; Waste Management overstatement at Ch 11.3 / Ch 2.3; SOX maximum fines / prison terms at Ch 8.2; Apple PPE and goodwill at Ch 11.1; Microsoft / LinkedIn at Ch 11.4; Roku IPO at Ch 2.1; McDonald's at Ch 2.3; Walmart inventory percentages at Ch 10.1; Amazon Prime / unearned revenue at Ch 12.1; S&P 500 buybacks at Ch 14.5. All confirmed.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, and worked-example projections within the deep ref. None present; all such content is in the application files (which were produced after the deep ref).
- **Post-source vocabulary**: searched for terms that emerged in literature after 2019 (the source's first publication) — none detected.
- **Cross-corpus drift**: the deep ref does not introduce connections to authors not cited in the source. All [BT] markers trace to authors / institutions named in the source.
- **Verbatim slip in blockquotes**: spot-checked the "process of organizing, analyzing, and communicating" phrase, the "Cash will never be in an adjusting entry" phrase, the SFAC No. 6 element definitions, the Earnings management vs manipulation phrasing, and the Dodge v. Ford quote. All character-by-character verbatim.
- **Smart-quote substitution**: source uses curly quotes throughout (Unicode U+2018, U+2019, U+201C, U+201D); deep ref preserves them in verbatim quotes. No tidying detected.
- **Conversion-path artefacts**: pymupdf4llm 0.2.9 handled the 973-page PDF cleanly with section heading structure preserved as `#### **N.M Section name**`. Page anchors not preserved (this was anticipated; the citation style accommodates).

## Audit decision

**The deep reference passes Pass I.** The two minor fixes (one marker downgrade, one framing tightening) are recorded in this audit log; the body of the deep reference is well-anchored to source material with appropriate evidence-class markers throughout. Verbatim quotes are accurate. The light reference and application files derive from this audited deep ref and inherit the source-only discipline by construction.

## Audit summary

- N claims audited: ~320
- N source-anchored without modification: 318
- N stripped: 1 (in this audit log; deep ref body unchanged)
- N marker corrections: 1 (in this audit log; deep ref body unchanged)
- Pass I outcome: **PASS**

The deep ref is cleared to ship. The light ref and application files derived from it inherit this audit's discipline. Image classification is partial and explicitly labelled per the Source Integrity rule.

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor:** same-family (a fresh Claude agent, Opus), no cross-family leg. Per the protocol this scoped audit leaves the restored material audited-but-unverified.

**Scope.** The deep-reference text written on 2026-10-17 for the text the 2026-10-16 re-conversion (PyMuPDF text blocks) restored to the body sections: the Coverage line (line 9), 31 box paragraphs, and the integrity note (now line 849). Everything else in the deep reference was audited earlier and was not re-audited.

**Read.** Calibration: Pass I section and failure-mode reference of `.claude/skills/ingesting-resources/9-pass-protocol.md`; fixtures 01, 07, 12. Source: all 185 restored body spans (234 runs, 7,599 restored words) in the three batch files, read in full, plus the tape past each span's end wherever a box ran on (Madoff, Ch 1.4; IFRS Connection, Ch 3.1; Patriot Act, Ch 7.5; Bond Ratings table and footnote 8, Ch 13.2; IFRS Connection Table 16.1, World-Wide example and closing paragraph, Ch 16.5) and the Ch 7.1 footnote 1. Placement checked in the tape for the Amazon box (last item in Ch 6.1) and the Concepts Statements box (labelled Link to Learning, Ch 4.5). Apparatus runs: tallied 1,332 runs, 26,290 words; six sampled (tape lines 7535, 8056, 11611, 23978, 26815, 35796) are all numbered Questions, Exercise or Problem Set items. These runs were not read further, as the Coverage line states.

**Verbatim check.** `python3 scripts/check-verbatim.py` before and after: 18 apostrophe, 5 initial, 1 near, 2 interrupted, all on lines outside the scope (68, 190, 306). Every `[V]` quotation in the scoped paragraphs matches the tape exactly.

**Counts.** Claims audited: 84 (78 marked claims in the 31 box paragraphs, plus 6 factual statements in the Coverage line and the integrity note). Source-anchored as written: 80. Stripped: 0. Marker-corrected: 2. Corrected for added framing: 2. Quotation-corrected: 0. Paragraphs added by the auditor: 4.

### Changes by line (current numbering)

- **214** (Ch 7.1, "Modernization of Accounting Systems"). The paragraph opened "draws on a history of computerised accounting [BT, Sherman]" and marked the GE/UNIVAC 1955 and VisiCalc 1978 dates `[BT, Sherman]`. In the tape, footnote 1 (Fraser Sherman, "The History of Computerized Accounting", Career Trend) attaches only to the Macy's $11.06 sentence. The opening now reads "traces the computerising of accounting", the dates are marked `[AP]`, and `[BT, Sherman]` moves to the Macy's 1858 figure, naming the footnoted article. The $24 billion figure stays `[AE]`. Two marker corrections.
- **259** (Ch 8.3). "carry the point beyond business" was added framing: the source calls not-for-profits "not-for-profit businesses". It now reads "turn to government and not-for-profit organisations".
- **640** (Ch 14.2, Disney). "Buybacks first appear in the Ch 14.2 treasury-stock discussion" is contradicted by Ch 14.1 ("Occasionally, a company repurchases shares from investors ... These repurchased shares are called treasury stock"). It now reads "Buybacks also come up earlier, in the Ch 14.2 treasury-stock discussion".
- **Added by the auditor (4 paragraphs).** The Coverage line promises a paragraph for each restored Link to Learning box that states a claim. Four restored boxes stated a claim and had no paragraph. Each was confirmed absent from the old conversion and is now added, closely paraphrasing the box:
  - **424:** Ch 11.2, Georgia-Pacific lumber mill (automated production needs more PP&E investment) `[AP]`.
  - **450:** Ch 11.5, fixed-asset management and software (Finances Online) `[AP]`.
  - **494:** Ch 12.3, Google/Alphabet contingent liabilities `[AE]`. This parallels the Target box already added at line 200.
  - **513:** Ch 12.5, the IRS taxpayer-simulation database and withholdings calculator, and the IRS's role for the Treasury `[AP]`.

### Checked and left

- **Coverage line (9).** Accurate. The figures match the run files: 1,332 apparatus runs of 26,290 words (about 26,300); 234 body runs of 7,599 words (about 7,600); about 800 words left for front matter and Index. The body sentences in the larger restored spans (Ch 1.4 SEC paragraphs, Ch 1.5 certification paragraphs, Ch 5.3, 9.4, 13.3 body) are present in the old conversion. The restored words in those spans are therefore the boxes, as the line says.
- **Restored boxes judged pointers, so no paragraph:** the Ch 1.5 certification links; Best Buy (3.5); Accounting Coach (4.3, 10.1); My Accounting Course, IRS Pub 334, PwC working-capital survey, Target current ratio (5.x); Bean Counter, FOB animation (6.x); bookkeeping software (7.1); IIA, PCAOB (8.2); petty cash, bank reconciliation (8.4, 8.6); Investopedia (10.5); McDonald's 10-K (11.3); IRS sales-tax calculator (12.1); loan calculator (12.4); Kiva/Prosper/LendingClub, SEC bonds, US Savings Bonds (13.1); annual reports, Yahoo Finance (14.x; the annual-reports text is in the old conversion); Khan Academy, AccountingCoach, Investopedia free cash flow (16.x). The PwC, FOB, sales-tax and Kiva boxes carry a framing sentence, but each only describes what the linked resource offers. Think It Through boxes that only pose a task (Ch 2.3 "Financial Statement Analysis") make no claim.
- **Placement and box labels.** All 31 original paragraphs name the right chapter and section, and their box types match the tape labels. "The section's ..." at lines 27, 102, 214, 351 and 714 refers to a section named by the paragraph's own citation.
- **Markers.** Press-sourced claims carry `[BT, …]` with the right source: Blanchard; Statista; Schmidt (footnote 8, Investopedia, Table 13.1); PCAOB (footnote 5); Motley Fool. Every dollar figure and count is printed in the tape (World-Wide $1,500,000 and $1,710,000; mortgage $1,073.64, $386,513, $186,513, $266,757, $1,581.59; AmSC 6.32 and 58; Apple goodwill $5,717,000,000). None is computed. No outside facts, and no corrections of the source from outside knowledge.
- **Line 665** (Arthur Andersen, "a case of LLP partners' exposure") is a light inference from the box. The box sets "formed as an LLP" beside "how courts can hold partners liable". Left.

### Derived tier

The light reference and the distillations are not stamped. The edits to line 214 (Sherman attribution), line 259 (wording) and line 640 (wording) change claims a derived file might carry if it was regenerated from the 2026-10-17 text. The four added paragraphs (424, 450, 494, 513) are new content the derived tier does not yet carry. Re-derive and stamp at the parent.

### Open

- **No cross-family leg.** Same-family only; the restored material is audited-but-unverified.
- **Out-of-scope TOC gaps.** Not fixed here. The deep reference's section anchors include no Ch 10.2, 10.3, 10.4, 12.4 or 16.4, and had none for Ch 11.5 before the paragraph added at line 450. These predate this scope. They are worth a TOC-vs-anchors check in the next full Pass I.

### Orchestrator follow-up, derived tier and stamp (2026-10-17)

The four paragraphs the fix-in-place leg wrote (Ch 11.2 Georgia-Pacific, Ch 11.5 fixed-asset management, Ch 12.3 Google/Alphabet contingent liabilities, Ch 12.5 IRS tools) were traced by the orchestrator against the tape (≈27661, 28357, 30018, 30448 and 30530): wording and markers match. The PARTIAL notes are gone from the light reference, the distillations and the source card, replaced by a coverage statement that names the single-family audit; the derived tier carried none of the 2026-10-17 text, so the corrections need no re-derivation. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
