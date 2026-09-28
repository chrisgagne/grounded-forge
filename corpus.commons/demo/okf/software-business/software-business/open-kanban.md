---
type: distillation
title: "Hurtado, Open Kanban"
description: "Hurtado, Open Kanban, projected onto the software-business task axis; evidence markers and attribution travel in-band."
resource: https://github.com/agilelion/Open-Kanban
tags: [distillation, software-business]
task: software-business
scope: open
sources:
  - id: open-kanban
    title: "Hurtado, J. (with Annita Yegorova Hurtado), AgileLion Institute. Open Kanban — Open Source Initiative to create a Kanban core that is Agile, Lean and Free. Release 1.00 Rev A. Licence: CC BY 3.0 Unported. https://github.com/agilelion/Open-Kanban."
    resource: https://github.com/agilelion/Open-Kanban
generated:
  by: grounded-forge/0.4.0
  at: 2026-09-28T15:12:32+13:00
---
# Hurtado, Open Kanban — Software-Business Distillation

**Source:** Hurtado, J. (with Annita Yegorova Hurtado), AgileLion Institute. *Open Kanban — Open Source Initiative to create a Kanban core that is Agile, Lean and Free*. Release 1.00 Rev A. Licence: CC BY 3.0 Unported. https://github.com/agilelion/Open-Kanban.

**Authoritativeness caveat (operator note, not from the source).** Open Kanban is the only clean-CC Kanban methodology specification this corpus ships, but it is not the canonical Kanban authority. Hurtado is a minor author by broader industry-recognition standards; other widely recognised Kanban primary sources (Lean Kanban University material, commercial publishers) are non-redistributable and therefore not in this corpus. For software-business questions where canonical Kanban authority is load-bearing, look outside this corpus. (Source: deep reference, "Corpus-role caveat".)

## Software-Business Relevance

Open Kanban applies to software-business work at the seam where engineering capacity, delivery cadence, and commercial commitment have to be priced against each other. The framework treats the *batch size* of committed work as the primary lever — explicitly upstream of WIP limits — and makes the per-stage decision rule the place where flow is decided. For a founder, CTO, engineering manager, or technical product leader, the four practices and five values cluster onto three software-business concerns: how to plan engineering capacity against commercial commitments (Phase 2), how to design delivery cadence and operating governance (Phase 4), and how to think about people-as-capacity in a way that does not silently externalise overwork onto the team and re-import the cost as attrition or defect rates (Phases 2 + 3 boundary).

Three threads carry the software-business projection.

**Thread one: batch-size reduction as the primary capacity-and-cadence decision.** Open Kanban's signature contrarian position is that the framework does not ask teams to limit WIP; it asks them to reduce the batch size of effort at every stage of the value chain, of which limiting WIP is a downstream consequence (Source: Hurtado, *Open Kanban*, "Open Kanban Practices" — Reduce the Batch Size). The software-business consequence is structural: capacity planning that begins with the smallest deployable unit at each SDLC stage will produce different commercial commitments than capacity planning that begins with aggregate headcount or with a fixed-length cycle. Hurtado cites Donald G. Reinertsen's *Principles of Product Development Flow* as "one of the best explanations" [V] of the batch-size-to-flow relationship (deep ref, "Open Kanban Practices"; "Connections the author makes in the text").

**Thread two: holistic / systemic framing over local optimisation.** The Holistic-or-Systemic-Approach value is grounded explicitly in Deming's System of Profound Knowledge and Goldratt's Theory of Constraints — both cited by name in the source. The position is that "no single part of a system can ever bring overall improvement" [V] (Source: Hurtado, "Open Kanban Values" — Holistic or Systemic Approach to Change). For software-business work, this is the operating principle that disciplines change-management situations (Phase 4) and resists a familiar failure in operating reviews: declaring one stage faster while overall lead time has not moved. Goldratt's Theory of Constraints is treated formally in OpenStax *Accounting Vol 2* (the five-step ToC); Open Kanban cites TOC by name for its holistic value without developing it.

**Thread three: sustainable pace as a financial discipline, not a virtue claim.** The Respect-for-people value pairs Agile's sustainable pace with Lean's *Muri*, and warns that an exhausted developer, manager, or team is "the perfect recipe for disaster" [V] and "Kanban cannot succeed this way" [V] (Source: Hurtado, "Open Kanban Values" — Respect for people). The software-business reading is that commitments which require overwork are commitments the framework refuses to call success — and the operating consequence is that the cost of overcommitment lands somewhere (attrition, defect rates, dropped roadmap items) regardless of whether the operating review acknowledges it. This is the methodology's contribution to the speed-vs-quality tension in Phase 2 and to the engineering-management culture decisions in Phase 3.

A fourth thread runs through the licence framing: Open Kanban explicitly chose Creative Commons Attribution 3.0 over LGPL v3 and MIT because the methodology is *knowledge work*, not source code (Source: Hurtado, "Open Kanban's License"). This carries a software-business adjacency for AI-integration and build-vs-buy decisions where the question is what licensing applies to knowledge-work artefacts (playbooks, prompts, model fine-tunes, training material); the framework's own choice is a worked example of the distinction.

## Key Concepts for Software-Business

1.  **Batch-size reduction as the primary flow lever.** Open Kanban's signature contrarian position: "Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around... Open Kanban does not ask you to limit WIP, but it does request that you 'Reduce the Batch Size of your Efforts'" [V] (Source: Hurtado, "Open Kanban Practices" — Reduce the Batch Size). For software-business work, this reshapes capacity planning, roadmap commitment, and the speed-vs-quality framing.

2.  **Per-stage batch discipline (software case).** The mechanism is two-lever: reduce *complexity per item* (avoid epics; keep stories simple) and reduce *quantity per stage* of the SDLC. The decision is per-stage, not aggregate (Source: Hurtado, "Open Kanban Practices" — Reduce the Batch Size).

