
# Becker et al., METR RCT on early-2025 AI and developer productivity, Warranting Agent-Built Software Distillation

**Source:** Joel Becker, Nate Rush, Beth Barnes and David Rein, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", Model Evaluation & Threat Research (METR), arXiv:2507.09089v2 [cs.AI], 25 Jul 2025. Licence: CC BY 4.0. Scope: open.

**Applicability gate (Pass G.0): clear yes.** (1) The source answers practitioner questions this axis asks: which claims about a build are demonstrated and which only asserted (here, a developer's sense of how much AI helped against measured time), and whether a run of past successes has become the evidence that a change is safe. (2) Its concepts land in seven of the eight phases, most strongly in Phase 7 (felt speed is not evidence) and Phases 4-6 (what agents leave undone, and where they change things nobody asked for). (3) Its contrarian position, that people who use AI tools overestimate their benefit even after many hours of use, is the axis's second reflex ("it worked first time", "the last ten went fine") stated as a measured gap.

**Phase mapping.** Primary: Phase 7, Warranting the change (perceived against measured effect; records checked against the trace; setting-bound figures). Secondary: Phase 1, Specifying the change (the undocumented repository knowledge AI lacks); Phase 4, Building in the sandbox (low acceptance of AI output, rejected attempts, run rules caught only by recordings); Phase 5, Gating deterministically (autonomous agents omitting docs, lint and key tests; benchmark scores against work in the wild); Phase 6, Reviewing independently (what reading AI code found; unwanted changes elsewhere; bias in briefs that probe a hypothesis). Supporting: Phase 2, Triaging risk (large, mature, complex code as a setting where AI performed worse); Phase 3, Locking the tests (autonomous agents leaving out key tests); Phase 8, Releasing and operating (output counts and felt speed as measures of the harness's effect). Phases 2 and 3 get one row each: the source sorts no change by what it touches, and it does not study test design.

**Transfer caveat.** The trial measured experienced maintainers using AI assistants (mostly Cursor with Claude 3.5/3.7 Sonnet) on their own mature repositories in February-June 2025, with a human reading and editing the AI's output; it did not measure agents building changes that nobody reads line by line, which is this axis's case. Its evidence on fully autonomous agents is preliminary and forthcoming (§4.1, p. 12). Its mechanism analysis is, in the authors' words, speculative and suggestive (§3.3, p. 10). Where this distillation carries a finding into the factory's case, it says the step is its own inference.

## Warranting Agent-Built Software Relevance

This source measures the gap between how much AI seems to help and how much it does, which is the gap a builder signing a warranty on agent-built software has to see across. Sixteen experienced developers forecast that AI would cut their completion time by 24% and afterwards estimated it had cut it by 20%; measured on 246 real tasks randomly assigned to allow or disallow AI, it increased completion time by 19% (Source: Becker et al., METR RCT, Abstract, p. 1; §3.1, pp. 8-9) [AE]. For the warranty, that turns the builder's sense that the agent has been doing well, and the agent's own report of its work, from evidence into a claim to be checked against a record.

The source also names the mechanisms the harness must watch for. AI lacked the undocumented knowledge the maintainers carried, edited in the wrong places, made unwanted changes elsewhere in large codebases, and had under 44% of its generations accepted; even accepted code needed cleaning for conventions and style (App. C.1.3-C.1.5, pp. 19-20) [AE]. Preliminary evidence on fully autonomous agents finds them often implementing an issue's core functionality while omitting documentation, failing linting or style rules and leaving out key tests (§4.1, p. 12) [AR]. And it models a discipline the warranty assessor can borrow: an outcome fixed before the work starts, self-reports checked against recordings, and caution against reading too much into any one subset. Its numbers keep their conditions: one setting, early-2025 tools, 16 developers, self-reported time, a confidence interval read approximately from a figure as about +1% to +39% (Figure 1, p. 2) [AE].

## Key Concepts for Warranting Agent-Built Software

1.  **Perceived versus measured AI speedup.** Developers forecast a 24% speedup and estimated a 20% speedup afterwards while measured time rose 19%; experts forecast 38-39% reductions (Source: Becker et al., METR RCT, §3.1, pp. 8-9) [AE]. Developers' forecasts still predicted relative task time well (correlations 0.64 and 0.59), so the authors read them as calibrated on how long work takes but with expectations of AI's usefulness reversed (§3.1, p. 9) [AR]. The authors conclude that "our results reveal a large disconnect between perceived and actual AI impact on developer productivity" (§1, p. 3) [V].

2.  **Over-optimism drives overuse.** Developers could use AI as much or as little as they liked, yet they were slowed; the authors' explanation is that the optimistic picture they held before and after may have led them to use AI where it hurt (Source: Becker et al., METR RCT, App. C.1.1, p. 18) [AR]. Several developers also said taking part sometimes led them to overuse AI unproductively (App. C.2.1, pp. 20-21) [AE].

3.  **A fixed outcome measure, defined before the treatment.** Earlier field studies counted lines, commits or pull requests, which AI can raise without productivity rising, since code can be more verbose and tasks can be split (Source: Becker et al., METR RCT, §1, p. 1; §1.1, p. 3) [AR]. This study measures time on tasks listed before randomization: "Crucially, the tasks are defined before they are randomized" (§1, p. 2) [V]. On AI-allowed issues developers wrote 47% more code per forecast hour (p = 0.16, not significant), which the authors say need not mean more scope or productivity (App. C.2.3, p. 22) [AE] [AR].

4.  **Implicit repository context.** Developers relied on undocumented knowledge of their codebase that AI lacked; one compared AI to a new contributor that picks the wrong place to edit, another said it missed a backwards-compatibility case only the maintainers knew (Source: Becker et al., METR RCT, App. C.1.5, p. 20) [AE]. The authors hypothesize that size and maturity raise the tacit knowledge experienced developers rely on (App. C.1.5, p. 20) [AR].

5.  **Worse performance in large, complex repositories.** Developers reported AI making unwanted changes in other parts of the code, and edit failures one tied to file size; the repositories averaged about 10 years old and over 1,100,000 lines (Source: Becker et al., METR RCT, App. C.1.3, p. 19) [AE]. The authors hypothesize this is part of why AI helped less here than in earlier, more greenfield studies [AR].

6.  **Low reliability and the cost of rejected attempts.** Developers accepted under 44% of Cursor generations; rejected ones led to re-prompting or reverting, and time spent reviewing, testing or modifying code before rejecting it was lost (Source: Becker et al., METR RCT, App. C.1.4, p. 20) [AE]. One developer spent at least an hour trying an issue with AI before reverting and doing it by hand (App. C.1.4, p. 20) [AE].

7.  **What reading AI code found.** 75% of developers read every line of AI code, 56% often made major changes to clean it up and 100% needed to modify it; one named "more to fix up, in terms of code conventions, code style" (Source: Becker et al., METR RCT, App. C.1.4, p. 20) [V]. About 9% of AI-allowed time went to reviewing and cleaning AI output (App. C.1.4, p. 20) [AE].

8.  **Autonomous agents miss requirements (preliminary).** Forthcoming evidence suggests fully autonomous agents using Claude 3.7 Sonnet can often implement the core of issues in several study repositories, but typically omit documentation, fail linting or style rules and leave out key tests (Source: Becker et al., METR RCT, §4.1, p. 12) [AR]. In the authors' words they "fail to fully satisfy all requirements" (§4.1, p. 12) [V].

9.  **Benchmark scores against work in the wild.** Benchmarks use self-contained tasks scored by algorithmic metrics that miss important capabilities (Source: Becker et al., METR RCT, §1, p. 1) [AR] [BT]. The authors read their slowdown as some evidence that capabilities in the wild may be lower than benchmark results suggest (§4, p. 10) [AR].

10.  **Effects bound to the setting.** Developers were slowed more on issues they knew well and needed few outside resources for, and said AI helped more on unfamiliar work (Source: Becker et al., METR RCT, App. C.1.2, pp. 18-19) [AE]. The authors caution against overgeneralizing: the result is consistent with small greenfield projects or unfamiliar codebases seeing substantial speedup, and they list claims it does not support (§4.1, p. 12; App. B, Table 2, p. 17) [AR].

11.  **Records checked against the trace.** Self-reported time was set against screen recordings: issues with more than a 20% gap between the two, broken recordings or cheating were dropped from the time-use analysis, and recording time gave a 25% slowdown against 24% from self-reports on the same subset (Source: Becker et al., METR RCT, §2.4, p. 8; App. C.3.4, p. 27) [AE]. The recordings showed AI used on 3 of 54 labelled AI-disallowed issues, at least once by accident, and one developer was dropped for widespread cheating (App. C.3.2, p. 26; App. G.6, p. 45) [AE]. Developers' qualitative notes were gathered partly with questions probing the authors' hypotheses, so bias there cannot be ruled out (§2.4, p. 7) [AR].

12.  **Sorting the evidence for each explanation.** Of 21 candidate factors, the authors find evidence that 5 contribute, mixed or unclear evidence for 10 and evidence against 6, and caution against over-indexing on any one piece of evidence because subsets are not powered for multiple comparisons (Source: Becker et al., METR RCT, §3.3, p. 10) [AE] [AR].

## Questions to Ask During Warranting Agent-Built Software

### Phase 1: Specifying the change

| Need | Question | Source-tag |
|---|---|---|
| Surface what the agent cannot see | What does a maintainer of this code know that is written nowhere: compatibility cases, conventions, places that must not change? Is it in the spec, or left for the agent to guess? | App. C.1.5 |
| Name what must not change | Where else in the codebase could an edit land unwanted, and does the spec say those parts are out of bounds? | App. C.1.3 |
| Test the speed assumption | Does the plan, estimate or client quote assume the agent will save time, and what measure on this codebase backs that? | §3.1 |

### Phase 2: Triaging risk

| Need | Question | Source-tag |
|---|---|---|
| Weigh the setting | Does this change land in large, mature, complex code that its maintainers rely on knowing by heart, the setting where AI performed worse? | App. C.1.2; App. C.1.3 |

### Phase 3: Locking the tests

| Need | Question | Source-tag |
|---|---|---|
| Keep key tests out of the agent's hands | Which tests does this change need, and are they written before the run rather than left to an agent that, on preliminary evidence, leaves key tests out? | §4.1 |

### Phase 4: Building in the sandbox

| Need | Question | Source-tag |
|---|---|---|
| Read a report of success | Did the run meet every requirement (docs, lint and style, tests), or only the core behaviour? | §4.1 |
| Keep discarded attempts visible | How many attempts were rejected, re-prompted or reverted, and does the ledger show them or only the last one? | App. C.1.4 |
| Check run rules can be seen | For each run rule (allowed tools, no network, locked files), is there a trace that would show a breach, accidental or not? | App. C.3.2; App. G.6 |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| Gate the commonly missed requirements | Do the gates fail a change that adds behaviour without docs, without new tests, or with lint and style failing? | §4.1 |
| Judge a model or setting swap | Is a change to the model or agent settings justified by a benchmark score or a demo, or by a trial on this codebase's own work with the measure fixed first? | §4, p. 10 |
| Check scope | Do the touched paths match the parts of the code the task named? | App. C.1.3 |

### Phase 6: Reviewing independently

| Need | Question | Source-tag |
|---|---|---|
| Review what reading found | If nobody reads every line, what checks catch the convention and style problems, and the rework, that these developers found by reading? | App. C.1.4 |
| Look outside the named scope | Which hunks touch code the task never named, and why? | App. C.1.3; App. C.1.5 |
| Keep the reviewer's brief neutral | Does the reviewer's or assessor's brief ask what the change does, or does it name the hypothesis it hopes to confirm? | §2.4, p. 7 |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Class impressions | Which claims on the pack about speed, quality or the agent's reliability rest on someone's impression rather than a record? | §3.1; App. C.1.1 |
| Reconcile the records | Do the agent's summary, the ledger and the session trace agree about what was done, and was each ledger entry checked against its trace? | §2.4, p. 8; App. C.3.4 |
| Bound each figure | Does every figure on the pack carry its setting and source, and is any outside figure for AI's effect read as if it applied here? | §4.1; App. B |
| Weigh thin evidence | Does any claim rest on a few runs or one subset? | §3.3 |
| Check the run of successes | Is a streak of good changes being used as the reason to sign this one, or to relax a gate? | App. C.1.1 |

### Phase 8: Releasing and operating

| Need | Question | Source-tag |
|---|---|---|
| Measure the harness's effect | Is the case that agents made delivery faster measured as time or outcome on work defined beforehand, or as lines, commits, pull requests and felt speed? | §1, pp. 1-2; §1.1 |

## What to Look For

| Signal | Diagnosis | Follow-up |
|---|---|---|
| The builder says the agent saved time, and the pack carries that as a benefit | Felt speed; in the trial developers believed they were 20% faster when measured 19% slower (§3.1) [AE] | Mark it asserted; ask for a measure of time or outcome on this codebase, or drop the claim |
| Gates were loosened, or review lightened, because recent changes went well | Over-optimism leading to overuse, the authors' leading explanation for the slowdown (App. C.1.1) [AR] | Restore the gate; make any change to a gate a recorded decision with its evidence |
| The agent reports done; the diff adds behaviour with no docs change, no new tests, or lint not run | The pattern preliminary evidence finds typical of autonomous agents (§4.1) [AR] | Send it back until each is met |
| The diff touches files or modules the task never named | Unwanted changes in other parts of large codebases, as developers reported (App. C.1.3) [AE] | Review those hunks first; require a reason in the spec for each, or revert |
| A legacy behaviour or edge case changed and nothing in the spec mentioned it | Implicit repository context the agent lacked (App. C.1.5) [AE] | Ask the person who knows this code what else the spec leaves unsaid; write it down |
| The session log shows rejected, re-prompted or reverted attempts; the ledger shows only the final one | Low reliability hidden by the ledger; under 44% of generations were accepted in the trial (App. C.1.4) [AE] | Record each discarded attempt and why |
| The ledger and the session trace disagree, or an entry has no linked trace | Self-report unchecked against the record; the trial dropped issues where the two differed by more than 20% (§2.4) [AE] | Reconcile before signing; correct or drop the entry |
| A figure on the pack (a benchmark score, a study's speedup) has no setting | A number read outside its conditions; the authors warn against overgeneralizing their own (§4.1) [AR] | Name the setting; require this change's own run record |

## When to Use This Reference

- Reach for it when the evidence for a change, or for the harness, is someone's sense of how well the agent is doing. It is the corpus's measured account of perception running opposite to measurement.
- Reach for it when deciding what counts as a measure of the harness's effect: it argues for outcomes fixed before the work over output counts.
- Reach for it when an agent works in a large, mature codebase whose maintainers carry knowledge the spec does not, and when a diff reaches beyond what the task named.
- Reach for it when someone justifies a model or agent change by a benchmark score.
- Reach for another source when the question is how strong agent-written tests are (`egashira-testsuitebench-2026`), how agent code fares against tests it did not write (`jimenez-swe-bench`), whether complexity rises over time in agent-assisted projects (`he-cursor-velocity-complexity-2025`), or what a change touches and which gates that makes mandatory (the standards and threat lists). This source does not sort changes by risk, does not study test design, and stops before release.

## Worked Example

*Scenario (operator-authored).* A two-person studio uses a coding agent to add a refund endpoint to a client's eight-year-old billing service, maintained for years by one of the two. The agent runs for forty minutes and reports done. The draft warranty pack reads *done, all checks green, agent saved about a day*, and the builder wants to sign because the last ten changes through the harness went fine. The independent reviewer reads the pack and the session trace, not the whole diff.

*Applying the source.* The reviewer first takes *saved about a day* off the pack's evidence column. It is an impression, and the source measured how far such impressions can run from the clock:

> "Surprisingly, we find that allowing AI actually increases completion time by 19%—AI tooling slowed developers down." (Source: Becker et al., METR RCT, Abstract, p. 1) [V]

The same goes for the run of ten good changes as a reason to sign. The authors' leading explanation for why developers kept using AI where it slowed them is their optimism about it:

> "This overoptimistic view may lead developers to overuse AI assistance, despite its negative effect on their productivity." (Source: Becker et al., METR RCT, App. C.1.1, p. 18) [V]

The trial measured developers using assistants, not unattended agents; carrying its finding to a streak of passed changes is this distillation's inference. A streak is a record of what was checked, not of what the next change does.

Next the reviewer checks the diff's footprint against the task. Besides the refund endpoint, the agent changed a shared currency-rounding helper used by invoicing. The maintainer recognises why it matters: old invoices round the other way, a case written nowhere. The source reports exactly this blind spot:

> "It doesn’t know we need to take care of this weird case of backwards compatibility" (Source: Becker et al., METR RCT, App. C.1.5, p. 20) [V]

Developers in the trial also reported AI making unwanted changes in other parts of large codebases (App. C.1.3, p. 19) [AE]. The reviewer reverts the helper change, and the maintainer adds the rounding rule to the spec as something that must not change.

Then the reviewer checks what preliminary evidence says autonomous agents tend to leave out: documentation, lint and style, key tests (§4.1, p. 12) [AR]. The endpoint has no API docs entry and no test for a partial refund. The session trace shows two earlier attempts the agent reverted; the ledger shows only the third. The reviewer sends the change back with three asks: the docs entry, a partial-refund test written by the maintainer before the rerun, and ledger entries for the discarded attempts with the reason each was dropped. The builder signs once the rerun's trace and ledger agree.

## Anti-patterns This Reference Helps Avoid

- **Felt speed as evidence.** *Signal:* the pack or the builder cites how fast the agent seemed. *Why it fails:* developers believed they were 20% faster while measured 19% slower, even after many hours with the tools (§3.1; §4, p. 10) [AE] [AR]. *Instead:* record time or outcome against work defined beforehand, or leave speed off the pack.
- **Success streaks that loosen the harness.** *Signal:* fewer gates or lighter review because the agent "has been fine". *Why it fails:* optimism about AI is the source's leading explanation for overuse (App. C.1.1) [AR]. *Instead:* change a gate only by a recorded decision with its evidence.
- **Core behaviour taken for done.** *Signal:* the feature works and the change is called complete. *Why it fails:* preliminary evidence finds autonomous agents typically omit docs, fail lint or style and leave out key tests (§4.1) [AR]. *Instead:* gate each of those explicitly.
- **Trusting the agent with what nobody wrote down.** *Signal:* the spec omits the codebase's quirks because "the agent will read the code". *Why it fails:* AI lacked the undocumented knowledge maintainers relied on (App. C.1.5) [AE]. *Instead:* have the person who knows the code name what must not change.
- **A ledger of winners.** *Signal:* only the final attempt reaches the ledger. *Why it fails:* under 44% of generations were accepted, and rejected attempts cost time (App. C.1.4) [AE]; a ledger without them hides how reliable the agent was. *Instead:* log each discarded attempt and why.
- **Output counts as productivity.** *Signal:* the harness's success reported as lines, commits or pull requests. *Why it fails:* AI can move those without productivity rising (§1, p. 1) [AR]. *Instead:* measure outcomes fixed before the work.
- **Borrowed numbers.** *Signal:* a benchmark score or an outside study's speedup offered as the reason to trust a change. *Why it fails:* the authors read their own result as evidence that capabilities in the wild may be lower than benchmarks suggest, and warn against overgeneralizing it: "We caution readers against overgeneralizing on the basis of our results." (§4.1, p. 12) [V]. *Instead:* require this change's own run record on this codebase.
- **A leading brief.** *Signal:* the reviewer is told what to confirm. *Why it fails:* the authors could not rule out bias in evidence gathered with questions that probed their hypotheses (§2.4, p. 7) [AR]. *Instead:* ask the reviewer what the change does.

## Integration with Other References

| Reference | Relationship |
|---|---|
| `dora-ai-assisted-swdev-2025` | DORA cites this study (slowed 19%, believed faster) among signs the industry is early in understanding AI's effects [BT] (pp. 35, 48). Its own survey finds more than 80% perceive AI raised their productivity (p. 30) [AE], and its measurement chapter warns that self-reports carry recall and social-desirability bias and that logs-based metrics are not objective (p. 91) [AP] [AR]. This source is the measured counterweight to self-reported gains; DORA supplies the measurement guidance for acting on it |
| `he-cursor-velocity-complexity-2025` | He et al. cite this study for over-optimism and no speedup [BT] (§1, p. 2) and measure velocity as commits and lines added (§3.2) [AP], finding gains that fade while complexity rises and stays. This source warns that such output measures can rise without productivity rising. Together: neither felt speed nor output counts warrant a change, and a velocity gain can carry a lasting cost |
| `jimenez-swe-bench` | This source cites SWE-bench on environment complexity [BT] (App. C.1.3). SWE-bench's authors say execution-based testing alone is insufficient to guarantee reliable generations, and that performance differs heavily across repositories (§7; App. C.2). With this source's reading that in-the-wild capability may be lower than benchmarks suggest (§4), both argue that a benchmark score is not a warrant for this codebase |
| `egashira-testsuitebench-2026` | This source's preliminary evidence has autonomous agents leaving out key tests (§4.1); TestSuiteBench measures that the tests agents do write are valid but weak. Together they say agent test evidence is thin in both quantity and strength |
| `microsoft-code-with-engineering-playbook` | Its Definition of Done lists documentation updated, unit tests written and passing, and code review complete, and it automates linting so human review can go to logic ("Definition of Done"; code-review process guidance) [AP]. Those are the items this source's preliminary evidence finds autonomous agents leaving out, so the playbook's checklist is a ready gate for them |
| `uk-duck-book-qa-of-code` | The Duck Book relays this study's finding and its five explanations [BT], and warns that an AI-assisted programmer may become a full-time reviewer of the AI's output, with total task time unchanged or higher [AP] (book/generative_ai.md, "Vibe check failed"). This source carries the measurement behind that warning |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The six earlier studies of AI speedup the paper compares itself with, the benchmark literature it critiques, the economics and forecasting literature, and the statistical methods it cites are relayed as the authors cite them and not held in this corpus [BT]. Of the works the paper cites, only SWE-bench is held here (`jimenez-swe-bench`). The evidence on fully autonomous agents (§4.1) is the authors' own forthcoming work, described but not presented in this paper [AR].

**Named limits of the source.** The authors list what the result does not show: that AI fails to speed up most developers, people outside software, near-future AI in this setting, better uses of current AI here, developers with far more AI experience, or these developers on every task (App. B, Table 2, p. 17) [AR]. The setting is 16 experienced maintainers on mature repositories averaging over 1,100,000 lines, February-June 2025 tools, self-reported time, and issues smaller than usual (§2.1; App. C.2.2) [AE]. The mechanism analysis is speculative and not powered for multiple comparisons (§3.3) [AR]. The confidence interval for the 19% is read approximately from Figure 1 (about +1% to +39%), and the caption does not state its level (Figure 1, p. 2) [AE]. The trial studied humans using AI assistants, not agents building unread changes; every step from its findings to the factory's case is marked here as this distillation's inference.

**Evidence-marker continuity.** Measured results carry `[AE]` as in the deep reference; the authors' readings and hypotheses (over-optimism as the cause, implicit context, the benchmark gap, the preliminary agent evidence) carry `[AR]`. Verbatim passages are copied from the deep reference's audited `[V]` blocks (Abstract, p. 1; §1, p. 2; §1, p. 3; App. C.1.1, p. 18; App. C.1.4, p. 20; App. C.1.5, p. 20; §4.1, p. 12, twice); none was re-extracted from the tape. The §4 benchmark-gap sentence and the §3.3 caution against over-indexing are paraphrased rather than quoted. The What-to-Look-For row on borrowed figures paraphrases the §4.1 caution and points to Key Concept 10. Cross-references in the integration table cite the sibling deep references' own sections and markers.

## Runtime triggers this source addresses

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The agent is asked to "build X like Y" with no statement of what must not change (Phase 1) | Developers reported AI making unwanted changes in other parts of large codebases, and missing a backwards-compatibility case only the maintainers knew (App. C.1.3; App. C.1.5) [AE] | Ask the person who knows this code what must stay as it is, and put it in the spec. The agent can't respect a constraint nobody wrote down. |
| The builder says "the agent will figure out the details" (Phase 1) | AI lacked the undocumented repository knowledge experienced developers relied on, and picked the wrong places to edit (App. C.1.5) [AE] | The details only the maintainer knows are the ones the agent will get wrong. Write them down before the build. |
| The change is business-critical, or complex enough that nobody can predict its effects (Phase 2) | AI performed worse in large, complex repositories, with unwanted changes elsewhere and edit failures (App. C.1.3) [AE]; the authors hypothesize size and maturity raise tacit knowledge (App. C.1.5) [AR] | Complex, mature code is where the agent is least reliable. Raise the review on it, starting with anything outside the named scope. |
| The agent runs for an hour unattended and reports success (Phase 4) | Preliminary evidence: autonomous agents often implement the core but omit docs, fail lint or style, and leave out key tests (§4.1) [AR] | Working core behaviour isn't done. Check docs, lint and style, and the key tests before accepting the report. |
| The builder approves because reading the diff is too slow (Phase 6) | Developers who read AI code found convention and style problems and needed to modify all of it; 56% often made major changes (App. C.1.4) [AE] | If nobody reads it, something else must catch what reading caught. Name the check that covers conventions, style and rework, or read the parts it doesn't cover. |
| The builder signs because the last ten went fine (Phase 7) | Developers believed AI sped them up by 20% when it slowed them by 19%, and the authors' leading explanation for overuse is that optimism (§3.1; App. C.1.1) [AE] [AR] | Feeling it's been fine is an impression, and impressions of AI's help ran the wrong way in the trial. Sign on this change's record, not the streak. |

## Trigger extensions surfaced by this source

| Phase | Trigger (what the practitioner notices) | Response (grounded in this source) |
|---|---|---|
| 1 | A plan, estimate or client quote assumes the agent will cut the time, with no measure on this codebase | Treat the figure as a forecast to test: developers forecast a 24% cut and took 19% longer (§3.1) [AE] |
| 3 | The plan leaves the agent to write the key tests for its own build | Write the key tests before the run, outside the agent: preliminary evidence finds autonomous agents leave key tests out (§4.1) [AR]. Locking them before the build is this distillation's inference |
| 4 | The session log shows attempts rejected, re-prompted or reverted, and only the final attempt reaches the ledger | Record each discarded attempt and why: under 44% of generations were accepted, and rejected ones cost time (App. C.1.4) [AE] |
| 4 | A run rule (no network, allowed tools only, locked tests) has no trace that would show a breach | Add the trace before relying on the rule: screen recordings caught AI used where it was disallowed, at least once by accident (App. C.3.2; App. G.6) [AE] |
| 5 | The agent marks the task done and the diff adds behaviour with no new tests or docs, or lint and style were not run | Block until each is met: preliminary evidence finds these the typical shortfalls of autonomous agents (§4.1) [AR] |
| 5 | A model or agent setting is swapped on a benchmark score, a leaderboard or a demo, and the gates stay as they were | Trial old and new on this codebase's own work with the measure fixed first: the authors read their result as evidence capabilities in the wild may be lower than benchmarks suggest (§4) [AR] |
| 6 | The diff touches files or modules the task never named | Review those hunks first and require a reason in the spec for each, or revert: developers reported unwanted changes in other parts of large codebases (App. C.1.3) [AE] |
| 6 | The reviewer's or assessor's brief names the hypothesis it is meant to check | Rewrite the brief to ask what the change does: the authors could not rule out bias in evidence gathered with probing questions (§2.4) [AR] |
| 7 | The pack's evidence for speed or quality is an impression, the builder's or the agent's, with no record behind it | Mark it asserted and send it back for a record or a measure: estimated 20% speedup against measured 19% slowdown (§3.1) [AE] |
| 7 | The agent's summary, the ledger and the session trace disagree, or a ledger entry has no linked trace | Reconcile before signing and correct or drop the entry: the trial checked self-reported time against recordings and set aside issues where they differed by more than 20% (§2.4; App. C.3.4) [AE] |
| 7 | A figure on the pack has no setting: an outside figure for AI's effect, or a claim resting on a few runs | Name the figure's setting and size: the authors caution against overgeneralizing their result and against over-indexing on any subset (§4.1; §3.3) [AR] |
| 8 | The case that agents made delivery faster is reported as output (lines, commits, pull requests) or as felt speed | Measure time or outcome on work defined before the change: output counts can rise without productivity, and felt speed ran opposite to measured time (§1; §3.1) [AR] [AE] |
