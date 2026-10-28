[Facilitator]
I can help you run this, and I can help you answer your VP by Friday. I'd advise against using this review to pick the person, though. Here's why, and then the first questions for setting up.

## The "one person by Friday" request

The sources in this library all say the same thing: keep the learning review and any personal-accountability decision on **separate tracks**.

- **The Columbia report** chose to "identify and correct threats" rather than assign blame. It took privileged statements so people would admit mistakes, and left personal accountability to a separate process (`caib-report-vol1`, Concept 10). It also says individuals are still "responsible and accountable", but that systemic problems "cannot be solved simply by retirements, resignations, or transferring personnel" [V].
- **The Forest Service guide** calls a firewall between the review and any disciplinary action "critical", because "Information is the lifeblood of safety" [V] (`lfuo-learning-review-guide-2024`, Concept 3). If the on-call engineer and the developer believe this review is where a culprit gets chosen, you won't hear what they actually saw and knew.
- **The DOE handbook** warns: "Events will continue as long as event investigations stop prematurely at the active human error" [V] (`doe-hpi-handbook-vol1`, Concept 9).

You can still give your VP something concrete. The **NHS Just Culture guide** is a decision tree for exactly the question "is individual action warranted?" It's meant to be shared openly before anyone is judged. It starts from this position: "Action singling out an individual is rarely appropriate — most patient safety issues have deeper causes and require wider action" [V]. The guide was written for healthcare, so applying it to software is my adaptation. It has two rules that matter here:

1. **One action at a time.** "If multiple actions are involved in an incident they must be considered separately" [V]. Silencing the page and merging without reading the changelog are two separate trips through the tree, and each one needs facts we don't have yet.
2. **The foresight test comes before anything aimed at the person.** Was there an agreed protocol? Was it workable and actually in routine use? Did the person *knowingly* depart from it? If any answer is no, the guide's outcome is that singling out the individual is unlikely to be appropriate (Recommendation D).

**My suggestion for Friday:** send the VP the process rather than a name. Tell them the review is under way, that any individual decision will go through a published decision tree on a separate track, and that every action from the AAR will have one named owner, a date and someone who checks it worked. The Forest Service guide calls this *forward-looking accountability*: who will fix it, not who caused it. I can draft that note.

## Questions the timeline already raises (for the review, not verdicts)

- **The signal that pointed to the cause went nowhere.** `db-pool-saturation` fired at 16:22 as a *warning*, to Slack only, with no page. The page the on-call got at 16:31 was about *p99 latency*, a symptom. What did that page tell them, and what does the runbook say to do with it?
- **Is a 2-hour silence normal practice?** This is the substitution test: would other on-call engineers have done the same with the same page? Is silencing a noisy latency alert common on this rotation?
- **Is reading the changelog for an internal minor bump a real, routinely followed step?** For 3.4 → 3.5 of `platform-commons`, did the changelog even mention pool behaviour? Who owns that library and how it announces changes?
- **16:33 to 17:48 is blank.** Was anyone looking at payments during that time? Detection came from support, not monitoring.
- **The rollback was decided at 18:05 and approved by the DBA at 18:33.** That's 28 minutes waiting for approval after the 18:00 bank cut-off had already passed.

## Setup (Phase 0)

No issue tracker, Slack or alerting tool is connected to this session, so we'll work in **paste mode** from what you give me. Please **leave out the customer list and any customer data** from the 17:48 escalation, and any credentials. Ticket counts and timestamps are enough.

Before we build out the timeline, two questions. Please answer in your own words; I'll keep your answers exactly as you write them:

1. **In a few sentences, what would you tell a coworker about this incident?**
2. **Who saw it differently, and what would they say?** In particular, have the on-call engineer and the developer given their own accounts yet? If not, it's better to get those before they see the assembled timeline.

Also:

3. **Dates:** the timeline says Tuesday 29 September, which was four weeks ago. Is that right, or was it this Tuesday (27 October)? It affects how fresh people's memories are.
4. **Who's coming to the review:** payments engineering, on-call, the `platform-commons` owners, the DBA, support, and whoever owns alert routing?

[Participant]
Honestly, I think he just wasn't paying attention; he's fairly new. To a coworker I'd say a library bump took payroll submissions down for a couple of hours, we heard about it from support rather than monitoring, and we missed the bank cut-off. I've talked to the on-call, the DBA, the support lead and the payments engineer, but not the developer; the on-call is mortified and has asked his manager whether he'll be taken off the rota. I'd have to check the date and who can make the review.

[Facilitator]
## First account (kept as you gave it)

> "A library bump took payroll submissions down for a couple of hours, we heard about it from support rather than monitoring, and we missed the bank cut-off."

> "Honestly, I think he just wasn't paying attention; he's fairly new."

I'll compare both with the timeline later. Two differences already show up, and they're things to look into, not mistakes to correct:

- **"A couple of hours":** submissions failed from 16:14 until the rollback at 18:46, which is about 2½ hours. The queue didn't clear until 19:20, so it was about 5 hours from deploy to fully drained. Which figure does payroll care about?
- **"We heard about it from support rather than monitoring":** monitoring did fire, twice: `db-pool-saturation` at 16:22 and the latency page at 16:31. So the question isn't why monitoring missed it. It's why two signals that fired didn't lead anyone to the cause. That changes which fixes make sense.

## "He just wasn't paying attention; he's fairly new"

Which person do you mean, the on-call or the developer? Either way, I'd treat it as a lead to follow rather than a conclusion:

- **The DOE handbook** says plainly: "'Inattention to detail' and 'not following procedures' are not root causes" [V] (`doe-hpi-handbook-vol1`, Concept 8). It also says hindsight pushes investigators toward individual shortcomings, and that explaining what someone *should* have done tells you nothing about why they did what they did (`doe-hpi-handbook-vol2`, Concept 3).
- **"Fairly new" is a system question.** In the NHS tree's substitution test, two of the three questions are: *was the person missed when training was given?* and *did supervision fall short?* A yes to either leads to the outcome where singling out the individual is unlikely to be appropriate (`nhs-just-culture-guide`, Concept 6). So we'll want to know how this person was onboarded to the rota or to the merge process, and who was backing them up.

## The on-call engineer asking about the rota

This matters now, before the review happens. It's not a side issue.

- **The Marine Corps doctrine (MCDP 1)**: "a subordinate's willingness to admit mistakes depends on the commander's willingness to tolerate them" [V] (`mcdp1-warfighting`, Concept 3). Everyone else on the rota is watching how his question gets answered.
- **The Columbia report**: systemic problems "cannot be solved simply by retirements, resignations, or transferring personnel" [V] (`caib-report-vol1`, Concept 11). If he's taken off the rota, the next engineer gets the same Slack-only warning and the same latency page.

**My suggestion:** ask his manager to tell him this week that no rota decision depends on this incident, and that the review is about how the alerts and the response were set up. That's his manager's call, not mine or yours. But if he goes into the review worried about his position, you'll get a careful account instead of an honest one.

## The developer: get their account before they see anything

You haven't talked to the developer yet, which is actually an advantage. The DOE handbook says to interview people before you've built up detailed knowledge of the event. Let them tell the story, mark the key moments, and at each one ask what they noticed, knew, expected and were aiming for, and what time pressure they were under (`doe-hpi-handbook-vol2`, Concept 4). Don't show them the timeline, and don't open with the changelog. TC 25-20 recommends questions like "What happened when X?" over "Why didn't you Y?", because the second kind puts people on the defensive (route, Phase 1).

Suggested questions, in order:

1. Walk me through the v4.18 change, from when you picked it up to the merge.
2. What was the `platform-commons` bump for? Was it the point of the PR, or did it come along with other changes?
3. How do library bumps usually go on this team? What do people normally check?
4. What did review and CI tell you about it?
5. What else was going on that day or that week?
6. Looking back, was there a moment you weren't sure about something?

Questions 3 and 4 give us the facts for the NHS foresight test: was there an agreed step to read changelogs, and was it actually in routine use?

## Phase 1: what I need from the interviews you've done

You've talked to four people, so you can probably answer most of these now. Please leave out customer and employee personal data.

1. **Impact:** How many payroll submissions or employers missed the 18:00 cut-off? What did that mean for them (late pay, manual bank runs, fees)?
2. **On-call, 16:31–17:55:** What did the latency page say, and what did he do after acknowledging it? Was the 2-hour silence his choice or a default option? Did he see the `db-pool-saturation` message in Slack?
3. **The `db-pool-saturation` alert:** Who set it to warning, Slack-only, no page, and when? Has it fired before without anything going wrong?
4. **The `platform-commons` 3.5 changelog:** What does it actually say about connection pooling? Paste the relevant lines if you can.
5. **The PR for payments-api v4.18:** Who reviewed it, and did anyone mention the library bump?
6. **18:05–18:33:** Why was DBA approval needed for the rollback, and what took 28 minutes?
7. **Support, 17:10–17:48:** How long were tickets coming in before they were escalated, and what made the support lead escalate when they did?

There's no issue tracker, Slack or alerting tool connected to this session, so I'm working only from what you paste. Every timeline entry will need an evidence link (alert ID, Slack permalink, PR URL), and I'll mark any entry without one. When you have the date and the attendee list, send them along with these answers and I'll put together the draft timeline.