3.  **Reinertsen flow lineage.** Hurtado cites Donald G. Reinertsen's *Principles of Product Development Flow* as "one of the best explanations" [V] of why batch-size reduction improves flow (Source: Hurtado, "Open Kanban Practices"; "Connections the author makes in the text"). Hurtado does *not* reproduce Reinertsen's quantitative apparatus (cost-of-delay, weighted-shortest-job-first); the source is conceptual not quantitative on this front.

4.  **Multitasking refused.** "Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work" [V] (Source: Hurtado, "Open Kanban Practices" — Reduce the Batch Size). A pre-committed position against parallel work as a productivity strategy in capacity-planning conversations.

5.  **Holistic / systemic frame as the decision lens.** "Deming's System of Profound Knowledge and Goldratt's Theory of Constraints reminds us that no single part of a system can ever bring overall improvement. We need to take a holistic view of the system and understand it" [V] (Source: Hurtado, "Open Kanban Values" — Holistic or Systemic Approach to Change). For software-business: improving one part of the system does not by itself bring overall improvement; judge the change against the whole.

6.  **Sustainable pace as financial discipline.** "If you respect your team you will not work them to death, or subject any worker to intellectual or physical demands that make it nearly impossible to succeed. An exhausted developer, manager or team are the perfect recipe for disaster. Kanban cannot succeed this way" [V] (Source: Hurtado, "Open Kanban Values" — Respect for people). The source pairs this sustainable pace with Lean's *Muri*; the cost of overcommitment lands somewhere regardless of whether the operating review acknowledges it.

7.  **Pull-based scheduling as a decision-rights claim.** "Respect for people allows for delegation and the demand-pull that is crucial to Kanban. When any developer is able to take a story from the backlog and pull it to development or QA, he is able to do so because we respect him" [V] (Source: Hurtado, "Open Kanban Values" — Respect for people). Respect lets the person doing the work pull the next item; the push-versus-pull contrast is this distillation's reading.

8.  **Kanban board / information radiators as transparency artefacts.** "Kanban boards [are] visual representations of the flow of work that show how work items move from stage to the next... If you are a manager you can easily see at any moment what is the status of things, and if you are a team member you can see your impact on the overall work" [V] (Source: Hurtado, "Open Kanban Practices" — Visualize the workflow). Alistair Cockburn's "information radiators" term is cited; the scope extends to dashboards and performance metrics in the work environment. For software-business: the artefact that makes operating status legible to non-engineering stakeholders without translation overhead.

9.  **Team-based leadership without role restructuring.** "Although Kanban starts where you are, and does not need to modify any titles or roles in an organization, Kanban cannot work without a team to deliver value. Teams and team leadership are crucial to deliver value... No need for new roles or titles, but we do have a need for working teams, with leaders in them!" [V] (Source: Hurtado, "Open Kanban Practices" — Lead using a team approach). For software-business: the methodology does not require reorganisation ("Kanban starts where you are" [V]), which lowers the change-management cost of adoption.

10.  **Continuous learning is under-prescribed by design.** "There are many ways a Kanban team can implement this practice, you could have Retrospectives, Strategy Meetings or even Kaizen Groups" [V] (Source: Hurtado, "Open Kanban Practices" — Learn and improve continuously). The form is left to local context; the function is non-negotiable. For software-business operations and process design, the choice of which form fits is the operator's call, not the framework's.

11.  **Kernel-plus-extensions architecture.** "Open Kanban is not a full or complete Agile or Lean method, instead it is the heart of that method that is the reason it can be ultra light. The best comparison in the software world would be the kernel of an open source operating system" [V] (Source: Hurtado, "Open Kanban Definition"). Extensions such as Hurtado's own Kanban Ace build on the kernel; Scrumban, Kanban for Teams and Kanban Thinking are fellow-traveller methods the source invites to join. For software-business adoption: the methodology can be combined with existing practices without requiring wholesale replacement.

12.  **CC BY 3.0 as a knowledge-work licensing choice.** "Although the first two licenses [LGPL v3, MIT] are appropriate, both are designed for sharing of computer source code. Creative Commons on the other hand is appropriate for knowledge work that deals with writing, and media creation" [V] (Source: Hurtado, "Open Kanban's License"). For software-business work touching the licensing of methodologies, prompts, model fine-tunes, training material, and other knowledge-work artefacts, this is a worked example of the source-code-vs-knowledge-work licensing distinction.

13.  **Cross-domain applicability.** "Although it's main focus is in IT and Software Development, Open Kanban can be used in any business or non-profit to achieve agility and continuous improvement" [V] (Source: Hurtado, "Open Kanban Definition"). The methodology can carry from engineering teams to operations, marketing, finance, and other business functions without re-derivation.

## Questions to Ask During Software-Business Work

### Phase 1: Strategic positioning

| Need | Question |
|---|---|
| Surface flow-economics in a build-vs-buy decision | If the *buy* option preserves the buyer's existing batch size and the *build* option requires reducing batch size to ship, does the comparison price the flow-economics difference, or only the unit cost? Open Kanban's per-stage batch discipline (and the Reinertsen lineage Hurtado cites) is the framework that makes the difference legible. |
| Test a pricing decision tied to engineering effort | Is the price being set against resource hours (how busy people are) or against deliverable units per cycle? Open Kanban's holistic value asks whether the whole system improves and treats people as more than resources; set the price against what the system delivers, not against how busy people are. |
| Frame a capacity-claim in market-entry analysis | When the analysis claims the team "has capacity" to enter a new market, is the claim about per-stage batch size at each SDLC stage, or about aggregate headcount? Open Kanban's framing treats per-stage discipline as the load-bearing claim. |
| Surface an AI-integration scope question | If the AI-integration proposal expands the team's batch size at the discovery and design stages (more concurrent prompt-and-model experiments) while shrinking it at the build stage (faster code generation), is the *overall* flow improved or shifted? Apply the holistic-systemic test. |
| Anchor competitive-response reasoning | If a competitor ships faster, is the response to add headcount (push more into the system) or to reduce batch size so the team focuses and finishes faster? Open Kanban's batch-size practice favours the second; its holistic value asks whether the whole system improves. |

