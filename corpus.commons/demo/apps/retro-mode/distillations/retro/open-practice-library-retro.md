# Open Practice Library, Retro Distillation

**Source:** Open Practice Library (Red Hat Open Innovation Labs community, 2016–present). 266 community-curated practice pages at `openpracticelibrary.com`. Licence: CC BY 4.0. Cloned commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e` (2026-05-13). Scope: open.

## Retro Relevance

The Open Practice Library projects onto the retro axis as both a practice catalogue and a principles-first warning. The library's *Retrospectives* practice carries multiple shapes (4Ls, Rose Thorn Bud, Plus Minus Interesting, Realtime Retrospective, Futurespective); its *Establish Shared Principles* practice names the failure mode of copying the shapes without the values underneath. Across the retro axis the library's most load-bearing contributions are: *1-2-4-All* for the anti-HiPPO data-gathering pattern; *Five Whys* for contributory-factor drill-down; *Design of Experiments* for converting experiments from a sticky note into a testable hypothesis with pass criteria; *Disagree and Commit* for closing on owned commitment rather than coerced consensus; *Psychological Safety* and *Establish Shared Principles* for the working-agreement infrastructure that makes blameless retro conversation possible; and *Evals* plus *Human-in-the-Loop* for the AI-adoption-era retro patterns the 2026 community cohort named. The library also carries *Blameless Postmortem* as the boundary practice between the retro and AAR axes: when the retro tips into incident review, the postmortem practice is the named transition.

## Key Concepts for Retro

1.  **Retrospectives.** "Retrospectives provide opportunities for groups to reflect, inspect and adapt their ways of working. They often take place at the end of sprints but can be scheduled at any time." The library carries multiple shapes: *4Ls Retrospective* (Liked / Learned / Lacked / Longed-for), *Rose, Thorn, Bud*, *Plus, Minus, Interesting (PMI)*, *Realtime Retrospective*, *Design Retro: Active*, *Futurespective*. (Source: Practice "Retrospectives", "What is it?") The Retrospective practice references *Five Whys* internally as the drill-down technique for Phase 3 (insight) — one of the library's explicit cross-practice compositional links.

2.  **Establish Shared Principles.** "Organizations that have done the work to articulate 'why they exist and what they believe' then need to clearly explain the 'how they will act' they will work before they move to the 'what they will do.'" The library's most self-aware contrarian: "Blindly following practices are not encouraged, establish a set of shared principles and you can weather the storms that beat at your door… Copying just the practices of successful organizations will not get us the same result if we do not also adopt the values and principles that originated these practices." (Source: Practice "Establish Shared Principles", "Why do it?", "What is it?") In a retro context this is the Phase 0 (setup) working-agreement move — before the team runs any retro shape, the principles (blameless-by-default, psychologically safe, committed to follow-through) must be named, not just assumed.

3.  **1-2-4-All.** "1-2-4-All is a way for every member of a large group to participate and generate ideas together." Anti-HiPPO: "All voices are heard, incorporating 'silent' conversations and expanding input diversity - No more HiPPOs (Highest Paid Person's Opinion)!" (Source: Practice "1-2-4-All", "Why do it?") Cited from the Liberating Structures collection. In a retro the 1-2-4-All structure is the Phase 2 (data gathering) pattern that gets every participant's account into the room before the dominant voice anchors the group. The library explicitly recommends combining with *$100 Prioritisation* for the group variant.

4.  **Five Whys.** "The 'Five Whys' is a way to figure out what causes a problem. You keep asking 'why' until you find the real reason. It was made up by Taiichi Ohno at Toyota." Anti-pattern warning: "we should ask why the process failed instead of just asking why. It's important to look for a process that's not working well or not there at all. Sometimes people will say the problem is not enough time, money, or resources. But we can't control those things." (Source: Practice "Five Whys (5 Whys)", "Why do it?") Used at Phase 3 (insight / cause analysis). Referenced from inside *Retrospectives* as the primary drill-down technique.

5.  **Design of Experiments.** "The Design of Experiments is the practice we use to turn ideas, hypothesis and/or assumptions into concrete well defined set of experiments which can be carried out in order to validate those ideas, hypothesis and assumptions, i.e. provide us with valuable learning." Minimum design fields: Hypothesis / Current Condition / Target Condition / Obstacles / Pass criteria / Measures / Learning. The practice's contrarian: "Successful experiments are not experiments that have proven our assumption as correct. Successful experiments are those that provide valid and reliable data which shows a statistically significant conclusion." (Source: Practice "Design of Experiments", "What is it?", "How to do it?") Used at Phase 4 (experiment design) — converting a retro sticky note into a well-structured experiment that produces valid learning whether or not the hypothesis is confirmed.

6.  **Disagree and Commit.** "An approach to enable teams to transition from thinking to doing, whilst ensuring the team are committed to the execution." Against coerced consensus: "There is a common misconception that collaboration eventually requires consensus; it does not. In fact consensus can come at a very high cost to the team dynamic." Two pre-conditions: "everybody must have a meaningful choice, and there must be an agreed review point." (Source: Practice "Disagree and Commit", "What is it?", "Why do it?") Used at Phase 4 (experiment design) and Phase 5 (close) — the move that lets the team commit to one or two experiments without forcing unanimity and without leaving dissent latent.

7.  **Psychological Safety.** The library treats psychological safety as a named practice delivered through named facilitation primitives. "It gives everyone the opportunity to speak up and be heard. This prompts the behaviour and gives permission for each person to share their own insights, establishing a good foundation for psychological safety." (Source: Practice "Check-ins", "Why do it?") The retro's safety infrastructure is the library's facilitation default: check-ins, social contract, blameless-conversation posture. When the safety check returns low (1-2), the library routes to Establish Shared Principles before content — matching the retro.md task spec's Phase 0 rule.

8.  **Blameless Postmortem.** "Blameless Postmortem is a post-incident practice assessing an incident or other types of outages, its timeline, environment conditions, and all possible factors that lead an incident to happen." Two foundations: "Availability of the information regarding the incident" and "Psychological safety of all participants that promotes speaking up openly." (Source: Practice "Blameless Postmortem", "What is it?", "How to do it?") In a retro context, the Blameless Postmortem is the boundary practice: when blame language surfaces in a team retro about an incident, the retro should either run the Blameless Postmortem shape or route to the AAR axis. The postmortem practice references *Wheel-of-Misfortune* as a follow-on training practice.

9.  **Backcasting / Pre-mortem.** "The method originates from Gary Klein (HBR article) and was made popular by the Nobel prize winner Daniel Kahneman in his book 'Thinking Fast and Slow.'" Imagine the experiment has failed; reconstruct the reasons. (Source: Practice "Backcasting / Pre-mortem", "What is it?") In a retro, the Pre-mortem move is used at Phase 4 (experiment design): before the team commits to an experiment, "if this experiment fails badly in three weeks, what will the reasons turn out to have been?" — surfaces the assumptions the experiment must hold and the obstacles the design needs to address.

10.  **Impact-Effort Prioritisation Matrix and RICE.** Two-axis 2×2 (high/low impact × high/low effort) and Reach × Impact × Confidence ÷ Effort. Used at Phase 4 (experiment design) when the retro has surfaced more possible improvements than the team can run. The library's approach: "Where does each option land on impact × effort?" gives a visible quadrant-based triage; RICE adds a quantified comparison when the quadrant is not enough. Paired with the Open Kanban one-constraint discipline borrowed-through the retro task spec — the prioritisation tools help the team find the one experiment that matters.

11.  **Establish Shared Principles for the AI-era retro.** When the team is overwhelmed by AI tool adoption the library's 2026-era practices name the relevant patterns: *Evals* for AI overconfidence ("Traditional tests give you certainty. Evals give you confidence") and *Human-in-the-Loop* for silent AI delegation ("A computer can never be held accountable, therefore a computer must never make a management decision"). (Source: Practice "Evals", "What is it?"; Practice "Human in the loop", "Why do it?") The retro move: surface the AI-adoption-era wicked question using Establish Shared Principles — what principles govern the team's use of AI tools, before the team makes commitments about adoption or delegation?

12.  **Dissent Cards.** "It's a way to encourage greater diversity of ideas and increase the psychological safety necessary for disagreement to occur productively within the group. This practice is taken from L. David Marquet's book, 'Leadership is Language.'" Red-card-must-dissent / black-card-free-choice mechanic, 1:5 ratio. (Source: Practice "Dissent Cards", "What is it?") Used at Phase 4 (experiment design) when artificial consensus is suspected — the mandatory-dissent red card makes it structurally safe to voice the concern the team member has been holding.

## Questions to Ask During Retro

### Phase 0 — Setup

| Need | Question |
|---|---|
| Is the room psychologically safe? | Have we done a check-in? Is there a social contract in place? If safety check returns 1-2, run Establish Shared Principles before content. |
| Are the principles named, not just the practices? | Establish Shared Principles: "why do we run blameless retros?" — before asking people to speak candidly, name the principle that makes candour safe. |
| Is this a retro or a postmortem? | If an incident just happened and the team is mid-incident, route to the Blameless Postmortem practice and the AAR axis. |

### Phase 0.5 — Experiment review

| Need | Question |
|---|---|
| Last retro's experiments weren't done | Was the experiment owned? If not, the design failed, not the team — redesign with Design of Experiments' named-owner field. |
| Experiments done but results unclear | Design of Experiments' "Learning" field: what did the data show? Did the experiment pass its stated pass criteria? |
| Team allergic to "experiments" language | Establish Shared Principles: surface why the word lands wrong before swapping vocabulary. |

### Phase 1 — Priming

| Need | Question |
|---|---|
| Which retro shape to use | Retrospectives carries multiple shapes — 4Ls, Rose Thorn Bud, PMI, Futurespective. Match the shape to the team's state, not to the facilitator's preference. |
| Team overwhelmed by AI adoption | Establish Shared Principles + Evals + Human-in-the-Loop: what principles govern AI use on this team? Surface the wicked question before committing to practices. |

### Phase 2 — Data gathering

| Need | Question |
|---|---|
| One voice dominating | 1-2-4-All: individual → pairs → groups of 4–6 → whole group. No HiPPO anchoring before the small-group round. |
| Team agrees too quickly | Dissent Cards: the mandatory red-card move makes it structurally safe to voice the concern held in silence. |
| Blame language surfacing | Blameless Postmortem's framing: "Our job is not to point fingers — our job is to figure out why." |

### Phase 3 — Insight / cause analysis

| Need | Question |
|---|---|
| Surfacing contributory factors | Five Whys: "Keep asking 'why' until you find the real reason" — redirect from resources to process failure. |
| Same pattern appearing three retros running | Five Whys beyond five: keep going until the structural cause emerges. SSDL system archetypes (available cross-axis) as hypothesis-generators. |
| Blame language persisting | Blameless Postmortem: "Our job is not to point fingers at an unlucky engineer." If the retro is tipping into incident review, route to the AAR axis. |

### Phase 4 — Experiment design

| Need | Question |
|---|---|
| Converting stickies to experiments | Design of Experiments: Hypothesis / Current Condition / Target Condition / Obstacles / Pass criteria / Measures / Learning — for each proposed experiment. |
| Testing the experiment before committing | Backcasting / Pre-mortem: if this experiment fails in three weeks, what will the reasons turn out to have been? |
| Prioritising when there are too many | Impact-Effort matrix: where does each experiment land on impact × effort? RICE when a quantified comparison is needed. |
| Committing without coercing consensus | Disagree and Commit: everybody must have a meaningful choice; there must be an agreed review point. |
| Dissent latent but unspoken | Dissent Cards: the mandatory red-card mechanic makes disagreement structurally safe. |

### Phase 5 — Close

| Need | Question |
|---|---|
| Reading back commitments | Named owner, named date, named pass criteria from the Design of Experiments fields — before the room clears. |
| Maintaining working agreements | Retrospectives + Establish Shared Principles: are the principles visible enough that the team can apply them to the next retro without starting from scratch? |
| Safety check low at close | Address safety before the next retro — run Establish Shared Principles as the opening move next time. |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| One voice anchors Phase 2 before others have written | HiPPO dynamic | 1-2-4-All: individual → pairs → groups of 4–6 → whole group |
| Team agrees quickly in Phase 2 | Artificial consensus; dissent is latent | Dissent Cards: the mandatory red-card move makes disagreement structurally safe |
| Experiments on the board at close have no pass criteria | Design of Experiments structure not applied | For each experiment: name the Hypothesis, Current Condition, Target Condition, Pass criteria |
| Team commits collectively but no individual owns it | Disagree-and-Commit's two pre-conditions not met | Name who specifically commits; set the agreed review point |
| Retro is surfacing blame about a specific incident | Retro is tipping into incident review | Route to the Blameless Postmortem practice and the AAR axis |
| Team is anxious about AI tool adoption | No named practice for the pattern | Establish Shared Principles + Evals + Human-in-the-Loop: what principles govern AI use? |
| Experiment confirmed the hypothesis — team celebrates | Success defined as confirmation, not as valid learning | Disagree and Commit's contrarian: successful experiments provide valid data, not just confirmation |

## When to Use This Reference

Reach for this distillation when:
- The team needs a named practice catalogue for a specific retro moment: 1-2-4-All for anti-HiPPO, Design of Experiments for experiment structure, Disagree-and-Commit for close discipline, Dissent Cards for latent dissent, Backcasting for pre-mortem.
- The team wants to match a retro shape to its current situation — the library carries multiple shapes (4Ls, Rose Thorn Bud, PMI, Futurespective) and the guidance is to match shape to state, not facilitator preference.
- The retro is tipping into incident review — the Blameless Postmortem practice is the named boundary.
- AI adoption is surfacing in retro data and the team needs named practices rather than improvised responses.
- The team is running a retro shape borrowed from another team without examining the principles underneath.

Pair with the Approach Perfect Field Guide for the protocol container and Liberating Structures for the facilitation-craft layer within phases.

## Worked Example

A team runs a retro after a major feature deployment that went poorly. Phase 0: the lead checks whether this is a retro (team-internal learning) or a Blameless Postmortem (incident review). The incident happened in production and affected users. The lead routes to the Blameless Postmortem practice for the incident analysis and keeps the team retro for the process retrospection.

In the retro, Phase 2 uses 1-2-4-All: everyone writes, then pairs, then groups, then whole group. Two themes emerge that wouldn't have surfaced with verbal-first: "we don't have a shared understanding of our deployment criteria" and "we approved the deploy at 4pm on a Friday."

Phase 4: three experiments are proposed. The lead applies Design of Experiments to each: Hypothesis / Current Condition / Target Condition / Obstacles / Pass criteria / Measures / Learning. One experiment fails immediately — no one can state what would confirm the hypothesis. It is removed. The remaining two have pass criteria.

Closing: one person privately disagrees with the second experiment. Dissent Cards: the mandatory red-card move makes it structurally safe to voice this. The team opens the conversation before committing. The Disagree-and-Commit close: the dissenter agrees to commit with the named review point in two Sprints.

The 1-2-4-All anti-HiPPO structure, Design of Experiments scaffold, Blameless Postmortem boundary, Dissent Cards mechanic, and Disagree-and-Commit close all trace to the Open Practice Library (Practice "1-2-4-All"; Practice "Design of Experiments"; Practice "Blameless Postmortem"; Practice "Dissent Cards"; Practice "Disagree and Commit").

## Anti-patterns This Reference Helps Avoid

- Copying the Retrospective practice from another team without the psychological-safety and blameless-conversation principles that make it work — the Establish Shared Principles contrarian names this failure mode directly.
- One voice anchors the data-gathering phase before others have spoken — solved by 1-2-4-All's structural anti-HiPPO sequencing.
- Five experiments on the board at close, none structured as testable hypotheses with pass criteria — solved by Design of Experiments' minimum design fields.
- Closing on collective intention rather than owned commitment — solved by Disagree and Commit's two pre-conditions (meaningful choice + agreed review point).
- Treating resource shortage as the root cause when the Five Whys drill would reveal a process failure — the Five Whys anti-pattern warning addresses this directly.
- Artificial consensus achieved through coercion rather than genuine agreement — solved by Dissent Cards' mandatory-dissent structure.
- The retro tips into incident review but the team stays in retro mode — the Blameless Postmortem and the AAR axis are the named boundary; route when blame language or incident-specific analysis is required.
- Treating an experiment as successful because it confirmed the hypothesis — the Design of Experiments contrarian: "Successful experiments are not experiments that have proven our assumption as correct."
- Skipping the Pre-mortem before committing to a high-risk experiment — the Backcasting / Pre-mortem move surfaces the assumptions that must hold before the team commits.
- AI tool adoption driving retro anxiety without a named practice for the pattern — solved by Evals (AI overconfidence) and Human-in-the-Loop (silent delegation) as named practices the team can surface explicitly.

## Integration with Other References

| Reference | Relationship |
|---|---|
| Approach Perfect Field Guide | The Field Guide supplies the five-segment agenda container; OPL supplies the practice catalogue for specific moves within each phase |
| Liberating Structures Handbook | OPL carries 1-2-4-All from the LS collection; LS supplies additional moves (TRIZ, Troika Consulting, Discovery & Action Dialogues) that OPL's retro practice doesn't carry |
| Open Kanban | OPL's Design of Experiments formalises the hypothesis that Open Kanban's learning-before-improvement principle demands |
| TC 25-20 Army AAR | OPL's Blameless Postmortem and TC 25-20's discovery-over-critique frame are the boundary practices for the retro-vs-AAR distinction |
| Scrum Guide 2020 | OPL's Retrospective practice is the practitioner complement to the Scrum Guide's structural definition of the Sprint Retrospective |
| LFUO Learning Review Guide | LFUO's Five Hows and OPL's Five Whys are complementary Phase 3 tools; LFUO adds the counterfactual prohibition and networked-causality framing that Five Whys alone doesn't supply |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The OPL carries extensive borrowed-through lineages within individual practices: Lean Coffee (Jim Benson and Jeremy Lightsmith) [BT]; Backcasting / Pre-mortem (Gary Klein, via Kahneman) [BT]; RICE prioritisation (reach × impact × confidence ÷ effort) as a named methodology [V]; Dissent Cards (L. David Marquet, *Leadership is Language*) [BT]; Human-in-the-Loop attribution note for machine decision-making [V]; Evals (Karpathy's "march of nines" framing) [BT]. The Liberating Structures collection is cited for 1-2-4-All [BT]. The Five Whys is attributed to Taiichi Ohno at Toyota [BT]. None of Marquet, Klein, Kahneman, Karpathy, or Ohno are held directly in this corpus.

**Named limits of the source.** The OPL is a community-curated library with 266+ practices; this distillation covers the subset most applicable to the retro axis. The library is a living document — the commit used (8bfa450e75dfba1e2a3c68ac0e514e587f6f116e, 2026-05-13) is a snapshot. Individual practice pages carry varying levels of depth; some are well-developed, others are stubs. The retro axis projection draws primarily from the more fully developed practices (Retrospectives, Establish Shared Principles, 1-2-4-All, Design of Experiments, Disagree and Commit, Blameless Postmortem, Dissent Cards, Backcasting, Evals, Human-in-the-Loop).

**Evidence-marker continuity.** "Traditional tests give you certainty. Evals give you confidence" is `[V]` in the deep ref with an `[AR]` marker (reasoned assertion); the distillation carries the distinction without softening. "Successful experiments are not experiments that have proven our assumption as correct" is `[V]` in the deep ref; the distillation carries this as the Design of Experiments contrarian. "A computer can never be held accountable, therefore a computer must never make a management decision" is `[V]` in the deep ref; the distillation applies the principle to the AI-adoption retro pattern. The Disagree-and-Commit pre-conditions (meaningful choice + agreed review point) are `[V]` in the deep ref; the distillation carries both precisely.
