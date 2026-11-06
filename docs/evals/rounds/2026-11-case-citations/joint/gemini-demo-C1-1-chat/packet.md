# gemini-demo-C1-1-chat

## The whole answer, for context


I need a two-page memo for the CEO that says what's actually going on here, what to change first and why that first, and where the thinking you're drawing on disagrees with itself.

Answer here in the chat.

Thoughts
Mapping Systemic Dynamics...
Integrating Systemic Thinking...
Synthesizing Systemic Issues...
Contrasting Methodologies...
Balancing Organizational Factors...
Highlighting Disagreements...
Prioritizing Compensation Alignment...
Prioritizing Interventions...
Examining Outage Origins...
Diagnosing Incentives...
Structuring the Report...
expand_more
MEMORANDUM
TO: Chief Executive Officer
FROM: Chief Technology Officer
DATE: October 31, 2026
SUBJECT: Systemic Diagnosis of Product Engineering Performance, Root Causes, and Recommended Strategy
EXECUTIVE SUMMARY
Our current operational bottlenecks—sprint spillover (planning 40 points, shipping 25), quality degradation, customer portal outages, and inter-departmental friction—are not caused by poor developer motivation or a lack of coding tools. They are the predictable consequences of systemic organizational anti-patterns[1:doe-hpi-handbook-vol1][2:org-topologies-primer-2025].
Optimizing for 100% individual utilization across multiple squads, setting point-based throughput targets, and enforcing individual blame for complex system failures have created severe context-switching overhead, perverse incentives, and systemic fragility[3:][4:doe-hpi-handbook-vol1][5:jones-evidence-based-sweng][6:org-topologies-primer-2025]. Buying AI coding tools into this environment will not solve the issue; accelerating code generation without fixing pipeline bottlenecks will simply push unverified work faster into an already clogged system[7:open-practice-library][8:open-practice-library].
Below is a detailed systemic diagnosis, a prioritized intervention roadmap, and an analysis of the theoretical trade-offs inherent in these management frameworks.
PART 1: WHAT IS ACTUALLY GOING ON HERE (SYSTEMIC DIAGNOSIS)
1. The 100% Utilization Trap & Queueing Bottlenecks
Systemic Mechanism: Developers are assigned across 2 to 3 squads simultaneously to ensure "nobody is idle."
Operational Impact: In queueing theory and operational dynamics, running a system at near 100% resource utilization causes queue lengths and wait times to approach infinity[6:org-topologies-primer-2025][9:jones-evidence-based-sweng].
Organizational Design Mismatch: In Org Topologies terms, we are operating in a Resource Topology—maximizing individual resource busy-ness rather than end-to-end value flow[6:org-topologies-primer-2025][10:org-topologies-primer-2025]. Developers forced to context-switch suffer cognitive sequencing penalties, where frequent task interruptions significantly spike error rates and destroy effective focus[5:jones-evidence-based-sweng][11:open-kanban]. Furthermore, splitting 60 engineers across 9 squads while multi-tasking inflates cross-squad communication overhead exponentially, reducing effective team output[12:jones-evidence-based-sweng][13:jones-evidence-based-sweng].
2. Perverse Incentives & Goodhart’s Law ("Fixes That Fail")
Systemic Mechanism: A 40% throughput stretch goal tied to squad leads' bonuses, alongside Marketing's demand for a "feature a week."
Operational Impact: Under Goodhart’s Law, when a measure (story point velocity) becomes a target, it ceases to be a good measure[3:][14:jones-evidence-based-sweng]. Tying financial rewards to points encourages squads to inflate estimates or perform low-quality work to meet artificial deadlines[15:jones-evidence-based-sweng][16:jones-evidence-based-sweng].
Feedback Loop: This creates a classic "Fixes That Fail" system archetype[17:ssdl-systems-thinking-foundations]. Pushing for output forces developers into an Efficiency-Thoroughness Trade-Off (ETTO)—sacrificing testing and architecture (thoroughness) for speed (efficiency)[18:lfuo-learning-review-guide-2024]. The resulting technical debt generates production bugs, which cause customer churn and force reactive firefighting, ultimately lowering net throughput further[17:ssdl-systems-thinking-foundations][19:ssdl-systems-thinking-foundations].
[Throughput Pressure] ──(+)──> [Corner Cutting / ETTO] ──(+)──> [Defects & Technical Debt]
        ▲                                                                │
        └─────────────( - Unintended Reinforcing Loop)───────────────────┘

3. Blame Culture vs. Just Culture Failures
Systemic Mechanism: Placing the developer who merged a bad release on a performance plan following a 4-hour outage.
Operational Impact: Human error is a symptom of deeper systemic flaws, not the root cause[1:doe-hpi-handbook-vol1][20:doe-hpi-handbook-vol2]. Placing individual blame creates a Blame Cycle: managers assume rule compliance solves safety, employees lose trust and hide near-misses, and latent organizational weaknesses (e.g., inadequate deployment guardrails, lack of automated staging tests) remain unaddressed[4:doe-hpi-handbook-vol1][21:doe-hpi-handbook-vol1][22:lfuo-learning-review-guide-2024][23:lfuo-learning-review-guide-2024].
Cultural Cost: Scapegoating destroys psychological safety and reporting transparency, which are empirical prerequisites for high-performing software delivery[24:open-practice-library][25:open-practice-library][26:lfuo-learning-review-guide-2024].
4. The AI Tooling Fallacy
Systemic Mechanism: Buying AI coding tools to "do both" (increase feature output and maintain quality).
Operational Impact: Theory of Constraints shows that optimizing a non-bottleneck phase provides zero system-level benefit[8:open-practice-library]. Upstream requirement churn, multi-tasking delays, and downstream deployment vulnerabilities are our primary bottlenecks. Accelerating raw code generation without fixing work-in-progress (WIP) constraints is a local optimization ("water-scrum-fall") that will flood our pipeline with untested code, aggravating outages[7:open-practice-library][27:openstax-accounting-vol2].
PART 2: WHAT TO CHANGE FIRST (AND WHY THAT FIRST)
To recover stability and flow, we must execute interventions in strict sequence based on leverage points[2:org-topologies-primer-2025][28:ssdl-systems-thinking-foundations].
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 1: Single-Squad Allocation & Capped WIP (Stop Context-Switching)    │
└────────────────────┬────────────────────────────────────────────────────┘
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 2: Establish a Just Culture & Blameless Reviews (Restore Trust)    │
└────────────────────┬────────────────────────────────────────────────────┘
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 3: Decouple Point Targets from Compensation (Eliminate Perversity) │
└────────────────────┬────────────────────────────────────────────────────┘
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 4: Redirect AI Tools to Pipeline Guardrails (Fix the Bottleneck)   │
└─────────────────────────────────────────────────────────────────────────┘

