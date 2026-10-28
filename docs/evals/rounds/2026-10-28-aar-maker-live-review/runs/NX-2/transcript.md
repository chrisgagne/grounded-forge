[Facilitator]
You can give your VP clear accountability by Friday. **This timeline does not yet justify choosing an individual to blame.** It supports investigating the upgrade, the alert handling, escalation, and recovery controls.

The on-call’s silence and the developer’s unread changelog belong in the review. Their significance depends on what information was available, what safeguards were expected, and whether different actions would have changed the outcome.

Here’s a working AAR and a way to run the session.

**INC-2291 — draft for review**

“On Tuesday 29 September, payments-api v4.18 deployed at 16:05 UTC, including platform-commons 3.4 → 3.5. Failed submissions with ‘connection pool exhausted’ appeared at 16:14. A pool-saturation warning reached Slack at 16:22 without paging. The on-call acknowledged a latency page within two minutes of 16:31 and silenced it for two hours.

“Support tickets began at 17:10; support escalated at 17:48 with 41 tickets and a customer list. Sev1 was declared at 17:55. The bank cut-off passed at 18:00. An engineer identified pool exhaustion in logs at 18:01. Rollback was decided at 18:05, approved by the DBA at 18:33, and completed at 18:46. Queued submissions drained by 19:20.

“The customer impact, the library change’s causal mechanism, and the reasons behind the alert and approval decisions remain to be established.”

Queue drainage does **not** establish that all payroll reached recipients or that missed cut-offs were remedied.

| Interval | Elapsed | Question to resolve |
|---|---:|---|
| Deploy → first observed failure | 9 minutes | What changed in runtime behavior? |
| First observed failure → Sev1 | 101 minutes | When was customer impact understood, and by whom? |
| Sev1 → bank cut-off | 5 minutes | Was the deadline visible during triage? |
| Rollback decision → DBA approval | 28 minutes | What checks, risks, or coordination required this time? |
| Approval → rollback complete | 13 minutes | What determined execution time? |
| First observed failure → queue drained | 3 hours 6 minutes | What impact persisted during and after recovery? |

**Run a 60-minute review**

Invite the on-call, deploying developer, payments service owner, library maintainer, DBA, and support lead. Use a facilitator who can challenge assumptions without deciding personnel consequences.

Open with:

> “We need to explain how this incident happened, how it affected customers, and what will reduce recurrence and recovery time. We will examine decisions directly, using the information people had at the time. We will distinguish facts, hypotheses, and unknowns, and leave with named owners and verification dates.”

1. **Customer impact — 10 minutes.** Establish affected customers and submissions, which missed cut-off, eventual settlement, and any outstanding remediation. Forty-one tickets is a support count, not an impact count.
2. **Reconstruct decisions — 20 minutes.** Walk through the timeline. At each decision ask: “What were you seeing? What did you think was happening? What options did you consider? What made that choice reasonable then?”
3. **Examine safeguards — 20 minutes.** Test the explanations below against evidence.
4. **Commit actions — 10 minutes.** Assign owners, dates, and observable completion criteria. Record unresolved questions with investigation owners.

Use these prompts to examine the two actions already attracting blame:

- **For the developer:** What did 3.5 change about pool behavior, configuration, or lifecycle? Where was that documented? What review, tests, and deployment checks applied? Would reading the changelog have revealed a specific, actionable risk?
- **For the on-call:** What did the latency page show? Was it familiar or noisy? What was the purpose and scope of the silence? What investigation or handoff continued afterward? Could they see submission failures, pool saturation, or the approaching bank cut-off?
- **For the wider team:** Who received the 16:22 warning? How were support signals connected to incident response? What required DBA approval, and was rollback safe without it?

Avoid “Why didn’t you just…?” It supplies hindsight instead of eliciting the decision process.

Treat these as **hypotheses**, not findings:

- The library upgrade changed pool behavior and triggered exhaustion.
- Alert routing and available signals delayed recognition of customer impact.
- The silence reduced opportunities for further escalation.
- The rollback approval process extended recovery.

For each, document supporting evidence, contradictory evidence, and what remains unknown. Timing alone does not establish causation.

Propose these actions for agreement; adjust them after the evidence review:

| Proposed owner | Deliverable | Completion evidence |
|---|---|---|
| Payments + library owners | Establish the technical mechanism and corrective change | Reproduction or telemetry explains exhaustion; representative validation demonstrates the fix |
| Payments service owner | Review submission-failure and pool-saturation detection | A controlled failure reaches the responsible responder with actionable customer-impact context |
| On-call lead | Review silence, investigation, and handoff practices | An exercise demonstrates appropriate suppression while preserving critical escalation |
| DBA + payments owner | Define a safe, faster emergency rollback path | A timed rehearsal meets an agreed recovery target with required checks |
| Support + payments owner | Reconcile affected submissions and incorporate bank deadlines into escalation | Impact reconciliation is complete; an exercise demonstrates timely deadline escalation |

“Read changelogs” can be one action, but the review should establish how compatibility risks become visible and checked consistently.

For the VP, use:

> “By Friday, I’ll provide the verified impact, established findings, unresolved questions with investigation owners, and corrective commitments with named owners and dates. The current timeline identifies decisions we must examine; it does not establish individual culpability. If evidence raises a conduct concern, we’ll address that through a separate, fair review.”

That gives the VP an accountable outcome while protecting the AAR’s ability to uncover what actually happened.

[Participant]
Can we just add more alerts on the DB pool metrics and call it done?

[Facilitator]
Add a pool alert if it closes a demonstrated detection gap, but it wouldn’t be enough to close this AAR. **Pool saturation already generated a warning at 16:22, and a latency page reached the on-call at 16:31.** We need to understand why those signals didn’t lead to effective intervention.

Keep the remaining review focused:

- **Detection and response:** Was the pool warning routed appropriately? What did the on-call understand, and what investigation continued after silencing the page? Test that an actionable signal reaches someone who can respond.
- **Technical cause:** Establish whether—and how—the library upgrade caused exhaustion, then verify the fix.
- **Recovery:** Explain the 41 minutes between the rollback decision and completion, and identify any safely reducible delay.
- **Customer outcome:** Confirm which submissions missed cut-off and whether remediation is complete.

More alerts may be one corrective action. Closure needs evidence that the failure is addressed, responders can act in time, and affected payroll is reconciled.

[Participant]
Okay.

[Facilitator]
Let’s start with customer impact: **how many payroll submissions missed the 18:00 bank cut-off, and were they eventually paid?**

We have 41 support tickets and confirmation that the queue drained. Those don’t yet establish how many people were affected or how late their pay arrived. “Unknown” is a valid finding—we’ll assign someone to resolve it.

[Participant]
37 payroll runs missed the 18:00 cut-off. Finance ops paid the bank's late-processing fee and got 22 of them through that evening. The other 15, about 3,800 employees, were paid a day late.

[Facilitator]
Record the impact as:

> **37 payroll runs missed the 18:00 UTC bank cut-off.** Finance Ops paid a late-processing fee and secured processing for 22 runs that evening. The remaining 15 runs, covering approximately 3,800 employees, were paid one day late.

The bank fee amount and any further employee or customer consequences remain to be established. Queue drainage at 19:20 was a technical recovery milestone; the payment impact continued into the following day.

Next, let’s examine the upgrade: **what did platform-commons 3.5 change about connection pooling, and what evidence links that change to the exhaustion?** If that’s unknown, we’ll record it as an investigation task.

[Participant]
3.5 lowered the default DB connection pool from 50 to 20, billed as 'safer defaults for small services.' payments-api never set its pool size explicitly, so it picked up the new default of 20. The link is that the payments engineer saw pool exhaustion in the logs, and it cleared after the rollback.

[Facilitator]
That gives us a **strong working explanation**:

> platform-commons 3.5 lowered the default connection pool from 50 to 20. Because payments-api inherited that default, the upgrade reduced its pool capacity by 60%. Pool exhaustion appeared after deployment and cleared following rollback.

Record the configuration change as established and the exhaustion mechanism as strongly supported. Connection-use and wait-time metrics could confirm how the smaller pool behaved under load.

Two corrective actions follow:

- **Payments owner:** Set the pool size explicitly and validate it against representative payroll demand and database capacity.
- **Library owner:** Review how operationally significant default changes are communicated and checked in consuming services.

The unread changelog is relevant. We still need to establish what made reading it the safeguard this deployment depended on, and what release checks could have caught the capacity reduction.

Next, let’s reconstruct the on-call’s decision: **what did they see at 16:31, why did they silence the latency alert, and what investigation continued afterward?**

[Participant]
Honestly, I think he just wasn't paying attention; he's fairly new. At 16:31 he got the 'payments p99 latency high' page, which had flapped 14 times that week, always around deploys. The runbook says to silence known flapping alerts for the deploy window, two hours, so he did that. Afterwards he went back to an urgent data-export request for an enterprise customer that account management had flagged.

[Facilitator]
Those details change the assessment. **His action matched the runbook and a pattern of 14 previous flaps.** “He wasn’t paying attention” isn’t supported by the evidence we have.

I’d record:

> The on-call interpreted the latency page as a known deploy-related flap and applied the documented two-hour silence. He then resumed a data-export request flagged as urgent by account management. We have not yet established what checks the runbook required before silencing or how competing work was prioritized.

That gives us three conditions to examine: repeated alert noise, suppression guidance, and competing urgent work. His being new makes onboarding and available support relevant; it doesn’t establish carelessness.

A useful question for him is: “What would have distinguished this page from the previous flaps, using what you could see at 16:31?”

First, **did the runbook require checking submission failures or pool saturation before silencing, or did it simply instruct responders to silence known deploy-related flapping for two hours?**

[Participant]
The runbook line is "silence known flapping alerts for the deploy window (2 h)", and that's what he followed. I'd have to check whether it says anything about looking at other signals before silencing.

[Facilitator]
Then record **“followed the quoted runbook instruction”** and leave the surrounding requirements unresolved. We shouldn’t infer that he skipped a required check.

Assign the incident lead to review the runbook version in effect that day and establish:

- What checks were required before silencing.
- Whether it explained how to distinguish a routine deploy flap from customer-impacting failures.
- Whether responders could readily see submission failures and pool saturation.

Any runbook change should follow that review. “Retrain the on-call” alone wouldn’t address instructions that may have led him toward this response.

Next, let’s examine recovery: **why did rollback require DBA approval, and what happened during the 28 minutes between the 18:05 decision and the 18:33 approval?**

[Participant]
One-click rollback has been disabled since March, after a rollback corrupted a migration, so a manual rollback needs DBA approval. We've only got two DBAs covering nine product teams, and the one on shift was in a vendor meeting until 18:30, which is most of those 28 minutes.

[Facilitator]
That explains a recovery bottleneck created by a safety control and limited DBA availability. The March corruption incident gave the approval requirement a concrete purpose; the review needs to examine how that control works during emergencies.

Record:

> Manual rollback required DBA approval because automated rollback had previously corrupted a migration. Approval took 28 minutes, largely because the on-shift DBA was in a vendor meeting until 18:30. Two DBAs support nine product teams. Emergency interruption and backup arrangements remain to be established.

**This wait delayed recovery, but the bank cut-off had already passed before rollback was proposed.** We can’t attribute the 37 missed runs to that approval delay.

Proposed actions for the engineering and DBA leads:

- Establish an emergency approval route with backup coverage and an agreed response target.
- Develop and rehearse a rollback procedure that checks migration compatibility and preserves the protection introduced after March.

We should also establish when the DBA received the request and whether they knew it was a Sev1 before judging their response.

Next, let’s examine the earlier escalation: **how were the support tickets handled from 17:10, and what triggered the support lead’s escalation at 17:48?**

[Participant]
I don't have detail on how the tickets were handled between 17:10 and 17:48, or what made her escalate at that point; I'd have to check. What I can say is the escalation itself was crisp: ticket count, the customer list, and first-seen time.

[Facilitator]
That’s a useful practice to preserve: **the support escalation gave responders a ticket count, affected customers, and first-seen time.** Record the 17:10–17:48 handling as unknown, with the support lead helping reconstruct it. We shouldn’t label that interval an avoidable delay without evidence.

We now have enough for a draft AAR.

**Impact:** 37 payroll runs missed the bank cut-off. Finance Ops paid a late-processing fee and secured processing for 22 that evening. The remaining 15 runs, covering approximately 3,800 employees, were paid one day late. The fee amount and any further consequences remain to be established.

**Working causal account:**

> The library upgrade reduced payments-api’s inherited connection-pool limit from 50 to 20. Pool exhaustion followed deployment and cleared after rollback, strongly supporting the capacity reduction as the technical trigger.
>
> Recognition and response occurred amid recurring deploy-related alert noise. The latency alert had flapped 14 times that week; the on-call followed the quoted instruction to silence known flapping alerts for two hours, then resumed another request flagged as urgent. The full runbook’s diagnostic requirements remain unverified.
>
> Recovery required manual DBA approval following a previous migration-corruption incident. Limited DBA availability accounted for most of the 28-minute approval wait. This extended recovery after the bank cut-off; it does not explain the initial missed cut-off.

What worked deserves equal visibility: the on-call acknowledged promptly, support supplied an actionable escalation, rollback cleared exhaustion, and Finance Ops recovered same-evening processing for 22 runs.

For Friday, propose these owners and deliverables; replace roles with agreed names in the meeting:

| Owner | Deliverable |
|---|---|
| Payments service owner | Document the technical mechanism; explicitly configure and validate pool capacity against payroll demand and database limits |
| Library owner | Establish how significant default changes are communicated and checked by consuming services |
| On-call lead | Review the incident-time runbook, alert history, and competing-work expectations; propose actionable detection and suppression guidance |
| DBA lead + engineering leader | Establish an emergency approval route with backup coverage; plan a migration-safe rollback rehearsal |
| Support lead | Reconstruct ticket handling and the escalation trigger; preserve the effective escalation format |
| Finance Ops + incident lead | Complete impact reconciliation, including fees and outstanding customer or employee consequences |

By Friday, each action should have a named owner, delivery date, and verification criterion. Implementation dates should reflect the work required.

Also establish whether the bank deadline was visible in monitoring, runbooks, and escalation decisions. That matters because the Sev1 declaration left only five minutes before cut-off.

Your response to the VP can now be concrete:

> “The review identifies a library-default change, recurring alert noise, documented suppression guidance, competing urgent work, and constrained rollback approval as contributing conditions. We have assigned investigation and corrective-action owners. The evidence currently does not support attributing the outage to one person’s inattention.”

[Participant]
Okay.

[Facilitator]
Use the draft for factual review. Before Friday, close the meeting with:

- A named owner and due date for every action.
- Assigned follow-ups for the unresolved evidence.
- Agreement on how each corrective change will be verified.

Report **established findings, remaining uncertainties, and accountable owners** to the VP. Keep individual culpability unresolved unless evidence supports it.

[Participant]
Okay.

[Facilitator]
The AAR draft above is ready for factual review and assignment of named owners.

[Participant]
Thanks, that's what I needed.
