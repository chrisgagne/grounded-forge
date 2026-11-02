# Keyword match: does Gemini Notebook's retrieval need the sources' words? (pre-registration)

*Written and committed on 31 October 2026, before any arm ran. The results go in this folder's README; this file isn't edited after the first run except to fix a typo, and any such fix is named in the README.*

## The hypothesis

Gemini Notebook's retrieval accuracy depends on lexical overlap between the question and the target passage; grounded-forge's concept and topic routing doesn't.

It comes from the [October private round](../2026-10-22-gemini-notebook-private-corpus/). There, Gemini tied grounded-forge where the question used the sources' own vocabulary (Q3, Q5, Q6). Where it shared no words with the sources (Q2), Gemini's quotations were real but every citation marker pointed at a chunk from another book that shared a word with the question. That round couldn't say whether the wording or the chunk size (the notebook held level-sized bundles and whole books) was the cause. This round separates the two.

## Targets

Ten passages in the public demo corpus, one per source, each carrying one concept that `concept-index.json` files under a topic. Line numbers are in `corpus.commons/demo/sources/converted/{slug}.md`, as `grep -n` counts them. Full records, with the key elements a scorer checks, are in [`targets.json`](targets.json).

| ID | Source | Concept (index row) | Topics | Passage | Section scored against |
|---|---|---|---|---|---|
| K01 | `caib-report-vol1` | Normalization of Deviance | t079, t084 | 14107–14114 | 6.1 A History of Foam Anomalies, 12966–14194 |
| K02 | `mcdp1-warfighting` | Friction | t056 | 277–284 | Ch 1, Friction, 276–331 |
| K03 | `lfuo-learning-review-guide-2024` | Counterfactual Reasoning | t002, t036 | 3041–3056 | Final FLA Considerations, 3020–3077 |
| K04 | `scrum-guide-2020` | Definition of Done | t008 | 616–624 | Commitment: Definition of Done, 613–636 |
| K05 | `org-topologies-primer-2025` | Work Mandate | t052, t053 | 505–511 | Vertical Dimension: Work Mandate, 497–588 |
| K06 | `doe-hpi-handbook-vol1` | Paper Plant | t004, t078 | 1264–1269 | Ch 1, The Work Place, 1262–1284 |
| K07 | `openstax-psychology-2e` | Diathesis-Stress Model | t034 | 26217–26228 | 15.3, The Diathesis-Stress Model, 26208–26229 |
| K08 | `openstax-organizational-behavior` | Equity Theory | t039 | 10326–10345 | 7.3, Equity Theory, 10324–10518 |
| K09 | `ssdl-systems-thinking-foundations` | System Archetypes | t023 | 1169–1173 | Brief 1.07, Archetype #1: Fixes that fail, 1163–1196 |
| K10 | `liberating-structures-handbook` | Agreement/Uncertainty Matrix | t025, t027, t037 | 1626–1634 | Agreement/Uncertainty Matrix, 1624–1659 |

Answer keys, one line each:

- **K01.** Normalization of deviance (Vaughan): accepting events that aren't supposed to happen until the deviation is viewed as normal and acceptable; NASA kept flying with foam losses on that basis.
- **K02.** Friction: the countless factors that make the apparently easy so difficult (Clausewitz); it resists all action, saps energy, and makes the simple difficult.
- **K03.** Avoid counterfactual arguments ("if this person had done X, the accident would not have occurred"); learn why people did what they did, why it made sense to them at the time.
- **K04.** The Definition of Done: a formal description of the state of the Increment when it meets the product's quality measures; it gives everyone a shared understanding, and an item that doesn't meet it can't be released or presented at the Sprint Review.
- **K05.** Scope of work mandate: the vertical axis of the Org Topologies map, the scope of work given to a unit, from tasks at the bottom up to overlapping, co-owned scopes (team-of-teams) at the top; the higher, the bigger its field of play.
- **K06.** The paper plant: the aggregate of all the documentation that controls the configuration of the physical plant; flaws in it can lie dormant and lead to bad outcomes or injury in the physical plant.
- **K07.** The diathesis-stress model: people with an underlying predisposition (diathesis) are more likely to develop a disorder when faced with adverse events (stress); both are necessary, and the more predisposition, the less stress is needed.
- **K08.** Equity theory: motivation depends on our outcomes for our inputs compared with others' outcomes and inputs; perceived unfairness (underreward) lowers satisfaction and effort.
- **K09.** The "fixes that fail" archetype: a short-term fix solves the problem in the short run but generates unintended consequences that make the original problem worse.
- **K10.** The Agreement/Uncertainty Matrix (Stacey): two axes, how certain a group is about what's going on and how far it agrees about what to do, separating simple, complicated and complex situations.

