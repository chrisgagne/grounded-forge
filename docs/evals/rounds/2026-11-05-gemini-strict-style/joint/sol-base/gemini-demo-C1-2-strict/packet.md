# gemini-demo-C1-2-strict

## The whole answer, for context


I need a two-page memo for the CEO that says what's actually going on here, what to change first and why that first, and where the thinking you're drawing on disagrees with itself.

Answer here in the chat.

MEMORANDUM
TO: Chief Executive Officer
FROM: Chief Technology Officer
DATE: November 4, 2026
SUBJECT: Operational Diagnosis, Prioritized Action Plan, and Theoretical Tensions in Engineering
1. What Is Actually Going On Here? (Systemic Diagnosis)
Resource Utilization vs. Flow Capacity:
Work in progress (WIP) limits frame the capacity of a team's workflow at any moment to establish stable and predictable delivery[1:open-practice-library]. When individuals take on all incoming tasks without limiting work in progress, they become overloaded, tasks get stuck, and overall responsiveness declines[2:open-practice-library]. Multitasking does not work, and reducing the batch size of efforts allows teams to finish work faster[3:open-kanban]. Directing optimization toward high employee utilization rather than work item flow results in work getting done slower even when everyone is busy[4:open-practice-library][5:open-practice-library]. In Scrum, a development team cannot make a firm commitment to deliver more than historical performance supports; attempting to do so leads to burnout, poor quality, loss of trust, and attempts at gaming the system[6:approach-perfect-field-guide-scrum-events].
My inference: Our rule requiring zero idle time by assigning developers to two or three squads simultaneously inflates work in progress and context switching across our nine squads.
My inference: Planning 40 story points per sprint when historical capacity supports only 25 points forces sprint overflow, creates chronic backlog carryover, and degrades software quality.
Perverse Incentives & Target Pressure:
Implementing unrealistic goals and high-pressure targets from the top down can create undue organizational pressure, leading to compromised standards and unethical or dysfunctional behaviors[7:openstax-principles-management]. Linking extrinsic rewards to target achievement shapes team dynamics and can damage morale[8:open-practice-library]. In organizational design, maximizing output metrics does not equate to maximizing outcomes, as producing more output often increases investment costs without improving overall business outcomes[9:org-topologies-primer-2025].
My inference: Tying squad leads' bonuses to a stretch target of 40% increased throughput incentivizes leads to push raw feature volume over technical rigor, accelerating bug creation.
My inference: Marketing's demand for weekly feature releases pushes the engineering organization past its empirical delivery capacity, shifting defect resolution into customer-facing churn.
Blame Culture vs. Systemic Root Causes:
Complex systems fail in complex ways, and limiting accident investigations to individual operator error or the last step in a process leads to the false belief that the problem is solved while leaving unresolved organizational system problems[10:open-practice-library][11:caib-report-vol1][12:caib-report-vol1]. Human error is a symptom of failure and latent organizational conditions, not the primary cause of system breakdown[13:doe-hpi-handbook-vol1][14:doe-hpi-handbook-vol1][15:doe-hpi-handbook-vol2]. Investigating incidents by asking what people could or should have done fails to explain why their actions made sense to them at the time[16:doe-hpi-handbook-vol1][17:doe-hpi-handbook-vol2]. Punishing or shaming employees for honest errors undermines psychological safety, damages trust, and suppresses the open reporting of errors[18:open-practice-library][19:doe-hpi-handbook-vol1][20:doe-hpi-handbook-vol2][21:lfuo-learning-review-guide-2024].
My inference: Placing the developer on a performance plan following the customer portal outage treats a single person as the root cause, ignoring underlying deployment and testing weaknesses.
My inference: This punitive action creates a blame cycle that discourages developers from transparently reporting risks or production issues.
The Myth of Local Tooling Fixes:
Attempting to solve delivery speed problems by introducing tools or platform changes in isolation without addressing surrounding workflow constraints or customer needs results in over-engineered solutions that fail to solve the core problem[22:open-practice-library]. The Theory of Constraints establishes that "Any improvements made anywhere besides the bottleneck are an illusion."[23:open-practice-library][24:open-practice-library].
My inference: Relying on AI coding tools to solve both velocity expectations and defect rates fails to address our primary organizational bottleneck, which is excessive work in progress and fragmented team structures.
No source in this notebook covers the specific impact of AI coding tools on software throughput or defect rates.
2. What to Change First and Why That First (Prioritized Action Plan)
Phase 1 (Immediate): Establish a Just Culture and Conduct Blameless Postmortems
A blameless postmortem evaluates incident timelines and contributing factors without making harmful judgments, focusing on why decisions made sense in real time[25:open-practice-library][26:open-practice-library]. Applying the substitution test evaluates whether another well-motivated individual with similar skills and training would have committed the same error under identical circumstances[27:doe-hpi-handbook-vol1][28:doe-hpi-handbook-vol1][29:doe-hpi-handbook-vol2]. In a just culture, management holds the organization accountable for the systems it designs rather than punishing individual errors[30:doe-hpi-handbook-vol1][31:lfuo-learning-review-guide-2024].
My inference: We must immediately take the release developer off the performance plan and re-evaluate the four-hour outage using a blameless postmortem framework.
My inference: This must be changed first because without restoring psychological safety, engineers will conceal risks and game metrics, preventing any further operational improvements.
Phase 2 (Near-Term): Restructure Teams for Single-Squad Focus and Cap Sprint Capacity
Organizing work into complete, multi-skilled cross-functional units increases flow and reduces cross-unit dependencies compared to fragmented functional resource allocation[32:org-topologies-primer-2025][33:org-topologies-primer-2025]. Limiting work in progress and keeping team members focused on finishing current work before starting new items stabilizes workflow and reduces cycle times[1:open-practice-library][34:open-practice-library][35:open-practice-library].
My inference: We should eliminate the zero-idle-time rule, assign developers dedicatedly to single squads, and cap sprint planning at our historical throughput of 25 points.
Phase 3 (Medium-Term): Align Priorities via Value Stream Constraints and Cost of Delay
The Theory of Constraints requires identifying the single bottleneck limiting throughput, exploiting it, and subordinating all other process steps to that constraint[36:open-practice-library]. Weighted Shortest Job First (WSJF) prioritizes backlog items by dividing cost of delay by job size to deliver high-value, smaller jobs first[37:open-practice-library][38:open-practice-library].
My inference: Product, Marketing, and Engineering must adopt WSJF prioritization to select high-value features collaboratively rather than demanding arbitrary weekly output targets.
3. Where the Thinking Disagrees With Itself (Theoretical Tensions)
Fixed-Iteration Planning vs. Continuous Flow Systems:
Scrum prescribes fixed-length timeboxed iterations (Sprints) with defined Sprint Goals and committed Sprint Backlogs[39:approach-perfect-field-guide-scrum-events][40:scrum-guide-2020][41:scrum-guide-2020]. In contrast, Kanban advocates for continuous pull replenishment, explicit WIP limits per workflow column, and delivering items on demand as soon as they are ready rather than waiting for batch iteration boundaries[1:open-practice-library][35:open-practice-library][42:open-practice-library].
My inference: Literature on agile practices contains a fundamental tension regarding whether software teams perform best under fixed batch timeboxes or continuous pull-based flow.
Individual Accountability vs. Systemic Just Culture:
Traditional management and incentive frameworks emphasize tying individual rewards strictly to job performance, enforcing individual performance-reward contingencies, and maintaining top-down targets[8:open-practice-library][43:openstax-introduction-business][44:openstax-organizational-behavior]. Conversely, Just Culture, High Reliability Organization (HRO), and Human Performance Improvement (HPI) literature argue that individual actions are shaped by organizational systems, and that holding individuals accountable for systemic failures destroys trust and learning[11:caib-report-vol1][13:doe-hpi-handbook-vol1][14:doe-hpi-handbook-vol1][31:lfuo-learning-review-guide-2024].
My inference: Management theory is divided between holding individuals directly responsible for operational outcomes versus treating individual actions as downstream products of system design.
Resource Utilization vs. Flow Efficiency:
Classical administrative theories and Resource Topologies prioritize 100% resource utilization to ensure no personnel or machine capacity is idle[45:org-topologies-primer-2025][46:openstax-organizational-behavior]. Conversely, Lean manufacturing, Kanban, and Theory of Constraints demonstrate that operating at 100% capacity creates severe queueing, increases lead time, and slows total system throughput[2:open-practice-library][3:open-kanban][4:open-practice-library].
My inference: Executive management assumptions favoring full human resource utilization directly contradict operational flow models that require slack capacity to maintain speed.
Efficiency-Thoroughness Trade-Off (ETTO):
System safety and ergonomics literature highlights the Efficiency-Thoroughness Trade-Off, recognizing that individuals and organizations face inherent goal conflicts between production speed and safety or quality precautions[47:lfuo-learning-review-guide-2024][48:lfuo-learning-review-guide-2024].
My inference: Demanding simultaneous increases in feature output speed and bug elimination represents an unresolvable operational trade-off unless workload constraints are reduced.
💡 Would you like to draft a 15-minute executive briefing slide deck outline based on this memo to prepare for your upcoming board or leadership meeting?