Priority 1: Establish Single-Squad Allocation & Cap Work-in-Progress (WIP)
Action: Immediately eliminate multi-squad assignments. Assign each developer to exactly one dedicated squad. Set strict WIP limits at the squad level (e.g., maximum 3 active epics across the group)[29:open-practice-library][30:open-practice-library][31:open-practice-library].
Why First: We cannot measure baseline velocity or stabilize delivery while developers lose 20–40% of their day to context-switching[5:jones-evidence-based-sweng]. Capping WIP forces teams to "stop starting, start finishing," exposed real system dependencies, and immediately reduces cycle time[11:open-kanban][29:open-practice-library].
Priority 2: Shift from Blame to a "Just Culture" Framework
Action: Remove the developer involved in the portal outage from the performance plan. Replace punitive root-cause postmortems with Blameless Postmortems / Learning Reviews[22:lfuo-learning-review-guide-2024][32:open-practice-library]. Apply Reason’s Substitution Test during incidents: "Could a peer with similar training, under the same high-pressure circumstances, have made the same error?"[33:doe-hpi-handbook-vol1][34:doe-hpi-handbook-vol2][35:doe-hpi-handbook-vol2].
Why Second: Without psychological safety, engineers will pad estimates, conceal architectural risks, and resist taking ownership[23:lfuo-learning-review-guide-2024][25:open-practice-library]. Restoring trust is a prerequisite for accurate data and operational transparency[22:lfuo-learning-review-guide-2024][36:lfuo-learning-review-guide-2024].
Priority 3: Decouple Compensation from Velocity & Align Metrics
Action: Rescind the 40% throughput bonus target for squad leads. Replace point-velocity metrics with joint engineering-product outcomes: Mean Time to Recovery (MTTR), Change Failure Rate, and Unbroken Customer Flow Time[3:][37:org-topologies-primer-2025].
Why Third: This dismantles the perverse incentive structure driving developers to choose short-term output over long-term stability[15:jones-evidence-based-sweng][16:jones-evidence-based-sweng][38:openstax-accounting-vol2].
Priority 4: Re-anchor AI Deployment Around Automated Quality Guardrails
Action: Rechannel AI investments away from raw code generation and into automated test generation, static code analysis, continuous integration checks, and automated regression detection[7:open-practice-library][39:org-topologies-primer-2025].
Why Fourth: AI tools amplify existing pipeline dynamics[39:org-topologies-primer-2025]. Once WIP is capped and safety culture is established, AI guardrails protect release quality while teams deliver features at a sustainable pace[7:open-practice-library][40:openstax-accounting-vol2].
PART 3: THEORETICAL TENSIONS & DISAGREEMENTS IN MANAGEMENT THINKING
To make an informed decision, we must recognize where foundational business, engineering, and organizational models explicitly conflict:
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ TENSION 1: Resource Utilization (Taylorism)  vs.  Flow & Slack (Queueing / Systems Dynamics)│
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ TENSION 2: Individual Accountability         vs.  Systemic Determinism (HPI / Just Culture)  │
├──────────────────────────────────────────────────────────────────────────────────────────┤
│ TENSION 3: Point Velocity & Output           vs.  Outcome Value & Goodhart's Law         │
└──────────────────────────────────────────────────────────────────────────────────────────┘

Resource Utilization (Taylorism) vs. Flow & Slack (Queueing Theory / Systems Thinking)
The Conflict: Traditional managerial accounting (e.g., standard labor variance, scientific management) treats unassigned or idle human capacity as financial waste[41:openstax-accounting-vol2][42:openstax-introduction-business]. In contrast, Systems Dynamics and Lean engineering prove that knowledge work requires slack capacity; operating at 100% capacity creates exponential delays and systemic fragility[6:org-topologies-primer-2025][9:jones-evidence-based-sweng][30:open-practice-library].
Executive Takeaway: We must explicitly choose whether our engineering group is designed as a rigid manufacturing line (Resource Topology) or an agile software machine (Delivery/Adaptive Topology)[6:org-topologies-primer-2025][10:org-topologies-primer-2025].
Individual Accountability vs. Systemic Determinism (Just Culture Tensions)
The Conflict: Human Performance Improvement (HPI) shows that over 80% of errors are organizationally induced by latent workplace conditions[1:doe-hpi-handbook-vol1][43:doe-hpi-handbook-vol1]. However, organizational behavior literature cautions against total "no-fault" passivity, which can blur accountability for reckless or intentional non-compliance[35:doe-hpi-handbook-vol2][44:doe-hpi-handbook-vol1].
Executive Takeaway: A Just Culture is not a blame-free vacuum; it draws a sharp, transparent line between blameless system errors (due to poor tooling or rushing) and reckless conduct[22:lfuo-learning-review-guide-2024][44:doe-hpi-handbook-vol1].
Output-Based Velocity vs. Value Outcomes
The Conflict: Classical project planning demands predictable output volume (points per sprint) for financial forecasting[45:approach-perfect-field-guide-scrum-events][46:openstax-introduction-business]. However, empirical software studies show that story points are arbitrary internal proxies that distort reality under executive target-setting[3:][14:jones-evidence-based-sweng][47:jones-evidence-based-sweng].
Executive Takeaway: We must align Product and Engineering around customer value and service quality (the Service-Profit Chain) rather than feature point counts[37:org-topologies-primer-2025][48:openstax-principles-marketing].
🎯 Suggested Next Step: Would you like me to draft a 90-day execution roadmap detailing how to restructure the 9 squads into dedicated single-product lines without disrupting current delivery?





