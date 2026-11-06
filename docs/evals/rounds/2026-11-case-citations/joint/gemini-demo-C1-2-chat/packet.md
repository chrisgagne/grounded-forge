# gemini-demo-C1-2-chat

## The whole answer, for context


I need a two-page memo for the CEO that says what's actually going on here, what to change first and why that first, and where the thinking you're drawing on disagrees with itself.

Answer here in the chat.

MEMORANDUM
TO: Chief Executive Officer
FROM: Chief Technology Officer
DATE: October 31, 2026
SUBJECT: Systemic Diagnostic & Strategic Action Plan: Engineering Flow, Quality, and Operational Governance
Executive Summary & Diagnostic: "What Is Actually Going On Here"
Our current operational crisis—sprint overruns, escalating churn from production bugs, department friction, and recent outages—is not caused by developer apathy or insufficient coding speed. It is the predictable result of a systemic design failure. We are running our software organization on flawed operational assumptions that systematically generate bottleneck queues, incentivize quality compromises, and create severe single-point failures[1:doe-hpi-handbook-vol1][2:doe-hpi-handbook-vol1][3:org-topologies-primer-2025].
Below is the systemic diagnosis across four key organizational dynamics:
1. The Utilization Trap & Queuing Chaos (Operating as a Resource Topology)
Our rule that "nobody is idle," which splits developers across two or three squads simultaneously, is the primary driver of our delivery collapse[3:org-topologies-primer-2025][4:open-practice-library]. In organizational design terminology, we are operating in a Resource Topology—a model that attempts to maximize local labor utilization ("keeping people 100% busy") rather than value flow[3:org-topologies-primer-2025][5:org-topologies-primer-2025].
Queuing Theory (Little’s Law) dictates that as resource utilization approaches 100%, queue times and lead times increase exponentially (Cycle Time=WIP/Throughput)[6:open-practice-library]. By forcing engineers onto multiple squads, we inflate Work-In-Progress (WIP) and generate massive context-switching overhead[4:open-practice-library][7:open-kanban].
Furthermore, software development communication overhead grows non-linearly with team interdependencies (D
peak
	​

 thresholds)[8:jones-evidence-based-sweng]. Because our 60 engineers are fragmented across 9 squads, individual focus is destroyed, handover friction spikes, and velocity stalls[4:open-practice-library][7:open-kanban][8:jones-evidence-based-sweng]. A system with 100% busy people inevitably yields 0% flow efficiency[3:org-topologies-primer-2025][9:open-practice-library].
2. Goodhart’s Law & Perverse Incentives (The 40% Stretch Target)
Tying squad leads' bonuses to an arbitrary "stretch" target of 40% more throughput by Q1 triggers Goodhart’s Law: "When a measure becomes a target, it ceases to be a good measure"[10:open-practice-library][11:jones-evidence-based-sweng].
Expecting a clogged system to deliver 40% more throughput forces engineers into an Efficiency-Thoroughness Trade-Off (ETTO)[12:lfuo-learning-review-guide-2024]. When output volume is tied to financial compensation, teams systematically sacrifice thoroughness—skipping automated testing, truncating code reviews, and taking architectural shortcuts[12:lfuo-learning-review-guide-2024][13:openstax-organizational-behavior][14:openstax-principles-management].
The result is a surge in technical debt and production defects[15:open-practice-library]. Marketing correctly observes that churn is driven by bugs, but engineering is being explicitly incentivized to generate those bugs to meet volume targets[13:openstax-organizational-behavior][14:openstax-principles-management][15:open-practice-library][16:doe-hpi-handbook-vol1].
3. The Blame Cycle vs. Systemic Safety (The Postmortem Failure)
Placing the developer who merged the bad release on a Performance Improvement Plan (PIP) is a critical organizational mistake[17:caib-report-vol1][18:doe-hpi-handbook-vol2].
Human Performance Improvement (HPI) and Just Culture research demonstrate that human error is a symptom of underlying system weakness, not the root cause[1:doe-hpi-handbook-vol1][2:doe-hpi-handbook-vol1][19:doe-hpi-handbook-vol2]. Blaming the individual ("the sharp end") creates a false illusion that the problem is solved while leaving the latent organizational pathogens—unclear rollback procedures, missing automated integration tests, and fatigue—completely intact[2:doe-hpi-handbook-vol1][17:caib-report-vol1][20:lfuo-learning-review-guide-2024].
Disciplining staff for honest operational errors initiates a destructive Blame Cycle[18:doe-hpi-handbook-vol2][21:doe-hpi-handbook-vol1]. It destroys psychological safety, encourages developers to hide near-misses, stifles open communication, and destroys the reporting culture required to prevent catastrophic outages[21:doe-hpi-handbook-vol1][22:open-practice-library][23:lfuo-learning-review-guide-2024][24:lfuo-learning-review-guide-2024][25:lfuo-learning-review-guide-2024].
4. AI Coding Tools as a "Fix That Fails"
Investing in AI coding tools as a standalone solution to "do both" (increase throughput and maintain quality) represents the classic system archetype Fixes that Fail[26:ssdl-systems-thinking-foundations][27:ssdl-systems-thinking-foundations].
AI tools accelerate localized code generation ("doing" tasks)[28:org-topologies-primer-2025]. However, if we feed more code into a pipeline blocked by multi-squad dependencies, manual testing, and high WIP, AI will simply generate buggy code faster[3:org-topologies-primer-2025][15:open-practice-library][29:org-topologies-primer-2025]. AI cannot solve a structural queueing and alignment problem[3:org-topologies-primer-2025][30:org-topologies-primer-2025].
Prioritized Action Plan: "What to Change First and Why That First"
To restore operational stability, we must apply the Theory of Constraints (TOC): "Any improvements made anywhere besides the bottleneck are an illusion"[31:open-practice-library][32:open-practice-library][33:openstax-accounting-vol2].
[Phase 1: Unblock Bottleneck] ──► [Phase 2: Remove Perverse Incentives] ──► [Phase 3: Institute Just Culture] ──► [Phase 4: Strategic AI]
  • Eliminate Multi-Squads        • Cancel 40% Throughput Bonus           • Reverse Developer PIP              • Target Automated Gates
  • Enforce Strict WIP Limits     • Implement Flow & Quality Metrics       • Blameless Postmortems              • Elevate Skill Mandate

Step 1: Eliminate Multi-Squad Allocation & Limit WIP (Immediate Priority)
Action: Immediately ban multi-squad assignment. Mandate that every developer belongs to exactly one squad. Restructure the 60 engineers into dedicated, stable teams aligned to clear product capabilities, and establish strict WIP limits across all product backlogs[4:open-practice-library][7:open-kanban][34:open-practice-library][35:org-topologies-primer-2025].
Why First?: Multi-squad context-switching is our single greatest system bottleneck[4:open-practice-library][7:open-kanban]. Until we stop task-switching and clear the clogged pipeline, no amount of target-setting, process changes, or AI tools will increase output[31:open-practice-library][32:open-practice-library]. Single-squad dedication instantly reduces WIP, lowers context-switching costs, and restores predictable flow[4:open-practice-library][6:open-practice-library][36:open-practice-library].
Step 2: De-Link Bonuses from Throughput & Align on Flow/Quality Metrics
Action: Cancel the 40% throughput bonus target for squad leads. Replace sprint velocity targets with Flow Metrics (Lead Time, Cycle Time, Defect Escape Rate) and shared customer outcomes co-owned by Product, Marketing, and Engineering[9:open-practice-library][10:open-practice-library][37:open-practice-library][38:open-practice-library][39:open-practice-library].
Why Second: Once WIP is capped, we must remove the perverse financial incentives driving Goodhart's Law gaming, point-inflation, and quality cutting[10:open-practice-library][11:jones-evidence-based-sweng][16:doe-hpi-handbook-vol1].
Step 3: Transition to a Just Culture & Institute Blameless Postmortems
Action: Reverse the PIP for the developer involved in the portal outage. Implement James Reason's Culpability Decision Tree and the Substitution Test ("Would another engineer with similar training have made the same error under those exact system pressures?") for all postmortems[40:doe-hpi-handbook-vol1][41:doe-hpi-handbook-vol1][42:doe-hpi-handbook-vol1][43:doe-hpi-handbook-vol2][44:doe-hpi-handbook-vol2]. Shift investment toward automated deployment guardrails and pre-release verification testing[1:doe-hpi-handbook-vol1][45:doe-hpi-handbook-vol1][46:open-practice-library].
Why Third: Unclogging the workflow requires transparent reporting[25:lfuo-learning-review-guide-2024][47:lfuo-learning-review-guide-2024]. Rebuilding psychological safety ensures engineers report system flaws and production risks early without fear of retribution[22:open-practice-library][23:lfuo-learning-review-guide-2024][25:lfuo-learning-review-guide-2024].
Step 4: Deploy AI Strategically to Elevate Team Capabilities
Action: Shift our AI investment from general code generation to automating our specific delivery constraints—such as automated regression test suite generation, pull-request verification, and deployment pipeline checks[29:org-topologies-primer-2025][30:org-topologies-primer-2025].
Why Fourth: Guided by Org Topologies, AI should be used to broaden our teams' skills mandate and work mandate, elevating them toward cross-functional, end-to-end delivery units[30:org-topologies-primer-2025][35:org-topologies-primer-2025][48:org-topologies-primer-2025][49:org-topologies-primer-2025][50:org-topologies-primer-2025].
Theoretical Disagreements: Tensions & Nuance in the Management Science
To make an informed decision, we must acknowledge where the foundational management theories we are drawing upon disagree with one another:
Strategic Area
	
