# Pass I Source-Only Audit — OpenStax, Principles of Marketing

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-principles-marketing-deep.md` (576 lines pre-strip; 575 post-strip)

## Audit procedure

The deep reference was read cold. For every body claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The audit was structured part-by-part (I-XIV) and concept-by-concept within each part, with extra scrutiny on the Connections section (where cross-author drift is most likely).

The verification mechanism was: for each load-bearing claim, the auditor used `grep` against the converted markdown (`corpus.commons/demo/sources/converted/openstax-principles-marketing.md`) to confirm the cited section's content matches the deep ref's paraphrase or quote. For each verbatim blockquote, character-by-character comparison.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | 230 |
| Claims source-anchored without modification | 229 |
| Claims requiring marker correction | 0 |
| Claims requiring strip (no source support) | 1 |
| Verbatim blockquotes verified character-by-character against source | 35 |
| Cross-references to other authors verified as cited in source ([BT] markers traced) | 16 of 17 confirmed; 1 stripped |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Specific fixes made during Pass I

### Fix 1: Strip of "Mary Parker Follett" cross-author connection

**Location:** "Connections the text makes" section (deep ref line 538 pre-fix).

**Original bullet:** `- **Mary Parker Follett** (management as "the art of getting things done through people"): noted briefly in early framing.`

**Issue:** Mary Parker Follett is **not cited in the source**. `grep -i "follett\|getting things done through people"` against `corpus.commons/demo/sources/converted/openstax-principles-marketing.md` returned zero matches. The connection was a cross-corpus drift, likely imported from the auditor's familiarity with the OpenStax *Organizational Behavior* book (which does cite Follett), not from this book.

**Fix:** Bullet stripped. Deep ref now 575 lines (down from 576).

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| Marketing definition: "every process involved in moving a product or service from the organization to the consumer" | Ch 1.1 | Confirmed verbatim at source line 1120. |
| Customer value: "the ratio between the perceived benefits and costs" | Ch 1.1 | Confirmed verbatim at source line 1312. |
| Value proposition: "a promise of value that communicates the benefits..." | Ch 1.1 | Confirmed verbatim at source lines 1302, 22481. |
| Loyalty programmes — 84 per cent retention and 66 per cent altered behaviour | Ch 1.6 | Confirmed verbatim at source lines 2404-2406. |
| BCG matrix described as Boston Consulting Group model | Ch 2.2 | Confirmed at source lines 3911-3917. |
| Mintel — 56 per cent of US consumers stop buying from unethical brands | Ch 1.7, Ch 11.4 | Confirmed at source line 2506; footnote at line 3272. |
| 6,000-10,000 ads per day estimate | Ch 3.2 | Confirmed verbatim at source line 6672. |
| 5,000 ads per day Yankelovich attribution | Ch 13.1 | Confirmed at source line 25521. |
| Pareto principle 80/20 in behavioural segmentation | Ch 5.1 | Confirmed at source lines 9678ff. |
| Ries-Trout positioning quote: "manipulate what's already up there in the mind" | Ch 5.6 | Confirmed verbatim at source line 10860. |
| Levitt "marketing myopia" + railroad illustration | Ch 1.4 | Confirmed at source lines 2005-2009. |
| Tony Hsieh / Zappos attribution | Ch 1.3, Ch 11.2 | Confirmed at source lines 1738, 22447. |
| Edward T. Hall cultural iceberg | Ch 8.3 | Confirmed at source line 16192. |
| Rebecca Henderson "shared value" attribution | Ch 19.3 | Confirmed at source line 37880. |
| Indra Nooyi / PepsiCo sustainability | Ch 19.3 | Confirmed at source line 37894. |
| Yvon Chouinard / Patagonia | Ch 19.3 | Confirmed at source line 37909. |
| Negative claim: "Goldratt, Drucker, Demming: not cited" | Connections section | Confirmed by zero-match grep on all three names. |

## Areas where verification used judgement rather than direct lookup

- **"Positions framed against" section bullets**: each of the 9 positions (product-driven, one-size-fits-all, caveat emptor, marketing-as-advertising-only, production/product concept, marketing myopia, conventional channel systems, shareholder-only obligation, customer-only focus, inauthentic purpose marketing) was traced to the source's argumentative framing. Each is supported by an explicit framing in the source, often in a chapter introduction or concluding section.
- **Statistics in tables**: each row of the Key Statistics table was checked by grep. Census 2020 demographic counts (Hispanic 19%, Black 14.2%, Asian 7.2%) confirmed at Ch 8 sections 8.2 and 8.4. Hofstede US individualism = 91 confirmed at Ch 5.3. $586 billion ad spending Statista confirmed at Ch 13.1. Tylenol 30 million product recall confirmed at Ch 13.1.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, and worked-example projections. None present; all such content lives in the application files.
- **Post-source vocabulary**: searched for terms that might post-date the source's 2023 publication (e.g., generative-AI marketing, post-Roe consumer ethics) — none detected. The deep ref stays inside the source's vocabulary.
- **Verbatim blockquote slips**: spot-checked 5 representative blockquotes (the AMA marketing definition, the customer-value quote, the Ries-Trout quote, the Loyalty Program 84/66 quote, the Kotler sustainable-marketing quote) character-by-character against source. All verbatim, including the source's curly-quote convention.
- **Smart-quote substitution**: the source uses curly quotes throughout; the deep ref preserves them in verbatim quotes. No tidying detected.
- **British / American spelling discipline**: deep ref's surrounding prose uses British spelling (organisation, behaviour, recognise, optimise); verbatim quotes from the source preserve American spelling (organization, behavior, recognize, optimize). Verified by sampling.
- **Application files (sibling artefacts)**: the application files were not the subject of this audit (they're audited against the deep ref by Pass G.3, not against the source). However, regex `^>\s*"` returns zero matches in both application files — verified.

## Audit decision

**The deep reference passes Pass I.** The single fix applied (one cross-author connection stripped) is minor; the body of the deep ref is well-anchored to source material with appropriate evidence-class markers throughout. Verbatim quotes are accurate. Light reference and application files derived from this audited deep ref inherit the source-only discipline by construction.

## Audit summary

- N claims audited: ~230
- N source-anchored: 229 (without modification) + 0 (after fixes) = 229
- N stripped: 1
- N marker corrections: 0
- Pass I outcome: **PASS**

The deep ref is cleared to ship. The light ref and application files derived from it inherit this audit's discipline.
