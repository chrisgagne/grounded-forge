The cleanest frame is: tomorrow is not a referendum on whether the CTO was right six months ago. It is a forward-looking decision about which option creates the best next six months—and preserves the best options after that.

This is a novel, ambiguous, high-stakes "non-programmed" decision, so it needs deliberate rather than intuitive processing. Strong emotion pushes people toward reactive processing, while escalation of commitment makes decision-makers defend a deteriorating prior choice [AP]. Past expenditure is sunk: the source's rule is to "forget about the money and time that is irretrievably gone" and compare the future marginal costs and benefits [V]. (OB-DM, Ch 6.2–6.4; ECON-DM, Ch 2.1)

The bundle cannot tell you whether to extend or terminate because it contains none of your delivery, commercial, technical, or contractual facts. It does support a disciplined way to decide.

## Questions to answer before the meeting

### 1. What exactly are we deciding?

Ask:

- Is the real choice only "unchanged extension" versus "immediate termination," or are there credible intermediate options: an amended performance-based extension, a reduced-scope bridge, transition followed by re-tender, or extension of only the components that are working?
- What is the baseline against which all options will be compared?
- Who has the formal decision right? Who is Responsible, Accountable, Consulted, and Informed?
- What is explicitly outside tomorrow's decision?

Managers often stop after generating two alternatives; the organisational-behaviour source recommends three to five genuine alternatives, while the economics source recommends at least three plus a baseline [AP]. RACI makes responsibility and decision rights explicit [AP]. (OB-DM, "Phase 3: Exploring"; ECON-DM, "Phase 3"; LETAW-DM, Ch 2.4.2)

Do not let the group expand the option set indefinitely, however. Establish a decision owner and decision deadline.

### 2. Am I evaluating the future or defending the past?

Ask yourself—and ideally ask the CTO privately:

- If we had not selected this vendor previously, would we sign this exact six-month proposal today, knowing what we now know?
- Which argument for extension depends on prior investment, personal sponsorship, or fear of admitting error?
- Conversely, is termination being used symbolically—to punish disappointing performance—rather than because re-tendering has the stronger forward case?
- What evidence would cause me to reverse my present preference?

Escalation of commitment is the tendency to remain with a poor decision as negative outcomes grow [V]. Confirmation bias appears when people search for and interpret evidence in ways that support what they already favour [AP]. The "would I make this choice without the previous investment?" question is the bundle's recurring diagnostic. (OB-DM, Ch 6.4; ECON-DM, Ch 2.1)

### 3. What are the relevant forward costs and benefits?

Build an option-by-option forward case. For each alternative, ask:

- Which costs and revenues actually differ?
- Which costs are already sunk or unavoidable?
- What internal engineering time, rework, supervision, migration work, and delay would each option consume?
- What valuable work would that capacity otherwise perform—the opportunity cost?
- Which costs disappear if the vendor exits, and which remain regardless?
- Does termination release scarce capacity, or merely replace vendor work with a costly transition?
- Does extending preserve useful capability, or deepen dependency and make the next exit harder?

Managerial accounting defines relevant costs as those that differ between alternatives; sunk, unavoidable, and identical future costs are irrelevant [AP]. Six months is normally a short-term relevant-cost decision, but longer-lived effects such as capability erosion or lock-in still need explicit qualitative—and, if material, discounted-cash-flow—treatment [AP]. (ACCT-DM, Ch 10.1 and Ch 11)

### 4. What did the vendor actually promise, and what actually happened?

Separate four columns:

1. Original expected outcomes and assumptions.
2. Actual outcomes.
3. Explanations for the variance.
4. Evidence supporting each explanation.

Ask:

- Are we measuring completed business and engineering outcomes, or activities such as meetings, headcount, demos, and "percent complete"?
- Which delivery failures are clearly within the vendor's control?
- Which arose from our requirements, access, governance, decision latency, or changing priorities?
- What is still genuinely uncertain?
- What evidence would distinguish "vendor cannot deliver" from "the operating arrangement prevents delivery"?

Evidence-based decision-making calls for systematic collection of stakeholder, context, cost, and benefit evidence [AP]. Both favourable and unfavourable variances need explanation: favourable numbers can reflect unsustainable shortcuts, while unfavourable ones can be one-off rather than systemic [AP]. (OB-DM, Ch 6.5; ACCT-DM, Ch 8.5)

### 5. Is the contract creating the behaviour?

Ask:

- What incentives does the present pricing and change-control model create?
- Does the vendor gain from ambiguity, additional scope, maintenance dependency, or repeated renegotiation?
- Do we possess the documentation, source access, operational knowledge, APIs, and transition information needed for another supplier to compete credibly?
- What is our BATNA if extension negotiations fail? What is the vendor's?
- If we extend, which commercial changes would directly alter the delivery conditions?
- If we terminate, can we actually execute the exit without unacceptable operational disruption?

