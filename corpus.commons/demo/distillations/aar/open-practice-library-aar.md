# Open Practice Library, AAR Distillation

**Source:** Open Practice Library (Red Hat Open Innovation Labs community, 2016–present). 266 community-curated practice pages at `openpracticelibrary.com`. Licence: CC BY 4.0. Cloned commit `8bfa450e75dfba1e2a3c68ac0e514e587f6f116e` (2026-05-13). Scope: open.

## AAR Relevance

The Open Practice Library projects onto the AAR axis through its reliability and learning practices, its blameless-conversation infrastructure, and its experiment-discipline for translating AAR outputs into owned, trackable actions. The library's canonical AAR practice is *Blameless Postmortem*, which carries the OPL's sharpest statement of the default-to-system stance: "Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future." That framing matches the NHS just-culture default and LFUO's local-rationality discipline, making OPL a facilitation-layer complement to both. Beyond the postmortem the library offers *Five Whys* for contributory-factor chains, *Backcasting / Pre-mortem* for proactive AARs convened before an incident, *Establish Shared Principles* for the working agreement that makes blameless conversation possible, and *Design of Experiments* for action design that produces valid learning rather than a list of promises. For AI-adjacent incidents, the library's 2026-era additions — *Evals* and *Human-in-the-Loop* — give the facilitator named practices for the specific contributory-factor pattern of AI overconfidence and silent delegation.

## Key Concepts for AAR

1. **Blameless Postmortem.** "Blameless Postmortem is a post-incident practice assessing an incident or other types of outages, its timeline, environment conditions, and all possible factors that lead an incident to happen." Two foundations the practice names explicitly: "Availability of the information regarding the incident" and "Psychological safety of all participants that promotes speaking up openly." The load-bearing quote: "Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future." (Source: Open Practice Library, Practice "Blameless Postmortem", "What is it?", "How to do it?")

2. **Five Whys.** "The 'Five Whys' is a way to figure out what causes a problem. You keep asking 'why' until you find the real reason." The practice carries its own anti-pattern warning: "we should ask why the process failed instead of just asking why. It's important to look for a process that's not working well or not there at all. Sometimes people will say the problem is not enough time, money, or resources. But we can't control those things." (Source: Practice "Five Whys (5 Whys)", "Why do it?")

3. **Backcasting / Pre-mortem.** "Premortem is an analytical / thought experiment technique… The method originates from Gary Klein (HBR article) and was made popular by the Nobel prize winner Daniel Kahneman in his book 'Thinking Fast and Slow.'" The technique: imagine the project has failed and reconstruct the reasons. In an AAR context this is a *proactive AAR* — convened before the event to surface the most likely contributory factors in advance. Lineage: Klein, Kahneman borrowed-through. (Source: Practice "Backcasting / Pre-mortem", "What is it?")

4. **Establish Shared Principles.** "Organizations that have done the work to articulate 'why they exist and what they believe' then need to clearly explain the 'how they will act' they will work before they move to the 'what they will do.'" The practice's strongest claim: "Blindly following practices are not encouraged, establish a set of shared principles and you can weather the storms that beat at your door… Copying just the practices of successful organizations will not get us the same result if we do not also adopt the values and principles that originated these practices." (Source: Practice "Establish Shared Principles", "Why do it?")

5. **Disagree and Commit.** "An approach to enable teams to transition from thinking to doing, whilst ensuring the team are committed to the execution." The contrarian: "There is a common misconception that collaboration eventually requires consensus; it does not." Two pre-conditions: "everybody must have a meaningful choice, and there must be an agreed review point." (Source: Practice "Disagree and Commit", "What is it?", "Why do it?")

6. **Design of Experiments.** "The Design of Experiments is the practice we use to turn ideas, hypothesis and/or assumptions into concrete well defined set of experiments which can be carried out in order to validate those ideas, hypothesis and assumptions, i.e. provide us with valuable learning." Minimum design fields: Hypothesis / Current Condition / Target Condition / Obstacles / Pass criteria / Measures / Learning. The practice's contrarian: "Successful experiments are not experiments that have proven our assumption as correct. Successful experiments are those that provide valid and reliable data which shows a statistically significant conclusion." (Source: Practice "Design of Experiments", "What is it?", "How to do it?")

