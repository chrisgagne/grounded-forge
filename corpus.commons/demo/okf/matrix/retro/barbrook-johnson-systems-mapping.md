---
type: distillation
title: "Barbrook-Johnson & Penn, Systems Mapping"
description: "Barbrook-Johnson & Penn, Systems Mapping, projected onto the retro task axis; evidence markers and attribution travel in-band."
resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
tags: [distillation, retro]
task: retro
scope: open
sources:
  - id: barbrook-johnson-systems-mapping
    title: "Barbrook-Johnson, P., & Penn, A. S. (2022). Systems Mapping: How to build and use causal models of systems. Palgrave Macmillan / Springer Nature, Cham. ISBN 978-3-031-01833-6. DOI: https://doi.org/10.1007/978-3-031-01919-7. Licence: CC BY 4.0. Scope: open. Seven methods covered: Rich Pictures, Theory of Change, Causal Loop Diagrams, Participatory Systems Mapping, Fuzzy Cognitive Mapping, Bayesian Belief Networks, System Dynamics."
    resource: https://link.springer.com/book/10.1007/978-3-031-01919-7
generated:
  by: grounded-forge/0.4.0
  at: 2026-09-28T15:12:32+13:00
---
# Barbrook-Johnson & Penn, Systems Mapping, Retro Distillation

**Source:** Barbrook-Johnson, P., & Penn, A. S. (2022). *Systems Mapping: How to build and use causal models of systems*. Palgrave Macmillan / Springer Nature, Cham. ISBN 978-3-031-01833-6. DOI: https://doi.org/10.1007/978-3-031-01919-7. Licence: **CC BY 4.0**. Scope: open. Seven methods covered: Rich Pictures, Theory of Change, Causal Loop Diagrams, Participatory Systems Mapping, Fuzzy Cognitive Mapping, Bayesian Belief Networks, System Dynamics.

## Retro Relevance

Barbrook-Johnson & Penn's method catalogue projects onto the retro axis at phases where the team needs to move beyond flat lists of problems and quick-fix experiments. Two methods carry the most load. Rich Pictures (Ch 2) give the data-gathering phase a participatory, low-overhead tool for externalising each team member's picture of the sprint before the group negotiates a shared view — particularly useful when the team has diverse roles whose vantage points rarely surface in a standard sticky-note format. Causal Loop Diagrams (Ch 4) give Phase 3 a shared-model artefact for recurring problems: when the same issue returns for the second or third retro, a CLD built together surfaces the feedback structure that is keeping the problem in place. The book's core warning — the "horrendogram" failure mode where a map overwhelms rather than clarifies — is directly applicable to retro Phase 3: a CLD should focus on the core system engine (the one or handful of central variables) and the feedbacks around it rather than attempting to map the whole sprint's complexity. The appropriateness triangle from Ch 11 applies: if feedback loops are not present, or important, in the recurring problem, a CLD "will be less useful" [V] (Ch 4, "What Are Causal Loop Diagrams Good and Bad At?").

## Key Concepts for Retro

**Appropriateness triangle for tool selection (Ch 11, "Comparing, Choosing, and Combining Systems Mapping Methods"; Fig. 11.1 in "Choosing Systems Mapping Methods")** The retro facilitator applies this to Phase 3: does the recurring problem's complexity warrant a CLD, or does a simpler tool suffice? Defaulting to CLDs for every recurring problem is the hammer-and-nail failure mode.

2.  **Rich Pictures as low-barrier data-gathering tool (Ch 2, "What Are Rich Pictures?")** — "Rich Pictures are a drawing, a picture, of a system or 'situation'" [V]; "very few, if any, prompts are given by facilitators beyond asking them to 'draw the system'" [V]. Rich Pictures externalise each person's view of the sprint in a way that written stickies often suppress: relationships, tensions, emotional load, communication gaps. Useful in Phase 2 when the team holds strongly different views of what the sprint was like that haven't been surfaced yet.

3.  **Rich Pictures surface what formal methods cannot (Ch 2, "What Are Rich Pictures Good and Bad At?")** — strengths include flexibility, openness, the ability to capture different perspectives, values and perceptions, and a low barrier to participation; "even in a tricky process... there is still something to work with" [V]. Weaknesses: Rich Pictures "will never" formalise knowledge precisely or feed directly into a CLD. They are a sense-making precursor, not a causal model.