Theoretical Tension
	
Core Contradiction in Literature
	
Resolution for Our SaaS Context


Goal Setting vs. Process Quality
	
Goal-Setting Theory (Locke & Latham) vs. Total Quality Management (TQM) (Deming)
	
Goal-Setting Theory argues that difficult, specific "stretch" goals drive higher motivation and effort[51:openstax-organizational-behavior][52:openstax-principles-management][53:openstax-introduction-business]. Deming and TQM counter that numerical stretch targets narrow vision, induce fear, invite cheating, and destroy process quality[54:openstax-principles-management][55:openstax-introduction-business][56:openstax-principles-management].
	
Stretch goals work for simple, independent tasks; in complex software engineering, aggressive numerical targets induce systemic gaming under Goodhart's Law[10:open-practice-library][14:openstax-principles-management][54:openstax-principles-management]. We must adopt Deming's focus on continuous process improvement over arbitrary velocity quotas[54:openstax-principles-management][55:openstax-introduction-business].


Resource Efficiency vs. Flow Efficiency
	
Scientific Management (Taylorism) vs. Lean / Queuing Theory
	
Classical Management prioritizes 100% labor utilization ("nobody is idle") to maximize resource cost-efficiency[3:org-topologies-primer-2025][57:openstax-introduction-business][58:openstax-introduction-business]. Lean and Queuing Theory prove that 100% capacity utilization causes infinite queue delays, destroyed flow, and higher overall costs[3:org-topologies-primer-2025][6:open-practice-library][9:open-practice-library][39:open-practice-library].
	
In software delivery, optimizing for human utilization destroys value flow[9:open-practice-library][39:open-practice-library]. We must intentionalize capacity slack so work items can move rapidly without waiting in queues[4:open-practice-library][6:open-practice-library][39:open-practice-library].


Individual Accountability vs. System Safety
	
Strict Individual Accountability vs. Just Culture / Blameless Safety
	
Pure "blameless" models posit that human errors are 100% system-induced and individual discipline is always counterproductive[24:lfuo-learning-review-guide-2024][59:open-practice-library][60:open-practice-library][61:lfuo-learning-review-guide-2024][62:lfuo-learning-review-guide-2024]. Just Culture frameworks (Reason, DOE HPI) distinguish between honest human error and reckless, intentional violations[18:doe-hpi-handbook-vol2][40:doe-hpi-handbook-vol1][63:doe-hpi-handbook-vol1][64:doe-hpi-handbook-vol1].
	
We must reject individual scapegoating for honest errors while maintaining clear accountability for adherence to workable, agreed-upon engineering safety standards[18:doe-hpi-handbook-vol2][40:doe-hpi-handbook-vol1][63:doe-hpi-handbook-vol1][65:lfuo-learning-review-guide-2024].


AI Value Model
	
Micro-Efficiency vs. Strategic Organizational Elevation
	
Conventional executive views see AI as an individual labor-saving tool (writing syntax faster)[28:org-topologies-primer-2025]. Org Topologies demonstrates that localized speedups in "doing" tasks without expanding team scope or removing dependencies merely compound downstream bottlenecks[3:org-topologies-primer-2025][29:org-topologies-primer-2025][66:org-topologies-primer-2025].
	
AI investment must focus on expanding team capabilities to eliminate dependencies, not padding task-level coding speed[29:org-topologies-primer-2025][30:org-topologies-primer-2025].
Summary Recommendation
By ending multi-squad matrixing, capping Work-in-Progress, replacing velocity quotas with flow/quality metrics, and establishing a Just Culture, we can stabilize our customer portal, reduce bug-driven churn, and create a sustainable delivery engine[4:open-practice-library][6:open-practice-library][25:lfuo-learning-review-guide-2024][34:open-practice-library][40:doe-hpi-handbook-vol1].
💡 Next Step: Would you like me to prepare an implementation matrix mapping out squad realignments, WIP limit thresholds, and replacement flow metrics for our upcoming leadership meeting?





## Sentences to grade

### S1

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [1], [2], [3]):
> We are running our software organization on flawed operational assumptions that systematically generate bottleneck queues, incentivize quality compromises, and create severe single-point failures.

Markers on it:

[1] source: doe-hpi-handbook-vol1:466
It is not easy to anticipate exactly how trivial conditions can influence individual performance. Error-provoking aspects of facility*1 design, procedures, processes, and human nature exist everywhere. No matter how efficiently equipment functions; how good the training, supervision, and procedures; and how well the best worker, engineer, or manager performs his or her duties, people cannot perform better than the organization supporting them.1 Human error is caused not only by normal human fallibility, but also by incompatible management and leadership practices and organizational weaknesses in work processes and values. Therefore, defense-in-depth with respect to the human element is needed to improve the resilience of programmatic systems and to drive down human error and events.

[2] source: doe-hpi-handbook-vol1:11323
In 1997, Reason published Managing the Risks of Organizational Accidents. Reason maintained that to understand how organizational accidents occur requires that we look deeper into the system. Unsafe acts by individuals may trigger an event. However, latent conditions within the organization, aligned with local workplace and task factors, contribute to accidents in the form of process errors or as error-likely situations. Thus it is the combination of these latent conditions in conjunction with an active error that more correctly accounts for events. From this perspective, errors are the consequences, not the causes, of disturbances in the organization. Accidents are the result of failed controls and barriers. People are fallible, even the best make mistakes. It is human nature to err. However, events can be eliminated or controlled by changing the conditions in which people work. Managing the risks of organizational accidents requires that managers, supervisors, and staff work to eliminate latent organizational weaknesses. Reason proposes three compelling reasons why latent conditions have to be eliminated.

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

### S2

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [4]):
> Our rule that "nobody is idle," which splits developers across two or three squads simultaneously, is the primary driver of our delivery collapse.

Markers on it:

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[4] source: open-practice-library:3783
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

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [6]):
> Queuing Theory (Little’s Law) dictates that as resource utilization approaches 100%, queue times and lead times increase exponentially (Cycle Time=WIP/Throughput).

Markers on it:

[6] source: open-practice-library:21149
What will you get?
Kanban will provide you a set of metrics to measure your process. These metrics are very usefull to improve your flow and identify points of failure.
* Lead Time: Measures how much time a task spends in the Kanban board, since get in and get out. A measure for our customers.
* Cycle Time: Measures how much time a task spends going through the process, from when the task started.
* Throughput: Measures the total amount of work delivered (completed work items).
These metrics are connected by the Little's Law: Cycle Time = WIP / Throughput

### S4

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [4], [7]):
> By forcing engineers onto multiple squads, we inflate Work-In-Progress (WIP) and generate massive context-switching overhead.

Markers on it:

[4] source: open-practice-library:3783
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

[7] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

### S5

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [8]):
> Furthermore, software development communication overhead grows non-linearly with team interdependencies (D
peak
	​

 thresholds).

