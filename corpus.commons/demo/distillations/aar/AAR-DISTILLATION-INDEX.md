# AAR Distillation Index

> **Purpose:** Situation-to-resource router for After-Action Review work. "I'm at this point in an AAR — which references should I reach for?"

This is the *when-to-use* layer for the After-Action Review task. It partitions the task into phases and lists distillations appropriate to each phase. For the *what-is* layer (descriptions of each reference), read [`reference-index.json`](../../reference-index.json) at the corpus root. For the task-axis scoping that produced this index, see [`corpus.commons/demo/tasks/aar.md`](../../tasks/aar.md).

**Workflow:** Distillation index (when) → distillation (how) → deep reference (citations, if needed).

The AAR axis is the event-triggered cross-functional counterpart to the iterative team-internal [[retro]] axis; see [`corpus.commons/demo/distillations/retro/RETRO-DISTILLATION-INDEX.md`](../retro/RETRO-DISTILLATION-INDEX.md) for the retro side of the same conversation.

---

## Format

Two table shapes appear in this index.

**Phase-by-phase tables** (the main routing layer) use four columns. The "Need" column describes the situation; "Reference" names the source; "Distillation" links to the projected distillation; "Reach for this when" gives a one-line routing cue.

```markdown
| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| ... | ... | ... | ... |
```

**Quick-start tables** (the situation-first lookup) use three columns: a situation description, the primary references that apply, and the distillation file paths.

```markdown
| Incident type | Primary references | Distillations |
|---|---|---|
| ... | ... | ... |
```

Concepts within a distillation may be referenced with line ranges (`{file}.md L{start}-L{end}`) for fine-grained pointers. The build validates the filename inside the backticks; line ranges are a human convention.

---

## Quick start by incident type

| Incident type | Primary references | Distillations |
|---|---|---|
| **Small in-team event, want fast learning** | TC 25-20 (informal AAR pattern) | `tc-25-20-army-aar-aar.md` |
| **Cross-functional production incident** | TC 25-20 + LFUO Learning Review + NHS Just Culture | `tc-25-20-army-aar-aar.md`, `lfuo-learning-review-guide-2024-aar.md`, `nhs-just-culture-guide-aar.md` |
| **Customer-impact event, blame language anticipated** | NHS Just Culture + LFUO + TC 25-20 | `nhs-just-culture-guide-aar.md`, `lfuo-learning-review-guide-2024-aar.md`, `tc-25-20-army-aar-aar.md` |
| **Near-miss, no harm but learning opportunity** | LFUO four-tool ladder (favours FLA / RLS) + TC 25-20 fratricide-equivalent rule | `lfuo-learning-review-guide-2024-aar.md`, `tc-25-20-army-aar-aar.md` |
| **Software incident with engineering-organisation contributory factors** | TC 25-20 + LFUO + Jones + Letaw | `tc-25-20-army-aar-aar.md`, `lfuo-learning-review-guide-2024-aar.md`, `jones-evidence-based-sweng-aar.md`, `letaw-handbook-sweng-methods-aar.md` |
| **Recurring incident pattern (drift)** | SSDL system archetypes + Barbrook-Johnson CLD + LFUO networked-causality | `ssdl-systems-thinking-foundations-aar.md`, `barbrook-johnson-systems-mapping-aar.md`, `lfuo-learning-review-guide-2024-aar.md` |
| **Just-culture call (individual vs system)** | NHS five-test decision tree + LFUO reckless-and-willful threshold | `nhs-just-culture-guide-aar.md`, `lfuo-learning-review-guide-2024-aar.md` |
| **AAR that surfaces org-design questions** | OpenStax Principles of Management (Mintzberg, six structures) + OpenStax Business Ethics (Mitchell-Agle-Wood for escalation) | `openstax-principles-management-aar.md`, `openstax-business-ethics-aar.md` |
| **AAR surfaces org structure as a named contributory factor (team-archetype mismatch, topology drag)** | Org Topologies Primer (Krivitsky, Larman & Flemm) — naming vocabulary + remediation pathway for org-structure subset | `org-topologies-primer-2025-aar.md` |
| **AAR action requires structural escalation to leadership** | Org Topologies Primer — strategic-design-stance framing; pairs with OpenStax PoM for structure catalogue | `org-topologies-primer-2025-aar.md`, `openstax-principles-management-aar.md` |
| **Project-completion review, not an incident** | TC 25-20 + Open Practice Library Blameless Postmortem + Field Guide retro discipline | `tc-25-20-army-aar-aar.md`, `open-practice-library-aar.md`, `approach-perfect-field-guide-scrum-events-aar.md` |

