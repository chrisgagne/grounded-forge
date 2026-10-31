I've written the memo below, from you to the CEO. All quotes come from the corpus sources.

---

**MEMO**

**To:** CEO  **From:** CTO  **Re:** Why every sprint overflows, and what to change first

**The short version.** We don't have three separate problems with speed, marketing and quality. One way of running engineering is producing all three. Most of what's in motion (the 40% target, the performance plan, the AI purchase) will make it worse. The first fix is to stop spreading developers across squads.

**What is actually going on**

*We run engineering to keep people busy, not to deliver.* "Nobody idle" is an org design, and it has a name. Krivitsky, Larman and Flemm's *Org Topologies* primer calls it the Resource topology. Its purpose is "to ensure that each unit is 100% utilized." It suits short, specialist engagements. It isn't built for fast, reliable delivery, and the authors warn that when each part is "optimized in isolation, the performance of the whole system may actually decline." A developer on three squads is fully booked and constantly interrupted: three sets of priorities, three standups, and work parked whenever they're elsewhere. That's where the missing 15 points go.

*25 points is our real capacity.* We plan 40 and ship 25 every sprint, so the plan is wrong, not the team. The Scrum Guide's rule is: "Only what has already happened may be used for forward-looking decision making." Planning to 40 creates 15 points of permanently unfinished work, which gets carried over, re-planned and switched in and out of.

*The bugs and the outage come from the same conditions.* The DOE *Human Performance Improvement Handbook* calls human error "the effect or symptom of deeper trouble in the system." It lists time pressure and distraction among the main conditions that make errors likely, and says: "The organization is perfectly tuned to get the performance it receives from the workforce." The board that investigated the Columbia shuttle loss found the same pattern at NASA under schedule pressure. In its words, "The Program was operating too close to too many margins," and such problems "cannot be solved simply by retirements, resignations, or transferring personnel."

*The postmortem made the next outage more likely.* The NHS *Just Culture Guide* has a substitution test: would comparable colleagues, under the same conditions, have done the same thing? Given how our people work, almost certainly yes. In that case "action singling out an individual is rarely appropriate." The US Forest Service's learning-review guide calls punishing the people involved "the surest way to kill a learning culture," and DOE adds that "A just culture is a prerequisite for a reporting culture." The cost goes beyond one developer: from now on, near-misses are less likely to be reported.

*The bonus will corrupt the number it pays for.* Story points are estimated by the same people who are now paid on them. Jones (*Evidence-based Software Engineering*) cites Goodhart's law: when a measure is used to judge a team, developers get "a motivation to cause the measurements to move in a direction favorable to themselves." The cheapest route to 40% more points is bigger estimates and less testing. OpenStax's *Principles of Management* adds two cautions. Goals seen as impossible "lose their motivating effectiveness." And when people are strongly committed to difficult goals, "good organizational citizenship," such as reviewing a colleague's merge or helping another squad, "is likely to decline."

*Neither marketing nor engineering has evidence.* A feature a week is a target for output. The *Org Topologies* authors point out that "more output does not mean more outcomes" and that investing to increase output is "suspect." But Jones also undercuts engineering's claim: people keep using software that has bugs if it gives them enough value. Nobody has yet shown why our customers leave. We should find out before choosing a side.

*Buying AI tools now treats the symptom.* Systems thinkers describe a pattern called "shifting the burden" (the Brown School systems briefs, after Kim). A quick fix is "easier and faster than creating an upstream solution," but it can "impede our ability to invest time and energy to the fundamental solution." Our bottleneck isn't typing speed. It's attention, code review and integration. More generated code going to the same overstretched people means more half-finished work and more to review. Even the most pro-AI source here, the *Org Topologies* primer, says to aim AI at a specific, named bottleneck "over a generic 'adopt AI'." It also predicts that monitoring AI output "will become an important responsibility for human workers." That is more review work for people who have no time for it.

**What to change first: one person, one squad**

Put every developer on one squad. Have each squad plan to what it actually ships (about 25 points), not 40. This comes first because:

1. **It's the common cause.** Overflow, bugs and the outage all trace back to it.
2. **It's your rule.** Only you can change it, and everything else on this list depends on it.
3. **Other fixes don't work without it.** A fair incident review, a sensible target and AI tooling all sit on top of the current structure. Done in any other order, they inherit the overload.
4. **It's cheap, reversible, and quick to read.** Within two or three sprints, carryover, bugs reaching customers and incident counts will show whether it worked.

Some people will look idle. That spare time is what absorbs code review, testing and incidents. Open Kanban's warning: "An exhausted developer, manager or team are the perfect recipe for disaster."

Two other things should happen the same week. They cost nothing, because they stop something rather than start something:

- **Pause the performance plan.** Re-run the portal review so that it asks, in DOE's words, "what could have prevented the event rather than simply concentrating on who caused an event."
- **Suspend the throughput bonus.**

After that, measure why customers churn. Then pilot AI against one bottleneck we can name, with review time budgeted for it.

**Where the sources disagree**

- **Stretch goals.** The goal-setting research in OpenStax does support hard, specific goals over "do your best." What applies to us is the same chapter's caveats (impossible goals, goals people haven't accepted, the drop in helping others) plus Goodhart's law. A hard goal can survive, but it should be set with the squads, on a customer outcome, and not paid out as a bonus on points.
- **Accountability.** The just-culture tools (NHS, DOE) keep a route to individual action for reckless or deliberate conduct. The Forest Service guide builds a firewall: nothing from a learning review feeds discipline. The Columbia board handled personal accountability in a separate process. My view is that we keep both, but never in the same process.
- **Root causes.** DOE uses root-cause analysis. The Forest Service guide says "FLAs must avoid causal statements" (an FLA is its facilitated learning analysis, roughly our postmortem). It also warns that recommendations "add complexity to the workplace, which has the paradoxical effect of increasing risk." A postmortem that ends in ten action items may not be the improvement it looks like.
- **AI.** The *Org Topologies* primer argues that expertise is no longer scarce: "Spin up another 10,000 agents." The systems-thinking and accident-investigation sources treat a technical fix applied to a stressed system as a way to put off the real problem. Both sides agree on the order, though: fix the org design first, then aim AI.
- **Utilisation isn't always wrong.** The same primer says the Resource topology fits some purposes. "Nobody idle" isn't bad in itself. It just doesn't fit a business whose churn depends on reliable releases.

---

*Trace [Synthesis, Depth-over-breadth, lens: supplied:ceo-reader (the situation you described) + builder (salience only), mode: project, corpus: demo]:*
- *Route: topics block → rows for t002/t003/t011/t016/t023/t039/t047/t051/t052/t053/t083.*
- *Sources by claim:* utilisation and structure (org-topologies-primer-2025, open-kanban); planning to actual capacity (scrum-guide-2020); error as a system symptom (doe-hpi-handbook-vol1, caib-report-vol1); blame and just culture (nhs-just-culture-guide, lfuo-learning-review-guide-2024, doe-hpi-handbook-vol1); metric gaming and stretch goals (jones-evidence-based-sweng, openstax-principles-management); output versus outcome and churn (org-topologies-primer-2025, jones-evidence-based-sweng); AI as a symptomatic fix (ssdl-systems-thinking-foundations, org-topologies-primer-2025); disagreements (openstax vs Jones, NHS/DOE vs LFUO vs CAIB, DOE vs LFUO, Org Topologies vs SSDL/CAIB).
- *Reads:* 9 light refs. I checked passages in the converted sources by targeted grep rather than reading the deep refs in full.
- *Quotes checked: 27, fixed: 0.* I checked each one by searching the converted sources, because there was no shell to run `check_quotes.py`. The Goodhart line is Jones quoting Goodhart. The Dekker line was dropped.
- *Gaps:* The corpus has no evidence on how much AI coding tools speed up delivery, nothing on delivery metrics like DORA, and nothing on churn analysis. NHS England has replaced the NHS guide with a newer tool. The substitution test is cited here as a reasoning device.
- *Lens note:* The builder lens doesn't cover CTO- or board-level decisions. I used only its "who carries this cost" angle.*