## Sentences to grade

### S1

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [1]):
> Work in progress (WIP) limits frame the capacity of a team's workflow at any moment to establish stable and predictable delivery.

Markers on it:

[1] source: open-practice-library:21107
Work In Progress (WIP) represent the number of work items that a team is currently working on in each stage. This limit frames the capacity of the teams's workflow at any moment and helps to identify bottlenecks. This value will help us to define a stable workflow and then a predictable delivery. whyDo: >- Kanban applies in situations where work arrives in an unpredictable fashion and/or when work items should be deployed as soon as they are ready, rather than waiting for other work items.
This framework helps you to:

### S2

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [2]):
> When individuals take on all incoming tasks without limiting work in progress, they become overloaded, tasks get stuck, and overall responsiveness declines.

Markers on it:

[2] source: open-practice-library:3783
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

### S3

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3]):
> Multitasking does not work, and reducing the batch size of efforts allows teams to finish work faster.

Markers on it:

[3] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

### S4

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [7]):
> Implementing unrealistic goals and high-pressure targets from the top down can create undue organizational pressure, leading to compromised standards and unethical or dysfunctional behaviors.

Markers on it:

[7] source: openstax-principles-management:5621
If the end (terminal) value creates undue pressures and is unrealistic and unobtainable, then the means (instrumental) value would likely create tension and unethical behavior as well. This example in some ways mirrors what actually recently happened at Wells Fargo & Company—an American international banking and financial services holding company headquartered in San Francisco. High pressure and unrealistic sales goals were adopted and implemented from the top down in that organization. A result was that members of that sales force lied, pressured, and misled loyal customers to buy bogus financial products to meet unrealistic sales goals. Such actions when discovered led to and revealed illegal and unethical actions from not only the sales professionals but officers at the top of that organization. Ultimately, the CEO was pressured to resign, 5,300 employees were fired, and several lawsuits ensued.15