4.  **Rich Picture facilitation: give power to participants (Ch 2, "Common Issues and 'Tricks of the Trade'")** — key facilitator moves include using an icebreaker, leaving the room while participants draw ("give power to the participants" [V]), and not trying to force-fix issues during the session. In a retro context: assign small groups of three to six, give them the prompt ("draw what this sprint felt like"), and step back.

5.  **Causal Loop Diagrams for recurring-problem analysis (Ch 4, "What Is a Causal Loop Diagram?")** — "CLDs represent a system in three basic elements: boxes, connections, and feedback loops." [V] When the same retro topic reappears, a CLD built collaboratively surfaces the feedback structure that may be keeping the problem alive.

6.  **The core system engine (Ch 4, "What Is a Causal Loop Diagram?")** — "The feedback loops are usually focused around a 'core system engine', which is a set of nodes that are the core of the system" [V]. In a retro context: start with the two or three variables the team agrees are at the heart of the recurring problem, and build the feedback loops between them before expanding outward. Keep the first draft to twenty nodes maximum.

7.  **The horrendogram failure mode (Ch 1, "How Can Systems Mapping Be Useful?")** — "system maps are sometimes referred to as 'horrendograms', and much worse (!), when they show us the complexity of a system in an unfiltered manner." [V] A retro CLD that grows to cover everything that happened in the sprint is an anti-pattern. The response: tune the map's complexity to the team's visual literacy, and "allocate half of your resources to design and communication" [V] (Ch 4, "Commons Issues and 'Tricks of the Trade'").

8.  **Process value over product (Ch 12, "Our Final Take-Home Messages")** — "the opportunity to reflect and generate understanding with others is surprisingly powerful. Often more so than delivering 'answers'." [V] The CLD built in Phase 3 is most valuable for the conversation it generates — the shared negotiation of the system's structure — not for the diagram it leaves behind.

9.  **Maps as boundary objects (Ch 9, "Defending the Use of a Participatory Process to Build and Use Your Map")** — participatory maps "become 'boundary objects' (see Star & Griesemer, 1989) around which stakeholders and researchers can learn" [V] [BT]. The map and the facilitator become "interested amateurs" that participants can critique and improve without the critique attaching to any individual. In a retro, this is the mechanism that lets the team argue about the diagram rather than about each other.

10.  **Theory of Change for experiment design (Ch 3, "What Is Theory of Change Mapping?")** — a ToC traces inputs through activities, outputs, outcomes, and impacts. In retro Phase 4, a lightweight ToC for a proposed experiment forces the team to state the causal theory: *this experiment produces these outputs, which lead to this outcome, because...* Surfacing the assumption in each causal link makes the experiment testable.

11.  **ToC diagrams are theories, not reality maps (Ch 3, "What Is Theory of Change Mapping?")** — "ToCs are theories, they represent the mental models of the people who constructed them. They are not maps of reality and they may contain gaps and ambiguities." [V] A retro experiment design that cannot be traced through even a rough ToC has no stated causal theory.

12.  **Participatory mapping in data-poor contexts (Ch 9, "Defending the Use of a Participatory Process to Build and Use Your Map")** — "when working in a genuine complex adaptive system, it is highly unlikely we will have access to the breadth or depth of quantitative data or evidence we need to formally validate every node and edge in a system map." [V] Teams rarely have data on why a sprint pattern persists. Participatory map-building from the team's experience is the appropriate response — the discipline is to be explicit about what the map is and is not claiming.

## Questions to Ask During Retro

### Phase 2: Data gathering

| Need | Question |
|---|---|
| The team holds different pictures of the sprint and quick agreement is likely to paper over the differences | Ask each small group to draw their picture of the sprint — no formal structure. What does each picture show that the others leave out? Where do they disagree on what the sprint felt like? (Rich Pictures, Ch 2, "What Are Rich Pictures?") |
| Safety is low or dominant voices are shaping the data-gathering phase | If a dominant voice is likely, manage it at planning and inviting: separate groups or sessions (Ch 2, "Common Issues and 'Tricks of the Trade'"; Ch 10, "Common Issues"). During the drawing itself, the facilitator gives away their own power by leaving the room (Ch 2, "Common Issues and 'Tricks of the Trade'"). |
| The team is producing stickies that cluster into the same two buckets every retro | Shift from sticky notes to drawing. What relationships, tensions, and communication gaps appear when people draw rather than list? (Ch 2, "What Are Rich Pictures?") |

### Phase 3: Insight and cause analysis