Markers on it:

[8] source: jones-evidence-based-sweng:22359
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

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [4], [7], [8]):
> Because our 60 engineers are fragmented across 9 squads, individual focus is destroyed, handover friction spikes, and velocity stalls.

Markers on it:

[4] source: open-practice-library:3783
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

[7] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

[8] source: jones-evidence-based-sweng:22359
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

### S7

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [9]):
> A system with 100% busy people inevitably yields 0% flow efficiency.

Markers on it:

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[9] source: open-practice-library:3823
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: manage-flow.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Manage Flow subtitle: Optimize the processing work items date: 2019-10-19T09:24:08.129Z authors:
- rhdojun tags:
- culture mobiusTag: foundation icon: /images/pullstuckcar.jpg whatIs: Direct the focus of optimization on work items, e.g. tasks, problems, process steps, instead of the people. That means metrics also need to focus on work items, not on people. whyDo: >- Everybody already experienced a few times in their life that it is totally possible that everybody is busy to the point of being overworked but the work gets done slower and slower.

### S8

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [12]):
> Expecting a clogged system to deliver 40% more throughput forces engineers into an Efficiency-Thoroughness Trade-Off (ETTO).

Markers on it:

[12] source: lfuo-learning-review-guide-2024:5098
or to exchange ideas. (Oxford Dictionary)
Doctrine: a body of principles evolved from laws, culture, history and precedence that
guides the action of an organization. It is the expression of the fundamental framework
and concepts that also guides the planning and conduct of operations.
Efficiency-Thoroughness Trade-Off: “In their daily activities, at work or at leisure, people (and organizations) routinely make a choice between being effective and being
thorough, since it rarely is possible to be both at the same time. If demands to productivity or performance are high, thoroughness is reduced until the productivity goals are met. If demands to safety are high, efficiency is reduced until the safety goals are

### S9

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [12], [13], [14]):
> When output volume is tied to financial compensation, teams systematically sacrifice thoroughness—skipping automated testing, truncating code reviews, and taking architectural shortcuts.

Markers on it:

[12] source: lfuo-learning-review-guide-2024:5098
or to exchange ideas. (Oxford Dictionary)
Doctrine: a body of principles evolved from laws, culture, history and precedence that
guides the action of an organization. It is the expression of the fundamental framework
and concepts that also guides the planning and conduct of operations.
Efficiency-Thoroughness Trade-Off: “In their daily activities, at work or at leisure, people (and organizations) routinely make a choice between being effective and being
thorough, since it rarely is possible to be both at the same time. If demands to productivity or performance are high, thoroughness is reduced until the productivity goals are met. If demands to safety are high, efficiency is reduced until the safety goals are

[13] source: openstax-organizational-behavior:10987
CONCEPT CHECK
to decide who is laid off (procedural justice). For example, layoffs based on seniority may be perceived as more fair than layoffs based on supervisors’ opinions.
Goal Theory It remains true that difficult, specific goals result in better performance than easy and vague goals, assuming they are accepted. Recent research highlights the positive effects of performance feedback and goal commitment in the goal-setting process. Monetary incentives enhance motivation when they are tied to goal achievement, by increasing the level of goal commitment. There are negative sides to goal theory as well. If goals conflict, employees may sacrifice performance on important job duties. For example, if both quantitative and qualitative goals are set for performance, employees may emphasize quantity because this goal achievement is more visible.

[14] source: openstax-principles-management:25685
supervisors who insist on maintaining excessive control.
Another dysfunctional result of poor control systems can be seen in their effect on goal-setting programs. Whereas a good control system can help design and monitor valuable goal-setting programs, a poor control system can accomplish quite the opposite. A control system focused on unreasonable ends and means goals can motivate workers to establish inappropriate individual goals. For instance, the ends goal Donald Pemble established of having all bridges inspected within two years was unreachable, and his monthly inspection quotas (means goals) were unobtainable. Donald’s insistence on maintaining these inappropriate goals was evident in his reactions when the inspectors failed to meet them. Consequently, Shannon and her coworkers focused on preserving their jobs as a primary goal, rather than on conducting quality inspections.

### S10

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [15]):
> The result is a surge in technical debt and production defects.

Markers on it:

[15] source: open-practice-library:22168
time: 30 mins difficulty: easy participants:
- The Team
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: technical-debt.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Technical Debt subtitle: The cost of reworking quickly implemented solutions date: 2020-02-17T13:56:42.629Z authors:
- dappleyard93 tags:
- value
- methods mobiusTag: delivery icon: /images/Tech debt Radar.jpg whatIs: >- Technical debt as a concept reflects the cost of rework caused by taking shortcuts or choosing an easier solution, instead of using a better approach that may take longer. Technical debt can in some ways be compared to monetary debt in that it can accumulate 'interest', making it harder to implement changes later on. Unaddressed technical debt increases software entropy, slows development and may cause much bigger problems further down the line.

### S11

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [13], [14], [15], [16]):
> Marketing correctly observes that churn is driven by bugs, but engineering is being explicitly incentivized to generate those bugs to meet volume targets.

Markers on it:

[13] source: openstax-organizational-behavior:10987
CONCEPT CHECK
to decide who is laid off (procedural justice). For example, layoffs based on seniority may be perceived as more fair than layoffs based on supervisors’ opinions.
Goal Theory It remains true that difficult, specific goals result in better performance than easy and vague goals, assuming they are accepted. Recent research highlights the positive effects of performance feedback and goal commitment in the goal-setting process. Monetary incentives enhance motivation when they are tied to goal achievement, by increasing the level of goal commitment. There are negative sides to goal theory as well. If goals conflict, employees may sacrifice performance on important job duties. For example, if both quantitative and qualitative goals are set for performance, employees may emphasize quantity because this goal achievement is more visible.

[14] source: openstax-principles-management:25685
supervisors who insist on maintaining excessive control.
Another dysfunctional result of poor control systems can be seen in their effect on goal-setting programs. Whereas a good control system can help design and monitor valuable goal-setting programs, a poor control system can accomplish quite the opposite. A control system focused on unreasonable ends and means goals can motivate workers to establish inappropriate individual goals. For instance, the ends goal Donald Pemble established of having all bridges inspected within two years was unreachable, and his monthly inspection quotas (means goals) were unobtainable. Donald’s insistence on maintaining these inappropriate goals was evident in his reactions when the inspectors failed to meet them. Consequently, Shannon and her coworkers focused on preserving their jobs as a primary goal, rather than on conducting quality inspections.

[15] source: open-practice-library:22168
time: 30 mins difficulty: easy participants:
- The Team
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: technical-debt.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Technical Debt subtitle: The cost of reworking quickly implemented solutions date: 2020-02-17T13:56:42.629Z authors:
- dappleyard93 tags:
- value
- methods mobiusTag: delivery icon: /images/Tech debt Radar.jpg whatIs: >- Technical debt as a concept reflects the cost of rework caused by taking shortcuts or choosing an easier solution, instead of using a better approach that may take longer. Technical debt can in some ways be compared to monetary debt in that it can accumulate 'interest', making it harder to implement changes later on. Unaddressed technical debt increases software entropy, slows development and may cause much bigger problems further down the line.

[16] source: doe-hpi-handbook-vol1:6385
 lacking correction or coaching of at-risk practices, or using human performance tools improperly;
 having inconsistencies between what managers say they want and what they reward or pay attention to;
 making uncritical observation comments so as to not offend those observed;
 initiating disciplinary action for honest mistakes;
 providing bonuses based solely on productivity measures; and
 proceeding to the next action or step before signing off concurrent verification.
Oversight Controls

### S12

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [17], [18]):
> Placing the developer who merged the bad release on a Performance Improvement Plan (PIP) is a critical organizational mistake.

Markers on it:

[17] source: caib-report-vol1:20531
22 Changing personnel is a typical response after an organization has some kind of harmful outcome. It has great symbolic value. A change in personnel points to individuals as the cause and removing them gives the false impression that the problems have been solved, leaving unresolved organizational system problems. See Scott Sagan, The Limits of Safety. Princeton: Princeton University Press, 1993.
Diane Vaughan, The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA (Chicago: University of Chicago Press. 1996).

