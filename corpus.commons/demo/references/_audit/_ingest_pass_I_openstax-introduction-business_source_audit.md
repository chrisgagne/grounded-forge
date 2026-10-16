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

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor:** a fresh Claude agent (same model family as the generator), fix-in-place mode. No cross-family leg was run, so this scoped audit is same-family only and the restored material stands as audited-but-unverified until a second family reads it.

### Scope

Only the deep-reference text written on 2026-10-17 for the spans the 2026-10-16 re-conversion restored (`git diff origin/main` of `corpus.commons/demo/references/openstax-introduction-business-deep.md`: 100 added or replaced non-blank lines, 15 removed; current lines 9, 23–24, 33–35, 43–46, 51–52, 76–77, 96, 101–102, 107–108, 118–119, 126–127, 142, 157–158, 163–180, 183–184, 195–198, 207–208, 215–216, 225–226, 231–232, 237–238, 253–254, 259–262, 265–266, 271–272, 280–284, 286, 306–307, 316–317, 338, 342–343, 356–357, 372, 376–379, 396–397, 408–409, 420–421, 433, 439–440, 445–446, 451–454, 463–464, 479–480, 489–490, 498, 524–527, 530–531, 567–568, 583–584, 591–592, 638, 650–651, 656–657, 662–663, 666–667, 685, 689–690, 706, 712–713, 729–730, 735–743, 747–748, 755–756, 769–770, 794–795, 798–799, 812–817, 820–822, 826–827, 853, 869–870, 883–884, 896, 972, 1061), plus the orchestrator's correction at line 820 (Ch 15.6). For replaced lines only the added or changed clauses were audited. The rest of the deep reference was audited earlier and was not re-read.

### What was read

- Every added or replaced line of the deep reference, in full, from the diff; deep-reference lines 1–12 and 1055–1069 for context.
- The restored-span extract (399 `=====` spans, tape lines 1138–53095) in full, blank lines dropped only.
- Each of the 51 feature boxes and chapter-opening Exploring Business Careers features the new paragraphs summarise, read whole in the tape from the box title through its Sources list (including interleaved body text where PyMuPDF split a box across a page).
- Every table summarised (1.1, 2.1, 3.1, 3.2, 3.3, 5.5, 5.8, 6.1, 6.2, 6.3, 6.5, 6.6, 7.1, 8.3, 8.4, 9.1, 9.2, 11.3, 11.5, 12.1, 12.3, 13.2, 15.7, 16.1, 17.3, A2) and Exhibit 3.6, in full, with the headings around each to check section placement.
- Ch 15.6 in the tape (≈45684–45765) and the Ch 15 chapter summary (≈46049) for the orchestrator correction; the whole tape grepped for blockchain, Bitcoin and cryptocurrency.
- No PDF renders were needed; the tape text was legible for every box and table in scope.

### Verbatim check

`python3 scripts/check-verbatim.py` before and after: 8 apostrophe, 11 initial, 1 missing (line 595, pre-existing, out of scope), 6 no-quote. All 87 `[V]` quotations in the added text pass; no quotation needed correcting.

### Counts