---

## Phase 0: Scoping (which tool, what time-budget, what attendance)

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Select the right learning tool for the event | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Operator names an event and asks "what kind of review" — apply the four-tool ladder (AAR / RLS / FLA / Learning Review), scaled by learning opportunity not outcome severity. |
| Choose informal AAR for small in-team learning | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | A platoon-equivalent event; the 15-minute on-the-spot AAR with pencil and paper is often better than a formal review. |
| Choose formal AAR for high-stakes cross-functional incident | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Formal-AAR 6-8 week lead time; two-echelons-above evaluator rule; experience-over-rank OC selection. |
| Convene without administrative-action contamination | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Without an explicit no-punitive-action commitment in the delegation of authority, honest accounts will not surface. The administrative firewall is non-negotiable. |
| Hold the default-to-system posture before the conversation begins | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | "Action singling out an individual is rarely appropriate — most patient safety issues have deeper causes and require wider action." Read this aloud before scoping. |
| Budget time honestly for the depth required | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | The TC's *no rushing, no waste* discipline: 30-45 min platoon, 1 hr company, 2 hr battalion-and-above. Match duration to depth. |
| Set the climate and spirit as operational concern | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Climate of an AAR is load-bearing, not soft skill; the AAR is professional discussion, not critique. |
| Identify the fratricide-equivalent topics | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | What events in your domain are severity-overrides-time-budget topics, named in advance not after the fact? |
| Establish the Ten Principles and Agreements | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Group-dialogue agreements as the precondition for honest accounts in any tool from the ladder. |
| Scope as cross-functional rather than team-internal | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | The AAR is the cross-functional, event-triggered learning conversation; team-internal iterative learning routes to [[retro]] instead. |

## Phase 1: Timeline and local-rationality reconstruction

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Choose the discussion-organisation technique for this event | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Three options — chronological for narrative recall, BOS-equivalent for systemic patterns across phases, key events for tight-focus when time is limited. |
| Decompose pre-event beliefs, perceptions, expectations, paradigms | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Surface the participants' pre-event situational awareness; four-category decomposition makes invisible mental models visible. |
| Build the timeline through the Five Hows | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Structured decision-reconstruction tool inside the Lessons Learned Analysis. "Use those that are helpful and don't waste time trying to cook-book the process." |
| Treat divergent accounts as evidence, not problem | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | The AAR is multi-perspective discovery; "no commander, no matter how skilled, will see as much as the individual soldiers and leaders who actually conduct the training." |
| Apply the deflection-question protocol for emotional recall | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Interview as soon as possible; deflect to perception rather than performance; keep participants focused on their own perspective. |
| Interview before hindsight contaminates accounts | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Interview as soon as possible; Roese & Vohs 2012 borrowed-through citation on hindsight bias. |
| Surface attribution and perception biases in participant accounts | OpenStax, Organizational Behavior | `openstax-organizational-behavior-aar.md` | Reach for the OB framing on perception (bottom-up vs top-down), fundamental attribution error, actor-observer bias. |
| Use open-ended questions, not yes/no | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Question-design contrast: *"What happened when X?"* (invites narrative) over *"Why didn't you Y?"* (invites self-defence). |
| Surface mental-model diversity in the room | SSDL, Systems Thinking Foundations (Brief 1.03) | `ssdl-systems-thinking-foundations-aar.md` | Each participant holds a partial-but-valid model; surface partial models *before* discussing options. |
| Build a shared model of the system the team can hold | Barbrook-Johnson & Penn, Systems Mapping | `barbrook-johnson-systems-mapping-aar.md` | When the system is too complex for one head — Rich Pictures, CLD, or Theory of Change diagram as a boundary object for collective sense-making. |
| Distinguish facilitative from transmissive question framing | FLO Facilitation Guide | `flo-facilitation-guide-aar.md` | The first question for any learning engagement: is the learning in the content (transmissive) or in the conversation (facilitative)? |
| Recognise hindsight bias contaminating the analysis | OpenStax, Psychology 2e | `openstax-psychology-2e-aar.md` | Hindsight bias, availability heuristic, anchoring — the perception and memory frame for facilitator vocabulary. |

