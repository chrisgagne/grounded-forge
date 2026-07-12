# Hurtado, Open Kanban — Decision-Making Distillation

**Source:** Hurtado, J. (with Annita Yegorova Hurtado), AgileLion Institute. *Open Kanban — Open Source Initiative to create a Kanban core that is Agile, Lean and Free*. Release 1.00 Rev A. Licence: CC BY 3.0 Unported. https://github.com/agilelion/Open-Kanban.

## Decision-Making Relevance

Open Kanban is, at its working core, a decision discipline for *flow-of-work* choices: what should the team commit to, in what quantity, at what stage of the value chain, with what authority to pull or postpone. The framework's five values condition the decisions a team is able to make (pull-based scheduling requires respect; upward correction requires courage; holistic improvement requires a systems-level view), and the four practices structure where the decisions are made (the Kanban board makes work visible enough to decide on; team-based leadership names who decides; batch-size reduction is a decision rule about quantity per stage; continuous learning produces decisions about how to decide next time).

The framework encodes decision discipline in three threads.

**Thread one: pull-based scheduling over push-based dispatch.** The Respect-for-people value is the prerequisite for pull-based work flow: "Respect for people allows for delegation and the demand-pull that is crucial to Kanban. When any developer is able to take a story from the backlog and pull it to development or QA, he is able to do so because we respect him." This is a decision-rights claim — the doer pulls; the manager does not push. The decision about *what to work on next* sits with the team member who will do the work, not with a dispatcher upstream.

**Thread two: batch-size reduction as the primary flow decision.** Open Kanban's signature contrarian position is that the discipline asks for batch-size reduction explicitly, not WIP-limiting: "Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around... Open Kanban does not ask you to limit WIP, but it does request that you 'Reduce the Batch Size of your Efforts.'" The decision rule is per-stage: at every stage of the value chain, reduce the *complexity* and the *quantity* of items in play. In software, this means simpler stories (not epics) and fewer concurrent items per SDLC stage. The decision is forward-looking — what to commit to next — rather than backward-looking — what to count after the fact.

**Thread three: holistic / systemic framing over local optimisation.** The Holistic-or-Systemic-Approach value is grounded explicitly in Deming's System of Profound Knowledge and Goldratt's Theory of Constraints — the source cites both by name: "no single part of a system can ever bring overall improvement. We need to take a holistic view of the system and understand it." This is a decision-quality claim: a decision optimising one stage at the expense of overall flow is a mistake the framework refuses to call an improvement. The improvement target is system throughput, not local efficiency.

A fourth thread — under-prescription as a deliberate methodological choice — runs through all the practices. Open Kanban does not mandate WIP limits, does not require new roles, does not specify the cadence of learning meetings (Retrospectives, Strategy Meetings, or Kaizen Groups are all named as candidates without prescription). The meta-decision the framework makes is: name what must be common (values, practices, licence) and leave the *how* to local context.

This distillation gathers these threads into a working pattern: how Open Kanban structures pull-based decision-rights; how batch-size reduction operates as a per-stage decision rule; how the holistic-systems lens disciplines which improvements count as improvements; and where the framework deliberately leaves the local decision to the team.

## Key Concepts for Decision-Making

1. <!-- concept: pull-based-scheduling --> **Pull-based scheduling as a decision-rights claim.** "Respect for people allows for delegation and the demand-pull that is crucial to Kanban. When any developer is able to take a story from the backlog and pull it to development or QA, he is able to do so because we respect him." The team member doing the work decides what to pull next; the upstream dispatcher does not push. (Source: Hurtado, *Open Kanban* Release 1.00 Rev A, "Open Kanban Values" — Respect for people.)

2. <!-- concept: batch-size-reduction --> **Batch-size reduction as the primary flow decision rule.** "Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around... Open Kanban does not ask you to limit WIP, but it does request that you 'Reduce the Batch Size of your Efforts.'" The decision is forward-looking and per-stage: reduce complexity and quantity at every stage of the value chain. WIP limits emerge as a downstream consequence. ("Open Kanban Practices" — Reduce the Batch Size.)

