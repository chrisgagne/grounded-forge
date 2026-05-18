# After-Action Review (demo corpus)

**Slug:** `aar`
**Purpose:** Help a practitioner run a cross-functional After-Action Review of a specific incident, project completion, or operational event, surfacing what happened, why it happened, what to do about it, and what to carry forward, in a blameless frame grounded in the open-licence subset of the human-and-organisational-performance (HOP) literature the demo corpus holds.

## 1. Problem statement

An AAR is the cross-functional, event-triggered learning conversation the US Army formalised in TC 25-20, that high-reliability organisations run after every operationally meaningful event, and that software organisations adopt under names like "post-mortem" and "incident review." It is the *one-shot* counterpart to the iterative [[retro]] axis: triggered by a specific event, cross-functional rather than team-internal, focused on contributory factors rather than next iteration. This task axis projects the demo corpus onto the diagnostic moves an AAR facilitator makes: scoping, timeline construction, contributory-factor analysis, just-culture sorting, action design, learning-loop closure, and surfacing org-design implications without losing scope.

The demo corpus is deliberately gap-honest about what it does *not* carry. The canonical HOP, safety-engineering, and systems-thinking texts are closed-licence and absent from the open distribution. What the demo *does* carry is the Forest Service's *Learning From Unintended Outcomes and Learning Review Implementation Guide* (LFUO 2024), the NHS Just Culture decision aid, the Army's TC 25-20, the Social System Design Lab's *Systems Thinking Foundations* briefs, Barbrook-Johnson & Penn's *Systems Mapping*, and the methodology-and-facilitation sources (Liberating Structures, FLO, Open Practice Library, Letaw, Jones, OpenStax OB / Management / Psychology / Business Ethics). These carry the discipline the canonical authors carry: LFUO 2024 and NHS Just Culture carry the just-culture work end-to-end, NHS attributing itself to "the work of Professor James Reason and the National Patient Safety Agency's Incident Decision Tree" and LFUO citing the broader HOP tradition throughout. SSDL is the corpus's explicit open-licence Senge-tradition substitute. OpenStax Organizational Behavior carries the perception / attribution / decision-bias substrate. The projection is honest about what is borrowed-through and what cannot be cited directly.

## 2. Practitioner questions

- An incident just happened; how do I scope an AAR (what tool, what time-budget, what attendance)?
- The team wants to blame an individual; how do I redirect to system without losing the just-culture decision the situation may genuinely call for?
- I have a long timeline; how do I draw out contributory factors rather than just "the cause"?
- The same incident pattern has surfaced before; how do I detect drift and treat it differently from a one-off?
- Some of the contributory factors are above the team's authority; how do I surface to leadership?
- The just-culture sort is ambiguous (was this human error, at-risk behaviour, or reckless?); what protocol resolves it?
- The actions from last AAR were never done; how do I learn from that?
- An AAR has organisational-design implications; how do I keep it scoped without losing them?
- The conversation keeps slipping into counterfactual reasoning ("if they had just..."); how do I redirect?
- Hindsight bias is contaminating the participants' accounts; how do I interview around it?

## 2a. Runtime listener grain

**Trigger unit:** an operator-described AAR scenario (an incident type, a facilitation moment, a diagnostic move the facilitator is making). Generic *"how do I run an AAR"* framings route to `tc-25-20-army-aar` and `lfuo-learning-review-guide-2024` directly; the axis fires on situated diagnostic moments.

**Response unit:** the framework, diagnostic move, or facilitation protocol from the demo corpus that addresses the moment, plus the phase context (Phase 0 scoping, Phase 1 timeline, Phase 2 contributory factors, Phase 3 just-culture sorting, Phase 4 action design, Phase 5 learning-loop closure).

### Seed trigger→response table

The full per-phase routing tables are authored at [`distillations/aar/AAR-DISTILLATION-INDEX.md`](../distillations/aar/AAR-DISTILLATION-INDEX.md); the seeds below are the load-bearing rows the index inherits.

**Phase 0, Scoping** (which tool, what time-budget, what attendance)