## Phase 2: Contributory-factor analysis

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Refuse the "root cause" framing | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | "Cause isn't something investigators 'find' or 'discover'; cause is always something we create by recreating the event"; *networked causality* as the replacement vocabulary. |
| Refuse counterfactual reasoning | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | "If they had done X, then Y would have happened" is the forbidden move; learn why people did what they actually did. |
| Apply contributory-factors-not-the-cause framing | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | "What happened, why did it happen, what to do about it, what to carry forward" — never *the* cause. Plural. |
| Look for multiple improbable events | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | "Most often, the Lessons Learned Analysis will reveal that multiple improbable events were necessary for the accident to occur." Resist single-cause anchoring. |
| Test the situation against system archetypes | SSDL, Systems Thinking Foundations (Brief 1.07) | `ssdl-systems-thinking-foundations-aar.md` | Five named patterns — Fixes that Fail, Success to the Successful, Shifting the Burden, Drifting Goals, Limits to Growth. Use as hypothesis-generators, not labels. |
| Map the feedback loops producing the pattern | SSDL, Systems Thinking Foundations (Brief 1.05) | `ssdl-systems-thinking-foundations-aar.md` | Replace the X-causes-Y frame with a structural read: what reinforcing and balancing loops produce the pattern? CLD is a hypothesis to iterate. |
| Generate a CLD or other systems-map artefact for contributory factors | Barbrook-Johnson & Penn, Systems Mapping | `barbrook-johnson-systems-mapping-aar.md` | When the contributory factors form a directed cyclic graph; PSM submap analysis surfaces leverage points. |
| Surface accumulated history shaping the current state | SSDL, Systems Thinking Foundations (Brief 1.06) | `ssdl-systems-thinking-foundations-aar.md` | The blank-slate failure mode — treating a current state as if it has no history; "meeting that [team] as an accumulation of their history". |
| Apply Five Whys with surprise-as-progress-signal | Open Practice Library | `open-practice-library-aar.md` | At an AAR: ask "why" five times; if you're rarely surprised, you may not be digging deep enough. |
| Distinguish active failures from latent conditions | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | Reason-lineage borrowed-through: active failures are at the sharp end; latent conditions are organisational; both belong in the analysis. |
| Read software-incident contributory factors against empirical patterns | Jones, Evidence-Based Software Engineering | `jones-evidence-based-sweng-aar.md` | Reliability statistics — bi-exponential fault-report duplicates pattern; survival-adjusted maintenance-to-development ratio; cone of uncertainty as artefact. |
| Locate decision-rights ambiguity as contributory factor | Letaw, Handbook of Software Engineering Methods | `letaw-handbook-sweng-methods-aar.md` | RACI matrix surfacing the gap between *who decided* and *who should have*. |
| Identify code-smell-shaped design-debt contributors | Letaw, Handbook of Software Engineering Methods | `letaw-handbook-sweng-methods-aar.md` | Twelve named code smells with refactoring prescriptions; the smell vocabulary lets the team name what kept compounding. |
| Detect Goodhart's-Law-shaped contributory factor | Jones, Evidence-Based Software Engineering | `jones-evidence-based-sweng-aar.md` | A metric was being treated as a target and collapsed under control pressure; the measurement itself contributed. |
| Locate the system constraint (Goldratt-borrowed-through) | Open Kanban | `open-kanban-aar.md` | "No single part of a system can ever bring overall improvement"; Holistic / Systemic value gives the substrate for system-level contributory factors. |
| Name an org-structure contributory factor with archetype precision | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | The LLA has surfaced that a team-archetype mismatch (e.g. CAPS-2 team asked to deliver CAPS-3 outcomes) was among the multiple improbable events; OT gives the naming vocabulary that "siloed" and "communication breakdown" lack. |
| Identify topology-mismatch as a recurring contributory-factor pattern | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | The incident shows a pattern of Resource-Topology drag (utilisation-optimised structure forced to do discovery work), Delivery-Topology absent-outcome-validation, or Adaptive-Topology variance absorbed as incident. |
| Name the local-optimisation amplifier among contributory factors | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | Multiple individually-defensible org-design choices (a reward structure, a policy, a reporting line) combined to produce the incident; OT's local-optimisation warning names the pattern ("performance of the whole system may actually decline"). |
| Identify single-team-island structure as a contributory factor source | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | A previously-fixed team produced repeat failure inside an unchanged surrounding system; OT names this as the structural source — the island intervention left the surround's contributory factors untouched. |
| Test whether Resource-Topology framing of frontline staff contributed | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | Frontline staff were being treated as fungible resources (rotated, denied voice in design, denied end-to-end accountability); the Resource-framing is a named structural contributory factor, not a leadership-style critique. |