3. <!-- concept: batch-size-reduction --> **How to reduce batch size (software case).** "Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle." The decision-rule has two levers — *complexity per item* and *quantity per stage*. ("Open Kanban Practices" — Reduce the Batch Size.)

4. <!-- concept: multitasking --> **Multitasking as a refused option.** "Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work." A pre-committed decision against parallel work as a productivity strategy. ("Open Kanban Practices" — Reduce the Batch Size.)

5. <!-- concept: systems-thinking --> **Holistic / systemic view as the decision lens.** "Deming's System of Profound Knowledge and Goldratt's Theory of Constraints reminds us that no single part of a system can ever bring overall improvement. We need to take a holistic view of the system and understand it." A decision that optimises one stage at the expense of overall throughput does not count as an improvement. ("Open Kanban Values" — Holistic or Systemic Approach to Change.)

6. <!-- concept: sustainable-pace --> **Sustainable pace as a decision constraint.** "Respect for people also aligns with sustainable pace in Agile, or Muri 無理 in Lean. If you respect your team you will not work them to death... An exhausted developer, manager or team are the perfect recipe for disaster. Kanban cannot succeed this way." Commitments that overload the team are decisions the framework refuses to call success. ("Open Kanban Values" — Respect for people.)

7. <!-- concept: courage --> **Courage as the upward-correction enabler.** "Like Kent Beck noticed in order to improve or even correct mistakes we need courage. When a manager, VP, or person in authority makes a mistake and someone with lower rank notices it, it takes courage for him to tell us about it." Without courage, the decision the team makes is whichever decision authority prefers — even when authority is wrong. ("Open Kanban Values" — Courage.)

8. <!-- concept: waste-elimination --> **Value (Focus on Value) and waste-elimination (Muda) as two sides of the same decision.** "Eliminate waste or 'Muda' in Japanese Muda 無駄 represents anything that does not add value to your process or flow. By eliminating waste, we optimize the creation of value." A decision can be made on either side: "what adds value?" or "what is waste?" Both questions decide the same thing. ("Open Kanban Values" — Focus on Value.)

9. <!-- concept: kanban --> **Visualisation as a precondition for collaborative decision-making.** "Kanban deals with this challenge by using Kanban boards, visual representations of the flow of work that show how work items move from stage to the next... This Kanban practice makes it easier to collaborate in a team setting, and also provides transparency about the process and the work everyone is doing." Decisions made on invisible work are decisions made on imagined work. ("Open Kanban Practices" — Visualize the workflow.)

