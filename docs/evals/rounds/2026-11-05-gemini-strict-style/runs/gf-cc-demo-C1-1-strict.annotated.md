# demo-C1-1-strict

I'm CTO at a 140-person logistics SaaS. Three product lines, one engineering group of about 60 in nine squads. Every sprint overflows: we plan around 40 points, ship 25, and carry the rest into the next one. Marketing wants a feature a week for the growth push and says quality is engineering's problem; engineering says the churn numbers come from bugs. My head of engineering has set a "stretch" target of 40% more throughput by Q1 and tied the squad leads' bonus to it. Most developers sit on two or three squads at once, because the CEO's rule is that nobody is idle. Last month a bad release took the customer portal down for four hours; the postmortem named the developer who merged it, and he's now on a performance plan. The CEO's answer to all of this is to buy AI coding tools so we can "do both".

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
