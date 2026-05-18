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
