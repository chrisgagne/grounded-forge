# Pass I source-only audit — SSDL Systems Thinking Foundations

**Audited file:** `corpus.commons/demo/references/ssdl-systems-thinking-foundations-deep.md`
**Source under audit:** Farrell, Hu, Chin, Branz, Evbuoma, Liem, & Ballard (2021). *Methods Briefs Series 1: Systems Thinking Foundations* (Briefs 1.02, 1.03, 1.05, 1.06, 1.07). CC BY-SA 4.0.
**Source path:** `corpus.commons/demo/sources/converted/ssdl-systems-thinking-foundations.md`
**Auditor:** claude-opus-4-7[1m], Effort: xhigh (9-pass), Date: 2026-05-13
**Calibration:** read fixtures 01 (training-data leakage), 07 (marker mismatch — [V] without verbatim), and 12 (clean negative control) at audit start.

## Audit method

Cold read of the deep reference end-to-end against the converted markdown. For every claim, marker, blockquote, and cross-reference, the question: can this be traced to a passage in the source? For markers ([V], [AP], [AR], [AE], [BT]), the question: does the marker match the source evidence?

## Findings and fixes applied

The deep reference was audited in three passes (verbatim-claim trace, marker consistency, cross-corpus drift / task-application bleed). Three issues surfaced and were corrected in place before the audit log was finalised.

### Issue 1 — Cross-corpus drift, *Matthew effects / Merton 1968*

**Location:** Brief 1.07, *Success to the successful* archetype passage.

**Issue:** the deep reference originally noted that the structural mechanism of *Success to the Successful* "is the brief's core claim about success-to-the-successful. The brief does not name *Matthew effects* (Merton 1968) by name but the dynamic is the same." The Merton reference is not in the source; introducing it as a parenthetical introduces a connection the source does not make. Strictly, the phrasing was disclaiming the connection ("does not name... but the dynamic is the same"), but the disclaimer-style introduction still imports an outside-author citation into the deep tier, which violates the deep-reference contract.

**Fix:** removed the Merton sentence. The deep reference now ends the *Success to the successful* worked-example summary at "is the brief's core claim about success-to-the-successful." If a corpus-level integration with Merton's work becomes useful, that integration belongs in the distillations' "Integration with other references" sections, not in the deep.

### Issue 2 — Cross-corpus drift, *Meadows et al. 1972 / Club of Rome* attribution

**Location:** Brief 1.07, *Limits to growth* worked-example passage.

**Issue:** the deep reference originally wrote that the *Limits to Growth* archetype's structural mechanism "is the canonical *Limits to Growth* pattern (Meadows et al. 1972, via Kim 1993 as cited by the brief) [BT]." Brief 1.07 does NOT cite Meadows et al. 1972 or the Club of Rome; the brief cites only Kim (1993), Meadows (1982) — a different work — Wolstenholme (2003), and an OCR-truncated *System Dynamics Review* paper. The Meadows-et-al-1972 attribution was imported from background knowledge.

**Fix:** rephrased to "matches the *Limits to Growth* archetype template as the brief adapts it from Kim (1993) [BT] (Brief 1.07, '+ SOURCES' reference 4)." The corrected sentence only attributes the template to a source the brief itself cites.

### Issue 3 — Marker stance softening, Wolstenholme attribution

**Location:** Brief 1.07, *Sources cited* subsection.

**Issue:** the deep reference originally stated that "Wolstenholme's *core set of archetypal structures* paper is the source for the claim that 'some even argue that four archetypes can explain all the other archetypes'." The brief does NOT explicitly attribute the four-archetypes claim to Wolstenholme by name — Wolstenholme is listed in *Sources* alongside the other references, and the four-archetypes mention appears in *Concept* without an explicit citation pointer. The inference is reasonable but the deep reference was treating it as the brief's claim.

**Fix:** softened to "Wolstenholme's *core set of archetypal structures* paper is listed in *Sources* and is the most plausible referent for the brief's mention that 'some even argue that four archetypes can explain all the other archetypes' [V] (Brief 1.07, '+ CONCEPT'), though the brief does not explicitly attribute the four-archetypes claim to Wolstenholme by name." The corresponding entry in the light reference's *Key Connections* section was softened identically.

## Items considered and judged clean

- **[V] markers across the deep reference** — spot-checked against the converted markdown for a representative sample including: the bathtub example in 1.06; the "feedback structure" sentence in 1.05; the "system structures are supported and held in place by our underlying beliefs" opening of 1.03; the "mental models are very sticky" sentence in 1.03; the five archetype template definitions in 1.07; the "*system archetypes should not be used prescriptively*" sentence in 1.07; the hike-and-broken-ankle quote in 1.02. All confirmed verbatim against the source, including the source's idiosyncratic punctuation (en-dash with surrounding spaces; smart quotes; bolded mid-paragraph phrases).