Other demo sources that carry the same concept by name are listed per target in `targets.json` (`alt_sources`): K04 (three), K06 (DOE-HPI vol 2), K08 (two OpenStax books), K09 (Barbrook-Johnson). A citation to one of them is right concept, wrong source, and is counted apart from a citation to an unrelated book.

The ten cover canonical material the models know well (K02, K04, K07, K08, K09) and material that is thin in training or the corpus's own (K03, K05, K06, K10, and K01's foam history). They also span file size, which the chunk control uses: four target sources are under 12,000 words (K04, K05, K09, K10), six are over 20,000 (K01 167,000; K07 343,000; K08 296,000).

## Questions

Two per target, in [`questions.json`](questions.json):

- **(A)** in the source's own terms: the concept's name and the author's phrase.
- **(B)** in a user's situation words, with no content word shared with the passage.

| ID | (A) source's terms | (B) situation words |
|---|---|---|
| K01 | What is the normalization of deviance, and how did it show up in NASA's decisions about foam loss? | Our pipeline throws the same warning on every deploy. Years ago it scared us; now nobody blinks, since nothing ever broke. How does a team drift into treating a red flag as fine? |
| K02 | What is friction in war, and why does it make the simple difficult? | Our office relocation looked straightforward on paper, yet each step turned into a slog: a late truck, a missing key, rain, a nervous crew. Is there a name for that drag that turns plain jobs hard? |
| K03 | Why should a learning review avoid counterfactual arguments? | Writing up last month's crane incident, my reviewers keep saying "had Sam checked the brake, we'd be fine." Is that a helpful way to frame the write-up? |
| K04 | What is the Definition of Done, and what happens to a Product Backlog item that doesn't meet it? | Our developers call a ticket finished when the code compiles on their laptop, then testers find it's half-baked. What should a group agree on so "finished" means one thing? |
| K05 | What is the scope of work mandate on the vertical axis of the Org Topologies map? | Our squads get handed tiny tickets like "tweak this button". How do I describe how far up the ladder of responsibility a squad's remit reaches, from chores to an entire product? |
| K06 | What is the paper plant, and how can flaws in it lead to error in the physical plant? | An engineer edited a drawing and a manual years ago; the mistake sat unnoticed until a technician followed the drawing and got hurt. Is there a name for the set of records that mistakes like that live in? |
| K07 | What does the diathesis-stress model say about how a psychological disorder develops? | Brothers Tom and Ian went through their parents' awful divorce; Tom sank into deep depression and Ian coped. Why might a rough patch tip one sibling over but not the other? |
| K08 | What does equity theory say about how our outcomes and inputs, compared with other people's, affect motivation? | My colleague learned that a recently recruited guy at her desk earns a bigger salary than she does, and she's lost all drive. What explains that? |
| K09 | What is the "fixes that fail" system archetype? | We hired temps to clear a backlog of customer complaints; the temps gave sloppy answers, which caused even more complaints. What pattern is this? |
| K10 | What are the two axes of the Agreement/Uncertainty Matrix? | Our board can't settle on a strategy, and nobody knows how the market will react. Is there a tool that plots issues by how sure we are of the facts and how much we see eye to eye? |

### The overlap check

[`check_overlap.py`](check_overlap.py) lists the content words each question shares with its passage. Matching is loose on purpose, so it errs towards finding overlap: function words are dropped and every other word counts; common suffixes are stripped; and two words match when their stems are equal or when both run to five letters or more and share the first five ("deviation" matches "deviance"). A (B) question passes only when the list is empty. All ten pass; the output, with each passage printed in full, is [`check-output.txt`](check-output.txt).

The script also lists, for information, the words each question shares with the whole target section. That list gates nothing: a section of hundreds of lines shares a few words with almost any question (K01B shares seven with its 1,229-line section, "warning" and "team" among them). It's there so a hit or miss on the section can be read against it.

## Arms

All three get the bare question, exactly as in `questions.json`, with no rules paragraph and nothing else.

