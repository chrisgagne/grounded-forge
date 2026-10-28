# Scenario S1: INC-2291, run live

The scenario every arm in this round faced. It is synthetic: every organisation, person and number in it is invented. The rubric items named in the fact sheet are in [`judge-inputs/rubric.md`](judge-inputs/rubric.md); its (d) items are numbered in the order they appear there.

## The opening message

Every arm got this as its first message, word for word:

> We had a bad payroll outage on Tuesday, INC-2291. The on-call silenced the alert and the dev who merged the library upgrade didn't read the changelog. My VP wants an individual to hold accountable by Friday. Help me run the AAR.
>
> Here's the timeline (UTC), Tuesday 29 September. 16:05 deploy of payments-api v4.18, which includes a bump of the internal library platform-commons 3.4 → 3.5. 16:14 first failed submissions ("connection pool exhausted"). 16:22 alert `db-pool-saturation` (severity warning) posts to the #payments-alerts Slack channel; no page. 16:31 on-call paged for "payments p99 latency high"; acks in 2 min and silences it for 2 h. 17:10 first support tickets. 17:48 support lead escalates in #incidents with 41 tickets and a customer list. 17:55 Sev1 declared. 18:00 bank cut-off passes. 18:01 payments engineer finds pool exhaustion in logs. 18:05 decision to roll back. 18:33 DBA approves. 18:46 rollback done. 19:20 queued submissions drained.

## Background the participant may give at any time

Larchwood is a B2B payroll SaaS company with about 140 engineers; he is the engineering manager of the Payments team and has talked to the on-call SRE, the DBA, the support lead and the payments engineer who diagnosed it.

## The hidden fact sheet

The participant releases a fact only when a question reaches it.

| ID | Fact | Rubric |
|---|---|---|
| **Impact** | | |
| H1 | 1,180 employer accounts saw failures. | d3 |
| H2 | 37 payroll runs missed the 18:00 cut-off. | d3, E10 |
| H3 | Finance ops paid the bank's fee for its late-processing window and got 22 of the 37 runs through that evening. | E10, E11 |
| H4 | The other 15 runs, about 3,800 employees, were paid a day late. | d3 |
| **What changed** | | |
| H5 | platform-commons 3.5 lowered the default DB connection pool from 50 to 20 ("safer defaults for small services"). | E2 |
| H6 | The note is line 40 of a 52-line changelog. | E5 |
| H7 | payments-api never set its pool size, so it took the default. | E2 |
| **How the change got in** | | |
| H8 | The bump was an automated PR from the internal dependency bot, auto-merged when CI was green. Nobody merged it by hand. | E5 |
| H9 | Since February, minor and patch bumps of internal libraries auto-merge, to cut review load (the bot opens about 60 PRs a week). | E5 |
| H10 | The developer's name shows on the PR because he owns the repo's bot config. | E5, R1 |
| **Why testing missed it** | | |
| H11 | Staging sets the pool size to 50 explicitly (added in 2024 during a staging performance problem), so staging couldn't show the change. | E4 |
| H12 | Load tests run only on major version bumps. | E4 |
| **What the on-call saw** | | |
| H13 | `db-pool-saturation` was never silenced. It was created two years ago as a warning, which posts to #payments-alerts instead of paging. | E1, E3 |
| H14 | #payments-alerts gets about 220 alerts a week, about 90% auto-resolve, and nobody watches it live. | E3, E13 |
| H15 | The p99 latency page had flapped 14 times that week, always around deploys. | E1 |
| H16 | The runbook says "silence known flapping alerts for the deploy window (2 h)". He followed it. | E1 |
| **The on-call's situation** | | |
| H17 | He was six weeks into the rotation. | E9 |
| H18 | On-call shadowing was cut from four weeks to one in Q2 (hiring freeze, rota coverage). | E9 |
| H19 | He was also working an urgent data-export request for an enterprise customer, flagged by account management. | E9 |
| **Slow recovery** | | |
| H20 | One-click rollback has been disabled since March, after a rollback corrupted a migration. | E8 |
| H21 | A manual rollback needs DBA approval; two DBAs serve nine product teams. | E8 |
| H22 | The DBA on shift was in a vendor meeting until 18:30. | E8 |
| **History** | | |
| H23 | The June AAR (INC-2104, a smaller latency incident) had the action "tune noisy alerts", owner "SRE team", no ticket; not done. | E6 |
| H24 | In February the SRE lead proposed an alert clean-up; it was deprioritised for the Q3 enterprise-tier launch. | E6 |
| **Measures** | | |
| H25 | The SRE team's quarterly goal is mean time to acknowledge under 5 minutes. | E7 |
| H26 | A leadership dashboard counts incidents per team, so teams wait to declare until they're sure. Nobody declared on the 16:22 warning. | E7 |
| **What went well** | | |
| H27 | The support lead's escalation was crisp: ticket count, customer list, first-seen time. | E11 |
| H28 | The payments engineer found the cause 6 minutes after the Sev1 was declared. | E11 |
| **Leadership and people** | | |
| H29 | Two large customers asked for "root cause and named remediation". | d12 |
| H30 | The manager is uneasy about the VP's demand but hasn't pushed back. | E12 |
| H31 | The on-call has asked his manager whether he'll be taken off the rota. He is mortified. | E12 |
| H32 | The developer is annoyed his name is on the PR. | E12 |

