[Facilitator]
I've written a draft AAR at `INC-2291-AAR-draft.md` covering the timeline, contributing factors, action items and open questions. Before you run it, your timeline argues against the framing you've been given.

## What the timeline shows

- **The alert that named the cause fired at 16:22 and paged no one.** `db-pool-saturation` was set to warning and only posted to Slack. If it had paged, on-call would have had the diagnosis 8 minutes into the outage and about 1h40m before the bank cut-off.
- **The on-call was paged for a symptom, not the cause.** The latency alert didn't mention the pool or the deploy. The tooling allowed a 2-hour silence with no reason required, and nothing knew that 2 hours ran past the cut-off.
- **Nothing caught the deploy.** Failures started 9 minutes after it went out. There was no canary, no automatic rollback and no deploy marker. It also shipped less than 2 hours before a hard cut-off.
- **A breaking change came in as a minor version of an internal library.** Reading the changelog was the only safeguard. The PR also had a reviewer, and staging didn't catch it either.
- **Customers noticed before engineering did.** Support took 38 minutes to escalate, and escalated through Slack, not a page.
- **The rollback waited 28 minutes for DBA approval** during a Sev1.

If you removed both people from the story, most of this would still happen. Any on-call could get that latency page, and any dev could merge that bump.

## Your VP and "an individual by Friday"

Don't refuse, and don't hand over a name the evidence doesn't support. Here's what I'd do:

1. **Run each of the two decisions through a fair test.** The NHS Just Culture Guide in this folder is built for exactly this. It asks about one action at a time:
   - Was there a protocol that was workable and normally followed, and did the person knowingly break it?
   - The substitution test: would a peer with similar experience have done the same in the same situation?

   Check two facts before Friday:
   - How often has "p99 latency high" fired in the last 90 days, and how often did it need action? If it's noisy and people routinely silence it, the silence is normal practice, not personal negligence.
   - Do people on that team usually read changelogs for internal minor bumps, and did the reviewer?

   If the facts point to the individuals, you'll have evidence. If they don't, you'll be able to show the VP why.
2. **Give the VP accountability they can track.** Each of the 11 action items gets a named owner and a due date. That's individual accountability tied to the fixes.
3. **Name the cost of picking a person.** If someone is blamed, the next on-call won't silence an alert, but they also won't tell you what they did. Every future AAR gets less honest. And the five gaps above stay open, so this happens again.

Suggested line for the VP: *"I'll bring named owners for every fix by Friday. On the two individual decisions, I'm checking whether they broke an established practice or followed one. If it's the first, I'll handle it with their manager. If it's the second, blaming them leaves the gap open."*

## Running the review (about 90 min)

1. **Before the meeting (Wed/Thu):** close the [TBC] items using records, not memory, because the incident was a month ago. Sources are PagerDuty silence metadata and alert history, the Slack exports, the deploy log, the v4.18 PR and its reviewers, and the platform-commons 3.5 diff and changelog. Talk to the on-call, the dev, the support lead and the DBA one-on-one first so nobody is surprised in the room.
2. **Ask "what did you see, what did you expect" questions, not "why didn't you".** For example, "When the page came in, what did the dashboard show you? What did you expect would happen after silencing?"
3. **Agenda,** using the Army AAR format from TC 25-20 in your folder:
   - What was supposed to happen (10 min)
   - What happened: walk the timeline (25 min)
   - Why the difference: contributing factors (30 min)
   - What to keep and what to fix, assigning owners in the room (25 min)

Before Friday I still need to know what actually changed in platform-commons 3.5 and how many payrolls missed the cut-off. The draft leaves both as placeholders.

[Participant]
Can we just add more alerts on the DB pool metrics and call it done? On your two placeholders: platform-commons 3.5 lowered the default DB connection pool from 50 to 20, billed as 'safer defaults for small services'. And 37 payroll runs missed the 18:00 cut-off.

[Facilitator]
No. More pool alerts wouldn't have changed Tuesday, because a pool alert already fired. `db-pool-saturation` went off at 16:22 and named the exact cause, but it was set to warning and only posted to Slack, so nobody was paged. Adding more alerts with the same routing just adds noise, and alert noise is the likely reason the latency page got silenced.

Your new facts also make the problem bigger than payments-api.

**Other services may still be exposed.** platform-commons 3.5 lowered the default connection pool from 50 to 20, and payments-api was relying on the default. Any other service that has taken 3.5 and doesn't set its own pool size is now capped at 20 connections. Checking those services is more urgent than finishing the AAR. payments-api will also hit this again if it re-upgrades without setting its pool size explicitly.

**This weakens the case against the dev.** The changelog called the change "safer defaults for small services." Someone who read it carefully could reasonably have decided it didn't apply to them or was harmless. So reading it probably wouldn't have prevented the outage. The deeper problem is that a cut to a production capacity default shipped as a minor version, described as a safety improvement.

