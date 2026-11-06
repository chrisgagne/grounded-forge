# gemini-demo-C1-1-strict

Condition: chat-strict. Converted sources: corpus.commons/demo/sources/converted

## Question

I'm CTO at a 140-person logistics SaaS. Three product lines, one engineering group of about 60 in nine squads. Every sprint overflows: we plan around 40 points, ship 25, and carry the rest into the next one. Marketing wants a feature a week for the growth push and says quality is engineering's problem; engineering says the churn numbers come from bugs. My head of engineering has set a "stretch" target of 40% more throughput by Q1 and tied the squad leads' bonus to it. Most developers sit on two or three squads at once, because the CEO's rule is that nobody is idle. Last month a bad release took the customer portal down for four hours; the postmortem named the developer who merged it, and he's now on a performance plan. The CEO's answer to all of this is to buy AI coding tools so we can "do both".

I need a two-page memo for the CEO that says what's actually going on here, what to change first and why that first, and where the thinking you're drawing on disagrees with itself.

## Chat answer

I need a two-page memo for the CEO that says what's actually going on here, what to change first and why that first, and where the thinking you're drawing on disagrees with itself.

Answer here in the chat.

MEMORANDUM
TO: Chief Executive Officer
FROM: Chief Technology Officer
DATE: November 4, 2026
SUBJECT: Operational Diagnosis, Systemic Priorities, and Foundational Disagreements in Management Literature
1. What Is Actually Going On Here: Systemic Diagnosis
The Resource Utilization Fallacy and Multitasking:
Org Topologies defines a "Resource Topology" as an organizational structure designed to ensure that each unit is "100% utilized"[1:org-topologies-primer-2025].
My inference: Operating under the rule that no developer should be idle forces engineering staff across two or three squads simultaneously, treating developers as interchangeable resource units rather than focused delivery teams.
Open Kanban states that "multitasking does not work" and that limiting active tasks is necessary to deliver value faster with better flow[2:open-kanban].
My inference: Context-switching across multiple product lines inflates active work-in-progress, directly causing every sprint to overflow.
Little's Law defines the relationship between flow metrics as "Cycle Time = WIP / Throughput"[3:open-practice-library].
My inference: High work-in-progress across nine squads inflates total cycle times and reduces overall delivery throughput.
Unrealistic Commitments and Incentive Distortions:
Scrum guidance recommends setting sprint forecasts based on historical capacity rather than wishful thinking[4:approach-perfect-field-guide-scrum-events][5:approach-perfect-field-guide-scrum-events].
My inference: Planning for 40 points when average historical velocity is 25 points creates a perpetual planning deficit that guarantees carryover.
Agile guidance warns that attempting to firm-commit to backlogs beyond historical velocity leads to "burnout, poor quality, loss of trust, and/or attempts at 'gaming the system'"[6:approach-perfect-field-guide-scrum-events].
Goodhart's Law dictates that "when a measure becomes a target, it ceases to become a good measure"[7:open-practice-library].
My inference: Tying squad leads' bonuses to a 40% throughput target encourages story point inflation and quality trade-offs rather than real engineering productivity gains.
No source in this notebook covers how marketing growth pushes directly influence customer churn numbers.
Blame Culture vs. System Safety:
The Department of Energy Human Performance Handbook explains that stopping investigations at active human error leaves underlying latent weaknesses uncorrected, while asserting that events triggered by human error are often "symptomatic of a system failure"[8:doe-hpi-handbook-vol1][9:doe-hpi-handbook-vol1].
The Columbia Accident Investigation Board report notes that limiting causal investigations to individual operator error leads to the false belief that problems are solved[10:caib-report-vol1][11:caib-report-vol1].
My inference: Naming and placing a developer on a performance plan following the customer portal outage misattributes a systemic deployment failure to individual neglect, driving a destructive blame cycle.
The Illusion of Non-Bottleneck Improvements:
The Theory of Constraints establishes that "any improvements made anywhere besides the bottleneck are an illusion"[12:open-practice-library].
My inference: Buying AI coding tools to accelerate code generation will not improve overall delivery throughput if the primary bottleneck lies in context switching, testing, and deployment verification.
No source in this notebook covers the impact of AI coding tools on software bug creation rates or customer portal outages.
2. What to Change First and Why That First
First Priority: Eliminate Multi-Squad Allocation and Cap Work in Progress (WIP)
The Theory of Constraints outlines a five-step cycle requiring organizations to identify the primary constraint and subordinate all other processes to it[13:open-practice-library][14:openstax-accounting-vol2].
Limit Work in Progress principles state that pipes that are not clogged increase overall flow through the system[15:open-practice-library].
My inference: The single highest-leverage intervention is to end multi-squad assignments and enforce dedicated developer allocation to a single squad.
My inference: Subordinating squad assignments to WIP limits directly addresses the root bottleneck of context switching, which will immediately stabilize cycle times and improve software quality.
Second Priority: Establish Empirical Planning and Remove Metrics-Based Bonuses
Scrum standards state that a team should function as a cohesive unit focused on one objective at a time, equipped with all cross-functional skills necessary to create value[16:scrum-guide-2020].
My inference: Sprint planning must be anchored strictly in historical capacity (25 points) rather than top-down targets.
My inference: Rescinding the bonus tie to throughput targets stops metric gaming and restores story points as a neutral estimation tool.
Third Priority: Transition to a Just Culture for Deployment Safety
Just Culture frameworks define accountability as a forward-looking process where organizations learn from systemic conditions rather than inflicting retributive punishment[17:lfuo-learning-review-guide-2024][18:lfuo-learning-review-guide-2024].
My inference: Removing the developer from the performance plan and replacing individual blame with systemic learning reviews will rebuild trust and encourage open reporting of software defects.
3. Where the Foundational Thinking Disagrees With Itself
Stretch Goals & Financial Incentives vs. System Dynamics & Intrinsic Motivation:
Management literature asserts that setting stretch goals and utilizing variable-pay bonus programs can inspire employees and serve as key levers to drive organizational performance[19:open-practice-library][20:openstax-introduction-business][21:openstax-principles-management].
Conversely, goal setting literature cautions that narrow goals and rigid targets can have unintended consequences, such as causing employees to neglect other duties, set easy targets, or engage in unhealthy competition[22:openstax-organizational-behavior][23:openstax-principles-management].
My inference: Executive management models assume financial incentives force higher effort, whereas agile and systems literature shows that financial targets on delivery metrics distort estimates and degrade code quality.
Resource Utilization vs. Flow Efficiency:
Traditional resource management models aim to reach business objectives by keeping 100% of personnel "100% busy"[24:org-topologies-primer-2025].
In contrast, flow management frameworks state that tracking individual employee utilization slows work down and that optimization must focus on work item metrics like work-in-progress duration[25:open-practice-library][26:open-practice-library].
My inference: Classical management design prioritizes high resource utilization, while modern flow frameworks prove that operating near 100% capacity starves system responsiveness and delays customer value.
Individual Performance Accountability vs. System Safety & Just Culture:
Traditional performance management models advocate tying rewards directly to individual job output and establishing clear performance-reward contingencies[27:openstax-accounting-vol2][28:openstax-organizational-behavior][29:openstax-organizational-behavior].
Conversely, Just Culture literature argues that blaming individuals for system-level failures obliterates learning opportunities and reduces trust[30:lfuo-learning-review-guide-2024][31:lfuo-learning-review-guide-2024].
My inference: Standard human resource models place accountability on the individual line worker, whereas safety science places accountability on management for the system environment supporting that worker.
AI Capacity Expansion vs. System Constraints:
Org Topologies literature suggests that AI adoption makes expanding team skill mandates easier and more feasible[32:org-topologies-primer-2025].
However, Theory of Constraints literature maintains that adding capacity outside the primary bottleneck yields zero total throughput improvement[12:open-practice-library][33:open-practice-library].
My inference: Strategic AI adoption frameworks treat AI tools as a direct booster of organizational capability, whereas constraint theory warns that generating code faster without resolving flow bottlenecks merely creates inventory buildup.
💡 Would you like me to draft a 30-day implementation roadmap for restructuring the nine squads into dedicated, single-assignment teams?