## Phase 3: Just-culture sorting

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Walk the five-test decision tree in order | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | An individual action concern is on the table; Q1 (deliberate harm) → Q2 (health) → Q3 (foresight) → Q4 (substitution) → Q5 (mitigation) applied sequentially. |
| Apply the foresight test as system-contract probe | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | Is there a protocol; is it workable and in routine use; did the individual knowingly depart? All three Yes to advance to substitution test. |
| Apply the substitution test as peer-and-supervision probe | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | Would peers in same circumstances have behaved similarly; was training missed; was supervision absent? Any Yes routes to system locus. |
| Decompose a multi-action incident into one-action evaluations | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | Multiple actions or omissions bound up in a single incident; each must be evaluated through the tree separately, not jointly. |
| Test the reckless-and-willful threshold | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | The criminal-act threshold (intentional, unjustifiable, foreknowledge of likely serious harm); high and bright; below it FLA continues, at/above it terminates. |
| Terminate the learning analysis on culpability grounds | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | If the reckless-and-willful threshold is met, team-leader writes a memo to the Delegating Official terminating the analysis without disclosing details. |
| Select the recommendation end-state from the just-culture tree | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | Seven end-states (A deliberate-harm through G residual management action); the choice names the response, paired with parallel wider-investigation obligation. |
| Communicate the just-culture decision to stakeholders | NHS Improvement, Just Culture Guide | `nhs-just-culture-guide-aar.md` | The guide is both decision aid and communication tool; differentiation by circumstances, not by outcome. |
| Read the just-culture call against organisational behaviour substrate | OpenStax, Organizational Behavior | `openstax-organizational-behavior-aar.md` | Attribution biases (fundamental attribution error, actor-observer bias) systematically push toward individual-blame in observers; surface this before deciding. |

