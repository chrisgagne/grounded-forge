# Case citations: do Gemini Notebook's markers point where its claims come from, on the questions a practitioner asks? (pre-registration)

*Written and committed before any run. The results go in this folder's README; this file isn't edited after the first run except to fix a typo, and any such fix is named there.*

## The question

The [keyword-match round](../2026-11-keyword-match/) asked single-concept questions and found Gemini Notebook locates a plainly described concept whatever the words used. It did not recreate the October failure ([Q2 of the private round](../2026-10-22-gemini-notebook-private-corpus/)): a long case raising several issues at once, over about 290 sources, where Gemini's prose was right but every citation marker pointed at a chunk from another book. Two explanations remain: the **shape** of the question (several issues tangled in a user's words, a deliverable asked for) and the **scale** of the notebook. This round runs the same cases over a 35-source notebook and a 291-source one, and scores every citation marker on whether the chunk it points at carries the claim it's attached to.

The cases are modelled on the questions the operator has put to the corpus since June 2026, read from his own session logs: a situation in a client's or colleague's words, several issues at once, a named reader and a form ("a two-page memo for the CEO"), and often "show where the sources disagree". None is a rerun; Coppervale (October's Q2) and Larchwood (the 28 October round) were set aside because Gemini has answered both.

## Cases

Three, in [`cases.json`](cases.json), each the bare prompt a user would type, with no rules paragraph.

- **C1, Harbourline.** A CTO's statement: overflowing sprints, marketing against engineering on quality, a stretch target with a bonus on it, developers on several squads because "nobody is idle", a postmortem that put one developer on a performance plan, and a CEO who wants AI tools to "do both". Asks for a two-page memo: what's going on, what to change first, and where the thinking disagrees with itself.
- **C2, Doctrine against the textbook.** A broad synthesis: what doctrine written for war, spaceflight, nuclear plants and wildfire says against the management textbooks' playbook, where they contradict it, and where that matters for a 300-person company. For a sceptical CEO; the sources' disagreements with each other shown.
- **C3, Contemplative traditions and leadership.** The widest synthesis, in the operator's own style: the esoteric contemplative traditions read against the leadership literature. Private corpus only, since the demo corpus holds no contemplative source. Nothing from those sources is published.

**Answer keys** ([`keys.json`](keys.json)): 11 expected ideas for C1 and 13 for C2, each with the demo sources that carry it, checked by grep before this file was committed. Both corpora hold every listed source; the private corpus holds more that qualify, and a scorer may credit them. C3 has no key.

## Arms and runs

- **Gemini Notebook, demo:** the 35-file notebook of the keyword-match round (the original files behind all 31 demo sources).
- **Gemini Notebook, aarbuddy:** the October private notebook, 291 sources, all ticked; no case text, note or lens is a source. Chat history deleted and Studio files removed before the first run and between runs.
- **grounded-forge, demo** and **grounded-forge, aarbuddy:** `answer-from-corpus` in project mode over each corpus's reference tier, isolated `claude -p` on Opus 5.5 at effort high ([`run_gf.py`](run_gf.py), as in the keyword-match round, with the corpus a parameter). No distillations. The aarbuddy copy includes its lens index and specs, as the project does; the prompt names no lens.

Two runs per case per arm: C1 and C2 on all four arms, C3 on the two aarbuddy arms. 20 answers in all, 10 of them Gemini's.

Capture is as in the keyword-match round ([`capture.js`](capture.js), run in the notebook page): the answer with its markers, and for every marker the source name and the full chunk text its citation panel shows, saved as JSON. The aarbuddy notebook's file names map to corpus slugs through October's upload manifest.

## Scoring

Every number is rebuilt by [`summary.py`](summary.py) from the committed records. The scorer is Opus 5.5 in a fresh context, with the brief in `scores/scoring-brief.md`; it sees the chunks and the sources, not this file's reading rules.

1. **Citation support, the primary score.** The unit is one citation: a Gemini marker, or a grounded-forge sentence that credits a source by name or quotes it. For Gemini, the scorer reads the sentence the marker sits on and the chunk the marker opens, and grades the chunk **supports** (the chunk carries the claim), **partial** (the chunk is on the topic but doesn't carry the claim as stated) or **does not support** (the claim isn't in the chunk). For grounded-forge, the scorer finds the claim in the credited source's converted text (by the quotation, or by searching for the claim's terms) and grades the same three ways, with "not found after searching" as does-not-support. Each citation also gets the mechanical fields: the chunk's or credited source's slug, and whether the sentence names a different author or work than the one it's cited to (**wrong book**).
2. **Expected ideas** (C1, C2): each key idea present, and credited to a source that carries it.
3. **Quotation exactness:** every passage of five words or more in quotation marks and credited to a source, located word for word in the converted text ([`../2026-11-keyword-match/quotes.py`](../2026-11-keyword-match/quotes.py) with the corpus's converted folder).
4. **Breadth:** distinct sources cited per answer.

No two-sentence windows and no single key sentence: the keyword-match round showed those measure layout.

## Reading the result, stated before any run

Let U be an arm's share of citations graded does-not-support, pooled over a case's two runs.

- **The October pattern recurs** on a case and notebook when Gemini's U is at least 25% there.
- **Scale is the cause** if, on both C1 and C2, Gemini's U on the 291-source notebook exceeds its U on the 35-source notebook by 15 points or more.
- **Shape is the cause** if Gemini's U is at least 25% on both notebooks for C1 or C2.
- **Neither** if Gemini's U stays under 15% on both notebooks for both cases; then the October failure needs an explanation this round didn't test (the rules paragraph those first runs carried, or the case notes being a source in the notebook rather than in the prompt).
- grounded-forge's U is reported beside Gemini's on each arm. It isn't a hypothesis here; it's the comparison the October round made by hand.
- C3 is reported on its own, on the private corpus, as the closest thing to the operator's real use.

Three cases and two runs give a direction, not a rate. Private-corpus results are published as counts and kinds of failure; no answer text, chunk or quotation from a confidential or copyrighted source leaves the repo's private tier.

## Known limits, stated before running

- **The scorer is Claude, and one arm is Claude.** Chunk location and quotation location are mechanical; "supports" is a judgement.
- **Gemini and grounded-forge cite differently.** Gemini puts a marker on most sentences; grounded-forge credits by name and quotes. Support is graded per citation on both, so an arm that cites less is graded on fewer units.
- **Sources overlap the models' training.** Both may state a right idea from memory and cite it to the nearest chunk. Score 1 catches that only when the chunk doesn't carry the claim.
- **n is small,** and the operator wrote the cases with the corpora in view.