### S5

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [10], [11], [12]):
> Complex systems fail in complex ways, and limiting accident investigations to individual operator error or the last step in a process leads to the false belief that the problem is solved while leaving

Markers on it:

[10] source: open-practice-library:None
- link: https://github.com/openpracticelibrary/opl-media/blob/master/images/technical-debt-cycle.png?raw=true
- link: https://github.com/openpracticelibrary/opl-media/blob/master/images/tech-debt-radar.jpg?raw=true resources:
- link: https://www.linkedin.com/pulse/when-your-tech-debt-comes-due-kevin-scott/ linkType: web description: Linkedin's Project Inversion participants: [] area: delivery-measure-and-learn perspectives: []
--------------------------------------------------------------------------------

[11] source: caib-report-vol1:352
In order to understand the findings and recommendations in this report, it is important to appreciate the way the Board looked at this accident. It is our view that complex systems almost always fail in complex ways, and we believe it would be wrong to reduce the complexities and weaknesses associated with these systems to some simple explanation. Too often, accident investigations blame a failure only on the last step in a complex process, when a more comprehensive understanding of that process could reveal that earlier steps might be equally or even more culpable. In this Board's opinion, unless the technical, organizational, and cultural recommendations made in this report are implemented, little will have been accomplished to lessen the chance that an-

[12] source: caib-report-vol1:20531
22 Changing personnel is a typical response after an organization has some kind of harmful outcome. It has great symbolic value. A change in personnel points to individuals as the cause and removing them gives the false impression that the problems have been solved, leaving unresolved organizational system problems. See Scott Sagan, The Limits of Safety. Princeton: Princeton University Press, 1993.
Diane Vaughan, The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA (Chicago: University of Chicago Press. 1996).