## Phase 4: Action design

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Frame actions through Blameless Postmortem | Open Practice Library | `open-practice-library-aar.md` | "Our job is not to point fingers"; two foundations — information availability + psychological safety. |
| Hold the FLA / Learning Review boundary on recommendations | US Forest Service, LFUO 2024 | `lfuo-learning-review-guide-2024-aar.md` | Recommendations require Learning Review with focus groups, academic SMEs, Learning Review Board, Safety Action Plan; cannot be added to an FLA after the fact. |
| Treat critical capabilities as stop-rules, not gradients | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Critical gate tasks (CATS): performance below standard is a stop, not a partial score. Identify gate-task equivalents and honour the stop. |
| Allocate retraining resources to weakness, not strength | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Default allocation rule for finite development resource is known weakness, not known strength. Deviation requires a reason. |
| Surface ownership ambiguity before adjourning | Liberating Structures Handbook | `liberating-structures-handbook-aar.md` | LS Discovery & Action Dialogues' closing question: *"Who will do what when next?"* — refuses adjournment without named owner. |
| Resolve decision-rights ambiguity in action ownership | Letaw, Handbook of Software Engineering Methods | `letaw-handbook-sweng-methods-aar.md` | RACI matrix (Responsible / Accountable / Consulted / Informed) for ambiguous-ownership actions. |
| Surface latent dissent before commit | Letaw, Handbook of Software Engineering Methods | `letaw-handbook-sweng-methods-aar.md` | Fist of five six-level voting before commit — *two or fewer fingers blocks*; surfaces latent dissent the meeting tone is suppressing. |
| Frame escalation to leadership when contributors are above team authority | OpenStax, Principles of Management | `openstax-principles-management-aar.md` | Mintzberg's six structures + organisational-design primitives; name the right interlocutor for the structural change being requested. |
| Frame the action's stakeholder-prioritisation | OpenStax, Business Ethics | `openstax-business-ethics-aar.md` | Mitchell-Agle-Wood stakeholder prioritisation when actions cross multiple stakeholder interests; Donaldson-Preston three approaches. |
| Frame ethical exposure surfaced by the AAR | OpenStax, Business Ethics | `openstax-business-ethics-aar.md` | When the AAR has surfaced duty-of-care, employee-rights, or whistleblower-protection questions, the ethical substrate names them. |
| Avoid AI overconfidence in proposed actions | Open Practice Library | `open-practice-library-aar.md` | Open Practice Library's Evals practice (against AI overconfidence) and Human-in-the-Loop (against silent AI delegation) are the action-discipline cues. |
| Frame the action through Establish Shared Principles | Open Practice Library | `open-practice-library-aar.md` | Against copy-without-principles: the action is grounded in the underlying principle, not just the surface practice. |
| Constrain actions to the one constraint | Open Kanban | `open-kanban-aar.md` | Holistic / Systemic value (Goldratt borrowed-through): find the one constraint; local optimisation is not system improvement. |
| Decide retraining-allocation for software-incident root themes | Jones, Evidence-Based Software Engineering | `jones-evidence-based-sweng-aar.md` | Survival-adjusted ROI applied to retraining decisions; the survival rate of the system shapes the retraining horizon. |
| Frame structural-remediation actions as Elevating-Kata experiments | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | Structural actions are framed as "thoughtful experiments with named hypotheses and checkpoints", not pronouncements; pairs with LFUO Learning-Review-required-for-recommendations constraint for structural changes. |
| Frame escalation of org-design contributory factors to leadership | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | Escalation memo frames the ask as "the leaders who own the business objective also own the structural fix" — converts a structural FYI into a leadership action item; pairs with OpenStax PoM for structure catalogue. |
| Use named-archetype vocabulary in escalation memos to non-engineering leadership | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | Precise archetype labels (CAPS-2 → CAPS-3) survive transit to leadership not engaged in the incident; avoids vague language ("more autonomy", "cross-functional teams") that gets escalation memos dismissed. |
| Defend against single-element structural fixes in action design | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | A proposed remediation that changes only one org-design element (a role, a policy, a committee) without systems-fit carries the local-optimisation warning: "flow can get worse." The action needs to address systems-fit. |

## Phase 5: Learning-loop closure

| Need | Reference | Distillation | Reach for this when |
|---|---|---|---|
| Close with What/So What/Now What sequenced debrief | Liberating Structures Handbook | `liberating-structures-handbook-aar.md` | Three-question sequence (Center for Creative Leadership lineage; explicitly named *After Action Debrief* in the handbook); refuses jumping to Now-What before What and So-What. |
| Apply TC 25-20 closing-comments rule | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Leader summarises key points, ends positively, links to next training, then leaves so the unit can discuss in private. |
| Lock in the next-action commitment before the review ends | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | The benefits live in follow-up; an AAR without a clear retraining commitment has not produced its benefit. |
| Mark delayed retraining as visible and timed | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | If the next action is deferred, the deferral must be visible and timed, not silent. |
| Revise SOPs surfaced by the review | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | If the AAR has surfaced SOP problems, the SOP must be revised and the change implemented during the next iteration. |
| Open the response zone for the helpless team | Liberating Structures Handbook | `liberating-structures-handbook-aar.md` | 15% Solutions reframes locus-of-control: *"Where do you have freedom to act? What's in your 15%?"* (Gareth Morgan borrowed-through). |
| Confirm learning as precondition for continuous improvement | Open Kanban | `open-kanban-aar.md` | "Learning is the key concept before continuous improvement can ever happen!"; AAR is the named learning form, not the improvement itself. |
| Frame the AAR as discovery, not critique | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | AAR vs critique is a decision rule about how to construct evaluation evidence; participants discover what happened. |
| Address force protection (safety) at every AAR | US Army, TC 25-20 | `tc-25-20-army-aar-aar.md` | Standing-agenda discipline: safety touched every review regardless of whether it came up during the event under review. |
| Schedule OT re-mapping to test whether structural recommendations took hold | Krivitsky, Larman & Flemm, Org Topologies Primer | `org-topologies-primer-2025-aar.md` | "Periodic re-mapping is an easy and fast way to complete a learning loop of feedback and adapting" — did the topology actually shift, or did the structural change stall at announcement? Tie re-mapping to a calendar date and a participant list. |
| Cross-link to the iterative team-internal cadence | (cross-axis) | (`retro` axis — see [[retro]]) | When the team also needs iterative team-internal learning at retrospective cadence, route to the retro axis. |

