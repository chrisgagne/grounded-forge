# Pass I Source-Only Audit — OpenStax, Entrepreneurship

**Operator model:** claude-opus-4-7[1m] (Opus 4.7, 1M context)
**Audit date:** 2026-05-05
**Subject:** `corpus.commons/demo/references/openstax-entrepreneurship-deep.md` (post-Pass-E)

## Audit procedure

The deep reference was read cold. For every body claim, table cell, evidence-class marker, and cross-reference, the auditor asked: "Can I trace this to a passage in the converted source markdown?" The audit was structured part-by-part (I-XV) and concept-by-concept within each part.

The verification mechanism: for each load-bearing claim, the auditor either re-read the relevant section in the source or used `grep` against the converted markdown (`corpus.commons/demo/sources/converted/openstax-entrepreneurship.md`) to confirm the cited section's content matches the deep ref's paraphrase or quote.

## Audit results

| Audit dimension | Count |
|---|---|
| Total claims audited (body sentences with citations or evidence markers) | ~210 |
| Claims source-anchored without modification | ~208 |
| Claims requiring marker correction | 1 |
| Claims requiring strip (no source support) | 1 |
| Verbatim blockquotes verified character-by-character against source | 35+ |
| Cross-references to other authors verified as cited in source ([BT] markers) | All sampled instances confirmed |
| Application guidance found in deep ref (tier violation) | 0 |
| Post-source vocabulary detected | 0 |

## Specific fixes made during Pass I

### Fix 1: Marker tightening (Part X, lean startup share-of-revenue claim)

**Location:** Part X, "Lean startup, MVP, and the build-measure-learn loop" — the Dropbox $1 billion in revenue and 500-plus million users figure.

**Issue:** The figure was carried with [V] in an early draft, but the source phrasing is paraphrased ("Even with Dropbox's reported $1 billion in revenue and 500-plus million users") rather than verbatim-stated as such within quotation marks.

**Fix:** Marker downgraded to inline citation without [V]; the figure is presented as a paraphrase referenced to Ch 10.1 rather than a verbatim quote. The claim itself is source-anchored.

### Fix 2: Strip of unsupported context sentence (Part II, Madam C. J. Walker case)

**Location:** Part II, "Historical evolution of US entrepreneurship".

**Original sentence (early draft):** A meta-commentary line that read "the Madam C. J. Walker, Charles Drew, and Sybilla Masters cases together establish the systemic exclusion thesis the chapter builds toward".

**Issue:** "the systemic exclusion thesis the chapter builds toward" is the auditor's framing, not the source's. The source presents these cases without explicitly framing them as a unified exclusion thesis.

**Fix:** Sentence rewritten to attribute the cases as the source uses them ("are used to surface the historical exclusion of women, African Americans, and enslaved people from patent rights despite their inventive contributions"), which is supported by the source's own narrative arc in Ch 2.2.

## Specific spot-checks performed and confirmed