### S6

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [22]):
> Attempting to solve delivery speed problems by introducing tools or platform changes in isolation without addressing surrounding workflow constraints or customer needs results in over-engineered solut

Markers on it:

[22] source: open-practice-library:9385
An example of this would be development teams trying to solve speed to market issues by adopting Agile practices... only to find that the work before and after them is still using traditional waterfall methods. The result is water-scrum-fall; it doesn't solve the problem.
A second example would be an infrastructure operations team trying to solve speed to market by introducing a Kubernetes platform... but they fail to look outside of their silo to what their customers (software engineers) need from the platform rather than what the operations team think they want. The result is almost always an over-engineered solution that has taken too long to build and doesn't deliver the features the developers want; it's a 'field of dreams' approach only this time they build it but they don't come.

### S7

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [25], [26]):
> A blameless postmortem evaluates incident timelines and contributing factors without making harmful judgments, focusing on why decisions made sense in real time.

Markers on it:

[25] source: open-practice-library:19780
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: blameless-postmortem.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Blameless Postmortem subtitle: Turn incident into an investment in future reliability date: 2022-03-22T11:10:08.413Z authors:
- jfilipcz tags:
- learn mobiusTag: delivery icon: /images/markus-winkler-afw1hht0nss-unsplash.jpg whatIs: >- Blameless Postmortem is a post-incident practice assessing an incident or other types of outages, its timeline, environment conditions, and all possible factors that lead an incident to happen. A postmortem typically also covers incident timeline and all factors that in a given organization generate incident, and impacts operators behavior before, during and after the outage has happened. Practice allows participants and stakeholders to quickly form conclusions on what were the most important factors contributing to the incident. It also serves a learning purpose, both by providing in depth experience for participants and by producing a postmortem summary which can be shared with all interested parties. A postmortem can be treated as the evolution of a Root Cause Analysis (RCA) which is done in almost all major IT support organizations.

[26] source: open-practice-library:19794
The major difference between an RCA and Blameless Postmortem is the way both of them are run, with the later putting emphasis not only establishing the root cause but also ensuring that there’s no form of possibly harmful judgement being made along the way. Often a postmortem is also carried out in a less formalized manner, making sure that the actual story comes before documentation.
“Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future.” whyDo: >- A Blameless Postmortem serves couple of important purposes:

### S8

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [32], [33]):
> Organizing work into complete, multi-skilled cross-functional units increases flow and reduces cross-unit dependencies compared to fragmented functional resource allocation.

Markers on it:

[32] source: org-topologies-primer-2025:446
2. Multi-​Skill Units (cross-​functional teams) provide more flow and  responsiveness than Functional Units. Example: Surgical Team of doctors and  nurses. Multi-​skill Units are incomplete, meaning they do not contain all the  skills required to deliver value end-​to-​end. They co-​exist with functional units  and other teams on whom they depend to deliver complete value. Example:  The Surgical Team relying on Post-​Op Care Team, and both together needed  for a complete service for the patient.

[33] source: org-topologies-primer-2025:919
specialists. Fast delivery of proven worth with minimal 
change or learning. Fast delivery of uncertain results, to seek, 
change, discover, and adapt.
Goal/Focus Maximizing resource use, specialization. Maximizing output, predictability. Maximizing outcome, innovation.
Value Creation Fragmented and reliant on multiple 
handoffs and coordination. Narrowly focused on specific capabilities. Flexible, holistic, and novel.
Dependencies High; units depend on coordination 
across functional silos. Moderate; units coordinate across

### S9

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [1], [34], [35]):
> Limiting work in progress and keeping team members focused on finishing current work before starting new items stabilizes workflow and reduces cycle times.

Markers on it:

[1] source: open-practice-library:21107
Work In Progress (WIP) represent the number of work items that a team is currently working on in each stage. This limit frames the capacity of the teams's workflow at any moment and helps to identify bottlenecks. This value will help us to define a stable workflow and then a predictable delivery. whyDo: >- Kanban applies in situations where work arrives in an unpredictable fashion and/or when work items should be deployed as soon as they are ready, rather than waiting for other work items.
This framework helps you to:

[34] source: open-practice-library:21009
WIP Limit
Limit work in progress. These sample numbers represent the maximum number of functional items for workflow. Promote finishing and provoke important discussions. “Stop starting, start finishing!”
One Way
Do not move cards backwards. An item flows when work is completed at each step. If a correction needs to be made, keep the item in the same column, eventually signaling that a block exists. Focus on finishing.
Metrics
Throughput - The amount of items delivered in a given time frame, usually weeks.

[35] source: open-practice-library:21086
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: kanban.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Kanban subtitle: Visualized workflow management method to maximize efficiency and become more agile. date: 2020-09-15T12:02:15.251Z authors:
- rmarting mobiusTag: delivery icon: /images/kanbanoriginal.png whatIs: >- Kanban is a framework used to implement agile software development based in the following practices:
* Visualize the workflow
* Limit Work in Progress (WIP)
* Manage flow
* Make Process Policies Explicit
* Feedback loops

### S10

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [36]):
> The Theory of Constraints requires identifying the single bottleneck limiting throughput, exploiting it, and subordinating all other process steps to that constraint.

Markers on it:

[36] source: open-practice-library:8611
Stage 1: Identify the constraint. Look at where "Work In Progress" (WIP) is piling up.
Stage 2: Exploit the constraint. Are there any quick improvements you can make to the throughput of this stage? This is essentially "making the most of what you have". Check to see if you've solved the constraint and moved the bottleneck somewhere else.
Stage 3: Subordinate the constraint. Look at the rest of the process. Are other stages really aligned with this stage? Is there something another stage could do that could improve the flow through this stage? Maybe other stages could add a little more documentation, make a few tweaks to their process, or take on some of the work? Check to see if you've solved the constraint and moved the bottleneck somewhere else.

### S11

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [39], [40], [41]):
> Scrum prescribes fixed-length timeboxed iterations (Sprints) with defined Sprint Goals and committed Sprint Backlogs.

Markers on it:

[39] source: approach-perfect-field-guide-scrum-events:78
1½–4 hours per week. Newer backlogs usually need more refinement.
10% of the Development Team’s Capacity .
© 2020, Approach Perfect, Limited. https://approachperfect.com 2
The Sprint  
Also known as an “Iteration” in Extreme Programming.
Goal  
• Deliver a usable, potentially-releasable product Increment that meets the Definition of “Done” ( ap.tips/dod ) and accomplishes the Sprint Goal .
Timing  
• 1–4 weeks. (Agile principles #1, 3, and 7; ap.tips/principles ) 2-week Sprints are increasingly the most common.
• Each sprint starts immediately after the last ends. Don’t extend the sprint duration.

[40] source: scrum-guide-2020:139
3
Scrum Definition
Scrum is a lightweight framework that helps people, teams and organizations generate value through
adaptive solutions for complex problems.
In a nutshell, Scrum requires a Scrum Master to foster an environment where:
1. A Product Owner orders the work for a complex problem into a Product Backlog.
2. The Scrum Team turns a selection of the work into an Increment of value during a Sprint.
3. The Scrum Team and its stakeholders inspect the results and adjust for the next Sprint.

[41] source: scrum-guide-2020:446
Topic Three: How will the chosen work get done?
For each selected Product Backlog item, the Developers plan the work necessary to create an Increment
that meets the Definition of Done. This is often done by decomposing Product Backlog items into
smaller work items of one day or less. How this is done is at the sole discretion of the Developers. No
one else tells them how to turn Product Backlog items into Increments of value.
9
The Sprint Goal, the Product Backlog items selected for the Sprint, plus the plan for delivering them are

### S12

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [1], [35], [42]):
> In contrast, Kanban advocates for continuous pull replenishment, explicit WIP limits per workflow column, and delivering items on demand as soon as they are ready rather than waiting for batch iterati

Markers on it:

[1] source: open-practice-library:21107
Work In Progress (WIP) represent the number of work items that a team is currently working on in each stage. This limit frames the capacity of the teams's workflow at any moment and helps to identify bottlenecks. This value will help us to define a stable workflow and then a predictable delivery. whyDo: >- Kanban applies in situations where work arrives in an unpredictable fashion and/or when work items should be deployed as soon as they are ready, rather than waiting for other work items.
This framework helps you to:

[35] source: open-practice-library:21086
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: kanban.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Kanban subtitle: Visualized workflow management method to maximize efficiency and become more agile. date: 2020-09-15T12:02:15.251Z authors:
- rmarting mobiusTag: delivery icon: /images/kanbanoriginal.png whatIs: >- Kanban is a framework used to implement agile software development based in the following practices:
* Visualize the workflow
* Limit Work in Progress (WIP)
* Manage flow
* Make Process Policies Explicit
* Feedback loops

[42] source: open-practice-library:20967
Functional Item
“Between dogs and camels, all things are animals. You should avoid rats and Elephants” - Although there is variability in the size of the items, we avoid the extremes. A functional item generates value, each card on the board represents a delivery of value perceived by the business. if you want a dog, it’s leg, tail or head alone does not generate value.
Replenishment
Replenishment is the act of understanding and committing to demand. It is like a wedding - after the commitment point it is not desirable to give up the item (although it may happen ☹️ ). Kanban is a pull system - Frequent replenishment is more agile, on-demand replenishment is most agile!

### S13

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [8], [43], [44]):
> Traditional management and incentive frameworks emphasize tying individual rewards strictly to job performance, enforcing individual performance-reward contingencies, and maintaining top-down targets.

Markers on it:

[8] source: open-practice-library:12750
However there are some limitations to this framework:
* Focuses on ‘What’ not ‘How’
* It’s a time-consuming process to craft
* The pressure to meet objectives can damage morale and retention
* Link to extrinsic rewards shapes team dynamics in new ways howTo: >- 1﻿. Leadership team define Company Objectives for a cycle (typically 12 months) and share widely throughout the organisation.
2﻿. Leaders at team level then set individual Objectives (privately)
3﻿. Employees then have autonomy in how they aim to achieve these objectives. resources:

[43] source: openstax-introduction-business:26585
1. The link between effort and performance, or the strength of the individual’s expectation that a certain amount of effort will lead to a certain level of performance
2. The link between performance and outcome, or the strength of the expectation that a certain level of performance will lead to a particular outcome
3. The link between outcomes and individual needs, or the degree to which the individual expects the anticipated outcome to satisfy personal needs. Some outcomes have more valence, or value, for individuals than others do.

[44] source: openstax-organizational-behavior:20152
Strategic contingencies A requirement of the activities of one subunit that is affected by the activities of other subunits.
Utilitarian power Power based on performance-reward contingencies; for example, a person will comply with a supervisor in order to receive a pay raise or promotion.
Work centrality The more interconnected subunit A is with other subunits in the organization, the more central it is.
Work to rule Occurs when employees diligently follow every work rule and policy statement to the letter; this typically results in the organization’s grinding to a halt as a result of the many and often conflicting rules and policy statements.

### S14

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [11], [13], [14], [31]):
> Conversely, Just Culture, High Reliability Organization (HRO), and Human Performance Improvement (HPI) literature argue that individual actions are shaped by organizational systems, and that holding i

Markers on it:

[11] source: caib-report-vol1:352
In order to understand the findings and recommendations in this report, it is important to appreciate the way the Board looked at this accident. It is our view that complex systems almost always fail in complex ways, and we believe it would be wrong to reduce the complexities and weaknesses associated with these systems to some simple explanation. Too often, accident investigations blame a failure only on the last step in a complex process, when a more comprehensive understanding of that process could reveal that earlier steps might be equally or even more culpable. In this Board's opinion, unless the technical, organizational, and cultural recommendations made in this report are implemented, little will have been accomplished to lessen the chance that an-

[13] source: doe-hpi-handbook-vol1:466
It is not easy to anticipate exactly how trivial conditions can influence individual performance. Error-provoking aspects of facility*1 design, procedures, processes, and human nature exist everywhere. No matter how efficiently equipment functions; how good the training, supervision, and procedures; and how well the best worker, engineer, or manager performs his or her duties, people cannot perform better than the organization supporting them.1 Human error is caused not only by normal human fallibility, but also by incompatible management and leadership practices and organizational weaknesses in work processes and values. Therefore, defense-in-depth with respect to the human element is needed to improve the resilience of programmatic systems and to drive down human error and events.