[18] source: doe-hpi-handbook-vol2:3182
the balance right between how unintentional errors and willful violations are addressed in the organization. Ideally there should be zero tolerance for reckless conduct balanced by widespread confidence among managers that the vast majority of unintended unsafe acts will go unpunished as honest errors.
1. Stop naming, blaming, shaming, and retraining individuals for honest errors. Remember an error is an unintentional departure from an expected behavior—it is something the performer did not intend to do.

### S13

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [2], [17], [20]):
> Blaming the individual ("the sharp end") creates a false illusion that the problem is solved while leaving the latent organizational pathogens—unclear rollback procedures, missing automated integratio

Markers on it:

[2] source: doe-hpi-handbook-vol1:11323
In 1997, Reason published Managing the Risks of Organizational Accidents. Reason maintained that to understand how organizational accidents occur requires that we look deeper into the system. Unsafe acts by individuals may trigger an event. However, latent conditions within the organization, aligned with local workplace and task factors, contribute to accidents in the form of process errors or as error-likely situations. Thus it is the combination of these latent conditions in conjunction with an active error that more correctly accounts for events. From this perspective, errors are the consequences, not the causes, of disturbances in the organization. Accidents are the result of failed controls and barriers. People are fallible, even the best make mistakes. It is human nature to err. However, events can be eliminated or controlled by changing the conditions in which people work. Managing the risks of organizational accidents requires that managers, supervisors, and staff work to eliminate latent organizational weaknesses. Reason proposes three compelling reasons why latent conditions have to be eliminated.

[17] source: caib-report-vol1:20531
22 Changing personnel is a typical response after an organization has some kind of harmful outcome. It has great symbolic value. A change in personnel points to individuals as the cause and removing them gives the false impression that the problems have been solved, leaving unresolved organizational system problems. See Scott Sagan, The Limits of Safety. Princeton: Princeton University Press, 1993.
Diane Vaughan, The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA (Chicago: University of Chicago Press. 1996).

[20] source: lfuo-learning-review-guide-2024:3953
learning because it faults only one part of the system. However, safety is in the entire system. Practitioners at the “sharp end” (those workers who directly confront the risks of the workplace) are inheritors of policies, training programs, tools,
culture, incentives, etc., that are the responsibility of those managers and administrators at the “blunt-end.” Practitioners at the sharp end are those who make real-time, operational risk management decisions. Those at the blunt end are the supervisors, and administrators who are engaged in strategic risk management

### S14

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [21], [22], [23], [24], [25]):
> It destroys psychological safety, encourages developers to hide near-misses, stifles open communication, and destroys the reporting culture required to prevent catastrophic outages.

Markers on it:

[21] source: doe-hpi-handbook-vol1:9858
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

[22] source: open-practice-library:19804
* Identifying factors that lead to an incident and affected the incident timeline, both in good and bad way
* Improves communication both within the team and across teams involved in the incident response and Postmortem itself - “if we can openly talk about failures, we can talk about anything”
* Promote the safe culture of “it’s alright to fail” howTo: >- A successful Blameless Postmortem is build on two fundations:
* Availability of the information regarding the incident.
* Psychological safety of all participants that promotes speaking up openly

[23] source: lfuo-learning-review-guide-2024:416
terms of wholes and relationships.
JUST CULTURE
Just Culture is characterized by the intersection of valuing trust, fairness and dignity. In a just culture, an organization has an open and safe reporting system where everyone can speak. In a
just culture, organizations are accountable for systems they design and analysis of the incident—not the individual. Many organizations have policies that describe nonpunitive responses to error. However, internal barriers to speaking up include
negative management responses and the risk of discipline from leaders.

[24] source: lfuo-learning-review-guide-2024:477
“You’ve got nothing to fear if you’ve done nothing wrong.”
Punishing or blaming employees involved in an accident is the surest way to kill a learning culture. The attitude expressed in the quote above is a threat and has no place
in an FLA.
“Holding people accountable and blaming people are two quite different things. Blaming people may in fact make them less accountable: they will tell fewer accounts,
they may feel less compelled to have their voice heard, to participate in improvement efforts. Blame-free or no-fault systems are not accountability-free systems. On the contrary: such systems want to open the ability for people to hold their account, so that everybody can respond and take responsibility for doing something about the problem.

[25] source: lfuo-learning-review-guide-2024:3849
flow of information is constrained.
We want to create a culture where employees feel safe to raise their hands and openly share unsafe conditions, individual mistakes, errors, close calls and risky decisions. A “Just Culture” is a workplace where employees at all levels are
accountable for their participation and their commitment to the organization’s
safety culture. The “Just” part of Just Culture which stems from the word Justice, is the essential and fundamental recognition that workers are inheritors of the tools,

### S15

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [26], [27]):
> Investing in AI coding tools as a standalone solution to "do both" (increase throughput and maintain quality) represents the classic system archetype Fixes that Fail.

Markers on it:

[26] source: ssdl-systems-thinking-foundations:1256
Archetype #3: Shifting the burden
The “shifting the burden” archetype shows what happens when we address the symptoms of a problem with a quick-fix solution. This solution is easier and faster than creating an upstream solution to the problem, and we are often meeting a very real, urgent need for a student. However, the quick-fix to the symptoms may actually impede our ability to invest time and energy to the fundamental solution. This makes it even harder to apply a fundamental solution and even more tempting to rely on quick fixes. Thus, the problem cannot be completely solved.

[27] source: ssdl-systems-thinking-foundations:1169
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

### S16

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [28]):
> AI tools accelerate localized code generation ("doing" tasks).

Markers on it:

[28] source: org-topologies-primer-2025:1533
“Doing” 
Task-​oriented work  without a view of the  whole picture.
Heavily reliant on  directives from others.
Operational efficiency booster for tasks requiring routine  expertise with intelligent automation, task-​specific agents, 
and virtual assistants.
Optimizes repetitive and tactical work.
Automated and predictive guidance within task execution.
Enhances productivity by reducing the  cognitive load.
Ensures consistent execution quality.
“Delivering”
Deliver value within a  narrow scope but often

### S17

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [15], [29]):
> However, if we feed more code into a pipeline blocked by multi-squad dependencies, manual testing, and high WIP, AI will simply generate buggy code faster.

Markers on it:

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[15] source: open-practice-library:22168
time: 30 mins difficulty: easy participants:
- The Team
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: technical-debt.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Technical Debt subtitle: The cost of reworking quickly implemented solutions date: 2020-02-17T13:56:42.629Z authors:
- dappleyard93 tags:
- value
- methods mobiusTag: delivery icon: /images/Tech debt Radar.jpg whatIs: >- Technical debt as a concept reflects the cost of rework caused by taking shortcuts or choosing an easier solution, instead of using a better approach that may take longer. Technical debt can in some ways be compared to monetary debt in that it can accumulate 'interest', making it harder to implement changes later on. Unaddressed technical debt increases software entropy, slows development and may cause much bigger problems further down the line.

[29] source: org-topologies-primer-2025:1442
> What parts of the company are the focus of org development?  The Product Management and R&D departments, so focus on AI  investment there. 
> What archetypes are part of the target? What’s a dominant constraint  from one to the other?  The R&D department has mostly TASKS-1 individuals, and the target is  CAPS-3 teams. On investigation, it’s a lack of front-​end design and  coding skilled people. Focus time, money, and management attention on  AIs, especially on that big bottleneck, over a generic “adopt AI.”

### S18

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [30]):
> AI cannot solve a structural queueing and alignment problem.

Markers on it:

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[30] source: org-topologies-primer-2025:1446
Evolving rightward on the horizontal axis to broader skills mandate will  become ever easier due to AI. And likewise upward on the vertical axis  to a broader work mandate. So, top-​right Driving archetypes will  become more feasible.
Obviously, “adopt AI everywhere you can” will be the general guidance,  but given the limited resources of money, time, and attention, in  strategic org design with OT we recommend that you ask and answer  these questions:
For example, a pet-​supply company creates e-​commerce software in a  Resource topology. It’s a mature, uncomplicated market. Competition  has delivered a better website and app that customers love. Leadership  has decided on a business objective of retaining customers, with an org  goal of fast flow to parity, by targeting a Delivery topology with CAPS-3  teams.

### S19

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [4], [7], [34], [35]):
> Restructure the 60 engineers into dedicated, stable teams aligned to clear product capabilities, and establish strict WIP limits across all product backlogs.