- **G-whole, Gemini Notebook Pro.** A new notebook holding the 31 demo sources, one file each: the converted Markdown, except `doe-hpi-handbook-vol2`, whose original PDF is the one source redistributed as a single file. (Open Kanban's and the Open Practice Library's originals are folders of many pages whose joined text is the converted file; the SSDL originals cover three of its five briefs, not the target's.) Built by [`split_sources.py`](split_sources.py) into `whole/`. Default chat settings and response length, no custom instructions, no web or Discover sources.
- **G-split, the chunk control.** A second notebook, the same except that the six target sources over 20,000 words go in as one file per chapter: 99 files. The cuts are fixed in `split_sources.py` (`PLAN`), at each chapter's first heading. The four small target sources go in whole, as they already are chapter-sized. Only the (B) questions run here.
- **GF, grounded-forge project mode.** [`run_gf.py`](run_gf.py): an isolated `claude -p` run per question in a fresh copy of the demo corpus's reference tier (references, converted sources, concept and reference indexes, lens index and specs) with the `answer-from-corpus` skill and a two-line CLAUDE.md that points at it. No distillations, task indexes or apps. Opus 5.5 at effort high, project and local settings only, auto-memory off, an empty MCP config, tools Read, Grep, Glob, Write, Skill and Agent, no Bash and no web. Without Bash, the skill checks quotations by searching the converted sources, as it says to.

Two runs per question per arm: 20 GF answers ×2, 20 G-whole answers ×2, 10 G-split answers ×2.

**Between Gemini questions,** as the October round learned: delete the chat history, untick any saved note (a saved note becomes a ticked source), and delete any Studio file (they survive "Delete chat history" and are read in later chats). Each question is a fresh chat.

**Capture per Gemini answer:** the answer through the copy button; and for each citation marker, the source name and the opening words of the passage it highlights, read live in the notebook, since the copy keeps the `[n]` but not what it points to. Chris drives the notebook, or Claude drives it in his browser with his say-so; either way, what's captured is Gemini's own output.

## Scoring

Each answer gets five scores. The first is the hypothesis's.

1. **Key citation on target (yes/no).** Find the first sentence that states the answer key (all its `key_elements`). For Gemini, that sentence's citation markers; for grounded-forge, the source the sentence credits, with any quotation or locator it gives. **Yes** when a citation points at the target source *and* at material inside the target section. For Gemini that's mechanical: the passage a marker highlights is located with [`locate.py`](locate.py) and its line checked against the section range. For grounded-forge, the quotation or locator (chapter, section, page) given for the claim must fall inside the section; a claim credited to the right source with no quotation or locator scores **source only**, which counts as no here and yes under 2. An answer that never states the key scores no.
2. **Key claim on target source (yes/no):** as 1, ignoring the section.
3. **Wrong-book citations on the key claim:** markers or credits on that sentence that point at a source that is neither the target nor one of its `alt_sources`.
4. **Answer-key hit (yes/no):** every key element is present, whatever is cited. This separates finding the passage from knowing the answer anyway, which the October round's Q2 showed are different: Gemini named the right ideas from its own knowledge while citing the wrong books.
5. **Quotation exactness:** every passage the answer puts in quotation marks and credits to a source, of five words or more, located with `locate.py`; exact, or not found.

The scorer is the Claude session running this round, with the key elements fixed above. Scores 1, 2, 3 and 5 are mechanical once the key sentence is picked; 4 is a judgement against the key.

## Reading the result, stated before any run

Let A and B be each arm's count of targets (out of 10) where score 1 is yes in both runs, and report the per-run counts beside them.

- **The hypothesis holds** if G-whole's B is at least 3 below its A, and GF's B is no more than 1 below its A.
- **It fails for Gemini** if G-whole's B is within 1 of its A: wording doesn't decide its retrieval here, and the October round's Q2 failure needs another explanation (the case's length, its multiple sub-questions, or the private corpus).
- **It fails for grounded-forge** if GF's B is at least 3 below its A: concept routing needs the words too.
- **Wording or chunk size.** If G-whole's B drops, G-split says why. If G-split's B recovers to within 1 of G-whole's A on the six split targets, chunk size is the cause; if it stays within 1 of G-whole's B, wording is. In between is reported as both. The four small targets, unsplit in both notebooks, are a second check: if B fails on them in G-whole, file size can't be the cause there.
- Score 4 is read alongside: a B answer that hits the key but cites the wrong book is the October Q2 pattern, retrieval covered by model knowledge.

Ten targets and two runs support a direction, not a rate.

## Known limits, stated before running

- **One question writer.** Claude wrote the (B) questions knowing the concept names. A user's words may carry fewer cues, or different ones. The overlap check binds the vocabulary, not how strongly a situation evokes a concept.
- **The judge is Claude, and so is the GF arm.** Scores 1, 2, 3 and 5 are mechanical; score 4 is a Claude judgement.
- **GF can also search by words.** It has Grep over the converted sources, so it isn't routing-only. Its tool log (`tools.json`) shows whether each run reached the target through the concept index's topics and rows or by searching the text, and the README reports which.
- **Small n and one corpus,** a public one whose OpenStax and Scrum material is dense in both models' training.
- **Gemini's chunking isn't documented.** The split notebook changes file size; whether that changes what the notebook retrieves is what's being tested, not assumed.
