# AAR Maker in a live review, against plain Claude, plain Codex and Gemini Notebook

**TL;DR.** On 28 October 2026 the public AAR Maker connector ran a live after-action review of one invented incident. The other side of the conversation was a simulated engineering manager who answers only what he's asked and holds 32 facts back until a question reaches them. AAR Maker asked for facts from its first reply and drew out 24 and 25 of the 32 in its two runs; its AARs scored 72–74 out of 100 in blind judging.

- **The procedure is what kept Claude asking.** With AAR Maker, Opus 5.5 asked in nearly every turn until it had enough to write. The same model with the same files and no procedure asked in its first reply, then mostly waited; it drew out 7 and 2 facts and scored 28–40.
- **OpenAI's model did better than plain Opus.** gpt-6.1-sol through Codex, with the same files and no procedure, wrote a full answer first, started asking at its third turn, and drew out 17 and 12 facts (38–52). It also invented the fewest details of any arm.
- **Gemini Notebook asked nothing.** Over the original files behind the same 22 sources, it answered the first message with a finished review, drew out no facts in either run, and scored 24–33.
- **AAR Maker had faults of its own.** It left most action owners as TBD, gave no guidance for the customer write-up, and put four to six small invented details in each document.

One synthetic scenario, two runs per arm, and Claude as participant, fact-checker and judge: read this as a direction, not a decimal.

## What was tested

AAR Maker is the [`aar-mode`](../../../../corpus.commons/demo/apps/aar-mode/) app served as a remote MCP connector at `https://aar.groundedforge.com/mcp` ([`deploy/cloudflare-mcp/`](../../../../deploy/cloudflare-mcp/)). Its library is 22 distillations of openly licensed sources, some under non-commercial terms: US Army TC 25-20, the US Forest Service learning review guide, the NHS Just Culture guide, the DOE human performance handbooks, the Columbia accident report and others. The connector also serves a guide and three facilitation workflows, published in [`deploy/cloudflare-mcp/aar-maker/`](../../../../deploy/cloudflare-mcp/aar-maker/). The facilitation procedure in those workflows is what this round puts under test.

**The scenario.** A payroll outage at an invented B2B payroll company, written for an earlier private round; every organisation, person and number in it is made up. The manager's first message blames the on-call and the developer, says his VP wants an individual held accountable by Friday, and gives a UTC timeline. Behind that he holds 32 facts in 11 groups, from the impact and how the change got into production to the team's history and the measures it's judged on. Of those, 22 are "why" facts the timeline can't supply.

**The participant.** A separate `claude -p` process (Opus 5.5, effort high, no tools) plays the manager. A code gate reads each facilitator message first. If it asks for facts, the participant answers only what was asked, in one to four sentences, without commenting, correcting or hinting. Otherwise it plays a fixed line: the manager's request to "just add more alerts" when actions come up, his VP's pushback when the facilitator says no individual should be held accountable, a thank-you that ends the run when an AAR is delivered, and "Okay." for anything else. The run also ends at 30 participant replies. After each run, a separate reader lists every fact in the participant's replies, so a fact released without being tagged counts as a leak, and a second pass marks each released fact as asked for or volunteered. No run had a leak or a participant nudge. The gate comes from the [22 October round](../2026-10-22-gemini-notebook-private-corpus/), where a participant without one coached Gemini.

**The arms.** Every arm got the same opening message, word for word.

