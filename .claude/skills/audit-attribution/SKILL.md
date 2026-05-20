---
name: audit-attribution
description: Audit an essay or draft for under-attribution against the library's curated corpus: surfaces the one or two closest neighbours whose work overlaps with the author's distinctive synthesis, classifies the overlap, and recommends specific provenance fixes. Not a fact-check; a build/contribute-boundary check.
argument-hint: "<path to essay file>"
---

# Audit attribution

Run an essay or draft through the library to surface **under-attribution**: the gap between an essay properly citing sources and an essay where a careful reader can tell what's being built on versus what's being contributed. Citation count is not the metric; the metric is whether the build/contribute boundary is visible from the text alone.

## Why this skill exists

When synthesising across multiple bodies of work, an author can produce an essay that:
1. Properly cites individual sources, and
2. Reproduces the structure, catalogue, or argumentative shape of one source closely enough that a reader of that source recognises it as the same territory, but
3. Frames the synthesis as the author's own without naming the closest neighbours in the lineage.

This is not plagiarism—citations exist—but it is **under-attribution**: the reader can't tell from the text alone what the author is building on versus contributing. The fix is provenance markers that make the build/contribute boundary visible.

A 30-citation essay can still under-attribute. Citation breadth is not citation depth.

## When to use

- Sanity-checking a draft before publication (blog post, paper, book chapter, board paper).
- After heavy revision where multiple sources have been integrated and the author's distinctive contribution may have been buried among attributions.
- When the audience includes readers familiar with one or more of the source bodies of work: they're the readers most likely to feel the under-attribution.

## When not to use

- Light editorial polish: this skill is heavyweight, designed for substantive synthesis work.
- Fact-checking individual claims against the corpus: that's `answer-from-corpus` with an audit framing, not this skill.
- First-draft generation: this is a late-stage check, not a generation tool.

## Procedure

### Step 1: Read the essay and identify load-bearing contributions

Read the essay in full. Identify:

- **The 1-3 distinctive claims** the author is contributing. The synthesis is usually one or two specific claims, not the whole essay. Surface these explicitly before any neighbour scan: buried distinctive claims are a separate failure mode (silent demotion) that the audit must flag.
- **The named coinages** in the essay: capitalised phrases, in-quotes terms, idiosyncratic vocabulary that may be someone else's. Examples: "Poetic Attunement", "Inherent Simplicity", "Self-Improvement Trap", "Lethal Paradigm", "Build/Contribute Boundary".
- **The argument's shape**: section logic, what it catalogues, what it prescribes, the diagnosis-prescription arc.

### Step 2: Closest-neighbour retrieval

Read the curated indexes in full first, then query Chroma, then grep the library as fallback. Queries are derived from:

- The essay's section headers
- Named claims in the load-bearing contribution list (Step 1)
- Already-cited authors (their neighbours and successors)
- Named coinages (check whether each is someone else's)

#### Step 2a: Precondition gate: read the corpus-level indexes

This is a precondition, not a guideline. The matrix indexes are curated routing documents: they do sense-making about how the corpus clusters that keyword search cannot recover. Read them as maps; reading them through is the work of Pass 1.

Read these three indexes in the order listed before proceeding to any other step:

1. **`{corpus-root}/references/slug-table.json`**: slug ↔ ID mapping. Load once; the `id → slug` map lives under the top-level `slugs` key.
2. **`{corpus-root}/reference-index.json`**: file catalogue (one entry per reference: author, year, title, primary_topic, concept_tags, scope, line counts). The per-ID entries live under the top-level `refs` key.
3. **`{corpus-root}/concept-index.json`**: concept axis with aliases and per-source section pointers. Entries live under `concepts`. Use `python3 -c "import json; ci = json.load(open('{corpus-root}/concept-index.json'))['concepts']; print(json.dumps(ci.get('{concept-slug}'), indent=2))"` to query a specific concept cheaply rather than reading the whole file; concept slugs are kebab-case (e.g., `systems-thinking`, `theory-of-constraints`).

Any of these indexes may exceed the Read tool's single-call token cap. Read them in paginated chunks (`offset` + `limit`, increase `offset` by `limit` each call) until the next call returns fewer lines than `limit` (the EOF signal). Before proceeding to any other step, **declare in plain text the line range you have read** (e.g., "reference-index.json read: L1–L420, complete"). The declaration is the gate: keep paginating until you can make it truthfully.

**When the Read tool returns a token-cap error, call Read again on the same file with the next `offset` and the same `limit`.** That is the path forward. If you notice yourself reaching for grep, ToolSearch, or any keyword approach to an index file, treat that as a signal you've drifted from the protocol: return to paginated reads or targeted python3 queries. The chunks-and-stitch path costs a few extra turns and preserves the curator's structure, which is what makes this work.

`{corpus-root}` is the active corpus directory: `corpus.commons/{corpus}/` for a commons corpus, `corpus.local/{corpus}/` for a local corpus. When the skill runs inside a deployed application (`apps/{profile}/`), the indexes live at bare paths (`./reference-index.json`, `./references/slug-table.json`, `./concept-index.json`) with the corpus prefix stripped.

#### Step 2b: Read relevant task-axis indexes in full

Same precondition: paginated reads to EOF, declare the line range covered before moving on. Read whichever task-axis indexes are relevant to the essay's territory: `{corpus-root}/distillations/{task}/task-index.json` for each applicable task domain. Task slugs correspond to the distillation directories present in the corpus (e.g., `decision-making`, `stakeholder-engagement`, `software-business`).

#### Step 2c: Query Chroma via `matching-references`

With `n_results: 50` and queries derived from the essay's load-bearing claims and named coinages. The skill returns metadata (filenames + author + similarity scores), not document bodies. Chroma catches semantic neighbours the index summaries don't surface by literal keyword. Apply the relevance floor (0.5 cosine similarity).

**Grep belongs to the library.** When Chroma is unavailable and index reading hasn't surfaced coverage for a sub-claim, grep `{corpus-root}/references/*.md`: the library files themselves. The distinction is load-bearing: the library is content to find by keyword; the indexes are curator maps to read in full.

The output of Step 2 is a candidate set, *not* a final list. Step 3 narrows it.

### Step 3: Apply the closest-neighbour filter

The skill must NOT surface every adjacent author. Apply the **strongest-form check** to each candidate:

> **Would the candidate themselves, reading this essay, feel their work was being passed off?**

If plausibly yes → flag for diagnosis. If clearly no → drop. If ambiguous → drop unless the overlap is in the load-bearing contribution. The discipline is the same as `matching-references`'s applicability gate: have an opinion, surface only the borderline-yes cases.

A useful secondary filter: *would a reader of only this neighbour's most-cited work mistake the essay's distinctive contribution for theirs?* If yes, the candidate is a closest neighbour.

Aim for 1-4 closest neighbours. More than that is over-flagging; this skill should produce a tight list.

### Step 4: Read each closest neighbour at depth

For each candidate that survives Step 3, read their light reference and the relevant deep reference. Lights tell you the candidate's argument shape; deeps surface the specific catalogues, coinages, and named cases that overlap with the essay.

The Pass 3 regime here is **Citation-grade**: the audit's whole purpose is defensible attribution, so deeps are mandatory. Skip a deep only if the candidate is light-only in the corpus.

### Step 5: Classify each overlap

For each closest neighbour, classify the overlap as one of:

- **Catalogue overlap**: same list of named phenomena (e.g., misfit paradigms; lean wastes; failure modes).
- **Argument overlap**: same claim, possibly with different framing.
- **Structural overlap**: same essay shape (diagnosis → prescription, same section logic).
- **Phrase overlap**: specific named coinages (the named-coinage check).
- **Origin-story overlap**: same illustrative narrative (e.g., PERT-as-façade, Healthcare.gov five-sprint plan).

A single neighbour may have overlap of multiple types; name them all.

### Step 6: Diagnose provenance markers per overlap

For each (candidate × overlap), check:

- **Named at all?** Does the essay cite this candidate anywhere?
- **Named in proximity?** Does the essay cite the candidate in the same paragraph or section as the overlapping claim?
- **Distinguishing language present?** Does the essay explicitly distinguish what's the candidate's vs. what the author is adding?

Three checks, three possible failures per overlap. The shape of the failure determines the fix.

### Step 7: Recommend a specific fix per gap

Match the fix to the failure shape:

- **Acknowledging sentence**: when the overlap is real but the essay doesn't name the candidate near the overlapping claim. *"X named several of these phenomena; what I add is the threshold being new, not the catalogue."*
- **Synthesis claim**: when multiple candidates are doing different parts of the work and the author's contribution is the synthesis. *"Block names why; Weinberg names that; the synthesis is mine."*
- **Boundary statement**: when the candidate works at one level and the author at another. *"X operates at the strategy level; what I add sits at the paradigm beneath."*
- **Provenance correction**: when an existing citation is doing more confessional work than the actual reading path warrants (false-confessional attribution). Reframe the citation for the reader's verification, not the author's autobiography.

Each fix should be a *suggested sentence*, not just a category: the author can reject or refine, but the audit should produce concrete language.

### Step 8: Named-coinage scan

Independent of the closest-neighbour pass, scan the essay for capitalised or in-quotes phrases. For each, check the corpus: is this someone's coinage? If yes:

- **Travel rule:** the attribution must travel with the phrase. Especially if the essay will be torn off into shorter excerpts (LinkedIn, blog teaser, conference abstract), every instance of the phrase needs the attributor in the same paragraph, not just on first use.
- Flag every instance where the named coinage appears without its attributor in proximity.

### Step 9: False-confessional check

Scan the essay's citations for a particular failure pattern: *the author claims to have come through one source to another that source didn't actually name*. Example: "I came to the PERT story via Poppendieck": true biography, but if Poppendieck didn't write the PERT story (Sapolsky did), the citation reads as deferential while being misleading about provenance.

The rule: **citations exist for the reader's verification, not the author's autobiography.** Name the primary source; only flag the secondary route if it materially shaped the reading. If the author's reading path doesn't load-bear, drop the secondary citation.

### Step 10: Silent-demotion check

Re-read the load-bearing contribution list from Step 1. For each claim, check that it's *explicitly claimed* somewhere in the essay, not just implicit among attributions. If the author has buried their distinctive contribution among citations, flag for promotion: the reader can't tell the contribution exists if it's not stated.

This is the inverse failure to under-attribution: the author isn't passing off others' work as theirs; they're passing off their own work as others'.

### Step 11: Write the audit report

Use the output shape below. The audit is a structured punch list, not prose.

## Output shape

```
ESSAY: [filename or first-line]

LOAD-BEARING CONTRIBUTIONS (the author's distinctive synthesis):
1. [claim 1, in plain language]
2. [claim 2]
[3, 4, ...]

CLOSEST NEIGHBOURS:

1. [Author, Work]
   - Overlap type: [catalogue | argument | structural | phrase | origin-story]
   - Overlapping with: [section number / specific claim]
   - Currently attributed: [yes / partial / no]
   - Named in proximity: [yes / no]
   - Distinguishing language present: [yes / no]
   - Strongest-form check: [would the candidate feel passed off? brief reasoning]
   - Recommended fix: [acknowledging sentence | synthesis claim | boundary statement | provenance correction]
   - Suggested wording: "[one sentence the author can use or refine]"

2. [...]

NAMED COINAGES TO TRAVEL WITH ATTRIBUTION:
- "[phrase 1]" (Author) — appears in §[N], §[M] without attributor in proximity. Suggested fix: [name the attributor in each paragraph where it appears, especially in tear-off-prone sections]
- "[phrase 2]" ...

PROVENANCE CORRECTIONS:
- [§N citation of X-via-Y]: false-confessional. The author read [primary] via [secondary], but [secondary] didn't actually treat this material. Suggested: cite [primary] for verification; mention [secondary] only if the reading path materially shaped the framing.

SILENT-DEMOTION FLAGS (the author's contribution is buried):
- [Claim from load-bearing list] is implicit but never explicitly claimed. Suggested: promote to a distinct sentence in §[N].

CITATIONS PRESENT BUT NOT AT RISK:
[Brief list of authors cited where the citation is doing the right work — included so the audit doesn't read as "everything is broken." The skill should NOT recommend changes to these.]

---
*Trace [Audit]: read essay (X words) → Pass 1 (reference-index.json + concept-index.json L1–LN, task-index(es), Chroma → M candidates) → strongest-form filter → K closest neighbours retained → Pass 3 deeps (K authors, citation-grade) → 11-step audit complete*
```

## Discipline

- **Citation count is not the metric.** A 30-citation essay can still under-attribute its closest neighbour. Don't be fooled by breadth.
- **Surface only the closest neighbours.** Apply the strongest-form check ("would the candidate feel passed off?") rigorously. Over-flagging makes the audit noise; the operator stops reading.
- **Provenance is for the reader, not the author.** Citations tell the reader where to verify, not the author's reading path. False-confessional citations are a real failure mode: name them.
- **The author's distinctive claim is usually 1-3 specific things, not the whole essay.** Identify these early so silent demotion can be checked.
- **Recommended fixes are *suggested wording*, not categories.** The author can reject the wording; the audit's job is to produce concrete language.
- **No prose generation.** The output is a structured punch list, not an essay or summary.

## Inputs

- Path to an essay file (markdown, plain text, or pasted body in chat).
- Optional: list of fields/lineages the essay operates in (helps narrow the neighbour search).

## Outputs

- A structured audit report following the output shape above.
- A trace footer showing which sources were consulted at which depth.

## Related skills

- `matching-references`: framework-discovery routing via Chroma. Called from Step 2c.

## Failure modes to avoid

- **Over-flagging.** Flagging every adjacent author makes the audit noise. Apply the strongest-form check.
- **Confusing breadth of citation with depth of attribution.** A heavily-cited essay can still under-attribute.
- **Treating the author's reading path as load-bearing.** Citations are for the reader, not for autobiography.
- **Silent demotion of distinctive claims.** If the author has buried their original synthesis among attributions, flag it for promotion, not just accuracy.
- **Flagging factual disagreement.** This skill is not a fact-check. If the corpus contradicts the essay's claim, that's a separate audit (use `answer-from-corpus` with an audit framing). This skill checks *whose argument shape this is*, not *who's right*.