## Citation legend (full chunk text per marker)

[1] org-topologies-primer-2025:749
Resource Topology There are three common Org Topologies to know, starting  with: The Resource Topology—​a topology characterized by  frozen functional archetypes specialized in one domain. Its  purpose is to ensure that each unit is 100% utilized (i.e.  resource utilization). It is seen in “resource management”  approaches where “resource managers” (or project  managers) are responsible for planning and monitoring  resource allocation and utilization.
In this topology, the value-​creation work takes place among  the Doing Archetypes in the lower left quadrant. However,  none of these can independently produce end-​to-​end  customer value. They depend on each other due to narrow  specialization. Additionally, they lack a clear and holistic  understanding of customer value, as their work mandate  focuses solely on specific tasks or capabilities.

[2] open-kanban:115
3. Reduce the Batch Size of your Efforts Research in the way the mind works, and countless experiences from Lean, the Theory of Constraints and Kanban confirm that to deliver value faster, with better flow and good team morale we need to focus and limit the number of things we do. Multitasking does not work. Limiting how many things you do at any given time, means reducing the batch size of whatever you are doing at a particular stage of the value chain. By doing this you will deliver value faster because you are able to focus your efforts, one of the best explanations of this fact has been given by Donald G. Reinertsen. Keeping the team focused helps them finish what they start faster. Limiting WIP is a consequence of reducing the batch size of your efforts, and not the other way around. However doing either will result in improvements in efficiency and productivity. Open Kanban does not ask you to limit WIP, but it does request that you “Reduce the Batch Size of your Efforts.” How do you reduce the batch size of your efforts? Reduce the complexity and the quantity of things you do at any stage of the value chain. In software development this would mean: reduce the number of large stories (epics) you create, and do your best to keep stories simple; also reduce the volume of stories you work on any stage of the Software Development Life Cycle; this way your team will focus, and deliver more value.