**Minimum before you call it done:**
1. **Now:** find every service on platform-commons 3.5 or later that relies on the default pool size, and set it explicitly wherever peak usage is near 20.
2. Set payments-api's pool size explicitly before it retries the upgrade.
3. Make the existing `db-pool-saturation` alert page on-call.
4. Limit how long payments alerts can be silenced, and don't allow a silence to run past the bank cut-off without the incident commander's approval.

Also give the platform-commons team a policy action: changes to capacity, timeout or retry defaults ship as major versions and are flagged as breaking. They should also decide whether to revert the 3.5 pool default. Without that, the next library default change causes the same incident in a different service. The canary rollout, Support paging, rollback pre-approval and cut-off-aware severity can follow later with owners and dates. Without them, 37 missed payroll runs will get a smaller fix than they justify.

I've updated the draft with:
- the pool change and the 37 missed runs in the summary and timeline
- the "safer defaults" wording and the risk to other services in the library section
- the four items above at the top of the action list

The remaining open questions are mostly about the alerting history and the silence. Answering them before Friday is still the way to give your VP a straight answer about the on-call.

[Participant]
Okay.

[Facilitator]
I'd do these in order:

1. **Today:** run the check for other services on platform-commons 3.5 or later. It's the only item with live risk.
2. **Before Thursday:** get the alert-history data. That means how often "p99 latency high" fired in the last 90 days, how often it needed action, and whether silencing it is normal on that rotation. It decides what you can honestly tell your VP about the on-call.
3. **Friday:** take the action list to your VP with a named owner and a date on each item.

The draft is at `INC-2291-AAR-draft.md`. When you have the alert history or the list of other services on 3.5, send it over and I'll add it to the draft. I can also help write the note to your VP or the interview questions.

[Participant]
Fine. I'll get someone on the services check today and pull the 90-day alert numbers. I don't have those to hand.

[Facilitator]
Good. Here's exactly what to ask for, so neither request has to come back for more detail.

**Services check:**
- Every service running platform-commons 3.5 or later
- For each one, whether it sets its own pool size in config or uses the default
- Its peak connection use over the last 30 days

Anything that uses the default and peaks near 20 needs the pool size set explicitly now. The same audit also covers anything that upgrades later.

**Alert numbers (last 90 days) for "payments p99 latency high":**
- Times it fired
- How many of those led to real action (a rollback, fix or incident) and how many resolved on their own
- How many were silenced or acked with no follow-up, and by how many different people

The last point matters most. If several people routinely silence it, Tuesday's silence was normal practice for the team, not one person's failing. If it's rare and usually needs action, that's a different conversation. Pull the same three numbers for `db-pool-saturation` too: how often it fired and whether anyone acted, which shows whether it's ever been watched.

When you have the numbers, send them over and I'll update section CF2 and the note to your VP.

[Participant]
Got it. I'll pass both requests on as written and send you the numbers when they come back.

[Facilitator]
Sounds good. When the numbers come back, I'll update the alerting and library sections of the draft and write the note to your VP.

If the services check turns up anything that uses the default and is running near 20 connections, don't wait for the AAR. Set that service's pool size explicitly straight away.

[Participant]
Okay.

[Facilitator]
Okay. Send the numbers over when they come in.

[Participant]
Will do.

[Facilitator]
Thanks.

[Participant]
Okay.

[Facilitator]
Okay, talk then.

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
Nothing else is needed for now. The draft is saved, and I'll pick it up when you send the numbers.

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
If you meant to send something else, only "Okay" is coming through. Otherwise, there's nothing to do until the numbers arrive.

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
👍

[Participant]
I'm out of time. Please write up the AAR with what we have.

[Facilitator]
I've written the AAR to `INC-2291-AAR.md` and left the earlier draft as it was. It uses only the facts we've established.

**How I handled the gaps:**
- The services check and the 90-day alert numbers are listed as outstanding inputs in section 7. The review says plainly that they're still to come and doesn't guess at them.
- The Owner and Due columns in the action table are blank because I don't know who should own each item. That's the one thing to fill in before Friday.
- Section 8 covers the two individual decisions:
  - **The dev:** the evidence doesn't support treating the merge as a cause. The changelog called the change "safer defaults for small services," so reading it probably wouldn't have prevented the outage.
  - **The on-call:** no judgement until the alert numbers come back. If silencing that alert turns out to have been rare, their manager follows up with them directly, outside the review.

**A note you can send your VP:**

> INC-2291 AAR attached. 37 payroll runs missed the 18:00 cut-off. The cause was a platform-commons update that cut the default DB pool from 50 to 20, shipped as a minor version and described as a safety improvement. The alert that named the cause went to Slack instead of paging anyone. Accountability is in section 6: each action will have a named owner and due date, and items 0–3 must be done before we close the incident. We're checking whether other services are exposed to the same pool change. The on-call's silence is still being assessed against 90-day alert history; if it was outside normal practice, their manager will handle it directly.

When the numbers come back, send them and I'll update sections 4, 7 and 8.