[Participant]
I meant the on-call. Impact: 1,180 employer accounts saw failures and 37 payroll runs missed the 18:00 cut-off; finance ops paid the bank's late-processing fee and got 22 through that evening, and the other 15 (about 3,800 employees) were paid a day late. He acked the latency page and silenced it for 2 h because the runbook says to 'silence known flapping alerts for the deploy window (2 h)', and he followed it; `db-pool-saturation` was never silenced, it was created two years ago as a warning that only posts to #payments-alerts, which gets about 220 alerts a week, mostly auto-resolving, and nobody watches live. I don't know who set it up or its firing history. The 3.5 changelog lowered the default DB pool from 50 to 20 ('safer defaults for small services'), on line 40 of 52. The bump was an automated dependency-bot PR, auto-merged when CI went green, so nobody reviewed or merged it by hand. One-click rollback has been off since March after one corrupted a migration, so manual rollbacks need DBA approval, and the DBA on shift was in a vendor meeting until 18:30. On support, tickets started at 17:10 and were escalated at 17:48; I'd have to check what made the support lead escalate then. I still need to confirm the date and who can attend.

[Facilitator]
Those answers change the picture a lot, including the question your VP asked.

## What the facts now show

**Neither of the two original claims holds up as stated:**

- **"The dev who merged the library upgrade didn't read the changelog":** no person merged it. A dependency bot opened the PR and it auto-merged when CI passed. There's no human decision there to evaluate. The decisions that matter are older ones: someone turned on auto-merge for bot PRs, and the `platform-commons` maintainers shipped a pool-size cut from 50 to 20 in a minor version, described as "safer defaults", on line 40 of 52.
- **"The on-call silenced the alert":** he silenced the *latency page*, and he did it by following the runbook ("silence known flapping alerts for the deploy window (2 h)"). The alert that pointed at the cause, `db-pool-saturation`, was never silenced. It posted to a channel that gets about 220 alerts a week and that nobody watches live. It was set up that way two years ago.

If your VP heard the original version, they need the corrected one before Friday. I've drafted a note at the end.

## Draft timeline (Phase 1)

All times UTC. **Date still to be confirmed.** None of these entries has an evidence link yet. Each one needs an alert ID, Slack permalink, PR URL or ticket link before the AAR is final.

| Time | Event | Evidence |
|---|---|---|
| ~2 yrs ago | `db-pool-saturation` created as a warning that only posts to #payments-alerts; no page | Needed: alert config and history |
| March | One-click rollback switched off after one corrupted a migration; manual rollbacks now need DBA approval | Needed: decision record or ticket |
| Unknown | Dependency bot set to auto-merge when CI is green | Needed: repo settings history |
| Unknown | `platform-commons` 3.5 released; default DB pool 50 → 20, "safer defaults for small services" (changelog line 40/52) | Needed: changelog or release link |
| Before 16:05 | Bot PR bumping `platform-commons` 3.4 → 3.5 auto-merges on green CI; no human review | Needed: PR URL |
| 16:05 | payments-api v4.18 deployed (automatic or manual? *gap*) | Needed: pipeline run |
| 16:14 | First failed submissions: "connection pool exhausted" | Needed: logs |
| 16:22 | `db-pool-saturation` (warning) posts to #payments-alerts; no page | Needed: Slack permalink |
| 16:31 | On-call paged: "payments p99 latency high" | Needed: alert ID |
| 16:33 | On-call acks and silences for 2 h, following the runbook's deploy-window rule | Needed: page log, runbook link |
| 17:10 | First support tickets | Needed: ticket IDs |
| 17:48 | Support lead escalates in #incidents (41 tickets) | Needed: Slack permalink |
| 17:55 | Sev1 declared | Needed: incident record |
| 18:00 | Bank cut-off passes | — |
| 18:01 | Payments engineer finds pool exhaustion in logs | Needed: Slack permalink |
| 18:05 | Decision to roll back; DBA approval needed; DBA on shift in a vendor meeting | Needed: Slack permalink |
| 18:33 | DBA approves | Needed: Slack permalink |
| 18:46 | Rollback complete | Needed: pipeline run |
| 19:20 | Queued submissions drained | Needed: metrics or log |
| Evening | Finance ops pays the bank's late-processing fee; 22 of 37 runs go through | Needed: finance ops record |
| Next day | 15 runs (~3,800 employees) paid a day late | Needed: finance ops record |

**Impact:** 1,180 employer accounts saw failures; 37 payroll runs missed the cut-off; ~3,800 employees were paid a day late; the bank charged a late-processing fee.

**What the timeline already shows:**

- **The cut-off was lost before anyone knew the cause.** The Sev1 was declared at 17:55 and the cause found at 18:01, both within minutes of the 18:00 cut-off. Even an instant rollback at 18:05 wouldn't have saved it. So two problems need separating: the **1 h 47 min from first failure to diagnosis** cost the cut-off; the **28-minute wait for approval** cost the 1,180 accounts more time failing.
- **Two signals fired, and neither pointed anyone to the cause.** The Columbia report asks that a timeline carry the signals that existed but didn't register, and say why each one was discounted (`caib-report-vol1`, Concept 3). Here we have two: a correct diagnosis sent to a channel nobody watches, and a symptom page that the runbook classes as deploy noise.
- **The runbook rule silences alerts during exactly the window when a bad deploy shows up.** "Silence known flapping alerts for the deploy window" quiets alerts in the two hours after a deploy, which is when a deploy-caused fault is most likely to appear. The DOE handbook calls this kind of failure rule-based: "applying the correct procedure to the wrong situation" [V] (`doe-hpi-handbook-vol1`, Concept 2). He applied the rule correctly; the rule had no way to tell flapping from a real fault.
- **Possible pattern for later: a fix that created a new problem.** Turning off one-click rollback after March was a sensible fix, and it may have added the approval wait seen here. I'm noting it as a hypothesis to test in Phase 7, not a finding.

## The on-call's action through the NHS tree (provisional)

The guide says it "may need to be revisited as more information becomes available" [V] (`nhs-just-culture-guide`, Concept 10), so treat this as provisional. One action only: **silencing the latency page at 16:33.**

1. **Deliberate harm?** No.
2. **Health?** Nothing you've told me suggests it. Confirm through his manager rather than assume.
3. **Foresight:** There was an agreed protocol, and it seems to be workable and in routine use. But he **did not depart from it; he followed it.** That makes the knowing-departure question a no, and the tree stops here at **Recommendation D**: "Action singling out the individual is unlikely to be appropriate; the patient safety incident investigation should indicate the wider actions needed to improve safety for future patients. These actions may include, but not be limited to, the individual." [V]

**There's nothing to take through the tree for the developer**, because no human merged the PR. On the DOE handbook's culpability spectrum, which judges by intent rather than consequence (`doe-hpi-handbook-vol2`, Concept 11), the on-call's action sits at the *organisation-induced* end: he followed the procedure the organisation gave him.

The "fairly new" point still matters, but as a system question: how was he onboarded to the rota, and did the runbook or the page tell him a payments deploy had just gone out?

## Still open for the timeline

1. **On-call's inside view:** Was "payments p99 latency high" on a known-flapping list, or was that his judgement? Did he know payments-api had deployed at 16:05? What did he do between 16:33 and 17:55?
2. **The 16:05 deploy:** Did it go out automatically after the bot merge, or did someone trigger it?
3. **CI:** Is there any test that would show pool exhaustion under realistic load?
4. **`db-pool-saturation`:** Its firing history (has it fired before with nothing wrong?), and whether anyone ever watched #payments-alerts live. This tells us whether this is drift or something that was never designed in.
5. **Support:** What made the support lead escalate at 17:48 rather than earlier?
6. **The date and the attendee list.** Add the `platform-commons` maintainers and whoever owns the dependency-bot settings.

## Draft note to your VP

> **INC-2291 (payroll submission outage): status of review**
>
> The review is under way. Initial facts change the picture we started with:
> - The library upgrade wasn't merged by a person. A dependency bot auto-merged it when CI passed. The upgrade cut the default DB connection pool from 50 to 20, a change described in the changelog as "safer defaults".
> - The on-call engineer silenced the latency page by following our runbook's rule for alerts during deploy windows. The alert that identified the actual cause posts only to a Slack channel that gets ~220 alerts a week and isn't watched live. It has been set up that way for two years.
> - Rollback took longer because one-click rollback has been disabled since March and manual rollbacks need DBA approval.
>
> Impact: 1,180 employer accounts affected; 37 payroll runs missed the 18:00 bank cut-off; 22 were recovered that evening at the cost of a late-processing fee; 15 (~3,800 employees) were paid a day late.
>
> On individual accountability: we're applying the NHS Just Culture decision tree, one action at a time. The on-call engineer followed the agreed procedure, so action aimed at him isn't appropriate. No individual merged the upgrade. Accountability from this review will be forward-looking: each corrective action will have one named owner, a deadline and a named person who checks it worked. The full AAR and action owners will follow on [date].

Do you want to change anything in the note? Once you have the date, the attendees and the on-call's answers to question 1, I'll finish the timeline and we'll move on to what kind of problem this is and the decision-by-decision reconstruction.

[Participant]
My VP is going to push back on that. What do I tell him? On your questions: the p99 page had flapped 14 times that week, always around deploys, and he was also working an urgent data-export request for an enterprise customer that account management had flagged. Load tests run only on major version bumps, and staging sets the pool size to 50 explicitly, so it couldn't have shown the change; I don't know whether the deploy went out automatically, the alert's firing history, or what made support escalate when they did, and I'm still checking the date and attendees.

[Facilitator]
The new facts make the case for not singling anyone out stronger, so you have more to stand on with your VP than you did yesterday.

## What the new facts add

- **The p99 page had flapped 14 times that week, always around deploys.** This is the substitution test: would a peer have done the same? Most on-call engineers would, after 14 false alarms in a week, with a runbook rule telling them to silence it. That's a yes, so the tree lands on Recommendation E as well as D: singling out the individual is unlikely to be appropriate (`nhs-just-culture-guide`, Concept 6). Note too that this alert had come to be treated as normal background. The Columbia report describes the same thing happening to foam strikes, which went from a safety issue to "in family" (`caib-report-vol1`, Concept 2).
- **He was also working an urgent enterprise data export that account management had flagged.** So he had two goals pulling at his attention and time pressure on both. That belongs in the decision reconstruction, and it doesn't count against him.
- **CI couldn't have caught it.** Load tests only run on major version bumps, and staging sets the pool to 50 explicitly, so the change from 50 to 20 couldn't show up before production. A green CI run said nothing about this risk.