[3] open-practice-library:21149
What will you get?
Kanban will provide you a set of metrics to measure your process. These metrics are very usefull to improve your flow and identify points of failure.
* Lead Time: Measures how much time a task spends in the Kanban board, since get in and get out. A measure for our customers.
* Cycle Time: Measures how much time a task spends going through the process, from when the task started.
* Throughput: Measures the total amount of work delivered (completed work items).
These metrics are connected by the Little's Law: Cycle Time = WIP / Throughput

[4] approach-perfect-field-guide-scrum-events:234
it in Story Points, but note that this is not officially part of the Scrum framework.
Outputs  
• A prioritized Sprint Backlog that the team expects—ideally based on data and not just
wishful thinking—to fully complete by the end of the Sprint time-box.
• An initial sense of how the Development Team ( ap.tips/devteam ) will work together to
accomplish the Sprint Goal and deliver the product Increment .
• A Sprint Goal that can be met through the implementation of at least most of the Sprint

[5] approach-perfect-field-guide-scrum-events:324
  43 24
50 31
× 4 ≈ 3 A few Scrum-oriented tools on the market will calculate a forecasted Velocity for you, but we are not aware of any that address all edge cases well, particularly accounting for changes in Capacity and the number of Development Team members. It’s probably easiest to use the free Velocity calculator we’ve created for your use, located at ap.tips/velocitytool . If the work in process in your carried-over Sprint Backlog meets or exceeds your forecast velocity and it is all still valuable to work on, we strongly recommend against taking in any new work this Sprint . You may even need to remove some items. This can be painful, but it’s honest empirical process control ( ap.tips/empirical ) : the data available to us tells us that this is all that our Development Team is capable of, even if we wished we could do more.