7. **Psychological Safety.** The library treats psychological safety as a named practice, not a background assumption. "It gives everyone the opportunity to speak up and be heard. This prompts the behaviour and gives permission for each person to share their own insights, establishing a good foundation for psychological safety." (Source: Practice "Check-ins", "Why do it?")

8. **1-2-4-All.** "1-2-4-All is a way for every member of a large group to participate and generate ideas together." Anti-HiPPO framing: "All voices are heard, incorporating 'silent' conversations and expanding input diversity - No more HiPPOs (Highest Paid Person's Opinion)!" (Source: Practice "1-2-4-All", "Why do it?") Cited from the Liberating Structures collection.

9. **Impact-Effort Prioritisation Matrix and RICE.** Two-axis 2×2 (high/low impact × high/low effort) and Reach × Impact × Confidence ÷ Effort. Used at Phase 4 (action design) when the AAR has surfaced more potential actions than the team can pursue. (Source: Practice "Impact-Effort Prioritisation Matrix"; Practice "RICE Prioritisation")

10. **Evals (AI overconfidence).** "Evals are systematic methods for measuring the quality of AI and LLM outputs. They serve the same purpose as Test Automation — giving you confidence that your system behaves correctly — but they are fundamentally different. Traditional tests give you certainty. Evals give you confidence." And: "No single eval can tell you the system is working perfectly. Instead, multiple evals across different dimensions combine to build a level of confidence." Cites Karpathy's "march of nines" framing borrowed-through. (Source: Practice "Evals", "What is it?")

11. **Human-in-the-Loop.** "Human-in-the-Loop (HITL) is a design pattern in which people remain actively involved in the decision-making process of an automated or AI-driven system. Rather than handing full control to a machine, a human reviews, approves, or corrects the system's output before it takes effect." Distinguishes HITL, HOTL (human on the loop), and HIC (human in command). (Source: Practice "Human in the loop", "What is it?", "Why do it?")

12. **Wheel-of-Misfortune.** A role-play exercise where the team practises incident response on past postmortems. Referenced from within *Blameless Postmortem* as a follow-on training practice. Used at Phase 5 (learning-loop closure) — after the AAR closes, the Wheel of Misfortune converts the learning into team rehearsal of the response, not just a written record.

## Questions to Ask During AAR

### Phase 0 — Scoping

| Need | Question |
|---|---|
| Is the room psychologically safe enough to run this AAR? | Have we done a check-in? Do we have a working social contract? Is the blameless-by-default commitment named explicitly before the timeline reconstruction begins? |
| Is this a reactive AAR or a proactive one? | If the event has not yet happened but the risk is known, should this be a Pre-mortem / Backcasting session rather than a post-incident review? |
| Do we have the principles in place, not just the practices? | Establish Shared Principles: have we stated why we run blameless AARs before we ask people to speak candidly? |

### Phase 1 — Timeline and local-rationality reconstruction

| Need | Question |
|---|---|
| Getting every voice into the timeline | 1-2-4-All: individuals write what they observed; pairs compare accounts; groups of 4–6 surface the divergences; whole group integrates. No HiPPO anchoring before the small-group round. |
| Confirming information availability | Blameless Postmortem foundation one: Is information about the incident available to all participants? If not, who holds it and how do we get it into the room? |

### Phase 2 — Contributory-factor analysis

| Need | Question |
|---|---|
| Drilling below the obvious | Five Whys: "Keep asking 'why' until you find the real reason" — and redirect to process failure rather than resource shortage. |
| When an AI system is a contributor | Evals: What confidence did the AI system's outputs actually carry, and was that confidence communicated to the operator? Human-in-the-Loop: Where were the human review gates, and were they bypassed? |
| Surfacing systemic factors | Blameless Postmortem: "why did he pick the wrong one and what we personally and as an organization can do to prevent it in the future" — the question is systemic, not individual. |