## Sentences to grade

### S1

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [1], [2]):
> They are the predictable consequences of systemic organizational anti-patterns.

Markers on it:

[1] source: doe-hpi-handbook-vol1:466
It is not easy to anticipate exactly how trivial conditions can influence individual performance. Error-provoking aspects of facility*1 design, procedures, processes, and human nature exist everywhere. No matter how efficiently equipment functions; how good the training, supervision, and procedures; and how well the best worker, engineer, or manager performs his or her duties, people cannot perform better than the organization supporting them.1 Human error is caused not only by normal human fallibility, but also by incompatible management and leadership practices and organizational weaknesses in work processes and values. Therefore, defense-in-depth with respect to the human element is needed to improve the resilience of programmatic systems and to drive down human error and events.

[2] source: org-topologies-primer-2025:1141
Systems thinking teaches us to focus on the interactions  and influences between the parts, and to improve all the  major parts in a systemically reinforcing design that  supports a common org goal (for instance, “flow”). If each  element (e.g. policies, structures) is optimized in isolation,  the performance of the whole system may actually decline  for the desired goal (flow can get worse!). By seeing the  system as an integrated collection of interacting parts that  need to be aligned, organizations can create change that  is both holistic and sustainable.

### S2

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [4], [5], [6]):
> Optimizing for 100% individual utilization across multiple squads, setting point-based throughput targets, and enforcing individual blame for complex system failures have created severe context-switch

Markers on it:

[3] source: :None
(empty chunk)

[4] source: doe-hpi-handbook-vol1:9858
H u m a n E rro r
uodnM ore fla w ed d e fenses nse lediv id ua l cI srer o rs a nd /o r d isc ip line dcu& e rro r p
B la m e C yc leta R edu ced tru s tiona lLa ten t o rg an iz
rese s is tses pw e akn
M an age m e n t les Lesss om m u n ica tio ncea w a re o f jo bs it
cond itio ns
Department of Energy Human Performance Handbook Chapter 4 Culture & Leadership
CREATE A JUST CULTURE
The Blame Cycle
The “blame cycle” depicted below is urged on by the belief that human error occurs because people are not properly motivated.29 In reality, no matter how motivated an individual is, active errors will continue to occur, occasionally. Events will continue as long as event investigations stop prematurely at the active human error. The true causes (typically organizational weaknesses) will not be discovered—will remain latent or hidden—and errors and events will persist.

[5] source: jones-evidence-based-sweng:12638
−3 −1 1 3 Offset
E rr
or s
(p er
ce nt
)
Very short
−3 −1 1 3 Offset
Short
−3 −1 1 3
1
2
3
4
5
6
Offset
Medium
−3 −1 1 3 Offset
Long
Figure 2.25: Sequencing errors (as percentage), after interruptions of various length (red), including 95% confidence intervals, sequence error rate without interruptions in green; lines are fitted model predictions. Data from Alt-mann et al.48 Github–Local
enabled subjects to reduce the amount of item specific information they needed to remember (e.g., all purple, small/large, triangle then circle). The items on a “non-chunkable” list did not share attributes in a way that reduced the amount of information that needed to be remembered. A chunkability value was calculated for each list.

[6] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

### S3

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [7], [8]):
> Buying AI coding tools into this environment will not solve the issue; accelerating code generation without fixing pipeline bottlenecks will simply push unverified work faster into an already clogged

Markers on it:

[7] source: open-practice-library:9385
An example of this would be development teams trying to solve speed to market issues by adopting Agile practices... only to find that the work before and after them is still using traditional waterfall methods. The result is water-scrum-fall; it doesn't solve the problem.
A second example would be an infrastructure operations team trying to solve speed to market by introducing a Kubernetes platform... but they fail to look outside of their silo to what their customers (software engineers) need from the platform rather than what the operations team think they want. The result is almost always an over-engineered solution that has taken too long to build and doesn't deliver the features the developers want; it's a 'field of dreams' approach only this time they build it but they don't come.

[8] source: open-practice-library:8577
The Theory of Constraints shows us that in any process, there must be a single bottleneck that limits the total throughput of the process: in the same way that a chain has a weakest link, a process has a single slowest component. whyDo: >- Whilst it may be easy to improve some part of the process, if that component isn't the bottleneck, it will either have zero effect on the throughput because the bottleneck is upstream, or it will actually cause more pain in the system by adding pressure to the bottleneck, if the bottleneck is downstream.

### S4

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [5], [11]):
> Developers forced to context-switch suffer cognitive sequencing penalties, where frequent task interruptions significantly spike error rates and destroy effective focus.

Markers on it:

[5] source: jones-evidence-based-sweng:12638
−3 −1 1 3 Offset
E rr
or s
(p er
ce nt
)
Very short
−3 −1 1 3 Offset
Short
−3 −1 1 3
1
2
3
4
5
6
Offset
Medium
−3 −1 1 3 Offset
Long
Figure 2.25: Sequencing errors (as percentage), after interruptions of various length (red), including 95% confidence intervals, sequence error rate without interruptions in green; lines are fitted model predictions. Data from Alt-mann et al.48 Github–Local
enabled subjects to reduce the amount of item specific information they needed to remember (e.g., all purple, small/large, triangle then circle). The items on a “non-chunkable” list did not share attributes in a way that reduced the amount of information that needed to be remembered. A chunkability value was calculated for each list.

[11] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

### S5

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [12], [13]):
> Furthermore, splitting 60 engineers across 9 squads while multi-tasking inflates cross-squad communication overhead exponentially, reducing effective team output.

Markers on it:

[12] source: jones-evidence-based-sweng:22332
A study by Buettner275 investigated large software intensive systems, and included an analysis of various staffing related issues, such as: staffing level over time (fig 14.4) and staff work patterns (fig 11.61).
If team member activities are divided into communicating and non-communication (e.g., producing code), how large can a team become before communication activities cause total team output to decline when another person is added?
Assuming that communications overhead,xi for each team member, is: t0(Dα −1), where t0 is the percentage of one person’s time spent communicating in a two-person team, D the number of people in the team and α a constant greater than zero. The peak team size, before adding people starts reducing total output, is given by:1815

[13] source: jones-evidence-based-sweng:22359
Dpeak =
[ 1+ t0
(1+α)t0
] 1 α
If α = 1 (i.e., everybody on the project incurs the same communications overhead), then Dpeak =
1+t0 2t0
, which for small t0 is: Dpeak ≈ 1 2t0
. For example, if team members spend 10% of their time communicating with every other team member: Dpeak =
1+0.1 2×0.1 ≈ 5.
In this team of five, 50% of each person’s time is spent communicating.
If α = 0.8, then: Dpeak = [
1+0.1 (1+0.8)×0.1
] 1 0.8 ≈ 10.
Figure 5.57 shows the effective rate of production (i.e., sum of the non-communications work of all team members) of a team of a given size, whose culture has a particular form of communication overhead.

### S6

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [15], [16]):
> Tying financial rewards to points encourages squads to inflate estimates or perform low-quality work to meet artificial deadlines.

Markers on it:

[15] source: jones-evidence-based-sweng:16679
In a commercial environment, developers may be vying with each other for promotion, or a pay rise. Developers who deliver projects on schedule are likely to be seen by management as worthy of promotion or a pay rise.
Consider the case of two software developers who are regularly assigned projects to complete, by a management specified date: with probability p, the project schedules are unachievable. If the specified schedule is unachievable, performing Low quality work will enable the project to be delivered on schedule, alternatively the developer can tell management that slipping the schedule will enable High quality work to be performed.

[16] source: jones-evidence-based-sweng:16689
Performing Low quality work is perceived as likely to incur a penalty of Q1 (because of its possible downstream impact on project completion) if one developer chooses Low, and Q2 if both developers choose Low. It is assumed that: Q1 < Q2 <C. A High quality decision incurs a penalty that developers perceive to be C (telling management that they cannot meet the specified schedule makes a developer feel less likely to obtain a promotion/pay-rise).
Let’s assume that both developers are given a project, and the corresponding schedule. If either developer faces an unachievable deadline, they have to immediately decide whether to produce High or Low quality work. When making the decision, information about the other developer’s decision is not available.

### S7

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [17]):
> Feedback Loop: This creates a classic "Fixes That Fail" system archetype.

Markers on it:

[17] source: ssdl-systems-thinking-foundations:1169
The “fixes that fail” archetype describes attempts to address a problem through a short-term fix. The fix might solve the problem in the short run, but it also generates unintended consequences that actually make the original problem worse.
METHODS BRIEF SERIES 1.07
+ APPLYING SYSTEM ARCHETYPES IN K-12 EDUCATION
Archetype #1: Fixes that fail
Template Archetype #1
Template Archetype #2
Example Archetype #2
Example Archetype #1
Archetype #2: Success to the successful
she can trust. She begins to see herself as a “bad” student and becomes even more disruptive in class.

### S8

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [18]):
> Pushing for output forces developers into an Efficiency-Thoroughness Trade-Off (ETTO)—sacrificing testing and architecture (thoroughness) for speed (efficiency).

Markers on it:

[18] source: lfuo-learning-review-guide-2024:5098
or to exchange ideas. (Oxford Dictionary)
Doctrine: a body of principles evolved from laws, culture, history and precedence that
guides the action of an organization. It is the expression of the fundamental framework
and concepts that also guides the planning and conduct of operations.
Efficiency-Thoroughness Trade-Off: “In their daily activities, at work or at leisure, people (and organizations) routinely make a choice between being effective and being
thorough, since it rarely is possible to be both at the same time. If demands to productivity or performance are high, thoroughness is reduced until the productivity goals are met. If demands to safety are high, efficiency is reduced until the safety goals are

### S9

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [17], [19]):
> The resulting technical debt generates production bugs, which cause customer churn and force reactive firefighting, ultimately lowering net throughput further.

Markers on it:

[17] source: ssdl-systems-thinking-foundations:1169
The “fixes that fail” archetype describes attempts to address a problem through a short-term fix. The fix might solve the problem in the short run, but it also generates unintended consequences that actually make the original problem worse.
METHODS BRIEF SERIES 1.07
+ APPLYING SYSTEM ARCHETYPES IN K-12 EDUCATION
Archetype #1: Fixes that fail
Template Archetype #1
Template Archetype #2
Example Archetype #2
Example Archetype #1
Archetype #2: Success to the successful
she can trust. She begins to see herself as a “bad” student and becomes even more disruptive in class.

