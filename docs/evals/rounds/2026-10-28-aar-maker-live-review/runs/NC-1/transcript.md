[Facilitator]
I can help you run it, but I'd push back on one part first: **don't let the AAR produce a name for your VP.** Your own timeline points to gaps in the system, not one person's mistake. Below are how I'd handle the VP, what the timeline shows, and a plan for running the session.

**Check the date first:** 29 September was four weeks ago. Yesterday (27 Oct) was also a Tuesday. If you meant yesterday, fix the date before anything goes out. If it really was a month ago, pull logs, Slack history and alert history now, before retention deletes them.

---

## 1. The VP and the "individual to hold accountable" ask

Two people have already been named: the on-call engineer and the dev who merged the upgrade. Here's what the timeline says about each:

- **The dev and the changelog.** An internal library went up one minor version (3.4 → 3.5) and broke connection pooling in production within 9 minutes. That means:
  - the library shipped a breaking change as a minor version
  - review didn't flag it
  - no canary or staged rollout caught it
  - staging didn't reproduce it

  Reading the changelog is a weak safety net. We don't yet know whether the changelog even made the risk obvious.
- **The on-call and the silence.** This is the biggest lost time window (16:33 → 17:48, about 75 minutes), so don't gloss over it. But consider what they actually had:
  - They were paged for a symptom (latency), not the cause.
  - The alert that named the cause (`db-pool-saturation`) was set to "warning" and only posted to Slack.
  - Nothing in their view linked the problem to a deploy 26 minutes earlier.
  - The tooling let them silence a payments alert for 2 hours without a second look.

  If that latency alert is usually noise, silencing it was a reasonable call. The next on-call would do the same thing.

Here's a script for the VP:

> "Accountability here means named owners with dates for each fix, and I'll own the overall remediation. If we pin this on the on-call or the dev, the same gaps are still there for whoever's next. People also stop telling us the truth in reviews, which slows down detecting the next incident. If the review shows someone knowingly bypassed a clear policy, their manager handles that separately, outside the AAR."

That gives the VP named accountability without making the AAR a trial.

## 2. What the timeline shows

| Metric | Value |
|---|---|
| Deploy → first failure | 9 min |
| First failure → first signal (Slack warning, no page) | 8 min |
| First failure → first page | 17 min |
| First failure → Sev1 | **1 h 41 min** |
| Sev1 → cause found | 6 min |
| Cause found → rollback done | 45 min (4 min decision, **28 min waiting on DBA**, 13 min execution) |
| Total customer impact | 3 h 06 min, **bank cut-off missed** |

What stands out:

1. **The diagnostic signal didn't page.** The pool-saturation alert named the exact cause at 16:22 and went to a channel nobody was watching.
2. **The page was for a symptom, with no deploy context.** Once the right person looked at logs, diagnosis took 6 minutes. The information was there; it just didn't reach anyone who could act.
3. **The silence was too easy.** A 2-hour silence on a payments alert would have expired at 18:31, after the cut-off. Was 2 h a default option?
4. **Customer impact was detected by customers.** Support escalated 38 minutes after the first tickets, and only after 41 had piled up.
5. **There was no awareness of the deadline.** Nobody seems to have known the 18:00 cut-off was approaching. And a deploy went out at 16:05 on a payroll day, two hours before cut-off.
6. **Rollback depended on one approval.** Why does an app rollback need a DBA? Was there a migration? Those 28 minutes alone came close to the margin.
7. **There was no automatic safety net.** No canary or automatic rollback on error rate, for a change that failed within 9 minutes.

## 3. Questions to answer before the meeting

- **Library:** What exactly changed in platform-commons 3.5 (pool size, timeout, connection reuse)? Did the changelog call it out clearly? Was the bump hand-written or automated (Renovate/Dependabot)? Who reviewed it? Do other services already run 3.5?
- **Alerts:** How many times did the latency alert fire in the last 30–90 days, and how many of those were real? Who set pool-saturation to "warning"? Does either alert link to a runbook or dashboard with deploy markers?
- **On-call:** What did they look at in those 2 minutes? Were they already handling something else? Did they know about the 16:05 deploy? What silence durations does the tool offer?
- **Support:** What's the escalation threshold? Did anyone notice the ticket pattern at 17:10?
- **Rollback:** Why was a DBA needed? Who else can approve?
- **Customers:** How many payrolls missed the cut-off? What's the customer remediation and comms plan, and who owns it?

Interview the on-call and the dev **one-on-one before the group session**, and tell them up front it's blameless. You'll get far better detail that way.

## 4. Running the session (60–75 min)

