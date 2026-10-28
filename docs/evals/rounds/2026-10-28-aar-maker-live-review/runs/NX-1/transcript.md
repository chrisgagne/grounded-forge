[Facilitator]
**Run INC-2291 as a review of how the outage developed and how the response worked. The timeline does not establish that either individual caused the outcome or warrants discipline.** Their actions deserve examination alongside deployment safeguards, alert routing, escalation and rollback authority.

For Friday, give your VP a named remediation lead, verified findings, remaining uncertainties and owners for corrective actions. Assess any conduct concerns separately, using evidence about expectations, available information and working conditions.

Here is a working facilitation pack.

**Before the meeting**

Invite the on-call, merging engineer, payments engineer, platform-commons maintainer, DBA, support lead and incident commander. Use a facilitator who was not directly involved and a separate note-taker. Interview key participants individually first, particularly given the pressure to identify someone.

Collect:

- Deployment diff, effective pool configuration, platform-commons changelog and relevant test results.
- Database metrics, application logs and submission success/queue metrics.
- Alert payloads, routing rules, silence scope and incident communications.
- Procedures in force that day for upgrades, escalation and emergency rollback.
- Reconciled payment outcomes: delayed or failed submissions, affected customers, missed bank processing and any duplicates.

Treat the unread changelog as a reported fact to verify. Establish what it actually said and whether it explained the failure mechanism.

**Working timeline — Tuesday 29 September, UTC**

These entries come from your account; attach supporting evidence during preparation.

| Time | Event |
|---|---|
| 16:05 | payments-api v4.18 deployed, including platform-commons 3.4 → 3.5 |
| 16:14 | First failed submissions: “connection pool exhausted” |
| 16:22 | Pool saturation warning posts to Slack; no page |
| 16:31 | Latency page fires; acknowledged within two minutes, then silenced for two hours |
| 17:10 | First support tickets |
| 17:48 | Support escalates with 41 tickets and a customer list |
| 17:55 | Sev1 declared |
| 18:00 | Bank cut-off passes |
| 18:01 | Payments engineer finds pool exhaustion in logs |
| 18:05 | Rollback decision |
| 18:33 | DBA approval |
| 18:46 | Rollback complete |
| 19:20 | Queued submissions drained |

Three intervals deserve attention:

- First failed submission → Sev1: **101 minutes**.
- Rollback decision → completion: **41 minutes**, including 28 minutes before DBA approval.
- First failed submission → queue drained: **3 hours 6 minutes**. This is an observed incident interval; it does not prove every submission failed throughout.

Forty-one tickets do not establish 41 affected customers. Queue drain also does not establish that payroll reached recipients on time.

**Run a 60-minute AAR**

Open with:

> The purpose is to understand what happened, what people understood at the time, and what needs to change. Describe observations and decisions specifically. Distinguish evidence, recollection and hypotheses. Everyone can correct the record.

Do not promise immunity or confidentiality you cannot guarantee. Explain honestly how notes and findings will be used.

1. **Minutes 0–10: What was supposed to happen?**  
   Establish the intended payroll outcome and bank deadline, then the expected deployment checks, paging, escalation and rollback process. Record actual standards separately from practices people wish had existed.

2. **Minutes 10–25: What happened?**  
   Walk through the timeline. At each decision ask: “What could you see then? What did you think was happening? What options did you consider? What did you expect next?” Preserve disagreements as open questions pending evidence.

3. **Minutes 25–45: Why did events unfold this way?**  
   Use the questions below. Resist settling on a single cause before the technical mechanism and response conditions are understood.

4. **Minutes 45–55: What should be sustained or changed?**  
   Capture strengths as well as gaps: prompt page acknowledgement and support’s escalation with concrete customer evidence are observable positives. Ask what enabled those actions.

5. **Minutes 55–60: Read back commitments.**  
   Confirm findings, uncertainties, named action owners, dates and verification criteria. Let participants correct the account before publication.

**Questions that matter for this incident**