| Claim | Citation | Verification |
|---|---|---|
| "an entrepreneur is someone who identifies and acts on an idea or problem that no one else has identified or acted on" | Ch 1.1 | Confirmed verbatim at source line 766. |
| Brown Forbes quote on franchisees as entrepreneurs | Ch 1.1 | Confirmed verbatim at source lines 781-784. |
| US VC investment 2015 ($72.3 billion, 3,916 deals) | Ch 1.1 | Confirmed at source line 1141. |
| China VC investment 2015 ($49.2 billion, 1,611 deals) | Ch 1.1 | Confirmed at source line 1141-1142. |
| 47% US employment at risk through AI/tech (Frey and Osborne) | Ch 1.1 | Confirmed at source lines 1052-1054. |
| Christensen's disruptive technology definition | Ch 1.3 | Confirmed verbatim at source lines 1966-1968. |
| Independent contractor 42% projection for 2020 | Ch 2.1 | Confirmed verbatim at source line 2427. |
| Net job growth 94% in alternative work 2005-2015 | Ch 2.1 | Confirmed verbatim at source lines 2433-2435. |
| US self-employed 9.6 million end of 2016 | Ch 2.1 | Confirmed at source line 2438. |
| Immigrant 25% of US entrepreneurs | Ch 2.1 | Confirmed at source lines 2474-2476. |
| Fortune 500 40.2% immigrant founders | Ch 2.1 | Confirmed at source line 2477. |
| Angola 41% entrepreneurial activity (GEM 2018/2019) | Ch 2.1 | Confirmed at source lines 2494-2495. |
| Schumpeter creative destruction quote | Ch 2.2 | Confirmed verbatim at source lines 3427-3429 (citing the New World Encyclopedia summary as the OpenStax source). |
| Whyte Organization Man bureaucratic-social-ethic quote | Ch 2.2 | Confirmed verbatim at source lines 3437-3439. |
| Jean-Baptiste Say resource-shift definition | Ch 2.2 | Confirmed verbatim at source line 3158-3160. |
| Cantillon "willingness to bear personal financial risk" | Ch 2.2 | Confirmed verbatim at source line 3245-3246. |
| Vertical integration definition (Carnegie) | Ch 2.2 | Confirmed verbatim at source lines 3282-3284. |
| Patent definition | Ch 2.2 | Confirmed verbatim at source line 3291-3292. |
| Intrapreneur definition | Ch 2.2 | Confirmed verbatim at source line 3471-3472. |
| Entrepreneurial opportunity definition | Ch 5.1 | Confirmed verbatim at source line 9336-9337. |
| Schumpeter on entrepreneurial value creation | Ch 5.1 | Confirmed verbatim at source lines 9352-9355. |
| Schumpeter's five methods for finding new opportunities | Ch 5.1 | Confirmed at source lines 9395-9402. |
| Three opportunity-recognition criteria | Ch 5.2 | Confirmed at source lines 9728-9734. |
| Half of new businesses fail within five years (SBA) | Ch 5.2 | Confirmed at source line 9977-9978. |
| Pridham six conditions for startups | Ch 5.1 | Confirmed at source lines 9577-9605. |
| Brown's design thinking quote | Ch 6.3 | Confirmed verbatim at source line 11838-11839. |
| ASQ Six Sigma definition | Ch 6.4 | Confirmed verbatim at source line 12108-12112. |
| Crowdsourcing definition (Brabham) | Ch 6.2 | Confirmed verbatim at source line 11622-11623. |
| Shareholders vs. stakeholders distinction | Ch 3.1 | Confirmed verbatim at source line 5001-5004. |
| Business Roundtable five commitments (deliver/invest/deal-fairly/support/generate) | Ch 3.1 | Confirmed at source lines 5055-5083. |
| Antitrust acts (Sherman 1890, Clayton 1914, FTC 1914, Bayh-Dole 1980) | Ch 3.1 | Confirmed at source line 5536-5538 plus Table 3.1. |
| WMEC 8% excess return (Areal and Carvalho) | Ch 3.1 | Confirmed at source lines 5188-5193. |
| ~3,000 certified B-corps in 65 countries | Ch 3.2 | Confirmed verbatim at source lines 6135-6136 and again at lines 28589-28590. |
| Mycoskie's TOMS first-person account | Ch 3.2 | Confirmed at source lines 6037-6092 (extended quoted block). |
| 60% of millennial workers accept 15% pay cut for value alignment | Ch 3.3 | Confirmed verbatim at source lines 6341-6342. |
| 60% of misconduct involves managerial authority (2014 Ethics Survey) | Ch 15.2 | Confirmed at source line 33102-33103. |
| 60% of strong-ethics-culture misconduct is one-time | Ch 15.2 | Confirmed verbatim at source line 33115. |
| Drucker seven sources of innovation | Ch 4.2 | Confirmed at source lines 8105-8116 (Table 4.3). |
| Disruptive innovation definition | Ch 4.2 | Confirmed verbatim at source lines 8147-8149. |
| Pioneering vs. incremental innovation distinction | Ch 4.2 | Confirmed at source lines 8168-8175. |
| DICEE attributes (Kawasaki) | Ch 4.3 | Confirmed at source lines 8657-8659 (Figure 4.13 caption). |
| Five stages of creativity (Wallas) | Ch 4.3 | Confirmed at source lines 8470-8481. |
| Mozart on incubation | Ch 4.3 | Confirmed verbatim at source lines 8523-8526. |
| Musk's six-step decision process | Ch 4.2 | Confirmed at source lines 8305-8313. |
| Thompson on US patent statute language | Ch 4.3 | Confirmed verbatim at source line 8881-8883. |
| Lean startup definition (Ries) | Ch 10.1 | Confirmed verbatim at source line 22139-22141 (paraphrased in deep ref). |
| Build-measure-learn loop (Ries) | Ch 10.1 | Confirmed at source lines 20186-20193. |
| Ten pivot strategies (Ries) | Ch 10.1 | Confirmed at source Table 10.2 lines 20585-20635. |
| 18-month startup success rate 20% | Ch 10.2 | Confirmed verbatim at source lines 20675-20676. |
| 10-year startup success rate ~30% | Ch 10.2 | Confirmed at source lines 20676-20678. |
| 75% venture-backed startups fail | Ch 11.1 | Confirmed at source line 22628-22629. |
| 42% of CB Insights failures due to "no market need" | Ch 11.1 | Confirmed verbatim at source line 22637-22638. |
| Maurya three business model archetypes | Ch 11.1 | Confirmed at source lines 22675-22681. |
| Christensen jobs-to-be-done | Ch 11.1 | Confirmed at source lines 22893-22900. |
| Andreessen "great markets pull product" | Ch 7.3 | Confirmed verbatim at source lines 13553-13555. |
| F&F share 50-70% of US startup capital | Ch 7.3 | Confirmed at source lines 13492-13494. |
| HubSpot 70% customer-experience-driven-by-treatment | Ch 8.6 | Confirmed verbatim at source lines 17626-17627. |
| HubSpot 12 positives counter 1 negative | Ch 8.6 | Confirmed verbatim at source line 17633. |
| Federal corporate income tax rate 21% (2019) | Ch 13.2 | Confirmed at source lines 28764-28768. |
| US utility patent term 20 years | Ch 14.1 | Confirmed at source line 30540-30541. |
| US design patent term 14 years | Ch 14.1 | Confirmed at source line 30556. |
| Pfeffer-Salancik RDT 1978 | Ch 14.3 | Confirmed at source lines 31649-31651. |
| Granovetter strong/weak ties | Ch 6.1 | Confirmed at source lines 11142-11149. |
| Kirton KAI Inventory adaptive vs. innovative | Ch 6.1 | Confirmed at source lines 11006-11030. |
| YouTube $1.65 billion harvest in 21 months | Ch 15.1 | Confirmed at source lines 32871-32876. |
| Bailey and Rehman three reflection themes | Ch 15.5 | Confirmed at source lines 33708-33715. |
| Cossette overconfidence and optimism findings | Ch 15.2 | Confirmed at source lines 32986-32989. |
| Six entrepreneurial problem-solving skills | Ch 6.1 | Confirmed at source Figure 6.3 and surrounding text. |
| Lay's Do Us a Flavor 14M submissions, 8% sales increase | Ch 6.2 | Confirmed at source lines 11675-11677. |
| Stacy's Pita Chips $65 million Frito-Lay sale | Ch 15.2 | Confirmed at source line 33063-33064. |
| Eight-step Toyota lean problem-solving (Table 6.1) | Ch 6.4 | Confirmed at source Table 6.1 lines 12164-12173. |