### Phase 3 — Just-culture sorting

| Need | Question |
|---|---|
| Redirecting blame to the system | Blameless Postmortem: "Our job is not to point fingers." Paired with NHS just-culture decision tree for the formal locus decision. |
| Naming dissent before proceeding | Disagree and Commit precondition: does everybody have a meaningful choice in whether to proceed, or are we coercing consensus on the individual-vs-system call? |

### Phase 4 — Action design

| Need | Question |
|---|---|
| Designing actions as experiments | Design of Experiments: Hypothesis / Current Condition / Target Condition / Obstacles / Pass criteria / Measures / Learning — for each action item, can it be structured as a testable experiment? |
| Prioritising when there are too many actions | Impact-Effort matrix: where does each action land on impact × effort? RICE when a quantified comparison is needed. |
| Closing on commitment without coercing consensus | Disagree and Commit: "everybody must have a meaningful choice, and there must be an agreed review point." |

### Phase 5 — Learning-loop closure

| Need | Question |
|---|---|
| Turning the learning into rehearsal | Wheel-of-Misfortune: can the team run a role-play exercise on this incident's postmortem before the next iteration? |
| Confirming the principles, not just the practices | Establish Shared Principles: are the principles that underlie these actions visible enough that the team can apply them to the next incident without running through the same process? |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| The postmortem is called "blameless" but the framing of questions assigns responsibility to individuals | Blameless in name only — the systemic question has not replaced the individual-blame question | Reframe: "Why did they pick the wrong one, and what can we as an organisation do to prevent it?" |
| Five Whys reaches "not enough time / money / resources" and stops | The Five Whys anti-pattern — the practice's own warning | Redirect: "We can't control those things — ask why the process failed to accommodate the resource constraint" |
| The action list has seven items with no prioritisation | Too many concurrent improvement items — the team will not finish any of them | Apply Impact-Effort matrix or RICE before adjourning |
| An AI system contributed to the incident but the analysis treats it as a black box | Evals and HITL disciplines are absent — the AI's confidence and human oversight gates are not examined | Ask: what confidence did the AI's outputs carry, and where were the human review gates? |
| The team agrees on an action but one member remains silent | Disagree and Commit's pre-condition unmet — meaningful choice was not available to everyone | Apply Disagree and Commit: ask the silent member directly; confirm the agreed review point |

## When to Use This Reference

Reach for this source when:
- The AAR involves a software or AI system and the team needs named practices for AI-specific contributory factors (Evals, Human-in-the-Loop).
- Action design needs to be structured as testable experiments rather than vague commitments — Design of Experiments provides the minimum design fields.
- The team has too many candidate actions and needs a structured prioritisation — Impact-Effort or RICE is the tool.
- A proactive AAR is warranted before a high-risk event — Backcasting / Pre-mortem is the named practice.
- The AAR is closing and the team needs to convert learning into rehearsal — Wheel-of-Misfortune is the follow-on practice.

This source is most valuable as a facilitation-layer and action-design-layer complement to TC 25-20 and LFUO. Its distinctive contribution is the AI-incident vocabulary (Evals, HITL) that no other source in the corpus carries.

## Worked Example

