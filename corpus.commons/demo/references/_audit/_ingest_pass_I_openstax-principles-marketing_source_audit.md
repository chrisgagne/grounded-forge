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

## Scoped re-audit 2026-10-17: restored feature boxes and body text

**Auditor:** a fresh Claude agent (same family as the drafter). No cross-family leg was run, so this scoped audit is audited-but-unverified in the protocol's terms.

### Scope

Only the deep-reference text written on 2026-10-17 for material the 2026-10-16 re-conversion restored (`git diff origin/main` ranges 9, 29–32, 39–40, 52–53, 58–59, 70–71, 82–83, 100–103, 130–146, 152–160, 164–165, 170–171, 188–189, 202–203, 218–219, 222, 228–229, 236–237, 244–245, 252–254, 268–270, 286–287, 294–295, 300–301, 304–306, 322–323, 328–330, 336–337, 353–355, 359–360, 375–376, 385–386, 391, 401–402, 407–408, 423–424, 431–432, 437–438, 441–443, 465–466, 473–474, 489–492, 497–498, 513–517, 523–526, 533–534, 537–543, 551–553, 557–559, 563–564, 567–568, 577–578, 601–602, 613–614, 623–626, 633–634, 641–642, 647–648, 651–652, 655–656, 724), plus the new Ch 4 In the Spotlight paragraph (RingCentral, line 164). For replaced lines, only the added clauses. Everything else was audited earlier and was not re-audited.

### Read

