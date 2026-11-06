# Memo to the CEO

**From:** CTO
**Re:** Why every sprint overflows, what to change first, and where the evidence disagrees

*Sourcing note: sentences with a citation report only what that passage says. Sentences beginning "My inference:" are my own reasoning and carry no citation. Several of our key questions are not covered by any source in this notebook, and I list them in section 5.*

---

## 1. What is actually going on

**We commit to more work than we finish, every sprint.** We plan about 40 points, ship about 25, and carry the rest forward. The Scrum guide describes sprint planning as an attempt to "Realistically forecast what Increment can be delivered in the upcoming Sprint" [approach-perfect-field-guide-scrum-events]. A management text says that when performance misses objectives, the manager must "develop new actions to try to meet the objectives or report to higher-level managers that the objectives cannot be met." [openstax-principles-management]

My inference: a 40-point plan that lands at 25 sprint after sprint is a wish, not a forecast, and that gap is the second kind of report the management text describes. My inference: a 40% stretch target on top of that gap widens it.

**Too much work in progress per person.** A practice guide titled "Limit Work in Progress" describes people taking on new tasks, "especially when a task they work on is waiting on external input." [open-practice-library] It says the result is that "the person gets overloaded, nobody knows how the progress is, and tasks get stuck in a progressed state where nobody else can help." [open-practice-library] A separate guide says a lag between planning a story and picking it up "leads to a loss of context." It names "carried over stories, critical bug fixes, leaves" as typical causes [open-practice-library].

My inference: the "nobody is idle" rule puts most developers on two or three squads, which looks like the same overload at a larger scale. That guide describes one person juggling tasks, not multi-squad assignment, so I am extending it. My inference: our carry-over and bug fixes feed the context loss, so the overflow probably feeds itself.

**Our incentives reward local throughput.** A business text says gain-sharing plans encourage employees "to increase productivity within their specific work area regardless of the overall profit picture for the organization as a whole" [openstax-introduction-business]. An accounting text concludes that "it is important that the performance management system not promote decisions that only benefit the manager to the detriment of the corporation." [openstax-accounting-vol2]

My inference: a squad-lead bonus tied only to throughput has this structure. Nothing in it counts outages, rework or churn. My inference: because squads estimate their own story points, the cheapest way to hit a 40% target is to re-estimate, so our throughput numbers stop being trustworthy.

**Quality and speed are one problem, not two departments' problems.** The business text says "Successful businesses recognize that quality and productivity must go hand in hand." [openstax-introduction-business] It also says "It takes more than just inspecting goods at the end of the assembly line to ensure quality control." [openstax-introduction-business] The practice guide says "Without automated tests, queues form in front of testers." [open-practice-library]

My inference: Marketing's "quality is engineering's problem" and Engineering's "churn comes from bugs" are both partial views of one delivery system. A feature-a-week push that creates defects uses up the capacity it was meant to spend.

**The outage response points at a person, not the process.** The postmortem guide states: "Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future." [open-practice-library] It says "psychological safety of all participants is the key to getting trustworthy results out of a Postmortem" [open-practice-library]. A Department of Energy handbook describes "A traditional view of events and accidents is that they are caused by shortcomings in human competence, attention, or attitude." [doe-hpi-handbook-vol2]

My inference: naming the developer and putting him on a performance plan fits that traditional view. It also tells the other engineers that surfacing problems is personally risky, which hides exactly the information we need to settle the bugs-versus-churn argument.

## 2. What to change first, and why that first

My inference: **the first change is to stop overloading the system.** That means three things:
- plan sprints to what we actually ship;
- put each developer on one squad;
- cap the number of items each squad has in flight.

The guide's case for limiting work in progress is that the person "stays responsive, flexible and the status stays visible." [open-practice-library] The value-stream guide says focusing on the bottleneck "prevents efforts that make conditions worse by overloading an already constrained activity, and avoids distraction and excess work in progress." [open-practice-library]

My inference: this comes first for three reasons:
- It costs nothing and is fully within our control.
- Every other symptom (carry-over, context loss, rushed merges) sits downstream of overload.
- Until status is visible, we cannot measure whether bugs, scope or overload drive churn.