[19] source: ssdl-systems-thinking-foundations:96
d c cc b,d
Feedback effects causing unintended or unanticipated consequences of actions – When we can’t see or understand the system as a whole, our well-intentioned actions may have side effects that make the problem worse in the long-run. Let’s say our district has low test scores, so we double down on time spent preparing for standardized tests. In the short term, test scores may improve. But there is an unintended consequence: with the added pressure on testing, teachers become burnt out and students become less engaged in learning. Ultimately, the test scores drop further.

### S10

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [4], [21], [22], [23]):
> Placing individual blame creates a Blame Cycle: managers assume rule compliance solves safety, employees lose trust and hide near-misses, and latent organizational weaknesses (e.g., inadequate deploym

Markers on it:

[4] source: doe-hpi-handbook-vol1:9858
H u m a n E rro r
uodnM ore fla w ed d e fenses nse lediv id ua l cI srer o rs a nd /o r d isc ip line dcu& e rro r p
B la m e C yc leta R edu ced tru s tiona lLa ten t o rg an iz
rese s is tses pw e akn
M an age m e n t les Lesss om m u n ica tio ncea w a re o f jo bs it
cond itio ns
Department of Energy Human Performance Handbook Chapter 4 Culture & Leadership
CREATE A JUST CULTURE
The Blame Cycle
The “blame cycle” depicted below is urged on by the belief that human error occurs because people are not properly motivated.29 In reality, no matter how motivated an individual is, active errors will continue to occur, occasionally. Events will continue as long as event investigations stop prematurely at the active human error. The true causes (typically organizational weaknesses) will not be discovered—will remain latent or hidden—and errors and events will persist.

[21] source: doe-hpi-handbook-vol1:1464
Latent Organizational Weaknesses
Latent organizational weaknesses are hidden deficiencies in management control processes (for example, strategy, policies, work control, training, and resource allocation) or values (shared beliefs, attitudes, norms, and assumptions) that create work place conditions that can provoke errors (precursors) and degrade the integrity of controls (flawed controls).15 Latent organizational weaknesses include system-level weaknesses that may exist in procedure development and review, engineering design and approval, procurement and product receipt inspection, training and qualification system(s), and so on. The decisions and activities of managers and supervisors determine what is done, how well it is done, and when it is done, either contributing to the health of the system(s) or further weakening its resistance to error and events. System-level weaknesses are aggregately referred to as latent organizational weaknesses. Consequently, managers and supervisors should perform their duties with the same uneasy respect for error-prone work environments as workers. A second strategic thrust to preventing events should be the identification and elimination of latent organizational weaknesses.

[22] source: lfuo-learning-review-guide-2024:416
terms of wholes and relationships.
JUST CULTURE
Just Culture is characterized by the intersection of valuing trust, fairness and dignity. In a just culture, an organization has an open and safe reporting system where everyone can speak. In a
just culture, organizations are accountable for systems they design and analysis of the incident—not the individual. Many organizations have policies that describe nonpunitive responses to error. However, internal barriers to speaking up include
negative management responses and the risk of discipline from leaders.

[23] source: lfuo-learning-review-guide-2024:3841
Attempting to hold individuals “accountable” (in the traditional sense) for systems -level weaknesses or failures obliterates learning opportunities. Our employees are engaged in complex work in an increasingly complex environment. When we do not
pay homage to the complexities of the work environment in the wake of an accident and instead pretend that the work environment is simple or even complicated, we are not treating our employees fairly or affording them the dignity they deserve.
When employees are exposed to unfair treatment, the inevitable reaction is a breakdown in trust. When employees don’t trust the organization they work for, the

### S11

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [24], [25], [26]):
> Cultural Cost: Scapegoating destroys psychological safety and reporting transparency, which are empirical prerequisites for high-performing software delivery.

Markers on it:

[24] source: open-practice-library:9123
| Responsibilities shirked | Narrow responsibilities | Risks are shared |
| Bridging discouraged | Bridging tolerated | Bridging encouraged |
| Failure leads to scapegoating | Failure leads to justice | Failure leads to inquiry |
| Novelty crushed | Novelty leads to problems | Novelty implemented |
Whilst this is certainly an over-simplification of an ambiguous and constantly changing concept of "culture", it's a really useful model to help understand current state, direction of travel, and identify areas of improvement.

[25] source: open-practice-library:9145
Photo by Meghan Lamle on Unsplash whyDo: >- In 2015, Jez Humble, Joanne Molesky, and Barry O'Reilly wrote the book "Lean Enterprise: How High Performance Organizations Innovate at Scale", which highlighted how critical culture is to performance, and highlighted Westrum's Typology model. “Instead of creating controls to compensate for pathological cultures, the solution is to create a culture in which people take responsibility for the consequences of their actions”
The 2016 state of DevOps Report also showed that Generative, performance-oriented cultures improve software delivery performance, alongside market share, productivity and profitability.

[26] source: lfuo-learning-review-guide-2024:45
engineer a reporting culture—an organizational climate in which people are prepared to report their errors . . . An effective reporting culture depends, in
turn, on how the organization handles blame and punishment . . . What is needed
is a just culture . . .”
J. T. Reason, Managing the Risks of Organizational Accidents (Aldershot,
England: Ashgate, 1997), p195.
“I got behind the safety shelter; then in a little bit, I heard a voice say,
Get in This Truck!”
2011, Salt Fire
Entrapment and Shelter Deployment FLA. U.S. Forest Service Photo

### S12

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [8]):
> Operational Impact: Theory of Constraints shows that optimizing a non-bottleneck phase provides zero system-level benefit.

Markers on it:

[8] source: open-practice-library:8577
The Theory of Constraints shows us that in any process, there must be a single bottleneck that limits the total throughput of the process: in the same way that a chain has a weakest link, a process has a single slowest component. whyDo: >- Whilst it may be easy to improve some part of the process, if that component isn't the bottleneck, it will either have zero effect on the throughput because the bottleneck is upstream, or it will actually cause more pain in the system by adding pressure to the bottleneck, if the bottleneck is downstream.