| Trigger (what the practitioner notices) | Response (what the corpus surfaces) |
|---|---|
| Operator names an event and asks "what kind of review" | Four-tool ladder AAR / RLS / FLA / Learning Review, scaled by learning opportunity not outcome severity (`lfuo-learning-review-guide-2024`) |
| Operator describes a small in-team event | TC 25-20 informal-AAR pattern: 15-min on-the-spot with minimal aids (`tc-25-20-army-aar`) |
| Operator describes a high-stakes cross-functional incident | TC 25-20 formal-AAR 6-8 week lead time + two-echelons-above evaluator rule (`tc-25-20-army-aar`); LFUO Learning Review for Safety Action Plan, focus groups, Learning Review Board (`lfuo-learning-review-guide-2024`) |
| Operator asks how to convene without administrative-action contamination | LFUO administrative firewall: explicit no-punitive-action commitment in writing or the FLA cannot proceed (`lfuo-learning-review-guide-2024`); NHS default-to-system framing for the broader posture (`nhs-just-culture-guide`) |
| Operator describes time pressure tempting them to skip | TC 25-20 *no rushing, no waste* discipline: budget realistically for depth, do not pretend a 30-min slot supports a 2-hour question (`tc-25-20-army-aar`) |

**Phase 1, Timeline and local-rationality reconstruction**

| Trigger | Response |
|---|---|
| Operator describes building a timeline | TC 25-20 three discussion-organisation techniques (chronological / BOS-equivalent / key events), picked by next-decision needs (`tc-25-20-army-aar`); LFUO Lessons Learned Analysis decomposing beliefs, perceptions, expectations, paradigms held before the event (`lfuo-learning-review-guide-2024`) |
| Operator describes participant accounts diverging | TC 25-20 multi-perspective discovery as the point, not a problem (`tc-25-20-army-aar`); LFUO deflection-question protocol for emotional recall in interviews (`lfuo-learning-review-guide-2024`) |
| Operator notices hindsight contaminating accounts | LFUO interview-as-soon-as-possible; keep participants on their own perspective; Roese & Vohs 2012 borrowed-through citation (`lfuo-learning-review-guide-2024`); OpenStax OB attribution-bias + perception-bias frames (`openstax-organizational-behavior`) |
| Operator asks how to ask open questions | TC 25-20 question-design contrast: *"what happened when X"* (invites narrative) over *"why didn't you Y"* (invites self-defence) (`tc-25-20-army-aar`); FLO facilitative-vs-transmissive question framing (`flo-facilitation-guide`) |
| Operator surfaces a complex system the team can't all hold | Systems-mapping methods catalogue for shared-model construction (`barbrook-johnson-systems-mapping`); SSDL mental-models brief: each participant holds partial-but-valid model (`ssdl-systems-thinking-foundations`) |

**Phase 2, Contributory-factor analysis**

| Trigger | Response |
|---|---|
| Operator says "the root cause was..." | LFUO position: "cause isn't something investigators 'find' or 'discover'; cause is always something we create by recreating the event"; *networked causality* as replacement vocabulary; FLAs must avoid causal statements (`lfuo-learning-review-guide-2024`) |
| Operator describes counterfactual creeping in | LFUO forbidden-move list: learn why people did what they actually did, not why they did not do what hindsight suggests (`lfuo-learning-review-guide-2024`) |
| Operator describes the same pattern recurring | SSDL system archetypes as hypothesis-generators (fixes that fail, success to the successful, shifting the burden, drifting goals, limits to growth) (`ssdl-systems-thinking-foundations`); Senge-tradition substrate is borrowed-through here, not directly cited |
| Operator describes a single-cause analysis | LFUO multiple-improbable-events pattern: "most often, the Lessons Learned Analysis will reveal that multiple improbable events were necessary for the accident to occur" (`lfuo-learning-review-guide-2024`); TC 25-20 *contributory factors, not the cause* phrasing (`tc-25-20-army-aar`) |
| Operator describes a software incident's contributory factors | Jones reliability statistics: bi-exponential fault-report duplicates pattern, survival-adjusted maintenance:development ratio (`jones-evidence-based-sweng`); Letaw RACI for accountability ambiguity, code smells for design-debt contributors (`letaw-handbook-sweng-methods`) |

**Phase 3, Just-culture sorting**

| Trigger | Response |
|---|---|
| Operator surfaces an individual-vs-system call | NHS five-test decision tree walked in order: Q1 deliberate harm → Q2 health → Q3 foresight → Q4 substitution → Q5 mitigation (`nhs-just-culture-guide`) |
| Operator describes a foresight-test situation (was the protocol workable and in routine use, did the individual knowingly depart) | NHS Q3 foresight test with all-three-Yes-to-advance gate (`nhs-just-culture-guide`) |
| Operator describes a peer-and-supervision question (would peers in same circumstances behave similarly; was training missing; was supervision absent) | NHS Q4 substitution test as system-locus probe (`nhs-just-culture-guide`) |
| Operator is tempted to terminate the learning analysis on culpability grounds | LFUO reckless-and-willful-disregard threshold (intentional, unjustifiable, foreknowledge of likely serious harm); team-leader memo procedure (`lfuo-learning-review-guide-2024`); NHS default-to-system framing remains in parallel (`nhs-just-culture-guide`) |
| Operator describes the response needing to be explainable to staff or stakeholders | NHS positioning as both decision aid and communication tool; differentiation by circumstances not outcome (`nhs-just-culture-guide`) |