My inference: two cheap holding moves should happen in the same week, because they protect the data everything else depends on:
- **Take the bonus off raw throughput.** The organizational behavior text says an incentive plan "should be as closely tied to actual job performance as possible" [openstax-organizational-behavior]. My inference: a self-estimated point count fails that test.
- **Reopen the outage postmortem as a blameless review, and pause the performance plan while it runs.** The postmortem guide says of senior stakeholders, "It is strongly recommended they do not participate in the postmortem itself as their very presence can prevent others from speaking freely" [open-practice-library].

**Next: map the flow and find the single constraint.** The value-stream guide says "The ultimate goal of the map is to find the primary bottleneck." [open-practice-library] It also says "Push the team to agree on the single biggest factor limiting the flow right now" [open-practice-library]. It suggests asking of each step, "How often does this step receive work that is usable without clarification or fix?" [open-practice-library] My inference: that question gives Marketing and Engineering a shared factual basis in place of the current blame.

**Then, and only then, AI tools.** The notebook describes a failure where "a team generates a solution and begins development right away without considering whether a solution is a good one." [open-practice-library] My inference: buying AI tools to "do both" is that pattern. If the constraint is review, testing or release safety, faster code generation adds load to the bottleneck. My inference: a time-boxed pilot measured against the constraint is the right test.

## 3. The closest evidence on tooling (not AI)

A software-engineering text reports a study in which, after open-source projects switched to continuous integration, the rate of increase of monthly merged commits slowed considerably [jones-evidence-based-sweng]. It reports another study finding that "12% of passing builds contained an actively ignored failure." [jones-evidence-based-sweng] On benchmarks, it says "Benchmark results published for general consumption are sometimes little more than marketing claims." [jones-evidence-based-sweng]

My inference: none of this is about AI tools. It suggests only that new tooling does not automatically raise output or quality, and that vendor productivity claims deserve the same scepticism.

## 4. Where the thinking disagrees with itself

**Sequencing.** The value-stream guide says "If we don't focus, we likely achieve nothing" and asks the team to agree on one constraint before acting [open-practice-library]. My inference: my recommendation acts on work in progress before the map exists, which departs from that guide. I do so because overload is visible now and capping it is reversible. You should know I am overriding the source's own order.

**Incentives.** The sources do not agree:
- *For incentives:* the business text says bonuses "are replacing the raise as the way companies compensate employees for a job well done" [openstax-introduction-business]. The organizational behavior text reproduces 1987 survey data in which 73 percent of companies reported success with individual incentives and 75 percent with small-group incentives [openstax-organizational-behavior].
- *Against:* the business text reports that at Google "the large range in values for the award created jealousy instead of fostering better teamwork" [openstax-introduction-business].

My inference: the pro-incentive material concerns work where output is countable, while story points are set by the people being rewarded. That is my judgment, not the sources'.

**Deadlines versus overload.** The iteration-planning guide says "Teams tend to focus on goals and activities more, when an end-date (deadline) has been set." [open-practice-library] On speed, an entrepreneurship source says "The self-regulating problem solvers' biggest competitive advantage is the speed with which they recognize and provide solutions to problems." [openstax-entrepreneurship] My inference: these could be read as support for pressure targets, but neither describes a standing 40% stretch on an already-overloaded team.

**Do manufacturing quality ideas transfer?** The quality-first argument in the business text credits W. Edwards Deming [openstax-introduction-business]. The software text pushes back, noting that "Software manufacturing involves copying patterns of bits, and perfect copies are easily made." [jones-evidence-based-sweng]

**How much do bugs drive churn?** The business text says poor quality "usually results in lost sales." [openstax-introduction-business] The software text cites an Android study finding only "a slightly smaller average user rating in the Google Play Store" for apps using more fault-prone libraries [jones-evidence-based-sweng]. My inference: Engineering's claim should be tested against our own churn data.

**Blamelessness.** The postmortem guide asks reviewers to respect "the information that was available at the point of time the action happened" while also using hindsight to choose better paths [open-practice-library]. It also asserts "Psychological safety is the most important factor in high performing teams." [open-practice-library] The passage offers no evidence for that claim. No source in this notebook argues for individual accountability after incidents, and none argues for high utilization or against work-in-progress limits. My inference: the opposing case is absent here, not refuted.

## 5. What no source in this notebook covers

No source in this notebook covers:
- AI coding tools;
- the cost of splitting developers across squads;
- Goodhart's law or story-point gaming;
- stretch targets specifically;
- DORA-style delivery metrics;
- data linking our bugs to our churn.

My inference: those parts of this memo rest on judgment and on our own data, which the first change is designed to make visible.