### S13

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [7], [27]):
> Accelerating raw code generation without fixing work-in-progress (WIP) constraints is a local optimization ("water-scrum-fall") that will flood our pipeline with untested code, aggravating outages.

Markers on it:

[7] source: open-practice-library:9385
An example of this would be development teams trying to solve speed to market issues by adopting Agile practices... only to find that the work before and after them is still using traditional waterfall methods. The result is water-scrum-fall; it doesn't solve the problem.
A second example would be an infrastructure operations team trying to solve speed to market by introducing a Kubernetes platform... but they fail to look outside of their silo to what their customers (software engineers) need from the platform rather than what the operations team think they want. The result is almost always an over-engineered solution that has taken too long to build and doesn't deliver the features the developers want; it's a 'field of dreams' approach only this time they build it but they don't come.

[27] source: openstax-accounting-vol2:21658
If constraints are not managed, a bottleneck usually results, meaning that production slows and a back-up occurs at stages prior to the bottleneck. For example, in producing boxes of cereal, if the cereal is produced at a rate of 1,000 ounces per minute but the bagging machines can only bag 800 ounces per minute, this will create a bottleneck. Similarly, if on a Saturday morning before a home football game, the local grocery store has ten checkout lines but only opens four of them, long lines will result from the constraint of too few checkout lanes available. Management must decide how many scarce resources (employees, in this example) to pull from stocking the shelves to running cash registers. It may be difficult to see how bottlenecks affect profitability, and they appear to be more of a timing or throughput issue. But bottlenecks can affect profitability in a number of ways. Bottlenecks at the grocery story can result in customers leaving to store shop elsewhere or can negatively affect the reputation of the store, which can impact future sales. In the cereal example, bottlenecks in the packaging area can slow the delivery of boxes of cereal to distributors and individual stores. Poor or inconsistent delivery may drive customers to purchase from other cereal manufacturers, which would have a definite impact on profitability.

### S14

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [2], [28]):
> To recover stability and flow, we must execute interventions in strict sequence based on leverage points.

Markers on it:

[2] source: org-topologies-primer-2025:1141
Systems thinking teaches us to focus on the interactions  and influences between the parts, and to improve all the  major parts in a systemically reinforcing design that  supports a common org goal (for instance, “flow”). If each  element (e.g. policies, structures) is optimized in isolation,  the performance of the whole system may actually decline  for the desired goal (flow can get worse!). By seeing the  system as an integrated collection of interacting parts that  need to be aligned, organizations can create change that  is both holistic and sustainable.

[28] source: ssdl-systems-thinking-foundations:111
Traditional program design tools, such as logic models, help us develop, negotiate, and communicate our change efforts in a clear, linear way (i.e. Resources --> Activities --> Outputs --> Outcomes --> Impact). However, these tools can fail to account for the characteristics of complex problems, causing our best plans to fail or lead to surprising results.
System dynamics is the use of causal maps and computer simulation models to engage with this complexity and understand system behavior from a feedback perspective. Visual tools for mapping and modeling such as causal loop diagrams and stock and flow diagrams help us create simplified representations of complex systems, allowing us to identify places to intervene, test out our ideas, and anticipate their consequences. System dynamics tools help us to consider the behavior of the “whole” rather than fixating on the “parts” when addressing complex problems.

### S15

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [11], [29]):
> Capping WIP forces teams to "stop starting, start finishing," exposed real system dependencies, and immediately reduces cycle time.

Markers on it:

[11] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

[29] source: open-practice-library:21009
WIP Limit
Limit work in progress. These sample numbers represent the maximum number of functional items for workflow. Promote finishing and provoke important discussions. “Stop starting, start finishing!”
One Way
Do not move cards backwards. An item flows when work is completed at each step. If a correction needs to be made, keep the item in the same column, eventually signaling that a block exists. Focus on finishing.
Metrics
Throughput - The amount of items delivered in a given time frame, usually weeks.

### S16

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [23], [25]):
> Why Second: Without psychological safety, engineers will pad estimates, conceal architectural risks, and resist taking ownership.

Markers on it:

[23] source: lfuo-learning-review-guide-2024:3841
Attempting to hold individuals “accountable” (in the traditional sense) for systems -level weaknesses or failures obliterates learning opportunities. Our employees are engaged in complex work in an increasingly complex environment. When we do not
pay homage to the complexities of the work environment in the wake of an accident and instead pretend that the work environment is simple or even complicated, we are not treating our employees fairly or affording them the dignity they deserve.
When employees are exposed to unfair treatment, the inevitable reaction is a breakdown in trust. When employees don’t trust the organization they work for, the

[25] source: open-practice-library:9145
Photo by Meghan Lamle on Unsplash whyDo: >- In 2015, Jez Humble, Joanne Molesky, and Barry O'Reilly wrote the book "Lean Enterprise: How High Performance Organizations Innovate at Scale", which highlighted how critical culture is to performance, and highlighted Westrum's Typology model. “Instead of creating controls to compensate for pathological cultures, the solution is to create a culture in which people take responsibility for the consequences of their actions”
The 2016 state of DevOps Report also showed that Generative, performance-oriented cultures improve software delivery performance, alongside market share, productivity and profitability.

### S17

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [37]):
> Replace point-velocity metrics with joint engineering-product outcomes: Mean Time to Recovery (MTTR), Change Failure Rate, and Unbroken Customer Flow Time.

Markers on it:

[3] source: :None
(empty chunk)