## Reference categories

The references below are listed by Pass G applicability fire. Strong-fire references produce a substantive distillation; moderate-fire produces a focused distillation on the specific AAR moment; light-fire produces a thin distillation routing cross-axis where the source has more material.

**Strong fire (canonical AAR doctrine + learning-review + just-culture):**

- `tc-25-20-army-aar-aar.md` — the canonical AAR doctrine: four-step process, three discussion-organisation techniques, spirit-and-climate, AAR-vs-critique frame, train-to-weakness, critical gate tasks.
- `lfuo-learning-review-guide-2024-aar.md` — modern HOP-tradition learning-review framework: four-tool ladder, Ten Principles and Agreements, Five Hows, counterfactual prohibition, networked causality.
- `nhs-just-culture-guide-aar.md` — five-test decision tree with seven recommendation end-states; default-to-system prior; decision aid and communication tool.

**Strong fire (systems thinking and cause-analysis substrate):**

- `ssdl-systems-thinking-foundations-aar.md` — five briefs covering complex-problem characteristics, mental models, feedback thinking, accumulations, system archetypes; the corpus's open-licence Senge-tradition substitute.
- `barbrook-johnson-systems-mapping-aar.md` — seven systems-mapping methods; appropriateness-triangle for method selection; useful when AAR contributory factors need a shared-model artefact.
- `openstax-organizational-behavior-aar.md` — perception, attribution biases, decision-making biases, group dynamics, conflict types — the behavioural substrate for the facilitator's stance.

**Moderate fire (facilitation moves AAR adopts):**

- `liberating-structures-handbook-aar.md` — What/So What/Now What (named *After Action Debrief*), Discovery & Action Dialogues, Wicked Questions, TRIZ inversion, 15% Solutions.
- `open-practice-library-aar.md` — Blameless Postmortem, Pre-mortem / Backcasting, Five Whys, Establish Shared Principles, Evals + Human-in-the-Loop.
- `flo-facilitation-guide-aar.md` — facilitative-vs-transmissive framing, *Anxious-Annie* facilitator-anxiety pattern, Vegas-rules privacy, engagement-equity tracking.
- `openstax-principles-management-aar.md` — PDCA, organisational-design primitives (Mintzberg, six structures) for AAR org-design surfacing, change-management primitives.
- `openstax-psychology-2e-aar.md` — hindsight bias, perception, memory, social-influence — the facilitator's diagnostic vocabulary.

**Moderate fire (software-incident specificity):**