### Phase 2: Product and engineering economics

| Need | Question |
|---|---|
| Test a technical-debt-vs-revenue trade-off | Is the technical-debt remediation work being framed as a *commitment* that requires removing other commitments from the queue (batch-size discipline at the planning stage), or as overhead absorbed silently by the team (overwork)? Open Kanban's Respect-for-people value warns against the second. |
| Test a reliability investment against a commercial milestone | If the reliability work expands the team's commitment in one cycle, does the plan reduce batch size elsewhere, or does it stack the reliability work on top of existing commitments? Stacking pushes the team past a sustainable pace. |
| Frame a capacity-planning conversation | Is the planning conversation about how busy people can get, or about how small the per-stage batch can get and how fast it can move through the system? Open Kanban's batch-size practice speaks to the second; it does not address utilisation directly. |
| Detect a roadmap-capacity mismatch | If the roadmap commitments require N items in flight per stage and the team's empirical capacity is M items (where M < N), what is the plan to reduce N rather than ask the team to deliver M+? Open Kanban's "Reduce the Batch Size" [V] practice is the named lever. |
| Frame a "speed vs quality" tension | Is the speed-vs-quality framing being used to justify overwork as the only path to the milestone? Open Kanban's Respect-for-people value warns against it: an exhausted team is "the perfect recipe for disaster." [V] Reduce batch size before reducing quality or pace. |
| Surface multitasking as a hidden capacity cost | How many concurrent items is each engineer (or each engineering team) in-flight on at any one stage? Open Kanban's position: "multitasking does not work." [V] If the number is high, the capacity model is over-counting. |
| Apply the whole-system test to an improvement claim | Does the proposed improvement help the whole system, or only one stage? Open Kanban's holistic value holds that no single part of a system can bring overall improvement. |
| Frame an estimate against the cone of uncertainty | Open Kanban does not give a quantitative estimation framework, but the source's framing of "reduce the complexity and the quantity of things you do at any stage" [V] is structurally a request for smaller estimable units. For estimation discipline directly, route to Jones (`jones-evidence-based-sweng`) and Letaw (`letaw-handbook-sweng-methods`). |

### Phase 3: Team and capability building

| Need | Question |
|---|---|
| Frame a hiring decision against batch size | If the team's batch size is the problem, is hiring the right move? Open Kanban does not address hiring; its batch-size practice suggests asking first whether fewer concurrent items would do what more people are meant to do. |
| Test a culture-decision against the five values | Is the proposed culture intervention consistent with Respect for people, Courage, Focus on Value, Communication and Collaboration, and Holistic/Systemic Approach? Open Kanban's values are "an integral part of Open Kanban" [V]; an intervention that cuts against one should name the conflict. |
| Frame a levelling or compensation decision around sustainable pace | Are the compensation incentives rewarding overwork disguised as commitment, or sustainable pace? Open Kanban warns that an exhausted team is "the perfect recipe for disaster" [V]. |
| Test an "engineers should be more strategic" claim | Open Kanban does not require new roles or titles, but it does require team leadership and pull-based scheduling. If the strategic ask is for engineers to pull work they have the context to decide on, the framework supports it; If the strategic ask is for engineers to pull work they have the context to decide on, that fits the demand-pull the source ties to respect; if the ask is for engineers to absorb a coordination layer the org has not built, Open Kanban does not cover that, so name the gap. |
| Frame a contractor / vendor / hybrid-team decision | Open Kanban's cross-domain applicability claim allows the framework to extend to vendor teams; the values (especially Communication and Collaboration, packaged as one) become the design criterion for the contractor relationship. For the moral-hazard analysis directly, route to Jones (`jones-evidence-based-sweng`). |

### Phase 4: Operations and process

| Need | Question |
|---|---|
| Choose between Scrum, Kanban, and a hybrid for delivery cadence | Open Kanban prescribes no cadence; teams that find fixed-length Sprints a poor fit may find its values-and-practices kernel enough. Use Scrum (`scrum-guide-2020`) when the work can be organised into Sprint-Goal-anchored cycles. Open Kanban's deliberate under-prescription is the load-bearing fit-test: if the team needs less structure than Scrum provides, Open Kanban is the framework that names what is non-negotiable (values + practices) without prescribing the *how*. |
| Design a change-management approach for software-process adoption | Open Kanban's "starts where you are" [V] framing asks for no new titles or role redefinition, which keeps adoption friction low. For richer practice-by-phase guidance, combine with `open-practice-library`. |
| Frame governance / decision-rights ambiguity | Open Kanban ties demand-pull to respect: the person doing the work is empowered to pull the next item. Combine with Letaw's RACI (`letaw-handbook-sweng-methods`) for the formal decision-rights structure; Open Kanban supplies the principle that the doer is empowered to pull. |
| Detect a push-based dispatch pattern in delivery operations | Is work being assigned by an upstream dispatcher (push) or pulled by the team member when they have capacity (pull)? The source ties demand-pull to respecting and empowering the person doing the work; the push-versus-pull contrast is this distillation's reading. |
| Design a retrospective / learning loop | Open Kanban names Retrospectives, Strategy Meetings, and Kaizen Groups as candidate forms without prescribing a cadence. For Retrospective design specifically, combine with `approach-perfect-field-guide-scrum-events`; for AAR methodology, route to `tc-25-20-army-aar`. |
| Visualise the work for cross-functional governance | Is the work visible to non-engineering stakeholders (board members, commercial leads, customer-success teams) via a Kanban board or information radiator? Hurtado's visualisation practice, using Cockburn's term *information radiators*, is what makes operating status legible without translation overhead. |
| Apply the holistic-systemic frame to an operating-review claim | Is the operating review crediting a stage-local improvement as overall improvement? Open Kanban's holistic value, citing Deming and Goldratt, holds that no single part of a system can bring overall improvement. |

