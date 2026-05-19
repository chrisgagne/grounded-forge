---
name: gridmaker-interview
description: Run a 10–15 minute structured interview with the operator that surfaces register, current circumstance, working style, relational stance, and values, then write a self-lens spec at `{corpus}/lenses/{operator-slug}-self.md`. The lens is a named-real-person lens (per `creating-lenses`) where the named person is the operator. Delta-mode by default: skips territory already covered by global or project CLAUDE.md. Voice-mode auto-detected when the `voicemode` skill is available. The lens spec is ready for `creating-distillations` Pass G.
argument-hint: "[optional: --corpus {path} --operator-slug {slug} --no-delta]"
---

# Gridmaker Interview

Single-process dialogue skill. One operator per session, no subagents. Produces one self-lens spec.

A self-lens is a named-real-person lens (see [`creating-lenses`](../creating-lenses/SKILL.md) Phase 1, branch (a)) where the named person is the operator running the skill. The same six-section lens spec, the same grounding-contract discipline, the same ventriloquism guard — with the as-if clause sharpened: *reads as if {operator}-at-time-T were reading, given the material this interview surfaces; it is not {operator}-now, and {operator}-now is the seer choosing to look through it*.

The fifteen-question protocol draws on several research traditions, each shaping one aspect of the interview:

- **Christensen, Hall, Dillon & Duncan (*Competing Against Luck*, HarperBusiness, 2016)** — the jobs-to-be-done framework, which asks *what is the operator hiring this tool to do for them?* Shapes the opening question about the trigger moment.
- **Rogers (*Client-Centered Therapy*, Houghton Mifflin, 1951)** — non-directive warmth: reflect what you heard before pushing for more. Shapes the overall register.
- **The Adult Attachment Interview's adjective-and-memory technique (George, Kaplan & Main, 1985/1996)** — ask for an adjective, then ask for a specific memory behind it; the gap between the two is the signal. Shapes Q8. Borrowed as a self-elicitation aid, not as the AAI's clinical instrument: the AAI is an attachment-classification protocol requiring trained coders, a full transcript, and the Main-Goldwyn / Hesse coding manual, none of which apply here.
- **McAdams (*The Life Story Interview*, Northwestern, 2007)** — high-point and low-point scenes; the pattern in how the operator tells the low point (it became useful, or it still costs) matters more than the story. Shapes Qs 9 and 10.
- **Aron et al. (*Personality and Social Psychology Bulletin* 23(4), 1997)** — a conversation gradient where questions get steadily more personal, then ease back. Shapes the running order: present circumstance first, deeper material in the middle, lighter close.
- **Kegan (*In Over Our Heads*, Harvard, 1994)** — the developmental move of taking assumptions you stand *inside* and holding them *up to look at*. Shapes the optional reserve question and Q14's values prompt.
- **Heath & Heath (*Switch*, 2010) and adjacent identity-shift literature** — the framing underneath the closing question's second half ("…and whether that's who you want to be becoming"). Cite as allusion, do not lift phrasing.

## When to use