- Claims audited: about 420 (facts, figures, quotations, markers, section placements and box-type labels across the 100 changed lines).
- Source-anchored without change: all but the 7 below.
- Stripped: 1 (the orchestrator's line 820 strip, verified and logged here).
- Claim corrections: 4 (line 820 replacement, 338, 489, 743).
- Marker corrections: 2 (lines 173 and 743, `[BT, Surname]` narrowed to `[BT]`).
- Coverage-line corrections: 1 (line 9).
- Quotation corrections: 0.

### Changes by line

- **Line 820 (Ch 15.6), orchestrator correction, verified.** Stripped: "Online banking, mobile banking, blockchain/cryptocurrency emergence, and consolidation are catalogued as ongoing trends (Ch 15.6)". The book mentions blockchain and Bitcoin only in Ch 10 (tape ≈29431, 29481) and Ch 13 (≈38513, 40010), never in Ch 15; the only "consolidation" in Ch 15 is a 15.3 remark that small banks are declining through consolidations (≈44939), not a 15.6 trend. The replacement sentence was checked clause by clause against 15.6 (≈45684–45765): regulatory and compliance, operational efficiency and technology; customer engagement through data analytics; fintech disruption and partnerships, with the Goldman Sachs estimate; mobile apps and personalisation; fewer branches; online payment platforms (PayPal, Apple Pay). It holds. The light reference's matching sentence (`openstax-introduction-business.md` line 74) now names the same six trends with a (Ch 15.6) citation, and the old "International banking, online banking, mobile banking, and emerging blockchain/cryptocurrency" text is gone. Correct as edited.
- **Line 9 (Coverage).** The section list misplaced several restorations: the EU map (Exhibit 3.6) is in Ch 3.5, not 3.7–3.9; Tables 5.5 and 5.8 are in Ch 5.3 and 5.4, not "5.5 and 5.7"; Table 6.6 is in Ch 6.8, not within "6.1–6.7". Corrected to Ch 3.5 and 3.7–3.9, Ch 5.3–5.5, Ch 6.1–6.8, and the restored body text the list omitted was named (Ch 1.1 entrepreneurs, Ch 7.3 cross-functional teams, Ch 8.6 pay and job satisfaction, Ch 13.2 wireless LANs).
- **Line 173 (Ch 3.8, "U.S. Brands Face Global Competition").** "European brands that are becoming stronger and more consistent [BT, Davvetas and Diamantopoulos; Vence]": the box lists its sources only at the end and neither named source plainly carries the Haier/Kelon/Li Ning/Korean/European material (Haier's 2016 GE purchase postdates Vence 2005). Narrowed attribution replaced with `[BT]`; the paragraph's opening sentence still carries the full source list.
- **Line 338 (Ch 6.8, Table 6.6, Chiles Restaurants).** "used an all-employee scheduling platform" read a function into the product name. The table says "Hot Schedules, a platform all employees log into". Corrected to the table's words.
- **Line 489 (Ch 9.4, Table 9.1).** Theory Z's row reads "Is relatively concerned with worker's whole life, including the family"; the deep had dropped "relatively". Corrected to "relative concern for the worker's whole life".
- **Line 743 (Ch 13.6, "Unearthing Your Secrets").** "named the leader in digital forensics" implied an award; the box simply calls Guidance Software "the leader in this technology". Corrected to "which the box calls the leader". The Casey Anthony / Sony / bin Laden sentence carried `[BT, McCullagh; Narcisse]`, but the Casey Anthony case comes from a third, unauthored source in the list; changed to `[BT]`.

### Checked and left as is

- **Placement and labels.** Every box paragraph names the box's own label (Managing Change, Catching the Entrepreneurial Spirit, Ethics in Practice, Expanding Around the Globe, Customer Satisfaction and Quality, Exploring Business Careers) and the section the box sits in; all matched the tape. The Fishpeople box (line 118) sits under the Environmental Protection sub-part of Responsibility to Society; "the Responsibility to Society discussion" is accurate at that level. Panera's box carries the label "Ethics in Practice" twice in the tape; the deep's single label is right.
- **Markers.** Press-sourced boxes carry `[BT, Surname]`; the Jessica MacLean feature has no Sources list and is correctly `[AE]`; Table 2.1's training dilemma is `[AE]`; tables are `[AP]`. Narrowed `[BT, Surname]` citations inside paragraphs were kept where the box text itself names the source or the source title plainly matches the fact (Oil prices: Tejani; Work-life balance: Galoozis; PacSun: Masunaga, Church; UN goals: Kreiner, Embree; Stephenson: Stephenson, Egan, Heitz; Eberwein: Korn Ferry survey; Communities of practice: Chase/MAKE; da Vinci: Meskó; Whistleblower: SEC, Singerman and Hugel, Zuckerman and Stock).
- **Framing judged supported.** Domino's "its point for the chapter is the value of master franchisees" (the box ties master franchisees to "as discussed in this chapter"); Gordon Bernard's commercial work filling seasonal off-peak capacity (the box places the two facts together); the hurricane-pricing hotel example under the Chicago School view (the box adds it "in addition" to that argument); "cheesy" quoted with `[BT]` in the Kaplan feature (a one-word quote, verbatim).
- **Table summaries.** Rows checked against each table; nothing invented. Partial listings are honest subsets (Table 2.1 gives three of four discussion questions; Table 12.1's internet examples give three of six; Table 3.2 gives endpoints and the U.S. rank, which is seventh).

### Derived tier

The edits that change a claim are lines 173, 338, 489, 743 (marker and wording) and line 9 (coverage metadata). Grep of the light reference and the three distillations (`decision-making`, `software-business`, `stakeholder-engagement`) finds none of these claims carried; the decision-making distillation's Theory Z line (174) is generic and unaffected. No distillation carries a blockchain, cryptocurrency or consolidation trend claim for Ch 15. The light reference's line 74 correction was checked (above). The deep reference was not stamped; re-derivation and `check_derived_provenance.py --stamp` are for the parent.

### Open

- **Cross-family leg not run.** The restored material is audited-but-unverified until a different model family reads it blind.
- **Ch 9.8 Education and Training, restored clause not carried.** The restored run at tape ≈27250 begins mid-paragraph: training increases "employees' feelings of competence and self-worth" and conveys "we value you and are committed to your growth and development". Deep line 520 names education and training as a trend but does not carry this clause. Minor; outside the changed lines, so left for the parent.

### Orchestrator follow-up, derived tier and stamp (2026-10-17)

Open item 2 settled: the restored Ch 9.8 "Education and Training" clause is now in the Ch 9.8 trends paragraph (competence and self-worth; "we value you and are committed to your growth" [V], tape ≈27248–27255), so the Coverage line's "every span … added" holds. The PARTIAL notes are gone from the light reference, the three distillations and the source card, replaced by a coverage statement that names the single-family audit. The restored features are illustrative cases and tables that add no concept to the decision-making, software-business or stakeholder-engagement projections, so those carry no new content; none of them repeated the stripped Ch 15.6 claim. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
