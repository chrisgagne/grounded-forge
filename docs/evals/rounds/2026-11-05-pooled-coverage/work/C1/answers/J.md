# Answer J

MEMORANDUM
TO: Chief Executive Officer
FROM: Chief Technology Officer
DATE: November 4, 2026
SUBJECT: Operational Diagnosis, Prioritized Action Plan, and Theoretical Tensions in Engineering
1. What Is Actually Going On Here? (Systemic Diagnosis)
Resource Utilization vs. Flow Capacity:
Work in progress (WIP) limits frame the capacity of a team's workflow at any moment to establish stable and predictable delivery. When individuals take on all incoming tasks without limiting work in progress, they become overloaded, tasks get stuck, and overall responsiveness declines. Multitasking does not work, and reducing the batch size of efforts allows teams to finish work faster. Directing optimization toward high employee utilization rather than work item flow results in work getting done slower even when everyone is busy. In Scrum, a development team cannot make a firm commitment to deliver more than historical performance supports; attempting to do so leads to burnout, poor quality, loss of trust, and attempts at gaming the system.
My inference: Our rule requiring zero idle time by assigning developers to two or three squads simultaneously inflates work in progress and context switching across our nine squads.
My inference: Planning 40 story points per sprint when historical capacity supports only 25 points forces sprint overflow, creates chronic backlog carryover, and degrades software quality.
Perverse Incentives & Target Pressure:
Implementing unrealistic goals and high-pressure targets from the top down can create undue organizational pressure, leading to compromised standards and unethical or dysfunctional behaviors. Linking extrinsic rewards to target achievement shapes team dynamics and can damage morale. In organizational design, maximizing output metrics does not equate to maximizing outcomes, as producing more output often increases investment costs without improving overall business outcomes.
My inference: Tying squad leads' bonuses to a stretch target of 40% increased throughput incentivizes leads to push raw feature volume over technical rigor, accelerating bug creation.
My inference: Marketing's demand for weekly feature releases pushes the engineering organization past its empirical delivery capacity, shifting defect resolution into customer-facing churn.
Blame Culture vs. Systemic Root Causes:
Complex systems fail in complex ways, and limiting accident investigations to individual operator error or the last step in a process leads to the false belief that the problem is solved while leaving unresolved organizational system problems. Human error is a symptom of failure and latent organizational conditions, not the primary cause of system breakdown. Investigating incidents by asking what people could or should have done fails to explain why their actions made sense to them at the time. Punishing or shaming employees for honest errors undermines psychological safety, damages trust, and suppresses the open reporting of errors.
My inference: Placing the developer on a performance plan following the customer portal outage treats a single person as the root cause, ignoring underlying deployment and testing weaknesses.
My inference: This punitive action creates a blame cycle that discourages developers from transparently reporting risks or production issues.
The Myth of Local Tooling Fixes:
Attempting to solve delivery speed problems by introducing tools or platform changes in isolation without addressing surrounding workflow constraints or customer needs results in over-engineered solutions that fail to solve the core problem. The Theory of Constraints establishes that "Any improvements made anywhere besides the bottleneck are an illusion.".
My inference: Relying on AI coding tools to solve both velocity expectations and defect rates fails to address our primary organizational bottleneck, which is excessive work in progress and fragmented team structures.
No source in this notebook covers the specific impact of AI coding tools on software throughput or defect rates.
2. What to Change First and Why That First (Prioritized Action Plan)
Phase 1 (Immediate): Establish a Just Culture and Conduct Blameless Postmortems
A blameless postmortem evaluates incident timelines and contributing factors without making harmful judgments, focusing on why decisions made sense in real time. Applying the substitution test evaluates whether another well-motivated individual with similar skills and training would have committed the same error under identical circumstances. In a just culture, management holds the organization accountable for the systems it designs rather than punishing individual errors.
My inference: We must immediately take the release developer off the performance plan and re-evaluate the four-hour outage using a blameless postmortem framework.
My inference: This must be changed first because without restoring psychological safety, engineers will conceal risks and game metrics, preventing any further operational improvements.
Phase 2 (Near-Term): Restructure Teams for Single-Squad Focus and Cap Sprint Capacity
Organizing work into complete, multi-skilled cross-functional units increases flow and reduces cross-unit dependencies compared to fragmented functional resource allocation. Limiting work in progress and keeping team members focused on finishing current work before starting new items stabilizes workflow and reduces cycle times.
My inference: We should eliminate the zero-idle-time rule, assign developers dedicatedly to single squads, and cap sprint planning at our historical throughput of 25 points.
Phase 3 (Medium-Term): Align Priorities via Value Stream Constraints and Cost of Delay
The Theory of Constraints requires identifying the single bottleneck limiting throughput, exploiting it, and subordinating all other process steps to that constraint. Weighted Shortest Job First (WSJF) prioritizes backlog items by dividing cost of delay by job size to deliver high-value, smaller jobs first.
My inference: Product, Marketing, and Engineering must adopt WSJF prioritization to select high-value features collaboratively rather than demanding arbitrary weekly output targets.
3. Where the Thinking Disagrees With Itself (Theoretical Tensions)
Fixed-Iteration Planning vs. Continuous Flow Systems:
Scrum prescribes fixed-length timeboxed iterations (Sprints) with defined Sprint Goals and committed Sprint Backlogs. In contrast, Kanban advocates for continuous pull replenishment, explicit WIP limits per workflow column, and delivering items on demand as soon as they are ready rather than waiting for batch iteration boundaries.
My inference: Literature on agile practices contains a fundamental tension regarding whether software teams perform best under fixed batch timeboxes or continuous pull-based flow.
Individual Accountability vs. Systemic Just Culture:
Traditional management and incentive frameworks emphasize tying individual rewards strictly to job performance, enforcing individual performance-reward contingencies, and maintaining top-down targets. Conversely, Just Culture, High Reliability Organization (HRO), and Human Performance Improvement (HPI) literature argue that individual actions are shaped by organizational systems, and that holding individuals accountable for systemic failures destroys trust and learning.
My inference: Management theory is divided between holding individuals directly responsible for operational outcomes versus treating individual actions as downstream products of system design.
Resource Utilization vs. Flow Efficiency:
Classical administrative theories and Resource Topologies prioritize 100% resource utilization to ensure no personnel or machine capacity is idle. Conversely, Lean manufacturing, Kanban, and Theory of Constraints demonstrate that operating at 100% capacity creates severe queueing, increases lead time, and slows total system throughput.
My inference: Executive management assumptions favoring full human resource utilization directly contradict operational flow models that require slack capacity to maintain speed.
Efficiency-Thoroughness Trade-Off (ETTO):
System safety and ergonomics literature highlights the Efficiency-Thoroughness Trade-Off, recognizing that individuals and organizations face inherent goal conflicts between production speed and safety or quality precautions.
My inference: Demanding simultaneous increases in feature output speed and bug elimination represents an unresolvable operational trade-off unless workload constraints are reduced.
💡 Would you like to draft a 15-minute executive briefing slide deck outline based on this memo to prepare for your upcoming board or leadership meeting?
