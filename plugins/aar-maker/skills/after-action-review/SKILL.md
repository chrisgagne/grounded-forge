---
name: after-action-review
description: Use when someone wants to run, plan or write an after-action review (AAR), postmortem, post-incident or incident review, debrief or lessons-learned session, or asks how to look back at something that went wrong (an outage, a failed launch, a missed target, a clinical or safety event) without blaming people. Also use before drafting a postmortem or incident report document, and when a team is blaming one person for a failure.
---

# After-action review with AAR Maker

AAR Maker serves a blameless review method and an open library of 22 cited sources (US Army TC 25-20, the US Forest Service Learning Review Guide, the NHS Just Culture Guide and others) through its MCP server, `aar-maker`.

1. Call `start_after_action_review_or_postmortem` before asking the person anything or answering from general knowledge. It returns the facilitation guide: the discipline (blameless by default, local rationality, contributing factors rather than one root cause), the first questions to ask and how to cite the library.
2. Follow the guide. It names further tools (`route`, `read_distillation`, `find_concepts`, `list_sources`, `get_workflow`) for each phase of the review.
3. Cite only what a tool returned. Where the library doesn't cover something, say so.

If the `aar-maker` tools aren't available, the server isn't signed in yet. Tell the person to sign in with GitHub when Claude asks, or to open the connector's settings and connect it, then call the tool once it's there.

What the person tells you about their incident stays in this conversation. Only tool arguments (workflow and section names, source ids, search words) reach the server, so keep names and incident details out of searches.