- `letaw-handbook-sweng-methods-aar.md` — RACI for decision-rights ambiguity, fist-of-five for surfacing latent dissent, code smells as design-debt contributory factors.
- `jones-evidence-based-sweng-aar.md` — empirical reliability findings, bi-exponential fault patterns, post-1980 evidence collapse, Goodhart's Law in software measurement.
- `approach-perfect-field-guide-scrum-events-aar.md` — Sprint Retrospective patterns adaptable to AAR (Norm Kerth's Prime Directive, 5-Whys with *surprise as signal*, Vegas / Chatham House rules).
- `scrum-guide-2020-aar.md` — Sprint Retrospective as standing-cadence cousin; useful when AAR borders on retro.
- `open-kanban-aar.md` — learning-as-precondition for continuous improvement; Holistic / Systemic value (Goldratt borrowed-through).

**Moderate fire (doctrinal frame for high-tempo / high-uncertainty AARs):**

- `mcdp1-warfighting-aar.md` — US Marine Corps MCDP-1 (1997, supersedes FMFM-1 1989). Public domain (US Government work product); scope=open. The doctrinal frame every Marine AAR is conducted within: TC 25-20 is the procedure, MCDP-1 is the philosophy. Three threads sit directly on AAR practice: (1) *doctrine is a way of thinking, not a checklist* — reframes "did we follow doctrine?" into "did we exercise the thinking that doctrine teaches?"; (2) commander's intent + mission tactics — *intent must be understood two levels up*; if the sharp end didn't know it, the gap is the leader's responsibility, not the practitioner's compliance failure; (3) OODA loop credited to Boyd (Ch 2 Notes 18), reframes the AAR question from *what did we do?* into *what was our OODA tempo relative to the threat?* Rejects the zero-defects mentality directly (*leniency on overbold errors, severity on errors of inaction*) — AARs that punish errors of commission while tolerating errors of omission produce the inaction the doctrine is most concerned with. Useful in high-tempo / high-uncertainty / decentralised-execution incident reviews (SRE, emergency response, crisis operations, startup-launch retros).

**Light fire (specific contexts):**

- `openstax-business-ethics-aar.md` — accountability frames, duty-of-care chapters, Mitchell-Agle-Wood stakeholder prioritisation when AAR surfaces ethical exposure.
- `org-topologies-primer-2025-aar.md` — Krivitsky, Larman & Flemm (2025). *Strategic Org Design: The Primer*. CC BY-NC-SA 4.0. Not an AAR methodology text. Reached for as a *vocabulary* and *remediation-pathway* tool for the org-structure subset of contributory factors: named-archetype precision (CAPS-2, WHOLE-3, etc.), three topology patterns, local-optimisation warning, Elevating-Katas-as-experiments framing, and periodic re-mapping as learning-loop-closure artefact. Routes selectively to Phase 2 (when LLA surfaces org-structure as a contributory factor), Phase 4 (when structural actions need experiment-framing or escalation language), and Phase 5 (re-mapping as closure test). Does not route to Phase 0, Phase 1, or Phase 3.

**Pass G skip (no AAR-relevant content; routed cross-axis):**

- `openstax-accounting-vol1`, `openstax-accounting-vol2` — accounting; route to `decision-making` and `software-business`.
- `openstax-business-law` — law; route to `decision-making`.
- `openstax-economics-3e` — economics; route to `decision-making`.
- `openstax-entrepreneurship` — entrepreneurship; route to `decision-making`.
- `openstax-introduction-business` — intro business; route to `decision-making`.
- `openstax-principles-finance` — finance; route to `decision-making`.
- `openstax-principles-marketing` — marketing; route to `decision-making`.

---

## Anti-patterns this index helps avoid

- **Single-cause anchoring.** Both TC 25-20 and LFUO 2024 refuse it; *networked causality* is the replacement vocabulary.
- **Counterfactual creep.** "If they had done X..." is LFUO's forbidden move; redirect to *why people did what they actually did*.
- **Premature individual blame.** NHS default-to-system framing precedes the five-test decision tree; "action singling out an individual is rarely appropriate."
- **Verdict-mode statistics.** TC 25-20 *statistics serve teaching, not grading*; if a chart is being used to score people, it has slipped its role.
- **Hindsight-contaminated accounts.** LFUO *interview as soon as possible*; keep participants focused on their own pre-event perspective.
- **Recommendations from an FLA.** LFUO: recommendations require Learning Review with the Learning Review Board; cannot be added to an FLA after the fact.
- **AAR closing without a next-action commitment.** TC 25-20: "the real benefits of AARs come from taking the results and applying them to future training"; an AAR without retraining is not finished.
- **Action ownership left ambiguous.** LS Discovery & Action Dialogues' "Who will do what when next?" is the structural refusal; RACI is the artefact when written.
- **Source-integrity papering-over.** When the participant names a canonical HOP author (Dekker, Reason, Hollnagel, Weick, Conklin), surface that the framing is carried borrowed-through LFUO 2024 / SSDL and the demo cannot cite directly.
- **Retro-shaped event scoped as AAR.** The AAR is event-triggered cross-functional; iterative team-internal learning routes to [[retro]] — wrong axis selection produces wrong artefact.