- Deep reference: all 730 lines, in full.
- Restored-span extract (177 spans with context, tape lines 1179–34429): all 5,948 lines, in full.
- Tape, beyond the extract: the remainder of every scoped box the extract cut short (TOMS Shoes Ch 1.7, Marketing Manager, CLV with Table 2.1 and solutions, Patagonia, Alibaba, Kforce, LEGO, Global Marketing Manager, Ch 8.6 Culturally Sensitive and Socially Inclusive Marketing, Netflix, Upside, The Five Cs of Pricing, Warby Parker, Farmer Direct Organic, Measuring the Impact of Advertising with its solutions, Cost of Customer Acquisition with Table 15.1, Domino's, Targeted Advertising with Table 16.1 and solutions, Dollar Stores and the Community, Trader Joe's Ch 18.7); the Ch 4 In the Spotlight opener (tape 7134–7151); placement context for The Reckoning (Ch 1.4 product concept), Infographics (Analyze and Interpret the Data), ROCI (Evaluate and Measure the Objectives) and National Geographic (label MARKETING IN PRACTICE, tape 29081).
- Chapter References: every endnote behind a `[BT, …]` surname in scope (Ch 1 #62–63; Ch 2 #75–77; Ch 3 #20, 27–28; Ch 4 #1, 5–6, 24–27; Ch 5 #52, 85–87; Ch 6 #21, 26–29; Ch 7 #57, 89–92; Ch 8 #12–13, 72–74; Ch 9 #3, 11–12; Ch 10 #36–37, 52; Ch 11 #21–22, 48–49; Ch 12 #38–39; Ch 13 #21; Ch 14 #12, 29, 31–33; Ch 15 #9, 12–13; Ch 16 #32–34, 40–42; Ch 17 #9–10; Ch 18 #46–47; Ch 19 #14).
- Feature labels were checked in the tape, where each box's label line follows the box; no PDF renders were used.

### Verbatim check

`python3 scripts/check-verbatim.py` before and after: 3 apostrophe, 2 initial, 1 missing (line 210, pre-existing, out of scope). No new mismatches; the two quotations added at line 563 match the tape.

### Counts

| | Count |
|---|---|
| Scoped units (new paragraphs, added clauses, Coverage and integrity lines) | 92 |
| Claims audited (sentence-level clauses and markers; approximate) | ~320 |
| Source-anchored without change | ~308 |
| Stripped | 0 |
| Marker-corrected | 8 (lines 58, 100, 146, 160, 164, 298, 515, 559) |
| Content-corrected | 4 (lines 31, 270, 423, 563) |
| Quotation-corrected | 0 |

### Changes by line

- **31** (Reconciling Segmentation and Diversity): "three press articles" → "three articles"; one of the three is the Spectrem Group Blog, not press.
- **58** (The Reckoning): `[BT, Halberstam]` → `[AP]`. The box points to Halberstam's book for further reading; it attributes no claim to him.
- **100** (Classic Cleaners): the 17-locations fact comes from endnote 75, Classic Cleaners' own locations page, not TBH Creative. Opening marker now `[BT, TBH Creative; Classic Cleaners]`; the locations clause carries `[BT, Classic Cleaners]`.
- **146** (Abercrombie & Fitch): the closing sentence describes a linked CEO video, not Khan's article (endnote 20); `[BT, Khan]` → `[AP]`.
- **160** (Patagonia): endnote 27 (Baldwin, Vox) covers the fair-trade and supplier-disclosure claims; endnote 28 ("Reasons We Love Patagonia", wearedore.com) covers recycled materials and take-back. Split the markers accordingly; the book's own "leader in environmental and social responsibility" framing, which carries no endnote, is now `[AR]`.
- **164** (Ch 4 In the Spotlight, RingCentral): `[BT]` → `[BT, Medallia]` twice; endnote 1 is Medallia's RingCentral case study.
- **270** (Global Marketing Manager): "career guides" → "a career guide"; the box lists one Noodle article and one video.
- **298** (PepsiCo, added clause): `[AP]` → `[BT, Smith; Adams]`; the backlash and withdrawal sentences carry endnotes 12 (Smith, NBC News) and 13 (Adams, Essence).
- **423** (Meta): the paragraph merged two separate source statements. Krieger's role covered engineering and design; the RIT focused on identifying ethical issues at the design and development stage. Now stated separately.
- **515** (PepsiCo, Ch 14.4 added clause): `[AE]` → `[BT, Business Insider]`; the sentence carries endnote 12, a Business Insider video.
- **559** (National Geographic): `[BT, Oxford]` moved from the book's own judgement ("a great way to connect…") to the Wanderlust campaign fact that endnote 33 supports.
- **563** (Targeted Advertising): the paragraph reported the example only as a cost per click. The box's solution calls the $1.10 figure a "click-through rate" ("Was the click-through rate a good investment?"; "profited $7 on the single purchase at a click-through rate of just $1.10"), while Table 16.1's solution gives "$1.10/click". The line now gives the table's per-click figure and quotes the box's own wording `[V]`, with no outside correction.

### Checked and left

- Feature-type names: all 70-odd scoped box paragraphs name the label that follows the box in the tape (Careers in Marketing, Marketing in Practice, Companies with a Conscience, Marketing Dashboard, Link to Learning). No mislabels found.
- Placement: section citations match the tape's section for every scoped box, including the Reckoning (Ch 1.4 product concept), Infographics (analysis step), ROCI (Evaluate and Measure the Objectives) and the two Ch 18 dollar-store boxes, which do link the same video ("Deal or no deal? The expansion of Dollar Stores").
- `[BT, …]` surnames confirmed against endnotes: Naeini; TOMS; TBH Creative; Khan (A&F store practices); Medallia; Alibaba.com; Kforce; Huber; Anderson; Dodge; Holloway; Insights Association; Saad; Khoury and Semykoz; Gallup; Cain; Ethisphere; Gemeš; Kao; Nittle; Coca-Cola Australia; Day; Schneider; Mallinger; Rossy; Wilkinson; Bond; McHugh; Toporek; Nasco Gulf; Knowledge@Wharton; Farmer Direct Organic; Spary; Mycoskie; Shewan; Breen; Tentree; National Geographic Partners; Oxford; Nat Geo Wild; Apple; Kaczanowski; Allbirds; Seely; State Bags. Unendnoted attributions that the box itself makes (US Bureau of Labor Statistics, Barrios, Shen, American Marketing Association, GWI, Teeny, Garman, eMarketer, Wyzowl, Oberlo, ZipRecruiter, GS1, Marketing Dive, Advertising Association, Quantcast, Schultz) were left as attributed in the box.
- Subway (line 228): `[BT, Holloway]` covers facts the box gives without an endnote, but the box's only endnote (87, Holloway, "First Lady, Subway Launch Healthy Eating Campaign for Kids") covers the same campaign. Left.
- Coverage line (9) and integrity note (724): the description of what was added (feature boxes with a substantive claim, folded body sentences, pointer-only boxes excluded, the Ch 4 opener) matches the deep reference. Pointer-only Careers in Marketing boxes (Women in Marketing, B2B Jobs, Being a Buyer, the Ch 11 salaries box, the Ch 18 distribution-careers box) and the Ch 3 Situational Factors Marketing in Practice link list have no paragraph; that is consistent with "with a substantive claim".

### Derived tier

No stamp set. Edits that change a claim a light reference or distillation may carry: line 100 (Classic Cleaners attribution), 146 (A&F video attribution), 160 (Patagonia attribution and `[AR]`), 164 (RingCentral attribution), 298 and 515 (PepsiCo now `[BT]`), 423 (Meta: Krieger's role vs the RIT's focus), 559 (National Geographic attribution), 563 (Targeted Advertising: the box's "click-through rate" wording). Distillations were not edited. The parent re-derives.

### Open

- Coverage line count: line 9 gives "about 20,700 words in 350 runs". The extract's span headers sum to about 19,700 words in 177 spans (spans merge runs, and the headers are approximate). The figure was left as written; it could not be checked from the inputs supplied.
- No cross-family leg for this scope.

### Derived tier and stamp (2026-10-17, orchestrator)

The PARTIAL notes are gone from the light reference, the three distillations and the source card, replaced by a coverage statement that names the single-family audit. The restored boxes are illustrative cases, career notes and dashboards that add no concept to the decision-making, software-business or stakeholder-engagement projections; none of the corrected attributions above is carried by the derived tier (grep for each case name). On the open coverage count: 20,700 words in 350 runs is what the word diff found across the whole converted text; about 1,000 of those words sit in front matter, the Answer Key and the Index, which the extract skipped as out of scope. A Pass I stamp on line 2 of the deep reference records this scoped audit. Derived tier restamped against the new deep-reference hash.