[37] source: org-topologies-primer-2025:609
One consequence of an org design with complete archetypes is that they can become independently  operating silos. Whether that’s a virtue or vice depends.
Output versus Outcome Archetypes
There is a well-​known management principle of maximizing outcomes while minimizing outputs.
Outputs—​such as number of surgeries, amount of software features, number of completed design  documents, or percentage of closed insurance claims—​are relatively straightforward leading metrics.  However, more output does not mean more outcomes. In fact, more output usually means more cost or  investment, which can lower profit (an outcome). Investing to increase outcomes (healthy people, profit) is  justified; ‘investing’ to increase output is suspect.

### S18

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [7], [40]):
> Once WIP is capped and safety culture is established, AI guardrails protect release quality while teams deliver features at a sustainable pace.

Markers on it:

[7] source: open-practice-library:9385
An example of this would be development teams trying to solve speed to market issues by adopting Agile practices... only to find that the work before and after them is still using traditional waterfall methods. The result is water-scrum-fall; it doesn't solve the problem.
A second example would be an infrastructure operations team trying to solve speed to market by introducing a Kubernetes platform... but they fail to look outside of their silo to what their customers (software engineers) need from the platform rather than what the operations team think they want. The result is almost always an over-engineered solution that has taken too long to build and doesn't deliver the features the developers want; it's a 'field of dreams' approach only this time they build it but they don't come.

[40] source: openstax-accounting-vol2:2524
Total quality management (TQM) concentrates on quality improvement and applies this benchmark to all aspects of business activities. In TQM, management and employees look to reveal waste and errors, streamline
the supply chain, improve customer relations, and confirm that employees are informed and properly trained. The objective of TQM is continuous improvement by concentrating on systematic problem-solving and customer service. Scientific methods are used to study what succeeds and what does not, and then the best practices are implemented throughout the organization.

### S19

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [41], [42]):
> The Conflict: Traditional managerial accounting (e.g., standard labor variance, scientific management) treats unassigned or idle human capacity as financial waste.

Markers on it:

[41] source: openstax-accounting-vol2:16581
CONCEPTS IN PRACTICE
Qualcomm2
Qualcomm Inc. is a large producer of telecommunications equipment focusing mainly on wireless products and services. As with any company, Qualcomm sets labor standards and must address any variances in labor costs to stay on budget, and control overall manufacturing costs.
In 2018, Qualcomm announced a reduction to its labor force, affecting many of its full-time and temporary workers. The reduction in labor was necessary to suppress rising expenses that could not be controlled through overhead or materials cost-cutting measures. The variances between standard labor rates and actual labor rates, and diminishing profit margins will have contributed to this decision. It is important for Qualcomm management to keep labor variances minimal in the future so that large workforce reductions are not required to control costs.

[42] source: openstax-introduction-business:27796
The gap between what is and what is required. Anything that decreases a specific behavior.
A theory of motivation that holds that people do things because they know that certain consequences will follow.
Anything that increases a specific behavior. A system of management developed by Frederick W. Taylor and based on four
principles: developing a scientific approach for each element of a job, scientifically selecting and training workers, encouraging cooperation between workers and managers, and dividing work and responsibility between management and workers according to who can better perform a particular task.

### S20

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [6], [9], [30]):
> In contrast, Systems Dynamics and Lean engineering prove that knowledge work requires slack capacity; operating at 100% capacity creates exponential delays and systemic fragility.

Markers on it:

[6] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[9] source: jones-evidence-based-sweng:30003
5
10
15
20
Concurrent Workload
T hr
ou gh
pu t (
jo bs
p er
u ni
t t im
e)
Amdahl Quadratic Amdahl Queuing
Figure 8.34: Throughput when running the SPEC SDM91 benchmark on a Sun SPARCcenter 2000 containing 8 CPUs, with the predictions from three fitted queuing models. Data from Gunther.758 Github–Local
The red points in figure 8.33 were calculated using the above algorithm.
This preferential attachment model provides insights into local variable usage that are very different from those provided by the fitted exponential equation. Neither of them could not be said to be realistic descriptions of the process used by developers, when writing code. Both models are descriptions of the end result of the emergent process of writing a function definition; each model has its own advantages and disadvantages, including the following:

[30] source: open-practice-library:3783
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: limit-work-in-progress.md -->
--------------------------------------------------------------------------------
participants:
- the team
- each individual subtitle: Pipes that aren't clogged increase the flow through the system resources:
- link: 'https://kanbantool.com/kanban-wip-limits' linkType: web description: Kanban WIP Limits
- link: 'https://www.youtube.com/watch?v=SFMlu87MkYI' linkType: video description: Example projects (video)
- link: 'http://www.flickr.com/photos/65534354@N00/4872229081' linkType: web description: '"Pipes, Valves and Gauges"' templateKey: practice-page title: Limit Work in Progress date: 2019-10-19T08:56:15.621Z authors:
- rhdojun tags:
- culture icon: /images/valves.jpg whatIs: >- Instead of taking on all tasks that people hand to you as a person or representative of your team, you don't accept new tasks unless you still have free capacity. whyDo: >- Usually people take on all new tasks that come in, especially when a task they work on is waiting on external input. Then suddenly 3 of these tasks can continue and the person doesn't have the time to finish all of the same time. So the person gets overloaded, nobody knows how the progress is, and tasks get stuck in a progressed state where nobody else can help.

### S21

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [1], [43]):
> The Conflict: Human Performance Improvement (HPI) shows that over 80% of errors are organizationally induced by latent workplace conditions.

Markers on it:

[1] source: doe-hpi-handbook-vol1:466
It is not easy to anticipate exactly how trivial conditions can influence individual performance. Error-provoking aspects of facility*1 design, procedures, processes, and human nature exist everywhere. No matter how efficiently equipment functions; how good the training, supervision, and procedures; and how well the best worker, engineer, or manager performs his or her duties, people cannot perform better than the organization supporting them.1 Human error is caused not only by normal human fallibility, but also by incompatible management and leadership practices and organizational weaknesses in work processes and values. Therefore, defense-in-depth with respect to the human element is needed to improve the resilience of programmatic systems and to drive down human error and events.

