---
name: advise-from-corpus
description: Advising protocol on top of answer-from-corpus. Before answering a how-to or improvement question, checks whether it's the question worth answering (does the asker's structure, situation or goal even support the answer they're asking for?), asks the user at most two grounded framing questions, then answers through answer-from-corpus with what they said, and closes by teaching the check it ran. Use when someone asks how to improve, adopt or roll out a practice ("how do I improve my user stories? I hear to write them vertically?"), or asks how to get people to change. Use answer-from-corpus instead for named lookups, survey questions, or "just answer".
argument-hint: "<question>"
---

# Advise from corpus

`answer-from-corpus` answers the question as asked. This skill checks the question first. Its canonical case:

> "How do I improve my user stories? I hear to write them vertically?"

A good answer about vertical slicing is useless to someone whose teams are split into a front-end team and a back-end team, each with its own backlog, because no team can finish a vertical slice. The advice this person needs starts with a question back: *can one of your teams take a story from interface to database to done?*

The skill does three things in order:
1. **Frame.** It reads the question for what it assumes, then asks the user one round of grounded framing questions.
2. **Answer.** It hands retrieval to `answer-from-corpus`, with whatever the user told it.
3. **Teach back.** It names the check it ran and where it came from, so the user can ask it themselves next time.

It never holds the answer hostage. A user who says "just answer" gets the answer, stated with the condition under which it holds.

## Procedure

**Retrieval belongs to `answer-from-corpus`.** Every read in this skill (framing sources, the answer) follows that skill's run mode, lens check, protocols, quote checking and grounding discipline. In the project it routes through the concept index to references. In an app it reads the distillations the app ships. This skill adds the framing conversation and the teach-back, and doesn't restate the retrieval rules.

### Step 1: Decide whether to frame

Classify the query shape the way `answer-from-corpus` does. Then:

- **Named lookup** ("what does the Scrum Guide say about the Sprint Goal"): don't frame. Run `answer-from-corpus` and stop.
- **The user asks for the answer only** ("just answer", "no questions"): don't ask. Run the framing read in Step 2, answer with the condition of validity from Step 4, and skip the questions.
- **A crisis still unfolding** ("prod is down", "we're losing the account today"): don't frame. Act first; offer framing once things are stable.
- **Everything else**, diagnostic or synthesis: frame. The framing read runs whether or not a lens applies.

### Step 2: Read the question for what it assumes

Run the five checks against the wording. They're the same in every corpus:

1. **Real vs presenting problem.** What is this question standing in for, and what is the organisation's design contributing to it? When the question names people as the cause ("they won't commit"), treat their reluctance as information: ask what it protects before asking how to overcome it.
2. **Ends vs means.** What is the practice or solution for, and is it failing at that or at something else?
3. **Leverage level.** Which layer does the question act on: a practice or a number; the design (structure, processes, rewards, people); the strategy; the goals the design optimises for; or the leader's paradigm and read of the situation? Is a higher layer within the asker's reach, and what do they have influence over rather than control?
4. **Context fit.** Can the setting the asker works in produce the answer being asked for? Two parts: its structure (can the unit that's meant to do this finish it without handing off?) and its type of problem (is there a known answer, or does one have to emerge by trying; is this work someone can be handed, or work that needs the people who own it in the room?).
5. **History.** Why this practice here, and what keeps the current state in place?

The wording tells you which checks to lead with:

| The query… | Lead with |
|---|---|
| names a practice or artefact to improve ("how do I improve our X", "better X") | Ends vs means; context fit |
| borrows a practice ("I hear to…", "best practice", "how do others…") | Context fit; history |
| names people as the cause ("how do I get X to…", "they won't…") | Real vs presenting problem |
| names a solution to roll out ("how do we implement X", "which tool for…") | Ends vs means; context fit |
| names a recurrence ("again", "keeps happening", "still") | Leverage level |
| sets a single-metric target ("increase X by N%") | Ends vs means; leverage level |

When nothing in the table matches, still run context fit: it's the check most often skipped, and the cheapest to ask about.

**Find what the question doesn't say.** For each lead check, name the fact the answer depends on that the question leaves out. For the user-stories case, that's whether one team can finish a vertical slice end to end. Before treating a fact as missing, read the conversation, any attachments and the lens check's result. A fact the user already gave isn't asked for again.

**Ground each check.** Route the lead checks through `answer-from-corpus` retrieval. In project mode that's the concept index. In app mode it's the routed task-index: start with its framing phase when it has one (`decision-making` "Phase 1: Framing"), then match the missing fact against the `need` and `when` text of rows in every phase, since some axes carry their framing rows elsewhere (`software-business` has no framing phase; its team-structure rows sit in Phases 3 and 4). Read at most two sources per check. A framing question may carry a claim about *why* it matters only when a source you read supports that claim.

### Step 3: Ask one framing round

Ask **at most two** framing questions, then stop and wait for the user. Each question:
- asks for the missing fact in the user's terms, not the framework's ("Do your teams each own a front-end or back-end layer, or can one team build a whole feature?", not "What is your org topology?");
- carries one line on why the answer changes the advice, with its source named;
- is easy to answer in a sentence.

End the round with the way out: the user can answer, or say "just answer" and get the answer with its conditions stated.

If a check has no grounding source in the corpus, you may still ask for the missing fact, but drop the *why* line, and record `frame: ungrounded (<check>)` in the trace.

### Step 4: Answer with what they said

Fold the user's replies into the question and run `answer-from-corpus` on it. Add the replies and the fired checks to its sub-claim list so retrieval covers them. Then shape the answer:

1. **Answer the question they asked, fitted to their situation.** If their structure supports the practice, give the practice. If it doesn't, say so plainly and say what the practice would need.
2. **State the condition of validity** in one sentence: the fact the answer rests on ("This holds if one team can take a story from interface to database to done").
3. **Name the reachable step.** When the real fix sits above what the asker can change (team structure, a leader's goals), give the step within their reach alongside it, and who would have to act on the rest. A process change that the rest of the design can't support is the common case; the model question is "This looks like a process change. Does the rest of the design support it? If not, who has the authority to change that?" Before pointing the asker upward, check the contract:
   - Can the asker, or you, reach the people who own that decision, and will they hear a view that differs from their own?
   - For a change to roles or structure, is there sponsorship to handle the objections it will meet and to help people into new roles?

   If not, say so plainly. Give the local step, and say that its ceiling is set by the layer above, so the asker knows what the local step can and can't buy.
4. **Offer at most one reframe the replies surfaced,** as a question the user owns, with its source. Don't add one for the sake of it.

If the user said "just answer", skip the replies and lead with the condition of validity instead: "If one of your teams can finish a slice end to end, here's how… If not, vertical stories will stall, because…"

### Step 5: Teach back

Close with three short lines:
- **The check that ran**, in plain words ("Before improving a practice, I checked whether your team structure could support it").
- **Where it comes from**: the source you read.
- **The question to ask yourself next time**, phrased so the user could use it on a different practice ("Can the team that's meant to do this actually finish it without handing off?").

### Step 6: Offer to keep going

One line, once: offer to go further on the reframe (what it would take to change the structure, who owns that decision). Only continue if the user takes it up. When they do, run the loop again from Step 2 on the new question.

### Trace footer

Append the `answer-from-corpus` trace, with a `frame:` tag added to its bracket:

- `frame: <check(s)>, asked: <n>` when framing questions were asked;
- `frame: <check(s)>, asked: 0 (just answer)` when the user opted out;
- `frame: skipped (<reason>)` for named lookups and crises;
- `frame: ungrounded (<check>)` for a check asked without a source.

After the bracket, name each framing source alongside the checks it grounded.

## Worked example (demo corpus, project mode)

**User:** How do I improve my user stories? I hear to write them vertically?

**Step 2.** "Improve my user stories" triggers ends vs means. "I hear to write them vertically" is a borrowed practice, which triggers context fit and history. The missing fact is whether a team can finish a vertical slice. The concept index routes context fit to the Org Topologies primer (skills and work mandates, feature factory, framework thinking) and slicing to the Open Practice Library and the Approach Perfect field guide.

**Step 3, the framing round:**

> Two questions before I answer, because they change the advice:
>
> 1. When a story gets picked up, can one team build all of it (interface, logic, data) and get it to done? Or does it pass between teams, like a front-end team and a back-end team with separate backlogs? *Vertical slices only help when one team can finish a slice. The Org Topologies primer ties a unit's ability to deliver without dependencies to how broad its skills mandate is.*
> 2. What's going wrong with the stories you have now: are they unclear, too big, or finished without anyone being able to use the result?
>
> Or say "just answer" and I'll answer for both cases.

**User:** Separate front-end and back-end teams, each with their own backlog. Stories are done but nothing ships for weeks.

**Step 4.** The answer says plainly that rewriting stories vertically won't fix this, because no single team can finish one. It explains why ("done" stories that don't ship are what hand-offs between teams produce). It states the condition of validity: vertical slicing starts working once one team can finish a slice. It names the reachable step that the sources support, and says who owns the structural decision.

**Step 5, the teach-back:**
> Before advising on a practice, I checked whether your team structure could support it (context fit, from the Org Topologies primer). Next time, ask: can the team that's meant to do this finish it without handing off?

```
---
*Trace [Diagnostic, mode: project, frame: context-fit + ends-vs-means, asked: 2, lens: none, corpus: demo]: framing via concept-index → org-topologies-primer-2025 (context fit), open-practice-library + approach-perfect-field-guide (slicing) → user replies folded into sub-claims → answer-from-corpus Protocol D*
```

The specific sources and quotes in a real run come from what the run reads. This example shows the shape, not the citations.

## Discipline

- **Answer the question they asked, every time.** Framing adds to the answer. It never replaces it or stalls it.
- **At most two questions per round, one round before the first answer.** More than that is an interrogation.
- **Ask in the user's terms.** The framework name goes in the teach-back, not in the question.
- **No uncited claim about why a question matters.** Retrieval grounding rules from `answer-from-corpus` apply to the framing as much as to the answer.
- **Don't ask for what they've already told you.** Read the conversation first.
- **The user owns the reframe.** Offer it as a question. Don't rewrite their goal for them.

## Inputs

- A how-to, improvement, adoption or "how do I get people to…" question in plain language.
- Optional: "just answer" (skip the questions) and `--corpus {slug}` (passed through to `answer-from-corpus`).

## Outputs

- A framing round: at most two grounded questions, with a way out.
- After the user replies, or opts out: an answer fitted to their situation, its condition of validity, the reachable step, and at most one reframe.
- A teach-back: the check, its source, and a question to reuse.
- The `answer-from-corpus` trace footer with a `frame:` tag.

## Related skills

- `answer-from-corpus`: the retrieval protocol this skill runs on. Use it directly for named lookups, survey questions, or when no advice is wanted.
- `matching-references`: check whether the corpus covers a topic at all.
