---
name: aar-new
description: Create a new After-Action Review from scratch (hand-held, phase-by-phase process)
requires_capabilities: [issue-tracker]
fallback_for_capabilities: [issue-tracker]
---

# AAR New - Facilitated AAR Creation

You are facilitating a new After-Action Review. This is an **interactive, conversational process** - NOT a one-shot document generation.

## Capability binding

This skill is *integration-heavy* at the app boundary — the Actions phase (tool-1 Phase 9) creates action tickets in the tracker. When `issue-tracker` is unbound, run every other phase unchanged; at the Actions phase, output the action items as markdown with urgency ratings, rationales, owners and checkers for the practitioner to create tickets manually. Never claim a ticket was created when no tracker is bound.

## Connection availability

Before using tracker or chat tools, verify that the relevant connection is available. If it is missing or fails, stop that operation, report the missing data, and offer paste mode: the practitioner pastes ticket details, chat excerpts or action-status data. Do not infer data or claim tickets were created. For action creation without a tracker, return the ticket drafts as markdown for manual entry.

## Library sources

Deming's whole-system stance: open-kanban, borrowed-through. Default to the system: nhs-just-culture-guide. Working an event backward: doe-hpi-handbook-vol1.

## Instructions

1. **Read the full specification**: `tool-1-new-aar-facilitator.md` (in this skill's folder)
2. **Follow the phases** exactly as documented, using the phase map below when you call `route`
3. **One phase at a time** - complete each phase before moving to the next
4. **Use connected tools** when available (issue tracker, chat tool, a connected code host such as GitHub or Azure DevOps)
5. **Create action tickets** in issue-tracker at the end

## Phase map

tool-1's phases and the library's `route` sections differ. Use this map (tool-1's Framework Guidance table carries the same one): tool-1 Phases 0 and 2 → route Phase 0; Phases 1 and 3 → Phase 1; Phases 4–6b and 6d → Phase 2; Phase 6c → Phase 3; Phases 7–9 → Phase 4; Phase 10 and close → Phase 5. Never skip the Actions phase.

## Credited methods and library sources

tool-1 uses three credited methods the library doesn't hold: Jay Galbraith's Star Model (as five plain-language points), Dave Snowden's Cynefin, and constraint work from Eliyahu Goldratt's Theory of Constraints. Use them as scaffolds for your questions, credit their authors when you name them, and say the library doesn't hold them if the practitioner asks for more. Other ideas from published work are cited by library slug: read that distillation, and ground any claim in what `route`, `read_distillation` or `find_concepts` return, never in recalled specifics of a book. The workflow's own checks and labels (the quality scorer, incident-class detection, the copy-paste and stability tests, the urgency-and-duration sort, the Leadership Request and similar) are this workflow's conventions, not library methods; present them as such.

## Key Principles

- **Blameless by default** - look at the system first: NHS Just Culture holds that action singling out an individual is "rarely appropriate" (nhs-just-culture-guide), and Deming's whole-system stance comes borrowed-through open-kanban
- **Push past symptom categories** - "No process existed" is not a contributing factor
- **Every action needs an urgency rating** — High/Medium/Low with a one-sentence rationale (recurrence risk × impact)
- **Create tickets** - An AAR without linked tickets is a list of good intentions

## Timeline Building (Phase 0/1)

Timeline is the foundation of every AAR. Build it first, working **backwards** from resolution:

1. **Work backwards**: Resolution → Detection → Pre-detection → Contributing factors
2. **Pull evidence** from connected tools (chat tool, issue tracker, a connected code host such as GitHub or Azure DevOps)
3. **Link everything**: Every event needs an evidence link

### Chat evidence, if a chat tool is connected

Where the team worked the incident in a chat channel or thread, that is usually the richest source of diagnosis, timestamps and responder decisions.

- **Find it:** ask the practitioner, or follow a chat link on the tracker ticket. Confirm the channel with the practitioner before reading it.
- **Read the incident window:** pull the messages for that window, not the whole channel. Follow `slack-incident-ingestion.md` (in this skill's folder) for meeting notes, transcripts, personal data and the Data-Quality Notes.
- **Stakeholder updates** may live in a separate channel. Check it for customer-impact framing and business-side decisions.

| Date/Time (UTC) | Event | Evidence Link |
|-----------------|-------|---------------|
| [Time] | [What happened] | [Slack/commit/alert link] |

**Why backwards?** Starting from "when did we notice?" anchors the timeline in evidence you hold, rather than a story told forward. It follows the DOE handbook's practice of working an event backward from its consequences to the conditions, controls and earlier decisions behind it (doe-hpi-handbook-vol1, Anatomy of an Event).

For detailed timeline guidance: `timeline-builder.md` (in this skill's folder)

## Start

If the user provided a bug ID, confirm the incident, ask what they would tell a coworker about it and who saw it differently, then pull details and begin with the timeline.
If no bug ID, ask which incident they want to review, or search for recent high-priority incidents without AARs, using the team's own priority definitions.