### Phase 5: Risk, reliability, compliance

| Need | Question |
|---|---|
| Frame an incident-response cadence question | Open Kanban does not address incident response directly. For incident-response framing, route to `nhs-just-culture-guide` (Just Culture decision aid), `tc-25-20-army-aar` (AAR methodology), and `lfuo-learning-review-guide-2024` (Learning Review). Open Kanban's contribution is upstream: the sustainable-pace and pull-based-scheduling discipline that reduces the conditions under which incidents proliferate. |
| Test a compliance-investment-vs-revenue trade-off | Is the compliance work being added to the queue without removing other items (overwork), or is the planning explicit about what comes out to make space? Open Kanban's batch-size discipline applies. |
| Frame a reliability-vs-PR incident in operating terms | Open Kanban's Holistic-Systemic value, grounded in Deming, treats the system as the primary unit of analysis. The PR conversation often defaults to individual accountability; the holistic value points the analysis at the system instead. For deciding how to treat the people involved in the incident, route to `nhs-just-culture-guide`. |
| Apply the Courage value to a regulator-inquiry context | "When a manager, VP, or person in authority makes a mistake and someone with lower rank notices it, it takes courage for him to tell us about it" [V] (Source: Hurtado, "Open Kanban Values" — Courage). For regulator inquiries, the upward-correction mechanism the Courage value names is the same mechanism that lets the team surface issues before they become regulator issues. |

### Phase 6: Stakeholder communication