All sampled spot-checks confirmed.

## Audit pass/fail decision

The deep reference passes Pass I.

- Strip count is non-trivial but small (1 strip; 1 marker correction); both fixes were applied to the deep ref before this audit log was finalised.
- All 35+ verbatim blockquotes are character-by-character verified.
- All [BT] cross-references trace to citations the source itself makes (Schumpeter, Drucker, Christensen, Ries, Blank, Andreessen, Osterwalder/Pigneur, Maurya, Kelley/Brown/IDEO, Chesbrough, Kawasaki, de Bono, Rogers, Granovetter, Kirton, Brabham, Markides, Pfeffer/Salancik, Wallas via Sadler-Smith, Klein, Sandberg, Cossette, Bailey/Rehman, Cremades/Corcoran, Castleberry/Tanner, others).
- Zero application guidance found in the deep ref. All diagnostic questions, anti-patterns, and worked examples reside in the application files (decision-making and stakeholder-engagement).
- Zero post-source vocabulary. Concepts attributed to Ries, Christensen, Drucker, etc. are all attributed to the works cited within the OpenStax source, not to subsequent literature outside the source.

The deep reference ships.

## Light-reference downstream check

The light reference (`corpus.commons/demo/references/openstax-entrepreneurship.md`) was derived from the verified deep reference (Pass F). Spot-check confirmed:

- All quantitative claims in the light ref Key Statistics table appear in the deep ref Key Statistics table.
- All cited authors in the light ref Key Connections appear in the deep ref Connections section.
- The six contrarian positions in the light ref appear in the deep ref Positions Framed Against section.
- No application guidance present in the light ref (verified by section read).

## Application-file downstream check

Both application files (`openstax-entrepreneurship-decision-making.md` and `openstax-entrepreneurship-stakeholder-engagement.md`) were checked for tier-discipline compliance:

- Each concept paraphrased rather than blockquoted from source (verified by `grep -E "^>\s*\"" application files` returning no matches).
- Each concept carries a `(Source: …)` citation linking back to a chapter and section in the source.
- Worked examples are fictional and original to the application files, not lifted from the source.
- "Integration with Other Frameworks" sections include library-level synthesis (this is the application-file tier where such synthesis is permitted; it is not in the deep ref).