[14] source: doe-hpi-handbook-vol1:11323
In 1997, Reason published Managing the Risks of Organizational Accidents. Reason maintained that to understand how organizational accidents occur requires that we look deeper into the system. Unsafe acts by individuals may trigger an event. However, latent conditions within the organization, aligned with local workplace and task factors, contribute to accidents in the form of process errors or as error-likely situations. Thus it is the combination of these latent conditions in conjunction with an active error that more correctly accounts for events. From this perspective, errors are the consequences, not the causes, of disturbances in the organization. Accidents are the result of failed controls and barriers. People are fallible, even the best make mistakes. It is human nature to err. However, events can be eliminated or controlled by changing the conditions in which people work. Managing the risks of organizational accidents requires that managers, supervisors, and staff work to eliminate latent organizational weaknesses. Reason proposes three compelling reasons why latent conditions have to be eliminated.

[31] source: lfuo-learning-review-guide-2024:416
terms of wholes and relationships.
JUST CULTURE
Just Culture is characterized by the intersection of valuing trust, fairness and dignity. In a just culture, an organization has an open and safe reporting system where everyone can speak. In a
just culture, organizations are accountable for systems they design and analysis of the incident—not the individual. Many organizations have policies that describe nonpunitive responses to error. However, internal barriers to speaking up include
negative management responses and the risk of discipline from leaders.

### S15

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [45], [46]):
> Classical administrative theories and Resource Topologies prioritize 100% resource utilization to ensure no personnel or machine capacity is idle.

Markers on it:

[45] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[46] source: openstax-organizational-behavior:2418
Next, Argyris turns his attention to the defining characteristics of traditional work organizations. In particular, he argues that in the pursuit of efficiency and effectiveness, organizations create work situations aimed more at getting the job done than at satisfying employees’ personal goals. Examples include increased task specialization, unity of command, a rules orientation, and other things aimed at turning out a standardized product with standardized people. In the pursuit of this standardization, Argyris argues, organizations often create work situations with the following characteristics:

### S16

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [2], [3], [4]):
> Conversely, Lean manufacturing, Kanban, and Theory of Constraints demonstrate that operating at 100% capacity creates severe queueing, increases lead time, and slows total system throughput.

Markers on it:

[2] source: open-practice-library:3783
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

[3] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

[4] source: open-practice-library:3823
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: manage-flow.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Manage Flow subtitle: Optimize the processing work items date: 2019-10-19T09:24:08.129Z authors:
- rhdojun tags:
- culture mobiusTag: foundation icon: /images/pullstuckcar.jpg whatIs: Direct the focus of optimization on work items, e.g. tasks, problems, process steps, instead of the people. That means metrics also need to focus on work items, not on people. whyDo: >- Everybody already experienced a few times in their life that it is totally possible that everybody is busy to the point of being overworked but the work gets done slower and slower.

### S17

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [47], [48]):
> System safety and ergonomics literature highlights the Efficiency-Thoroughness Trade-Off, recognizing that individuals and organizations face inherent goal conflicts between production speed and safet

Markers on it:

[47] source: lfuo-learning-review-guide-2024:1099
we can about this accident.”
If we can agree that information is the life blood of safety, we should do all that we
can to encourage and protect it. We need to begin by believing that our employees
were well intended and acted based on their knowledge of the environment. Our employees always face conflicting goals and tensions between production and efficiency2. We need to know about these pressures. Blaming employees prevents
us from learning. Blaming employees can be a form of the Fundamental Attribution Error (see Handout C FLA “Watch Outs” on pages 90-91). It is essential that we gain a more complete understanding of the conditions of influence so that we can learn

[48] source: lfuo-learning-review-guide-2024:3857
trainings, procedures, the production incentives and the safety-vs.-production values of the workplace. In this culture, management holds itself accountable for how it manages these system- and culturally created artifacts, especially the safety-
vs.-production values of the workplace.
Accountability is a principle focus. Accountability means to give an honest account. In a Just Culture, there is consensus among all employees that information
(learning) is the lifeblood of safety. If our employees won’t tell us what happened, the probability that we will be able to improve as an organization and act to prevent similar accidents in the future is greatly reduced. Most importantly, employees and administrators openly share stories of how they balance the tradeoffs between safety