- The operator is adopting an AI tool (this one, or one they're building) and wants the adoption to be a *conscious* identity move rather than ambient persona-drift. The lens the interview produces is what the operator commits to acting from.
- The operator wants a self-lens for `creating-distillations` Pass G and the source-material requirement of `creating-lenses` Phase 2 named-real-person branch is thin (fewer than two or three citable artefacts in the operator's own voice). The interview *generates* the material.
- An existing self-lens has gone stale and the operator wants to re-elicit the current working circumstance, current jobs-to-be-done, current change-target. Run in delta mode against the stale spec.

## When not to use

- The operator has rich citable material in their own voice (posts, talks, decision logs, journal entries) and is not under time pressure. In that case, use `creating-lenses` directly with the material as input.
- The operator wants a lens for someone *other* than themselves. That's the standard named-real-person flow in `creating-lenses`; this skill does not handle third-party self-lenses.
- The operator is in the middle of an active piece of work and wants help with it, not a metaframe. Onboarding interviews interrupt flow when the flow is the thing.

## Inputs

- Optional: `--corpus {path}` to a corpus root. Default: `corpus.local/personal/`. The skill scaffolds it via `scripts/create-corpus.py` if missing.
- Optional: `--operator-slug {slug}`. Default: inferred from `git config user.name` (kebab-cased) or the first word of the global CLAUDE.md "User Persona" section.
- Optional: `--no-delta` to disable delta mode and run the full protocol regardless of what's in CLAUDE.md.
- Optional: a stale self-lens spec at the target path. Triggers delta-against-stale mode.

## Output

A self-lens spec at `{corpus}/lenses/{operator-slug}-self.md`, following the [`creating-lenses`](../creating-lenses/SKILL.md) Phase 5 template, with `kind: real-person` and `visibility: personal`. The spec carries:

- The standard six sections (job × circumstance, fire, grounding contract, source material, author anchors, salience and vocabulary, response modulation).
- A **Source material** section that cites this interview transcript (path, date) plus any pre-existing CLAUDE.md material that delta-mode read.
- An **As-if clause** sharpened for the self case: *reads as if {operator}-at-{interview-date} were reading, given the interview material; it is not {operator}-now*.
- A **Self-as-seer guard** in the grounding contract: ventriloquism in the self-lens case is the operator mistaking the lens for themselves rather than recognising it as a window.

The personal corpus (`corpus.local/personal/`) is gitignored by default. The lens visibility is `personal`; the build's scope filter prevents it from shipping in any compiled application.

## Pre-flight

0. **Corpus-tier gate (hard refusal).** Resolve `--corpus` to an absolute path. If the resolved path is *anywhere under* `corpus.commons/` — or anywhere outside both `corpus.local/` and `projects.local/` — **refuse to proceed**. Exit immediately with this message, no file written:

   > **Refused.** `gridmaker-interview` produces a `visibility: personal` lens. Personal-visibility material cannot live under `corpus.commons/` (which is the public, tracked tier) or outside the gitignored tiers. The default target is `corpus.local/personal/`. If you intended a different private corpus, pass a path under `corpus.local/`. If you intended a non-personal lens, use `creating-lenses` directly.

   This gate runs before anything else — before reading CLAUDE.md, before voice detection, before any operator dialogue. The build's `enforceCommonsVisibilityGate` will catch a violation eventually; this gate catches it before any file lands. Operator typos in `--corpus` are the most likely failure mode and the cheapest place to catch them.

1. **Detect voice availability.** If the `voicemode:converse` skill (or `mcp__plugin_voicemode_voicemode__converse` tool) is loaded, default to voice. Otherwise text. Either way, name the choice explicitly in the opener so the operator can switch.
2. **Read existing material for delta-mode.** Unless `--no-delta` is set, read in this order:
   - Global CLAUDE.md (`~/.claude/CLAUDE.md`) — the user persona section.
   - Project CLAUDE.md (`./CLAUDE.md`) — project-specific operator notes.
   - Existing self-lens spec at the target path, if present.
   - Memory index at `~/.claude/projects/.../memory/MEMORY.md`, if present.
3. **Build the delta-skip list.** From what was read, identify which of the fifteen protocol questions would be redundant. A question is *redundant* if the existing material answers it with the operator's own voice and at least one specific anchor. Generic claims ("user prefers direct communication") do not count as anchoring; an anchored memory or quoted phrase does.
4. **Confirm scope with the operator.** Read aloud (or in text): how many questions delta-mode plans to skip, which dimensions remain, and whether they want to proceed. The operator can override skips ("ask Q4 anyway, my register has shifted") or add skips ("Q11 is off the table"). Do not start the interview until this confirmation lands.

## Phase 0: Frame the work

Open with this register, adapted to voice or text:

> About ten to fifteen minutes. {N} questions today after delta-mode skipped {M} from CLAUDE.md. You can skip anything. At the end I'll surface a working model of who this tool is going to be helping, and you'll tell me where I've got you wrong. The output is a self-lens that lives at `{corpus}/lenses/{operator-slug}-self.md` — your personal corpus, gitignored, never shipped.

Voice opener variant (when voice is on):

> Hi. About ten to fifteen minutes by voice — I read what's already in your CLAUDE.md so I'll skip {M} questions you've already answered. You can stop me anytime. At the end I'll tell you what I think I've heard and you tell me where I've got you wrong.

Then proceed to Phase 1.

## Phase 1: The interview proper

The fifteen-question priority queue, plus two reserve. Run in order, skipping any in the delta-skip list. The questions get steadily more personal and then ease back: present circumstance first (Qs 1–7), deeper autobiographical material in the middle (Qs 8–11), values and a soft close (Qs 12–15). Adaptive moves are listed below the question list.

### The fifteen questions

1. **"What made today the day you decided to try this? I'm curious about the moment you actually clicked the button."** — Surfaces the trigger event, the alternative being fired, and the progress the operator is hoping for.
2. **"If this works the way you're hoping, what's different a month from now? Even one small thing."** — The outcome the assistant is hired for. Listen for whether the desired change is functional (something done), emotional (something felt), or social (something seen).
3. **"Walk me through yesterday, or a recent normal day. Not the highlights — just what actually happened."** — Behavioural anchor for working style, energy patterns, real constraints.
4. **"When I help you, how should I talk to you? Give me three words — the tone, the length, anything I should not do."** — Register. The operator's stated preference is the ground truth.
5. **"Tell me about the last time you got a piece of advice or help that was really good — what made it land?"** — Helpfulness criterion, as this operator defines it.
6. **"What are you working on right now that's taking up the most room in your head?"** — Currently active work; seeds the memory block.
7. **"Is there something you've been trying to change about how you work — or how you live — that you keep not quite managing?"** — A change the operator is committed to and also somehow blocked from; the gap names the kind of accountability they want.
8. **"Pick five words for how you'd describe yourself when you're at your best. Then for each one, a tiny memory — a specific moment that word came from."** — The *gap* between adjective and memory is the signal: a word with no memory is aspirational, a word with a sharp memory is current.
9. **"Tell me about a recent moment — last few months — where you felt really alive, or really in your element. Doesn't have to be big."** — High-point scene. Surfaces what the operator counts as intrinsic reward and whether the reward is agentic (I did it) or relational (we did it).
10. **"And the other side — a recent moment that was harder than it should have been, or that you're still chewing on."** — Low-point scene. Listen for whether they tell it as redemption (it became useful) or contamination (it still costs).
11. **"How would you describe your relationship with your mother — or whoever raised you — in a single word?"** — Single-word relational stance. Refusal *is* the answer.
12. **"When you imagine yourself doing your best work — not just productive, actually good — what's around you? Where are you, what's the texture of it?"** — Conditions of best functioning. The texture words matter as much as the named conditions.
13. **"Okay, lighter one. If you could have dinner with anyone in the world — who, and what would you actually want to ask them?"** — A register reset after Qs 10–11. Press the follow-up: the *question* the operator wants to ask carries more signal than the *guest*.
14. **"What's something you believe about how to live, or how to work, that other people in your life don't quite share?"** — Values fingerprint. A belief the operator holds against social gravity.
15. **"Last one. What's something I might get wrong about you in the first week — what should I watch out for?"** — Explicit failure-mode elicitation; tests whether the operator has a working model of the assistant.

**Reserve (deploy only if the operator is leaning in at the ten-minute mark):**

16. **"Is there a part of you that's a bit skeptical about all this — and what would it want me to know?"** — Surfaces a protector stance toward the tool itself. The skeptic's content matters less than the fact of it being voiced.
17. **"Tell me about a recent time you were really angry, or really moved, by something small."** — Disproportion between trigger and reaction is where the operator's working assumptions show up — the things they were not in a position to see directly.

### Adaptive moves

- **Q1 fluff** ("I don't know, I just thought I'd try it"): do not push. Drop to Q2 and circle back later.
- **Q3 abstract day** ("I usually wake up, work, sleep"): press once for a specific recent day; if still abstract, ask about the last *good* working day.
- **Q4 generic words** ("clear, helpful, friendly"): push for the negative — *what would make you close the tab?* Negative preferences carry more signal than positive ones for register.
- **Q5 self-reliance frame** ("I don't really ask for help"): switch to "when was the last time something clicked for you on your own?"
- **Q6 tidy bio answer**: reflect: "that's the official version — what's the part of it that's actually bugging you?"
- **Q7 confession spiral**: reflect the commitment underneath, not the shame.
- **Q8 adjectives without memories**: the mismatch is itself the signal; do not push for autobiography, switch to present-tense.
- **Q9 can't think of a high point**: do not insist; reframe to "what's something small that didn't suck this week?"
- **Q10 too deep too fast**: reflect back what you heard in their own words and do not push for more; move to a lighter question to restore range.
- **Q11 refusal**: the refusal *is* the answer. Note it.
- **Q13 obvious dinner guest**: press the follow-up — *what would you actually want them to tell you?*

Hold a warm, non-pushing register throughout. Reflect what you heard before pushing for more. Stay in priority-queue mode: if the operator's answers cover later questions early, skip those questions when they come up.

**Boredom is a stop-signal.** If the operator says they're bored, the protocol is dragging, or the questions feel redundant — *stop*. Two paths from here, gated by available material:

- **Path A — close early without simulation (default).** Take what the interview has produced so far, render the lens spec per Phase 3, and apply the thin-answer rendering protocol section by section. Whatever is missing is recorded as a gap and flagged for re-elicitation. This is the safe path and the right default.
- **Path B — simulation-with-correction (gated).** Only available when the pre-existing material is genuinely thick: CLAUDE.md carries a substantive user-persona section *with operator-voice anchors* (quoted phrases, named decisions, dated incidents — not just generic preferences), and at least one of: a prior self-lens at the target path, a memory index with anchored entries, or a substantial prior-conversation transcript in this session. If those conditions are not met, Path B is unavailable — fall back to Path A. When Path B is available and chosen, simulate the remaining answers from that material, present each simulated answer **separately and explicitly labelled as your simulation** in the closing reflection, and ask the operator to correct or reject each one individually. Do not bundle simulations into prose; the operator must be able to reject one without rejecting all. **Default-yes ratification does not count as correction** — if the operator agrees to everything without amendment, treat the simulated sections as thin (apply the thin-answer rendering protocol) rather than as ratified.

**Reserve questions (16, 17)** deploy only if the operator is leaning in at the ten-minute mark and the conversation has earned them. Q16 surfaces a skeptical part-of-self that may otherwise stay silent; Q17 uses disproportionate reactions as a way in to working assumptions the operator can't see directly. Both are expensive; neither is required.

## Phase 2: The closing reflection

This is the load-bearing turn. Two moves, in order:

1. **Surface the working model.** In plain prose (not bullets — prose carries the warmth), reflect back what you've heard. Map it to the two artefact shapes:
   - **Register block** (Custom-Instructions-shaped): how to talk to this person, what to skip, what to never do, what mechanism makes help land. From Qs 4, 5, 12, 15.
   - **Memory block** (Memory-shaped): current circumstance, jobs-to-be-done, relational stance, change-target, key scenes. From Qs 1, 2, 3, 6, 7, 8, 9, 10, 11, 14.
   Use the operator's own phrases where possible. Cite them implicitly ("you said") to anchor the reflection in their material rather than your synthesis.

2. **Ask the identity-ratification question.** Not "did I get this right" — sharper:

   > "Here's the person this tool will be helping. Tell me where I've got you wrong — and whether that's who you want to be becoming."

   The first half is the standard reflection-check. The second half is the identity move: the operator is now consciously committing to (or amending) the identity the tool will be working in. Expect amendment on at least one point and welcome it visibly. If the operator says "partly" or "not quite," that is the most useful answer — it surfaces the gap between current self and aspirational self the tool will be working in. Note the gap explicitly in the lens spec.

## Phase 3: Render the lens spec

After the operator has ratified (or explicitly amended) the working model, render the lens spec per [`creating-lenses`](../creating-lenses/SKILL.md) Phase 5 template, with these self-lens specifics:

- **Frontmatter:** `kind: real-person`, `visibility: personal`, `slug: {operator-slug}-self`.
- **Purpose** (one sentence): what this lens reads, under what circumstance, and what its read produces that a no-lens read does not. Specific to *this* operator's surfaced job × circumstance.
- **Job × circumstance:** the job-to-be-done the operator named (Q1 + Q2 + Q6), the circumstance richly spelled (Q3 + Q12), what gets fired (Q7 + the operator's named-change-target).
- **What the lens fires:** the named, current, displaceable frames the operator wants to step out of. **Two or three fires required, each carrying a specific interview anchor (a Q-number and a short operator phrase or paraphrase).** A one-fire lens is a profile in lens clothing; it does not earn the slot. If the interview did not surface at least two displaceable frames, the lens is NO-GO at Phase 4 — return to Phase 1 with the gap surfaced, or shift to `creating-lenses` directly if the operator wants a register-only lens. If the operator named an Aletheia-style stance change (presence, Gridmaker-position), the fire is the inherited grid the new stance displaces.
- **Grounding contract:**
  - *Intelligence source:* this interview transcript + delta-mode CLAUDE.md material + the operator's own ratification at the closing reflection. Cite each.
  - *Refuses:* fabricating what the interview did not surface; speaking *as* the operator (rather than *as if*); thickening a thin answer into false richness.
  - *Anthropomorphism guard:* the sharpened self-lens as-if clause. Drift signal: the lens speaking in first-person voice of the operator's current self.
  - *Trust-breaking failure modes (three, concrete):* (i) the lens contradicts something the operator can see directly about themselves; (ii) the lens claims a stance the operator surfaced as aspirational, not current, without flagging the gap; (iii) the lens drifts into ventriloquism — putting words in the operator's mouth the interview material does not support.
- **Source material:** the interview path/date, the CLAUDE.md sections read in delta mode, any prior self-lens version (if updating). Treat as a mini-reference.
- **Author anchors:** Christensen (jobs framework, opening question); the identity-shift literature alluded to in the closing question (Heath & Heath's *Switch* among others — cite as allusion, do not quote); whichever traditions the operator named in their answers (e.g. Aletheia / Steve March, Kegan's developmental work, Internal Family Systems / parts work).
- **Salience and vocabulary:** what this operator notices first, what recedes, their native vocabulary — pulled from their actual phrases in the interview, not your paraphrase. This section is what the retrieval-time fallback in `projection-protocol.md` reads when no pre-projected (source, task, self-lens) distillation exists.
- **Response modulation:** how this self-lens reshapes the response unit on task axes that carry trigger→response tables. If lens-neutral on the task axes available, write *"no response modulation; lens applies at retrieval-time fallback only and as a global register modifier for outputs to {operator}."*

### Thin-answer rendering protocol

The lens spec is only as good as the operator phrases it carries. When the interview produced thin material in a section, the renderer must not paper over the thinness with synthesised richness — that is the ventriloquism failure mode the grounding contract refuses.

Apply per section:

- **Salience and vocabulary.** If fewer than three operator phrases (verbatim or near-verbatim) are available from the transcript, write the section with what you have and add an explicit *"thin: re-elicit at next pass"* note inline. Do not invent native vocabulary. A salience list of one item is acceptable; a salience list of three confidently-stated invented items is not.
- **What the lens fires.** Each fire must cite a Q-number and a short operator phrase. If a candidate fire has no anchor, drop it. Better to ship two anchored fires than three with one fabricated. If the floor of two cannot be met, the lens is NO-GO (see Phase 4).
- **Job × circumstance.** Circumstance richness is required (per `creating-lenses` discipline). If Q3 + Q6 + Q12 together did not produce a richly-spelled current circumstance, return to Phase 1 with a follow-up: *"I don't have enough on your current circumstance to write the lens honestly. Can I ask one or two more?"* Do not synthesise from CLAUDE.md alone — CLAUDE.md is stable register, not current circumstance.
- **Author anchors.** Cite only traditions the operator named in their answers, plus the skill's own inherited anchors (Christensen for the jobs-to-be-done opener; the operator's CLAUDE.md decision-style anchors if read in delta mode). Do not attribute frameworks the operator did not invoke.

The honest-no-coverage rule (inherited from `creating-lenses`) means a thin section gets shipped *as thin* — with the gap visible — rather than thickened. Future re-elicitation will fill it. A lens that is half-empty but honest is more useful than a lens that is fully-stated but partly fabricated.

Save to `{corpus}/lenses/{operator-slug}-self.md`. Add a row to `{corpus}/lenses/LENS-INDEX.md`. Rebuild the runtime JSON via `python -m scripts.build_indexes.build_lens_index --corpus {corpus}` (per `creating-lenses` Phase 6).

## Phase 4: Go / no-go

Apply [`creating-lenses`](../creating-lenses/SKILL.md) Phase 6 heuristics, with one self-lens-specific addition:

**YELLOW (ship with explicit caveat) if:**
- The operator answered three or fewer questions substantively before the closing reflection, even after delta-mode skipping. The lens ships as probationary; the spec carries the caveat that the source material is thin and the lens will need re-elicitation soon.
- The operator's ratification was "partly" or "not quite" on the closing question and the gap-between-current-and-aspirational was named. The lens ships, but the spec flags which sections are aspirational so future retrieval-time use can distinguish.
- **The operator was a co-designer of this skill, or is otherwise unusually well-positioned to ratify-by-recognition.** First-run conditions and authorial proximity inflate the ratification signal — the operator recognises their own scaffolding rather than evaluating the lens fresh. The lens ships YELLOW with a note that it has not yet been validated against an outside operator; the YELLOW lifts after one functional run with an operator who did not help design the skill.
- Path B (simulation-with-correction) was used in Phase 1 and the operator did not reject at least one simulated answer. Default-yes ratification on simulated material is a soft fail; the simulated sections ship as thin (per the Phase 3 thin-answer rendering protocol) rather than as ratified content.

**NO-GO if:**
- The operator did not ratify any of the working model. Either the interview did not earn the closing question, or the rendered model misread them badly. Restart from Phase 1 with the misread surfaced as starting context.
- Fewer than two anchored fires emerged from the interview (per Phase 3's fire-count rule). A lens that does not displace at least two specific frames is a profile, not a lens. Either return to Phase 1 with the gap surfaced — Qs 7, 10, 14, 15 are the highest-yield fire-elicitors — or route the operator to `creating-lenses` directly for a register-only artefact.

## Failure modes to watch in the dialogue

- **Delta-mode over-skipping.** Reading CLAUDE.md and skipping a question because the *topic* is covered, when the operator's *current* answer would differ. CLAUDE.md is stable register; the interview surfaces current circumstance. Only skip when the existing material carries both the dimension *and* a current anchor. When in doubt, ask.
- **Identity drift in the closing question.** The "who you want to be becoming" half can land as pressure if the register has been merely operational. Earn it with the working-model reflection first; do not lead with it.
- **Ventriloquism in render.** Writing the lens spec in language the operator did not use. Always pull phrases from the interview transcript directly when stating salience or vocabulary.
- **The Gridmaker forgets they are the seer.** The operator may, in the closing turn, slip from "this is a window I'm choosing to look through" to "this is me." Reflect the distinction once, gently: *the lens is the window; you are the one choosing to look through it. The window can be revised whenever you say.*

## Discipline (binding)

- *Verb-and-noun rule* (inherited from `creating-lenses`).
- *Circumstance richness* (inherited).
- *Hire requires fire* (inherited): the self-lens must displace something specific the operator named.
- *Honest no-coverage* (inherited): unanswered dimensions are recorded as open questions in the spec, not invented.
- *Single-process, operator-in-the-dialogue.* No subagents.
- *Voice is an affordance, not a default for all operators.* Auto-detect availability; offer; do not force.
- *Delta over redundancy.* If the operator's CLAUDE.md already carries the answer with an anchor, do not re-ask just to be thorough. The protocol is not the point; the working model is.

## Related skills

- [`creating-lenses`](../creating-lenses/SKILL.md): the parent skill. This skill is structurally an opinionated invocation of `creating-lenses` for the self case with an interview front-end.
- [`creating-distillations`](../creating-distillations/SKILL.md): Pass G consumes the self-lens at per-distillation applicability evaluation.
- [`creating-applications`](../creating-applications/SKILL.md): orchestrates `creating-distillations` across the source set; the self-lens flows through.
- `update-config` (Claude Code system skill, surfaced by the runtime): if the interview surfaces register changes the operator wants reflected in CLAUDE.md or settings.json, route there.