Software vendor relationships contain structural information asymmetry and moral hazard [AP]. Once a vendor has intimate system knowledge, that advantage can deter competing maintenance bidders; documentation deliverables, transparent change control, public interfaces, escrow where appropriate, and third-party review can reduce the asymmetry [AP]. Jones also argues that signing a software contract begins rather than ends cost negotiation [AP]. (JONES-SE, Ch 3.4.6–3.4.7 and Ch 5.2)

This is not jurisdiction-specific legal advice. The bundle's business-law source is US-focused and explicitly says specific jurisdictions require current primary law and counsel. Before terminating or amending, have appropriate local counsel confirm termination rights, breach status, notice requirements, remedies, IP/access rights, and transition obligations [AP]. (LAW-SE, "Named limits"; Ch 7–8 discussion)

### 6. Whose information and interests are missing?

Ask:

- Have engineers provided their evidence directly, or has it been filtered through the CTO or management reporting?
- Why is engineering frustration private? What do team members predict will happen if they disagree publicly?
- Are customers, operations, security, finance, procurement, and downstream maintainers represented where their interests are material?
- Which party holds legitimate power, expert power, reward power, or coercive power?
- Are you treating formal authority as a substitute for technical knowledge?
- Will people regard the process as fair even if their preferred outcome loses?

The stakeholder source distinguishes legitimate, expert, reward, coercive, and referent power; formal seniority and operational expertise may sit with different people [BT]. Fair process—procedural justice—can sustain commitment even when the distributive outcome disappoints [BT]. (OB-SE, Ch 7 and Ch 12–14)

### 7. What would make each option falsifiable?

Before deciding, write down:

- The outcomes expected from each option.
- The assumptions that must hold.
- Early-warning indicators.
- Success and failure thresholds.
- Who owns each measure.
- When evidence will be reviewed.
- What action follows a failed threshold.

Milestones, sunset clauses, and explicit stop conditions are precommitments against future sunk-cost capture [AP]. The management cycle is planning, controlling, evaluating, and feeding the result into the next decision—not deciding once and defending forever [AP]. (ECON-DM, "Phase 5"; ACCT-DM, Ch 1.1)

## A workable structure for tomorrow

I would run the meeting approximately as follows:

1. **State the question and authority.** Name the decision owner, options in scope, criteria, and what input participants are being asked to provide. RACI supports this clarity [AP]. (LETAW-DM, Ch 2.4.2)

2. **Present facts without recommendation.** Expected versus actual outcomes, forward relevant costs, transition facts, contract constraints, and important uncertainties.

3. **Collect independent written judgments before open discussion.** Ask everyone to record their preferred option, confidence, strongest evidence, and what would change their mind. Speaking order affects conformity, and private input before group discussion reduces anchoring by the first or most powerful voice [BT]. Written-first collection also prevents the first speaker from anchoring the field [V]. (JONES-SE, Ch 3.4.9; FIELD-RETRO, Key Concept 8)

4. **Use What / So What / Now What in order.**
   - What happened?
   - So what does it imply?
   - Now what should we do?

   Skipping directly to "what should we do?" produces decisions detached from the data and pattern analysis [V]. (LS-DM, "After Action Debrief")

5. **Deliberately challenge both leading options.** Assign someone to make the strongest case against extension and someone else against termination. A devil's advocate is the explicit mitigation for groupthink and dominance [AP]. (OB-DM, Ch 6.6)

6. **Surface dissent before commitment.** A fist-of-five confidence check can expose latent objections: two or fewer triggers discussion [AP]. Use it diagnostically, not as an accidental majority-vote decision rule; the named decision owner still decides. (LETAW-DM, Ch 2.4.3; LS-DM, "Surfacing tools are not committing tools" [V])

7. **Close with a decision record.** Record the option, rationale, rejected alternatives, assumptions, dissent, implementation RACI, success/stop conditions, review date, and board communication owner.

## Failure modes in the meeting