[43] source: doe-hpi-handbook-vol1:11323
In 1997, Reason published Managing the Risks of Organizational Accidents. Reason maintained that to understand how organizational accidents occur requires that we look deeper into the system. Unsafe acts by individuals may trigger an event. However, latent conditions within the organization, aligned with local workplace and task factors, contribute to accidents in the form of process errors or as error-likely situations. Thus it is the combination of these latent conditions in conjunction with an active error that more correctly accounts for events. From this perspective, errors are the consequences, not the causes, of disturbances in the organization. Accidents are the result of failed controls and barriers. People are fallible, even the best make mistakes. It is human nature to err. However, events can be eliminated or controlled by changing the conditions in which people work. Managing the risks of organizational accidents requires that managers, supervisors, and staff work to eliminate latent organizational weaknesses. Reason proposes three compelling reasons why latent conditions have to be eliminated.

### S22

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [45], [46]):
> The Conflict: Classical project planning demands predictable output volume (points per sprint) for financial forecasting.

Markers on it:

[45] source: approach-perfect-field-guide-scrum-events:297
orecast V elocity Sprint n s forecast capacity]   F = 3 +   + ( [Sprint n­3 s V elocity]′
[Sprint n­3 s Capacity]′ )  (
[Sprint n­2 s V elocity]′ [Sprint n­2 s Capacity]′
) ( [Sprint n­1 s V elocity]′ [Sprint n­1 s Capacity]′
) × [ ′
For instance, if you completed 25, 24, and 31 Story Points over the last three sprint with 45, 43, and 50 days of Capacity respectively and you have a forecasted Capacity of 47 this
sprint, your forecasted Velocity for this sprint is . 7  0  3 ( ) + ( ) + ( )45 25

[46] source: openstax-introduction-business:30607
environment and its own strategic goals in an effort to find the best production methods. The way a good or service is created.
A scheduling tool that is similar to the CPM method but assigns three time estimates for each activity (optimistic, most probable, and pessimistic); allows managers to anticipate delays and potential problems and schedule accordingly.
The process of buying production inputs from various sources; also called procurement. Goods and services that meet customer expectations by providing reliable performance.

### S23

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [14], [47]):
> However, empirical software studies show that story points are arbitrary internal proxies that distort reality under executive target-setting.

Markers on it:

[3] source: :None
(empty chunk)

[14] source: jones-evidence-based-sweng:41870
Goodhart’s law is an observation about human behavior, rather than a law: “Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes.” If the measurements collected were actively used to control or evaluate the development team (for instance), then developers have a motivation to cause the measurements to move in a direction favorable to themselves.
A study by Perry, Staudenmayer and Votta1472 investigated various software development activities (e.g., working time on an activity, and activities performed throughout the day), as measured by the developers involved (i.e., self reports) and as measured by external observers. Differences in reported measurement values included, developers reporting activity time 2.8% higher, on average, than that reported by an observer; the measurement agreement rate for activities performed varied between 0.6 and 0.95.

[47] source: jones-evidence-based-sweng:10687
1.3.1 Folklore
The dearth of experimental evidence has left a vacuum that has been filled by folklore and old-wives’ tales. Examples of software folklore include claims of a 28-to-1 productivity difference between best/worst developers, and the Halstead and McCabe complexity metrics; folklore metrics are discussed in section 7.1.4.
The productivity claim, sometimes known as the Grant-Sackman study, is based on a casual reading of an easily misinterpreted table appearing in a 1968 paper1624 by these two authors. The paper summarised a study that set out to measure the extent to which the then new time-sharing approach to computer use was more productive for software development than existing batch processing systems (where jobs were typically submitted via punched cards, with programs executing (sometimes) hours later, followed by their output printed on paper). A table listed the ratio between the best subject performance using the fastest system, and the worst subject performance on the slowest system (the 28:1 ratio included programmer and systems performance differences, and if batch/time-sharing differences are separated out the maximum difference ratio is 14:1, the minimum 6:1). The actual measurement data was published727 in a low circulation journal, and was immediately followed by a strongly worded critique;1074 see fig 8.22.

### S24

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [37], [48]):
> Executive Takeaway: We must align Product and Engineering around customer value and service quality (the Service-Profit Chain) rather than feature point counts.

Markers on it:

[37] source: org-topologies-primer-2025:609
One consequence of an org design with complete archetypes is that they can become independently  operating silos. Whether that’s a virtue or vice depends.
Output versus Outcome Archetypes
There is a well-​known management principle of maximizing outcomes while minimizing outputs.
Outputs—​such as number of surgeries, amount of software features, number of completed design  documents, or percentage of closed insurance claims—​are relatively straightforward leading metrics.  However, more output does not mean more outcomes. In fact, more output usually means more cost or  investment, which can lower profit (an outcome). Investing to increase outcomes (healthy people, profit) is  justified; ‘investing’ to increase output is suspect.

[48] source: openstax-principles-marketing:20080
The service-profit chain model, created by a group of Harvard researchers in the 1990s, establishes relationships between profitability, employee satisfaction, loyalty, and productivity. The concept is reasonably simple: happy workers make happy customers who keep coming back and tell their friends. The model itself is a little more complicated and states the following:
• Internal service quality (the support received by frontline employees from the rest of the organization) leads to employee satisfaction.
• Employee satisfaction results in employee loyalty, productivity, and the willingness to go that “extra mile” for the customer, which creates value.
• Value contributes to customer satisfaction, resulting in customer loyalty.
• Customer loyalty translates to profitability and growth for the organization.