Markers on it:

[4] source: open-practice-library:3783
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

[7] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

[34] source: open-practice-library:21009
WIP Limit
Limit work in progress. These sample numbers represent the maximum number of functional items for workflow. Promote finishing and provoke important discussions. “Stop starting, start finishing!”
One Way
Do not move cards backwards. An item flows when work is completed at each step. If a correction needs to be made, keep the item in the same column, eventually signaling that a block exists. Focus on finishing.
Metrics
Throughput - The amount of items delivered in a given time frame, usually weeks.

[35] source: org-topologies-primer-2025:801
DIRECT﻿ING 
DOING
Resource Topology: Directing + Doing
Delivery Topology Compared to the Resource Topology, this topology upgrades  delivery units to have fast flow by removing dependencies.  Structurally, this typically involves forming complete cross-​ functional teams, and facilitating a smoother path to  “completely done” work. In some domains, this topology is  called a “Feature Factory” since Delivery units can provide a  near-​endless stream of features. Note a strong focus on  outputs and local efficiency.

### S20

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [4], [7]):
> Why First?: Multi-squad context-switching is our single greatest system bottleneck.

Markers on it:

[4] source: open-practice-library:3783
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

[7] source: open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

### S21

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [31], [32]):
> Until we stop task-switching and clear the clogged pipeline, no amount of target-setting, process changes, or AI tools will increase output.

Markers on it:

[31] source: open-practice-library:8571
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: the-theory-of-constraints.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: The Theory of Constraints subtitle: "“Any improvements made anywhere besides the bottleneck are an illusion.” " date: 2021-06-04T10:17:34.156Z authors:
- tom-geraghty tags:
- methods mobiusTag: foundation icon: /images/three-contract-management-bottlenecks-eliminated-by-automation.png whatIs: >- Eliyahu Goldratt first described the Theory Of Constraints (ToC) in his 1984 book, "The Goal", which focused on manufacturing and was a key catalyst for the revolution in the performance of manufacturing in subsequent years.

[32] source: open-practice-library:8577
The Theory of Constraints shows us that in any process, there must be a single bottleneck that limits the total throughput of the process: in the same way that a chain has a weakest link, a process has a single slowest component. whyDo: >- Whilst it may be easy to improve some part of the process, if that component isn't the bottleneck, it will either have zero effect on the throughput because the bottleneck is upstream, or it will actually cause more pain in the system by adding pressure to the bottleneck, if the bottleneck is downstream.

### S22

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [4], [6], [36]):
> Single-squad dedication instantly reduces WIP, lowers context-switching costs, and restores predictable flow.

Markers on it:

[4] source: open-practice-library:3783
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

[6] source: open-practice-library:21149
What will you get?
Kanban will provide you a set of metrics to measure your process. These metrics are very usefull to improve your flow and identify points of failure.
* Lead Time: Measures how much time a task spends in the Kanban board, since get in and get out. A measure for our customers.
* Cycle Time: Measures how much time a task spends going through the process, from when the task started.
* Throughput: Measures the total amount of work delivered (completed work items).
These metrics are connected by the Little's Law: Cycle Time = WIP / Throughput

[36] source: open-practice-library:3796
If one makes sure to only work on one task and then on the next one doesn't get overloaded. That means the person stays responsive, flexible and the status stays visible. If a task gets stuck waiting on external resources the person can help reducing this external dependency or making it more visible at least, to the rest of the team. howTo: >-
* As a team, determine the amount of in-progress work you want to be your maximum at any given time.
* Set that limit as your WIP limit and ensure throughout the sprint that it is not exceeded
* Review WIP Limit at the end of the sprint and adjust if needed jumbotron: /images/valves.jpg area: foundation-culture-and-collaboration time: '0' mediaGallery:
- link: 'https://www.youtube.com/watch?v=SFMlu87MkYI'
- link: 'https://openpracticelibrary.github.io/opl-media/images/valves.jpg' people: '1' difficulty: moderate mobiusTag: foundation

### S23

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [9], [10], [37], [38], [39]):
> Replace sprint velocity targets with Flow Metrics (Lead Time, Cycle Time, Defect Escape Rate) and shared customer outcomes co-owned by Product, Marketing, and Engineering.

Markers on it:

[9] source: open-practice-library:3823
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: manage-flow.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Manage Flow subtitle: Optimize the processing work items date: 2019-10-19T09:24:08.129Z authors:
- rhdojun tags:
- culture mobiusTag: foundation icon: /images/pullstuckcar.jpg whatIs: Direct the focus of optimization on work items, e.g. tasks, problems, process steps, instead of the people. That means metrics also need to focus on work items, not on people. whyDo: >- Everybody already experienced a few times in their life that it is totally possible that everybody is busy to the point of being overworked but the work gets done slower and slower.

[10] source: open-practice-library:9202
Points of note:
Try to keep this survey anonymous. Honest answers are of utmost importance.
Resist the temptation to measure too frequently. Once per quarter or every six months is appropriate.
Avoid setting score improvement as a goal - be conscious that GoodHart's Law means that when a measure becomes a target, it ceases to become a good measure.
If you have a large enough organisation, or enough data over time, you could try applying data science practices to identify outliers in the data that can indicate particular areas of concern, for particular teams, or disruptive events that correlate with a dip in scores. mediaGallery:

[37] source: open-practice-library:2319
It is an alternative to OKRs (Objective Key Results) and SMART (Specific Measurable Achievable Relevant Time bound) goals. whyDo: >- The thorny world of objective setting can kill a team's drive. Different people gravitate towards different models, but it is generally agreed that top down, cascaded objectives deserve to rot in the 90's. As teams move towards greater autonomy, translating the purpose and vision into meaningful and measurable activities can be uncomfortable at best. Enter GEMs - Goal : Experiments : Measures.

[38] source: open-practice-library:21031
Lead Time - The clock starts ticking on replenishment and ends when the item is delivered.The number of calendar days to get an item done is the lead time.
CFD - Cumulative Flow Diagram Shows demand, WIP, approximate average lead time and delivery rate capabilities.
To collect these metrics you only need the start and finishing date for an item then count how many items you have per day in each column.
Explicit Policies
Post policies where you can see them. Policies are rules for how we work and should be developed collaboratively. Example - pull criteria, wip limits, date to deploy.

[39] source: open-practice-library:3834
One could ask themselves, why is that? And what is more important? Is it better that everybody is busy or would it be better if more work gets done?
Usually in comparison it should be clear the second point is much more important: work needs to get done.
But to get there one cannot track indirect metrics like utilization of employees. Instead one needs to track work item related metrics like how long a task stays work in progress. And one needs to make visible when tasks get stuck so the team can analyse together why it got stuck and how this could be avoided the next time. howTo: >- Typical activities for managing flow are:

### S24

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [10], [11], [16]):
> Why Second: Once WIP is capped, we must remove the perverse financial incentives driving Goodhart's Law gaming, point-inflation, and quality cutting.

Markers on it:

[10] source: open-practice-library:9202
Points of note:
Try to keep this survey anonymous. Honest answers are of utmost importance.
Resist the temptation to measure too frequently. Once per quarter or every six months is appropriate.
Avoid setting score improvement as a goal - be conscious that GoodHart's Law means that when a measure becomes a target, it ceases to become a good measure.
If you have a large enough organisation, or enough data over time, you could try applying data science practices to identify outliers in the data that can indicate particular areas of concern, for particular teams, or disruptive events that correlate with a dip in scores. mediaGallery:

[11] source: jones-evidence-based-sweng:41870
Goodhart’s law is an observation about human behavior, rather than a law: “Any observed statistical regularity will tend to collapse once pressure is placed on it for control purposes.” If the measurements collected were actively used to control or evaluate the development team (for instance), then developers have a motivation to cause the measurements to move in a direction favorable to themselves.
A study by Perry, Staudenmayer and Votta1472 investigated various software development activities (e.g., working time on an activity, and activities performed throughout the day), as measured by the developers involved (i.e., self reports) and as measured by external observers. Differences in reported measurement values included, developers reporting activity time 2.8% higher, on average, than that reported by an observer; the measurement agreement rate for activities performed varied between 0.6 and 0.95.

