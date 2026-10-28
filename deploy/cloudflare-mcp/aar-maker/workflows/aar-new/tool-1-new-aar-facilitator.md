# Tool 1: New AAR Facilitator

**Purpose:** Hand-hold total beginners through creating a solid After-Action Review from scratch.

**Audience:** Teams new to AARs, first-time facilitators, anyone who hasn't done formal incident analysis before.

**Output:** A complete, well-structured AAR document ready for review.

---

## Framework Guidance

**First, call `route`.** It returns the AAR task index: six phase sections, each a set of rows that name a need, the source that serves it, and when it applies. This tool's phases map onto those sections:

| This tool's phases | `route` section |
|--------------------|-----------------|
| 0 Setup, 2 Problem Type | Phase 0: Scoping |
| 1 Timeline, 3 Reconstructing Decisions | Phase 1: Timeline and local-rationality reconstruction |
| 4 to 6b, 6d | Phase 2: Contributory-factor analysis |
| 6c Just Culture | Phase 3: Just-culture sorting |
| 7 to 9 | Phase 4: Action design |
| 10 AAR Document and Close | Phase 5: Learning-loop closure |

**For practical HOW-TO guidance, read the distillation each row names** (`read_distillation` with its slug):
- Example: For local rationality → doe-hpi-handbook-vol1 (inside-view questions, via Dekker); doe-hpi-handbook-vol2 (debrief before you know too much)
- Distillations contain: questions to ask, patterns to look for, worked examples

Use `route` for WHEN to apply a source. Use distillations for HOW to apply it. References and deep references are not served here; use distillations for all analysis.

---

## CRITICAL: This Tool Is Interactive

**DO NOT generate a complete AAR in one shot.** This tool is a facilitated conversation.

### How to Use This Tool

1. **Start with Phase 0 (setup), then Phase 1** — Ask the questions, wait for answers
2. **One phase at a time** — Complete each phase before moving to the next
3. **Pause and ask** — After presenting questions, STOP and wait for user input
4. **Build incrementally** — Compile the AAR document piece by piece as you go
5. **Push back when needed** — If answers are shallow, ask follow-up questions

### Pacing for 90-Minute Target

| Phase | Time | % | Key Activity |
|-------|------|---|--------------|
| **0. Setup** | 5 min | 6% | Pull data via MCP, confirm scope |
| **1. Timeline** | 15 min | 17% | Backward timeline with evidence links |
| **2. Problem Type** | 5 min | 6% | What kind of problem this is |
| **3. Reconstructing Decisions** | 10 min | 11% | What made each decision seem right at the time |
| **4. Contributing Factor Analysis** | 20 min | 22% | 5 Whys (multi-chain) + mapping to the five points |
| **5–6c. Organizational Factors, Drift, Handoffs, Just Culture** | 10 min | 11% | Organizational mapping, drift, handoffs, fair accountability |
| **6d. What Went Well** | 5 min | 6% | Resilience, adaptations, things to keep |
| **7–9. Side Effects, Constraint, Actions** | 15 min | 17% | Archetype check, constraint test, urgency rating, ticket creation |
| **10. AAR Document and Close** | 5 min | 6% | Write the AAR, summarize learnings, check facilitator presence |

**Time management rules:**
- Each phase is a separate conversational turn — present questions, WAIT for response
- Warn at 50% and 75% of total time ("We're halfway through — Phases 4–10 still ahead")
- If running long on Phase 4, offer: "We can go deeper with the aar-deep workflow after — let's capture the key contributing factors and move to actions"
- **Never skip Actions (Phase 9)** — an AAR without actions is a list of good intentions

**Never skip ahead.** The learning happens in the conversation, not the document.

---

## MCP Integration

This tool can automatically pull incident data from connected systems. Use available MCP tools to gather evidence; when no relevant connection is available, offer paste mode and wait for the user to provide data.

### CRITICAL: Write Operations Require Confirmation

**Always ask before performing any write operation via MCP.** This includes creating, editing, or deleting tracker tickets, sending Slack messages, updating stories, adding comments, or any other action that modifies external systems.

The only write operation that does NOT require confirmation is writing the AAR document into the conversation.

**Why:** MCP write operations affect shared systems visible to the entire team. A ticket created prematurely, a story updated incorrectly, or a comment posted before the AAR is finalized can cause confusion. The user must explicitly approve each write action.

**Pattern:**
```markdown
"I'm ready to [create/update/delete] [what] in [system]. Here's what I'll do:

[Preview of the action — ticket name, description, team, etc.]

Shall I proceed?"
```

**This applies to:**
- Creating tracker tickets with the connected tracker
- Updating tracker tickets with the connected tracker
- Adding external links, comments, or checklist items
- Sending Slack messages
- Any other MCP tool that modifies state

**Read operations are always safe** — pulling bug details, searching Slack, reading PRs, etc. require no confirmation.

### Available Data Sources

| MCP Server | What It Provides | When to Use |
|------------|------------------|-------------|
| **issue-tracker** | Bug details, comments, linked items, status history, iterations, team assignment | Pull bug ID details at start; create action item tickets at end |
| **Slack** | Channel messages, threads, search results | Start with the channel or thread where the incident was worked. Then search the team's release and team channels for context. |
| **Microsoft Teams** | Channel messages, chat threads | Search the team's incident channels |
| **Code host** (GitHub, Azure DevOps or similar) | Commits, PRs, review threads, pipelines, releases, deployments | Pull PR details linked from the bug, identify what changed, deployment history |
| **Jira** | Issues, comments, linked issues | Alternative to issue-tracker for bug tracking |
| **Confluence** | Wiki pages, documentation | Pull runbooks, architecture docs, prior AARs for context |
| **Microsoft 365** | Emails, calendar events | Search for incident-related communications |
| **Zendesk** | Customer tickets, support interactions | Pull customer reports that led to detection |
| **Alerting tool** (PagerDuty, Datadog or similar) | Alerts, incidents, on-call schedules | Alert timeline, who was paged, escalation path, response times |

**You are an outside model to the practitioner's organisation.** Before they paste anything, ask them to redact customer data and credentials. If a credential appears in anything you read or are given, say so and leave it out of everything you write.

### Automatic Data Gathering

Once the incident is identified and the first account is taken (Phase 0), automatically pull:

```
1. Bug/Story Details (issue-tracker, when connected)
   → Get full bug details using the connected tracker
   → Extract: team assignment (for action items), linked stories, comments

2. Incident Timeline (Slack)
   → **Follow `slack-incident-ingestion.md` (in this skill's folder) for the full procedure.** That file is authoritative; its sections are Discovery; Meeting notes and transcripts; Personal data and credentials; Time handling; Live vs closed incidents; and Data-quality notes.
   → Short version:
     - Find the channel or thread where the incident was worked: from the ticket's chat link, or by asking the practitioner.
     - Read its messages for the incident window only. Use whatever search and read functions the connected chat tool offers, and page through results until they run out; if you can't, say the coverage is partial.
     - Look for meeting notes, transcripts and files posted in that window (logs, screenshots, documents). Note in the AAR which came from an automated note-taker and which from people.
     - If there is no meeting transcript, reconstruct from the written messages and say so in the AAR section ("chat-only reconstruction, no meeting transcript available"). Log the absence in Data-Quality Notes.
     - Several calls or meetings per incident are normal. Merge them chronologically.
     - Normalise timestamps to UTC; render local zone alongside.
   → **Supplementary searches (lower priority):**
     - The channels where the incident was announced, for the bug ID
     - The team's release channel for deployment times and hotfixes
     - The team's chat channel for context
   → **Business-side comms:** Check the team's stakeholder-update channel for stakeholder framing and customer-impact decisions.
3. Deployment Context (connected code host: GitHub, Azure DevOps or similar)
   → Get recent releases around incident time
   → Identify commits/PRs merged before detection
   → For PRs linked from the bug: get metadata (title, author, reviewers, dates), the commits included, and the review threads
   → Extract: what changed, who reviewed, what concerns were raised

4. Related Incidents (issue-tracker)
   → issue-tracker: search tickets: Find similar past bugs
   → Check for patterns in recent high-priority bugs
```

**Claude Code tip:** Steps 1-4 are independent—run MCP calls in parallel for faster gathering.

### Similar Incidents Finder

After gathering bug details, automatically search for past incidents that may inform this AAR.

**Search Strategy:**

```markdown
1. Extract keywords from bug title and description
   → System names, error types, component names

2. Search past 12 months:
   → issue-tracker: search tickets: type=bug, team={same team}
   → issue-tracker: search tickets: description contains {keywords}

3. Filter for incidents with AARs:
   → Check each bug's linked documents for an AAR
   → OR check comments for an AAR link
   → Only include bugs that HAVE an AAR

4. Rank by relevance:
   - Same component/system: High relevance
   - Same team: Medium relevance
   - Similar keywords: Lower relevance
```

**Output Format:**

```markdown
"I found {N} similar past incidents with AARs:

| Bug | Title | Date | AAR Link | Similarity |
|-----|-------|------|----------|------------|
| {Ticket-ID} | {Title} | {Date} | [AAR]({url}) | Same component |
| {Ticket-ID} | {Title} | {Date} | [AAR]({url}) | Same team |

**Patterns from these AARs:**
- {Ticket-ID} identified {key finding}
- {Ticket-ID} found {key finding}

Want me to pull insights from these to inform our analysis?"
```

**Incident Class Detection:**
If 3+ incidents cluster at the **same system boundary** (not just similar symptoms), name this as an *incident class*, not a recurring incident:

```markdown
"These {N} incidents all occur at the {X}↔{Y} boundary. This isn't '{incident} that recurred' — 
it's an incident CLASS. Different symptoms, same structural fragility. This reframes the 
analysis from 'how do we prevent recurrence of this bug' to 'what is structurally fragile 
about this boundary.'"
```

The trigger is same *boundary*, not same *symptoms*. Two incidents with identical symptoms but different boundaries are recurring bugs. Two incidents with different symptoms at the same boundary are an incident class — and the class is the unit of analysis.

**If past incidents exist without AARs:**
```markdown
"Note: I also found {N} similar high-priority bugs WITHOUT AARs:
- {Ticket-ID}: {Title} ({date}) — No AAR found

This might indicate a pattern of incidents not getting analyzed."
```

### Creating Action Items

**IMPORTANT: Before creating any action items, ASK the user:**

```markdown
"I've identified {N} action items from this AAR. Would you like me to:

1. **Create tickets** — I'll create tracker tickets for each action
2. **Read-only mode** — I'll list the actions but won't create tickets (you can create them manually later)

Which would you prefer?"
```

When user chooses "Create tickets" mode, create tracker tickets with confirmation for each:

```
→ Use the connected issue-tracker to create a ticket for each action
   - Include contributing factor context, success criteria, urgency and owner

TEAM ASSIGNMENT:
   - Short-term/tactical actions: Use the SAME TEAM as the original bug
   - Long-term/structural actions (ownership changes, process documentation,
     budget decisions, architectural changes): Ask which team owns the change

   Example team assignments:
   - "Add validation to [component]" → Original bug's team
   - "Create automated regression test" → Original bug's team
   - "Revisit [tradeoff] decision" (what we optimise for) → Responsible leadership team
   - "Restructure [boundary/team/process]" (who owns what) → Responsible leadership team
   - "Fund [environment/tooling]" (budget decision) → Responsible leadership team

→ Add labels and acceptance criteria using the connected tracker's supported fields
   - Do NOT set priority automatically from urgency; ask how the team prioritises work

NOTE: Ask the user where the AAR should be stored and linked
   - If no archive is connected, return markdown for manual filing
```

### Evidence Linking

For timeline events, always include MCP-sourced evidence:
- Slack message permalinks
- Code host commit SHAs, PR URLs and release IDs
- Code review thread links (when concerns were raised pre-merge)
- tracker ticket links

### ⚠️ MCP Availability Gate (HARD REQUIREMENT)

**Before gathering ANY data, verify MCP access.** If MCP servers aren't configured or unavailable:

1. **STOP.** Do not proceed with data gathering.
2. **Report exactly which MCPs are missing** and what data each would provide.
3. **Ask the user to choose:** paste mode (they provide data manually) or abort.

**Do NOT:**
- Silently search local files, grep for bug IDs, or read existing AARs as a substitute
- Proceed with partial data without explicit user acknowledgment
- Treat MCP failure as a soft warning — it is an error condition that requires user decision

**Paste mode** (only after user explicitly chooses it):
- User pastes bug details (from issue-tracker)
- User pastes Slack thread excerpts
- User provides deployment timeline manually
- User decides what data to provide — you don't guess
- Ask the user to redact customer data and credentials before pasting; if a credential appears, say so and leave it out of everything you write

---

## How This Tool Works

This tool guides you through creating an AAR step-by-step. At each phase, it:
1. Explains what we're doing and why (in plain language)
2. Asks specific questions to gather information
3. Teaches the underlying concept as you go
4. Builds the AAR document incrementally

**No prior knowledge required.** The tool introduces frameworks (the five points, 5 Whys, etc.) as they become relevant, not upfront.

---

## Terminology: Always Explain Jargon

**When using framework terminology in conversation or AAR output, ALWAYS explain it in plain language.**

| Term | Always Explain As |
|------|-------------------|
| **Handoff problem** | "Failures at handoffs between teams. Each team may be working well, but work gets stuck waiting between them." |
| **The five points** | "Five places in how an organization is designed where a problem can come from: what we optimise for, who owns what, how work moves, what gets measured and rewarded, and who we hire, grow and staff." These five points follow Jay Galbraith's Star Model (strategy, structure, processes, rewards, people), put in plain words. |
| **Cynefin** | "A way of telling what kind of problem you're facing—clear, complicated, complex, or chaotic" |
| **Local rationality** | "Understanding why decisions seemed right at the time, given what people knew" |
| **Drift** | "How acceptable practices gradually shift toward risky ones without anyone noticing" |
| **Systems archetype** | "Common patterns where fixes create new problems" |

The five points, used as factors throughout this tool:

| Point | What it asks in an AAR |
|-------|------------------------|
| **What we optimise for** | What were we built to be good at, and what do we optimise for when goals compete? |
| **Who owns what** | Who owns a complete enough problem to act, and where must decisions cross a boundary? |
| **How work moves** | How work is chosen, planned, handed off and checked, within and across teams |
| **What gets measured and rewarded** | What pay, recognition, targets and pressure encourage people to do |
| **Who we hire, grow and staff** | Capability, staffing, expertise and load |

**Example - Don't say:**
> "This incident shows a clear Shifting the Burden pattern."

**Instead say:**
> "This incident shows a pattern called Shifting the Burden: the quick workaround eased the pressure, so the harder fix kept getting put off while the real problem grew."

---

## Methodology Transparency

This tool applies the following frameworks, introduced progressively as needed:

| Framework | When Introduced | Plain Language Name |
|-----------|-----------------|---------------------|
| Evidence-based timelines | Phase 1 | "What actually happened?" |
| Cynefin domains (Snowden) | Phase 2 | "What kind of problem is this?" |
| Local rationality (Dekker, via the DOE handbooks) and schedule pressure (Columbia report) | Phase 3 | "What made decisions seem right? What pressures existed?" |
| 5 Whys | Phase 4 | "Keep asking why" |
| The five points | Phase 5 | "Where in the organization did this come from?" |
| Drift analysis (Columbia report, DOE handbook) | Phase 6 | "Did this sneak up on us?" |
| Handoff analysis (Org Topologies primer: Krivitsky, Larman and Flemm) | Phase 6b | "Was everyone fast but nothing got done?" |
| Just Culture (NHS Just Culture Guide) | Phase 6c | "What kind of behavior was this?" |
| Systems archetypes (SSDL, after Kim and Senge) | Phase 7 | "Will our fix create new problems?" |
| Theory of Constraints (Goldratt) | Phase 8 | "What's THE bottleneck?" |
| Action design (DOE handbook: controls over reminders) | Phase 9 | "How do we make this stick?" |

**Why this order:** We start with facts (timeline), then context (what kind of problem), then dig into causes, then map to organizational factors, then generate actions. Each phase builds on the previous.

---

## Framework Reference Files

