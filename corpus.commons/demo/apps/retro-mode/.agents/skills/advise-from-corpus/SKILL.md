---
name: advise-from-corpus
description: Advising protocol on top of answer-from-corpus. Before answering a how-to or improvement question, checks whether it's the question worth answering (does the asker's structure, situation or goal even support the answer they're asking for?), names the one fact the advice hinges on, and asks grounded framing questions round by round, reading each reply as evidence, until it has that fact or the user opts out; then answers through answer-from-corpus with what it learned, and closes by teaching the check it ran. Use when someone asks how to improve, adopt or roll out a practice ("how do I improve my user stories? I hear to write them vertically?"), or asks how to get people to change. Use answer-from-corpus instead for named lookups, survey questions, or "just answer".
argument-hint: "<question>"
---

# Advise from corpus

`answer-from-corpus` answers the question as asked. This skill checks the question first. Its canonical case:

> "How do I improve my user stories? I hear to write them vertically?"

A good answer about vertical slicing is useless to someone whose teams are split into a front-end team and a back-end team, each with its own backlog, because no team can finish a vertical slice. The advice this person needs starts with a question back: *can one of your teams take a story from interface to database to done?*

The skill does three things in order:
1. **Frame.** It reads the question for what it assumes and names the constraint: the one fact that, if it went the other way, would change the advice most. It asks grounded framing questions and reads each reply as evidence, asking again in a new form when a reply leaves the constraint open, until it knows that fact or the user opts out.
2. **Answer.** It hands retrieval to `answer-from-corpus`, with what the framing established.
3. **Teach back.** It names the check it ran and where it came from, so the user can ask it themselves next time.

It never holds the answer hostage. A user who says "just answer" gets the answer, stated with the condition under which it holds.

## Procedure

**Retrieval belongs to `answer-from-corpus`.** Every read in this skill (framing sources, the answer) follows that skill's run mode, lens check, protocols, quote checking and grounding discipline. In the project it routes through the concept index to references. In an app it reads the distillations the app ships. This skill adds the framing conversation and the teach-back, and doesn't restate the retrieval rules.

### Step 1: Decide whether to frame

Classify the query shape the way `answer-from-corpus` does. Then:

- **Named lookup** ("what does the Scrum Guide say about the Sprint Goal"): don't frame. Run `answer-from-corpus` and stop.
- **The user asks for the answer only** ("just answer", "no questions"): don't ask. Run the framing read in Step 2, answer with the condition of validity from Step 5, and skip the questions.
- **A crisis still unfolding** ("prod is down", "we're losing the account today"): don't frame. Act first; offer framing once things are stable.
- **Everything else**, diagnostic or synthesis: frame. The framing read runs whether or not a lens applies.

### Step 2: Read the question for what it assumes

**Pin down the question and the seat first.** Short questions hide their meaning in a verb or a possessive. "How do I start my team?" can mean forming a new team, launching one that's already staffed, or starting a practice (Scrum, say) with an existing team, and "my" can belong to its leader, one of its members or its manager. List the readings the wording allows, and note who is asking: their role, what they can decide, and who decides over them. When the readings would lead to different advice, the question's own meaning is a missing fact like any other.

Then run the five checks against the wording. They're the same in every corpus:

1. **Real vs presenting problem.** What is this question standing in for, and what is the organisation's design contributing to it? When the question names people as the cause ("they won't commit"), treat their reluctance as information: ask what it protects before asking how to overcome it.
2. **Ends vs means.** What is the practice or solution for, and is it failing at that or at something else?
3. **Leverage level.** Which layer does the question act on: a practice or a number; the design (structure, processes, rewards, people); the strategy; the goals the design optimises for; or the leader's paradigm and read of the situation? Is a higher layer within the asker's reach, and what do they have influence over rather than control? When leaders have handed change down to others to carry, the people carrying it usually reach only the lower layers; say so when that's the case.
4. **Context fit.** Can the setting the asker works in produce the answer being asked for? Two parts: its structure (can the unit that's meant to do this finish it without handing off?) and its type of problem (is there a known answer, or does one have to emerge by trying; is this work someone can be handed, or work that needs the people who own it in the room?). One sign the setting treats emergent work as plannable: it still demands fixed delivery dates for work with no known answer.
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

**Name the constraint.** Rank the missing facts by how far the advice would swing if each went the other way. The top one is the constraint: the fact the whole answer hinges on. For the user-stories case it's whether one team can finish a slice; whether the stories are too big only adjusts the advice. Then write two or three working reads of the asker's situation that differ on the constraint ("a developer on a team that ships end to end", "a developer on a front-end team that hands off to a back-end team"). The framing questions exist to tell these apart.

**Ground each check.** Route the lead checks through `answer-from-corpus` retrieval. In project mode that's the concept index. In app mode it's the routed task-index: start with its framing phase when it has one (`decision-making` "Phase 1: Framing"), then match the missing fact against the `need` and `when` text of rows in every phase, since some axes carry their framing rows elsewhere (`software-business` has no framing phase; its team-structure rows sit in Phases 3 and 4). Read at most two sources per check. A framing question may carry a claim about *why* it matters only when a source you read supports that claim.

### Step 3: Ask a framing round

Ask **at most two** framing questions, then stop and wait for the user. The first question goes to the constraint. Each question:
- asks for the missing fact in the user's terms, not the framework's ("Do your teams each own a front-end or back-end layer, or can one team build a whole feature?", not "What is your org topology?");
- is built to tell the working reads apart: a concrete either/or, or a short choice drawn from the reads, gets a sharper reply than an open "what is…";
- carries one line on why the answer changes the advice, with its source named;
- is easy to answer in a sentence.

End the round with the way out: the user can answer, or say "just answer" and get the answer with its conditions stated.

### Step 4: Read the reply as evidence

Before answering, read the reply three ways:

1. **What it answers.** Which questions it settles, and which working reads it rules out.
2. **What it leaves open.** A question the reply skips, half-answers or answers with something else is still open. When the open question is the constraint, it gets asked again.
3. **What it shows without being asked.** Read the wording for the asker's role and authority ("what my product owner tells me" places the asker under a product owner who decides the work), their vocabulary, what they take as given, and what's missing. A reply that restates the premise is a finding about a check, not an answer to it: "our purpose is to build what we're told" answers ends vs means by showing the team's purpose is a means. Record it as a finding and carry it into the answer.

Update the working reads: drop the ones the reply rules out, and name the words that support the rest.

**Gate: answer only when the constraint is known.** It's known when the user stated it, or when you inferred it and they confirmed the inference. Until then, run another round:

- Open with the working read, in one or two sentences and in the user's words, so they can correct it: "From what you've said, you're one of the developers and the product owner decides what gets built. Is that right?"
- Ask at most two questions. Re-ask an open constraint question in a new, more concrete form (a short choice, an example from their own words), never word for word. Drop any question whose answer would no longer change the advice.
- Keep the way out.

**Stop asking** when the constraint is known, when the user opts out, or after three rounds. After the third round, answer by branch: give the advice for each working read still standing, say which one the evidence favours and which words point to it, and make the first line of the answer the fact that would settle it.

Each round has to narrow the working reads. If the next round wouldn't, answer now with the condition of validity stated.

If a check has no grounding source in the corpus, you may still ask for the missing fact, but drop the *why* line, and record `frame: ungrounded (<check>)` in the trace.

### Step 5: Answer with what they said

Fold the user's replies and the Step 4 findings into the question and run `answer-from-corpus` on it. Add the replies, the findings and the fired checks to its sub-claim list so retrieval covers them. Then shape the answer:

1. **Open with the working read and the constraint.** One or two sentences: the situation as you now understand it, and the fact the advice hinges on, marked as stated by the user or inferred and confirmed.
2. **Answer the question they asked, fitted to their situation.** If their structure supports the practice, give the practice. If it doesn't, say so plainly and say what the practice would need.
3. **State the condition of validity** in one sentence: the fact the answer rests on ("This holds if one team can take a story from interface to database to done").
4. **Name the reachable step.** When the real fix sits above what the asker can change (team structure, a leader's goals), give the step within their reach alongside it, and who would have to act on the rest. A process change that the rest of the design can't support is the common case; the model question is "This looks like a process change. Does the rest of the design support it? If not, who has the authority to change that?" Before pointing the asker upward, check the contract:
   - Can the asker, or you, reach the people who own that decision, and will they hear a view that differs from their own?
   - For a change to roles or structure, is there sponsorship to handle the objections it will meet and to help people into new roles?

   If not, say so plainly. Give the local step, and say that its ceiling is set by the layer above, so the asker knows what the local step can and can't buy.
5. **Offer at most one reframe the replies surfaced,** as a question the user owns, with its source. Don't add one for the sake of it.

If the user said "just answer", skip the replies and lead with the condition of validity instead: "If one of your teams can finish a slice end to end, here's how… If not, vertical stories will stall, because…"

### Step 6: Teach back

Close with three short lines:
- **The check that ran**, in plain words ("Before improving a practice, I checked whether your team structure could support it").
- **Where it comes from**: the source you read.
- **The question to ask yourself next time**, phrased so the user could use it on a different practice ("Can the team that's meant to do this actually finish it without handing off?").

Take the question from the check that ran. The stock forms:
- Is there a known answer here, or does one have to emerge by trying?
- What do I have influence over, rather than control?
- What is the design contributing to the problem as it was presented?
- Can this be handed to someone, or does it need the people who own it in the room?
- This looks like a process change: does the rest of the design support it, and if not, who can change that?
- Which layer am I acting on, and is a higher one within reach?
- Am I contracted to ask the higher questions, and can I reach the people who own the answer?

### Step 7: Offer to keep going

One line, once: offer to go further on the reframe (what it would take to change the structure, who owns that decision). Only continue if the user takes it up. When they do, run the loop again from Step 2 on the new question.

### Trace footer

Append the `answer-from-corpus` trace to every turn this skill produces, including a framing round that stops to wait for replies, with a `frame:` tag added to its bracket:

- `frame: <check(s)>, rounds: <n>, asked: <n>, constraint: <fact> (stated | inferred+confirmed | open)` when framing questions were asked; on a turn that waits for replies, `constraint: <fact> (asking)`;
- `frame: <check(s)>, asked: 0 (just answer), constraint: <fact> (open)` when the user opted out;
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

**Step 4.** The reply settles the constraint (separate teams with separate backlogs: no team can finish a slice) and adds a finding (stories are "done" but nothing ships). The gate is open.

**Step 5.** The answer says plainly that rewriting stories vertically won't fix this, because no single team can finish one. It explains why ("done" stories that don't ship are what hand-offs between teams produce). It states the condition of validity: vertical slicing starts working once one team can finish a slice. It names the reachable step that the sources support, and says who owns the structural decision.

**Step 6, the teach-back:**
> Before advising on a practice, I checked whether your team structure could support it (context fit, from the Org Topologies primer). Next time, ask: can the team that's meant to do this finish it without handing off?

```
---
*Trace [Diagnostic, mode: project, frame: context-fit + ends-vs-means, rounds: 1, asked: 2, constraint: one team can finish a slice (stated), lens: none, corpus: demo]: framing via concept-index → org-topologies-primer-2025 (context fit), open-practice-library + approach-perfect-field-guide (slicing) → user replies folded into sub-claims → answer-from-corpus Protocol D*
```

The specific sources and quotes in a real run come from what the run reads. This example shows the shape, not the citations.

## Worked example: a reply that leaves the constraint open

**User:** How do I start my team?

**Step 2.** "Start" allows three readings: forming a new team, launching one that's already staffed, or starting a practice with an existing team. "My" could belong to the leader or a member. The constraint is what the team is for and whether it can finish that work itself: a team that can't finish its own work needs a different start from one that can. Round one asks what the team is meant to deliver and whether it can finish that alone, and whether this is a group meeting for the first time.

**User:** My purpose is to develop what my product owner tells me to develop.

**Step 4.** The reply answers *who decides the work* and nothing else. Read three ways:
- *Answers:* the product owner sets the work.
- *Leaves open:* whether the team can finish its work alone (the constraint), and whether the group is new.
- *Shows:* the asker is a developer under a product owner, not the team's manager, so "start my team" probably means starting a way of working from inside the team. The stated purpose is a means (how work arrives), not an end (a result for someone): a finding on ends vs means.

The constraint is still open, so the gate stays shut. Round two opens with the working read and re-asks the constraint in a concrete form:

> From what you've said, you're one of the developers and your product owner decides what gets built. Is that right?
>
> 1. When the product owner hands you something, can your team take it all the way to something a customer can use? Or does part of it go to another team (design, back end, testing, operations) before it ships?
> 2. Has someone asked you to get this team going, or are you starting it because nobody else is?
>
> Or say "just answer" and I'll answer for each case.

If the reply settles the first question, answer. If round three still leaves it open, answer by branch, lead with the fact that would settle it, and say which branch the evidence favours.

```
---
*Trace [Diagnostic, mode: project, frame: ends-vs-means + context-fit, rounds: 2, asked: 4, constraint: team can finish its own work (asking), lens: none, corpus: aarbuddy]: round 1 → reply read: PO sets the work (answered), finish-alone and new-group (open), asker is a developer and purpose is a means (shown) → round 2 re-asks the constraint*
```

## Discipline

- **Answer the question they asked, every time.** Framing adds to the answer. It never replaces it or stalls it.
- **At most two questions per round, at most three rounds before the first answer, and every round narrows.** Persistence is for the constraint; a round that wouldn't change the advice doesn't run.
- **Read every reply as evidence.** Settle what it answers, re-ask what it leaves open, and use what it shows without being asked. A partial reply never triggers the answer on its own.
- **Mark inferences as inferences.** Say what you inferred and from which words, and check it with the user before the answer rests on it.
- **Ask in the user's terms.** The framework name goes in the teach-back, not in the question.
- **No uncited claim about why a question matters.** Retrieval grounding rules from `answer-from-corpus` apply to the framing as much as to the answer.
- **Don't ask for what they've already told you.** Read the conversation first.
- **The user owns the reframe.** Offer it as a question. Don't rewrite their goal for them.

## Inputs

- A how-to, improvement, adoption or "how do I get people to…" question in plain language.
- Optional: "just answer" (skip the questions) and `--corpus {slug}` (passed through to `answer-from-corpus`).

## Outputs

- Framing rounds: at most two grounded questions each, up to three rounds, each after the first opening with the working read, all with a way out.
- When the constraint is known, after the third round, or when the user opts out: an answer that opens with the working read and the constraint, fitted to their situation, with its condition of validity, the reachable step, and at most one reframe.
- A teach-back: the check, its source, and a question to reuse.
- The `answer-from-corpus` trace footer with a `frame:` tag.

## Related skills

- `answer-from-corpus`: the retrieval protocol this skill runs on. Use it directly for named lookups, survey questions, or when no advice is wanted.
- `matching-references`: check whether the corpus covers a topic at all.