| Need | Question |
|---|---|
| A problem is recurring for the second or third retro | Build a CLD together. Start with the core system engine: what are the two or three variables at the centre of this problem, and which feedback loops connect them? Build the first diagram around the engine, up to about twenty nodes ("Twenty nodes seem to be a useful limit here" [V]). (Ch 4, "How Do You Create Causal Loop Diagrams?") |
| The team has drawn a CLD and it is getting large and unwieldy | Extract a submap: pick the factor the team agrees is most important and map one to two steps upstream and downstream. What is driving it? What is it driving? (Ch 5, "What Is Participatory Systems Mapping?") |
| Participants are defending their positions rather than negotiating the map | The map is a boundary object. Redirect: *the map says X causes Y — does your experience confirm or contradict that link? What would you change?* The shared task is improving the map, not winning the argument. (Ch 9, "Defending the Use of a Participatory Process to Build and Use Your Map") |
| The team's CLD is growing into a horrendogram | Interrupt and refocus on the core system engine. Introduce the rest in steps (colour-code or group it by theme) rather than deleting it; for a large map, work through submaps. (Ch 4, "Commons Issues and 'Tricks of the Trade'"; Ch 5, "What Is Participatory Systems Mapping?") |
| The facilitator wants to check whether a systems-mapping tool is warranted | Are feedback loops present and important here? If not, a CLD "will be less useful" [V]. (Ch 4, "What Are Causal Loop Diagrams Good and Bad At?") |

### Phase 4: Experiment design

| Need | Question |
|---|---|
| The team has agreed on an experiment and wants to ensure it has a stated causal theory | Trace the ToC: what is the experiment, what does it produce, what does it change in the system, and what is the intended long-term effect? Name the assumption in each causal link — that is the hypothesis the experiment will test. (Ch 3, "How Do You Create Theory of Change Diagrams?") |
| The proposed experiment has been tried before with no lasting effect | Which feedback loop in the CLD does this experiment address? Does the experiment disrupt the vicious cycle or only one of its symptoms? What would addressing the loop directly require? (Ch 4, "Commons Issues and 'Tricks of the Trade'") |
| The team has multiple candidate experiments and wants to prioritise | Use the CLD from Phase 3: which experiment would disrupt a vicious cycle or strengthen a virtuous one? (Ch 4, "Commons Issues and 'Tricks of the Trade'") |

### Phase 5: Close

| Need | Question |
|---|---|
| The retro is closing and the team wants to capture the causal model | The CLD is a living document. Photograph and digitise it. Name the key loops. Return to it at the next retro when the same problem surfaces — ask whether the structure has changed, and whether the experiment addressed a loop or an event. (Ch 12, "Our Final Take-Home Messages") |
| The team wants to remember the insight without carrying a complex diagram forward | Identify the one feedback loop that best names the recurring pattern. Give it a short label the team will recognise next retro. The process generated the insight; the label is what travels forward. (Ch 12, "Our Final Take-Home Messages") |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| The same retro topic returns for the second or third Sprint | A feedback structure may be keeping the problem in place | Build a CLD — start with the core system engine (two or three variables) before expanding |
| Sticky notes cluster into the same two buckets every retro | One mental model is dominating the data-gathering phase | Switch from stickies to Rich Pictures; give small groups a blank page and a prompt, then step back |
| Participants defend their positions rather than negotiating the map | The map is not yet a boundary object; discussion is still personal | Redirect to the map: "the map says X causes Y — does your experience confirm that link?" |
| The CLD is growing large and unwieldy | Horrendogram failure mode; complexity overwhelming rather than clarifying | Extract a submap: pick the most important factor and map one to two steps upstream and downstream |
| The team's proposed experiment has been tried before without lasting effect | The experiment targets a symptom, not a feedback loop | Identify which loop the experiment addresses; does it disrupt the vicious cycle or only one of its symptoms? |
| Quick consensus on the retro's top theme | Rich Picture surfaces tensions the sticky-note format suppresses | Ask each sub-group to draw rather than list; what appears in the drawing that doesn't appear on the board? |

## When to Use This Reference

Reach for this distillation when:
- A problem has recurred for two or more retros and previous experiments have not held — this is the signal that a feedback structure is in play and a CLD is warranted.
- The team holds strongly different views of the sprint that have not been externalised — Rich Pictures at Phase 2 are the low-barrier tool for surfacing those views before discussion anchors the group.
- An experiment is proposed without a stated causal theory — the Theory of Change framework forces the team to name the assumption in each causal link.

