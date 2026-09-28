# Deep-ref fixes surfaced by the distillation audit (demo)

## jones-evidence-based-sweng
- Deep line 103 merges the Bass diffusion model's peak-sales and peak-time formulas. Source: peak sales m(1/2 − p/2q), at time (1/(p+q)) ln(q/p).
- Deep line 91 says real options is presented with warnings it doesn't apply; the source warns only against Black-Scholes and presents real options as most useful when uncertainty is high.

## openstax-psychology-2e
- Table 6.3 marked [V] is not the source's wording; Asch's 76% is [BT] in the body and [V] in the stats table; the deep lacks the source's "fixed interval is the least productive and the easiest to extinguish" and the named causes of groupthink.

## openstax-organizational-behavior
- Line 725 marks the complex-change quote [AP] though it is verbatim → [V]. Line 112 presents the positive-reinforcement preference as the book's own; the source relays it from Skinner and others, hedged. Line 368 omits the finding that reward and legitimate power give inconsistent results.

## open-practice-library
- Source says OPL takes 1-2-4-All from Liberating Structures (source L14248); the OPL deep ref doesn't record it.

## approach-perfect-field-guide-scrum-events
- SOURCE ERROR (for the author's next edition): the velocity worked example gives ≈30; (25/45 + 24/43 + 31/50)/3 × 47 = 27.2. Deep ref records ≈30 faithfully; the decision-making distillation depends on it.
- Deep line 7 says every event uses three participant tiers; only the Daily Scrum does.
- Deep line 340 places the non-interference rule under Daily Scrum "Tips"; it is under "Participants".

## lfuo-learning-review-guide-2024
- PRIORITY (safety): deep ref omits the source's instruction not to take the interview back into deep recall and to leave that to mental health professionals (source 1928-1930). The aar distillation (lines 30, 58, 101) therefore tells interviewers to return to the traumatic memory. Add the sentence to the deep; fix the aar distillation.
- Extend deep coverage of Part 5, Part 6 Participants and Agenda, Parts 10-11 and Appendix C (distillations quote these from source).

## letaw-handbook-sweng-methods
- Cycle-to-deep additions: "with the client" (priority matrix, Ch 2.5.2); fist of five stop-and-revote on two or fewer fingers; Ch 3.4 stakeholder list; Ch 8.2 "not an exhaustive list".

## mcdp1-warfighting
- Deep "Connections to corpus" (deep 219-230) points to another corpus's slugs, not demo. Several distillation claims about Marquet, Goldratt and the Boyd lineage trace only to that section. Strip or re-point.
- All five distillations predate the template: no Key Concepts, phase tables, Worked Example or citation notes; heavy leakage (DORA, XP, Blue Ocean, Coram). Regeneration candidate.

## barbrook-johnson-systems-mapping
- Five core claims used by the stakeholder distillation are absent from the deep ref (~25 quotations taken from source at Pass G); cycle-to-deep candidates.

## UPSTREAM: task spec
- corpus.commons/demo/tasks/software-business.md lines 35 and 48 (trigger table) seed a "flow over utilisation" framing that open-kanban-software-business attributes to the source. Fix the spec too, or regeneration reintroduces it.

## openstax-accounting-vol1
- Deep line 74 misquotes the accrual sentence ("method" vs "basis of accounting").
- Cycle-to-deep: consistency principle + method-change disclosure (Ch 10.1, src 26917-26923); IRS LIFO conformity (src 26924-26927); materiality (Ch 8.4, src 22187-22189); restatement (Ch 14.4, src 37694-37700); Amazon unearned revenue (src 31097-31100); the book's own limit on revenue-recognition detail (src 23749-23750).

## openstax-business-ethics
- Deep line 19 says the moral minimum is legal compliance; source and deep line 146 define the moral minimum as honouring obligations to all stakeholders (legal compliance is the ethical minimum). decision-making line 10 copies the error.
- Cycle-to-deep: facilitating-payment exception; latent-public "opportunity to communicate"; Equifax; Tylenol recall details.

## open-practice-library
- Line 203 misquotes $100 Prioritisation ("It's a method…"; source: "Prioritising is hard. This is a method…").
- Line 330 lists Schwaber and Sutherland as cited; they aren't.
- Line 32 puts Test Automation and TDD under Delivery; source tags both Foundation (L8390, L8451).
- Line 127 conflates tags and mobiusTag ("delivery" isn't a tag value; Container and Defence in Depth carry no tags).
- Lines 237, 314: "Our job is not to point fingers…" should be [BT] (quoted, unattributed on the page).
- Invented Disagree-and-Commit quote ("everybody must have a meaningful choice, and there must be an agreed review point") in all five distillations; source wording L18044-18049.

## openstax-accounting-vol2
- Line 202 cites the substandard-material passage to Ch 8.1; the passage sits just before that heading (src 17600-17608).

## openstax-economics-3e
- Deep line 181 states the textbook Coase theorem (low transaction costs, negotiation, "regardless of who holds the rights"); the source's Ch 12.3 only says that once property rights are defined, the responsible party finds the least costly fix. Spread to 8 distillation lines across all three files.
- Deep line 235 says good sellers are "driven out by adverse selection"; source Ch 16.1: higher-quality sellers "may be reluctant to participate", markets "may become extremely thin"; "adverse selection" used only for insurance (Ch 16.2) and wage cuts.
- Cycle-to-deep: expected value, present discounted value, present bias (Ch 16.2, 17.2, App C, 6.3).

## openstax-introduction-business
- "Carroll's pyramid" is a made-up attribution in all three distillations (7+ times each, in concept anchors too); deep line 879 correctly says the source names no theorist.
- Deep line 619: auditing definition cited to Ch 14.2 comes from the Ch 14 Key Terms glossary (outside the deep's stated coverage).
- Deep line 77: Brigham Young classification marked [AP]; [BT] fits (source relays BYU researchers).
- Cycle-to-deep: VPN/ASP (Ch 13); CPM certainty assumption; decentralisation "costly mistakes"; newspaper test conflict-of-interest line; annual-report passage; Lexus/JD Power survey; environmental-scanning goal.

## openstax-organizational-behavior (additional)
- Deep line 688 ties bounded rationality to Simon; source Ch 6.4 never names Simon.
- Deep line 298 uses a self-contradicting "[V, paraphrased]" marker.
- Thomas-mode situations table: source labels it Table 14.1; deep calls it Exhibit 14.4.
- Cycle-to-deep: Ch 6.1 stakeholder definition; Ch 6.5 creativity, evidence-based decision-making, critical thinking, Rest model, front-page test; causes of groupthink; Ch 7.3 schedule ranking.
- CROSS-FILE: the reinforcement-schedule inversion appears in both OB retro and Psychology 2e retro — fix both.

## openstax-principles-finance
- Deep line 531 credits Statman with the "about a dozen stocks" threshold; source (25866-25877) gives Statman only the declining-standard-deviation finding; the dozen is the authors' own view.

## openstax-entrepreneurship
- Deep 401 calls Delphi questionnaires "anonymous"; source never says so.
- Deep 488 cites Ch 4.3 and "software" for build-first-patent-later; source carries it only in Ch 7.4 ("intellectual property … in a highly competitive field").
- Cycle-to-deep (one re-ingest pass): Ch 15.1–15.4 (vesting, dispute resolution, lifestyle vs harvest, fail-safe points "within the business plan"), 7.3, 10.1 Table 10.2, 11.2.
- CROSS-FILE: software-business routes "technical debt" questions to Jones, whose deep ref records he rejects the term.

## openstax-psychology-2e (additional)
- PRIORITY (licence): stakeholder-engagement distillation line 196 says "Licensed CC BY 4.0; derivative works permitted"; the source is CC BY-NC-SA 4.0 (deep lines 5, 502).
- Deep line 351 overstates Pettigrew & Tropp: source says the effect was "enhanced" under the four conditions, not that it depends on them.
- Cycle-to-deep: availability heuristic "recent experience"; Carli (1999) on hindsight bias; WEIRD caveat; self-efficacy "developed through social experiences"; Asch and Milgram replication passages.

## openstax-principles-management
- Deep line 273 attaches Brown & Trevino's ethical-leadership definition to "moral entrepreneur"; source (7027-7073) credits the concept to Kaptein and Becker. Rewrite text is in stakeholder-engagement D004.
- CROSS-FILE global corrections: six structure types credited to Mintzberg (textbook's own Exhibit 4.6, adapted from Daft) — 10× in software-business incl. the mintzberg-structures anchor, 1× aar; "measurable" credited to Locke (SMART's); stuck-in-the-middle hardened; invented "high-stakes, ongoing relationship" condition on Follett's integration; Appreciative Inquiry "produces stronger commitment".
- Cycle-to-deep: Herzberg's two-stage process; cost of Follett's dominance path; Elkington for triple bottom line; nAff definition; Ch 17.8 uncertainty-to-involvement.

## org-topologies-primer-2025
- Cycle-to-deep (one pass clears ~15 findings): DESIGN and ELEVATE outcomes of the running MADE example (pp. 18-19); middle of the pet-supply walk-through (p. 21); p. 11 "treat the Doing Archetypes as 'resources'"; p. 20 "limited resources of money, time, and attention"; p. 1 "engaging for people to map…"; p. 4 training sentence.
- CROSS-FILE: invented "Adaptive-Topology variance / high-variance" failure mode (aar, retro, decision-making, software-business); invented "named drift/regression pattern" back to Resource Topology (4 files); retro worked example CAPS-2 vs CAPS-3.

## tc-25-20-army-aar (AAR canonical source; aar-mode app)
- CROSS-FILE: invented two-levels rationale ("next echelon too close") — aar 18, 135; decision-making 28, 61, 155; stakeholder-engagement (separate audit). TC gives no reason; external evaluations only; chain-of-command one level up when no observers; only caution is not evaluating your own duties.
- CROSS-FILE: invented 15-minute informal AAR; "90 minutes" vs TC's 1 hour; "five discussion phases" vs seven-part sequence; Field Guide retro agenda called 5-segment (it's 6); fratricide rule recast as a time-budget override; "train to weakness" drops the sustaining-tasks qualifier.
- decision-making line 10 places the AAR outside the operation; TC integrates AARs at the end of each critical phase and into combat operations.