A team reviews an incident where an AI-assisted code review tool flagged a critical security vulnerability as low-severity, and the human reviewer accepted the flag without further investigation. The facilitator applies the Evals and Human-in-the-Loop frames in Phase 2. (Source: Open Practice Library, Practice "Evals", "What is it?"; Practice "Human in the loop", "What is it?".) Evals: what confidence level did the AI tool report for its severity rating? Was that confidence communicated to the reviewer, or was only the final severity label shown? Human-in-the-Loop: where was the human review gate? Was the gate a HITL (human reviews before action), HOTL (human monitors but doesn't approve), or HIC (human in command of the overall process but not individual decisions)? The investigation reveals the tool was operating as HOTL with no confidence communication. In Phase 4, the team designs two experiments using Design of Experiments fields: Hypothesis — "displaying the AI confidence score alongside the severity label will reduce reviewer acceptance of low-confidence flags by 50%"; Current Condition — confidence score not displayed; Target Condition — confidence score displayed in review UI; Pass Criteria — zero low-confidence flags accepted without manual investigation over 30 days. The Wheel-of-Misfortune exercise (Practice "Wheel-of-Misfortune") is scheduled for the next sprint to rehearse the revised review process on the incident's actual postmortem.

## Anti-patterns This Reference Helps Avoid

- Treating the Blameless Postmortem as a name rather than a practice — running a postmortem that blames the individual who made the triggering action, without asking why they made it.
- Closing Phase 2 on resource shortage ("not enough time, money, or people") rather than process failure — the Five Whys anti-pattern warning addresses this directly.
- Designing actions as vague commitments rather than structured experiments with pass criteria and learning fields.
- Coercing consensus on action ownership rather than using Disagree and Commit's two pre-conditions (meaningful choice + agreed review point).
- Copying the Blameless Postmortem practice from another organisation without adopting the psychological safety and information-availability principles that make it work.
- Missing AI-related contributory factors because the facilitator does not have named practices for AI overconfidence (Evals) and silent AI delegation (Human-in-the-Loop).
- Prioritising actions by gut feel when the action list is too long — solvable by Impact-Effort matrix or RICE before the room clears.
- Treating the AAR as closed when the meeting ends rather than when the experiment design fields are filled and the review point is named.
- Skipping the proactive AAR (Pre-mortem / Backcasting) when a high-risk event is visible in advance.

## Integration with Other References

| Reference | Relationship |
|---|---|
| TC 25-20 (tc-25-20-army-aar) | TC 25-20 provides the four-step AAR protocol; this source's Blameless Postmortem is the software-team variant of the same epistemological discipline |
| LFUO 2024 (lfuo-learning-review-guide-2024) | LFUO provides the networked-causality methodology and administrative-firewall; this source's Establish Shared Principles and psychological safety practices are the facilitation-layer pre-conditions that make LFUO's principles real |
| NHS Just Culture Guide (nhs-just-culture-guide) | NHS provides the formal just-culture decision tree; this source's Blameless Postmortem sets the default-to-system posture before the NHS tree is applied |
| Liberating Structures Handbook (liberating-structures-handbook) | Both sources carry the 1-2-4-All structure; OPL cites it from the LS collection; use the LS Handbook for the full catalogue of LS patterns, use OPL for the software-incident and AI-incident practices |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The Backcasting / Pre-mortem practice cites Gary Klein (HBR article) and Daniel Kahneman (*Thinking Fast and Slow*) borrowed-through as the method's originators; neither is held directly in the demo corpus. The Evals practice cites Andrej Karpathy's "march of nines" confidence-threshold framing borrowed-through; Karpathy is not held directly. The Human-in-the-Loop practice references a 1979 IBM framing ("A computer can never be held accountable, therefore a computer must never make a management decision") borrowed-through. The 1-2-4-All practice is cited from the Liberating Structures collection; the Liberating Structures Handbook is held directly in this corpus.

**Named limits of the source.** The Open Practice Library is a community-curated catalogue, not an authored text — individual practices vary in depth, evidential support, and editorial consistency. The library cloned for this corpus is a snapshot as of May 2026; the live library continues to evolve. The Evals and Human-in-the-Loop practices are 2026-era additions and may not be present in earlier snapshots. The library does not address just-culture methodology, timeline reconstruction protocol, or formal learning-review design; those are carried by LFUO, TC 25-20, and NHS in this corpus.

**Evidence-marker continuity.** The Blameless Postmortem load-bearing quotation is `[V]` in the deep ref; the distillation quotes it directly in Concept 1. The Five Whys anti-pattern warning is `[V]` in the deep ref; the distillation quotes it in Concept 2. The Evals distinction ("tests give certainty; evals give confidence") is `[V]` in the deep ref with `[BT]` to Karpathy; the distillation preserves the borrowed-through flag in Concept 10 and in this section. The Disagree and Commit pre-conditions are `[V]` in the deep ref; the distillation preserves them in Concept 5.