[16] source: doe-hpi-handbook-vol1:6385
 lacking correction or coaching of at-risk practices, or using human performance tools improperly;
 having inconsistencies between what managers say they want and what they reward or pay attention to;
 making uncritical observation comments so as to not offend those observed;
 initiating disciplinary action for honest mistakes;
 providing bonuses based solely on productivity measures; and
 proceeding to the next action or step before signing off concurrent verification.
Oversight Controls

### S25

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [40], [41], [42], [43], [44]):
> Implement James Reason's Culpability Decision Tree and the Substitution Test ("Would another engineer with similar training have made the same error under those exact system pressures?") for all postm

Markers on it:

[40] source: doe-hpi-handbook-vol1:9985
Department of Energy Human Performance Handbook Chapter 4 Culture & Leadership
accountable for their actions in the same fashion that someone who intentionally performs work he or she knows is contrary to known standards.
A just environment is all about getting the balance right between how willful violations and unintentional errors are addressed in the organization. All too often organizations do not make clear the distinctions between errors and violations. A just organization clears the smoke in the air between erring and violating. To do so, management sets a zero tolerance policy for reckless conduct—bad acts that we call violations. Zero tolerance for violations is balanced by the belief and the widespread confidence among the leadership that the vast majority of unintended unsafe acts will go unpunished as honest errors—unintended departures from expected behavior—on the part of the performer. There are proven methods to help organizations determine culpability for serious incidences in which unsafe acts are involved.

[41] source: doe-hpi-handbook-vol1:10059
The Culpability Decision Tree
The logic diagram below is a proven management tool intended to help determine the culpability level of an individual in response to events or near misses triggered by human error.33 When used in conjunction with the organization’s accountability policy, the tool supports the fair and consistent application of disciplinary outcomes across all departments and work groups. An explanation of how to make use of the Culpability Decision Tree is provided in Appendix B. The tool is an adaptation of Dr. James Reason’s Culpability Decision Tree in his book, Managing the Risks of Organizational Accidents, which provides further in-depth description of the use of the diagram.

[42] source: doe-hpi-handbook-vol1:10185
self-reported?
Passes the substitution
test?
Were expectations
available, intelligible, workable, and
correct?
Knowingly violate
expectations?
Were consequences
intended?
Were actions
intended?
Evaluate relevant organizational processes and related management
and supervisory practices.
No
Yes
Yes
Yes
Yes No
No
No No
No Yes
Yes
Yes
No
Yes
No
When an event is initiated by an honest error, as determined by one or more of the tools described above, the entire system that supports the performance in question should be evaluated (see “systems-thinking” in Chapter 3). Events triggered by human error are often symptomatic of a system failure. Instead of asking how the individual failed the organization, the question “how did the organization fail the individual?” would be more appropriate. In addition to the individual, what or who could have prevented the event? What flaws or oversights in work processes, policies, or procedures contributed, promoted, or allowed the error and event to occur? Because the majority of the causes of events originate in the system of controls, processes, and values established by the management team, management's first reaction to events should be to look within the organization.

[43] source: doe-hpi-handbook-vol2:3204
• Culpability Test – If the individual was working while under the influence; was clowning around with equipment or vehicles; was taking unwarranted short cuts; or consciously selected sub-standard or inappropriate tools, equipment, or parts, then they are likely more culpable for their actions
• The Substitution Test – The following question is asked of several peers of the individual involved in the event: “In light of how events unfolded and were perceived by those involved in real time, is it likely that you (a different person with similar skills and training) would have behaved any differently?” The question can be worded differently: “given the circumstances that prevailed at the time, could you be

[44] source: doe-hpi-handbook-vol2:3215
DOE-HDBK-1028-2009
Human Performance Tools
sure that you would not have committed the same or a similar type of unsafe act?” If the answers are “no,” then blame is likely inappropriate.
• Culpability Decision Tree (CDT) – This is used in conjunction with an organization’s accountability policy. The CDT is a logic diagram that managers can follow as they ask questions to determine an individual’s intent, expectations, prior knowledge, and prior performance problems associated with their recent unsafe act. By following the logic on the CDT, the manager can gage both individual culpability (for an intentional act to cause harm, reckless violation, and negligent error) and organizational culpability (for induced violation and induced error). See attachment.

### S26

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [1], [45], [46]):
> Shift investment toward automated deployment guardrails and pre-release verification testing.

Markers on it:

[1] source: doe-hpi-handbook-vol1:466
It is not easy to anticipate exactly how trivial conditions can influence individual performance. Error-provoking aspects of facility*1 design, procedures, processes, and human nature exist everywhere. No matter how efficiently equipment functions; how good the training, supervision, and procedures; and how well the best worker, engineer, or manager performs his or her duties, people cannot perform better than the organization supporting them.1 Human error is caused not only by normal human fallibility, but also by incompatible management and leadership practices and organizational weaknesses in work processes and values. Therefore, defense-in-depth with respect to the human element is needed to improve the resilience of programmatic systems and to drive down human error and events.

[45] source: doe-hpi-handbook-vol1:1508
To improve human performance and facility performance, efforts should be made to (1) reduce the occurrence of errors at all levels of the organization and (2) enhance the integrity of controls, or safeguards discovered to be weak or missing. Reducing errors (Re) and managing controls (Mc) will lead to zero significant events (ØE). The formula for achieving this goal is Re + Mc → ØE. Eliminating significant facility events will result in performance improvement within the organization.
Reducing Error

[46] source: open-practice-library:20096
One part of managing a software-engineering process is catching problems at the "lowest-value" stage—that is, at the time at which the least investment has been made and at which problems cost the least to correct. To achieve such a goal, developers use "quality gates," periodic tests or reviews that determine whether the quality of the product at one stage is sufficient to support moving on to the next.
By this, a second important benefit is revealed: Ego-less Programming. As Jeff Atwood states in his blog post:

### S27

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [25], [47]):
> Why Third: Unclogging the workflow requires transparent reporting.

Markers on it:

[25] source: lfuo-learning-review-guide-2024:3849
flow of information is constrained.
We want to create a culture where employees feel safe to raise their hands and openly share unsafe conditions, individual mistakes, errors, close calls and risky decisions. A “Just Culture” is a workplace where employees at all levels are
accountable for their participation and their commitment to the organization’s
safety culture. The “Just” part of Just Culture which stems from the word Justice, is the essential and fundamental recognition that workers are inheritors of the tools,

[47] source: lfuo-learning-review-guide-2024:45
engineer a reporting culture—an organizational climate in which people are prepared to report their errors . . . An effective reporting culture depends, in
turn, on how the organization handles blame and punishment . . . What is needed
is a just culture . . .”
J. T. Reason, Managing the Risks of Organizational Accidents (Aldershot,
England: Ashgate, 1997), p195.
“I got behind the safety shelter; then in a little bit, I heard a voice say,
Get in This Truck!”
2011, Salt Fire
Entrapment and Shelter Deployment FLA. U.S. Forest Service Photo

### S28

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [29], [30]):
> Action: Shift our AI investment from general code generation to automating our specific delivery constraints—such as automated regression test suite generation, pull-request verification, and deployme

Markers on it:

[29] source: org-topologies-primer-2025:1442
> What parts of the company are the focus of org development?  The Product Management and R&D departments, so focus on AI  investment there. 
> What archetypes are part of the target? What’s a dominant constraint  from one to the other?  The R&D department has mostly TASKS-1 individuals, and the target is  CAPS-3 teams. On investigation, it’s a lack of front-​end design and  coding skilled people. Focus time, money, and management attention on  AIs, especially on that big bottleneck, over a generic “adopt AI.”

[30] source: org-topologies-primer-2025:1446
Evolving rightward on the horizontal axis to broader skills mandate will  become ever easier due to AI. And likewise upward on the vertical axis  to a broader work mandate. So, top-​right Driving archetypes will  become more feasible.
Obviously, “adopt AI everywhere you can” will be the general guidance,  but given the limited resources of money, time, and attention, in  strategic org design with OT we recommend that you ask and answer  these questions:
For example, a pet-​supply company creates e-​commerce software in a  Resource topology. It’s a mature, uncomplicated market. Competition  has delivered a better website and app that customers love. Leadership  has decided on a business objective of retaining customers, with an org  goal of fast flow to parity, by targeting a Delivery topology with CAPS-3  teams.