## What to tell your VP

He'll probably push back in one of these ways. Here's how I'd answer each.

**"So nobody is accountable?"**
"Yes, people are accountable, for fixing it. Every action from this review will have one named owner, a deadline and someone who checks it worked." The Columbia report holds both positions at once: individuals are "responsible and accountable", but problems like these "cannot be solved simply by retirements, resignations, or transferring personnel" [V] (`caib-report-vol1`, Concept 11). The NHS guide states its purpose as both "protecting staff from unfair targeting" [V] and "removing the tendency to treat wider patient safety issues as individual issues" [V]. Here that means customers and employees are better protected by fixing the alerts than by reprimanding the person who followed the runbook.

**"He should have checked the Slack channel / he's new."**
"The channel gets 220 alerts a week and nobody watches it live. That's how it was set up two years ago. The page he did get had been a false alarm 14 times that week, and the runbook told him to silence it. Anyone on the rota would have done the same." Then ask your VP: *would we be talking about this silence if nothing had broken?* He silenced the same page 14 times that week and nobody noticed. The DOE handbook names judging people "based on the consequence of their action, not the intent of the action" [V] as the failure (`doe-hpi-handbook-vol1`, Concept 10).

**"Customers were hurt, somebody has to answer for it."**
"If we take him off the rota, the next on-call gets the same unwatched channel, the same flapping page and the same runbook rule, and one-click rollback is still switched off." The DOE handbook calls this the *blame cycle*: discipline leads to less trust, people report less, managers know less about what's happening on the ground, and the hidden weaknesses stay put. "Events will continue as long as event investigations stop prematurely at the active human error" [V] (`doe-hpi-handbook-vol1`, Concept 9). Your VP also needs to know that the on-call engineer has already asked whether he'll be taken off the rota, and that the rest of the team is watching the answer.

**"Fine, then who set all this up?"**
Have this ready, because it's where the pressure goes next. The decisions that shaped this incident all have owners: the deploy-window silencing rule, the alert routing to an unwatched channel, auto-merge for bot PRs, load-testing only major versions, the staging pool override, switching off one-click rollback, and the library team shipping a pool-size change in a minor release. **Those owners are where the actions go, not people to blame.** Each was probably a reasonable choice when it was made; the March rollback decision clearly was. If anyone wants to evaluate one of those decisions as an individual's action, the same tree applies, one action at a time.

**How to say it:**
- **Hand him the decision tree itself.** The NHS guide is designed to be shared with everyone in advance, so they know what framework will be used (`nhs-just-culture-guide`, Concept 11). Walk him through the on-call's single action: he didn't depart from the protocol, and peers would have done the same, so the tree ends at D and E.
- **Give him something to own.** Several of the decisions above sit at his level, such as the rollback policy, the load-testing policy and on-call workload. Ask him to sponsor one of those actions. That's accountability he can show upward.
- **Know where your role stops.** Personnel decisions belong to him and HR, on a separate track. The Forest Service guide treats a firewall between the review and disciplinary action as "critical" [V] (`lfuo-learning-review-guide-2024`, Concept 3). If he still wants action against the on-call, the AAR's findings stay as the evidence shows, and he can't use the review to support that decision.

## A pattern to test in Phase 2 (a hypothesis, not a finding)

Four separate decisions seem to rest on the same belief, that **a minor version bump is safe**: auto-merge on green CI, load tests only for major bumps, a staging config that would hide a default change, and the library team putting a pool-size change in a 3.5 release. We'll test this rather than assume it. The detection and recovery problems (alert routing, the deploy-window rule, competing on-call work, the rollback policy, depending on one DBA) may be separate chains with separate causes.

## Still open

1. The date and attendees.
2. Did the 16:05 deploy go out automatically after the bot merge?
3. `db-pool-saturation` firing history.
4. What made the support lead escalate at 17:48?
5. Who owns the deploy-window runbook rule, and when was it written?

When you have those answers, I'll update the timeline and we'll move on to classifying the problem and reconstructing the key decisions.

[Participant]
Can we just add more alerts on the DB pool metrics and call it done? On your questions: I'd have to check the date, attendees, whether the deploy went out automatically, the alert's firing history and who owns the runbook rule. I don't know why support escalated at 17:48 specifically, but the escalation itself was crisp: ticket count, customer list and first-seen time.

[Facilitator]
## Short answer

You can add an alert as one action. It won't fix this on its own, and nothing is "done" until each action has an owner, a date and someone who checks that it worked.

## Why more alerts won't fix this

**1. The alert you have worked; the routing didn't.** `db-pool-saturation` fired at 16:22, eight minutes after the first failure, and it named the right cause. It went into a channel with about 220 alerts a week that nobody watches. More pool alerts in that channel add to the noise that buried this one.

**2. Turning it into a page doesn't solve it either.** The runbook tells on-call to silence alerts that flap around deploys, for two hours after each deploy. A new pool page that fires during a deploy window looks like exactly that kind of alert, and the on-call would be right to silence it. The rule and the alert have to change together.

**3. Better detection doesn't speed up recovery.** Rollback still needs DBA approval, and the DBA on shift was in a meeting until 18:30. Even with a page at 16:22, how fast could you have rolled back? We need to know when that meeting started.

**4. Prevention stays exactly as it is.** The next default change in a minor version follows the same path: the bot auto-merges it, load tests don't run because it's minor, and staging hides it because the pool size is set explicitly there. An alert can only tell you after customers are already failing.

**5. Alerts depend on someone noticing.** The DOE handbook says "it is the number of controls and the weaknesses of those controls that dictate the severity of the event" [V]. It also prefers engineered controls, built into the system, over rules that rely on people noticing (`doe-hpi-handbook-vol1`, Concept 7). An alert relies on a person who, that afternoon, was also working an urgent enterprise export.

Two patterns from SSDL are worth testing here. **Shifting the burden:** a symptom-level fix eases the pressure, so the fundamental fix never gets funded. **Fixes that fail:** the fix makes the original problem worse over time, for example by adding alert noise. SSDL treats these as questions to test against what actually happened, not labels to apply (`ssdl-systems-thinking-foundations`, Concepts 10–11). The Forest Service guide also warns that recommendations "add complexity to the workplace, which has the paradoxical effect of increasing risk" [V] (`lfuo-learning-review-guide-2024`, Concept 14).

## A rough shape for the actions

These are candidates, not decisions. We'll settle them in the actions phase, with the people who'll carry them out. Aim for two or three actions you actually finish: the library's *reduce the batch size* practice says to limit how much is in progress and finish what you commit to (`open-kanban`, via route).

| What failed | Possible action |
|---|---|
| **Prevention:** a behaviour change got to production unseen | Stop auto-merging bot bumps of internal platform libraries, *or* make staging use production defaults, *or* have `platform-commons` flag default changes as breaking |
| **Detection:** the right signal went nowhere | Pool saturation on payments pages on-call, *and* the deploy-window silencing rule stops covering saturation alerts. The deploy window is when to be most alert, not least |
| **Recovery:** 28 minutes waiting for approval | A backup approver or an agreed approval time for rollback, or a safe version of one-click rollback |

The constraint analysis will tell us which of these is the real bottleneck. My working guess is prevention, because it's the only row that stops the next incident rather than shortening it. That's a guess, not a finding.

## What went well (noted for later)

- **Support escalation:** the support lead's 17:48 message gave ticket count, customer list and first-seen time. Sev1 was declared 7 minutes later. *What made it that good: a template, experience, or a past incident?* We should keep it and spread it.
- **Payments engineer:** found the pool exhaustion 6 minutes after the Sev1 was declared.
- **Finance ops:** got 22 of the 37 missed runs through that evening by paying the bank's late fee. That cut the number of employees paid late.

## Next: what kind of problem is this?