[6] approach-perfect-field-guide-scrum-events:396
Tips  
• If your team does not have a known, stable Velocity (ideally 3-4 sprints worth of data) or chooses not to use a quantitative approach, try using “Fists of Five” ( ap.tips/fistsoffive ).
• The Development Team cannot and must not make a firm commitment to delivering the entire Sprint Backlog or even the Sprint Goal . ( ap.tips/tradeoffs ) Attempting to do so will only lead to burnout, poor quality, loss of trust, and/or attempts at “gaming the system.” Instead, the Sprint Backlog and Sprint Goal is a focusing tool that limits context switching and a good-faith forecast that the Development Team attempts to live up to.
• A mature team should be able to deliver 85-115% of the planned work or Velocity every sprint. If a team consistently underdelivers, this usually means that they are not being truly empirical and they are taking on more work than their historical performance supports.
• A team with a new backlog should spend close to 10% of their time building out their backlog before each Sprint Planning session. A well-established team can afford to spend less. If you are finding that it is hard to fully complete the “what are we building” phase of Sprint Planning within a one-hour per Sprint week time-box, you likely need more preparation from the Product Owner and/or Backlog Refinement .

[7] open-practice-library:9202
Points of note:
Try to keep this survey anonymous. Honest answers are of utmost importance.
Resist the temptation to measure too frequently. Once per quarter or every six months is appropriate.
Avoid setting score improvement as a goal - be conscious that GoodHart's Law means that when a measure becomes a target, it ceases to become a good measure.
If you have a large enough organisation, or enough data over time, you could try applying data science practices to identify outliers in the data that can indicate particular areas of concern, for particular teams, or disruptive events that correlate with a dip in scores. mediaGallery:

[8] doe-hpi-handbook-vol1:9858
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

[9] doe-hpi-handbook-vol1:10185
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

[10] caib-report-vol1:9658
17 Space Flight Operations Contract, Performance Measurement System Reports for January 2003, February 2003, USA004840, issue 014, contract NAS9-2000.
9 0
41
Many accident investigations do not go far enough. They identify the technical cause of the accident, and then connect it to a variant of "operator error" — the I i ne worker who forgot to insert the bolt, the engineer who miscalculated the stress, or the manager who made the wrong decision. But this is seldom the entire issue. When the determinations of the causal chain are limited to the technical flaw and individual failure, typically the actions taken to prevent a similar event in the future are also limited: fix the technical problem and replace or retrain the individual responsible. Putting these corrections in place leads to another mistake — the belief that the problem is solved. The Board did not want to make these errors.

[11] caib-report-vol1:20531
22 Changing personnel is a typical response after an organization has some kind of harmful outcome. It has great symbolic value. A change in personnel points to individuals as the cause and removing them gives the false impression that the problems have been solved, leaving unresolved organizational system problems. See Scott Sagan, The Limits of Safety. Princeton: Princeton University Press, 1993.
Diane Vaughan, The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA (Chicago: University of Chicago Press. 1996).

[12] open-practice-library:8588
This is why “Any improvements made anywhere besides the bottleneck are an illusion.”
In some systems, the bottleneck is clear to see, such as a narrow junction on a busy street, or a bend in a garden hose.
In some systems, especially those that don't have material, or "inventory" flowing through them, the constraint can be more difficult to see. This includes many business or technology processes such as software and product development.
Using the Theory of Constraints (ToC) to identify bottlenecks (constraints) in a process enables teams and organisations to decide where to focus optimisation work. When the optimisation, elevation, or removal of the constraint is complete, the process begins again to find the next constraint (because there is always the next one). howTo: >- This practice assumes that you already have a way of measuring the process - such as looking at tickets in jira, cards on a kanban board, or other tools. If you don't, then you can use techniques such as MBPM or value stream analysis to identify where the bottlenecks could be.

