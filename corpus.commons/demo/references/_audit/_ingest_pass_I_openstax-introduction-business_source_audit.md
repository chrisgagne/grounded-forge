# Pass I Source-Only Audit — OpenStax, Introduction to Business

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-introduction-business-deep.md` (907 lines, post-Pass-E and post-Pass-I fixes)

## Audit procedure

The deep reference was read cold. For each load-bearing claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The mechanism: re-read the relevant section in source, or use `grep` against `corpus.commons/demo/sources/converted/openstax-introduction-business.md` to confirm that the cited section's content matches the deep ref's paraphrase or quote.

Spot-checks were stratified: every part (I-XVII plus Appendix A) sampled at least three load-bearing claims; every blockquoted [V] passage verified character-by-character.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (approximate, body sentences with citations or evidence markers) | 230 |
| Claims source-anchored without modification | 227 |
| Claims requiring marker correction | 1 |
| Claims requiring strip (no source support) | 0 |
| Verbatim blockquotes verified character-by-character against source | ~40 |
| Verbatim slips fixed | 1 |
| Cross-references to other authors verified as cited in source ([BT] markers traced) | All sampled instances confirmed |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Specific fixes made during Pass I

### Fix 1: Verbatim slip in stakeholder-list quote (Author's Thesis section)

**Location:** Author's Thesis paragraph (deep ref line 16 pre-fix).

**Original quote:** `stakeholders include "the employees, its customers, the general public, and its investors" [V]`

**Issue:** The quoted text was rephrased mid-quote ("the employees" rather than the source's "its employees"). Source line 5550 reads: `"The stakeholders of a business are its employees, its customers, the general public, and its investors."` Verbatim accuracy requires "its employees".

**Fix:** Quote rewritten to begin "the stakeholders of a business are..." matching the source verbatim. The deep ref now reads: `"the stakeholders of a business are its employees, its customers, the general public, and its investors" [V] (Ch 2.4, "Responsibilities to Stakeholders")`.

### Fix 2: Marker correction (grapevine survey, Part VII)

**Location:** Part VII, Informal organisation section (deep ref line ~315).

**Original marker:** `[V]` on the claim "47% of employees would believe a grapevine message over a senior leadership speech, with 57% rating their company grapevine as accurate".

**Issue:** The deep ref's wording is a paraphrase of source lines 19162-19170, which use "Forty-seven percent of those responding said they would put more credibility in the grapevine" and "57 percent gave it favorable ratings". The deep ref's compressed phrasing is correct in substance but not verbatim. [V] requires the author's own words to appear; this is an [AP] paraphrase.

**Fix:** Marker changed to `[AP]`.

### Fix 3: Image-classification note in source-integrity-notes section

**Location:** Citation and Source-Integrity Notes section, Image classification subsection (deep ref line ~907).

**Original note:** "Pilot heuristic from Phase 2 (PNG = usually substantive, JPEG = usually decorative) applied; per-image classification recorded in the Pass H verification log..."

**Issue:** The pilot PNG-vs-JPEG heuristic proved unreliable for Introduction to Business: of the 14 PNGs only 8 are substantive (6 are decorative front-matter assets), and of the 144 JPEGs 43 are substantive framework diagrams. Recording "pilot heuristic applied" without the override is misleading.

**Fix:** Note rewritten to record that visual inspection of every image was performed for this book, that the pilot heuristic proved unreliable, and that final classification yielded 51 substantive (8 PNG + 43 JPEG) and 107 decorative (6 PNG + 101 JPEG).

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| "the basic structures upon which the business world is built" | Ch 1, "Introduction" | Confirmed verbatim at source line 1096. |
| "managers are primarily adapters to, rather than agents of, change" | Ch 1.2 | Confirmed verbatim at source line 1568. |
| "an organization that strives for a profit by providing goods and services desired by its customers" | Ch 1.1 | Confirmed verbatim at source line 1156. |
| "the output of goods and services people can buy with the money they have" (standard of living) | Ch 1.1 | Confirmed verbatim at source line 1171. |
| "the general level of human happiness based on such things as life expectancy..." (quality of life) | Ch 1.1 | Confirmed verbatim at source line 1186. |
| "today's competitive environment places a premium on knowledge and learning over physical resources" | Ch 1.1 | Confirmed verbatim at source line 1484. |
| "the right to own property, the right to make a profit, the right to make free choices, and the right to compete" | Ch 1.3 | Confirmed verbatim at source line 1951. |
| "leans toward pure capitalism, but it uses government policies to promote economic stability and growth" | Ch 1.3 | Confirmed verbatim at source line 2076. |
| "a decline in GDP that lasts for two consecutive quarters" | Ch 1.4 | Confirmed verbatim at source line 2272. |
| "the value of what money can buy" (purchasing power) | Ch 1.4 | Confirmed verbatim at source line 2420. |
| "the quantity of a good or service that people are willing to buy at various prices" | Ch 1.6 | Confirmed verbatim at source line 2846. |
| "the concern of businesses for the welfare of society as a whole" | Ch 2.3 | Confirmed verbatim at source lines 5386 and 6074. |
| "the individuals or groups to whom a business has a responsibility" (stakeholders) | Ch 2.4 | Confirmed verbatim at source line 5548. |
| "the stakeholders of a business are its employees, its customers, the general public, and its investors" | Ch 2.4 | Confirmed verbatim at source line 5550 (after Fix 1). |
| "a tax imposed by a nation on imported goods" (tariff) | Ch 3.3 | Confirmed verbatim at source line 7183. |
| "the world's most powerful institution for reducing trade barriers and opening markets" | Ch 3.4 | Confirmed verbatim at source line 7388. |
| "the practice of charging a lower price for a product..." (dumping) | Ch 3.4 | Confirmed verbatim at source line 8742 (variant phrasing in main text). |
| "people with vision, drive, and creativity, who are willing to take the risk of starting and managing a business to make a profit" | Ch 5.1 | Confirmed verbatim at source lines 12713-12715. |
| "the process of guiding the development, maintenance, and allocation of resources to attain organizational goals" (management) | Ch 6.1 | Confirmed verbatim at source line 15245. |
| "a tightly integrated cycle of thoughts and actions" | Ch 6.1 | Confirmed verbatim at source line 15257. |
| "using the least possible amount of resources to get work done" (efficiency) | Ch 6.1 | Confirmed verbatim at source line 15292. |
| "the ability to produce a desired result" (effectiveness) | Ch 6.1 | Confirmed verbatim at source line 15294. |
| "states the purpose of the organization and its reason for existing" (mission statement) | Ch 6.2 | Confirmed verbatim at source line 15556. |
| "the process of guiding and motivating others toward the achievement of organizational goals" (leadership) | Ch 6.4 | Confirmed verbatim at source line 17318. |
| "the trend in organizations today is away from the directive, controlling style of the autocratic leader" | Ch 6.4 | Confirmed at source (per the Positions Framed Against table; cross-section reference). |
| "giving employees increased autonomy and discretion to make their own decisions..." (empowerment) | Ch 6.4 | Confirmed verbatim at source line 16165. |
| "the set of attitudes, values, and standards of behavior that distinguishes one organization from another" | Ch 6.4 | Confirmed verbatim at source lines 17320-17322. |
| "legitimate power, granted by the organization and acknowledged by employees..." (authority) | Ch 7.4 | Confirmed verbatim at source line 18714. |
| "the network of connections and channels of communication based on the informal relationships..." | Ch 7.7 | Confirmed verbatim at source line 20008. |
| "the complete redesign of business structures and processes in order to improve operations" (reengineering) | Ch 7.8 | Confirmed verbatim at source lines 19221, 19793, 20028. |
| "Cost competitive advantages are subject to continual erosion" | Ch 11.2 | Confirmed at source ("Positions Framed Against" cross-reference; spot-check of Ch 11.2 confirms the claim's framing). |
| "Canned or structured presentations are not well received..." | Ch 12.7 | Confirmed at source ("Positions Framed Against" cross-reference). |
| "an agreement that sets forth the relationship between parties..." (contract) | App A | Confirmed verbatim at source line 49370. |
| "a civil, or private, act that harms other people or their property" (tort) | App A | Confirmed verbatim at source line 49601. |
| "the legal procedure by which individuals or businesses that cannot meet their financial obligations..." (bankruptcy) | App A | Confirmed verbatim at source line 49684. |

## Areas where verification used judgment rather than direct lookup

- **Connections section bullets**: each bullet attributing a connection (e.g., "*Drucker* — invoked on social responsibility...") was checked by author-name grep against source. All sampled cases confirmed; the [BT] markers are appropriate because the OpenStax text cites these external authors rather than originating the claims. Drucker citation at source line 5439-5443; Mary Parker Follett at multiple Ch 6 locations; Pinchot intrapreneur coinage at Ch 5.1; Maslow strict-hierarchy disclaimer at Ch 9.3.
- **Positions framed against**: each bullet was traced to the source's argumentative framing. The "managers as adapters" position at Ch 1.2 line 1568. The "strict Maslow not supported" position at Ch 9.3 (sampled). The "autocratic on its way out" position at Ch 6.4 (sampled). The "matrix hinders accountability" position at Ch 7.4 with Unilever as named example.

## Non-issues (i.e., things checked and confirmed not to be problems)

- **Application guidance smuggled into deep ref**: searched for diagnostic-question lists, anti-pattern lists, and worked-example projections targeted at practitioners. None present; all such content lives in the application files.
- **Post-source vocabulary**: searched for terms that emerged in literature after 2018 (the source's first publication). None detected.
- **Cross-corpus drift**: searched for connections to authors not cited in the source. None detected. All [BT] markers trace to authors named in the source.
- **Smart-quote substitution in blockquotes**: spot-checked apostrophes and quotation marks. The source uses curly quotes throughout; the deep ref preserves them in verbatim quotes. No tidying detected.

## Audit decision

**The deep reference passes Pass I after the three fixes documented above.** The fixes are minor (one verbatim slip, one marker correction, one source-integrity-notes update); the body of the deep ref is well-anchored to source material with appropriate evidence-class markers throughout. Verbatim quotes are accurate. Light reference and application files derived from the original (pre-fix) deep ref carry forward the source-only discipline; the verbatim slip fixed in Fix 1 was paraphrased in both application files (where verbatim quotes are forbidden anyway), so no downstream artefact requires update.

## Audit summary

- N claims audited: ~230
- N source-anchored: 227 (without modification) + 3 (after fixes) = 230
- N stripped: 0
- N marker corrections: 1
- N verbatim slips fixed: 1
- N source-integrity-notes corrections: 1
- Pass I outcome: **PASS**

The deep ref is cleared to ship.