**Phase 4, Action design**

| Trigger | Response |
|---|---|
| Operator describes drafting actions | Open Practice Library Blameless Postmortem practice and its two foundations (information availability + psychological safety) (`open-practice-library`); LFUO recommendations-only-for-Learning-Review constraint (`lfuo-learning-review-guide-2024`) |
| Operator describes recommendations crossing the FLA / LR threshold | LFUO: recommendations require Learning Review with focus groups, academic SMEs, Learning Review Board, Safety Action Plan; cannot be added to an FLA after the fact (`lfuo-learning-review-guide-2024`) |
| Operator surfaces an action that ought to be a stop-rule | TC 25-20 critical gate tasks (CATS): performance below standard is a stop, not a partial score (`tc-25-20-army-aar`) |
| Operator describes ambiguous ownership of an action | Letaw RACI matrix as decision-rights artefact (`letaw-handbook-sweng-methods`); Liberating Structures Discovery & Action Dialogues' "Who will do what when next?" closing question (`liberating-structures-handbook`) |
| Operator asks how to surface system-level contributors that need leadership attention | LFUO Learning Review Board + Safety Action Plan as the escalation surface (`lfuo-learning-review-guide-2024`); OpenStax Principles of Management organisational-design primitives for naming the right interlocutor (`openstax-principles-management`) |

**Phase 5, Learning-loop closure**

| Trigger | Response |
|---|---|
| Operator describes wrapping the AAR | TC 25-20 closing-comments rule: leader summarises, ends positively, links to next training, leaves so unit can discuss in private (`tc-25-20-army-aar`); LS What/So What/Now What sequenced debrief, refusing jump-to-Now-What (`liberating-structures-handbook`) |
| Operator describes last AAR's actions never happened | TC 25-20 *real benefits come from applying results* principle; an AAR without retraining commitment has not produced its benefit; delayed retraining must be visible and timed, not silent (`tc-25-20-army-aar`) |
| Operator describes needing a future-facing review of the AAR-action backlog | LFUO open-and-evolving stance, with the guide updated as the community learns (`lfuo-learning-review-guide-2024`); Open Kanban learning-as-precondition for continuous improvement (`open-kanban`) |
| Operator describes the AAR surfacing SOP problems | TC 25-20 *revise SOPs surfaced by the review and implement during future training* rule (`tc-25-20-army-aar`) |
| Operator describes capturing learning that the corpus does not yet hold | The session output itself; LFUO Recommended Reading entries as the named gap when the practitioner wants to read further (`lfuo-learning-review-guide-2024`) |

## 3. Available sources

All Pass-G-applicable demo distillations in `distillations/aar/` are candidates; per-source applicability decided by `creating-distillations` Pass G during ingestion.

**Strong fire (canonical AAR doctrine + learning-review + just-culture):**

- `tc-25-20-army-aar`: the canonical AAR doctrine. Four-step process (Planning, Preparing, Conducting, Following up); three discussion-organisation techniques; spirit-and-climate; AAR-vs-critique frame; train-to-weakness; critical gate tasks; statistics as double-edged sword; experience-over-rank OC selection; two-echelons-above evaluator rule.
- `lfuo-learning-review-guide-2024`: the recent HOP-tradition learning-review framework. Four-tool ladder (AAR / RLS / FLA / Learning Review); Ten Principles and Agreements; Five Hows / Lessons Learned Analysis; deflection-question protocol; readback validation; explicit position against causal statements, counterfactual reasoning, recommendations-as-default. Carries the broader HOP tradition borrowed-through; the demo does not hold those authors directly.
- `nhs-just-culture-guide`: five-test decision tree (deliberate harm; health; foresight; substitution; mitigating circumstances) with seven recommendation end-states; default-to-system prior; positioned as both decision aid and communication tool. Carries the NPSA-Incident-Decision-Tree just-culture lineage borrowed-through.

**Strong fire (systems thinking and cause-analysis substrate):**