Do not reach for this distillation on simple, one-off retro topics. Apply the appropriateness triangle first: do the project's purpose and constraints and the system's characteristics fit a CLD (Ch 11)? If feedbacks are not important, a CLD "will be less useful" [V] (Ch 4, "What Are Causal Loop Diagrams Good and Bad At?").

## Worked Example

A backend-platform team has named "release pipeline slowness" in three consecutive retros. Each retro produced an experiment: first, adding a fast-check gate; second, parallelising the test suite; third, caching build artefacts. None held. In Phase 1 of the fourth retro, the facilitator applies the appropriateness triangle across its three corners. The project: a single retro session with a team comfortable reading diagrams. The system: dev, ops and QA all involved, changes in one Sprint affecting the next, and a recurring pattern. The method: CLDs suit systems where feedbacks matter. A CLD fits.

Phase 2 uses Rich Pictures instead of stickies. Three sub-groups of three draw their picture of "the sprint." The QA group draws a funnel with a narrow bottleneck; the dev group draws a pipeline with branches tangling; the ops group draws a chain of handoffs with question marks at each node. Each picture shows something the others leave out. The facilitator photographs all three and asks: what relationship appears in all three pictures? The answer: every picture has a handoff where context is lost.

Phase 3 builds a CLD. The core system engine: "handoff count" → "context loss per handoff" → "rework needed" → "pipeline time" → "handoff count" (reinforcing loop: more rework increases the pressure to hand off rather than pair). The team recognises the loop. Previous experiments addressed pipeline speed, not handoff volume.

Phase 4 ToC: if the team reduces handoff count by pairing ops and dev on release steps (experiment), then context loss decreases, rework decreases, pipeline time decreases, and the reinforcing loop weakens. The assumption named: pairing is feasible within current capacity.

The appropriateness triangle, Rich Picture facilitation, the CLD core engine, and the ToC structure are all from Barbrook-Johnson & Penn (Ch 2, "What Are Rich Pictures?"; Ch 3, "What Is Theory of Change Mapping?"; Ch 4, "What Is a Causal Loop Diagram?"; Ch 11). The triangle the facilitator ran in Phase 1 rests on this passage:

> "It involves triangulating between the purpose, needs, and constraints of your project; the characteristics of the system and context you are working in; and the nature of the methods you are considering using. Where a method fits with both the project and the system, we can say it is an 'appropriate' method." [V] (Ch 11, "Comparing, Choosing, and Combining Systems Mapping Methods")

## Anti-patterns This Reference Helps Avoid

- Defaulting to a CLD for every recurring retro topic without applying the appropriateness triangle — CLDs are overhead on simple problems.
- Building a retro CLD that grows into a horrendogram: attempting to map the full sprint rather than focusing on the core system engine of the recurring problem.
- Treating the CLD or Rich Picture as a product to deliver rather than as a process that generates shared understanding through the conversation of building it.
- Skipping the Rich Picture phase and going straight to sticky notes when team members hold strongly different views of the sprint that haven't yet been externalised.
- Proposing an experiment in Phase 4 without tracing its Theory of Change — without a stated causal theory, the experiment cannot be designed to test anything specific.
- Letting the facilitator's method familiarity drive the choice of tool — picking CLDs because they are familiar, not because the problem's complexity warrants them.
- Treating the participatory map as a rigorous causal model rather than as a structured expression of the team's collective mental models, and making strong causal claims the data cannot support.
- Allowing the CLD-building process to remain entirely inside the workshop without capturing the insight as a shared commitment and a named experiment before the team leaves the room.
- Letting the facilitator hold the pen on the CLD: the method already puts a lot of power in the researcher's hands (Ch 4, "What Are Causal Loop Diagrams Good and Bad At?"), which sidelines the team's lived knowledge of the sprint. For the separate warning against introducing archetypes too early in a group session, see SSDL Brief 1.07.

## Integration with Other References