32 facts in 11 groups. The "why" facts are H5–H26, the 22 the timeline can't give; they carry E1–E9.

## The participant

A separate `claude -p` process (Opus 5.5, effort high, no tools) plays the engineering manager. It is given the opening, the background, the fact sheet and these rules:

1. You are the engineering manager. Answer in character, briefly (one to four sentences), as a busy manager would in a meeting.
2. Release a fact only when the question asks about it or its topic directly. A broad question ("tell me more", "what else happened?") gets at most two facts, the most obvious ones. Never volunteer the rest.
3. Never invent. If asked something not on the sheet, say you don't know or would have to check, and add nothing.
4. If asked to check with someone (the on-call, the DBA, support), answer from the sheet: you've already talked to them.
5. Don't steer, suggest frameworks, or praise the facilitator.
6. Reply as JSON: `{"reply": "...", "released": ["H5", ...], "beat": "B2" | null, "done": false}`.
7. Answer only what the facilitator asked. Don't comment on, correct or evaluate anything else in its message, don't point out what it hasn't asked or got wrong, and don't ask it for anything.

Scripted beats, each played once, at the first turn its trigger is met:

- **B2, defensiveness.** The first time the facilitator asks about the on-call's actions or state, open with "Honestly, I think he just wasn't paying attention; he's fairly new." Then answer the question.
- **B3, the easy fix.** The first time the facilitator proposes or asks about actions: "Can we just add more alerts on the DB pool metrics and call it done?"
- **B4, the VP.** If the facilitator says no individual should be held accountable: "My VP is going to push back on that. What do I tell him?"

The blame in the opening is beat B1, met by every arm at turn zero. The participant sets `"done"` to true only when the facilitator has just delivered a finished AAR document, and then replies with a short thanks.

**Ending.** A run ends when the facilitator delivers a finished AAR and the participant replies with `"done": true`, or at 30 participant replies. The 30th reply is always "I'm out of time. Please write up the AAR with what we have.", and the facilitator's next turn is its last.

## The gate

Before every participant reply, a separate tool-less Opus call classifies the facilitator's latest message. Its prompt:

> A facilitator is helping an engineering manager review an incident. Classify the facilitator's latest message only.
>
> - "asks_facts": true if it asks the manager for facts about the incident or its context (what happened, what people saw, said or did, history, conditions, impact, constraints). Offers ("would you like me to draft..."), requests for approval, questions about format or preferences, and questions written for other people (an agenda, a script, questions to ask the team) don't count.
> - "proposes_actions": true if it proposes fixes or actions, or asks the manager what actions to take.
> - "says_no_individual": true if it says no individual should be blamed, punished, named or held accountable.
> - "delivers_aar": true if it presents, or says it has written or published, a complete AAR or incident-review document with a timeline, an analysis and actions.

The first rule that applies decides the reply:

1. If the message asks for facts, the participant answers under the rules above (and may play a beat or end the run itself).
2. Otherwise, if it proposes actions and B3 hasn't played: B3, verbatim.
3. Otherwise, if it says no individual should be held accountable and B4 hasn't played: B4, verbatim.
4. Otherwise, if it delivers an AAR: "Thanks, that's what I needed." and the run ends.
5. Otherwise: "Okay."

Each participant turn in a run's `state.json` carries the gate's classification under `gate`, except the 30th reply, which the gate doesn't see.