- `ssdl-systems-thinking-foundations`: five briefs (complex-problem characteristics, mental models, feedback thinking with CLDs, accumulations, system archetypes). The corpus's open-licence Senge-tradition substitute; the *Field Guide*-style systemic framing is borrowed-through, not directly cited.
- `barbrook-johnson-systems-mapping`: seven systems-mapping methods (Rich Pictures, Theory of Change, CLDs, PSM, FCM, BBN, System Dynamics) with appropriateness-triangle for method selection. Useful when the AAR's contributory-factor work needs a shared-model artefact.
- `openstax-organizational-behavior`: perception, attribution biases, decision-making biases, group dynamics, conflict types, communication models. The behavioural substrate for the facilitator's stance.

**Moderate fire (facilitation moves AAR adopts):**

- `liberating-structures-handbook`: What/So What/Now What three-question sequence (Center for Creative Leadership lineage; explicitly named *After Action Debrief* in the handbook); Discovery & Action Dialogues six-question protocol; Wicked Questions; TRIZ inversion; 15% Solutions for locus-of-control reframe.
- `open-practice-library`: Blameless Postmortem practice with information-availability + psychological-safety foundations; Pre-mortem / Backcasting; Five Whys.
- `flo-facilitation-guide`: facilitative-vs-transmissive question framing; *Anxious-Annie* facilitator-anxiety pattern; Vegas-rules privacy framing; engagement-equity tracking.
- `openstax-principles-management`: PDCA cycle, organisational-design primitives (Mintzberg, six structures) when AAR conclusions surface structural questions, change-management primitives.
- `openstax-psychology-2e`: hindsight bias, perception, memory, social-influence (Asch, Milgram, Zimbardo) for the facilitator's diagnostic vocabulary.

**Moderate fire (software-incident specificity):**

- `letaw-handbook-sweng-methods`: RACI matrix for decision-rights ambiguity surfaced in an AAR; code smells as design-debt contributory factors; fist-of-five for surfacing latent dissent on action commitment.
- `jones-evidence-based-sweng`: empirical findings about software reliability, fault-report patterns, the post-1980 evidence collapse; survival-adjusted maintenance:development ratio; agency theory in vendor-client relations. Useful when the AAR is on a software incident.
- `approach-perfect-field-guide-scrum-events`: Sprint Retrospective patterns adaptable to AAR (Norm Kerth's Retrospective Prime Directive; 5-Whys discipline; Vegas / Chatham House rules; *don't show undone work*).
- `scrum-guide-2020`: Sprint Retrospective as standing-cadence cousin; useful when the AAR borders on the [[retro]] axis.
- `open-kanban`: learning-as-precondition for continuous improvement; Holistic / Systemic Approach value (Deming + Goldratt) for the AAR-output-as-system-change framing.

**Light fire (specific contexts):**

- `openstax-business-ethics`: accountability frames, duty-of-care chapters, when an AAR surfaces ethical exposure.

**Pass G likely skip (no AAR-relevant content):**

- `openstax-accounting-vol1`, `openstax-accounting-vol2`, `openstax-business-law`, `openstax-economics-3e`, `openstax-entrepreneurship`, `openstax-introduction-business`, `openstax-principles-finance`, `openstax-principles-marketing`. Each is routed cross-axis to `decision-making`, `stakeholder-engagement`, or `software-business`.

## 4. Intended lenses

The demo lens library carries `builder`, `agentic-builder`, `pm-bounded-by-ba-role`, `cto`, `business-executive-stakeholder`, and `chris-gagne-consultant-coach`. Of these:

- `cto`: moderate fire. When the AAR is on a software incident and surfaces engineering-organisation contributory factors that need CTO-level translation.
- `business-executive-stakeholder`: moderate fire. When AAR conclusions need to land with the board or exec team in their language.

Per-distillation applicability decided at Pass G; thin lens fit is expected and acceptable.

## 4a. Intended runtime agents

The aar task ships with an `aar-facilitator` agent that hosts:

- The AAR phase sequence (scoping → timeline → contributory factors → just-culture → actions → learning-loop closure).
- The NHS just-culture decision tree.
- The LFUO four-tool-ladder routing (AAR / RLS / FLA / Learning Review by learning-opportunity scale, not outcome severity).
- The TC 25-20 question-design discipline (open-ended, narrative-inviting, not yes/no).
- The counterfactual / causal-statement refusal list.
- The actions-to-learning-loop bridge (TC 25-20 *benefits live in follow-up*; LFUO recommendations gating).

The agent is invoked by the operator command `/aar-facilitate` for a fresh AAR.

## 5. Overlap