| Area | Ask |
|---|---|
| Upgrade and failure mechanism | What changed in 3.5? Can the exhaustion be reproduced under representative load and configuration? What made the upgrade appear ready to deploy? |
| Changelog | What relevant information existed, where was it presented, and how were consumers expected to act on it? What checks could catch the problem independently of reading it? |
| Alerting | Why was pool saturation a Slack warning? Who was expected to see it, and what response was expected? |
| On-call decision | What did the latency page and dashboards show? What made a two-hour silence seem appropriate? What investigation, monitoring or handoff continued afterward? Verify exactly what the silence suppressed. |
| Escalation and deadline | How did engineering receive support’s evidence? Who could see the approaching bank cut-off, and how did that affect incident severity and decisions? |
| Rollback | What happened between 18:05 and 18:33, then between approval and completion? What risks were being assessed, and what emergency authority existed? |

The upgrade is a **suspected trigger**. Pool exhaustion is an **observed failure mode**. The causal mechanism remains to be demonstrated. Likewise, the silence may have affected response, but its consequences need evidence.

**Proposed actions to refine in the meeting**

Assign an actual person to each role before closing.

| Proposed owner | Deliverable | Evidence of completion |
|---|---|---|
| Payments and library leads | Reproduce the failure; validate the fix and add a regression check | Representative workload demonstrates the mechanism and successful correction |
| SRE lead | Review paging, silence handling and escalation for submission failures | An injected failure reaches a responder and exercises escalation |
| Payments manager and DBA lead | Establish a safe emergency rollback path | A drill measures decision-to-recovery time against an agreed target |
| Support and incident-management leads | Connect customer impact and bank deadlines to escalation | A tabletop demonstrates timely handoff and decision ownership |
| Payments operations lead | Reconcile every affected submission | Recorded bank/customer outcomes, including delays and duplicate checks |

For individual accountability, examine each action separately: Was the expectation clear, workable and routinely followed? Did the person understand the risk? Would a similarly experienced colleague likely have acted the same way? What pressures or missing support mattered? A serious outcome alone cannot answer those questions.

This approach follows the Army AAR’s comparison of intended and actual performance and the NHS guide’s cautions about singling out individuals: [AAR guidance](run folder/tc-25-20-army-aar.pdf), [just-culture assessment](run folder/nhs-just-culture-guide.pdf).

[Participant]
Can we just add more alerts on the DB pool metrics and call it done?

[Facilitator]
More pool alerts could help, but they would leave most of INC-2291’s failure path intact. A pool warning already fired at 16:22; it posted to Slack without paging. Another alert only helps if it produces a timely response.

Keep the follow-up small, but cover three things:

- **Detection and response:** Make sustained submission failures page someone, with clear escalation and a defined follow-up when silenced. Test the route.
- **Prevention:** Verify what changed in platform-commons 3.5 and add a regression check that catches the failure.
- **Recovery:** Understand the 41 minutes from rollback decision to completion, then exercise a safe emergency rollback path.

Close those actions when there is evidence they work. “More alerts configured” is a deliverable; “a repeat failure is caught and recovered within an agreed time” is the outcome.

[Participant]
Okay.

[Facilitator]
Let’s start with what was supposed to happen. Before INC-2291, what was the agreed response to failed payroll submissions—who should be paged, when should they escalate, and who could authorize rollback?

If there was no explicit agreement, describe the usual practice.

[Participant]
Nothing written specifically for failed submissions that I know of. The pool-saturation alert was set up two years ago as a warning, so it posts to #payments-alerts rather than paging anyone. Rollback has been manual since March, when we disabled one-click after a rollback corrupted a migration, and a manual rollback needs DBA approval. On escalation, honestly, teams tend to hold off declaring until they're sure, because a leadership dashboard counts incidents per team.

[Facilitator]
That changes the AAR materially. The response was shaped by earlier decisions and incentives, alongside the actions taken that day.

Record these as **reported conditions to verify**:

- **Detection:** Pool saturation still used a two-year-old warning route, with no known procedure for failed submissions.
- **Recovery:** Manual rollback and DBA approval were safeguards introduced after migration corruption. Investigate how to make rollback safe and timely; simply restoring one-click could reintroduce that risk.
- **Escalation:** Counting incidents per team appears to discourage early declaration. Examine the dashboard and leadership’s use of it, then test whether that pressure influenced decisions during INC-2291.

These findings bring alert ownership, release safety and leadership incentives into scope. They also mean we cannot assess someone against an incident-response standard invented afterward.

For Friday, the VP should receive these conditions and corrective commitments, with leadership owning the review of incident-count incentives. Declaring an incident earlier should not become a penalty for the team raising it.

Next, reconstruct the on-call’s decision without assuming their reasoning: **What do we know about what they saw at 16:31, what they believed the customer impact was, and what investigation or monitoring continued after they silenced the latency alert?**

[Participant]
Honestly, I think he just wasn't paying attention; he's fairly new. What he saw at 16:31 was the p99 latency page, which had flapped 14 times that week, always around deploys, and the runbook says to silence known flapping alerts for the 2-hour deploy window, which he did. After that he was also working an urgent data-export request for an enterprise customer that account management had flagged; I don't know what he believed the customer impact was beyond that.

[Facilitator]
I’d leave “wasn’t paying attention” out of the findings. We have a more specific account: a relatively new responder received an alert that had flapped 14 times that week, followed the runbook’s two-hour silence instruction, and then worked another request marked urgent. His understanding of payroll impact remains unknown.

That makes three things worth examining:

- **Repeated flapping:** What had previous pages taught responders to expect, and who owned fixing the noise?
- **Runbook guidance:** How did responders distinguish a harmless deploy-related flap from an actual outage?
- **Competing priorities:** Who decided the export was urgent, and what coverage or prioritization support did the on-call have?

A provisional finding could be:

> The on-call silenced the latency alert in accordance with the documented instruction for known deploy-related flapping. Whether this occurrence met those conditions, and what monitoring was expected afterward, remain unresolved.

His relative inexperience makes onboarding and available support relevant; it does not establish carelessness.

**What checks, if any, did the runbook require before classifying a page as known flapping—such as checking submission success, queue growth or pool saturation?**

[Participant]
The line he followed just says "silence known flapping alerts for the deploy window (2 h)". I don't know of any required checks beyond that, but I'd have to check the full runbook to be sure.

[Facilitator]
Keep that uncertainty explicit. The quoted instruction supports his explanation, but we still need the full runbook and how “known flapping” was defined.

Tighten the provisional finding to:

> The on-call silenced the latency alert after repeated deploy-associated flapping, citing the runbook instruction to silence known flapping alerts for two hours. No required validation or follow-up checks have yet been identified. Review of the runbook version effective during INC-2291 is pending.

Assign the runbook owner to retrieve that version and check for prerequisites, monitoring requirements and escalation guidance. Assess his actions against the instructions available that day.

A candidate improvement is to define how responders verify a known flap, when they recheck or hand off, and how submission-failure detection stays effective during a latency-alert silence. Validate that proposal against the incident evidence.

**Now let’s examine the other initial allegation: what did the platform-commons 3.5 changelog actually say, and what evidence connects the upgrade to pool exhaustion?**

[Participant]
3.5 lowered the default DB connection pool from 50 to 20, billed as "safer defaults for small services", and that note is line 40 of a 52-line changelog. payments-api never set its pool size explicitly, so it picked up the new default of 20.

[Facilitator]
That gives us a concrete configuration-change path:

**Library upgrade → inherited pool limit falls from 50 to 20 → pool exhaustion observed after deployment.**

The upgrade changed payments-api’s effective production configuration even though nobody edited its pool settings. Metrics or reproduction should confirm that the smaller pool explains the failures under the workload that day.

Record this provisional finding:

> platform-commons 3.5 reduced the default connection pool from 50 to 20. payments-api inherited that change because it had no explicit setting. The changelog disclosed the change at line 40 of 52. Validation of the resulting capacity against payroll demand remains to be established.