### S29

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [54], [55], [56]):
> Deming and TQM counter that numerical stretch targets narrow vision, induce fear, invite cheating, and destroy process quality.

Markers on it:

[54] source: openstax-principles-management:25314
The Negative Side of Goals There is, however, a negative side to goal setting. Total quality management (TQM) pioneer W. Edwards Deming fears that goals tend to narrow the performer’s vision and invite people to slack off once the goal is achieved. TQM is also oriented more toward process (means) than toward success (goals, outcomes). Organizational learning and continuous improvement, a central component of TQM, is oriented toward continually finding problems in the production process that when eliminated will result in performance increases.40 Performance goals, on the other hand, generally focus the performer’s attention on successfully achieving a specified level of accomplishment at some future point.

[55] source: openstax-introduction-business:29725
Dr. W. Edwards Deming, an American management consultant, was the first to say that quality control should be a company-wide goal. His ideas were adopted by the Japanese in the 1950s but largely ignored in the United States until the 1970s. Deming believed that quality control starts with top management, who must foster a company-wide culture dedicated to producing quality.
Deming’s concept of Total Quality Management (TQM) emphasizes the use of quality principles in all aspects of a company’s production and operations. It recognizes that all employees involved with bringing a product or service to customers—marketing, purchasing, accounting, shipping, manufacturing—contribute to its quality. TQM focuses on continuous improvement, a commitment to constantly seek better ways of doing things in order to achieve greater efficiency and improve quality. Company-wide teams work together to

[56] source: openstax-principles-management:25362
Exhibit 17.12 Performance, Aspiration Level, and Satisfaction (Attribution: Copyright Rice University, OpenStax, under CC-BY 4.0 license)
Managing through Goal Setting What can managers do to motivate employees through goal setting? First, it is important to encourage goal acceptance and commitment. This can be accomplished by working with organizational members to set difficult, specific, and reasonable goals and to make certain that members perceive them as reasonable. If necessary, provide training and other support needed to make the goals attainable. Offer feedback that lets people know when they are approaching the goal. Avoid using threats. Feedback that criticizes without providing insight into ways to contribute to performance improvements is both frustrating and unlikely to be effective. One of Deming’s concerns about goal setting is that it creates fear in employees—fear of the failure to reach the goal. He sees fear as a serious disease that contributes to poor organizational performance.46

### S30

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [10], [14], [54]):
> Stretch goals work for simple, independent tasks; in complex software engineering, aggressive numerical targets induce systemic gaming under Goodhart's Law.

Markers on it:

[10] source: open-practice-library:9202
Points of note:
Try to keep this survey anonymous. Honest answers are of utmost importance.
Resist the temptation to measure too frequently. Once per quarter or every six months is appropriate.
Avoid setting score improvement as a goal - be conscious that GoodHart's Law means that when a measure becomes a target, it ceases to become a good measure.
If you have a large enough organisation, or enough data over time, you could try applying data science practices to identify outliers in the data that can indicate particular areas of concern, for particular teams, or disruptive events that correlate with a dip in scores. mediaGallery:

[14] source: openstax-principles-management:25685
supervisors who insist on maintaining excessive control.
Another dysfunctional result of poor control systems can be seen in their effect on goal-setting programs. Whereas a good control system can help design and monitor valuable goal-setting programs, a poor control system can accomplish quite the opposite. A control system focused on unreasonable ends and means goals can motivate workers to establish inappropriate individual goals. For instance, the ends goal Donald Pemble established of having all bridges inspected within two years was unreachable, and his monthly inspection quotas (means goals) were unobtainable. Donald’s insistence on maintaining these inappropriate goals was evident in his reactions when the inspectors failed to meet them. Consequently, Shannon and her coworkers focused on preserving their jobs as a primary goal, rather than on conducting quality inspections.

[54] source: openstax-principles-management:25314
The Negative Side of Goals There is, however, a negative side to goal setting. Total quality management (TQM) pioneer W. Edwards Deming fears that goals tend to narrow the performer’s vision and invite people to slack off once the goal is achieved. TQM is also oriented more toward process (means) than toward success (goals, outcomes). Organizational learning and continuous improvement, a central component of TQM, is oriented toward continually finding problems in the production process that when eliminated will result in performance increases.40 Performance goals, on the other hand, generally focus the performer’s attention on successfully achieving a specified level of accomplishment at some future point.

### S31

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [57], [58]):
> Classical Management prioritizes 100% labor utilization ("nobody is idle") to maximize resource cost-efficiency.

Markers on it:

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[57] source: openstax-introduction-business:27796
The gap between what is and what is required. Anything that decreases a specific behavior.
A theory of motivation that holds that people do things because they know that certain consequences will follow.
Anything that increases a specific behavior. A system of management developed by Frederick W. Taylor and based on four
principles: developing a scientific approach for each element of a job, scientifically selecting and training workers, encouraging cooperation between workers and managers, and dividing work and responsibility between management and workers according to who can better perform a particular task.

[58] source: openstax-introduction-business:27826
A theory developed by William Ouchi that combines U.S. and Japanese business practices by emphasizing long-term employment, slow career development, moderate specialization, group decisionmaking, individual responsibility, relatively informal control over the employee, and concern for workers.
The gap between what is and what is desired.
Summary of Learning Outcomes
9.1 Early Theories of Motivation 1. What are the basic principles of Frederick Taylor’s concept of scientific management?
Scientific management is based on the belief that employees are motivated by economic incentives and that there is “one best way” to perform any job. The four basic principles of scientific management developed by Taylor are as follows:

### S32

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [6], [9], [39]):
> Lean and Queuing Theory prove that 100% capacity utilization causes infinite queue delays, destroyed flow, and higher overall costs.

Markers on it:

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[6] source: open-practice-library:21149
What will you get?
Kanban will provide you a set of metrics to measure your process. These metrics are very usefull to improve your flow and identify points of failure.
* Lead Time: Measures how much time a task spends in the Kanban board, since get in and get out. A measure for our customers.
* Cycle Time: Measures how much time a task spends going through the process, from when the task started.
* Throughput: Measures the total amount of work delivered (completed work items).
These metrics are connected by the Little's Law: Cycle Time = WIP / Throughput

[9] source: open-practice-library:3823
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: manage-flow.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Manage Flow subtitle: Optimize the processing work items date: 2019-10-19T09:24:08.129Z authors:
- rhdojun tags:
- culture mobiusTag: foundation icon: /images/pullstuckcar.jpg whatIs: Direct the focus of optimization on work items, e.g. tasks, problems, process steps, instead of the people. That means metrics also need to focus on work items, not on people. whyDo: >- Everybody already experienced a few times in their life that it is totally possible that everybody is busy to the point of being overworked but the work gets done slower and slower.

[39] source: open-practice-library:3834
One could ask themselves, why is that? And what is more important? Is it better that everybody is busy or would it be better if more work gets done?
Usually in comparison it should be clear the second point is much more important: work needs to get done.
But to get there one cannot track indirect metrics like utilization of employees. Instead one needs to track work item related metrics like how long a task stays work in progress. And one needs to make visible when tasks get stuck so the team can analyse together why it got stuck and how this could be avoided the next time. howTo: >- Typical activities for managing flow are:

### S33

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [24], [59], [60], [61], [62]):
> Pure "blameless" models posit that human errors are 100% system-induced and individual discipline is always counterproductive.

Markers on it:

[24] source: lfuo-learning-review-guide-2024:477
“You’ve got nothing to fear if you’ve done nothing wrong.”
Punishing or blaming employees involved in an accident is the surest way to kill a learning culture. The attitude expressed in the quote above is a threat and has no place
in an FLA.
“Holding people accountable and blaming people are two quite different things. Blaming people may in fact make them less accountable: they will tell fewer accounts,
they may feel less compelled to have their voice heard, to participate in improvement efforts. Blame-free or no-fault systems are not accountability-free systems. On the contrary: such systems want to open the ability for people to hold their account, so that everybody can respond and take responsibility for doing something about the problem.