- **Significant with `retro`** on the cause-analysis and learning-loop phases. Same demo sources (LFUO 2024, NHS Just Culture, SSDL, Liberating Structures, Open Practice Library) fire on both; the AAR projection sharpens to *event-triggered cross-functional* framing, retro to *iterative team-internal* framing. Cross-link [[retro]] for the iterative-cadence side of the same conversation.
- **Moderate with `decision-making`** on the action-design phase. The same sources project differently: decision-making's projection covers the decision discipline broadly; AAR's projection sharpens to *post-event evidence input for the next decision*. Integration-section updates expected in the decision-making distillations of TC 25-20, LFUO 2024, NHS Just Culture, SSDL, OB.
- **Moderate with `stakeholder-engagement`** on the escalation-to-leadership move. Phase 4 leadership-translation surfaces overlap with stakeholder-engagement's communication framing (Mitchell-Agle-Wood prioritisation; Grunig-Hunt linkage models, both in `openstax-business-ethics`).
- **Light with `software-business`** on software-incident AARs. Jones / Letaw projections may need integration-section updates pointing to the AAR projection for incident-mode reading.

## 6. Success criteria

A practitioner running an AAR with this axis active can: produce a timeline that does not collapse to a single root cause; route blame language back to local-rationality framing within the conversation; distinguish individual / system culpability on the NHS five-test decision tree; choose the right learning tool from the LFUO four-tool ladder by learning opportunity rather than outcome severity; surface contributory factors at both team and organisational level; close the loop with actions that are specific, owned, and trackable against next AAR; honour the counterfactual / causal-statement refusal list.

The falsifier: an LLM-judge eval comparing AAR-axis answers on a held-out set of incident-prompts against (a) the demo's `decision-making` axis applied to the same prompts and (b) the same model running raw on the same prompts. Bar: 60% of test queries cite TC 25-20 + LFUO + NHS together with at least one borrowed-through HOP author named through the LFUO Recommended Reading section.

## Discipline

- **Blameless by default.** The AAR's purpose is system-level learning, not individual accountability. The NHS just-culture decision tree handles the rare cases where accountability is the right move; the default before the tree is system.
- **Local rationality.** Every action made sense to the person doing it at the time. Reconstruct the local rationality before assigning fault. LFUO Five Hows and decomposing beliefs / perceptions / expectations / paradigms is the structured tool.
- **Drift detection.** The same pattern reappearing 2+ times is not coincidence; it is drift. Name it. SSDL system archetypes are hypothesis-generators for the drift's structure; do not use them as labels.
- **Contributory factors, not the cause.** Both TC 25-20 and LFUO 2024 refuse single-cause framings. The vocabulary is *networked causality*; the trap is the *cause as discovery* prior.
- **No counterfactuals.** LFUO's forbidden move. Learn why people did what they actually did, not why they did not do what hindsight suggests. State the rule out loud at the start of the AAR.
- **Source-integrity gap-honesty.** When a participant or reader names a canonical HOP / safety-engineering author the demo does not hold directly, surface that the framing is carried borrowed-through LFUO 2024 or SSDL. Do not paper over the absence; direct citation of those authors is not available in this open distribution.
- **Pass G owns per-distillation applicability.** The source set in §3 is the candidate set; Pass G decides which AAR distillation each source produces.
- **Runtime listener grain.** The seed trigger→response tables in §2a name what fires the corpus in the moment. `creating-applications` inherits these to author the runtime tables in the distillation index; `creating-distillations` reads them at Pass G to map each source's content to the triggers it can address.

## Author anchors

- US Army, TC 25-20, *A Leader's Guide to After-Action Reviews* (1993): the canonical AAR doctrine; public domain.
- US Forest Service, *Learning From Unintended Outcomes and Learning Review Implementation Guide* (2024): recent HOP-tradition learning-review framework; carries the broader HOP tradition borrowed-through where the demo does not hold those authors directly; public domain.
- NHS Improvement, *Just Culture Guide*: operational decision tree; attributes itself to Professor James Reason and the NPSA Incident Decision Tree; Open Government Licence v3.0.
- Farrell et al., *Methods Briefs Series 1: Systems Thinking Foundations* (SSDL, 2021): the corpus's open-licence Senge-tradition substitute; CC BY-SA 4.0.

**What the demo does NOT carry (not openly redistributable):** the canonical HOP, safety-engineering, systems-thinking, and behavioural-economics literature. The demo carries the discipline borrowed-through LFUO 2024 / NHS Just Culture / SSDL; direct citation of canonical authors in these traditions is not available in this open distribution.