[13] open-practice-library:8611
Stage 1: Identify the constraint. Look at where "Work In Progress" (WIP) is piling up.
Stage 2: Exploit the constraint. Are there any quick improvements you can make to the throughput of this stage? This is essentially "making the most of what you have". Check to see if you've solved the constraint and moved the bottleneck somewhere else.
Stage 3: Subordinate the constraint. Look at the rest of the process. Are other stages really aligned with this stage? Is there something another stage could do that could improve the flow through this stage? Maybe other stages could add a little more documentation, make a few tweaks to their process, or take on some of the work? Check to see if you've solved the constraint and moved the bottleneck somewhere else.

[14] openstax-accounting-vol2:2610
Examples of Constraints
Bottleneck Examples
Physical Employee resources, limited space, equipment resources
Policy Procedures, regulations, contracts
Culture “It’s the way we’ve always done it”
Market Size of the market, demand for product, nature of competition
Table 1.5
There are five steps in the cycle of continuous improvement under TOC:
1. Identify the system constraint. 2. Decide how best to exploit the constraint and make quick changes using existing resources. 3. Subordinate everything else to the process to ensure alignment with and support of the needs of the

[15] open-practice-library:3783
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

[16] scrum-guide-2020:240
building trust.
5
Scrum Team
The fundamental unit of Scrum is a small team of people, a Scrum Team. The Scrum Team consists of
one Scrum Master, one Product Owner, and Developers. Within a Scrum Team, there are no sub-teams
or hierarchies. It is a cohesive unit of professionals focused on one objective at a time, the Product Goal.
Scrum Teams are cross-functional, meaning the members have all the skills necessary to create value
each Sprint. They are also self-managing, meaning they internally decide who does what, when, and

[17] lfuo-learning-review-guide-2024:458
It is concerned with preventing the next accident, not focused on correcting history.
In the criminal justice arena accountability means punishments and correction. In
our Just Culture, accountability means creating the space for each person involved to provide an honest account of what happened from his or her perspective. The agency is then held accountable to learn about the conditions that influenced the
outcome and make improvements to the overall system.
Post incident/accident, accountability means that we hold ourselves and each other accountable to learn from the event. When mistakes are made, this recognition may

[18] lfuo-learning-review-guide-2024:489
This also has different implications for what we mean by accountability. If we see an act as a crime, then accountability means blaming and punishing somebody for it. Accountability in that case is backward-looking, retributive. If, instead, we see the act
as an indication of an organizational, operational, technical, educational or political issue, then accountability can become forward-looking (Sharpe 2003). The question becomes what should we do about the problem and who should bear responsibility for

[19] open-practice-library:13594
C﻿ommitment - When you are part of a team defining the problem you are going to solve, and there is clarity on how success is defined. You have the ingredients for autonomy and empowerment. People will naturally commit.
Track - Know how you are doing, so you can change if you need to. This transparency also fosters accountability... there are no locked cupboards or water melon reports
R﻿esults - S﻿etting stretch goals and maintaining focus on them, will inspire and motivate people to do great work. I﻿ndeed, teams that consistently used goal setting frameworks can achieved a 3X increase in productivity in 12 months (Source: Align) howTo: >- Writing OKRs should be a bottom-up (80%) and top-down (20% process).  So thinking about the top-down, you should definitely make sure you have sight of the draft OKRs at the level above your team so you can align. If it's not clear, then have a chat with someone or ideally get them to present to your team as it's really key that your team all understand what bigger outcomes your team is working towards. 

[20] openstax-introduction-business:27115
Economic Incentives Any discussion of motivation has to include the use of monetary incentives to enhance performance. Currently, companies are using a variety of variable-pay programs such as piece-rate plans, profit sharing, gain sharing, stock options, and bonuses to encourage employees to be more productive. Unlike the standard salary or hourly wage, variable pay means that a portion of an employee’s pay is directly linked to an individual or organizational performance measure. In piece-rate pay plans, for example, employees are paid a given amount for each unit they produce, directly linking the amount they earn to their productivity. Profit-sharing plans are based on overall company profitability. Using an established formula, management distributes some portion of company profits to all employees. Gain-sharing plans are incentive programs based on group productivity. Employees share in the financial gains attributed to the increased productivity of their group. This encourages employees to increase productivity within their specific work area regardless of the overall profit picture for the organization as a whole.