- **[BT] markers for cited authors** — every author named as [BT] (Sterman, Meadows, Senge, Kim, Wolstenholme, Johnson-Laird, Doyle & Ford, Hovmand, Black, Cronin/Gonzalez/Sterman, Andrews) is named in the brief's *Sources* or *Acknowledgements* sections. No outside-author citations imported.

- **Task-application guidance in the deep tier** — none found. Diagnostic questions, anti-pattern lists, and worked task-vocabulary examples all live in the distillations (Pass G). The deep reference's "intervention design" passages reflect what the briefs themselves say about intervention design (e.g., "change the structure of the system by adding or removing feedback loops" is a direct paraphrase of Brief 1.05's prose). The "curriculum arc" section is structural reading of the briefs' relationships, not task-application guidance.

- **Field-agnostic vs education-example distinction** — the deep reference preserves the briefs' worked examples (achievement-gap dynamics, exclusionary discipline, teacher burnout, social-worker capacity, parent-teacher trust) as [AE] author-example material. The deep reference does NOT extend the briefs' claims to "archetypes apply uniquely or primarily to education systems"; the briefs themselves are explicit that the patterns apply "in schools, in businesses, in non-profit organizations, in health systems, and in communities" [V] (Brief 1.07, opening). The distinction the operator briefed in the task prompt was honoured.

- **Brief 1.07 archetype count** — the operator's task prompt mentioned 4 archetypes (Fixes that Fail, Shifting the Burden, Tragedy of the Commons, Limits to Growth). The source itself presents **5 archetypes** (Fixes that Fail, Success to the Successful, Shifting the Burden, Drifting Goals, Limits to Growth). The deep reference correctly captures all five, names Drifting Goals as one of them, and notes explicitly that Tragedy of the Commons is NOT in Brief 1.07's selected five (though it is in the broader canonical set per Kim 2000, which Barbrook-Johnson Ch 4 also references). This was a verification catch at Pass C; the deep reference's count matches the source.

- **Conversion-artefact handling** — the deep reference flags conversion artefacts (truncated lines, fragmented sentences, missing figures) explicitly in the *Citation and source-integrity notes* section and at each location where a sentence-bridge reconstruction was applied (e.g., the Drifting Goals worked example has a bracketed reconstruction noted in the body text). No silent reconstructions.

- **Brief 1.07 acknowledgements re: Senge** — the deep reference quotes the source's explicit Senge attribution verbatim ("Some recommended resources include work by Peter Senge, including the book 'The Fifth Discipline' and 'Schools that Learn'"). [BT] marker correct. The light reference and distillations reuse this quoted material without adding any claim about Senge that the source does not make. The Senge lineage is corpus-architecturally important (SSDL is the open-licence Senge-tradition substitute) but the deep reference does not over-claim Senge's role.

- **Sterman 2006 / 2000 / 2009 cross-brief consistency** — Sterman is cited in three different briefs for three different claims: 1.02 cites Sterman 2006 (*Learning from Evidence in a Complex World*); 1.05 cites Sterman 2000 (*Business Dynamics*); 1.06 cites Cronin/Gonzalez/Sterman 2009 (*Why don't well-educated adults understand accumulation?*). All three citations match the source's *Sources* listings.

- **Hovmand cross-brief consistency** — Hovmand is cited in 1.03 (*Community Based System Dynamics*, 2014, Springer) and acknowledged in 1.06 (the ice-chomping story attribution). Both consistent with the source.

- **Distillations' "Example" sections (Pass G discipline)** — the decision-making distillation reconstructs worked examples in software-engineering vocabulary (rising production incidents diagnosed as fixes-that-fail; hiring-and-attrition as success-to-the-successful). The stakeholder-engagement distillation reconstructs worked examples in stakeholder-vocabulary (CAB-with-integrators diagnosed as shifting-the-burden; multi-stakeholder coalition as success-to-the-successful). Neither distillation preserves the source's education-equity worked examples in its *Example* section — the Pass-G translation discipline was followed.

## Audit verdict

**Pass.** Deep reference ships. Three issues identified and fixed in place; no remaining trace-test failures, no remaining marker mismatches, no remaining cross-corpus drift, no task-application guidance smuggled into the deep, no post-source vocabulary, no silent partial coverage (all five included briefs read end-to-end; the two excluded briefs are an operator-recorded scope decision, not a coverage gap).

## Audit statistics

- Claims audited: ~120 prose claims + ~30 marker-bearing sentences + 19 explicit [V] blockquote passages + 14 [BT] cross-author citations + 25 [AE] author-example references = ~210 audit-relevant elements.
- Source-anchored after fixes: ~210 / 210.
- Stripped: 1 (the Merton reference).
- Marker-corrected: 0 (no marker mismatches surfaced — the issues were citation drift, not marker drift).
- Attribution-softened: 2 (the Meadows 1972 reference; the Wolstenholme four-archetypes attribution).
- Light reference cascade fix: 1 (the Wolstenholme entry in light's *Key Connections* softened to match).
- Distillations cascade fix: 0 (both distillations were drafted after the deep audit, so the corrected deep was the input throughout; no cascade required).