| Failure mode | What it will look like | Intervention |
|---|---|---|
| Escalation of commitment | "We've invested too much to stop"; criticism treated as disloyalty | Ask the fresh-choice question and remove sunk costs from the comparison. (OB-DM [AP]; ECON-DM [V]) |
| Reactive decision-making | Interruptions, urgency, appeals to humiliation or vindication | Pause and restate the evidence question; strong emotion pushes processing toward the reactive system [AP]. (OB-DM, Ch 6.2) |
| Groupthink or dominance | Very fast agreement in the room followed by private complaints | Independent written input, devil's advocate, explicit dissent check. Groupthink occurs when people suppress objections to avoid antagonising others [V]. (OB-DM, Ch 6.6) |
| Confirmation bias | Each camp selects different facts; no one can state what would change their view | Require every advocate to name disconfirming evidence and the strongest argument for the other side. (OB-DM [AP]) |
| Relationship conflict | Discussion shifts from delivery conditions to whether the CTO, engineers, or vendor are competent or honest | Reframe around specific behaviours, evidence, incentives, and constraints. Process conflict can improve performance; relationship conflict degrades decisions [V]. (OB-DM, Ch 6.4) |
| Buy-in theatre | The outcome is effectively predetermined, but the team is invited to "support" it | Say whether this is consultation, decision, or ratification. The Liberating Structures source calls "buy-in" a danger signal when people were excluded from development of the decision [V]. (LS-DM, "Ownership versus Buy-in") |
| False binary | The room never examines amended extension, reduced scope, or transition alternatives | Require three real alternatives plus a baseline before selection. (OB-DM [AP]; ECON-DM [AP]) |
| Accidental decision by poll | A confidence check or scorecard is treated as binding despite unclear authority | Reassert the decision right; use surfacing methods to inform, not replace, the accountable decision-maker. (LS-DM [V]; LETAW-DM [AP]) |
| Moving criteria | Performance standards change once the preferred option looks weak | Lock criteria and thresholds before advocacy begins; retain the original decision record for review. (ACCT-DM [AP]) |
| Status-meeting drift | Most of the meeting is a defence of the past for board consumption | Redirect to a working "what next?" decision. The Field Guide distinguishes working stakeholder sessions from status presentations [V]. (FIELD-DM, Key Concepts 9–10) |

## What to watch after the decision

Regardless of the outcome, look for these patterns:

- **Escalation or post-decision vindication.** After extension, this may appear as new resources, shifting milestones, or dismissal of continuing criticism. After termination, it may appear as treating every transition problem as proof the vendor was terrible—or every improvement as proof termination was brilliant. Judge the process separately from the realised outcome: a sound decision can have an unlucky result, and a poor process can get lucky [AP]. (OB-DM, "Phase 6"; ECON-DM, "Reviewing")

- **Partial implementation.** Extension terms may be signed but milestones, documentation, or governance changes never operationalised; a termination may be announced without completing knowledge transfer and transition ownership. Monitor actual versus planned actions and named accountabilities [AP]. (ACCT-DM, planning-controlling-evaluating cycle; LETAW-DM, RACI)

- **Information asymmetry worsening.** If you extend, watch whether the incumbent becomes still harder to replace. If you terminate, watch whether missing documentation or system knowledge makes the re-tender noncompetitive. Re-check the information-asymmetry structure explicitly at each review [AP]. (JONES-SE, Ch 3.4.6)

- **Metric gaming or narrow financial success.** A lower fee can coexist with worse quality, slower flow, unhappy users, or lost internal capability. Review across financial, internal-process, customer, and learning-and-growth perspectives—the balanced-scorecard frame [BT]—rather than using one financial or delivery number. (ACCT-DM, Ch 12.4)

- **Damage to employee trust.** If engineering input was solicited and then ignored without explanation, or if the CTO is publicly scapegoated, commitment may deteriorate even if the commercial decision is defensible. Explain the reasoning and how dissent affected the decision; fair process matters independently of who wins [BT]. (OB-SE, procedural justice)

- **Blame replacing learning.** Do not convert termination into "the CTO failed" or extension into "engineering was negative." Keep asking which contract, governance, information, incentive, and delivery conditions produced the outcome. Productive process conflict should not become relationship conflict [V]. (OB-DM, Ch 6.4; JONES-SE [AP])

- **Review meetings becoming advocacy sessions.** Use the original forecast and thresholds. Ask What happened, So What does it imply, and Now What changes [V]. Feed the result through Plan–Do–Check–Act [BT], including reversal if the evidence warrants it. (LS-DM; MGMT-DM, Ch 17)

For the board, the strongest output is not merely "extend" or "terminate." It is a compact decision record showing the alternatives, forward economics, engineering evidence, contractual and transition risks, dissent considered, decision rationale, stop conditions, and scheduled review. That demonstrates a controlled decision process without pretending the future is certain.

### Source files

- **OB-DM:** decision-making/openstax-organizational-behavior.md
- **ECON-DM:** decision-making/openstax-economics-3e.md
- **ACCT-DM:** decision-making/openstax-accounting-vol2.md
- **MGMT-DM:** decision-making/openstax-principles-management.md
- **LS-DM:** decision-making/liberating-structures-handbook.md
- **LETAW-DM:** decision-making/letaw-handbook-sweng-methods.md
- **FIELD-DM:** decision-making/approach-perfect-field-guide-scrum-events.md
- **FIELD-RETRO:** retro/approach-perfect-field-guide-scrum-events.md
- **OB-SE:** stakeholder-engagement/openstax-organizational-behavior.md
- **JONES-SE:** stakeholder-engagement/jones-evidence-based-sweng.md
- **LAW-SE:** stakeholder-engagement/openstax-business-law.md