[21] openstax-principles-management:15497
Both performance management and rewards systems are key levers that can be used to motivate and drive individual and group performance ... which leads to overall organizational performance, productivity, and growth. Performance and rewards systems are also “cultural” in that they provide a glimpse into the way a company manages the performance (or nonperformance) of its employees, and to what extent they are willing to differentiate and reward for that performance. There has been a great deal of discussion over the years to identify best practices in the ways we differentiate and reward employees, which will also drive employee performance and motivation.

[22] openstax-organizational-behavior:10607
Goal theory can be a tremendous motivational tool. In fact, many organizations practice effective management by using a technique called “management by objectives” (MBO). MBO is based on goal theory and is quite effective when implemented consistently with goal theory’s basic premises.
Despite its many strengths, several cautions about goal theory are appropriate. Locke has identified most of them.30 First, setting goals in one area can lead people to neglect other areas. (Randi may word process 70 pages per day, but neglect her proofreading responsibilities.) It is important that goals be set for most major duties. Second, goal setting sometimes has unintended consequences. For example, employees set easy goals so that they look good when they achieve them. Or it causes unhealthy competition between employees. Or an employee sabotages the work of others so that only she has goal achievement.

[23] openstax-principles-management:21375
Goal theory can be a tremendous motivational tool. In fact, many organizations practice effective management by using a technique called “management by objectives” (MBO). MBO is based on goal theory and is quite effective when implemented consistently with goal theory’s basic premises.
Despite its many strengths, several cautions about goal theory are appropriate. Locke has identified most of them.30 First, setting goals in one area can lead people to neglect other areas. (Randi may word process 70 pages per day, but neglect her proofreading responsibilities.) It is important that goals be set for most major duties. Second, goal setting sometimes has unintended consequences. For example, employees set easy goals so that they look good when they achieve them. Or it causes unhealthy competition between employees. Or an employee sabotages the work of others so that only she has goal achievement.

[24] org-topologies-primer-2025:783
Learning in this topology is largely confined to improving  existing skills rather than discovering new ones. The  Resource Topology is fit for organizations that rent available  resources for their existing defined skills, reaching their  business objectives (e.g. making profit) by keeping 100% of  them 100% busy. Such a topology is a management’s choice  and justified, for example, when the relationships are  temporary between the Directing and Doing archetypes (e.g.  a movie Producer hiring dancers for a scene).

[25] open-practice-library:3823
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
<!-- file: manage-flow.md -->
--------------------------------------------------------------------------------
templateKey: practice-page title: Manage Flow subtitle: Optimize the processing work items date: 2019-10-19T09:24:08.129Z authors:
- rhdojun tags:
- culture mobiusTag: foundation icon: /images/pullstuckcar.jpg whatIs: Direct the focus of optimization on work items, e.g. tasks, problems, process steps, instead of the people. That means metrics also need to focus on work items, not on people. whyDo: >- Everybody already experienced a few times in their life that it is totally possible that everybody is busy to the point of being overworked but the work gets done slower and slower.

[26] open-practice-library:3834
One could ask themselves, why is that? And what is more important? Is it better that everybody is busy or would it be better if more work gets done?
Usually in comparison it should be clear the second point is much more important: work needs to get done.
But to get there one cannot track indirect metrics like utilization of employees. Instead one needs to track work item related metrics like how long a task stays work in progress. And one needs to make visible when tasks get stuck so the team can analyse together why it got stuck and how this could be avoided the next time. howTo: >- Typical activities for managing flow are:

[27] openstax-accounting-vol2:25192
How can you motivate your employees to perform to your standards so that your company goals are met? Will an hourly wage be sufficient? Should you pay per task or per job? What motivation will they have to sell your company’s services to others? How will you know if they are performing the tasks in the manner you set forth? To answer these questions, you will need to be aware of the goals of your company, such as increasing the number of clients, as well as the goals of your employees, such as receiving raises, bonuses, or promotions. Armed with this knowledge, you will be able to design relevant evaluation measures and tie those measures to appropriate performance rewards so that both your goals and the goals of your employees are met. This same