[59] source: open-practice-library:19780
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: blameless-postmortem.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Blameless Postmortem subtitle: Turn incident into an investment in future reliability date: 2022-03-22T11:10:08.413Z authors:
- jfilipcz tags:
- learn mobiusTag: delivery icon: /images/markus-winkler-afw1hht0nss-unsplash.jpg whatIs: >- Blameless Postmortem is a post-incident practice assessing an incident or other types of outages, its timeline, environment conditions, and all possible factors that lead an incident to happen. A postmortem typically also covers incident timeline and all factors that in a given organization generate incident, and impacts operators behavior before, during and after the outage has happened. Practice allows participants and stakeholders to quickly form conclusions on what were the most important factors contributing to the incident. It also serves a learning purpose, both by providing in depth experience for participants and by producing a postmortem summary which can be shared with all interested parties. A postmortem can be treated as the evolution of a Root Cause Analysis (RCA) which is done in almost all major IT support organizations.

[60] source: open-practice-library:19794
The major difference between an RCA and Blameless Postmortem is the way both of them are run, with the later putting emphasis not only establishing the root cause but also ensuring that there’s no form of possibly harmful judgement being made along the way. Often a postmortem is also carried out in a less formalized manner, making sure that the actual story comes before documentation.
“Our job is not to point fingers at an unlucky engineer that applied a wrong configuration file, our job is to figure out why he picked the wrong one and what we personally and as an organization can do to prevent it in the future.” whyDo: >- A Blameless Postmortem serves couple of important purposes:

[61] source: lfuo-learning-review-guide-2024:400
tremendous impact. If the Leader assumes the accident happened because someone failed to do
something right, then the natural response is to determine what rules or protocols were broken. This leads to identifying (or blaming) the rule breaker and then the
assumption is that we’ve returned the system to safety. Following this logic, all that’s needed are better rules or better compliance. And that’s the end of story— until the next accident. History has shown us that this approach is not only

[62] source: lfuo-learning-review-guide-2024:3841
Attempting to hold individuals “accountable” (in the traditional sense) for systems -level weaknesses or failures obliterates learning opportunities. Our employees are engaged in complex work in an increasingly complex environment. When we do not
pay homage to the complexities of the work environment in the wake of an accident and instead pretend that the work environment is simple or even complicated, we are not treating our employees fairly or affording them the dignity they deserve.
When employees are exposed to unfair treatment, the inevitable reaction is a breakdown in trust. When employees don’t trust the organization they work for, the

### S34

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [28]):
> Conventional executive views see AI as an individual labor-saving tool (writing syntax faster).

Markers on it:

[28] source: org-topologies-primer-2025:1533
“Doing” 
Task-​oriented work  without a view of the  whole picture.
Heavily reliant on  directives from others.
Operational efficiency booster for tasks requiring routine  expertise with intelligent automation, task-​specific agents, 
and virtual assistants.
Optimizes repetitive and tactical work.
Automated and predictive guidance within task execution.
Enhances productivity by reducing the  cognitive load.
Ensures consistent execution quality.
“Delivering”
Deliver value within a  narrow scope but often

### S35

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [3], [29], [66]):
> Org Topologies demonstrates that localized speedups in "doing" tasks without expanding team scope or removing dependencies merely compound downstream bottlenecks.

Markers on it:

[3] source: org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[29] source: org-topologies-primer-2025:1442
> What parts of the company are the focus of org development?  The Product Management and R&D departments, so focus on AI  investment there. 
> What archetypes are part of the target? What’s a dominant constraint  from one to the other?  The R&D department has mostly TASKS-1 individuals, and the target is  CAPS-3 teams. On investigation, it’s a lack of front-​end design and  coding skilled people. Focus time, money, and management attention on  AIs, especially on that big bottleneck, over a generic “adopt AI.”

[66] source: org-topologies-primer-2025:812
However, in order to streamline delivery, discovery must  remain separated in space and time. Similar to the Resource  Topology, Directing Archetypes emphasize up-​front analysis  to supply the work, and they may direct an “analysis Doing  unit” to discover and then write “the specs”, or they may  create them themselves. 
Keeping the teams ‘fast’ and constantly ‘efficient’ in  producing the outputs is only possible when the teams in the  Delivery Archetypes are permanently fixed to a narrow work  scope—​an internal component or a specific set of  capabilities. The other side of this coin is that they cannot  easily switch contexts. By the intentions of this org design,  teams lack the work mandate to engage with the “big  picture” but are allowed to expand their skill set becoming  more and more efficient within their narrow area of expertise.

### S36

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [29], [30]):
> AI investment must focus on expanding team capabilities to eliminate dependencies, not padding task-level coding speed.

Markers on it:

[29] source: org-topologies-primer-2025:1442
> What parts of the company are the focus of org development?  The Product Management and R&D departments, so focus on AI  investment there. 
> What archetypes are part of the target? What’s a dominant constraint  from one to the other?  The R&D department has mostly TASKS-1 individuals, and the target is  CAPS-3 teams. On investigation, it’s a lack of front-​end design and  coding skilled people. Focus time, money, and management attention on  AIs, especially on that big bottleneck, over a generic “adopt AI.”

[30] source: org-topologies-primer-2025:1446
Evolving rightward on the horizontal axis to broader skills mandate will  become ever easier due to AI. And likewise upward on the vertical axis  to a broader work mandate. So, top-​right Driving archetypes will  become more feasible.
Obviously, “adopt AI everywhere you can” will be the general guidance,  but given the limited resources of money, time, and attention, in  strategic org design with OT we recommend that you ask and answer  these questions:
For example, a pet-​supply company creates e-​commerce software in a  Resource topology. It’s a mature, uncomplicated market. Competition  has delivered a better website and app that customers love. Leadership  has decided on a business objective of retaining customers, with an org  goal of fast flow to parity, by targeting a Delivery topology with CAPS-3  teams.

### S37

Sentence (as the per-marker scorer copied it, trimmed to 200 characters; find the full sentence in the answer by its markers [4], [6], [25], [34], [40]):
> By ending multi-squad matrixing, capping Work-in-Progress, replacing velocity quotas with flow/quality metrics, and establishing a Just Culture, we can stabilize our customer portal, reduce bug-driven

Markers on it:

[4] source: open-practice-library:3783
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

[6] source: open-practice-library:21149
What will you get?
Kanban will provide you a set of metrics to measure your process. These metrics are very usefull to improve your flow and identify points of failure.
* Lead Time: Measures how much time a task spends in the Kanban board, since get in and get out. A measure for our customers.
* Cycle Time: Measures how much time a task spends going through the process, from when the task started.
* Throughput: Measures the total amount of work delivered (completed work items).
These metrics are connected by the Little's Law: Cycle Time = WIP / Throughput

[25] source: lfuo-learning-review-guide-2024:3849
flow of information is constrained.
We want to create a culture where employees feel safe to raise their hands and openly share unsafe conditions, individual mistakes, errors, close calls and risky decisions. A “Just Culture” is a workplace where employees at all levels are
accountable for their participation and their commitment to the organization’s
safety culture. The “Just” part of Just Culture which stems from the word Justice, is the essential and fundamental recognition that workers are inheritors of the tools,

[34] source: open-practice-library:21009
WIP Limit
Limit work in progress. These sample numbers represent the maximum number of functional items for workflow. Promote finishing and provoke important discussions. “Stop starting, start finishing!”
One Way
Do not move cards backwards. An item flows when work is completed at each step. If a correction needs to be made, keep the item in the same column, eventually signaling that a block exists. Focus on finishing.
Metrics
Throughput - The amount of items delivered in a given time frame, usually weeks.

[40] source: doe-hpi-handbook-vol1:9985
Department of Energy Human Performance Handbook Chapter 4 Culture & Leadership
accountable for their actions in the same fashion that someone who intentionally performs work he or she knows is contrary to known standards.
A just environment is all about getting the balance right between how willful violations and unintentional errors are addressed in the organization. All too often organizations do not make clear the distinctions between errors and violations. A just organization clears the smoke in the air between erring and violating. To do so, management sets a zero tolerance policy for reckless conduct—bad acts that we call violations. Zero tolerance for violations is balanced by the belief and the widespread confidence among the leadership that the vast majority of unintended unsafe acts will go unpunished as honest errors—unintended departures from expected behavior—on the part of the performer. There are proven methods to help organizations determine culpability for serious incidences in which unsafe acts are involved.