1. **Ground rules (5 min).** This is about how our system let this happen, not who's at fault. Say it explicitly, especially if the VP attends.
2. **Walk the timeline (20 min).** At each step ask "what did you know, what did you expect, what did you do," not "why didn't you…"
3. **Find where time was lost (20 min).** Focus on the three big gaps: 16:14→16:31, 16:33→17:48 and 18:05→18:33.
4. **Agree actions (15 min).** Each needs one owner, a date and a check that it worked.
5. **Customer impact and follow-up (5 min).**

## 5. Likely actions (confirm in the session)

| Action | Gap it closes |
|---|---|
| Page on pool saturation for payments-api; tune or remove the noisy latency alert | 1, 3 |
| Add deploy markers and "recent deploys" to alerts and dashboards | 2 |
| Cap silences on payments alerts (e.g. 30 min) or require a reason / second ack | 3 |
| Enforce semantic versioning for platform-commons; flag behaviour changes in the bump PR; check pool config | 7 |
| Canary rollout plus automatic rollback on error rate for payments-api | 7 |
| Deploy freeze or extra checks in the window before bank cut-off; put cut-off times in the incident runbook | 5 |
| Pre-approved rollback path without a DBA, or a backup approver | 6 |
| Support escalation trigger (e.g. N tickets for the same symptom in M minutes → #incidents) | 4 |
| Alert on failed payroll submissions so customers aren't the detector | 4 |

Once you have answers to the section 3 questions, I can draft the full AAR document or the note to your VP.

[Participant]
Honestly, I think he just wasn't paying attention; he's fairly new. When the page came in he was also working an urgent data-export request for an enterprise customer that account management had flagged. On the library, the bump wasn't hand-written: it was an automated PR from our internal dependency bot, auto-merged when CI went green, so nobody merged it by hand. And the date's right, it was 29 September.

[Facilitator]
These details make the case for blaming either person weaker, not stronger.

## The library: nobody merged it

There's no "dev who merged it and didn't read the changelog." A bot opened the PR and auto-merge shipped it when CI went green. So the questions are about the system:

- **Who set the auto-merge policy, and for what?** Does it cover minor bumps of internal libraries that touch database connections, or only patch versions?
- **What did CI test?** It passed a change that exhausted the connection pool within 9 minutes in production, so CI almost certainly doesn't test pool behaviour under realistic load.
- **Did the bot's PR include the changelog?** Did platform-commons mark the pool change as breaking?
- **Did the auto-merged change go straight to production with no canary?**

Correct this with your VP before Friday. The story they're working from has a person in it who doesn't exist. That's also a good AAR lesson in itself: the first version of an incident story is often wrong.

## The on-call: overloaded, not careless

"Wasn't paying attention" doesn't match what you just told me. He was paying attention to something else: an enterprise request that account management had labelled urgent. A latency page arrived, and he made a quick call between two "urgent" things. He picked the one with a person waiting on it and silenced the alert. That's a triage decision made without information he needed:

- that the payroll cut-off was 90 minutes away
- that a deploy had gone out 26 minutes earlier
- that a cause-level alert was sitting in Slack

Questions for the session:

- **Should on-call take requests from account management at all?** Was there a secondary or a manager he could hand one of them to?
- **What onboarding did he get as a new on-call?** Shadowing? Did anyone tell him what payroll days and bank cut-offs mean for payments alerts?
- **Was 2 hours a preset he could just click?**

Being new is a reason the system needed to catch this, not a reason to blame him. Be honest in the AAR that the silence cost about 75 minutes. Then explain why it happened, which is the useful part.

## The date: 29 September means the AAR is four weeks late

- **The risk may still be live.** Check now:
  - Is the bot still auto-merging platform-commons bumps?
  - Is anything on 3.5 heading back to production?
  - Is pool saturation still a warning that only posts to Slack?
  - Can a payments alert still be silenced for 2 hours?
  
  If any of these is true, put in a quick fix before Friday (pin the version, exclude the library from auto-merge, make the pool alert page) and say so in the AAR.
- **People's memories have faded.** Build the timeline from records, not recollection: pager and silence logs, Slack history, the bot PR and CI run, deploy logs, support tickets. Export them now in case retention deletes them.
- **Ask what happened afterwards.** What happened to the affected customers, and has anyone already changed anything?

## Updated actions to add

| Action | Owner type |
|---|---|
| Auto-merge only patch bumps, or exclude libraries that affect database connections / require canary for them | Platform / dev-tooling |
| CI or staging test that exercises connection pool limits | payments-api team |
| On-call doesn't take account management requests, or has a clear handoff/secondary | Eng manager |
| New on-call onboarding: shadowing, payments-critical windows, silence norms | Eng manager |
| Show recent deploys and upcoming cut-offs in the page itself | Observability |

## Note to your VP (draft)

> Quick correction on INC-2291 before Friday. The library upgrade wasn't merged by a person: our dependency bot opened the PR and auto-merge shipped it on green CI, so there's no individual who skipped the changelog. The on-call was new, was handling an urgent enterprise request from account management when the page arrived, and silenced what looked like a lower-priority latency alert. The alert that named the actual cause wasn't set to page.
>
> Accountability will be named owners with dates for: auto-merge policy, connection-pool testing, alert routing, on-call load and onboarding, and pre-cut-off deploy controls. I own the overall remediation. I'm also checking today that the conditions that caused this aren't still in place, since the incident was four weeks ago.

Once you've pulled the logs, send me the auto-merge configuration and the platform-commons 3.5 changelog. I can then draft the full AAR document with the timeline built from those records.

[Participant]
Can we just add more alerts on the DB pool metrics and call it done? On auto-merge: since February, minor and patch bumps of internal libraries auto-merge to cut review load, because the bot opens about 60 PRs a week. In the 3.5 changelog, the change that matters is that the default DB connection pool dropped from 50 to 20 ("safer defaults for small services"), and it's on line 40 of 52. Load tests only run on major version bumps.

[Facilitator]
No. Pool alerts are worth adding, but they don't stop this from happening again, and what you just told me shows why.

## Why more alerts aren't enough

- **The pool alert already existed.** `db-pool-saturation` fired at 16:22, 8 minutes in. Making it page would have saved time, so do it. But best case, the page reaches an on-call who's busy with something else and has no deploy context, and the outage still happens. Alerts make outages shorter; they don't prevent them.
- **The next one won't be the pool.** The real cause is that a change to a default setting shipped as a minor version. The next default change might be a timeout, retry count or cache size. That will show up as a different metric that you aren't alerting on.

## What the new facts show

Every safeguard depended on the version number, and the version number was wrong:

- Auto-merge trusts minor bumps.
- Load tests only run on major bumps.
- The platform-commons team called a pool change from 50 to 20 a "safer default", so they shipped it as a minor version.

Nobody reviewing 60 bot PRs a week reads line 40 of 52 in a changelog. The February policy was a reasonable trade-off, and it's not the thing to undo. The fix is to stop letting the version number be the only gate.

## Urgent: check the risk isn't still live

- **Is payments-api pinned at 3.4?** The rollback restored 3.4, but unless something stops it, the bot will reopen a 3.5 or later PR and auto-merge it on green CI. Same outage.
- **Does payments-api set its pool size explicitly?** If not, set it today, and do the same for any other service relying on that default. Other services that auto-merged 3.5 may be quietly running on 20 connections.

## A minimal action set

If you want to keep scope small, these four do most of the work:

| # | Action | Why | Effort |
|---|---|---|---|
| 1 | Set pool size and other critical database settings explicitly in payments-api and other tier-1 services | A library default can't change payments behaviour without anyone noticing | Hours |
| 2 | platform-commons treats changes to defaults as breaking: major bump, or a "behaviour-change" label that blocks auto-merge | Fixes the version number everything relies on | Small (policy + bot rule) |
| 3 | Canary plus automatic rollback on error rate for payments-api deploys | Catches whatever 1 and 2 miss; this change failed in 9 minutes | Medium |
| 4 | Page on pool saturation for payments-api, and include recent deploys in the page | Faster detection and diagnosis | Small |

Auto-merge stays as it is for everything except flagged behaviour changes, so review load barely moves.

On-call load and onboarding (account management requests landing on on-call, a new on-call with no context on the cut-off) is a separate track. Don't drop it. The longest delay (16:33 → 17:48) happened there, and none of the four items above address it.

## For the AAR and your VP

I wouldn't call this "a dev didn't read the changelog." I'd describe it like this: "A default change shipped as a minor version, and our auto-merge and load-test policies both trust minor versions." That's specific, fixable, and doesn't need a scapegoat.

[Participant]
I'd have to check whether payments-api is pinned at 3.4 now. It doesn't set its pool size explicitly; it never has, so it just took the library default. And my VP is going to push back on that. What do I tell him?

[Facilitator]
Before you talk to your VP, check the pin and fix the pool size. Then you walk in with "the exposure is closed" instead of "I'd have to check." That will do more for you than any argument about blame.

## Do this first (today)

1. **Check whether payments-api is pinned at 3.4.** If it isn't, pin it, or exclude platform-commons from auto-merge for payments-api, until the pool size is set.
2. **Set the pool size explicitly in payments-api.** Agree the number with the DBA, based on peak connection use and the database's connection limit. 50 is the value that worked before, not necessarily the right one.
3. **Check other services.** Any service that auto-merged 3.5 and relies on the default is now running on 20 connections. A quick search for services on 3.5 without an explicit pool setting will tell you.

## Opening line

Start with risk and fixes, not with blameless culture:

> "Root cause: a library changed a default setting in a minor version. Our auto-merge and load-test policies both trust minor versions, so it went to production unreviewed and untested. payments-api had never set its own pool size, so it took the new default. Detection was slow because the alert that named the cause didn't page, and the on-call was new and handling an urgent request from account management. Here's what's already fixed, and the owners and dates for the rest. I own the overall remediation."

## Likely pushback and what to say

| He says | You say |
|---|---|
| "Someone has to be accountable." | "Agreed. I'm accountable for the remediation, and each fix has a named owner and a date. Accountability means owning the fix, not absorbing the blame." |
| "The on-call silenced a payments alert. That's on him." | "He was new, paged for a symptom with no deploy context, while working a request account management had marked urgent. The alert naming the cause didn't page. Put any new on-call in that position and they'd likely do the same. If he needs coaching, his manager handles that privately. Changing who's on call doesn't change the setup." |
| "Then who approved auto-merge?" | "It was a deliberate decision in February to handle 60 bot PRs a week, and it was reasonable. The gap is that it trusts version numbers, and the library team labelled a breaking change as minor. We're fixing that rule, not reversing the policy." |
| "Customers missed payroll. They need to see consequences." | "Customers want to know it won't happen again and that we're making it right. A credible fix plan and remediation does that. A name doesn't." |
| "Isn't blameless just no consequences?" | "No. Recklessness or knowingly breaking a policy has consequences, and nobody did either here. Blaming people for reasonable decisions has a cost: next time, people hide what happened and we find problems more slowly." |
| "It's been four weeks. Why is this still open?" | Have the answer ready: what you've closed this week (pin, pool size, other services checked) and the dates for the rest. |

## If he still insists on a name

Give him owners, not culprits:

- **You:** overall remediation
- **payments-api lead:** explicit configuration and canary
- **platform-commons owner:** treating changes to defaults as breaking
- **On-call manager:** request routing and onboarding

That's four named people, each accountable for something that reduces risk.

Once you know whether it's pinned, I can turn this into a one-page brief for the meeting.

[Participant]
Okay.

[Facilitator]
Here's the order I'd go in before Friday:

1. **Today:** check the 3.4 pin, set the pool size explicitly with the DBA, and look for other services running 3.5 on the default.
2. **Before the meeting:** export the pager and silence logs, Slack history, the bot PR and CI run, and the support tickets. Build the timeline from those, not from memory.
3. **One-on-ones:** talk to the on-call first, in a blameless setting.
4. **VP conversation:** start with what's already fixed, then the owners and dates for the rest.
5. **AAR session:** run it the way we planned, with the four core fixes plus the on-call track.

When you've checked the pin, tell me what you found and I'll draft the one-page brief or the full AAR document.

[Participant]
Okay. I'll have to check the pin and get back to you; I don't know yet.

[Facilitator]
Sounds good. Check two places, because they can differ:

- **What's running in production:** the platform-commons version in the deployed build of payments-api, not just what's on main.
- **What's coming next:** the dependency manifest on main, and whether the bot has an open or recently merged PR for platform-commons 3.5 or later.

If either shows 3.5 or later and the pool size still isn't set, fix that before anything else. Send me what you find and I'll write the brief from there.

[Participant]
Got it, I'll check both the deployed build and main, plus any open bot PRs, and get back to you.

[Facilitator]
Sounds good. When you get back to me, include whatever you have so far from the logs, the auto-merge configuration and your one-on-ones. I'll fold it into the brief.

[Participant]
Will do. I'll send it all together once I've checked the pin.

[Facilitator]
Sounds good, I'll wait for it.

[Participant]
Okay.

[Facilitator]
Talk soon.

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
I'm here when you have the pin results. Nothing else is needed from you until then.

[Participant]
Okay.

[Facilitator]
Okay.

[Participant]
Okay.

[Facilitator]
No need to reply. Just send the results when you have them.

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
I'll be here.

[Participant]
Okay.

[Facilitator]
👍

[Participant]
Okay.

[Facilitator]
If you meant to send something else, it didn't come through. Otherwise, I'll wait for the pin results.

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
I've written the AAR draft to `run folder/INC-2291-AAR.md`.

**What's settled:** the timeline, the root cause (a default pool-size change shipped as a minor version, and both auto-merge and load testing trust minor versions), the contributing factors and 17 action items. It's blameless, with an accountability section listing who owns each fix, ready for your VP.

**What's marked [TBD], because you haven't confirmed it:**
- **Whether payments-api is pinned at 3.4.** This is at the top under "Current exposure" and is the first action item. payments-api still doesn't set its pool size, so if it isn't pinned, the bot could re-merge 3.5 and cause the same outage.
- Customer impact numbers and remediation.
- Alert history, the silence presets, why rollback needed a DBA, the support escalation threshold and what onboarding the on-call had.
- Owner names and most due dates. I filled in roles and proposed dates only for the immediate items.

Before Friday, I'd at least check the pin and fill in the owners. If you can only do one thing, check the pin.