The changelog’s availability matters when examining the developer’s decision. We also need to examine how a shared-library default change reaches consumers and what release checks catch its effects.

Candidate corrective actions are to make payments-api’s pool configuration explicit, validate it against workload and total database capacity, and test dependency upgrades under representative load. Don’t assume restoring 50 is sufficient without that validation.

**What validation did v4.18 pass before deployment—particularly load tests, staging checks or a canary that could reveal failed submissions or pool exhaustion?**

[Participant]
Load tests only run on major version bumps, so a minor bump like 3.4 to 3.5 didn't get one. Staging wouldn't have shown it either: staging sets the pool size to 50 explicitly, which we added back in 2024 during a staging performance problem. I don't know whether there was any canary step for v4.18; I'd have to check.

[Facilitator]
That identifies two concrete gaps in the release safeguards:

- **Load-test policy used version number as a risk proxy.** This minor release changed production capacity but did not trigger a load test.
- **Staging masked the production change.** Its explicit setting retained 50 connections while production inherited 20. A previous staging fix created a difference relevant to this incident.

Record the provisional finding as:

> The pool-default change reached production without a required load test. Staging retained the previous pool size through an explicit override, so it did not exercise production’s new configuration. Whether a canary provided additional validation remains unverified.

Assign the release owner to retrieve v4.18’s deployment records, including any canary traffic, duration, success criteria and results. Keep that question open.

Corrective actions should address both gaps: require capacity validation when dependencies change consequential defaults, and detect relevant configuration differences between staging and production. Making payments-api’s pool size explicit addresses this instance; those safeguards address recurrence through another setting or library.

This also changes how we assess the developer’s action: the unread changelog remains relevant, alongside a testing policy that excluded the change and a staging configuration that concealed its effect.

**Next, the recovery delay: what happened between the rollback decision at 18:05 and DBA approval at 18:33?** Establish when approval was requested, what information or safety checks were needed, and whether anyone was waiting for an available approver.

[Participant]
The DBA on shift was in a vendor meeting until 18:30, so yes, we were effectively waiting for an available approver. We only have two DBAs covering nine product teams. I don't know exactly when the approval request went in or what checks the DBA ran before approving; I'd have to check.

[Facilitator]
That makes **access to rollback approval** a concrete recovery issue. Approval at 18:33 followed the DBA’s meeting ending at 18:30. We cannot attribute the entire 28-minute interval to waiting until we establish when approval was requested.

Record:

> Emergency rollback required DBA approval. The on-shift DBA was unavailable until approximately 18:30; approval followed at 18:33. The request time, approval checks and available backup arrangements remain unverified. Two DBAs support nine product teams.

Assign follow-up to the database and engineering managers:

- Recover the request timestamp, approval checks and steps between approval and rollback completion.
- Establish what backup or escalation path existed.
- Design and exercise emergency coverage, including delegated approval for defined, validated rollback scenarios where appropriate.

The staffing ratio warrants examining concurrent demand and coverage. It does not, by itself, establish the staffing level needed. Preserve the migration-safety safeguard while addressing the dependency on an available approver.

The emerging account now includes production configuration changes, validation gaps, noisy alerts, ambiguous silence guidance, escalation incentives and constrained recovery authority. That is substantial evidence for a broader explanation than either initial allegation alone.

**Next, establish the business impact: what do we know about how many payroll submissions were delayed or failed, which missed bank processing, and whether the 19:20 queue drain meant successful bank acceptance?**

[Participant]
1,180 employer accounts saw failures, and 37 payroll runs missed the 18:00 cut-off. Finance ops paid the bank's fee for its late-processing window and got 22 of those 37 through that evening. The other 15 runs, about 3,800 employees, were paid a day late, so no, the 19:20 drain didn't mean everything was accepted on time.

[Facilitator]
Then **19:20 was queue recovery, not completion of payroll recovery**. The AAR should lead with the people and employers affected.

There is enough information now for this consolidated draft, subject to participant review and the evidence checks below.