| Reference | Relationship |
|---|---|
| SSDL Systems Thinking Foundations | SSDL's five system archetypes are hypothesis-generators; Barbrook-Johnson's CLD method is the tool for testing and building the shared causal model the archetype suggests |
| Liberating Structures Handbook | LS's TRIZ inversion is a Phase 3 complement to CLDs: before building the map, invert to name the system that makes the problem inevitable |
| Open Kanban | Open Kanban's Holistic or Systemic Approach to Change (Deming + Goldratt borrowed-through) provides the values argument for why feedback-structural analysis matters; Barbrook-Johnson provides the method |
| Org Topologies Primer | When the CLD's core system engine is a structural constraint (team archetype mismatch), OT's ASSESS step names the strategy-design mismatch and its DESIGN and ELEVATE steps give the change path; Barbrook-Johnson supplies the diagnostic tool |
| FLO Facilitation Guide | FLO's scaffolding-then-fading arc (facilitators "step back" as the group develops) parallels this source's "give power to the participants" trick for Rich Pictures |
| OpenStax Psychology 2e | Psychology 2e's conformity research (Asch; normative social influence) explains the dominance risk this source names for Rich Pictures and why power dynamics must be managed at planning; Barbrook-Johnson supplies the method, Psychology 2e supplies the social-psychology rationale |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The source cites Meadows (2008) for the systems definition [BT] (Ch 1, "What Is Systems Mapping?") and Star & Griesemer (1989) for the boundary-object concept [BT] (Ch 9, "Defending the Use of a Participatory Process"). Gareth Morgan is cited for the 15-percent-control framing but this appears in the Liberating Structures Handbook, not in Barbrook-Johnson. Sterman's *Business Dynamics* underlies System Dynamics and is borrowed-through in the quantitative chapters. None of Meadows, Star & Griesemer, or Sterman are held directly in this corpus; this distillation cites Star & Griesemer only as the source of the boundary-object term (borrowed-through).

**Named limits of the source.** The book explicitly limits its scope to seven methods that "represent causality and influence in a system, and methods which can be used in a participatory way" [V] (Ch 1, "What Systems Mapping Methods Are in This Book?"). It excludes other mapping methods listed in its Table 1.2 (not recoverable from the converted text) and broad schools of practice such as participatory action research. System Dynamics and Bayesian Belief Networks are more formal and slower to build (System Dynamics "requires a relatively large amount of time to conduct compared to other methods" [V]; eliciting BBN conditional probabilities "can create rather repetitive conversations" [V]), so this distillation focuses on Rich Pictures, CLDs, ToC, and PSM as the retro-applicable subset (Ch 7, "Common Issues and 'Tricks of the Trade'"; Ch 8, "What Is System Dynamics Good and Bad At?"). The source's own warning about the "increasingly fast-paced nature of work" [V] — if you get half a day, use it well — is the discipline for limiting retro CLD sessions to what the team can build and use in the time available (Ch 1, "Why Think About Systems Mapping Now?").

**Evidence-marker continuity.** Quotations marked `[V]` match the source word for word and are copied from the deep ref: the appropriateness definition (Concept 1, and the Worked Example blockquote), the Rich Pictures definition (Concept 2), "even in a tricky process... there is still something to work with" (Concept 3), "give power to the participants" (Concept 4), the CLD elements and core-engine sentence (Concepts 5, 6), the horrendogram passage and the half-resources trick (Concept 7), the process-value passage (Concept 8), the boundary-object sentence (Concept 9, `[BT]` to Star & Griesemer), the ToC-as-theory passage (Concept 11), the data-poor passage (Concept 12), and the twenty-node limit and CLD limit in the Phase 3 table and When to Use, and the scope criterion, System Dynamics time cost, BBN elicitation and fast-paced-work quotations in Named limits. Rich Picture strengths are paraphrase in the deep ref and are paraphrased here.

## Related concepts

**Same source, other task axes:** [aar](../aar/barbrook-johnson-systems-mapping.md) · [decision-making](../decision-making/barbrook-johnson-systems-mapping.md) · [software-business](../software-business/barbrook-johnson-systems-mapping.md) · [stakeholder-engagement](../stakeholder-engagement/barbrook-johnson-systems-mapping.md)

- [SSDL Systems Thinking Foundations](ssdl-systems-thinking-foundations.md) — shared: Causal Loop Diagrams, Group Model Building, System Dynamics, Systems Thinking
- [Liberating Structures Handbook](liberating-structures-handbook.md) — shared: Complex Adaptive Systems, Facilitation, Participatory Design
- [Jones, Evidence-Based Software Engineering](jones-evidence-based-sweng.md) — shared: Regression Modeling, Statistics
- [US Forest Service LFUO 2024](lfuo-learning-review-guide-2024.md) — shared: Systems Thinking
- [NHS Improvement Just Culture Guide](nhs-just-culture-guide.md) — shared: Systems Thinking
- [Open Kanban](open-kanban.md) — shared: Systems Thinking
- [Open Practice Library](open-practice-library.md) — shared: Facilitation
- [Krivitsky, Larman & Flemm, Org Topologies Primer](org-topologies-primer-2025.md) — shared: Systems Thinking