| Need | Question |
|---|---|
| Translate engineering operating status to a non-engineering executive | The Kanban board (or information radiator equivalent) is the artefact that makes flow visible without translation. Hurtado's framing, using Cockburn's term, extends visualisation to "dashboards, performance metrics or other information radiators" [V], which supports the case for shared operating dashboards. |
| Frame a board-paper claim about engineering capacity | Is the capacity claim being made in flow vocabulary (per-stage batch size, lead time) or in resource vocabulary (engineer-hours, sprint velocity, headcount)? Open Kanban's batch-size practice supplies the first; the source does not address the second directly. |
| Communicate a roadmap-replan to commercial stakeholders | If the replan reduces commitments to bring the team back to sustainable pace, is the rationale being framed as *operational discipline* (the framework's framing) or as *the team can't deliver* (a framing the framework refuses)? The framework's framing puts the problem in overwork, not in the team's performance. |
| Anchor an exec-memo argument against a utilisation-target | Open Kanban's batch-size practice, with its Reinertsen citation, is a short primary-source argument for focusing and limiting work in progress; it does not address utilisation directly. |
| Frame a CTO-to-board translation of operating health | The Kanban board, the per-stage batch size, the sustainable-pace constraint, and the whole-system claim together form a board-reportable operating-discipline picture that does not require board members to read code. |

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| Operator names a pricing decision tied to engineering effort | Batch-size reduction and the whole-system view (Source: Hurtado, "Open Kanban Practices" — Reduce the Batch Size; "Open Kanban Values" — Holistic or Systemic Approach to Change). | Price against the smallest deployable unit at each SDLC stage rather than against how busy people are. Per-stage batch size is the capacity claim to test; aggregate headcount comes after. (Cite Hurtado on batch-size reduction and the whole-system view; Hurtado cites Reinertsen, who is not held in this corpus.) |
| Operator describes a roadmap-capacity mismatch | Batch-size reduction, of which limiting WIP is a consequence; per-stage batch discipline as the planning unit (Source: Hurtado, "Open Kanban Practices" — Reduce the Batch Size). | When roadmap commitments exceed empirical per-stage capacity, the right move is to reduce the batch size of committed work, not to ask the team to deliver more in parallel. Multitasking is named as not working, and an exhausted team as "the perfect recipe for disaster" [V]. |
| Operator names a "speed vs quality" tension | Sustainable pace (paired with Lean's *Muri*) and batch-size reduction (Source: Hurtado, "Open Kanban Values" — Respect for people; "Open Kanban Practices" — Reduce the Batch Size). | Open Kanban does not address the speed-quality trade-off directly; its batch-size practice (focus, fewer things in progress) and its warning against exhausting the team are the levers it offers. |
| Operator names a delivery-cadence question (sprints, releases, deployment frequency) | Kanban flow primitives (visualise the workflow, reduce batch size) with no prescribed cadence; under-prescribed learning practice (Source: Hurtado, "Open Kanban Practices" — Visualize the workflow; — Learn and improve continuously; "Open Kanban Definition"). | Open Kanban prescribes the values and the four practices and names no cadence; it asks for no new roles or titles and leaves the form of the learning practice open. Teams that find fixed-length cycles a poor fit can start from this kernel. |
| Operator describes a change-management situation specific to software work | Holistic/Systemic value (Deming + Goldratt lineage); "starts where you are" [V] framing (Source: Hurtado, "Open Kanban Values" — Holistic or Systemic Approach to Change; "Open Kanban Practices" — Lead using a team approach). | Open Kanban keeps adoption friction low: no role redefinition required, change happens at the team level through the four practices, and the whole-system frame disciplines which improvements count. |

## What to Look For

**Pattern: utilisation-based capacity claim.** *Signal:* the capacity claim is stated in engineer-hours, sprint velocity, or headcount; words like "busy," "available bandwidth," "burn rate" appear. *Diagnosis:* the framing treats the team only as a resource pool; Open Kanban's holistic value asks that people be seen "not just as resources, but also as full rounded individuals who make the system work" [V]. *Follow-up:* reframe the claim in flow vocabulary (per-stage batch size, lead time) before the claim becomes a board-level commitment.

**Pattern: stacking work without removing work.** *Signal:* a new commitment is added (a reliability investment, a compliance project, a technical-debt remediation, a strategic priority) but no existing commitment is identified as coming out. *Diagnosis:* the team is being asked to work past a sustainable pace; the cost will land somewhere (attrition, defects, dropped items) regardless of whether the plan acknowledges it. *Follow-up:* name the trade and decide what comes out; if the answer is "nothing comes out," name the overwork explicitly.

**Pattern: local-stage improvement celebrated as overall improvement.** *Signal:* one stage is faster, one tool is adopted, one team is praised; overall lead time is not measured or has not moved. *Diagnosis:* the failure Open Kanban's holistic value (citing Deming and Goldratt) warns against; the improvement is local-only. *Follow-up:* apply the holistic-systemic test — has the whole system improved, or only one stage? If only one stage, the source says it cannot bring overall improvement.

**Pattern: push-based dispatch dressed as agile process.** *Signal:* work is being assigned to engineers by an upstream dispatcher (a tech lead, a product manager, a manager) rather than pulled by the engineer when they have capacity; sprint commitments are made *for* engineers rather than *by* engineers. *Diagnosis:* pull-based scheduling has been replaced by push; the demand-pull the Respect-for-people value enables is not happening. *Follow-up:* the operating fix is structural — engineers pull from the prioritised backlog when they have capacity; the dispatcher's role becomes prioritisation, not assignment.

**Pattern: continuous-improvement language without a learning structure.** *Signal:* the team or org claims to be "continuously improving" but cannot name when the team last learned something from a Retrospective, Strategy Meeting, or Kaizen Group. *Diagnosis:* "Learning is the key concept before continuous improvement can ever happen!" [V] — the source's framing. Without an explicit learning structure, the continuous-improvement claim is rhetoric. *Follow-up:* pick one form (Retrospective, Strategy Meeting, Kaizen Group, AAR), commit to a cadence, and instrument the learning capture.

**Pattern: multitasking framed as productivity.** *Signal:* engineers (or product managers, or commercial leads) are in-flight on multiple items per stage; status reports list many items at "in progress." *Diagnosis:* "Multitasking does not work" [V] — the framework's named position. Parallel work is slowing delivery. *Follow-up:* reduce concurrent items per stage; "keeping the team focused helps them finish what they start faster" [V] (Hurtado, "Open Kanban Practices" — Reduce the Batch Size).

**Pattern: WIP-limit policy adopted as the lever.** *Signal:* the team adopts a Kanban board with per-column WIP limits but the batch size of items entering the system has not changed. *Diagnosis:* the framework's named position is that WIP-limiting is *downstream* of batch-size reduction, not the lever itself. The source says limiting WIP also improves efficiency, but treats it as the consequence; the lever it asks for is smaller, simpler items. *Follow-up:* reduce the batch size of items at intake (smaller stories; fewer epics); WIP limits become a downstream consequence that the team can verify against the board.

## When to Use This Reference

- A *batch-size-vs-WIP-limit* clarification is needed for a software-business decision; Open Kanban's distinctive position (limit WIP is downstream of batch reduction, not the primary lever) is the named view in this corpus.
- A *batch-size-first* framing is needed for a capacity-planning or roadmap-commitment conversation, and the operator wants a CC-licensed methodology specification to cite (the source does not address utilisation directly).
- A *Reinertsen* pointer needs to be surfaced in a software-business decision (batch-size effect on flow), and the corpus does not carry Reinertsen primary — Open Kanban is the secondary source that cites Reinertsen as "one of the best explanations" [V] of batch-size reduction's effect.
- A *Deming + Goldratt systems lens* is the right discipline for an operating-review or change-management question, and the operator wants the one-line whole-system principle Open Kanban states rather than the management-textbook treatment.
- A *sustainable-pace constraint* needs to be named in a speed-vs-quality, hiring, or commitment conversation; the *Muri* / sustainable-pace pairing is Open Kanban's named lever.
- A *low-friction adoption* path is wanted for a software-process change; Open Kanban's "starts where you are" [V] framing — no new titles, no role redefinition — keeps change-management cost low.
- A *kernel-plus-extensions* methodology architecture is wanted, where the operator wants a substrate to build local practice on rather than a complete prescription.
- A *knowledge-work licensing* example is needed for an AI-integration, vendor, or partnership decision; Open Kanban's CC BY 3.0 choice (with the explicit reasoning against LGPL v3 and MIT) is a worked example in the corpus.

## When this distillation is **not** the right reach

- The question requires *canonical Kanban authority*. Look outside this corpus (operator note).
- The question requires *quantitative flow metrics* (cumulative flow diagrams, lead-time histograms, throughput run charts, Little's Law, weighted-shortest-job-first, cost-of-delay calculations). Open Kanban does not carry these. Jones (`jones-evidence-based-sweng`) offers general empirical critique of software-engineering claims but no flow apparatus; the quantitative apparatus itself is outside the corpus.
- The question requires *Kanban service classes* (standard / expedite / fixed-date / intangible). Open Kanban does not address service classes; look outside this corpus.
- The question requires *Sprint-Goal commitment discipline* or fixed-length-cycle anchoring. Route to `scrum-guide-2020` and `approach-perfect-field-guide-scrum-events`.
- The question is primarily about *strategic-positioning frameworks* (SWOT, PESTEL, Porter, VRIO, JTBD). Route to `openstax-principles-management` (or, when JTBD-shaped, to the task spec's anchor in Christensen).
- The question is primarily about *agency theory, moral hazard, or vendor-client information asymmetry*. Route to `jones-evidence-based-sweng`.
- The question is primarily about *organisational structure and role design*. Route to `openstax-principles-management` (six organisational structure types, Exhibit 4.6) and `letaw-handbook-sweng-methods` (RACI, Tuckman).

## Worked Example

A CTO at a mid-sized SaaS company has committed to the board that the team will ship Feature X (a major reliability investment, including a multi-region failover) and Feature Y (a customer-requested product extension) by end of Q3. The engineering team has been working at high tempo for two quarters; attrition has risen from 8% annual to 15% in the last six months; defect-injection rates have crept up; one senior engineer has flagged burnout in a 1:1. The COO has asked the CTO to "find the capacity" for an additional compliance project (Feature Z) that has been escalated by Legal.

**Batch-size-and-flow framing.** Features X, Y, and Z are three concurrent items at the planning stage of the SDLC; the team's empirical capacity is closer to two items. The framework's position: "Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work." [V] "Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around... Open Kanban does not ask you to limit WIP, but it does request that you 'Reduce the Batch Size of your Efforts.'" [V] (Source: Hurtado, *Open Kanban*, "Open Kanban Practices" — Reduce the Batch Size)

**Sustainable-pace constraint.** The attrition rate, the defect-injection trend, and the burnout flag are signals that the team is being asked to work past a sustainable pace. The source is explicit: "If you respect your team you will not work them to death, or subject any worker to intellectual or physical demands that make it nearly impossible to succeed. An exhausted developer, manager or team are the perfect recipe for disaster. Kanban cannot succeed this way." [V] (Source: "Open Kanban Values" — Respect for people)

**Holistic-systemic value.** The proposal to "find the capacity" for Feature Z is a stage-local improvement — Legal's queue clears — that worsens the whole: X and Y slip, attrition compounds, defect cost grows. "Deming's System of Profound Knowledge and Goldratt's Theory of Constraints reminds us that no single part of a system can ever bring overall improvement. We need to take a holistic view of the system and understand it." [V] (Source: "Open Kanban Values" — Holistic or Systemic Approach to Change)

**The memo.** The CTO opens with what becomes possible: the team can ship a deliverable reliability investment in Q3 by reducing batch size from three concurrent commitments to two. Names the problem: per-stage batch size at the planning stage. Proposes the decision: defer Feature Z to Q4 or substitute it for Feature Y; do not stack. The COO's "find the capacity" framing is named as a request for more work in parallel, which the source's batch-size practice cuts against; the alternative — reduce committed items to match empirical per-stage capacity — is the operating-discipline move.

## Anti-patterns This Reference Helps Avoid

- **Utilisation-as-capacity in a board memo.** *Signal:* the memo claims capacity in engineer-hours or headcount; *Diagnosis:* a resource-only reading of the team, where Open Kanban's holistic value asks that people be seen as more than resources; *Follow-up:* reframe in flow vocabulary (per-stage batch size, lead time) — Hurtado's batch-size practice is the citation route.
- **Stacking new commitments without removing existing ones.** *Signal:* compliance, reliability, or strategic-priority work is added without identifying what comes out of the queue; *Diagnosis:* overwork disguised as commitment; *Follow-up:* name the trade explicitly; if nothing comes out, name the overwork — surface this in the memo as the load-bearing claim.
- **"Continuous improvement" without a learning structure.** *Signal:* the org claims continuous improvement but cannot point to the Retrospective, Strategy Meeting, or Kaizen Group that produced the last insight; *Diagnosis:* the framework's position — "Learning is the key concept before continuous improvement can ever happen!" [V] — is being inverted; *Follow-up:* commit to one form, name a cadence, instrument the learning capture.
- **WIP-limit policy as the lever rather than the consequence.** *Signal:* the team adopts per-column WIP limits but item batch size at intake has not changed; *Diagnosis:* the framework's named position is that limiting WIP is downstream of batch-size reduction; *Follow-up:* reduce batch size at intake (simpler stories, fewer epics); the source expects WIP to fall as a consequence, and says either route improves efficiency.
- **Local-stage improvement as the operating-review headline.** *Signal:* an operating review reports a stage-specific improvement (build times halved, code-review SLA cut) without overall lead-time evidence; *Diagnosis:* the local-only improvement Open Kanban's holistic value warns against; *Follow-up:* apply the holistic-systemic test — has the whole system improved, or only the stage?
- **Push-based dispatch dressed as agile process.** *Signal:* engineers are assigned work by a dispatcher rather than pulling from a prioritised backlog; *Diagnosis:* pull-based scheduling has been replaced by push, bypassing the demand-pull the Respect-for-people value enables; *Follow-up:* the prioritisation work belongs upstream of the team; the pull belongs to the team member who will do the work.
- **Multitasking framed as productivity in capacity claims.** *Signal:* capacity is calculated as concurrent items × team size; *Diagnosis:* the framework's named position is that multitasking does not work; *Follow-up:* recalculate capacity as items-finished-per-cycle at each stage; this is the load-bearing number.
- **Speed-vs-quality framing as a binary trade.** *Signal:* the conversation treats speed and quality as opposed, with the proposed resolution being to choose one; *Diagnosis:* Open Kanban does not address the trade-off directly, but its batch-size practice and its warning against exhausting the team offer a third move; *Follow-up:* surface the batch-size lever before accepting the speed-vs-quality framing.
- **Calling Open Kanban canonical-Kanban.** *Signal:* citing Hurtado as the authoritative voice on Kanban in a software-business context where canonical authority is load-bearing; *Diagnosis:* the operator's corpus-role caveat from the deep ref applies — Hurtado is a minor author and Open Kanban is the corpus's only clean-CC Kanban specification, not the canonical work; *Follow-up:* name the caveat in the artefact; look outside this corpus where canonical authority is needed.

## Integration with Other References

- **Jones, *Evidence-Based Software Engineering*:** Jones brings empirical critique of software-engineering claims generally. Hurtado cites Reinertsen as "one of the best explanations" [V] of why focus speeds delivery; Jones is the route to asking what the evidence says. Use Jones when the question is empirical adequacy; use Open Kanban when the question is the framework's stated position on flow.
- **Letaw, *Handbook of Software Engineering Methods*:** Letaw operationalises Agile methods at the practitioner-detail level (planning poker, story points, INVEST, Definition of Done, RACI, Tuckman). Open Kanban supplies the values-and-practices framing; Letaw supplies the methods that fit inside it. Use Letaw for the methods (especially INVEST, which is a quality-check for story-sized items that fits Open Kanban's batch-size practice); use Open Kanban for the value-and-practice frame.
- **OpenStax, *Accounting Vol 2*** (Ch 1.5 Theory of Constraints; Ch 10 relevant-cost analysis): the Theory of Constraints — which Hurtado cites by name as one of two grounding theories for the Holistic / Systemic value — is treated as a five-step optimisation in OpenStax Accounting Vol 2. Use OpenStax for the formal ToC and the relevant-cost analysis that supports build-vs-buy and technical-debt trade-off decisions; use Open Kanban for the whole-system principle it cites the lineage for.
- **OpenStax, *Principles of Management*:** The six organisational structure types (Exhibit 4.6), PDCA, and Mintzberg's managerial roles. Open Kanban's "starts where you are" [V] stance lives inside the existing management structure that Principles of Management describes; PDCA at the management level maps onto Open Kanban's *Learn and improve continuously* practice at the team level. Use both layers together for a complete management-team discipline picture.
- **Schwaber & Sutherland, *The Scrum Guide* (2020):** Scrum and Open Kanban are alternatives, not opposites. Use Scrum when the work can be organised into Sprint-Goal-anchored cycles; use Open Kanban when the team wants a values-and-practices kernel with no prescribed cadence. Hurtado explicitly cites the VersionOne 2013 State of Agile finding that Kanban is "frequently used as an alternative to Scrum." [V] Both frameworks share the continuous-improvement structure (Open Kanban's *Learn and improve continuously* ≈ Scrum's *Sprint Retrospective*) and the transparency-via-visualisation discipline.
- **Approach Perfect, *Field Guide to Scrum Events*:** the capacity-adjusted-velocity formula and Sprint-Goal facilitation depth that Open Kanban does not supply. Use the Field Guide when the team is running Sprint-anchored cadence and Sprint Goals; use Open Kanban when the team is not working to Sprints.
- **Open Practice Library:** Foundation, Discovery, Options, Delivery phase practices. Open Kanban's under-prescribed learning practice can be filled with Open Practice Library practices (blameless postmortems, retros, etc.). Use Open Practice Library for the catalogue of practices; use Open Kanban for the values-and-practices framing that disciplines which practices fit.
- **NHS *A Just Culture Guide*:** Open Kanban's Courage value names the upward-correction mechanism; NHS Just Culture steers managers away from singling out the staff member involved in an incident. Use both when designing the conditions under which the team can surface issues before they become incidents.
- **US Army, *TC 25-20 After-Action Reviews*:** Open Kanban names Retrospectives as one candidate continuous-improvement form; TC 25-20 is the canonical primary source for the AAR methodology when the chosen form is a structured retrospective.
- **US Forest Service, *LFUO Implementation Guide* (2024):** LFUO's Systems Thinking and Learning principles parallel Open Kanban's Holistic / Systemic value and Learning practice. Use LFUO for the operationalised learning-from-events methodology (AAR → RLS → FLA → Learning Review); use Open Kanban for the team-level operating discipline that produces the conditions under which learning is the default.

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** Open Kanban's framework claims rest on several sources this corpus does not hold as primary references.

- *Donald G. Reinertsen, Principles of Product Development Flow* — cited as "one of the best explanations" [V] of why batch-size reduction improves flow (Source: Hurtado, "Open Kanban Practices" — Reduce the Batch Size). The deep ref flags this as [BT]. The quantitative apparatus (cost-of-delay, weighted-shortest-job-first, queue-drain formulas) is not reproduced in Open Kanban and is not available in this corpus.
- *Deming, System of Profound Knowledge* — cited by name as one of two grounding theories for the Holistic/Systemic value (Source: Hurtado, "Open Kanban Values" — Holistic or Systemic Approach to Change). Flagged [BT] in the deep ref. PDCA is the corpus's closest Deming treatment (via OpenStax *Principles of Management*); the full Profound Knowledge framework is outside the corpus.
- *Goldratt, Theory of Constraints* — cited alongside Deming for the Holistic/Systemic value. Flagged [BT]; the formal five-step ToC treatment is in OpenStax *Accounting Vol 2*, not in Open Kanban.
- *Alistair Cockburn, information radiators* — cited by name for the Visualize-the-workflow practice. Flagged [BT]; Cockburn is not a primary reference in this corpus.
- *VersionOne 2013 State of Agile* — cited as empirical support for Kanban adoption rates. Flagged [BT]; the primary data is not in this corpus.
- *Lean / Muri / Toyota Production System* — cited for the sustainable-pace pairing (Muri) and the waste gloss (Muda). Flagged [BT]; no Toyota Production System primary reference is in this corpus.

**Named limits of the source.** Hurtado explicitly marks Open Kanban as "not a full or complete Agile or Lean method" [V] — it is described as "the heart of that method" [V] and compared to "the kernel of an open source operating system" [V] (Source: Hurtado, "Open Kanban Definition"). Operator-facing scope limits follow from this:

- Quantitative flow metrics (cumulative flow diagrams, lead-time histograms, throughput run charts, Little's Law) are not in scope; the source is conceptual on flow, not quantitative.
- Kanban service classes (standard / expedite / fixed-date / intangible) are not addressed in Open Kanban.
- The authoritativeness caveat (operator note) is stated in the distillation header: Hurtado is a minor author by broader industry-recognition standards; other widely recognised Kanban primary sources are outside this corpus.
- AI-native work is not addressed; the kernel-plus-extensions architecture supports extension to AI ops, but the extension is a distillation-level inference, not a source claim.

**Evidence-marker continuity.** All verbatim quotations in the Key Concepts and Worked Example sections are carried from the deep ref with [V] markers intact. Normative framework claims stated as the source's position (batch-size reduction as the primary lever; multitasking does not work) are paraphrases of [V]-marked content and are labelled with (Source: ...) citations throughout. The Reinertsen, Deming, Goldratt, and Cockburn citations are [BT] in the deep ref and are identified as such here. No [V]-marked content has been restated as the distillation's own analytical claim without attribution.

## Through the CTO lens

Open Kanban's signature contrarian move — "Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around... Open Kanban does not ask you to limit WIP" [V] (Source: Hurtado, "Open Kanban Practices" — Reduce the Batch Size) — is exactly the constraint-as-operational-mechanism discipline the CTO archetype reaches for. The framework refuses to name WIP-limiting as the lever; it names per-stage batch-size reduction as the lever; through the CTO lens, the owner is the team at each stage and the board is the gate.

When the lens reads a roadmap or capacity memo through Open Kanban:

- The constraint the CTO would name: batch size at each stage of the SDLC. One sentence, operational, with owner (the team at each stage) and gap (item complexity or quantity).
- The mechanism the artefact must supply: smaller items at intake; visible per-stage status on a board or information radiator; a learning structure (Retrospective / Strategy Meeting / Kaizen Group) that produces decisions about the next dial.
- The AI-native angle (a distillation-level inference): AI integration work can go through the same per-stage batch discipline. Open Kanban's kernel-plus-extensions shape lets the operator extend the framework to AI work (prompt-engineering as a stage; model evaluation as a stage) without re-deriving the values. The framework's Cockburn-derived information-radiator framing applies to AI ops dashboards.
- The decision implicit: assign an owner for batch-size discipline at each stage; fund the learning structure; approve a deferral of stacked commitments that push the team past a sustainable pace.

The lens reads pure-WIP-limit policy proposals as past-tempo framings — they treat WIP-limiting as the lever, which the framework names as the consequence. The lens reframes them: the batch-size dial at intake is the operational mechanism; WIP-limit telemetry is the gate that verifies the dial is doing the work.

## Through the business-executive-stakeholder lens

Open Kanban's batch-size-first framing is structurally a Paradigm-B move. Inside an A-shaped envelope, this is one B-move per artefact — and through this lens, the artefact supplies the A-shaped substrate the framework leaves open: a per-stage batch-size number, a named owner, a timeboxed first step, and measurable success criteria.

When the lens reads a capacity-planning conversation through Open Kanban:

- The Paradigm-A reading the stakeholder will perform: the conversation must produce a commitment, an owner, a deadline, a KPI. Capacity stated in engineer-hours or headcount lands; capacity stated in batch-size-per-stage lands only if the framework's B-move is named explicitly as a choice.
- The B-vocabulary the artefact can echo: *sustainable pace*, *system not people*, *less firefighting*. The stakeholder uses this vocabulary in low-heat moments; the framework's *Muri* / sustainable-pace pairing maps onto it directly.
- The Paradigm-A items the artefact must supply: named accountable owner for batch-size discipline at each stage; a measurable KPI (per-stage lead time, items finished per cycle); a timeboxed first step (one cycle of reduced intake); a decision being requested (approve the trade — Z deferred for X and Y to land at sustainable pace).
- The one B-move: name the framing — "capacity is per-stage batch size, not engineer-hours" — explicitly, as a structural reframe the stakeholder can take or leave. Do not stack additional B-moves (system-thinking, root-cause-as-systemic, hypothesis-not-commitment) onto the same artefact. The B-move lives inside an A-shaped envelope: A-vocabulary opening, A-vocabulary substance, one B-reframe surfaced as a choice, A-vocabulary close.

The lens reads pure-Paradigm-B framings (root cause as systemic; team is over-stretched; we need slack) as sermon-shaped; the lens's move is to supply the A-substrate (the batch-size number, the per-stage owner, the cycle-length first step) that makes the B-reframe operationally legible.

## Related concepts

- [Letaw, Handbook of Software Engineering Methods](letaw-handbook-sweng-methods.md) — shared: Agile, Software Development
- [Open Practice Library](open-practice-library.md) — shared: Agile, Open Source
- [OpenStax Organizational Behavior](openstax-organizational-behavior.md) — shared: Collaboration, Values
- [OpenStax Principles of Management](openstax-principles-management.md) — shared: Collaboration, Values
- [Krivitsky, Larman & Flemm, Org Topologies Primer](org-topologies-primer-2025.md) — shared: Flow, Systems Thinking
- [Gagné, The Approach Perfect Field Guide to Scrum Events](approach-perfect-field-guide-scrum-events.md) — shared: Agile
- [Barbrook-Johnson & Penn, Systems Mapping](barbrook-johnson-systems-mapping.md) — shared: Systems Thinking
- [Jones, Evidence-based Software Engineering](jones-evidence-based-sweng.md) — shared: Software Development
- [LFUO 2024](lfuo-learning-review-guide-2024.md) — shared: Systems Thinking
- [NHS Just Culture Guide](nhs-just-culture-guide.md) — shared: Systems Thinking
- [Schwaber & Sutherland, The Scrum Guide](scrum-guide-2020.md) — shared: Lean
- [SSDL, Systems Thinking Foundations](ssdl-systems-thinking-foundations.md) — shared: Systems Thinking