**Before each phase, call read_distillation on each slug named in the Library source column.** Rows without a slug are the three credited methods this tool uses as its own scaffolding (Snowden's Cynefin, the five points after Galbraith's Star Model, Goldratt's Theory of Constraints). Other ideas from published work are cited by library slug. The workflow's own checks and labels (the quality scorer, incident-class detection, the copy-paste and stability tests, the urgency-and-duration sort, the Leadership Request and similar) are this workflow's conventions, not library methods; present them as such.

| Phase | Framework | Library source | When to Read |
|-------|-----------|----------------|--------------|
| Phase 2 | Cynefin domains | Cynefin (Snowden) | Before asking domain questions |
| Phase 3 | Local rationality | doe-hpi-handbook-vol1 (inside-view questions, via Dekker); doe-hpi-handbook-vol2 (debrief before you know too much); caib-report-vol1 (schedule pressure) | Before reconstructing decisions |
| Phase 4 | 5 Whys + whole-system stance | open-practice-library (Five Whys); open-kanban (Deming's and Goldratt's whole-system stance, borrowed-through) | Before CFA (reinforces systemic focus) |
| Phase 5 | The five points | The five points (see Terminology) | Before organizational mapping |
| Phase 6 | Drift analysis | caib-report-vol1 (normalisation, weak signals, schedule pressure, vigilance decays); doe-hpi-handbook-vol1 (bald-tire attitude, at-risk behaviour becoming automatic) | Before checking for drift |
| Phase 6b | Handoff analysis | org-topologies-primer-2025 (capability-incomplete teams, Resource-Topology drag, local optimisation) | Before handoff analysis |
| Phase 6c | Just Culture | nhs-just-culture-guide (five tests, walked in order); doe-hpi-handbook-vol2 (culpability spectrum); lfuo-learning-review-guide-2024 (forward-looking accountability) | Before behavior assessment |
| Phase 7 | Systems archetypes | ssdl-systems-thinking-foundations (five system archetypes, borrowed-through) | Before checking for side effects |
| Phase 8 | Theory of Constraints | Theory of Constraints (Goldratt); open-kanban (whole-system stance only; it doesn't develop the constraint method) | Before constraint identification |
| Phase 9 | Action Urgency | open-kanban (batch size, WIP) | Before action prioritization (batch size, WIP) |
| Phase 9 | Action design | doe-hpi-handbook-vol1 (engineered over administrative controls; marking the critical step) | Before converting actions to checklists or procedure steps |

**Additional ideas (consult shipped distillations where named):**
- lfuo-learning-review-guide-2024 (forward-looking accountability) — For forward accountability framing
- open-kanban (batch size, WIP) — For WIP and iteration/capacity context
- flo-facilitation-guide (open questions that draw out the participant's account rather than carry the facilitator's conclusion); tc-25-20-army-aar (open-ended questions) — For questioning technique
- approach-perfect-field-guide-scrum-events (Prime Directive, borrowed-through); open-practice-library (1-2-4-All) — For facilitation techniques (Prime Directive, 1-2-4-All)

**Claude Code tip:** Read distillations just-in-time at each phase rather than all upfront to manage context.

---

## Phase 0: Session Setup

Before starting the AAR, check MCP server availability and help the user get the most out of the session.

### Encourage MCP Setup
```markdown
I can pull incident data automatically if you have MCP servers configured.
The more sources connected, the richer our timeline will be:

- **issue-tracker**: Bug details, linked stories, comments
- **Slack**: Incident threads, [incident channel], [release channel] channels
- **Code host (GitHub, Azure DevOps or similar)**: Deployment history, commits
- **Confluence**: Runbooks, prior AARs

Would you like to configure any of these before we start, or shall we proceed?
```

### Bug Selection
If MCP is available and user says "ready to do an AAR" without specifying a bug:

```markdown
Let me check for recent high-priority bugs that might need AARs...

→ issue-tracker: search tickets: type=bug, the team's top priority level, last 90 days
→ For each bug, check linked documents and comments for an AAR
   - If an AAR is found, exclude from list

Here are the high-priority bugs from the last 90 days that don't appear to have AARs yet:
[List bugs with ID, title, date, priority]

Which one would you like to review? Or enter a different bug ID.
```

### First account, before the records
Once the incident is identified, and before pulling detailed records, ask the practitioner:

```markdown
"Before I pull the records: in a few sentences, what would you tell a coworker about this incident?"

"Who saw it differently, and what would they say? Give me their view in your words, or paste theirs."
```

Keep both answers exactly as given. They are the first accounts. After the records are pulled, compare them with the draft timeline and treat differences as things to explore, not errors to correct. Hearing the story before reading the record follows `doe-hpi-handbook-vol2` (Concept 4): debrief before you know too much.

---

## Phase 1: Getting Started

### What we're doing
Building a factual timeline of what happened. This keeps us honest—memories change after stressful events.

Call route for this phase and read the distillations it returns before asking these questions.

### Accounts first
Start from the first accounts taken in Phase 0. If the practitioner will talk to others who were involved, get each person's own account before showing them the assembled record. `doe-hpi-handbook-vol2` (Concept 4) says to debrief participants before acquiring detailed knowledge of the event, let them tell the story, and mark the critical junctures. Then check the accounts against the draft timeline below, and treat differences as things to explore, not errors to correct.

### Auto-Draft Timeline (MCP-Enabled)

**Before asking the timeline questions below**, automatically assemble a draft timeline from available data sources. This reduces manual effort and surfaces evidence users might miss.

```markdown
## Auto-Timeline Assembly

### Step 1: Pull data in parallel

**Tracker Ticket:**
→ issue-tracker: get ticket by ID: {bug_id}, with its full history
→ Extract: created date, status changes, comments with timestamps
→ **Priority check:** Ask for the team's own priority definitions and assess the bug's priority against them; if none are provided, ask the user to paste them.

**Slack Channels:**
→ **Incident channel or thread (PRIMARY):** Find where the incident was worked, from the
  ticket's chat link or by asking the practitioner. Read its incident-window history for
  troubleshooting, diagnosis, and responder decisions.
→ Search the channels where the incident was announced for the bug ID
→ Search the team's release channel for deployment times and hotfixes
→ Search the team's chat channel for context
→ Check the stakeholder-update channel for stakeholder-side context

**Code host PR (if the ticket links one):**
→ Get the PR's metadata from the connected code host (GitHub, Azure DevOps or similar)
→ Extract: created, approved and merged dates

**Code host pipeline (if available):**
→ Get the recent pipeline runs
→ Extract: build completion, deployment timestamps

### Step 2: Assemble timeline

Sort all timestamps and categorize events:

| Event Type | Source | Timestamp Field |
|------------|--------|-----------------|
| Bug reported | issue-tracker | Created date |
| Escalated | Slack [incident channel] | First message timestamp |
| Investigation started | Slack thread | Activity start |
| Fix PR opened | Code host | PR created date |
| Fix reviewed | Code host | PR approval timestamp |
| Fix merged | Code host | PR merged date |
| Deployed | Pipeline | Completion timestamp |
| Resolved | issue-tracker | State → Done transition |

### Step 3: Present draft

"Here's a draft timeline I assembled from your systems:

| Time (UTC) | Event | Source |
|------------|-------|--------|
| {timestamp} | Bug reported | issue-tracker created date |
| {timestamp} | Escalated | Slack [incident channel] |
| {timestamp} | Investigation started | Slack thread |
| {timestamp} | Fix PR opened | Code host PR #{id} |
| {timestamp} | PR approved by {reviewer} | Code host |
| {timestamp} | Fix merged | Code host |
| {timestamp} | Deployed to production | Release pipeline |
| {timestamp} | Marked resolved | issue-tracker state change |

**Gaps I couldn't fill automatically:**
- Detection method (how was it noticed?)
- Customer impact numbers
- Any events in non-integrated systems

**What's missing or incorrect?**"
```

### Timeline Construction Approach
**Start from NOW (the time of the AAR) and work backwards** through:
1. Resolution → "When was it resolved?"
2. Detection → "When did we first notice?"
3. Pre-detection → "What was happening before that?"
4. Contributing factors → "What changed that caused this?"

Working backward is this workflow's choice for keeping each entry tied to evidence you hold, rather than a story told forward.

### Questions to ask (after presenting auto-draft)
```markdown
Based on the timeline draft above, let's fill in the gaps:

1. **What's the incident?** (Bug ID, title, brief description)
2. **When was it resolved?** (Date/time normal operation resumed)
3. **When was it first detected?** (Date/time, who noticed, how)
4. **What was the impact?** (Customers affected, revenue, reputation)

Now let's work backwards from detection:
5. **What was happening just before detection?**
6. **What changed that might have caused this?** (Deployment, config change, external event)
7. **Were there any earlier warning signs we missed?**
```

### Evidence Sources (MCP-Enabled)

**If MCP servers are configured, automatically pull:**

```markdown
1. **issue-tracker** (if available):
   → issue-tracker: get ticket by ID: Pull full bug details
   → issue-tracker: search tickets: recent bugs owned by the practitioner
   → Extract: description, comments, linked stories, workflow history

2. **Slack** (if available):
   → **Incident channel or thread (PRIMARY):** Find where the incident was worked, from the
     ticket's chat link or by asking the practitioner. Read the message history for the
     incident window — technical diagnosis, decisions, and responder commentary may be captured here.
   → Search the channels where the incident was announced for the bug ID or keywords
   → Search the team's release channel for deployment times and hotfixes
   → Search the team's chat channel for context
   → Extract: timestamps, participants, key decisions

3. **Microsoft Teams** (if available):
   → Search the team's incident-update channel
   → Search incident-specific channels
   → Extract: call recordings, chat threads

4. **Code host** (GitHub, Azure DevOps or similar, if available):
   → List recent deployments before incident time
   → Check the bug for linked PRs; get each PR's metadata, commits and review threads
   → Get build and release history
   → Extract: what changed, who reviewed and approved, concerns raised, release times, deployment stages
```

**⚠️ If MCP not available: STOP.** Stop automatic data gathering and offer paste mode for timeline construction. Remind the user which MCPs failed the availability gate (see MCP Availability Gate, above) and ask them to paste from (redacting customer data and credentials first):
- Slack channel messages
- tracker ticket URL
- Deployment logs or commit history
- Alerting systems (PagerDuty, Datadog, etc.)

**Do NOT** search local files, grep the codebase, or read existing AAR documents as a substitute. Missing data = ask the user, never fabricate or substitute.

### Teaching moment
> "We build timelines backwards from detection to keep each entry tied to evidence. If we start from the beginning, it's easy to tell a story and fit the facts to it. Starting from 'when did we notice?' and working back keeps us on what we can show."

### Evidence Link Quality Standard

Every timeline entry must have a verifiable evidence link. Apply these standards:

- **Slack:** Use message-level permalinks with timestamps (e.g., `https://workspace.slack.com/archives/{CHANNEL_ID}/{MESSAGE_ID}`), not channel URLs
- **issue-tracker:** Link to specific comments when possible (e.g., `[comment permalink]`), not just the story
- **Code host:** Link to specific PR, commit, or pipeline run
- **Inferred evidence:** If an event is inferred rather than directly sourced, mark it explicitly as "Inferred — [rationale]" and list it as a gap to fill. Generic URLs (e.g., `https://app.slack.com/client`) are not acceptable evidence links.

The evidence trail is what separates an AAR from a post-mortem opinion piece. If you can't link to it, flag the gap.

### Output format
```markdown
## Timeline of Events (All times in UTC)

| Date/Time | Event | Evidence Link |
|-----------|-------|---------------|
| [Time] | [What happened] | [Slack/commit/alert link] |
```

---

## Phase 2: Understanding the Problem Type

### What we're doing
Not all problems are the same. Some have clear causes; others are genuinely complex. This determines how we analyze.

Call route for this phase and read the distillations it returns before asking these questions.

### Questions to ask
```markdown
Let's figure out what kind of problem this is:

**Answer these questions:**

1. Looking back, was the cause obvious once you found it?
   - [ ] Yes, clear in hindsight
   - [ ] Needed expert analysis to understand
   - [ ] Still not entirely clear why it happened
   - [ ] Completely novel situation

2. Could this happen again the same way?
   - [ ] Yes, if nothing changes
   - [ ] Maybe, depends on conditions
   - [ ] Unlikely, it was a unique combination
   - [ ] Unknown
```

### Teaching moment
> "Some problems have clear causes you can find and fix. Others emerge from multiple factors interacting in ways that weren't predictable. Knowing which type you're dealing with prevents frustration—don't expect single causes for genuinely complex situations."

### Split Domain Assessment

Different aspects of an incident can live in different Cynefin domains. The technical cause may be Complicated (discoverable, fixable) while the organizational response may be Complex (emergent from interacting factors). When this occurs, note the split — it changes which analytical tools apply to which chain.

**Example:** "The label-printing defect is Complicated — one template, one fix, replicable in test. But the two-week gap between the first mis-shipped parcel and the fix is Complex — it emerged from the interaction of returns data nobody watched, customer reports routed to the depot instead of the software team, and a peak-season freeze on non-urgent changes, in ways no single factor explains."

### How this affects analysis
Use Snowden's Cynefin framework to match the analysis to the kind of problem. Where the cause was clear once found, find it and fix it. Where it needed expertise, bring the experts in and analyse thoroughly. Where many factors interacted, look for contributing factors and build resilience. Where the situation was novel and chaotic, stabilise first and analyse later.

---

## Phase 3: Reconstructing Decisions

### What we're doing
When humans made decisions that contributed to the incident, we need to understand their context—not to blame, but to understand what the system needs to change.

Call route for this phase and read the distillations it returns before asking these questions.

### Questions to ask
```markdown
For each key decision point in the timeline:

1. **What information did they have at the time?**
   (Not what we know now—what did THEY know THEN?)

2. **What were they trying to achieve?**
   (What goal were they working toward?)

3. **What pressures were they under?**
   (Deadlines, competing priorities, resource constraints)

4. **What would most people have done in the same situation?**
   (Be honest—is this a reasonable decision given the context?)
```

### Decision Context Table

**Always produce a decision context table** for each key decision point identified in the timeline. The table format ensures decisions are analyzed consistently and makes them shareable with stakeholders who weren't in the room.

```markdown
| Decision | Timestamp | What Was Known | What Was Missing | Time Pressure | Alternatives Available |
|----------|-----------|----------------|------------------|---------------|----------------------|
| [Decision] | [When] | [Info they had] | [Info they didn't] | [Pressure level] | [What else could they have done?] |
```

**Example:**
| Decision | Timestamp | What Was Known | What Was Missing | Time Pressure | Alternatives |
|----------|-----------|----------------|------------------|---------------|-------------|
| Logged as a routine support ticket | Nov 14 | Three mis-shipped parcels reported from one depot; dispatch still running | Reports from other depots hadn't been linked, so the pattern across depots was invisible | Peak-season queue | Re-assess once a second depot reports the same fault: a pattern across depots points to software, not a local printer |

### Teaching moment
> "When someone 'made a mistake,' imagine 100 different people in the same situation with the same information and pressure. How many would have done the same thing? If most of them would have, the problem isn't the person—it's the situation. That's what we need to fix."

### Pressure Question

After reconstructing local rationality, ask:

**"What did people believe the schedule required at this point?"**

The Columbia Accident Investigation Board (`caib-report-vol1`, Concept 7) asks what the people involved believed the schedule required, not only what the schedule said, and names the mechanism: small additions of risk, accepted little by little to stay on schedule. The DOE handbook (`doe-hpi-handbook-vol1`, Concept 1) adds that most departures from a rule are well intentioned, made to get the job done the way management wants it. This isn't failure—it's rational choice under constraints.

**Follow-up prompts:**
- "What pressure made the shortcut seem right at the time?"
- "If someone had taken the slower, safer route, what would they have given up?" (time, other work, meeting deadline)
- "What risk was accepted here, a little at a time, to stay on schedule?"
- "Has this same shortcut been taken before in this area?"

**Watch for drift:** A shortcut taken under pressure today ("I'll skip documentation this once") becomes tomorrow's normal practice. The DOE handbook (`doe-hpi-handbook-vol1`, Concept 11) notes that at-risk behaviours are rarely penalised and, left uncorrected, become automatic. When the same shortcut keeps winning in the same areas, that's a systemic signal for action items.

**Link to the five points:** These pressures often map to:
- **What gets measured and rewarded:** Measured on speed, not quality
- **How work moves:** The careful version is too slow to be practical
- **Who owns what:** Handoffs create pressure to "just get it done"

---

## Phase 4: Contributing Factor Analysis (5 Whys)

Phase 4 needs deeper reasoning than earlier phases. Identify independent factor chains before tracing depth. Two chains beats one deep chain — most Complicated/Complex incidents have multiple paths.

### What we're doing
Most incidents in complex systems have multiple independent contributing factors — not a single cause. We identify the distinct factor chains first, then trace each to depth using 5 Whys until we reach a stable cause — one that would persist if nothing changes. For most incidents, this lands in organizational territory (who owns what, how work moves, what we optimise for). For Clear-domain incidents with obvious technical causes, the stable cause may be simpler — and that's OK.

Call route for this phase and read the distillations it returns before asking these questions.

### Identifying Contributing Factor Chains

Before tracing depth, identify the independent chains:

**Chain identification questions:**
- "What are the distinct things that had to be true for this to happen?"
- "If we fixed one factor, would the incident still have occurred via a different path?"
- "Are there separate failure modes interacting?"

**Common chain patterns:**
- **Chain A:** Why did the defect exist? (technical/process)
- **Chain B:** Why wasn't it caught before impact? (detection/testing)
- **Chain C:** Why was the response slow? (escalation/communication)

**How the chains relate:** For each chain, say which of these is true. It was *necessary* if removing it would have prevented the incident. It was *sufficient* if it could have caused the incident on its own. It *interacted* if it only did harm in combination with another chain. Most incidents need several chains together: the Forest Service guide (`lfuo-learning-review-guide-2024`, Concept 11) finds that multiple improbable events were usually needed. Chains count as separate when each has its own path of whys, whichever of the three applies.

For Clear-domain incidents, a single chain may be sufficient. For Complicated or Complex incidents, expect 2+ chains.

### Who Has Got Past This? (Discovery & Action Dialogues)

Before tracing failures to depth, ask the question the Liberating Structures handbook builds into its Discovery & Action Dialogues (`liberating-structures-handbook`, Concept 3): who or where have you seen get past this barrier?

```markdown
"Before we dig into what went wrong — when did this failure NOT happen despite similar conditions? Who here, or where, has got past this?"
```

If such cases exist, they show what the system already does well, not just what went wrong.

**Follow-up prompts:**
- "What was different about those times?"
- "What keeps us from doing that all the time?"
- "Is there a team or person who consistently avoids this failure — and what do they do differently?"

Capture these cases in the AAR. They inform action items: start from what already works here before inventing new fixes.

### Questions to ask (per chain)
```markdown
Let's dig deeper. We've identified [N] contributing factor chains.

**Chain [A/B/C]: [Brief description]**

**Why #1:** Why did [the immediate failure in this chain] happen?
→ [Answer]

**Why #2:** Why was that possible?
→ [Answer]

**Why #3:** Why does the system allow that?
→ [Answer]

**Why #4:** Why hasn't that been addressed?
→ [Answer]

**Why #5:** What makes this the natural outcome? (In most cases, this is organizational — but follow the evidence, not the template.)
→ [Answer]
```

### IMPORTANT: Follow the Evidence, Not the Examples

The examples below teach the METHOD of pushing deeper — not the answers you should reach. Every incident has its own contributing factors. If you find yourself reaching the same conclusion as an example, pause and ask: "Am I following THIS incident's evidence, or am I pattern-matching from the example?" The examples show the SHAPE of good analysis; the content must come from the actual incident.

### Common Stopping Points That Aren't Contributing Factors

Most 5 Whys stop too early at **symptom categories**. These feel like contributing factors but aren't:

| Symptom Category | Why It's Not Deep Enough | Keep Asking... |
|------------------|--------------------------|----------------|
| "No process existed" | WHY didn't it exist? Was it never created, or did it erode? | Why wasn't this process a priority? What would have had to be true for it to exist? |
| "Teams operate independently" | WHY do they operate independently? Is it structure, incentives, or history? | What about the org design causes this? Who benefits from independence? |
| "No one owned it" | WHY was there no owner? Was it unclear, contested, or deliberately avoided? | What makes ownership ambiguous here? What would have to change to create clear ownership? |
| "It wasn't documented" | WHY wasn't it documented? Was it known but not written, or truly unknown? | What's the organization's relationship with documentation? Why did this knowledge stay tacit? |
| "Communication gap" | WHY was there a gap? Different tools, schedules, incentives, or mental models? | What structural barriers prevent this communication? What would make it automatic? |
| "Technical debt" | WHY was debt accumulated? Was it a conscious tradeoff or gradual erosion? | What pressures led to accepting this debt? What would have to change to pay it down? |
| "We didn't know about the dependency" | WHY didn't you know? Was it undocumented, or was there no reason to look? | What made this dependency invisible? What system would have surfaced it? |

### CRITICAL: Push Past the Process Gap to the Other Four Points

**AARs often stop at "process gap" — but process gaps don't exist in a vacuum.**

A process gap sits under **How work moves**. Every process gap has a deeper "why" in one or more of the other four points:

| If you found... | Ask... | The deeper contributing factor might be... |
|-----------------|--------|-----------------------------------|
| **Process gap** | "Why doesn't this process exist or work?" | ↓ See below ↓ |

**Push to What we optimise for:**
> "Was this process deprioritized? Did we accept this risk consciously? What were we optimizing for instead?"

- If the answer involves tradeoffs, deadlines, or priorities → **What we optimise for**
- Example: "We didn't add [safeguard] because it was deemed too expensive" → The organization chose to accept the risk

**Push to Who owns what:**
> "Why does this work cross team boundaries? Could one team or team-of-teams have owned this end-to-end? What about the org structure made this handoff necessary?"

- If the work crossed boundaries that didn't need to exist → **Who owns what**
- Example: "This required four teams because each owns a component, not a feature" → Component team structure creates handoff points. The Org Topologies primer (`org-topologies-primer-2025`, Concept 1) names this: a team asked for an end-to-end outcome without the capabilities to finish it needs a cross-silo handoff, so a failure at that handoff is structural, not behavioural.
- **When boundary failures recur:** If this isn't the first time work failed at a team boundary, ask a deeper question: "Are we proposing to manage a boundary that shouldn't exist?" The difference between "add an escalation policy for cross-team issues" (boundary management) and "restructure so one team owns this end-to-end" (boundary elimination) is the difference SSDL draws between acting on the event and acting on the feedback loop that keeps producing it (`ssdl-systems-thinking-foundations`, Phase 4). Both are valid. But if boundary management keeps appearing in action items across AARs, the boundaries themselves may be the constraint — and managing them is Shifting the Burden away from the structural change.

**Push to What gets measured and rewarded:**
> "What happens when someone proposes adding this safeguard? Is that welcomed or resisted?"

- If adding safety steps is culturally discouraged → **What gets measured and rewarded**
- Example: "Adding steps slows releases, and we're measured on velocity" → Incentives misaligned

**Push to Who we hire, grow and staff:**
> "Did people have the knowledge, time, and authority to fix this before it became an incident?"

- If people knew but couldn't act → **Who we hire, grow and staff** (capability, capacity, or authority gap)
- Example: "The engineer knew this was risky but didn't have time to address it" → Capacity constraint

Note: the open-practice-library Five Whys warns against stopping at "not enough time or people". When a chain lands on capacity, ask why the process didn't accommodate it before naming Who we hire, grow and staff as the factor.

**The complete question set for any process gap:**

```markdown
We found a process gap: [describe]

1. **What we optimise for:** Was this a conscious tradeoff? What were we optimizing for instead?
2. **Who owns what:** Why does this work cross team boundaries? Could one team or team-of-teams own this end-to-end?
3. **What gets measured and rewarded:** What happens when someone proposes adding safeguards here?
4. **Who we hire, grow and staff:** Did people have the knowledge, time, and authority to prevent this?
```

**Why this matters:**
- A process fix assumes someone will maintain it (Who owns what)
- A process fix assumes it will be prioritized (What we optimise for)
- A process fix assumes people will follow it (What gets measured and rewarded)
- A process fix assumes people can execute it (Who we hire, grow and staff)

**If any of those assumptions are false, the process fix will fail.**

**Example deep dive:**
- **Process-level finding:** "The deployment pipeline doesn't validate [downstream dependency]"
- **What we optimise for:** "Was excluding this validation a conscious decision?" → Maybe — investigate
- **Who owns what:** "Why does this work cross team boundaries? Could one team or team-of-teams own this end-to-end?" → Work splits across component teams → **Structural gap**
- **What gets measured and rewarded:** "What happens if someone proposes adding a step?" → Welcomed → Not a rewards issue
- **Who we hire, grow and staff:** "Did the team know about this dependency?" → No → Knowledge gap (possibly surfaced by the structural gap)

**Facilitator note:** The deep dive above is an EXAMPLE SHAPE, not a template for conclusions. Each incident has its own contributing factors. The point is to push past process into the point that actually explains WHY the process gap exists. Where you land depends on YOUR incident's evidence, not on this example.

### The Real Test: Specificity + Actionability

Ask yourself (for each chain):
1. **Could I copy-paste this contributing factor to a different incident and have it still make sense?**
   - If YES → It's a symptom category, keep going
   - If NO → You might be at a real contributing factor

2. **If we addressed this factor, would it actually prevent recurrence via this chain?**
   - "Create a process" → Maybe, but WHY will this process be followed when others aren't?
   - "The deployment pipeline doesn't include X because it was built before X existed, and there's no mechanism to revisit pipeline design when new dependencies are added" → NOW you have something specific

3. **Do your chains converge to a single generic conclusion?**
   - If YES → You've probably followed only one branch. Look for independent chains.
   - If NO → Good — distinct chains reveal distinct intervention options.

### Quality check
Your final "why" on each chain should NOT be:
- ❌ "Requirements were incomplete" (too generic—could apply to any incident)
- ❌ "Testing missed it" (too generic)
- ❌ "Someone made a mistake" (that's blame, not a contributing factor)
- ❌ "Communication gap" (too vague)
- ❌ "No process existed" (WHY didn't it exist?)
- ❌ "Teams weren't aligned" (WHY weren't they aligned?)
- ❌ "It wasn't a priority" (WHY wasn't it? What WAS the priority instead?)

Your final "why" on each chain SHOULD be:
- ✅ Specific enough that it couldn't be copy-pasted to other AARs
- ✅ About the system (which is usually organizational — who owns what, how work moves, what we optimise for — but could be purely technical for Clear-domain incidents)
- ✅ Something that, if addressed, would prevent recurrence via that chain
- ✅ Explains WHY the gap/missing process/misalignment exists, not just THAT it exists

### Example: Shallow vs. Deep

**Shallow (stops too early):**
1. Why did the API fail? → A downstream component threw an error
2. Why did the component error? → It referenced a removed dependency
3. Why wasn't the component updated? → No process to sync components after upstream changes
4. Why is there no process? → Teams operate independently ← **STOP: This is a symptom category**

**Deep (keeps going):**
1. Why did the API fail? → A downstream component threw an error
2. Why did the component error? → It referenced a removed dependency
3. Why wasn't the component updated? → No process to sync components after upstream changes
4. Why is there no process? → The pipeline was designed before the downstream system was adopted; there's no mechanism to revisit pipeline design when new dependencies are added
5. Why is there no mechanism to revisit? → Pipeline changes require cross-team coordination, but there's no regular forum or trigger for that review. Dependencies are only discovered in production incidents.
6. Why are dependencies only discovered in incidents? → Architectural decisions were made without documenting the operational constraints they would create. There's no review process that surfaces "if X changes, Y breaks" relationships.

**Now you have something specific to THIS incident.** The final "why" should be unique to your context — it names a concrete mechanism that explains why the gap persisted. Where it lands among the five points (What we optimise for? Who owns what? What gets measured and rewarded? Who we hire, grow and staff?) depends on what the evidence tells you, not on a template.

### Teaching moment
> "If your final 'why' on any chain could apply to dozens of different incidents unchanged, you haven't found a contributing factor—you've found a symptom category. And if all your chains converge to the same generic conclusion, you've probably followed only one branch. Keep asking until you reach something specific to your situation."

### Facilitator note
**If the user stops at a symptom category, push back:**
- "That's a common pattern—but WHY does that condition exist here? What would have had to be true for it to be different?"
- "I've seen 'teams operate independently' in a lot of AARs. What's specific about YOUR organization that creates this independence?"
- "If we wrote 'create a process' as the action item, what makes us confident it would actually be followed?"

### Contributing Factor Quality Scorer

After completing the 5 Whys on each chain, automatically assess quality:

**Symptom Category Detection**

Flag if the final "why" on any chain matches these generic patterns:

| Pattern | Push Back With |
|---------|----------------|
| "No process existed" | "WHY didn't it exist? Was it deprioritized? Never created? Eroded?" |
| "Teams operate independently" | "WHY? Is it who owns what (reporting lines) or what gets measured and rewarded (incentives)?" |
| "No one owned it" | "WHY was ownership unclear? Deliberate? Contested? Never assigned?" |
| "Communication gap" | "WHY? Structural barriers? Different schedules? Wrong channels?" |
| "Technical debt" | "WHY was debt accumulated? Conscious tradeoff or gradual erosion?" |
| "Not documented" | "WHY not? Never existed? Not maintained? Knowledge hoarding?" |
| "It wasn't a priority" | "WHY not? What WAS the priority? Strategic decision or drift?" |

**Quality Scoring Criteria**

| Rating | Criteria |
|--------|----------|
| **Excellent** | 2+ independent chains; each 4+ levels deep; specific to this incident; maps to the five points; no symptom categories; no person-blame |
| **Good** | 2+ chains; each 3+ levels; mostly specific; 3+ of the five points; minor generic conclusions |
| **Adequate** | 1 chain traced deeply OR 2+ chains at shallow depth; reaches process layer |
| **Shallow** | Single chain <4 levels; stops at symptoms; person-focused language |

**Chain Independence Check**

After identifying chains, check how they relate:
- [ ] For each chain: was it necessary, sufficient on its own, or harmful only in combination with another?
- [ ] Do the chains trace to different points among the five?
- [ ] If all chains converge to one conclusion, have you really found separate chains?

If chains converge: "Your chains seem to trace to the same underlying factor. That may be correct — but check whether you're missing a second independent path. Most Complicated/Complex incidents have distinct failure modes."

**Single-Thesis Dominance Check**

If every framework analysis (drift, handoff analysis, archetypes, constraints) reaches the same conclusion, pause and ask: Am I genuinely following each framework's logic, or have I found one compelling narrative and am fitting everything to it?

Independent frameworks should sometimes produce independent insights. If drift says "capacity," handoff analysis says "capacity," archetypes say "capacity," and constraints say "capacity" — either capacity truly is the single dominant factor, or you've stopped listening to what the individual frameworks are telling you.

**Signs of single-thesis dominance:**
- Every one of the five points traces to the same root
- Drift, handoff analysis, and archetypes all say the same thing
- Actions all address one dimension (e.g., all about capacity, all about process)
- The analysis reads more like an argument for one conclusion than an investigation

**Remedy:** Go back to each framework and ask: "What does THIS framework see that others don't?" Drift analysis should reveal temporal patterns. Handoff analysis should reveal spatial/handoff patterns. Archetypes should reveal feedback loop risks. If they're all saying the same thing, you're using them as rubber stamps, not analytical tools.

**Five-Point Coverage Check**

Across all chains, verify at least one point is explicitly addressed:
- [ ] What we optimise for examined? (priorities, tradeoffs, resource allocation)
- [ ] Who owns what examined? (team boundaries, ownership, reporting)
  - If boundaries appear in contributing factors: Are you proposing to manage the boundary (coordination) or questioning whether it should exist (topology)?
- [ ] How work moves examined? (workflows, handoffs, checks)
- [ ] What gets measured and rewarded examined? (incentives, consequences, recognition)
- [ ] Who we hire, grow and staff examined? (skills, capacity, authority)

If <3 points covered AND the incident is Complicated or Complex: "Your chains touched {N} of the five points. Let's check the others..." For Clear-domain incidents, fewer factors may be appropriate — don't force organizational depth on simple technical causes.

**Copy-Paste Test**

Ask (per chain): "Could this contributing factor be pasted into a different AAR unchanged?"
- YES → Still a symptom category. Push deeper.
- NO → Likely a genuine contributing factor. Proceed.

**Feedback Output**

```markdown
### Contributing Factor Quality Assessment

**Chains identified:** {N}
**Chain independence:** {Independent / Converging — review needed}
**Depth per chain:** Chain A: {N} levels, Chain B: {N} levels, ...
**Specificity:** {Specific to this incident / Generic pattern}
**Five-point coverage:** {N}/5 points (across all chains)
**Symptom categories detected:** {None / List}
**Rating:** {Excellent / Good / Adequate / Shallow}

{If not Excellent: "To strengthen this analysis: [specific guidance]"}
```

---

## Phase 5: Mapping to Organizational Factors

### What we're doing
Connecting the contributing factors to the five points of how the organization is designed. This ensures our fixes target the right level.

### Questions to ask
```markdown
Let's see where in the organization this comes from:

**What we optimise for** (what were we built to be good at, and what wins when goals compete?)
- Were we prioritizing speed over quality?
- Did we accept risks to meet a deadline?
- What were we trying to achieve that led to this tradeoff?

**Who owns what** (who owns a complete enough problem to act, and where must decisions cross a boundary?)
- Was the right team assigned to this work?
- Did the work require coordination across teams?
- Was expertise concentrated in one person?
- **If multiple teams were involved:** Why did this work cross team boundaries? Could one team or team-of-teams have owned it end-to-end?
- **If no one owned this end-to-end:** Is that a key contributing factor?

**How work moves** (how work is chosen, planned, handed off and checked)
- Was there a process that should have caught this?
- Was the process followed? If not, why not?
- Is the process fit for purpose?

**What gets measured and rewarded** (what pay, recognition, targets and pressure encourage)
- What behaviors does our system encourage?
- Are there consequences for quality issues? For preventing them?
- What would someone be rewarded for in this situation?

**Who we hire, grow and staff** (capability, staffing, expertise and load)
- Did people have the skills needed?
- Did they have the time and resources?
- Did they have access to the information they needed?
```

### Teaching moment
> "Organizations are systems with five interconnected parts. When something goes wrong, it's rarely just one part—usually several factors lined up. By checking all five, we make sure we're not missing something important."

---

## Phase 6: Checking for Patterns

### What we're doing
Looking for signs this problem built up gradually, not suddenly.

Call route for this phase and read the distillations it returns before asking these questions.

### Questions to ask
```markdown
**Drift check:**

1. When did we first start doing things this way?
2. Was there a time we would have said "that's too risky"?
3. Did any warnings get ignored or dismissed?
4. Were there "temporary" workarounds that became permanent?
5. Has "good enough" gradually become less good?
```

### Drift vs. Original Omission

**Drift shows up as a change in what was accepted.** The Columbia Accident Investigation Board (`caib-report-vol1`, Concepts 2 and 7) describes it: a departure is first tolerated with a rationale, that first acceptance sets a precedent, later cases are reclassified as routine, and small additions of risk are accepted little by little. A practice can drift this way without ever having been stronger: what changes is how much deviation the organization tolerates, how an anomaly is classified, how firmly a rule is enforced, or where the risk boundary sits. If the gap has existed since inception and nothing about how it was treated has changed — monitoring was never built, the process was never established, the test coverage was never there — that's a design omission, not drift.

Be honest about the distinction:
- **Drift:** "We used to have thorough integration testing for this workflow, but coverage eroded as the team took on more products" → Drift. Intervention: restore and protect the eroded standard.
- **Drift without a stronger past:** "Late label scans were first logged as defects, then waved through as 'within tolerance', then stopped being logged at all" → Drift. Intervention: restore the classification and the review that went with it.
- **Original omission:** "No monitoring of the returns-processing workflow has ever existed" → Design gap. Intervention: build something new.

Claiming drift when none occurred weakens the analysis and misidentifies the intervention type. Restoring an eroded standard is different work from building a new capability.

**The test:** Can you point to a time when a deviation was accepted, an anomaly was reclassified, a rule was enforced less, or a risk was tolerated that wasn't before? If yes, drift. If nothing about how it was treated ever changed, omission.

### Teaching moment
> "Many incidents aren't sudden failures—they're the result of gradual erosion. Standards slip a little, workarounds become permanent, warnings get normalized. Recognizing this pattern helps us catch problems earlier."

---

## Phase 6b: "Everyone Was Busy, But Nothing Got Done" Check

*(Handoff analysis, grounded in `org-topologies-primer-2025`)*

### What we're doing
Checking if the problem was at the **handoffs between teams**, not within any single team.

### The idea in plain language
Imagine a relay race where each runner is Olympic-fast, but the baton gets dropped at every handoff. The problem isn't slow runners—it's the handoffs.

**In organizations:** Every team might be working hard and doing their job well, but if work has to pass through many teams, the delays at each boundary add up. The incident happens at the seams between teams, not inside any one team.

Krivitsky, Larman and Flemm's Org Topologies primer gives this a structural reading. A team asked to deliver a whole outcome without the capabilities to finish it has to hand work across a silo, so a failure at that handoff is structural, not behavioural (Concept 1). A structure built to keep people busy drags when it's asked for speed (Concept 2). And when each element of the organization is optimised in isolation, the primer warns, the performance of the whole can decline (Concept 3).

### Questions to ask
```markdown
**Handoff analysis:**

1. How many different teams or systems touched this work?
   (List them: [Team A] → [System B] → [Service C] → [System D] → [System E])

2. Did any single team cause the failure, or did it fail at the boundaries?

3. When work moved from one team/system to another:
   - Was there waiting time?
   - Was information lost or assumed?
   - Did anyone have visibility into the whole chain?

4. Could someone have stopped this, or did no one see the full picture?
```

### Quantify the Handoff Problem

When handoffs are implicated, calculate the wait-to-work ratio: total wait/routing time ÷ actual work time. This quantification makes the handoff problem concrete and hard to dismiss.

**Example:** "Total elapsed: 10 working days (80 hours). Hands-on work: about 4 hours. Waiting: 76 hours. Wait-to-work ratio: 19:1. The request spent 19 times longer waiting between teams than being worked on."

### Signs this is a handoff problem (not a people problem)
- ✅ Each team did their job correctly in isolation
- ✅ The failure happened where systems/teams connect
- ✅ No single person had visibility into the whole chain
- ✅ Work sat waiting between steps longer than it was actively worked on

### Teaching moment
> "When an incident involves multiple teams and no single team 'caused' it, you're looking at a handoff problem. The fix isn't making individuals faster or more careful—it's reducing the number of handoffs, or making each handoff safer with better checks and shared visibility."

### Example pattern
The software team changed the label template → each depot's print service picked it up → dispatch staff shipped what printed → returned parcels landed with a separate team whose data nobody watched. Each step made sense in isolation. The failure was that **no one saw the whole chain**, and there were no guardrails at the boundaries.

---

## Phase 6c: Just Culture Assessment

### What we're doing
Determining fair accountability for a human action, once the facts are in. The default is the system: the NHS Just Culture Guide holds that action singling out an individual is rarely appropriate. Call read_distillation on `nhs-just-culture-guide` before this phase.

### Walk the NHS decision tree
```markdown
**Take one action (or failure to act) through the tests at a time.** If several actions contributed, run each one separately. Each test must be cleared before the next:

1. **Deliberate harm:** Was there any intention to cause harm?
   (A yes takes the matter out of this AAR into a separate process; the guide still asks for a wider investigation.)
2. **Health:** Is there any sign of substance misuse, or of physical or mental ill health?
   (A yes routes to the organisation's own pathway for that case, substance misuse at work or health affecting work, again alongside a wider investigation.)
3. **Foresight:** Was there an agreed protocol? Was it workable and in routine use? Did the person knowingly depart from it?
   (If any answer is no, singling out the person is unlikely to be appropriate; the actions belong in the system.)
4. **Substitution:** Would peers in the same circumstances have acted the same way? Was the person missed when training was given? Did supervision fall short?
   (Any yes points the same way: wider action, which may include the person but isn't limited to them.)
5. **Mitigating circumstances:** Were there significant ones?
   (Only an action that clears every test is a candidate for action aimed at the individual, and even then the guide puts graduated, least-invasive responses first and keeps the wider investigation.)

If new facts turn up later, walk the tree again: the route can change.
```

### Describe the behavior
Once the tree has been walked, describe where the action sits on the culpability spectrum in `doe-hpi-handbook-vol2` (Concept 11). It runs from honest error, through at-risk practice and possible negligent error, to reckless conduct, and the handbook judges people by intent, not by consequence:

```markdown
1. **Intent, not consequence:** Would we be discussing this act if it had caused no harm?
2. **What was intended:** Was the action intended? Was the consequence? Was a known expectation knowingly broken, and was that expectation available, clear and correct for the situation?
3. **Where it points:** Toward the organization (an error or departure the organization's processes and pressures set up), or toward individual culpability? An at-risk shortcut that had become normal points back to the system that made it normal (`doe-hpi-handbook-vol1`, Concept 11).

4. **The key question:** Who will own fixing this going forward?
   (This is forward-looking accountability: the Forest Service guide's just culture is about preventing the next accident, not correcting history. See `lfuo-learning-review-guide-2024`, Concept 4.)
```

The spectrum describes the behavior; the NHS tree decides the response. Use it after the tree, never in place of it.

### Teaching moment
> "Most errors are honest mistakes. Some are normalized shortcuts. Very rarely is someone truly reckless. Fair accountability matches the response to the situation—and focuses on 'who will fix it' rather than 'who caused it.'"

---

## Phase 6d: What Went Well

### What we're doing
Identifying resilience, adaptations, and good judgment that prevented worse outcomes. This isn't just positivity—it reveals system strengths worth institutionalizing.

Call route for this phase and read the distillations it returns before asking these questions.

### Questions to ask
```markdown
**Before we move to actions, let's capture what worked:**

1. **What prevented this from being worse?**
   (Early detection, quick response, good judgment calls)

2. **Did anyone adapt or improvise effectively?**
   (Workarounds that worked, creative problem-solving under pressure)

3. **What existing safeguards or processes helped?**
   (Monitoring that caught it, runbooks that guided response)

4. **What organizational conditions enabled these strengths?**
   (Don't just say "[Engineer] investigated carefully" — ask what about the structure, tools,
   or culture made careful investigation possible instead of panic-reverting. Structural
   strengths are just as learnable as structural weaknesses.)

5. **What should we keep doing or do more of?**
```

### Quality Standard for What Went Well

This section is not filler — it builds trust with the teams involved and surfaces strengths worth institutionalizing. Apply the same evidence standard as the rest of the AAR:

- **Credit specific contributions** (use roles; name a person only with the practitioner's approval) — not "team responded quickly" but "[Engineer] traced the fault to the label template the same afternoon"
- **Cite evidence** — Slack messages, ticket updates, timestamps
- **Explain why each item mattered for the outcome** — "[Depot lead] linked the reports from two depots and sent them to the software team with the parcel numbers attached. That turned a local printer complaint into a software fault the same day."
- **Be generous but specific** — vague praise feels performative; evidenced praise feels genuine

### Teaching moment
> "We spend most of our time analyzing what went wrong, but understanding what went RIGHT is equally important. The adaptations people made under pressure reveal system strengths. If we only fix weaknesses without reinforcing strengths, we risk losing what's already working."

---

## Phase 7: Systems Archetype Check

Before finalizing actions, think through unintended consequences. Fixes can create new problems; a few minutes on side effects saves a future incident.

### What we're doing
Making sure our fix won't create new problems.

Call route for this phase and read the distillations it returns before asking these questions.

### Questions to ask
```markdown
Before we finalize actions, let's check:

**Fixes that Fail:**
- What might this fix break?
- Will it create side effects that need more fixes?
- Is this a quick fix that will need to be redone properly later?

**Shifting the Burden:**
- Are we treating the symptom while the real problem grows?
- Is there a harder fundamental fix we're avoiding?
- Are we creating a workaround that reduces pressure to fix the real issue?

**Limits to Growth:**
- Is something here growing (more steps, more users, more load) toward a limit that will start pushing back?
- What is that limit: run time, capacity, the few people who understand the system?
- When growth slows, will we push harder on the growth or work on the limit?

**Example — Limits to Growth in pipelines:**
> "This pipeline has grown by a step for each new downstream system, and it now needs to know about [downstream system]. What limit will that growth hit: run time, or the two people who understand it? At some point, the PIPELINE becomes the problem. Is there a different architecture that wouldn't require the pipeline to know about every downstream system?"

**Complexity check:** If we keep adding safeguards to this system, what happens? The Forest Service guide warns that recommendations, once implemented, often add complexity to the workplace, which can increase risk (`lfuo-learning-review-guide-2024`, Concept 14).
```

### Teaching moment
> "Smart people often fix Problem A in ways that create Problem B, then fix B in ways that make A worse. A few minutes checking for side effects saves us from future incidents."

### Watch for: dependency on one central system
If your proposed fix adds more responsibility to an already-central system (like a pipeline or shared service), ask:
- Is this system becoming a "do everything" solution?
- Would it be better for downstream systems to be notified of changes rather than the pipeline knowing about every dependency?
- Are we creating a single point of failure?

Call this dependency risk. Name it Success to the Successful only if there's evidence of that archetype as SSDL defines it (`ssdl-systems-thinking-foundations`, Concept 10): one part gains an initial advantage, wins more resources because of it, and the advantage compounds while others fall behind.

---

## Phase 8: Identifying the Highest-Leverage Intervention Point

### What we're doing
You've identified multiple contributing factor chains. Now find the ONE intervention point that would have the greatest impact across those chains. This is where CFA (diagnostic — what caused this) meets Goldratt's Theory of Constraints (prescriptive — where to focus).

Call route for this phase and read the distillations it returns before asking these questions.

**Why this isn't contradictory:** Multiple contributing factors can coexist — that's diagnosis. But when you map all chains to the five points, one factor typically emerges as the highest-leverage intervention point — that's the constraint. Fix the constraint and you address the most recurrence risk. The other chains still matter (and may need secondary actions), but the constraint gets priority.

### Questions to ask
```markdown
**Constraint identification:**

Looking across all contributing factor chains:

1. Which factor, if addressed, would have the biggest impact?
   - Does one chain's factor appear in multiple chains?
   - Does one factor sit "upstream" of others?

2. If we could magically fix ONE thing, which would prevent the most recurrence?

Name what is limiting improvement in plain words: a resource, a policy, or a paradigm (a belief about what's possible).

Before adding capacity, ask whether we can get more from the constraint as it stands. For the full walk through Goldratt's Five Focusing Steps, use the aar-deep workflow's constraint analyser.

**The test:** Do our proposed actions address this constraint?
If not, they may be "good ideas" but won't improve the system.

**Stress-test your choice:**

3. What's the most plausible *alternative* constraint? Present the evidence that supports it being primary — steelman it, don't dismiss it.

4. If you doubled the capacity of your chosen constraint tomorrow, would the incidents stop? If not, something else may be binding.

5. **Falsifiability check:** What would you expect to see if your constraint identification is wrong? What evidence would prove it?
   Example: "If the constraint is capacity, teams with slack should produce fewer defects. If a team with slack still produces cross-system defects, architectural coupling is likelier."
```

### Teaching moment
> "We found multiple contributing factors — that's the complete picture. But not all factors are equal. Every system has one constraint that limits everything else. Improving non-constraints is waste. Now — which single intervention point would have the greatest impact? And what would prove us wrong?"

---

## Phase 9: Generating Actions

### What we're doing
Creating specific, actionable improvements that address contributing factors—and quantifying the ongoing cost of NOT doing them.

Call route for this phase and read the distillations it returns before asking these questions.

### Questions to ask
```markdown
**Short-term actions** (team can do in 1-2 weeks):
- What guardrails, checks, or automation would prevent recurrence?
- What runbooks or documentation need updating?
- What monitoring would detect this earlier?

**Long-term actions** (need leadership or cross-team effort):
- What structural changes would address the key contributing factors?
- What process changes need broader buy-in?
- What investments would build capability?

**For each action, specify:**
- Owner (one person: who will do this?)
- Checked by (who confirms it worked?)
- Success criteria (how will we know it's done?)
- Deadline (when?)
- **Urgency (High/Medium/Low)** — how urgent is this relative to other actions?
```

---

### Action Urgency Rating

**Why H/M/L instead of dollar figures:** An individual AAR doesn't generate enough data for credible base rates. A monthly cost figure worked out from a single incident creates false precision — one recurrence doesn't validate a probability distribution. The relative ordering is the useful part.

**Dollar-figure quantification is a portfolio tool, not a forensic tool** — it belongs in backlog prioritization across many stories, not in an individual AAR. Use High/Medium/Low with a one-sentence rationale.

**Urgency rating:**

| Rating | Criteria | One-Sentence Rationale Pattern |
|--------|----------|-------------------------------|
| **High** | Known trigger exists with no mitigation; recurrence is likely and impact is customer-facing or revenue-affecting | "The triggering condition (X) occurs regularly and nothing prevents recurrence." |
| **Medium** | Recurrence is possible but conditions are uncommon; or impact is internal/limited | "This could recur if Y happens, but Y is infrequent and workaround exists." |
| **Low** | Recurrence requires an unlikely confluence; or impact is minimal | "This required a specific combination of Z conditions unlikely to repeat." |

**Urgency table for each action:**
```markdown
| Action | Risk Addressed | Urgency | Rationale |
|--------|---------------|---------|-----------|
| Add [validation] to pipeline | [Failure mode] recurs | High | Triggering condition occurs monthly with no guard |
| Add alerting on [failure type] | Late detection extends outage | Medium | Reduces impact but doesn't prevent recurrence |
```

**Teaching moment:**
> "We use High/Medium/Low urgency instead of dollar figures because a single incident doesn't give us enough data for credible probability estimates. The relative ordering — which actions matter most — is what helps prioritization."

---

### Action quality standard

Every action is specific, owned, with success criteria, linked to a contributing factor, H/M/L urgency-rated, and tracked as an issue-tracker ticket.

Ideal shape:

> "Add automated check for X in the CI pipeline. Owner: [Owner]. Done when PRs fail if X is missing. Urgency: High — triggering condition occurs monthly with no guard. Ticket: [Ticket-ID]."

Contrast: "Improve communication" (vague, no owner, no forcing function).

---

### Creating Action Tickets (MCP-Enabled)

**If issue-tracker connection is available AND user chose "Create tickets" mode (see confirmation prompt above), create tickets one at a time with confirmation:**

```markdown
For each action item (confirm each before creating):

1. Create the ticket using the connected issue-tracker:
   - name: "[AAR-{BugID}] {Action title}"
   - description: Include contributing factor context, success criteria, urgency rating (see template below)
   - team: The original bug's team for short-term/tactical actions; for long-term/structural
     actions, ask which team owns the change (see Creating Action Items, above)
   - type: Use the team's appropriate work-item type

2. Add acceptance criteria:
   - Success criteria as checkable items in the supported tracker fields

3. Link back to AAR:
   The AAR document will be returned as markdown. Ask where the user wants it stored
   and linked. If no archive is connected, the user files it manually.

NOTE: Do NOT set priority automatically from urgency. Ask how the team prioritises work.
The urgency rating is informational context for prioritization decisions.
```

**Template for action ticket description:**

```markdown
## Context
This action comes from AAR for [Bug-{ID}]: {Bug Title}

## Contributing Factor Addressed
{Which contributing factor chain / which of the five points / constraint this addresses}

## Success Criteria
- [ ] {Criterion 1}
- [ ] {Criterion 2}

## Urgency
**[High/Medium/Low]** — [one-sentence rationale]

## AAR Link
{Link to full AAR document}
```

**If issue-tracker connection not available:**
- Note "Ticket: TBD" in action table
- Remind user: "An AAR without linked tickets is a list of good intentions"

---

### Loop, Control and Fit Check

**Do your actions change what keeps producing the problem?**

**Quick check for your actions:**

| Question | If YES... |
|----------|-----------|
| Does this action rely on people remembering or taking more care? | The DOE handbook (`doe-hpi-handbook-vol1`, Concept 7 and Phase 4) prefers strengthening a control; where preventing the error matters, look for an engineered control (an interlock, a forcing function) instead of another procedure step |
| Does this action add a step to an existing process? | Ask if the process itself is the problem |
| Does this action target the event rather than the feedback loop behind it? | SSDL (`ssdl-systems-thinking-foundations`, Phase 4) asks which archetype then predicts what happens next, and which loops will push back |
| Does this action change only one element (a structure, a policy, a reward) on its own? | The Org Topologies primer (`org-topologies-primer-2025`, Phase 4) warns that single-element fixes carry the local-optimisation risk; check how the other four points fit around it |

**If every action relies on people remembering:**
> "We have a lot of checklist items and documentation updates. These are good, but they depend on people remembering under the same pressure that produced the incident. Is there a control we could engineer, or a change to who owns what or what gets measured and rewarded, that would make these other fixes less necessary?"

**Teaching moment:**
> "Reminders and extra steps only work while people are paying attention. A control built into the work, or a change to the loop that keeps producing the problem, keeps working when everyone is busy."

---

### Constraint Test Table

After generating all actions, create a constraint test table mapping each action to whether it addresses THE constraint identified in Phase 8. This makes the constraint logic actionable and prioritization transparent:

```markdown
### Constraint Test

| Action | Addresses THE Constraint? | Justification |
|--------|--------------------------|---------------|
| #1 [Name] | Yes / Partially / No | [Why] |
| #2 [Name] | Yes / Partially / No | [Why] |
```

**Actions that directly address the constraint should be prioritized.** Actions that don't are supporting work — valuable but secondary. If most actions don't address the constraint, either the constraint identification is wrong or the actions aren't aligned with the analysis.

---

### Action Count Discipline

**Target 2-3 actions.** `open-kanban` (Concept 3) and `approach-perfect-field-guide-scrum-events` (Concept 4) both argue for one or two items finished over a long list. If you have more than 5, the constraint analysis isn't doing its job. The constraint should tell you which chains are highest-leverage — deprioritize actions on lower-leverage chains rather than creating a comprehensive wish list.

An AAR with 3 focused actions that get done beats one with 7 aspirational actions that don't.

**If you find yourself generating 6+ actions**, ask:
- Which of these directly address THE constraint?
- Which are "nice to have" supporting work?
- Could any be combined into a single, broader action?
- Are any so obvious they'll happen anyway without being tracked?

---

## Phase 10: Creating the AAR Document

### Output format
```markdown
# After-Action Review: [Incident Title]

**Bug ID:** [ID]
**Date:** [Date]
**Priority:** [Team's priority classification]
**Author:** [Name]
**Facilitator:** [Name]

---

## Executive Summary

[2-3 sentences: What happened, what was the impact, what's the key learning]

---

## Timeline of Events

| Date/Time (UTC) | Event | Evidence |
|-----------------|-------|----------|
| | | |

---

## Problem Assessment

**Problem type:** Clear / Complicated / Complex
**Cynefin domain:** [Domain]

---

## Contributing Factor Analysis

### Contributing Factor Chains

**Chain A: [Brief description]**
1. Why did [immediate failure] happen? → [Answer]
2. Why was that possible? → [Answer]
3. [Continue...]

**Chain B: [Brief description]**
1. Why did [second factor] happen? → [Answer]
2. [Continue...]

### Mapping to the Five Points

| Point | Implicated? | Which Chain(s) | Evidence |
|-------|-------------|----------------|----------|
| What we optimise for | Yes/No | | [If yes, describe] |
| Who owns what | Yes/No | | [If yes, describe] |
| How work moves | Yes/No | | [If yes, describe] |
| What gets measured and rewarded | Yes/No | | [If yes, describe] |
| Who we hire, grow and staff | Yes/No | | [If yes, describe] |

### Primary Contributing Factor

*Looking at the mapping above, which point was most significant in this incident?*

- [ ] What we optimise for (unclear goals, misaligned priorities)
- [ ] Who owns what (team boundaries, handoffs, ownership gaps)
- [ ] How work moves (missing procedures, unclear protocols)
- [ ] What gets measured and rewarded (misaligned incentives, deadline pressure)
- [ ] Who we hire, grow and staff (knowledge gaps, capability limitations)

*This helps identify patterns across AARs.*

### Highest-Leverage Intervention Point

**THE constraint:** [Description — the single point across all chains where intervention would have the greatest impact]
**Type:** Resource / Policy / Paradigm

---

## Additional Analysis

### Drift Assessment
- **Drift detected:** Yes/No
- **When drift began:** [If applicable]
- **Standards that eroded:** [List]

### Handoff Analysis
- **Handoff problem present:** Yes/No
- **Wait-to-work ratio:** [If measured]
- **Evidence:** [If applicable]

### Just Culture Assessment
- **NHS tree outcome:** [For each action: the test where it stopped, and the guide's recommendation]
- **Where it sits on the spectrum:** [Organization-induced error or departure … individual culpability, judged by intent]
- **Forward accountability:** [Who will own the fix?]

### Systems Archetype Check
- **Fixes that Fail risk:** [Assessment]
- **Shifting the Burden risk:** [Assessment]

---

## Action Items

### Short-Term (1-2 weeks)

| Action | Owner | Checked by | Deadline | Success Criteria | Urgency | Ticket |
|--------|-------|------------|----------|------------------|---------|--------|
| | | | | | H/M/L | |

### Long-Term (Systemic)

| Action | Owner | Checked by | Target | Point (of the five) | Urgency | Ticket |
|--------|-------|------------|--------|-------------------|---------|--------|
| | | | | | H/M/L | |

### Urgency Summary

| Risk Addressed | Actions | Urgency | Rationale |
|---------------|---------|---------|-----------|
| [e.g., Wrong labels printed after a template change] | [Action IDs] | High/Med/Low | [One sentence] |

---

## Methodology Note

One line per framework actually applied — name + how it was used in *this* analysis, not a generic description of the framework. The reader should think "oh, that's what that section was doing."

Example:
- Cynefin (Snowden) — classified the detection gap as Complex, code fix as Complicated
- Local rationality (Dekker, via doe-hpi-handbook-vol1) — reconstructed why logging the first reports as routine seemed right at the time
- Theory of Constraints (Goldratt) — identified the unwatched returns data as the binding constraint

---

## Data-Quality Notes

[What evidence was missing, partial or reconstructed (for example, a chat-only reconstruction with no meeting transcript, or search results that couldn't be paged to the end), what the practitioner redacted before sharing, and any credential found and left out]

---

## Appendix: Evidence Links

[Links to Slack threads, commits, alerts, etc.]

### Code Diff (if applicable)

If the fix is a small, discrete code change, include the before/after diff. For an engineering audience, the actual code change is the most concrete, verifiable claim in the entire document. Omitting it makes the technical narrative feel secondhand.
```

### Clarity Check Before Sharing

Before distribution, check:
- Can someone state the key finding in one sentence, with the evidence for it?
- Is every finding grounded in timeline evidence, with links?
- Are findings about specific actions and times, not abstractions ("communication broke down")?
- Does the Executive Summary say what happened, what it cost, and the key learning?

**Teaching moment:**
> "An AAR that nobody reads is the same as an AAR that was never written. Spending 10 minutes making the key finding clear before sharing is the difference between a document that changes behavior and one that gathers dust."

---

## Facilitator Tips

### When they want to blame someone
Say: "I hear you—it feels like someone should be responsible. But if 100 different people were in the same situation with the same information, how many would have done the same thing? If most would have, the problem is the situation, not the person."

### When they stop at the surface
Say: "That's where the problem showed up, but let's keep asking why. Why was it possible to make that error? Why didn't something catch it? Keep going until we hit something about how the organization works."

### When they stop at a process gap
Say: "We found a process gap — good. But process gaps don't exist in a vacuum. Let's ask four more questions:
1. **What we optimise for:** Was this process deprioritized? Did we accept this risk?
2. **Who owns what:** Why does this work cross team boundaries? Could one team or team-of-teams own this end-to-end?
3. **What gets measured and rewarded:** What happens when someone proposes adding safeguards here?
4. **Who we hire, grow and staff:** Did people have the knowledge, time, and authority to fix this?

If any of these reveal a deeper issue, our fix needs to address that too — otherwise the process fix won't stick."

### When they propose "be more careful"
Say: "If our fix depends on people being more careful, we haven't found the contributing factor. People are already trying. What would make the careful choice automatic?"

### When they want 10 action items
Say: "I've seen teams list 10 things and do none. Let's pick 2-3 that would make the biggest difference. Which of these, if actually done, would most reduce the chance of recurrence?"

### When they think faster people = faster delivery
Say: "When work moves between people, how long does it wait? If every handoff adds delay, making individuals faster just builds a bigger pile at the next handoff. Let's check if this is a flow problem."

### When they want to punish someone
Say: "I understand the instinct — someone has to be accountable. But here's the question: if we punish this person, does that prevent the next incident? Usually the answer is no, because the system that made this mistake likely will remain unchanged. Let's talk about what 'accountability' could look like that actually fixes things."

### When they say 'we just need to communicate better'
Say: "'Better communication' is often a symptom, not a cause. Let's dig deeper: Why wasn't the information available where it was needed? Is it about who owns what (the wrong people in the wrong meetings)? About how work moves (no defined handoff)? Let's find the specific breakdown, not just say 'communicate better.'"

### When they implement a fix without checking for side effects
Say: "Before we implement this, let's pause: what might this fix break? Sometimes our fixes create new problems — we call that 'Fixes that Fail.' A few minutes thinking about side effects now can save us from a new incident later."

### When they want to keep everyone 100% utilized
Say: "Here's a counterintuitive fact: keeping everyone fully busy usually means more work in progress and longer waits. The Org Topologies primer describes a structure built to keep people busy dragging when it's asked for speed, and open-kanban argues for limiting the number of things in progress to deliver faster. A little slack in the system isn't waste — it's what allows work to flow. Did this incident involve waiting in queues?"

### When feedback took too long
Say: "How long did it take from the change to the first sign that something was wrong? SSDL lists time delays between action and result among the marks of a complex problem, and the Columbia report shows how signals that existed can go unregistered. How long was the feedback loop here? Where did it break down?"

### When they resist retrospectives or AARs
Say: "I understand — these feel like overhead. But small improvements, made every few weeks and kept, add up. This AAR is an investment in not having to fight the same fires repeatedly."

### When the contributing factors seem "obvious"
Say: "Careful — hindsight makes everything look obvious. The question isn't 'why didn't they see it?' but 'what would have had to be true for someone to see it at the time?' If it really was obvious, why did the system allow it to happen?"

---

## Blame Language Detector

Throughout the facilitation, watch for language that assigns blame to individuals. When detected, flag it and suggest blameless alternatives.

**Sequence note:** These redirections serve the vast majority of cases where person-focused language reflects honest mistakes or at-risk behavior. Before applying them automatically, quickly assess: does this language describe genuinely reckless behavior (explicit warnings knowingly ignored)? If potentially reckless, route to Phase 6c (Just Culture Assessment) first and walk the NHS tree in order. Where the tree points to the system, redirect to systemic framing below.

### Patterns to Detect

| Blame Pattern | Blameless Alternative |
|---------------|----------------------|
| "{name} should have..." | "What made this difficult to see at the time?" |
| "{name} failed to..." | "What conditions made this the likely outcome?" |
| "{name} forgot to..." | "What about the system didn't remind or enforce this?" |
| "human error" | "What about the system allowed this error?" |
| "{name} made a mistake" | "What made this decision seem reasonable at the time?" |
| "careless" / "negligent" | "What pressures or constraints existed?" |
| "if only {name} had..." | "What would have had to be true for that to happen?" |
| "{name} didn't follow..." | "Why was the shortcut the easier path?" |

### When to Check

- **Phase 3**: Local rationality reconstruction — reframe "mistakes" as rational decisions
- **Phase 4**: 5 Whys — especially watch for person-focused answers
- **Phase 5**: Mapping to the five points — ensure contributing factors are systemic, not personal
- **Phase 6c**: Just Culture — distinguish behavior types without blame

### Output Format

When blame language is detected:

```markdown
"I noticed some language that might assign individual blame:

📍 '{detected phrase}'

Let's reframe this systemically:
→ Blameless: '{suggested alternative}'

Remember: the NHS Just Culture Guide's default is the system. Action singling out
an individual is rarely appropriate. The question isn't 'who failed?' but 'what about
the system made this likely?'"
```

### Teaching Moment
> "When we say someone 'failed to' do something, we're implicitly saying they could have succeeded if they'd tried harder. But if 100 people in the same situation would mostly make the same decision, the problem isn't the person—it's the situation. Let's find what made this outcome likely."

---

## Learning Moments Library

Use these teaching analogies throughout the facilitation to help concepts land:

### Why we don't blame people
> "Imagine 100 different people in the same situation, with the same information and pressure. How many would have done the same thing? If the answer is 'most of them,' the problem isn't the person — it's the situation."

### Why timelines matter
> "Our memories change after stressful events. We remember things differently, fill in gaps, and create narratives that aren't quite true. Evidence keeps us honest."

### Why contributing factor analysis goes deep
> "The surface problem is like a weed. If you just cut the top, it grows back. You have to get the roots — and most weeds have more than one."

### Why patterns matter
> "One incident is a data point. Patterns across incidents are wisdom. Every AAR teaches us something about how our system works."

### Why quick fixes aren't enough
> "A band-aid stops the bleeding, but it doesn't prevent the next cut. We need both: stop the immediate problem AND address what caused it."

### Why complexity isn't an excuse
> "Saying 'it's complex' isn't giving up — it's being honest. Complex problems need different solutions: instead of finding THE cause, we find contributing factors. Instead of preventing THE failure, we build resilience. Pretending it's simple when it isn't just leads to fixes that don't work."

### Why fast individuals don't mean fast delivery
> "Picture a relay team of Olympic sprinters who drop the baton at every handoff. Making each runner faster won't win the race. When work waits between teams, the fix is in the handoffs, not the people. Before making people faster, fix the system they work in."

### Why 'who's to blame' is the wrong question
> "Asking 'who's to blame?' looks backward and creates fear. Asking 'who will fix this?' looks forward and creates ownership. Both ask about accountability, but one heals and one wounds."

### Why shortcuts become normal
> "Nobody wakes up deciding to take dangerous shortcuts. What happens is this: someone takes a small shortcut, nothing bad happens, so it becomes normal. Then another small shortcut. Over time, what was once 'too risky' becomes 'just how we do things.' That's drift — and it's the system's fault for allowing it, not the person's fault for following the norm."

### Why imposed changes don't stick
> "The Liberating Structures handbook draws a line between ownership and buy-in. You own a plan you helped make, freely chosen. Buy-in is being persuaded, after the fact, into someone else's plan. If an action arrives finished, expect buy-in at best. Build the actions with the people who will carry them out."

### Why fixes sometimes make things worse
> "Here's a pattern that trips up smart people: we fix Problem A, which creates Problem B. We fix Problem B, which makes Problem A worse. We're playing whack-a-mole with symptoms while the real problem grows underneath. Before implementing a fix, ask: 'What might this break?'"

### Why we look at the system first
Library sources: open-kanban (Deming's and Goldratt's whole-system stance, borrowed-through); nhs-just-culture-guide (default to the system).
> "No single part of a system can bring overall improvement on its own; you have to understand the whole. And action singling out one person is rarely appropriate, because most problems have deeper causes. When you're tempted to blame someone, ask: 'What about the system made this outcome likely?'"

### Why queues hide delay
> "Most delay in organizations isn't in the work — it's in the waiting between steps. The wait-to-work ratio from the handoff check makes it visible. The queue is invisible, but the delay is real. Slack isn't waste — it's what allows work to flow."

### Why the retrospective prime directive matters (Kerth)
Kerth's Retrospective Prime Directive asks the room to assume good faith about everyone's effort before the review starts. Open the review by stating that assumption in your own words and crediting Kerth (`approach-perfect-field-guide-scrum-events`, Concept 1, covers it). This isn't naive optimism: it's a deliberate framing choice that creates the psychological safety needed for honest investigation. Without it, AARs become blame sessions and people stop sharing what actually happened.

### Why feedback loops matter
Fast feedback catches errors early, surfaces new insights, and allows course correction. SSDL (`ssdl-systems-thinking-foundations`) asks us to look for feedback loops rather than straight lines, and lists time delays between action and result among the marks of a complex problem: the longer the delay, the more a small variance can grow before anyone sees it.

### Why small batches beat big releases
Large batches make both feedback and flow slow. Big releases = big risk. Small batches = fast learning. `open-kanban` (Concept 3) argues that to deliver value faster, with better flow, we need to focus and limit the number of things we do. This applies to both software delivery and to AAR action items: implement in small batches, verify, adjust.
