---
name: aar-actions
description: Generate action items with urgency rating and constraint evaluation
---

# AAR Action Generator

Generate specific, actionable improvements with relative urgency ratings.

## Connection availability

Before using tracker or chat tools, verify that the relevant connection is available. If it is missing or fails, stop that operation, report the missing data, and offer paste mode: the practitioner pastes ticket details, chat excerpts or action-status data. Do not infer data or claim tickets were created. For action creation without a tracker, return the ticket drafts as markdown for manual entry.

## Instructions

1. **Read the component spec**: `action-generator.md` (in this skill's folder)
2. **Address contributing factors**: Actions must target the contributing factors identified, across the five points: what we optimise for, who owns what, how work moves, what gets measured and rewarded, and who we hire, grow and staff. These five points follow Jay Galbraith's Star Model (strategy, structure, processes, rewards, people), put in plain words.
3. **Identify THE constraint** (Goldratt): every system has one — actions that don't address it are deprioritized
4. **Rate urgency** (High/Medium/Low) with a one-sentence rationale per action
5. **Create tickets**: With the practitioner's approval of each one, use the connected tracker to create tickets
6. **Check for side effects**: Will this fix create new problems?

## Urgency Rating

An individual AAR doesn't generate enough data for credible base rates — probability estimates from a sample of one are fabrications. Use relative ordering instead.

**Urgency factors:**
- Recurrence risk — known trigger exists, no mitigation
- Impact severity — customer-facing, revenue impact, data loss
- Detection time — no monitoring, silent failures
- Recovery time — manual steps, no runbook, expertise required

**Categories:**
- **Do Now** — High urgency, short duration → implement immediately
- **Schedule** — High urgency, long duration → start soon, track progress
- **Batch** — Low urgency, short duration → group with similar work
- **Deprioritize** — Low urgency, long duration → defer or reconsider

## Action Quality

Actions should NOT be:
- "Be more careful" (not a forcing function)
- "Improve communication" (too vague)
- "Add training" without system change (won't stick)

Actions SHOULD be:
- Specific and actionable
- Have a clear owner
- Include success criteria
- Carry an urgency rating with rationale
- Have linked tracker tickets

## Ticket Creation

For each action:
```
Use the connected issue-tracker to create the ticket:
  name: "[AAR-{BugID}] {Action title}"
  team: Same as original bug for a tactical action; for a structural action, ask which team owns the change
  type: The team's appropriate work-item type
```

---

## Action Status Tracking

When checking on existing actions (rather than generating new ones):

1. **Get the original bug** by ID via issue-tracker connection
2. **Find action tickets** by searching for `[AAR-{bug_id}]` in ticket titles
3. **Assess health** based on status and age

### Health Scoring

| Status | Age | Health |
|--------|-----|--------|
| Done | Any | Healthy |
| In Progress | <30 days | On track |
| In Progress | 30-60 days | Aging |
| In Progress | >60 days | Overdue |
| Backlogged | <14 days | Recently created |
| Backlogged | 14-30 days | Needs attention |
| Backlogged | >30 days | Stale |

## Start

- To **generate new actions**: Ask what contributing factors to generate actions for, or continue from CFA
- To **check status**: Provide a bug ID to look up existing AAR action tickets