**INC-2291 affected 1,180 employer accounts. Thirty-seven payroll runs missed the 18:00 bank cut-off.** Finance operations secured late processing for 22 runs that evening and paid the bank’s fee. The remaining 15 runs, covering approximately 3,800 employees, were paid one day late. The fee amount and other financial consequences remain to be established.

The incident began after payments-api v4.18 deployed at 16:05 UTC on Tuesday 29 September. Failed submissions appeared at 16:14. A pool-saturation warning posted to Slack at 16:22 without paging. The 16:31 latency page was acknowledged promptly and silenced for two hours. Support escalated at 17:48; Sev1 was declared at 17:55, five minutes before cut-off. Rollback was decided at 18:05, approved at 18:33 and completed at 18:46. Queued submissions drained by 19:20, while affected payroll recovery continued into the following day.

The working explanation has six connected parts:

1. **The dependency upgrade changed production capacity.** platform-commons 3.5 lowered the default pool from 50 to 20. Production inherited that setting. This is a strong candidate explanation for the observed exhaustion; metrics or reproduction should confirm the mechanism.

2. **Known validation safeguards missed that configuration change.** Load tests were required only for major upgrades. Staging explicitly retained 50 connections, masking production’s new setting. Canary use remains unknown.

3. **Alerting and response guidance provided weak discrimination.** The pool warning did not page. The latency alert had flapped 14 times that week, and the quoted runbook instructed responders to silence known flapping alerts for the two-hour deploy window. The full runbook and the responder’s classification of this occurrence still need review.

4. **Work competed for the on-call’s attention.** After silencing the page, the responder worked an enterprise export request marked urgent. Their understanding of payroll impact and the prioritization arrangements are unknown.

5. **Leadership measures reportedly discouraged early escalation.** Teams described waiting for certainty because a dashboard counted incidents per team. Establish how that pressure affected decisions during INC-2291 and review leadership’s use of the measure.

6. **Recovery depended on scarce approval availability.** Manual rollback required DBA approval following an earlier migration-corruption incident. The on-shift DBA was unavailable until approximately 18:30. The approval-request time, safety checks and backup arrangements remain unverified.

Preserve the useful responses too: prompt acknowledgement of the page, support’s escalation with customer evidence, and finance operations’ recovery of 22 payroll runs through late processing.

For corrective work, assign actual names against these proposed owners:

| Proposed owner | Commitment | Completion evidence |
|---|---|---|
| Payments service owner | Confirm the failure mechanism; set and validate explicit pool configuration against workload and database capacity | Representative load demonstrates successful submissions with the intended configuration |
| Platform and release leads | Trigger validation for consequential dependency changes; identify relevant staging/production differences | The incident’s configuration change is detected before production in a replay |
| SRE/on-call lead | Repair flapping, define silence checks and follow-up, and ensure submission failures reach a responder | An exercise demonstrates detection and escalation within agreed response targets |
| Database and engineering managers | Provide migration-safe emergency rollback coverage and backup authority | A drill demonstrates safe recovery without waiting for one specific approver |
| Engineering leadership | Change dashboard use and escalation expectations so early declaration is supported | Explicit policy, revised reporting and review of subsequent escalation decisions |
| Finance operations lead | Reconcile all affected runs, fees and customer outcomes | Every affected run has a confirmed final outcome and recorded remediation |

**For Friday, name one senior service owner accountable for delivering this plan.** Each action should also have its own named owner, date and acceptance criterion. Friday can be the deadline for those commitments and the provisional findings; completion dates should reflect the work required.

The current evidence does not justify selecting either the on-call or merging engineer for discipline. Obtain both accounts, verify the expectations in force, and assess any specific conduct concern separately. In particular, the quoted runbook supports the on-call’s explanation, while the upgrade passed through a validation policy that excluded load testing and a staging configuration that masked its effect.

Before publishing, read this account back to participants, attach evidence, and retain unresolved questions explicitly. Keep remediation open until the agreed checks demonstrate that the changes work.

[Participant]
Thanks, that's what I needed.