10. <!-- concept: information-radiators --> **Information radiators broaden the visualisation scope.** "Visualizing the workflow is not limited to Kanban boards; one can also use signs and diagrams that the team can see in their work environment, like dashboards, performance metrics or other information radiators." (Cockburn's term.) The decision context expands beyond the board itself. ("Open Kanban Practices" — Visualize the workflow.)

11. <!-- concept: team-based-leadership --> **Team-based leadership without role restructuring.** "Although Kanban starts where you are, and does not need to modify any titles or roles in an organization, Kanban cannot work without a team to deliver value." The decision *not* to restructure is itself a methodological commitment — the framework refuses to require a precondition it cannot guarantee. ("Open Kanban Practices" — Lead using a team approach.)

12. <!-- concept: continuous-improvement --> **Learning as upstream of continuous improvement.** "Learning is the key concept before continuous improvement can ever happen! Once learning is part of the culture, part of the workflow, then improving continuously becomes easy." A decision to "improve continuously" without a learning structure is a decision that won't take effect. Retrospectives, Strategy Meetings, and Kaizen Groups are named as candidate forms. ("Open Kanban Practices" — Learn and improve continuously.)

13. <!-- concept: method-incompleteness --> **Method incompleteness as a deliberate design choice.** "Open Kanban is not a full or complete Agile or Lean method, instead it is the heart of that method that is the reason it can be ultra light. The best comparison in the software world would be the kernel of an open source operating system." The decision to leave gaps is intentional; local methods (Kanban Ace, Scrumban, Kanban for Teams, Kanban Thinking) fill them. ("Open Kanban Definition"; "The Open Kanban Movement".)

14. <!-- concept: cross-domain-applicability --> **Cross-domain applicability.** "Although it's main focus is in IT and Software Development, Open Kanban can be used in any business or non-profit to achieve agility and continuous improvement." The decision rules transfer across knowledge-work domains. ("Open Kanban Definition.")

## Questions to Ask During Decision-Making

### Phase 1: Framing (Recognising the decision and gathering context)

| Need | Question |
|---|---|
| Test for batch-size framing | Is the question about *quantity per stage of the value chain* rather than about a single artefact? If multiple items are queued at one stage, the decision is about batch size, not about the next item. |
| Detect a push-based dispatch pattern | Is work being assigned to people by an upstream dispatcher (push), or is it being pulled by team members when they have capacity (pull)? If push, the framework would name the pattern and ask the team to switch to pull. |
| Surface multitasking | How many items is each team member currently in-flight on? Open Kanban's named position is that "multitasking does not work" — the decision discipline is to limit the number of concurrent items per stage. |
| Detect local optimisation | Is the proposed improvement local to one stage of the value chain? Open Kanban's holistic / systemic value (grounded in Deming + Goldratt) refuses to call stage-local improvements overall improvements unless system throughput rises. |
| Test for sustainable pace | Is the commitment the team is about to make sustainable, or does it require *Muri* (overburden)? Decisions that overload the team are decisions the framework refuses to call success. |
| Make the work visible before deciding | Is the work being decided on visible on a Kanban board or other information radiator? If the work is invisible, the decision is being made on imagined work. |
| Identify whose decision this is | Does the decision belong to the team member who will pull and do the work, or to an upstream authority? The Respect-for-people value puts pull decisions with the doer. |
| Test whether learning has happened | If this is a "continuous improvement" decision, is there an explicit learning structure (Retrospective, Strategy Meeting, Kaizen Group) that has surfaced what to improve? Decisions to improve without a learning step are decisions that won't land. |

### Phase 2: Bounding (Defining the decision and its constraints)

| Need | Question |
|---|---|
| Bound by stage of the value chain | At which stage of the value chain is the decision being made? Open Kanban's batch-size discipline is per-stage; the same decision (commit-to-N items) has different costs at different stages. |
| Bound by item complexity | If the item being committed to is large (in software terms: an epic, not a story), can it be decomposed into simpler items before commitment? "Reduce the number of large stories (epics) you create, and do your best to keep stories simple." |
| Bound by team-based leadership | Is the decision being made by the team, with team leadership, or is it being made above the team and handed down? Open Kanban requires the former without requiring formal restructuring. |
| Bound by sustainable pace | Will the commitment sustain over multiple cycles, or will it consume reserves the team cannot rebuild? Sustainable pace is a hard constraint, not a soft preference. |
| Bound by the immutable values | Is the proposed move consistent with the five values (Respect, Courage, Focus on Value, Communication and Collaboration, Holistic / Systemic Approach)? If a decision requires violating a value, the framework asks for a different decision. |
| Bound by the holistic frame | Will the decision improve overall system throughput, or only one stage? "No single part of a system can ever bring overall improvement." |

### Phase 3: Exploring (Generating alternatives)

| Need | Question |
|---|---|
| Generate batch-reduction alternatives | What's the smallest version of this work that delivers value? In software: what's the smallest user story? In business: what's the smallest deliverable that proves a hypothesis? |
| Generate de-multitasking alternatives | If multiple items are in flight at one stage, which one finishes first if the team focuses on it? "Keeping the team focused helps them finish what they start faster." |
| Surface the system-level view | If the decision optimises one stage, what happens to throughput at downstream stages? Apply the Theory-of-Constraints question: where is the system constraint, and does this decision relax it or shift it? |
| Bring courage to the option set | What's the option that authority might not want to hear but the data supports? Open Kanban's Courage value exists to keep this option on the table. |
| Use the value lens to surface tacit options | Which options were *not* considered because they violate a current organisational habit but are actually consistent with one of the five values? |
| Frame the option as value-add or waste-elimination | Can the option be framed as adding value, or alternatively as eliminating waste? Both framings decide the same thing; sometimes one is easier to commit to than the other. |

### Phase 4: Deciding (Analysing and selecting)

| Need | Question |
|---|---|
| Apply the pull-based rule | Who pulls? The person who pulls is the person who does the work. If the decision is being made by someone other than the doer, ask why. |
| Apply the holistic test | Does this decision improve overall flow, or only local efficiency? If only local, the framework asks for a different decision. |
| Apply the sustainable-pace test | If the team commits to this, will they sustain it across the next several cycles? If not, scale the commitment down to what is sustainable. |
| Apply the batch-size test | Is the chosen scope the smallest viable batch at this stage, or is the team being asked to commit to a larger batch because "we always have"? The default is reduce, not maintain. |
| Surface the courage cost | What's the courage cost of saying *no* to this commitment? If saying no is socially expensive, that is information about whether the decision is being made under push pressure rather than pull discipline. |
| Anchor on team-based leadership | Has the team's leadership (named or unnamed) endorsed the decision? Open Kanban does not require new titles, but does require team leadership to be present in the decision. |

### Phase 5: Ratifying (Implementing the decision)

| Need | Question |
|---|---|
| Make the commitment visible | Has the committed work been placed on the Kanban board (or other information radiator) so the team and stakeholders can see it? "Decisions on invisible work are decisions on imagined work." |
| Confirm per-stage batch limits | If the decision adds work to a stage, does it respect the team's working batch size at that stage, or does it push the stage over? |
| Honour pull discipline | Have team members been told to push the new work, or is the work in a backlog they can pull from when they have capacity? Push violates pull discipline. |
| Communicate the decision (and the reasoning) | Has the *why* of the decision been communicated alongside the *what*? Open Kanban's Communication and Collaboration value treats these as inseparable. |
| Schedule the learning point | When will the team inspect whether this decision worked? Retrospective, Strategy Meeting, or Kaizen Group — pick one. Decisions without an inspection point have no learning loop. |
| Surface any value-violation in the commitment | If the implementation requires *Muri* (overburden), or push-based dispatch, or local optimisation at the expense of system flow — name it before the work begins, not after. |

### Phase 6: Monitoring (Was the decision a good one?)

| Need | Question |
|---|---|
| Inspect against system flow, not local efficiency | Has overall flow (lead time, throughput, value delivered) improved, or only stage-local efficiency? The holistic / systemic value puts the question at the system level. |
| Watch for multitasking creep | Has the team's WIP at each stage drifted back up? Batch-size discipline is forward-looking; without monitoring, it lapses. |
| Check sustainable pace | Is the team sustaining the cadence, or are they running on reserves they cannot rebuild? *Muri* is the named anti-pattern. |
| Surface what was learned | At the next learning event (Retrospective, Strategy Meeting, or Kaizen Group), name what the team learned from this decision. Open Kanban's continuous-improvement practice is empty without an explicit learning step. |
| Test for upward-correction patterns | Has the team had courage moments — has lower-rank correction of higher-rank decisions actually happened? If not, the courage value is rhetorical, not operational. |
| Adjust the batch-size dial | If overall flow improved with smaller batches, can the team go smaller still? If it worsened, the batch may have been too small for the work's structural minimum. |
| Watch for partial-implementation drift | Has the team quietly dropped one of the practices (the learning step is the most commonly skipped)? Open Kanban's deliberate incompleteness assumes the four practices are all present. |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| Work queues build at one stage while other stages sit idle | A batch-size or pull-discipline problem, not a resource problem | Map the value chain; identify the stage where work accumulates; apply per-stage batch reduction |
| Team members juggling five or more items simultaneously | Multitasking is the operating norm; "multitasking does not work" is Open Kanban's named position | Surface total WIP per person; ask which one item finishes fastest with focused effort |
| A proposed improvement speeds up one stage but overall lead time stays flat | Local optimisation — the holistic / systemic value (Deming + Goldratt) refuses to call this improvement | Identify where the system constraint has shifted; work is now stuck elsewhere |
| Work is being assigned by a manager or upstream scheduler rather than pulled by the doer | Push-based dispatch; violates pull-scheduling and the Respect-for-people value | Establish a visible backlog; let team members pull when capacity is available |
| "Continuous improvement" is claimed but no regular learning event (Retro, Strategy Meeting, Kaizen Group) exists | Improvement decisions are being made without a learning structure | Introduce a named learning cadence before the next improvement cycle |
| Team is consistently working late or running on reserves | Muri (overburden); sustainable pace is a hard constraint, not a preference | Scale back committed batch; use the sustainable-pace test before next commitment |
| Correction of a higher-rank decision never happens even when the data supports it | Courage value is rhetorical, not operational; upward feedback is suppressed | Create a structured forum where lower-rank correction is expected and recorded |

## When to Use This Reference

- A *flow-of-work* problem needs structuring — work piles up at one stage, gets pushed at another, with no team-level discipline about what gets pulled and when.
- A *push-based dispatch pattern* needs naming — work is being assigned by an upstream dispatcher rather than pulled by the team member who will do it.
- A *multitasking pattern* is visible — team members are in-flight on multiple items and finishing none quickly.
- A *batch-size question* needs framing — is the team committing to too large a batch at one stage of the value chain?
- A *local optimisation* is being celebrated — one stage is faster, but overall flow has not improved or has worsened.
- A *Lean lineage / TPS framing* is needed — *Muri*, *Muda*, and pull-based scheduling vocabulary apply.
- A *Deming + Goldratt systems lens* is appropriate — the question is about system throughput, not local efficiency.
- An *open-licence Kanban methodology* is wanted — Open Kanban is the only clean-CC Kanban specification this corpus ships.
- A *WIP-limit-versus-batch-size* clarification is needed — Open Kanban's distinctive position (limit WIP is downstream of batch reduction, not the primary lever) is the named view.
- A *learning-step-before-improvement* discipline needs naming — continuous improvement without an explicit learning structure is rhetoric.
- A *kernel-plus-extensions* methodology shape is helpful — Open Kanban's "heart of method" framing fits when the operator wants a substrate to build local practice on, not a complete prescription.
- Canonical Kanban authority works (Anderson, Burrows, Reinertsen) are not CC-licensed and do not ship with this corpus. For WIP-limit policies, service classes, quantitative flow metrics, cost-of-delay, or WSJF, look outside this source.

## Worked Example

A six-person product team has just shipped a major release. The product manager observes that the team consistently carries eight to twelve stories in flight simultaneously across three stages (dev, review, QA), yet the average story takes three weeks to finish. A senior engineer proposes doubling the team's code-review velocity as the fix.

The team leads reads the Open Kanban framework before the retrospective. She recognises the proposal as stage-local optimisation: speeding up review leaves dev and QA intact, so the constraint likely shifts rather than dissolves. She runs the holistic / systemic check — "no single part of a system can ever bring overall improvement" (Source: Hurtado, *Open Kanban*, "Open Kanban Values" — Holistic or Systemic Approach to Change) — and asks the team to map the whole value chain instead.

The mapping reveals that QA is the constraint: stories reach QA faster than QA can work them, so batch build-up is at QA, not review. The team leads applies the batch-size decision rule: "Reduce the complexity and the quantity of things you do at any stage of the value chain" (Source: "Open Kanban Practices" — Reduce the Batch Size). Instead of more reviewers, the team agrees to limit the stories that can enter QA at one time to three, and to reduce story size so individual items take two days to QA rather than seven.

The team member who will do the QA work sets the pull limit herself — the decision about what to pull next sits with the doer, not with a dispatcher (Source: "Open Kanban Values" — Respect for people). The senior engineer's original proposal is recorded with its reasoning; the team agrees to revisit the review-velocity question after one cycle to see whether QA is still the constraint.

Four weeks later the team's average story completion time has dropped from three weeks to nine days. The constraint has shifted slightly to dev capacity, which is the next batch-size target.

## Anti-patterns This Reference Helps Avoid

**Confusing WIP-limiting with batch-size reduction.** Treating a WIP cap as the primary Kanban lever — and assuming batch-size reduction is merely a synonym or consequence — inverts the framework's stated logic. Open Kanban names WIP-limiting as *downstream* of batch-size reduction: "Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around." The decision-maker who focuses on the cap rather than on the complexity and quantity of work at each stage has the sequence backwards. (Source: Hurtado, *Open Kanban*, "Open Kanban Practices" — Reduce the Batch Size.)

**Celebrating local-stage improvements as overall improvement.** Speeding up one stage of the value chain and calling it a system improvement. The holistic / systemic value, grounded in Deming and Goldratt, refuses this: "no single part of a system can ever bring overall improvement." A decision that raises one stage's throughput while leaving overall lead time flat — or shifting the constraint elsewhere — is not an improvement by the framework's standard. ("Open Kanban Values" — Holistic or Systemic Approach to Change.)

**Treating "continuous improvement" as a slogan rather than a practice.** Announcing improvement cycles without an explicit learning structure in place. Open Kanban is direct: "Learning is the key concept before continuous improvement can ever happen!" A team that iterates without retrospectives, strategy meetings, or Kaizen Groups is running improvement decisions without a feedback mechanism. The improvement is rhetorical, not operational. ("Open Kanban Practices" — Learn and improve continuously.)

**Overloading the team in the name of commitment.** Accepting commitments that require the team to work beyond a sustainable pace — *Muri* in Lean vocabulary. "If you respect your team you will not work them to death... An exhausted developer, manager or team are the perfect recipe for disaster. Kanban cannot succeed this way." Decisions about batch size, commitment scope, and deadline pressure must pass the sustainable-pace test before they count as real commitments. ("Open Kanban Values" — Respect for people.)

**Suppressing upward correction of authority errors.** A culture where lower-rank team members will not surface mistakes made by managers or executives. The framework names this directly: "When a manager, VP, or person in authority makes a mistake and someone with lower rank notices it, it takes courage for him to tell us about it." Without the Courage value operating, the pull-based decision model is silently replaced by push-based compliance. Decisions get made on the authority's preference rather than on the system's evidence. ("Open Kanban Values" — Courage.)

**Imposing work on team members rather than letting them pull.** Assigning work to individuals (push) instead of maintaining a visible backlog from which team members pull when they have capacity. The Respect-for-people value is the prerequisite for pull-scheduling: "Respect for people allows for delegation and the demand-pull that is crucial to Kanban." Push-based dispatch removes the decision right from the person who will do the work — a violation of the framework's authority model regardless of how the assignments are described. ("Open Kanban Values" — Respect for people.)

## Integration with Other References

| Reference | How it pairs with Open Kanban |
|---|---|
| Schwaber & Sutherland, *The Scrum Guide* (2020) | Open Kanban and Scrum share continuous-improvement and visualisation disciplines but differ in cadence (continuous flow vs fixed Sprint), roles (no new titles vs three accountabilities), and control variable (batch-size per stage vs Sprint Goal commitment). Use Open Kanban when arrival patterns are unpredictable or Sprints feel forced; use Scrum when work organises naturally into Sprint-Goal-anchored cycles. |
| Letaw, *Handbook of Software Engineering Methods* | Letaw operationalises Agile practice at practitioner detail. INVEST, Definition of Done, story points, and fist-of-five voting all fit inside Open Kanban's practices. Use Letaw for the methods inside the practices; use Open Kanban for the value-and-practice framing. |
| Jones, *Evidence-Based Software Engineering* | Jones interrogates Agile and Kanban claims as largely folklore. Open Kanban's empirical claims (multitasking, batch-size effect on flow) are the kind Jones would press; Reinertsen (cited by Hurtado) is one of few sources Jones treats as evidence-grounded. Use Jones to assess evidence quality behind Kanban claims; use Open Kanban for the framework's stated position. |
| OpenStax, *Accounting Vol 2* | Covers the Theory of Constraints five-step (identify, exploit, subordinate, elevate, repeat) that Open Kanban cites by name. Use OpenStax for the formal ToC analysis; use Open Kanban for how the holistic-systems lens lands at team level. |
| OpenStax, *Principles of Management* | PDCA at the management level maps onto Open Kanban's *Learn and improve continuously* at team level. Use Principles of Management for the management-cycle framing; use Open Kanban for the team cycle inside it. |
| OpenStax, *Introduction to Business* | Covers Deming's broader management theory (TQM, DMAIC) that Open Kanban cites for its Holistic / Systemic value. Use Introduction to Business for TQM context; use Open Kanban for how Deming's systems thinking lands inside Kanban team discipline. |
| OpenStax, *Organizational Behavior* | Provides the team-decision theory (groupthink, escalation, conflict modes, speaking-up culture) that Open Kanban's pull-based, courage-enabled decision-rights operationalise. Use OB for the broader theory of team voice; use Open Kanban for how that voice functions inside a Kanban team. |
| OpenStax, *Psychology 2e* | The *Muri* / sustainable-pace claim in the Respect-for-people value lands directly on stress and burnout literature (GAS, allostatic load). Use Psychology 2e for empirical grounding of why exhausted teams fail; use Open Kanban for how the methodology builds non-exhaustion into the framework. |
| NHS *A Just Culture Guide* | The Courage value (upward correction without fear) and NHS Just Culture (default to system investigation) work opposite sides of the same problem. NHS Just Culture protects the person who surfaces an issue; Open Kanban's Courage value motivates them to surface it. Use both when designing conditions for lower-rank correction of higher-rank decisions. |
| US Forest Service, *LFUO/FLA/LR 2024 Implementation Guide* | LFUO's Just Culture / Systems Thinking / Learning principles are the same lineage Open Kanban cites for its Holistic / Systemic value (Deming) and Learning practice. Use LFUO for operationalised learning-from-events methodology (AAR → RLS → FLA → Learning Review); use Open Kanban for team-level decision-discipline. |
| US Army, *TC 25-20 After-Action Reviews* | Open Kanban names Retrospectives as one candidate form for its *Learn and improve continuously* practice; the AAR is the structured retrospective at its most disciplined. Use TC 25-20 for AAR methodology when the team's learning form is a retrospective. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The following sources appear in the deep reference as [BT] citations — the source text cites them by name but this corpus does not hold them as primary references. Treat claims tracing to these sources as resting on a second-hand representation:

- *Kent Beck, Extreme Programming Explained* — cited by name as the source of the Courage value framing ("Like Kent Beck noticed...").
- *W. Edwards Deming, System of Profound Knowledge* — cited (with link to deming.org) as grounding for the Holistic / Systemic Approach value.
- *Eliyahu M. Goldratt, Theory of Constraints* — cited alongside Deming for the same value.
- *Alistair Cockburn, "Information radiator"* — cited as the conceptual source for visualisation extending beyond the Kanban board.
- *Donald G. Reinertsen, The Principles of Product Development Flow* — cited as "one of the best explanations" of batch-size reduction's effect on flow.
- *Toyota Production System* (Wikipedia citation) — cited as the Japanese origin of Kanban and the Lean / TPS lineage.
- *Agile Manifesto* (agilemanifesto.org) — cited as one of the two movements Open Kanban aligns with.
- *Lean software development* (Wikipedia citation) — cited as the second movement Open Kanban aligns with.
- *VersionOne 2013 State of Agile Survey* — cited as evidence of Kanban's doubling adoption among Agile methodologies.
- *Alan Shalloway, Kanban for Teams; Corey Ladas, Scrumban; Karl Scotland, Kanban Thinking* — named as fellow-traveller methods.
- *Free Software Foundation, four freedoms* — cited as the model for Open Kanban's four freedoms.
- *Kaizen Groups* (Wikipedia citation) — one form the Learn and improve continuously practice can take.

**Named limits of this source.** Open Kanban is the heart of a Kanban method, not a complete methodology. It explicitly declines to prescribe WIP limits, service classes, quantitative flow metrics (cumulative flow diagrams, Little's Law, lead-time histograms), cadence or replenishment rituals, or cost-of-delay analysis. Claims about those topics require sources outside this corpus.

**Evidence-marker continuity.** The deep reference carries several [V] passages that this distillation paraphrases. Key [V] passages include: the pull-based scheduling / Respect-for-people coupling; the batch-size-vs-WIP-limit distinction; the multitasking claim ("multitasking does not work"); the Deming + Goldratt holistic systems quotation; the Muri / sustainable-pace passage; and the *Learn and improve continuously* passage on learning as the prerequisite for improvement. Distillation cites by section name throughout; verbatim text lives in the deep reference only.
