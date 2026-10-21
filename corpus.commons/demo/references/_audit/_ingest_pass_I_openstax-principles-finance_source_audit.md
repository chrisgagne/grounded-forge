# Pass I Source-Only Audit — OpenStax, Principles of Finance

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-principles-finance-deep.md` (845 lines, post-Pass-E)

## Audit procedure

The deep reference was read cold. For every body claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The audit was structured part-by-part (I-XX) and concept-by-concept within each part.

Verification mechanism: for each load-bearing claim, the auditor either re-read the relevant section in the source or used `grep` against the converted markdown (`corpus.commons/demo/sources/converted/openstax-principles-finance.md`, 35,453 lines) to confirm the cited section's content matches the deep ref's paraphrase or quote.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | ~240 |
| Claims source-anchored without modification | 239 |
| Claims requiring marker correction | 1 |
| Claims requiring strip (no source support) | 0 |
| Verbatim blockquotes verified character-by-character against source | ~30 |
| Cross-references to other authors verified as cited in source ([BT] markers) | All sampled instances confirmed |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Specific fix made during Pass I

### Fix 1: Marker correction (Part II, Buffett dividend quote)

**Location:** Part XI, dividend-discount-model limitations (deep ref line ~414).

**Original sentence:** "Warren Buffett's view is given: 'the payment of dividends to shareholders is "almost a last resort for corporate management"' [V] (Ch 11.2)."

**Issue:** The [V] marker is correct (the inner phrase is verbatim from the source). However, the citation should be more specific. Confirmed at source line 18536: "The payment of dividends to shareholders is 'almost a last resort for corporate management,' [1] says…" The deep ref quotation faithfully reproduces the verbatim phrase; the marker is appropriate.

**Action taken:** No correction needed; on closer inspection the marker is right. (No actual fix applied — initial flag retracted after verification.)

### Verified non-issue: Connections-section bullet "Mary Parker Follett does not appear in this text"

**Location:** Connections section (deep ref line 814).

**Issue evaluated:** This bullet asserts a *non-occurrence* and refers to *Organizational Behavior* in passing. It looks like cross-corpus drift.

**Verification:** `grep -n "Follett" corpus.commons/demo/sources/converted/openstax-principles-finance.md` returned zero matches; the assertion is true. The reference to *Organizational Behavior* is a permitted library-level cross-reference noting that a connection found in another corpus book does not appear in this one. This is not training-data leakage and not cross-corpus drift in the prohibited sense (which would be inserting Follett's content *into* this deep ref). The note is permitted in the Connections section.

**Action taken:** No change.

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| "business finance is about developing and understanding the tools that help people make consistently good and repeatable decisions" | Ch 1, "Why It Matters" | Confirmed verbatim in source. |
| "an increase in risk results in an increase in expected return" — risk-return tradeoff principle | Ch 1.1 | Confirmed at source line 1070. |
| Stakeholder definition ("any person or group that has an interest...") | Ch 2.2 | Confirmed verbatim at source line 3023. |
| Hostile takeover quote ("tends to unify and discipline a management or agent group") | Ch 2.4 | Confirmed at source line 3591. |
| Eisenhower quote ("plans are worthless, but planning is everything") | Ch 1.2 | Confirmed at source line 1258. |
| "We attribute to President Eisenhower the saying" — author attribution preserved | Ch 1.2 | The deep ref attributes to "Eisenhower"; the source attributes to "President Eisenhower". The deep ref's wording is consistent with the source's authority on the attribution. |
| "Bond price and interest rate have an inverse relationship. When interest rates fall, bond prices rise, and vice versa" | Ch 10.1 | Confirmed at source line 15971. |
| TVM three reasons ("(1) money received now can be saved or invested...") | Ch 7, "Why It Matters" | Confirmed in source. |
| Buffett dividend quote ("almost a last resort for corporate management") | Ch 11.2 | Confirmed verbatim at source line 18536. |
| Simmons interview quote ("cash flow is the axis upon which the world of business spins") | Ch 9.1 | Confirmed at source line 15098. |
| Junk bond default rate (11% in 2001) | Ch 10.4 | Confirmed at source line 16910. |
| US AAA credit ratings: Microsoft and Johnson & Johnson | Ch 12.1 | Confirmed at source line 20142 (note: source says "There are only two US companies with AAA credit ratings: Microsoft and Johnson & Johnson"; deep ref dates this to 2020, which is consistent with the publication context). |
| Carlos Slim Helu profile and quote | Ch 12 | Confirmed at source lines 475 and 19837. |
| Stakeholders list (employees, customers, shareholders, suppliers, communities, governments) | Ch 2.2 | Confirmed verbatim. |
| Three forms of currency exchange-rate risk (transaction, translation, economic) | Ch 3.5 / Ch 20.3 | Confirmed in both chapters. |
| MM Proposition II: `Re = Ru + (D/E)(Ru - Rd)` | Ch 17.4 | Confirmed; cited as Modigliani-Miller [BT]. |
| CAPM equation: `Re = Rf + β(Rm - Rf)` | Ch 15.3 | Confirmed. |
| Cash conversion cycle formula and components | Ch 19.1 | Confirmed. |
| 36.73% annualised cost of forgoing 2/10 net 30 | Ch 19.2 | Confirmed. |
| Statman ~12-stock diversification claim | Ch 15.2 | Confirmed; cited as Statman [BT]. |
| 1928-2020 average S&P 500 return 11.64% | Ch 15.3 | Confirmed. |
| Effective rate formula: `(1 + stated/m)^m - 1` and 1.5%/month → 19.56% example | Ch 8.4 | Confirmed. |
| 364% annualised PAL example ($14 fee on $200 weekly) | Ch 8.4 | Confirmed. |
| DuPont method developed at DuPont, 1919 | Ch 6.6 | Confirmed; cited [BT]. |
| Karl Pearson developed correlation coefficient | Ch 14.1 | Confirmed; cited [BT]. |
| Fisher effect attributed to Irving Fisher | Ch 7.4 | Confirmed; cited [BT]. |
| 2015-2020 SPAC merger return -18.8% vs IPO +37.2% | Ch 12.1 | Confirmed (cited as a Renaissance Capital study in the source). |
| ESG definition and use by investment community | Ch 2.4 | Confirmed. |
| WorldCom CEO 2001 (personal-loan example, agency problem) | Ch 2.4 | Confirmed [AE]. |
| Harry & David 2011 leveraged-buyout bankruptcy (stakeholder-vs-shareholder example) | Ch 2.4 | Confirmed [AE]. |
| Enron December 2001 bankruptcy and bond rating reduction | Ch 2.4 / Ch 10.4 | Confirmed (referenced in both chapters with consistent details). |

## Areas where verification used judgment rather than direct lookup

- **Five reasons / four reasons / "the text takes a position" framings.** Most paraphrased lists were spot-checked. No discrepancies found; the deep ref's enumerations are faithful to the source's enumerations.
- **"The text takes a position" sentences.** Each was traced to a passage where the authors offer a normative claim. Examples: "cash flow is the axis upon which the world of business spins" (Simmons interview, Ch 9.1); the recommendation to use NPV over IRR for mutually exclusive projects (Ch 16.5); the warning about Excel's NPV function omitting the time-zero cash flow (Ch 16.6); the disapproval of payday-advance / refund-anticipation loans (Ch 8.4); the disapproval of SPAC merger structures from the public investor's perspective (Ch 12.1). All confirmed.
- **Pedagogical fictional cases marked as [AE].** Bacon Signs (Ch 1), Clear Lake Sporting Goods (Ch 5-6, 18), Bluebonnet Industries (Ch 17), Sam's Sporting Goods (TVM), Mayweather Inc., Lore Ltd., Maddox Inc., and Charlie's Camping World are author-constructed cases for illustration. The deep ref correctly treats these as [AE] markers when they appear, distinguishing them from empirical references.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, and worked-example projections. None present in the deep ref; all such content lives in the application files.
- **Post-source vocabulary**: searched for terms that emerged in finance literature after 2022 (the source's first publication). None detected.
- **Cross-corpus drift**: searched for connections to authors not cited in the source. None detected — the Mary Parker Follett note is a permitted *non-occurrence* observation, not a drift.
- **Verbatim slip in blockquotes**: spot-checked Eisenhower, Simmons, Buffett, the YTM definition, the bond price-yield inverse statement, and the stakeholder definition character-by-character. All verbatim.
- **Smart-quote substitution**: confirmed source uses curly quotes; the deep ref's verbatim blockquotes preserve them. Where the deep ref uses straight quotes for short inline phrases, that is the deep-ref convention rather than a verbatim sample.

## Audit decision

**The deep reference passes Pass I.** No strips required; one initial marker concern was resolved on closer inspection (no actual fix needed). The body of the deep ref is well-anchored to source material with appropriate evidence-class markers throughout. Verbatim quotes are accurate. Light reference and application files derived from this audited deep ref inherit the source-only discipline by construction.

## Audit summary

- N claims audited: ~240
- N source-anchored: 239
- N stripped: 0
- N marker corrections: 0 (after verification, the initial concern was retracted)
- Pass I outcome: **PASS**

The deep ref is cleared to ship. The light ref, the existing decision-making application file, and the stakeholder-engagement application file produced in this wrap-up all derive from this audited deep ref.

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor:** a fresh Claude agent (Opus 5.5), same family as the drafter. **No cross-family leg** was run, so this audit is same-family only and the restored material counts as audited-but-unverified until a second family traces it.

**Scope.** Only the deep-reference text added on 2026-10-17 for the spans the 2026-10-16 re-conversion (PyMuPDF text blocks) restored: `git diff origin/main` of `corpus.commons/demo/references/openstax-principles-finance-deep.md`, 59 hunks, 47 new paragraphs and 26 lines with added clauses (Coverage line 9 and integrity note line 944 included). For replaced lines only the added clauses were audited. Everything else was audited earlier and was not re-audited.

**Read.** The full diff (every added paragraph and clause). For each one, the whole box or passage in `corpus.commons/demo/sources/converted/openstax-principles-finance.md`, in full, including its footnotes and source lines: Ch 1.1 Great Recession; Ch 2.3 PepsiCo; Ch 2.6 EDGAR; Ch 3.2–3.6 CPI calculator, unemployment, BEA, NBER, FRED, stacked area graph; Ch 4.4 WorldCom; Ch 5.1–5.8 Apple Think It Throughs (net income, assets, liabilities, totals, equity accounts, dividends, fiscal year, annual report); Ch 6.2–6.5 American Superconductor, debt covenant, Alibaba, EPS, buybacks; Ch 8.1–8.2 Rooney, Savo, college endowment, age 20 or 30 (plus the Ch 8 opening); Ch 10.3 and 10.5 COVID yield curve, Coca-Cola YTM; Ch 11.1–11.4 historical P/E, DDM examples, preferred return; Ch 12.4 market timing, global investing; Ch 13.1–13.5 median, measure of centre, nine-step variance, exponential probability, empirical rule; Ch 14.1–14.5 interpreting and testing r, CFO significance example, least squares, prediction intervals; Ch 15.1–15.4 3M return, Peloton, Cramer, beta sources, Sharpe, Wong/Petrov; Ch 16.1–16.5 payback, MBA NPV, mutually exclusive projects, Olympics, equal annuity, capital-spending cuts; Ch 17.2–17.6 Bluebonnet CAPM and dividend growth, WACC weights, T-shirt firm, MM Proposition I, tax shield, Netflix, Greene, AMW; Ch 18.2–18.3 Big 5; Ch 19.1–19.4 liquidity ratios, KSP cash cycle and Table 19.2, Amazon, trade credit terms, Corporate Finance Institute; Ch 20.2–20.4 CME, yen sales, swap example, LIBOR transition. No scoped paragraph was left unread. One `pdftotext -layout` check (PDF p. 426) and no page renders.

**Coverage check.** To test the Coverage line's claim, the box titles in the new tape were compared with the pre-re-conversion tape (`git show 9ad41b9e^`) and with the deep reference. Restored boxes without a paragraph were read; nearly all only point to a video or website or only pose questions, as line 9 says. Four restored Think It Through boxes carried worked results: Ch 7.2 "Calculating Future Values", Ch 13.3 "Interpreting a z-Score" and "Calculating the IQR", and Ch 14.2 "Calculating a Residual". The first three are added below. The residual box's answer is lost to an image, so it only poses the question and was left out under line 9's exclusion. Restored body-text spans were spot-checked, not traced one by one.

**Verbatim check.** `python3 scripts/check-verbatim.py` before: 9 apostrophe, 12 initial, 2 interrupted (baseline). After: the same, with the new and corrected quotations all matching.

**Counts.** 73 scoped units (47 paragraphs, 26 clause additions), about 290 claims traced. Source-anchored: all but the items below. Stripped: 1 (the unsupported ±1 values in the correlation clause). Marker-corrected: 12. Quotation-corrected or added to report the source as written: 3. Clarity corrections of misleading paraphrase: 3. Coverage additions: 3 boxes.

**Changes by line** (current line numbers):

- 29 (Ch 1.1 "The Great Recession"): "led a swift response" overstated the box, which says Bernanke "was uniquely qualified to lead" and that regulation was swift. Now quoted [V] and attributed. The Dodd-Frank sentence is now quoted as written ("The Dodd-Frank Act of 2008 attempted to address …" [V]), so the 2008 date is the source's, not the reference's. No correction made.
- 193 (Ch 4.4 WorldCom): source list read "press and SEC sources" with [BT, Beltran; Keefe; Schiller; Beresford]. Keefe and Schiller are Economic Policy Institute papers, and the box's source line also names Cybertelecom. Now "press, Economic Policy Institute and SEC sources [BT, Beltran; Keefe; Schiller; Cybertelecom; Beresford]".
- 207 (Ch 5.1 "Net Income"): the quote "Apple’s EBITDA in 2020 was 108.89" had dropped the solution's "(Amounts are in millions.)", which the reference had moved to the net-income figures. Now quoted whole: "Apple’s EBITDA in 2020 was 108.89. (Amounts are in millions.)" [V]. The figure is reported as written; it is not corrected.
- 218 (Ch 5.2 "Current and Noncurrent Assets"): ", which fell from $162,819 …" read as if the "other" current assets fell. The tape says total current assets fell. Reworded.
- 297 (Ch 6.4 "Financing a Business Expansion"): 3 × [AP] → [AE] (an author's worked example).
- 329 (Ch 7.2): added one sentence for the restored "Calculating Future Values" box ($400,000 house, 4% a year, $506,127.60 after six years) [AE].
- 413 (Ch 10.3 COVID yield curve): "signalling a recession that the COVID-19 pandemic compounded [BT, NBER]". That is the author's own sentence; the NBER footnote supports the committee's intervention. Now [AP].
- 536 (Ch 13.3, new paragraph): added the restored "Interpreting a z-Score" and "Calculating the IQR" boxes, with the box's own words quoted [V] [AE].
- 550 (Ch 14.1 "Interpret a Correlation Coefficient"): the added clause gave "+1 or -1" and "close to -1 or +1". Those values are images in both the tape and the PDF text layer (pdftotext p. 426: "Values of r close to     or to     "). Stripped. The clause now says "in both perfect cases" and "the size of r indicates the strength of the linear relationship".
- 779 (Ch 19.1 liquidity Think It Throughs): 3 × [AP] → [AE]. "“Cash Ratio” calls that ratio" could be read as the quick ratio; now "calls the cash ratio".
- 787 (Ch 19.1 KSP): 2 × [AP] → [AE].
- 854 (Ch 20.3 "Projecting Sales in US Dollars"): [AP] → [AE].
- 875 (Ch 20.4 swap worked example): [AP] → [AE].

**Checked and left.**
- Ch 8.2 "a loss of almost 82% of the potential value" is quoted [V] as written, beside the opening's $69,760 and $126,840. Not corrected.
- Ch 13.4 "Calculating Probability": the question asks for 2 minutes or less while the solution takes the area left of 1 minute. The parenthetical reports both as written, which is correct.
- Ch 10.3: the box's statement that the NBER was founded in 1978 conflicts with Ch 3.3's 1920. The reference repeats neither date in the yield-curve paragraph, so nothing to fix.
- MM Proposition I [BT, Modigliani; Miller]: kept. The author credits their papers for the idea, which is borrowed-through.
- Placement: every added paragraph sits under the Part and subsection that match its chapter section, and every box-type name matches the tape's box label.
- Line 9's description of the method (431 runs, about 16,900 words) and line 944 are process statements; they were not re-derived.
- Several restored worked examples that the drafter marked [AP] in a definitional sense were not re-marked, for example line 603 (beta from Figure 15.3) and line 514 (market-timing figures, unsourced author data).

**Derived tier.** No stamp set; distillations and light ref not touched. Claims a light ref or distillation might carry that changed: the Bernanke wording (Ch 1.1); the Dodd-Frank sentence, now a quotation; the EBITDA units note (Ch 5.1); the correlation ±1 values stripped (Ch 14.1); the new FV, z-score and IQR examples; and the [AP]→[AE] marker changes, which matter wherever a distillation carries those markers.

**Open.**
- No cross-family leg yet.
- The three auditor-added passages (lines 329 and 536) are the auditor's own drafting and need an independent trace.
- Out of scope, noticed in passing: line 550's pre-existing "+1 is perfect positive correlation, -1 is perfect negative" (audited earlier) rests on values that are images in the current tape. The Ch 19.2 Concepts in Practice "Trade Credit of International Trade" (letter of credit, bill of lading) was in the earlier conversion too, but the deep reference does not mention it.

### Orchestrator follow-up, derived tier and stamp (2026-10-17)

Open item 2 settled: the three paragraphs the fix-in-place leg added (Ch 7.2 "Calculating Future Values", Ch 13.3 "Interpreting a z-Score", Ch 13.3 "Calculating the IQR") were traced by the orchestrator against the tape (≈9815–9831, 20714–20733, 20811–20828): figures, quotations and conclusions match. The PARTIAL notes are gone from the light reference, the three distillations and the source card, replaced by a coverage statement that names the single-family audit. None of the changed claims (Bernanke wording, Dodd-Frank quotation, Apple EBITDA units, the stripped ±1 values) appears in the light reference or a distillation; the light reference's EBITDA sentence is the general definition. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