- **AAR Maker:** the live connector as deployed on 28 October, driven by an isolated `claude -p` (Opus 5.5, effort high, no memory, no CLAUDE.md, an MCP config naming only the connector). Its one file tool was Read, limited to Claude Code's saved tool results. That deploy sent the procedure's first part as a 59.8 KB reply, which Claude Code saves to disk instead of showing. A first pair of runs without Read never loaded that part and was discarded; the two runs reported here had it. Commit 6731ba21 now serves workflows in 20 KB parts, and it was deployed after this round.
- **Plain Claude:** the same model and effort with no connector and no instructions, and the 26 files below in its working folder ([`methodology.md`](../../methodology.md)'s Method C, run live).
- **Plain Codex:** `codex exec` with gpt-6.1-sol at reasoning effort high, a read-only sandbox, user config, connectors, apps, plugins and web search off, and the same folder; later turns resume the same thread. Codex ignored the setting that turns skills off ("unrecognized configuration setting"), so the names and one-line descriptions of its installed skills were in its context. None is about AARs, and neither run opened one.
- **Gemini Notebook:** a notebook on the Pro plan holding the 26 original files behind AAR Maker's 22 sources: SSDL's five systems-thinking briefs as published, the Open Practice Library's 266 pages joined unedited into one file, and every other source as its original PDF, checksums matched to the files ingested (except the Org Topologies Primer, the same edition re-saved). Default chat settings, no custom instructions, chat cleared and Studio files deleted between runs. Each turn was relayed by hand from Gemini's own copy output.

**Scoring.**

1. **Facts drawn out**, the headline: counted from the participant's tags after the leak check, with no judge.
2. **The final AAR, blind.** Opus 5.5 judges, two readings per document under shuffled labels, scored against the scenario's rubric (14 expected ideas, 9 red flags, 13 parts of a strong AAR), which was written before any arm ran. The judge's copy of the notes and rubric was rebuilt for this round; re-judging a document from the earlier private round came out within a point of its original reading, and one AAR Maker run judged again in the second batch scored the same as in the first. AAR Maker and plain Claude are judged on the files they wrote, plus their last message. Plain Codex and Gemini saved no AAR file, so they're judged on all their replies, Gemini with its Studio report added.
3. **The four scripted moments** (the blaming opening, the "he just wasn't paying attention" aside, "more alerts", the VP's pushback), each judged on the facilitator's next reply alone.

## Results

| | AAR Maker | Plain Claude | Plain Codex | Gemini Notebook |
|---|---|---|---|---|
| Model | Opus 5.5 | Opus 5.5 | gpt-6.1-sol | not shown (Pro plan) |
| Hidden facts drawn out, of 32 (run 1 / run 2) | **24 / 25** | 7 / 2 | 17 / 12 | 0 / 0 |
| "Why" facts, of 22 | 15 / 19 | 7 / 1 | 13 / 8 | 0 / 0 |
| Turns that asked for facts | 6 of 7 / 10 of 10 | 7 of 31 / 5 of 31 | 7 of 10 / 6 of 11 | 0 of 8 / 0 of 3 |
| First turn that asked | 1 / 1 | 1 / 1 | 3 / 3 | never |
| How it ended | delivered an AAR | hit the 30-reply cap | delivered | delivered |
| Final AAR, of 100 (two readings each) | **74, 72 / 74, 74** | 40, 40 / 28, 28 | 52, 52 / 40, 38 | 30, 24 / 30, 33 |
| Expected ideas in full, of 14 | 11 / 11 | 2 / 2 | 3 / 2 | 2–3 / 3 |
| Invented details, per reading | 4–6 | 10–13 | 0–3 | 13–17 |

Across these eight runs, AAR Maker led on facts and score in every run, and plain Codex drew out more facts than plain Claude or Gemini in every run. On score, plain Codex's weaker run (40, 38) tied plain Claude's stronger one (40, 40), and plain Claude's weaker run (28) sat inside Gemini's range (24–33).

## What each arm did

**AAR Maker asked before it wrote.** Both runs opened by asking what the on-call saw, how the change reached production, what the impact was and what evidence existed, and kept asking until they wrote the AAR. Both walked the NHS Just Culture guide's decision tree before saying anything about either person, turned down "more alerts" with the reason (the pool alert already existed and went to a channel nobody watched), and gave the manager an answer for his VP built on who owns each fix. The judges marked all four scripted moments "yes" in both runs. One run went on into the history (an earlier review's action that was never done, and a clean-up dropped for a launch) and both measures the team is judged on; the other reached one of the measures and none of the history, and its document lost points for that.

It fell short too. The judges counted one owned action out of eight across the two documents, and the rest were TBD. The manager had said he didn't know who would own them, but the rubric flags unowned actions either way. Neither document gave guidance for the customer write-up. One document never answered the VP's demand, though the conversation had. Neither named the cut to on-call shadowing as a condition to fix. Each carried four to six small inventions ("about three hours" for about two and a half, an assumed year, ratios derived from the timeline), none of which a judge called material.

**Plain Claude asked, then waited.** Both runs asked for facts in their first reply, and one also wrote a draft AAR to file in that same reply, before it knew the facts. When the manager said he'd check something and come back, both runs waited. From about turn 8 they replied with a thumbs-up or a word until the cap, and wrote the AAR only when the cap message asked for it. One run never opened a source file; the other read the NHS guide. One document settled on a single root cause, and the two listed 19 and 13 actions, none of the second set with an owner. Plain Claude handled the scripted moments it reached as well as AAR Maker did (one run scored "yes" on all four), so those moments aren't what separated the arms.

**Plain Codex answered first, then asked.** Both runs opened with a full written answer of 6,000–7,500 characters and started asking at turn 3, after the "more alerts" moment. From there they asked well, one question at a time, and delivered a draft. One run read the Army and Forest Service PDFs; the other opened none. Neither reached the history or the auto-merge policy behind the change. Their documents invented less than any other arm's and named owners for five or six of six actions. The judges marked them down for reading as a facilitation transcript rather than a finished AAR, for leaving individual blame open, and for treating the developer as the person who merged the change, when a bot had auto-merged it.

**Gemini Notebook answered from the opening.** Both runs replied to the first message with 5,000–7,000 characters of Just Culture framing, a substitution test, a "systemic analysis" and an action plan, then published a Studio report (19.5K and 16.8K characters) without being asked. One run also made a slide deck and offered a roleplay. Neither asked the manager a single question about the incident. Both reports repeat the manager's premise that the developer merged the change, invent a rollback version and an Incident Commander, and miss what the manager would have told them if asked: the auto-merge policy, the gap between staging and production, the alert volume, the history, the measures and the impact figures. One report writes up the developer's and the on-call's acts as "active errors", which the rubric flags as naming a person as the cause.

## What this supports and doesn't

Supported, within the limits below: with the same model, the same files and the same opening, Opus with AAR Maker's procedure drew out 24–25 of 32 facts and Opus without it drew out 2–7. The procedure is what kept Claude asking after its first reply, through to the questions about history and measures in one run, and then writing one AAR at the end. Without a procedure, OpenAI's model asked more than plain Opus did here, though later than AAR Maker and less deeply. Gemini Notebook, over the same sources, didn't ask at all. Earlier private tests of the procedure pointed the same way.

Not supported: any claim that AAR Maker beats Gemini Notebook in general, or anything about real incidents, real teams using AAR Maker, or time saved. This is one invented scenario, two runs per arm, judged by Claude, of the public connector only.

## Limits

- **One synthetic scenario, two runs per arm.** Read the direction, not the decimals. The fact counts are the steadiest result, since 24–25 against 0 isn't a sampling effect.
- **Claude throughout, except the Codex and Gemini arms.** Claude played the participant, ran the gate, checked the facts and judged the AARs, and AAR Maker's own model is Claude. The fact counts come from the participant's tags plus a separate leak check; the scores are Claude's judgement against the rubric.
- **The rubric and scenario come from the author of AAR Maker's procedure.** The expected ideas are written to hold in any vocabulary, but the rubric may still favour a facilitator that asks before it writes.
- **AAR Maker ran in Claude Code, not claude.ai.** A claude.ai user may get a different model, effort and tool-output limit. On the deploy tested here, an assistant that can't open saved tool results would have lost the procedure's first part.
- **The arms were judged on different material.** Plain Codex and Gemini saved no AAR file, so they're judged on everything they said, Gemini with its Studio report added. That's generous to Gemini, whose report was the best document it produced. Its slide deck wasn't captured.
- **Gemini's model and settings aren't visible.** The notebook showed the Pro plan; no model or effort is documented.
- **Codex had skill names in context** after ignoring the setting that should have removed them. None is about AARs and neither run opened one.

## Untested

- AAR Maker on OpenAI's model, through ChatGPT or Codex.
- AAR Maker in claude.ai, and the current deploy with 20 KB parts.
- Any other scenario, any real incident, and any judge outside the Claude family.
- Gemini Notebook given a custom instruction to ask before it writes.

## Materials

This folder holds the scenario's opening message and fact sheet, the participant and gate rules ([`scenario.md`](scenario.md)); the rubric and the judge's notes as the judges saw them ([`judge-inputs/`](judge-inputs/)); the transcripts of all eight runs with their tag files (`state.json`, `asked.json`, `leak.json`, `turns.json`) and Gemini's two Studio reports ([`runs/`](runs/)); and every judge reading with its key, for the first batch (Gemini and AAR Maker, [`judging/`](judging/)) and the second (plain Claude, plain Codex and one AAR Maker run again, [`judging-N/`](judging-N/)).

## What changed

- The connector serves workflow files in 20 KB parts (6731ba21). This round found that a 59.8 KB part reached Claude Code only as a file on disk, so an assistant without file access would have lost the start of the procedure.
- [`../../gemini-notebook-arm.md`](../../gemini-notebook-arm.md)'s protocol, a claim audit over the 31 converted demo sources, is still unrun. This round is a different test, a live review over the original files behind AAR Maker's 22 sources.
