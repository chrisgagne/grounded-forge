# AAR Maker

Run blameless after-action reviews, postmortems and incident reviews in Claude, from an open library of 22 cited sources.

![AAR Maker](icon.svg)

AAR Maker takes you through a review one phase at a time: the timeline, why decisions made sense at the time, contributing factors, and actions with owners. Its method draws on US Army TC 25-20, the US Forest Service Learning Review Guide, the NHS Just Culture Guide, the DOE human performance handbooks, the Columbia accident report and others. Every claim cites the source it came from.

## What's in the plugin

- **A skill, `after-action-review`.** It tells Claude to use AAR Maker when you ask for an after-action review, postmortem, incident review, debrief or lessons-learned session, or when a team is blaming one person for a failure.
- **One remote MCP server, `aar-maker`,** at `https://aar.groundedforge.com/mcp`. It's the same server as the AAR Maker connector in the Claude directory, so if you have both you see one set of tools. Its tools are read-only: they return the facilitation guide, workflows and library passages.

The plugin runs no local code, hooks or scripts.

## Signing in

The server asks you to sign in with GitHub the first time it's used. Signing in shares your public GitHub username, nothing else: no email, no repositories.

## What's sent and logged

The server receives only what its tools are called with: workflow and section names, source ids and search words. Your incident details reach it only if Claude puts some in a search. It logs your GitHub username, the tool called and the library file it read, never the words of a search. Cloudflare keeps the logs for a few days. Nothing is sent anywhere else. Privacy details: https://aar.groundedforge.com/privacy

## Try it

- "Help me run an after-action review of last week's failed release."
- "Write a blameless postmortem for this morning's outage."
- "My team is blaming one person for a missed deadline. Help me run the debrief."

## Terms

The plugin's files are MIT licensed (`LICENSE`). The library the server returns keeps each source's own licence, and non-commercial terms apply to some of it; ask Claude for AAR Maker's licence. A review run with it isn't legal, safety, clinical or HR advice. It's free, and it may change or stop at any time.

Built by Chris Gagné. Issues: https://github.com/chrisgagne/grounded-forge/issues