[28] openstax-organizational-behavior:12543
• Trust levels between managers and subordinates must be high.
• Individual performance must be able to be accurately measured.
• Pay rewards to high performers must be substantially higher than those to poor performers.
• Few, if any, negative consequences for good performance must be perceived.
Under these conditions, a climate or culture is created in which employees have reason to believe that significant performance-reward contingencies truly exist. Given this perception (and assuming the reward is valued), we would expect performance to be increased.15

[29] openstax-organizational-behavior:12992
of contribution to the organization. Extrinsic rewards Rewards that are external to the work itself. Flexible benefits system A rewards program where employees are allowed some discretion in the
determination of their own packages and can make trade-offs, within certain limits. Gain sharing An incentive plan in which employees or customers receive benefits directly as a result of cost-
saving measures that they initiate or participate in. Graphic rating scale A performance appraisal technique where the supervisor or rater is typically presented

[30] lfuo-learning-review-guide-2024:477
“You’ve got nothing to fear if you’ve done nothing wrong.”
Punishing or blaming employees involved in an accident is the surest way to kill a learning culture. The attitude expressed in the quote above is a threat and has no place
in an FLA.
“Holding people accountable and blaming people are two quite different things. Blaming people may in fact make them less accountable: they will tell fewer accounts,
they may feel less compelled to have their voice heard, to participate in improvement efforts. Blame-free or no-fault systems are not accountability-free systems. On the contrary: such systems want to open the ability for people to hold their account, so that everybody can respond and take responsibility for doing something about the problem.

[31] lfuo-learning-review-guide-2024:3841
Attempting to hold individuals “accountable” (in the traditional sense) for systems -level weaknesses or failures obliterates learning opportunities. Our employees are engaged in complex work in an increasingly complex environment. When we do not
pay homage to the complexities of the work environment in the wake of an accident and instead pretend that the work environment is simple or even complicated, we are not treating our employees fairly or affording them the dignity they deserve.
When employees are exposed to unfair treatment, the inevitable reaction is a breakdown in trust. When employees don’t trust the organization they work for, the

[32] org-topologies-primer-2025:1446
Evolving rightward on the horizontal axis to broader skills mandate will  become ever easier due to AI. And likewise upward on the vertical axis  to a broader work mandate. So, top-​right Driving archetypes will  become more feasible.
Obviously, “adopt AI everywhere you can” will be the general guidance,  but given the limited resources of money, time, and attention, in  strategic org design with OT we recommend that you ask and answer  these questions:
For example, a pet-​supply company creates e-​commerce software in a  Resource topology. It’s a mature, uncomplicated market. Competition  has delivered a better website and app that customers love. Leadership  has decided on a business objective of retaining customers, with an org  goal of fast flow to parity, by targeting a Delivery topology with CAPS-3  teams.

[33] open-practice-library:8577
The Theory of Constraints shows us that in any process, there must be a single bottleneck that limits the total throughput of the process: in the same way that a chain has a weakest link, a process has a single slowest component. whyDo: >- Whilst it may be easy to improve some part of the process, if that component isn't the bottleneck, it will either have zero effect on the throughput because the bottleneck is upstream, or it will actually cause more pain in the system by adding pressure to the bottleneck, if the bottleneck is downstream.

## Quotation locations

4 quotations, 4 found
  found    approach-perfect-field-guide-scrum-events:404 burnout, poor quality, loss of trust, and/or attempts at 'gaming the system'
  found    open-practice-library:9211                    when a measure becomes a target, it ceases to become a good measure
  found    doe-hpi-handbook-vol1:10188                   symptomatic of a system failure
  found    open-practice-library:8565, open-practice-library:8588 any improvements made anywhere besides the bottleneck are an illusion