The open facts (date, attendees, whether the deploy went out automatically, firing history, runbook owner, when the DBA's meeting started) can come in parallel. Meanwhile, two quick questions:

1. **Once found, was the cause obvious?** Pool default changed from 50 to 20, connections ran out. My read: yes, clear in hindsight.
2. **Could this happen again the same way?** Another default change in a minor version, a flapping page silenced during a deploy, a rollback waiting on one approver. My read: yes, if nothing changes.

If you agree, this probably splits in two. The **technical fault is complicated but knowable**: one cause, one fix, reproducible once staging matches production. The **reason it took nearly two hours to see** is complex: it came from alert routing, a runbook rule, competing work and test policy interacting. Each part needs different analysis, so tell me if you see it differently.

[Participant]
Yes, it was obvious once the payments engineer saw it. payments-api never set its own pool size, so it just took the new default. And yes, it could happen again: since February, minor and patch bumps of internal libraries auto-merge to cut review load, and the bot opens about 60 PRs a week. The split sounds right to me, and I'd have to check when the DBA's meeting started and why the support escalation was that good.

[Facilitator]
## Problem type (Phase 2): recorded

- **The technical fault is complicated:** one cause, knowable and reproducible. payments-api never set its own pool size, so when the library default dropped from 50 to 20, payments-api got 20.
- **The two hours before anyone saw it is complex.** It came from several things interacting: alert routing, the runbook's deploy-window rule, the on-call's competing work, the test policy and the rollback policy.

The Forest Service guide expects that "multiple improbable events were necessary for the accident to occur" [V] (`lfuo-learning-review-guide-2024`, Concept 11). That fits the second part.

**Added to the timeline:**
- **February:** internal library minor and patch bumps set to auto-merge, to cut review load. The bot opens about 60 PRs a week.
- **March:** one-click rollback switched off.
- **Unknown date:** payments-api relies on the library's default pool size.

Two policies changed within about a month of each other this year. We'll check in Phase 6 whether that's drift or two separate decisions.

## Phase 3: reconstructing the key decisions

**The goal:** for each decision, work out what the person knew, what they were trying to do, and what was pushing on them at the time. Hindsight doesn't count. The DOE handbook asks, for each person, what they were trying to do, what they were focused on and what they knew at each critical point (`doe-hpi-handbook-vol1`, Concept 8, credited to Dekker [BT]). Rows marked *?* are gaps I need from you or from the people involved.

| Decision | When | What was known | What was missing | Pressure | Options they could see then |
|---|---|---|---|---|---|
| **Auto-merge minor/patch bumps of internal libraries** | Feb | ~60 bot PRs a week; reviewing them was a real load; minor and patch versions are meant to be compatible | That an internal library would change a runtime default in a minor; that load tests skip minor bumps; that staging hides pool changes | Review load (*how heavy? who raised it?*) | Keep manual review; auto-merge only patches; exempt some libraries (*were any considered?*) |
| **Ship a 50→20 pool default in `platform-commons` 3.5** | *?* | Small services were over-provisioned; "safer defaults" | Which consumers relied on the default, and how much load they carry (*did they have a way to know?*) | *?* | Major version; opt-in; notify consumers (*need the maintainers' account*) |
| **On-call silences the p99 page for 2 h** | 16:33 | Page had flapped 14 times that week, always around deploys; runbook says silence known flappers for the deploy window | That `db-pool-saturation` had fired 11 min earlier (*did he know payments-api had just deployed?*) | Urgent enterprise export flagged by account management | Follow the runbook; dig in while also carrying the export |
| **Support escalates to #incidents** | 17:48 (tickets from 17:10) | Rising ticket count, customers, first-seen time | *?* What made 17:48 the moment | *?* | *?* |
| **Roll back, wait for DBA approval** | 18:05–18:33 | Cause found; rollback needs DBA approval since March; cut-off already passed | When the DBA would be free (*was a backup approver possible?*) | 1,180 accounts failing; queue growing | Wait; interrupt the vendor meeting; find another approver (*did the policy allow one?*) |
| **Switch off one-click rollback** | March | A one-click rollback had corrupted a migration | How often a fast rollback would be needed, and who'd be available to approve it | After an incident; protecting data | Fix the rollback tool; gate only rollbacks that touch migrations (*were these considered?*) |

Every row looks like a reasonable decision given what that person knew. The cost appears where the decisions meet:
- auto-merge (Feb) × minor-only load tests × staging override × relying on the default
- the deploy-window rule × a page that really did flap × an unwatched channel
- the rollback gate (March) × one approver

None of those combinations was visible to whoever made each decision on its own.

**On the on-call specifically:** the DOE handbook says "Competence does not guarantee positive control" [V], and it reads violations as mostly "well intentioned, arising from a genuine desire to get a job done according to management's wishes" [V] (`doe-hpi-handbook-vol1`, Concepts 12 and 1). His case goes further than that: he wasn't breaking a rule at all. He was following one and carrying a second urgent job at the same time.

## The pressure question

The Columbia report asks what people *believed* the schedule required, not only what it said (`caib-report-vol1`, Concept 7). For each person:

1. **February auto-merge:** What did the team believe it couldn't afford, and who was asking for review load to come down?
2. **On-call:** What did he believe account management needed from him on the export, and by when? Did anyone tell him which mattered more?
3. **DBA:** Was it acceptable to step out of a vendor meeting for a rollback approval, and did anyone ask?
4. **`platform-commons` maintainers:** Was "safer defaults" driven by cost, an incident, or a platform goal?

## People to hear from

The original "developer" turned out to be a bot, so that interview isn't needed. The accounts we're missing now are:

- the **`platform-commons` maintainers** about the 3.5 change
- **whoever decided in February** to turn on auto-merge
- **whoever owns payments-api's configuration**, about relying on the default

Same approach as before: hear their account before showing them the timeline.

## Still open

- The date and the attendees
- Did the 16:05 deploy go out automatically?
- `db-pool-saturation` firing history
- Who owns the runbook rule
- When the DBA's meeting started
- Why support escalated at 17:48, and why the escalation was so good

You can answer the pressure questions from what you already know, and mark the rest as gaps. Next comes Phase 4, where we trace each failure path to its underlying causes. I expect three paths: **prevention** (how the change reached production unseen), **detection** (why two signals that fired didn't lead to the cause), and **recovery** (why rollback waited on one approver).

[Participant]
On February, all I know is it was done to cut review load from the roughly 60 bot PRs a week; I'd have to check who pushed for it. On the DBA, there are two DBAs serving nine product teams, so there wasn't much of a backup approver to go to, but I don't know whether anyone tried to pull the DBA out of the meeting. I don't know what the on-call understood the export deadline to be or whether anyone told him which took priority, and I haven't heard why the platform-commons team made the 'safer defaults' change.

[Facilitator]
## Phase 4: The three chains

Each chain traces one way this failed, step by step, through a series of "why?" questions. **Facts** come from what you've told me. **Hypotheses** are my reading and need checking with the people involved.

The Forest Service guide treats cause as "something we create by recreating the event" [V] (`lfuo-learning-review-guide-2024`, Concept 5). These chains are a construction to test, not a verdict.

### Chain A: Prevention. How a pool-size change reached production without anyone seeing it

1. **Why did submissions fail?** payments-api's DB pool dropped from 50 to 20 and ran out under payroll load. *Fact*
2. **Why did it drop?** payments-api never set its own pool size, so it took the library default, and `platform-commons` 3.5 lowered that default. *Fact*
3. **Why did nothing catch it before production?** Three checks all missed it:
   - the bot PR auto-merged when CI passed (policy since February)
   - load tests only run on major bumps
   - staging sets the pool to 50 explicitly, so the new default never showed there

   *Fact*
4. **Why did all three checks miss the same kind of change?** Each one assumes that a minor or patch bump doesn't change behaviour. The library team shipped a change in runtime behaviour as a minor release and called it "safer defaults". *Fact for the checks; hypothesis that it's one shared belief*
5. **Why does that assumption go untested?** The problem of reviewing 60 bot PRs a week was solved by removing review, not by sorting which bumps carry risk. Nobody seems to own the contract between `platform-commons` and the services using it: the library team may not know who relies on its defaults, and the consuming teams can't read 60 changelogs a week. *Hypothesis: we need the library team's account and the February decision-maker's account*

### Chain B: Detection. Why two signals fired and neither led to the cause (16:14 → 18:01)

1. **Why was the cause found at 18:01, after the support escalation?** The alert that named the cause went to an unwatched channel, and the symptom page was silenced. *Fact*
2. **Why was the channel unwatched?** It gets about 220 alerts a week, mostly auto-resolving, and `db-pool-saturation` has been a Slack-only warning since it was created two years ago. *Fact*
3. **Why was the page silenced?** The runbook's deploy-window rule told him to silence it; the page had flapped 14 times that week around deploys; and he was working an urgent enterprise export at the same time. *Fact*
4. **Why does the system create that much noise and then a rule to silence it?** Noisy alerts are handled by downgrading them, routing them to a quiet channel, or silencing them, rather than by fixing them. As a result, the two hours after a deploy, when deploy-caused faults are most likely, are when alerting is quietest. *Facts about the outcome; hypothesis about how it came about*
5. **Why has nobody fixed alert quality?** Possibly nobody owns it, and on-call shifts also absorb interrupt work such as account management's export request, so there's no protected time to fix noise. *Hypothesis: who owns the runbook rule, the alert, and on-call's workload?*

**A possible link I'd like to check:** if the bot's 60 PRs a week lead to more payments-api deploys, then the auto-merge policy from Chain A also increases the number of hours each week that alerts are silenced under the deploy-window rule in Chain B. If that's true, the two chains reinforce each other.

### Chain C: Recovery. Why rollback took 41 minutes (18:05 → 18:46)

1. **Why 41 minutes?** 28 of them were spent waiting for DBA approval. *Fact*
2. **Why was approval needed?** One-click rollback has been switched off since March, after one corrupted a migration. *Fact*
3. **Why the wait?** The DBA on shift was in a vendor meeting; there are two DBAs for nine product teams; and we don't know whether anyone tried to interrupt. *Fact, with a gap*
4. **Why does a rollback depend on a scarce role with no emergency route?** The March fix put a gate on *every* rollback, not only rollbacks that touch migrations, and it didn't define an approval time or a way to interrupt. *Hypothesis: what options were considered in March?*
5. **Is this capacity, or process?** The Open Practice Library warns against stopping at "not enough time, money, or resources"; instead, "we should ask why the process failed" [V] (`open-practice-library`, Concept 2). Two DBAs for nine teams is a real limit. The question is why the rollback process was designed as though one of them would always be free.

### How the chains relate

| Chain | Role | Effect |
|---|---|---|
| **A, prevention** | Necessary: no pool change, no incident | Started it |
| **B, detection** | Interacted with A | **Lost the 18:00 cut-off**, because the cause was found at 18:01 |
| **C, recovery** | Interacted with A | Did **not** affect the cut-off; kept 1,180 accounts failing longer and delayed the queue drain |

## Coverage of the five points

The five points are a way of checking where in the organisation a problem comes from. They follow Jay Galbraith's Star Model, put in plain words.

| Point | Implicated? | Where |
|---|---|---|
| **What we optimise for** | Yes | Reducing review load over checking bumps (A); urgent customer work landing on on-call (B) |
| **Who owns what** | Yes, likely | Library–consumer contract (A); alert quality (B); rollback approval (C) |
| **How work moves** | Yes | Auto-merge, major-only load tests, staging override, deploy-window rule, rollback gate (A, B, C) |
| **What gets measured and rewarded** | **Unknown** | Not examined yet |
| **Who we hire, grow and staff** | Yes | Two DBAs for nine teams (C); new on-call carrying interrupt work (B) |

## Quality check (this workflow's own scorer, not a library method)

- **Three chains, each traced four to five steps.** Each ends somewhere specific to this incident. "Minor bumps auto-merge because 60 PRs a week was too many to review" wouldn't fit another AAR unchanged.
- **The chains point to different things.** A is about a shared assumption, B about alert noise and on-call load, C about a single approver. This isn't one story with everything forced into it.
- **Rating: Good, could reach Excellent.** Step 5 of each chain is still a hypothesis, and the "measured and rewarded" point is untouched.

## Questions to firm this up

1. **Measured and rewarded:** What are the library team, the on-call rota and the payments team judged on? For example, ack time, deploy frequency, review turnaround, or customer requests closed.
2. **Deploy frequency:** How often does payments-api deploy in a typical week, and does the bot drive much of that? This tells us whether the A–B link is real.
3. **The library–consumer contract:** Does `platform-commons` know which services rely on its defaults? Is there any way for a consuming team to mark a setting as important to them?
4. **Alert ownership:** Who owns alert quality for payments, and has anyone tried to fix the p99 flapping before?
5. **Precedent:** Before February, did a reviewer ever catch a risky minor bump? Has a default change in an internal library caused trouble before?

These will mostly need the people involved. Answer what you can and mark the rest as gaps. Next comes Phase 6: checking whether this was drift (standards loosening over time), plus handoffs between teams and what went well. After that we move to actions.

[Participant]
On measurement: SRE's quarterly goal is mean time to acknowledge under 5 minutes, and a leadership dashboard counts incidents per team, so teams wait to declare until they're sure; nobody declared on the 16:22 warning. I don't know what the library or payments teams are judged on. On alerts, the June AAR for INC-2104 had the action 'tune noisy alerts', owner 'SRE team', no ticket, and it wasn't done; back in February the SRE lead had proposed an alert clean-up, but it was deprioritised for the Q3 enterprise-tier launch. I'd have to check deploy frequency, whether platform-commons knows who relies on its defaults, and any precedent from before February.

[Facilitator]
These answers add something important: a previous review already found the noisy-alert problem, and its action was never done.

## Two new contributors from how things are measured

**1. The incidents-per-team dashboard delays declaring.** Teams wait until they're sure before declaring an incident, so nobody declared on the 16:22 warning. The Sev1 came at 17:55, after 41 support tickets. This sits directly in the path that lost the cut-off. The Columbia report describes a similar trap, in which engineers had "to prove that the situation was unsafe — a reversal of the usual requirement to prove that a situation is safe" [V] (`caib-report-vol1`, Concept 4). Here the dashboard puts the burden on a team to be *sure* there's an incident before declaring one.

**2. The time-to-acknowledge target was met while the incident carried on.** SRE's goal is to acknowledge within 5 minutes. He acknowledged in 2 and then silenced the page, as the runbook says to. The target measures acknowledging, not understanding. Nothing measured time to diagnose or time to declare.

The Jones distillation carries Goodhart's Law as a way to read metrics like this: "Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes" [BT] (`jones-evidence-based-sweng`, Concept 2). This is a hypothesis, not a finding: I'd want to know whether on-call engineers feel the target, not only that it exists.

**Effect on the just-culture result:** none. The on-call followed the runbook *and* met his team's target. The NHS tree still ends at D and E.

## Phase 6: Is this drift?

**Drift** means what an organisation accepts as normal slowly shifts toward the risky, without anyone deciding it should. To call something drift, you have to be able to point to a moment when a risk was accepted that wasn't accepted before (this workflow's test, built on `caib-report-vol1`, Concepts 2 and 7).

| Pattern | Drift? | Evidence |
|---|---|---|
| **Alert noise accepted as normal** | **Yes.** | **February:** SRE lead proposes a clean-up; it's deferred for the Q3 enterprise-tier launch. **June:** the INC-2104 AAR assigns "tune noisy alerts" to "SRE team", with no ticket; it isn't done. **September:** the p99 page has flapped 14 times in a week and is treated as a "known flapping alert", and the runbook says to silence it. The Columbia report describes the same slide with foam strikes, which went from safety issue to "in family" to a maintenance item (Concept 2). |
| **Human review of minor bumps removed (Feb)** | **A deliberate loosening, not gradual drift** | A check was removed for a stated reason, reducing review load. It meets the test because a risk was knowingly accepted, but it was one decision, not a slow slide. |
| **One-click rollback switched off (Mar)** | **No.** It's the opposite. | A safety fix that tightened the process and had a side effect. We'll check in Phase 7 whether it's a fix that created a new problem. |
| **`db-pool-saturation` as a Slack-only warning** | **Probably a design gap, not drift** | It's been that way since it was created two years ago. The firing history would confirm. |
| **payments-api relying on the library's default pool size** | **Probably a design gap** | No sign it ever set the pool size itself. |

**The finding that matters most:** this is the **second AAR to find noisy alerts**. The first one produced an action with a team as owner, no ticket and no date, and it didn't happen. The Columbia report warns: "This decline in vigilance is a characteristic of many large organizations" [V] (`caib-report-vol1`, Concept 12).

So this AAR's actions have to differ from INC-2104's in *how they're set up*: one named person as owner, a ticket, a date, and someone who checks the action worked. That's also the best answer to your VP. The accountability that failed here was an action nobody owned.

The **Q3 enterprise launch** also shows up twice: it got priority over the alert clean-up in February, and an urgent enterprise export was on the on-call's plate during the incident. It's now Q4. Is the launch done? If so, the reason for deferring the clean-up may be gone.

## Phase 6b: Handoffs between teams

The incident crossed six teams: library team → bot and CI → payments → SRE alerting and on-call → support → DBA. The delays sat **at the boundaries between teams, not inside any one team**:

| Boundary | What was lost or delayed |
|---|---|
| Library → payments | The default change reached a team that depended on it without any notice beyond line 40 of a changelog |
| Alert → a person | The right diagnosis went into a channel nobody owns watching |
| Support → engineering | 38 minutes from first ticket to escalation, plus the dashboard's discouragement of declaring |
| Rollback decision → DBA | 28 minutes waiting on a shared role (two DBAs for nine teams) |

**Wait-to-work ratio (rough):** 16:14 to 18:46 is 152 minutes. Hands-on work after the Sev1 was about 23 minutes: diagnosis 6, decision 4, rollback 13. That leaves about 129 minutes undetected or waiting, a ratio of about **5.6 to 1**. That's rough, because "waiting" includes time before anyone knew. Still, about 85% of the outage went by with nobody working on it.

The Org Topologies primer names what ties these together: "If each element (e.g. policies, structures) is optimized in isolation, the performance of the whole system may actually decline" [V] (`org-topologies-primer-2025`, Concept 3). Each piece made sense for its own owner:
- auto-merge cut review load
- the acknowledge-time target measured responsiveness
- the incident dashboard tracked reliability
- the rollback gate protected data
- "safer defaults" saved resources for small services

**Single-thesis check:** this is an *amplifier* that runs across the three chains. It doesn't replace them. Each chain still needs its own action.

## What went well (as of now)

- **Support lead's escalation:** count, customer list, first-seen time. Sev1 followed within 7 minutes. *Still open: what made it that good?*
- **Payments engineer:** diagnosed it 6 minutes after the Sev1.
- **Finance ops:** recovered 22 of the 37 payroll runs that evening.
- **SRE lead:** proposed the alert clean-up in February, before this incident. Someone saw this risk coming, and that's a strength to build on, not a point to score.

## Questions before we design actions

1. **INC-2104:** What was it about? If it also involved payments, alerting or a library bump, and we find a third one, we may be looking at a class of incident at the same team boundary, not a one-off.
2. **The deploy-window silencing rule:** When was it written, and by whom? If it came after the alert noise grew, it's part of the drift.
3. **Enterprise-tier launch:** Has it shipped? Is the SRE lead's February clean-up proposal still on file?
4. **Owners:** Who in your organisation could personally own each of these? (a) alert routing and noise for payments; (b) the policy for bumping internal libraries; (c) the emergency path for rollbacks; (d) the incident-declaration norm and the dashboard. (d) may sit with your VP.

Next are Phases 7 to 9: checking for side effects of the fixes, finding the single highest-leverage fix, and the actions themselves, aiming for two or three with named owners.

[Participant]
INC-2104 was a smaller latency incident; I'd have to check the details beyond that. I don't know who wrote the deploy-window silencing rule or when, whether the enterprise-tier launch has shipped, or whether the SRE lead's February proposal is still on file. On owners, I'd have to check before putting names against any of those four.

[Facilitator]
We can design the actions now and leave the owner names blank until you've checked. What we can't do is close the AAR with those blanks still empty. That's how the INC-2104 action ended up unowned.

## Phase 7: Will the fixes create new problems?

SSDL describes a small set of recurring system patterns, or *archetypes*, and treats each as a hypothesis to test against the incident, not a label to apply (`ssdl-systems-thinking-foundations`, Concepts 10–11).

| Pattern | Fits? | Evidence |
|---|---|---|
| **Shifting the burden:** a quick workaround eases the pressure, so the real fix keeps getting put off | **Strong fit** | Alert noise was handled by downgrading alerts, routing them to a quiet channel and adding the deploy-window silencing rule. Meanwhile the clean-up was deferred twice (February, then the June INC-2104 action). |
| **Fixes that fail:** a fix solves one problem and creates another | **Likely** | Switching off one-click rollback in March protected data, but added a dependency on a scarce approver that slowed this recovery. *Your "add more alerts" idea would also fit this pattern if the alerts land in the same noisy channel.* |
| **Limits to growth:** something keeps growing until it hits a limit that pushes back | **Possible** | Bot PRs grew to about 60 a week and hit the limit of review capacity. The response was to remove review, not to deal with the limit. |
| **Drifting goals:** the standard drops instead of performance rising | **Possible, overlaps with the first row** | "Known flapping" became an acceptable state for a page. |

**Side effects to design around:**
- Paging on pool saturation adds pages. It only helps if the p99 flapping is fixed and the silencing rule changes at the same time.
- Gating every bot PR brings February's review load back. Only the risky bumps should go to a person.
- A faster rollback path brings back the risk of migration corruption, unless rollbacks that touch migrations keep their gate.
- The Forest Service guide warns that recommendations can "add complexity to the workplace, which has the paradoxical effect of increasing risk" [V] (`lfuo-learning-review-guide-2024`, Concept 14). That's another reason to keep the list short.

## Phase 8: The highest-leverage point

This step follows Goldratt's Theory of Constraints: of all the contributing factors, find the one where fixing it would do the most.

**Proposed constraint: the path from "an alert fires" to "a person declares and diagnoses" doesn't work.** Two things block it:
- **Noise is tolerated.** The silencing rule, the unwatched channel and the clean-up deferred twice all come from accepting noise as normal.
- **Declaring is discouraged.** The incidents-per-team dashboard means teams wait until they're sure.

**Type:** a *policy* constraint (the silencing rule, the dashboard) resting on a *paradigm*, a belief about how things should be: "noise is normal" and "declare only when sure".

**Why this one:**
- It's the chain that lost the cut-off.
- It's the second time an AAR has found it.
- It would catch *any* future fault, not only changed library defaults.

**Strongest alternative: prevention.** About 60 bot PRs a week auto-merge with nothing checking for default changes, so the trigger keeps coming. Fixing detection only shortens incidents; it doesn't stop them.

**Stress test, and an open question that could overturn this choice: when did the DBA's vendor meeting start?** Suppose detection had been perfect at 16:22. If the DBA was unavailable from before about 16:30 until 18:30, rollback would still have waited until after the cut-off. In that case detection alone wouldn't have saved it, and **recovery is jointly binding**. The meeting start time decides which reading is right.

**What would show this choice is wrong:** if a deploy with good alerting and fast declaration still misses its window because of approval waits or prevention gaps.

## Phase 9: Actions

Three actions, one per chain, plus one decision for leadership. The constraint comes first.

**Proposed dates assume today is 28 October.** Change them freely.

### Short-term (2–3 weeks)

| # | Action | Owner | Checked by | Deadline | Done when | Urgency |
|---|---|---|---|---|---|---|
| **1** | **Detection (the constraint):** Make `db-pool-saturation` on payments page on-call. Rewrite the deploy-window rule so pages tied to the service just deployed are **investigated, not silenced**. Fix the p99 flapping that made silencing reasonable. | *One named person in SRE, TBD* | *Payments engineering lead, TBD* | 18 Nov | Pool exhaustion injected in staging, during a deploy window, pages on-call within 5 min and isn't suppressed. The p99 page flaps 2 times a week or fewer for 4 weeks. | **High.** Every deploy opens a 2-hour window where a deploy-caused fault gets silenced. Nothing has changed since INC-2104. |
| **2** | **Prevention:** payments-api sets its pool size explicitly. Staging stops overriding the pool and uses production's effective config. Bot bumps of internal libraries whose changelogs flag a **default or behaviour change** go to a person for review; all other bumps keep auto-merging. | *One named person (payments or platform), TBD* | *`platform-commons` maintainer, TBD* | 18 Nov | payments-api's pool is set in its own config. Staging and prod configs match for the pool. A test bump with a flagged default change is held for review. | **High.** About 60 bot PRs a week auto-merge, and nothing would catch the next default change. |

### Longer-term

| # | Action | Owner | Checked by | Target | Point (of the five) | Urgency |
|---|---|---|---|---|---|---|
| **3** | **Recovery:** Rollbacks that don't touch migrations go back to one-click or pre-approved. Rollbacks that do touch migrations keep the DBA gate, with a defined way to interrupt the DBA and a target approval time. | *One named person (DBA lead or platform), TBD* | *Incident commander rota lead, TBD* | 9 Dec | How work moves; who we hire, grow and staff | **Medium.** Any bad deploy needs it, and two DBAs for nine teams makes waiting likely. It didn't decide *this* cut-off unless the DBA meeting started early. |
| **4** | **Leadership request (this workflow's term, not a library method):** Stop the incidents-per-team dashboard from discouraging declaring. Pair the 5-minute acknowledge target with a time-to-declare or time-to-diagnose measure. Run it as an experiment with a hypothesis and a check date (`org-topologies-primer-2025`, Concept 8). | **Decider:** *probably your VP* | *You, TBD* | Decision by 18 Nov; review after one quarter | What gets measured and rewarded | **High.** It delayed the Sev1 on this incident, and every team is still working under it. |

**Explicitly not doing:**
- Adding more alerts to #payments-alerts (it would add noise).
- Retraining the on-call. The DOE handbook matches the fix to the type of error, and he followed the rule, so the rule is what needs changing (`doe-hpi-handbook-vol1`, Concept 3).
- Taking anyone off the rota.

### Do the actions target the constraint?

| Action | Targets the constraint? | Why |
|---|---|---|
| #1 Detection | **Yes** | Directly fixes alert-to-person |
| #4 Declaration norm | **Yes** | Directly fixes person-to-declaration |
| #2 Prevention | No, supporting | Cuts how often incidents start; doesn't help detect them |
| #3 Recovery | Partly | Becomes joint if the DBA meeting started early |

### Built to last longer than INC-2104's action

The DOE handbook prefers engineered controls to administrative ones: things built into the system over rules people have to remember (`doe-hpi-handbook-vol1`, Concept 7). Actions #1 to #3 change configuration and policy; none relies on someone remembering. Each will have one named person as owner, which is the difference from "SRE team, no ticket". The Liberating Structures handbook's closing question is "Who will do what when next?", asked before anyone leaves (route, Phase 4). The aim is to **build these actions with the people who'll carry them out**, not hand them over finished.

There's **no issue tracker connected to this session**, so I can't create tickets. I can write ticket descriptions for you to paste in: context, the contributing factor, success criteria and urgency for each.

## To close the AAR (Phase 10)

1. **The constraint:** Do you agree it's detection, with the DBA meeting start time as the open question that could change it?
2. **Owners, checkers and dates** for #1–3, and confirmation of who decides #4.
3. **Ticket drafts now, or with the final document?**

Once you've checked the remaining facts (date, attendees, DBA meeting start, INC-2104 details, the silencing rule's history, the enterprise launch status), I'll put together the full AAR document, `aar-inc-2291-{date}`. Every gap still open will be listed in its Data-Quality Notes, along with the evidence links still needed.

[Participant]
Detection as the constraint sounds plausible to me, but I still don't know when the DBA's vendor meeting started, so I can't rule out recovery. I'd have to check before putting names, checkers or dates against #1 to #3, and before saying who decides #4. Ticket drafts can come with the final document.

[Facilitator]
Here's the AAR as a **draft**. Everything you're still checking is marked inline and collected in the Data-Quality Notes. The tickets follow at the end. You can file it now and finalise it once the open facts and owners are in.

---

# After-Action Review: INC-2291, payroll submission outage after `platform-commons` 3.5 bump

`aar-inc-2291-2026-09-29` · **Status: DRAFT, not yet closed** (owners, checkers and dates pending)

**Incident:** INC-2291
**Date of incident:** Tuesday 29 September 2026 *(to be confirmed)*
**Priority:** Sev1 (team's classification)
**Author:** *TBD*
**Facilitator:** *TBD*
**Attendees:** *TBD.* Proposed: payments engineering, on-call engineer, SRE lead, `platform-commons` maintainers, owner of the dependency-bot settings, DBA, support lead, finance ops.

---

## Executive summary

A dependency bot auto-merged `platform-commons` 3.5, which cut the default DB connection pool from 50 to 20. payments-api never set its own pool size, so it took the new default, and it exhausted its pool under payroll load from 16:14 UTC.

An alert that correctly named the cause fired at 16:22, but it went to a Slack channel that gets about 220 alerts a week and isn't watched live. The symptom page that did reach on-call was silenced under the runbook's deploy-window rule. It had flapped 14 times that week.

The incident was declared at 17:55, after support escalated 41 tickets, and the cause was found at 18:01, one minute after the 18:00 bank cut-off. Rollback then waited 28 minutes for DBA approval.

**Impact:**
- 1,180 employer accounts saw failures.
- 37 payroll runs missed the cut-off.
- 22 were recovered that evening at the cost of a bank late-processing fee.
- 15 runs (about 3,800 employees) were paid a day late.

**Key learning:** each safeguard was set up sensibly for its own purpose, and together they left the riskiest window, just after a deploy, as the least watched. This is the second review to find alert noise as a contributor. The first one's action had no single owner and wasn't done.

---

## Timeline (UTC)

| Time | Event | Evidence |
|---|---|---|
| ~2024 | `db-pool-saturation` created as a warning that only posts to #payments-alerts | *Needed: alert config and history* |
| Unknown | payments-api relies on the library's default pool size | *Needed: config history* |
| Feb 2026 | SRE lead proposes an alert clean-up; deferred for the Q3 enterprise-tier launch | *Needed: proposal or decision record* |
| Feb 2026 | Minor and patch bumps of internal libraries set to auto-merge on green CI, to cut review load (~60 bot PRs a week) | *Needed: repo settings, decision record* |
| Mar 2026 | One-click rollback switched off after one corrupted a migration; manual rollbacks need DBA approval | *Needed: decision record* |
| Jun 2026 | INC-2104 (smaller latency incident) AAR assigns "tune noisy alerts" to "SRE team"; no ticket; not done | *Needed: INC-2104 AAR link* |
| Unknown | Runbook rule: "silence known flapping alerts for the deploy window (2 h)" | *Needed: runbook history* |
| Unknown | `platform-commons` 3.5 released: default pool 50 → 20, "safer defaults for small services" (changelog line 40 of 52) | *Needed: release link* |
| Before 16:05 | Bot PR bumping 3.4 → 3.5 auto-merges on green CI. Load tests run only on major bumps; staging sets the pool to 50 explicitly | *Needed: PR URL, CI run* |
| 16:05 | payments-api v4.18 deployed *(automatic or manual: unknown)* | *Needed: pipeline run* |
| 16:14 | First failed submissions: "connection pool exhausted" | *Needed: logs* |
| 16:22 | `db-pool-saturation` (warning) posts to #payments-alerts; no page; no one declares | *Needed: Slack permalink* |
| 16:31 | On-call paged: "payments p99 latency high" (14th flap that week, all around deploys) | *Needed: alert ID* |
| 16:33 | On-call acknowledges (within the 5-minute target) and silences for 2 h, as the runbook says; he's also working an urgent enterprise data export flagged by account management | *Needed: page log* |
| 17:10 | First support tickets | *Needed: ticket IDs* |
| 17:48 | Support lead escalates in #incidents with ticket count (41), customer list and first-seen time | *Needed: Slack permalink* |
| 17:55 | Sev1 declared | *Needed: incident record* |
| 18:00 | Bank cut-off passes | — |
| 18:01 | Payments engineer finds pool exhaustion in logs | *Needed: Slack permalink* |
| 18:05 | Decision to roll back; DBA on shift in a vendor meeting until 18:30 *(start time unknown)* | *Needed: Slack permalink* |
| 18:33 | DBA approves | *Needed: Slack permalink* |
| 18:46 | Rollback complete | *Needed: pipeline run* |
| 19:20 | Queued submissions drained | *Needed: metrics* |
| Evening | Finance ops pays the bank's late fee; 22 of 37 runs processed | *Needed: finance ops record* |
| Next day | 15 runs (~3,800 employees) paid a day late | *Needed: finance ops record* |

---

## Problem assessment

The incident splits into two kinds of problem (in the sense of Snowden's Cynefin framework):

- **Technical fault: complicated.** One cause, knowable and reproducible once staging matches production.
- **The nearly two hours before anyone saw it: complex.** It came from alert routing, a runbook rule, competing work, test policy, measurement and rollback policy interacting.

---

## Key decisions, as they looked at the time

| Decision | When | What was known | What was missing | Pressure |
|---|---|---|---|---|
| Auto-merge minor and patch bumps | Feb | ~60 bot PRs a week; minor and patch versions are meant to be compatible | That a library would change a runtime default in a minor; that load tests and staging couldn't show it | Review load |
| Ship 50 → 20 default in 3.5 | *?* | Small services were over-provisioned | Which services relied on the default *(library team's account needed)* | *?* |
| Silence the p99 page | 16:33 | 14 flaps that week around deploys; runbook rule; 5-minute acknowledge target | That `db-pool-saturation` had fired *(and whether he knew payments-api had just deployed)* | Urgent enterprise export *(deadline and priority unclear)* |
| Escalate to #incidents | 17:48 | 41 tickets, customers, first-seen time | *?* | Dashboard norm: declare only when sure |
| Wait for DBA approval | 18:05–18:33 | Policy since March; cut-off already passed | DBA availability; no backup (two DBAs for nine teams) | 1,180 accounts failing |
| Switch off one-click rollback | Mar | A rollback had corrupted a migration | How often a fast rollback would be needed, and who'd be free to approve | Protecting data |

---

## Contributing-factor analysis

### Chain A: Prevention. How the change reached production unseen
1. Pool dropped from 50 to 20 and was exhausted under payroll load.
2. payments-api took the library default; 3.5 changed it.
3. Three checks all missed it: auto-merge on green CI, load tests only on major bumps, and a staging pool override of 50.
4. All three assume that minor and patch bumps don't change behaviour. The library shipped a behaviour change in a minor release as "safer defaults".
5. *Hypothesis:* review load of 60 bot PRs a week was solved by removing review rather than by sorting bumps by risk. Nobody owns the contract between `platform-commons` and the services that use it.

### Chain B: Detection. Why two signals fired and neither led to the cause (16:14 → 18:01)
1. The alert naming the cause went to an unwatched channel; the symptom page was silenced.
2. The channel gets ~220 alerts a week, mostly auto-resolving. The pool alert has been Slack-only since it was created.
3. Silencing followed the runbook rule, after 14 flaps that week, while the on-call was carrying urgent enterprise work.
4. Noise was handled by downgrading, rerouting and silencing alerts, not by fixing them. The result is that the 2 hours after a deploy are the least monitored.
5. The fix was deferred for the Q3 launch (February), then assigned with no single owner (June, INC-2104). The incidents-per-team dashboard discourages declaring early, and the 5-minute acknowledge target rewards acknowledging, not diagnosing.

### Chain C: Recovery. Why rollback took 41 minutes
1. 28 minutes waiting for DBA approval.
2. One-click rollback has been off since March.
3. The DBA was in a vendor meeting; two DBAs serve nine teams; it's unknown whether anyone tried to interrupt.
4. *Hypothesis:* the March fix gated *all* rollbacks, with no emergency route and no target approval time.

**How the chains relate:**
- A was **necessary**: without the pool change there's no incident.
- B **interacted** with A and **lost the cut-off**.
- C **interacted** with A and lengthened the impact. It becomes **jointly binding** if the DBA's meeting started before about 16:30.

### Mapping to the five points

The five points are a way of checking where in the organisation a problem comes from; they follow Galbraith's Star Model, put in plain words.

| Point | Implicated? | Chains | Evidence |
|---|---|---|---|
| What we optimise for | Yes | A, B | Review load over checking bumps; Q3 enterprise launch over alert clean-up; enterprise export on the on-call's plate |
| Who owns what | Yes, likely | A, B, C | Library–consumer contract; alert quality ("SRE team" as owner); rollback approval |
| How work moves | Yes | A, B, C | Auto-merge, major-only load tests, staging override, deploy-window rule, rollback gate |
| What gets measured and rewarded | Yes | B | Incidents-per-team dashboard delays declaring; the 5-minute acknowledge target was met while the outage continued. *Library and payments team measures unknown.* |
| Who we hire, grow and staff | Yes | B, C | Two DBAs for nine teams; a fairly new on-call carrying interrupt work |

**Highest-leverage point (provisional):** detection. The path from an alert firing to a person declaring and diagnosing doesn't work, because noise is tolerated and early declaring is discouraged. **Type:** a policy constraint, resting on a belief ("noise is normal", "declare only when sure"). **Open question that could overturn it:** if the DBA was unavailable from before about 16:30, recovery binds jointly with detection.

---

## Additional analysis

**Drift:**
- **Yes, for alert noise.** Clean-up deferred in February, an unowned AAR action in June, and 14 flaps a week treated as "known flapping" by September.
- **The February auto-merge** was a single deliberate loosening, not gradual drift.
- **The pool alert's routing and payments-api's reliance on the default** look like design gaps, pending the firing history.

**Handoffs:** six teams were involved. The delays sat at the boundaries: library → payments, alert → person, support → engineering, decision → DBA. Rough ratio of time waiting to time working: about **5.6 to 1** (about 129 of 152 minutes undetected or waiting). Each choice made sense for its owner, and the whole system performed worse (`org-topologies-primer-2025`, Concept 3).

**Just culture:** one action reviewed, the on-call's silencing of the p99 page, using the NHS decision tree.
- No deliberate harm.
- No health indicators reported; to be confirmed through his manager.
- **Foresight test:** an agreed protocol existed, was workable and was in routine use, and he **did not depart from it**. That leads to **Recommendation D**.
- **Substitution test:** peers would have done the same after 14 flaps. That leads to **Recommendation E**.

Both outcomes say action singling out the individual is unlikely to be appropriate. On the DOE culpability spectrum this sits at the **organisation-induced** end. There was **no human merge to review**, because the bot auto-merged the PR. The tree can be re-run if new facts emerge (`nhs-just-culture-guide`, Concept 10).

**Forward accountability:** owners for actions 1–3 and the decision-maker for action 4, TBD.

**Patterns that fixes can fall into:**
- **Shifting the burden** (a workaround eased the pressure while the real fix was put off): strong fit, from silencing and rerouting while the clean-up was deferred.
- **Fixes that fail** (a fix solved one problem and created another): likely, from the March rollback gate. Adding alerts to the noisy channel would be another instance.
- **Limits to growth** (something kept growing until it hit a limit): possible, from bot PR volume against review capacity.

---

## What went well

- **Support lead:** the escalation came with ticket count, customer list and first-seen time; Sev1 followed 7 minutes later. *What made it that good: TBD.*
- **Payments engineer:** diagnosed the cause 6 minutes after the Sev1.
- **Finance ops:** recovered 22 of 37 payroll runs that evening, which cut the number of employees paid late.
- **SRE lead:** proposed the alert clean-up in February, eight months before this incident.

---

## Action items

### Short-term

| # | Action | Owner | Checked by | Deadline | Done when | Urgency | Ticket |
|---|---|---|---|---|---|---|---|
| 1 | **Detection:** page on payments `db-pool-saturation`; rewrite the deploy-window rule so pages tied to the just-deployed service are investigated, not silenced; fix the p99 flapping | *TBD (one person)* | *TBD* | *TBD (proposed 18 Nov)* | Injected pool exhaustion in staging during a deploy window pages within 5 min, unsuppressed; p99 page flaps ≤2 a week for 4 weeks | **High** | *TBD* |
| 2 | **Prevention:** payments-api sets its pool size explicitly; staging uses production's effective pool config; bumps flagging a default or behaviour change go to human review; others keep auto-merging | *TBD (one person)* | *TBD* | *TBD (proposed 18 Nov)* | Pool set in payments-api config; staging and prod match; a test flagged bump is held for review | **High** | *TBD* |

### Longer-term

| # | Action | Owner | Checked by | Target | Point (of the five) | Urgency | Ticket |
|---|---|---|---|---|---|---|---|
| 3 | **Recovery:** rollbacks that don't touch migrations go back to one-click or pre-approved; rollbacks that do touch migrations keep the DBA gate, with an interrupt path and a target approval time | *TBD (one person)* | *TBD* | *TBD (proposed 9 Dec)* | How work moves; who we hire, grow and staff | **Medium** | *TBD* |
| 4 | **Leadership request:** stop the incidents-per-team dashboard from discouraging declaring; pair the acknowledge target with a time-to-declare or time-to-diagnose measure; run as an experiment with a review date | **Decider:** *TBD* | *TBD* | *TBD (proposed decision by 18 Nov)* | What gets measured and rewarded | **High** | *TBD* |

### Urgency summary

| Risk | Actions | Urgency | Rationale |
|---|---|---|---|
| A deploy-caused fault is silenced during the deploy window | 1, 4 | High | Every deploy opens the window, and nothing has changed since INC-2104 |
| The next library default change reaches production unseen | 2 | High | About 60 bot PRs a week auto-merge with no check for default changes |
| Rollback waits on an unavailable approver | 3 | Medium | Any bad deploy needs it, and two DBAs for nine teams makes waiting likely |

### Does each action target the constraint?

| Action | Targets detection? | Why |
|---|---|---|
| 1 | Yes | Fixes the path from alert to person |
| 4 | Yes | Fixes the path from person to declaration |
| 2 | No (supporting) | Reduces how often incidents start |
| 3 | Partly | Becomes joint if the DBA meeting started early |

**Not doing:**
- Adding alerts to #payments-alerts (adds noise).
- Retraining the on-call (he followed the rule).
- Changing anyone's rota.

---

## Closing the loop

- **No action closes on the owner's word.** Someone other than the owner checks it worked (`doe-hpi-handbook-vol1`, via route).
- **Report back in person** to the on-call, the support lead and the SRE lead on what changed because of what they told us (`doe-hpi-handbook-vol2`, via route).
- **Update the runbook's deploy-window rule** as part of action 1, and write the rule's purpose into the step (`tc-25-20-army-aar`, `mcdp1-warfighting`, via route).
- **Check again at 30 and 90 days, and plan for attention to fade.** The Columbia report expects post-incident energy to dissipate (`caib-report-vol1`, Concept 12). At 90 days, specifically check whether this AAR's actions avoided INC-2104's fate.
- **Share the incident beyond payments as a lesson for other teams.** Any service using `platform-commons` defaults is exposed to the same change.

---

## Methodology note

- **Backward timeline (doe-hpi-handbook-vol1, Anatomy of an Event):** worked from the cut-off loss back to the February and March policy decisions.
- **Cynefin (Snowden):** classified the pool fault as complicated and the two hours before anyone saw it as complex.
- **Local rationality (Dekker, via doe-hpi-handbook-vol1 [BT]):** reconstructed why silencing a 14-times-flapping page under the runbook made sense.
- **Schedule pressure (caib-report-vol1):** traced the Q3 enterprise launch to the deferred clean-up and to the on-call's competing work.
- **Five Whys (open-practice-library):** three chains; the DBA chain was pushed past "not enough people" to the process.
- **The five points (after Galbraith's Star Model):** confirmed all five are implicated; the dashboard and acknowledge target filled "measured and rewarded".
- **Drift (caib-report-vol1):** separated drifted alert noise from the deliberate auto-merge loosening and from design gaps.
- **Handoff analysis (org-topologies-primer-2025):** found about 85% of the outage time sitting at team boundaries.
- **NHS Just Culture guide:** one action through the tree, ending at D and E.
- **System archetypes (ssdl-systems-thinking-foundations):** shifting the burden on alert noise; fixes that fail on the rollback gate.
- **Theory of Constraints (Goldratt):** detection proposed as the constraint, with the DBA meeting start as the test that could overturn it.

---

## Data-Quality Notes

- **Paste-mode reconstruction.** No tracker, chat, code-host or alerting tool was connected. Every fact comes from the facilitator's account and interviews. **No timeline entry has an evidence link yet.**
- **Accounts heard:** on-call engineer, DBA, support lead, payments engineer, all via the facilitator. **Not yet heard:** `platform-commons` maintainers, whoever made the February auto-merge decision, owner of payments-api config. No meeting transcript.
- **Open facts:**
  - incident date
  - attendees
  - whether the 16:05 deploy was automatic
  - `db-pool-saturation` firing history
  - who wrote the deploy-window rule, and when
  - **when the DBA's vendor meeting started** (decides whether detection is the sole constraint)
  - whether anyone tried to interrupt the DBA
  - why support escalated at 17:48, and what made the escalation good
  - the on-call's understanding of the export deadline and priority
  - why `platform-commons` made the "safer defaults" change
  - whether the library knows who relies on its defaults
  - payments-api deploy frequency
  - precedent before February
  - INC-2104 details
  - enterprise-tier launch status
  - whether the SRE lead's February proposal is on file
  - library and payments team measures
- **Redaction:** the 17:48 customer list was not shared; please keep it out of the filed document.
- **Health:** no indicators reported; to be confirmed through the on-call's manager, not assumed.

---

## Ticket drafts (paste into your tracker)

**[AAR-INC-2291] Page on payments pool saturation; stop silencing deploy-caused pages**
> **Context:** From the AAR for INC-2291 (payroll outage, 29 Sep). `db-pool-saturation` fired at 16:22 with the correct diagnosis but only posts to #payments-alerts (~220 alerts/week, unwatched). The p99 page was silenced under the deploy-window rule after flapping 14×/week. The noisy-alert action from INC-2104 (June) had no single owner and wasn't done.
> **Contributing factor:** Chain B, detection (the constraint). Five points: how work moves; who owns what.
> **Success criteria:**
> - [ ] Payments `db-pool-saturation` pages on-call
> - [ ] Deploy-window rule rewritten: pages tied to the just-deployed service are investigated, not silenced
> - [ ] Injected pool exhaustion in staging during a deploy window pages within 5 min, unsuppressed
> - [ ] p99 page flaps ≤2/week for 4 consecutive weeks
>
> **Urgency:** High. Every deploy opens a 2-hour window where a deploy-caused fault gets silenced, and nothing has changed since INC-2104.
> **Owner:** *one named person* · **Checked by:** *TBD* · **AAR:** *link*

**[AAR-INC-2291] Stop internal library default changes reaching production unseen**
> **Context:** `platform-commons` 3.5 cut the default pool from 50 to 20 (changelog line 40/52). The bot PR auto-merged on green CI (policy since Feb); load tests run only on major bumps; staging overrides the pool to 50; payments-api never set its own pool size.
> **Contributing factor:** Chain A, prevention. Five points: how work moves; who owns what.
> **Success criteria:**
> - [ ] payments-api sets its pool size explicitly
> - [ ] Staging uses production's effective pool config
> - [ ] Bot bumps whose changelog flags a default or behaviour change are held for human review; other bumps keep auto-merging
>
> **Urgency:** High. About 60 bot PRs a week auto-merge with no check for default changes.
> **Owner:** *one named person* · **Checked by:** *TBD* · **AAR:** *link*

**[AAR-INC-2291] Emergency rollback path that doesn't wait on one DBA**
> **Context:** Rollback was decided at 18:05 and approved at 18:33. One-click rollback has been off since March (migration corruption); two DBAs serve nine teams; the DBA on shift was in a vendor meeting.
> **Contributing factor:** Chain C, recovery. Five points: how work moves; who we hire, grow and staff.
> **Success criteria:**
> - [ ] Rollbacks that don't touch migrations are one-click or pre-approved
> - [ ] Rollbacks that touch migrations keep the DBA gate, with a defined interrupt path and target approval time
> - [ ] Tested on a non-production rollback of each type
>
> **Urgency:** Medium. Any bad deploy needs it, and approver scarcity makes waiting likely. Raise to High if the DBA's meeting started before ~16:30.
> **Owner:** *one named person* · **Checked by:** *TBD* · **AAR:** *link*

**[AAR-INC-2291] Leadership request: make early declaration safe**
> **Context:** Nobody declared on the 16:22 warning. Sev1 came at 17:55, after 41 support tickets. The incidents-per-team dashboard leads teams to wait until they're sure. The 5-minute acknowledge target was met (2 min) while the outage continued.
> **Contributing factor:** Chain B, detection (the constraint). Five points: what gets measured and rewarded.
> **Success criteria:**
> - [ ] Decision made on how declared incidents are counted on the dashboard
> - [ ] Acknowledge target paired with a time-to-declare or time-to-diagnose measure
> - [ ] Run as an experiment: stated hypothesis, measure, review after one quarter
>
> **Urgency:** High. It delayed this Sev1, and every team still works under it.
> **Decider:** *TBD* · **Checked by:** *TBD* · **AAR:** *link*

---

To close the AAR, I need:
1. One named owner, a checker and a date for actions 1–3.
2. Who decides action 4.
3. The DBA meeting start time.
4. Evidence links for the timeline.

The DBA meeting start time is the fact most likely to change the analysis. If it was before about 16:30, action 3 moves to High and recovery joins detection as a constraint. Send me those and I'll produce the final version.

[Participant]
Thanks, this is really helpful. I'll check the DBA meeting time, the owners and the evidence links and come back to you.
