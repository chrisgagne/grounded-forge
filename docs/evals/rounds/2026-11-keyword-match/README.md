# Keyword match: does Gemini Notebook need the sources' words to find a passage?

**TL;DR.** On 31 October 2026, ten passages in the public demo corpus were each asked for twice: once in the source's own terms (A), and once in a user's situation words that share no content word with the passage (B). The test ran against Gemini Notebook Pro over the original files and against grounded-forge's `answer-from-corpus` in project mode, two runs per question per arm. The hypothesis was that Gemini's retrieval depends on shared words and grounded-forge's doesn't.

- **No support for the hypothesis.** Asked in situation words, Gemini still cited the target section in all 20 answers, as it did in all 20 asked in the source's terms. grounded-forge also cited it in all 40. The pre-registered score was inconclusive (see below); every other reading shows no drop.
- **The test is narrower than the hypothesis.** The situation questions share no words with their passages, but each is a plain paraphrase of one concept ("the temps gave sloppy answers, which caused even more complaints" is the textbook fixes-that-fail case), and Gemini Notebook retrieves by meaning, not by words. What this shows is that Gemini finds a single, plainly described concept in a 35-source notebook. It doesn't recreate the October failure: a long case raising several issues at once, over a library in the low hundreds of sources.
- **Situation wording drew wider answers, not wrong ones.** On (B), Gemini's answers carried half as many citations again (14.8 against 9.7), more of them from books other than the target, as the answers took in neighbouring ideas. Whether those citations support their sentences wasn't checked. On the key claim itself, credits to unrelated books didn't rise (7 on A, 5 on B). Three of Gemini's (B) answers missed part of the answer key; grounded-forge hit it in all 40.
- **The pre-registered score fell between its two thresholds.** On it, Gemini dropped from 7 targets to 5 (both runs on target), short of the 3 that would have supported the hypothesis and more than the 1 that would have rejected it. The score turned out to measure answer layout as much as retrieval (see Scoring), and every other reading shows no drop.
- **grounded-forge reached the concept through words the question didn't use.** In 18 of its 20 (B) runs it fetched the topic the target concept is filed under from the index. It also looked concepts up by names it supplied itself ("friction", "paper", "diathesis", "fixes that fail").

Ten passages, two runs, one public corpus of 35 sources, and Claude as question writer and scorer: read this as a direction, not a decimal.

## Why this round

The [22 October round](../2026-10-22-gemini-notebook-private-corpus/) ran a private corpus in the low hundreds of sources against Gemini Notebook. A re-read of its per-question files on 31 October found the retrieval tie only on questions in the sources' own vocabulary. On a case with no shared vocabulary, Gemini's quotations were real but every citation marker pointed at a chunk from another book that shared a word with the case. That suggested Gemini retrieves by shared words. The round couldn't say whether wording or chunk size (the notebook held whole books and level-sized bundles) was the cause. This round tests the first directly, over public sources anyone can rerun.

## What was tested

The design was committed before any run ([`DESIGN.md`](DESIGN.md), commit 016fcd6d).

**Targets.** Ten passages from ten demo sources, each carrying one concept the concept index files under a topic: normalization of deviance (Columbia report), friction (MCDP 1), counterfactual arguments (Forest Service learning review guide), the Definition of Done (Scrum Guide), work mandate (Org Topologies primer), the paper plant (DOE human performance handbook), the diathesis-stress model (OpenStax *Psychology*), equity theory (OpenStax *Organizational Behavior*), fixes that fail (SSDL systems archetypes brief) and the Agreement/Uncertainty Matrix (Liberating Structures). [`targets.json`](targets.json) gives each passage's lines, the section a citation is scored against, a one-line answer key and its required elements.

**Questions.** Two per target, in [`questions.json`](questions.json). (A) uses the concept's name and the author's phrase. (B) describes a user's situation: "Our office relocation looked straightforward on paper, yet each step turned into a slog …" for friction, "We hired temps to clear a backlog of customer complaints …" for fixes that fail. [`check_overlap.py`](check_overlap.py) checks every (B) question against its passage with loose matching (suffixes stripped, a shared five-letter start counts as a match), and all ten share no content word ([`check-output.txt`](check-output.txt)).

**Arms.** Both got the bare question and nothing else.

- **Gemini Notebook,** Pro plan. The notebook from the [28 October round](../2026-10-28-aar-maker-live-review/), holding the original files behind AAR Maker's 22 sources (26 files: SSDL's five briefs as published, the Open Practice Library's pages joined into one file, the rest as original PDFs), plus the nine demo sources it lacked as original PDFs: eight byte-identical to the corpus's own originals, and NIST SSDF 1.1 (SP 800-218), whose original isn't in this checkout, from another corpus's copy of the same publication. That's 35 files and all 31 demo sources ([`split_pdfs.py`](split_pdfs.py) assembles the nine). Default chat settings, no custom instructions. Before every question the chat history was deleted and the Studio panel checked empty. Claude drove the notebook in Chris's browser. For each answer it saved the text with its citation markers and, for every marker, the source name and the full chunk text its citation panel shows ([`runs/gemini/`](runs/gemini/)).
- **grounded-forge,** project mode. [`run_gf.py`](run_gf.py) gives each run a fresh copy of the demo corpus's reference tier (references, converted sources, concept and reference indexes, lens index) with the `answer-from-corpus` skill, and no distillations. Each run is an isolated `claude -p` (Opus 5.5 at effort high, project and local settings only, auto-memory off, an empty MCP config, no Bash and no web). Answers and tool logs are in [`runs/gf/`](runs/gf/). The 40 runs cost $16.97 in all, about 56 seconds each.

**Two changes from the design, both made before any Gemini question was asked:**

- **Original files, not converted Markdown.** Chris chose to test over the originals grounded-forge ingested, so the notebook held PDFs where the design named the converted text.
- **No split notebook.** The design's chunk-size control re-uploaded the six large target sources one chapter per file. Chris chose to keep the sources as ingested. The design's second size check remained: four targets sit in small files (under 12,000 words) and six in large ones (up to 343,000).

## Scoring

Each Gemini citation chunk is located in the converted text by [`locate_citations.py`](locate_citations.py). A chunk is IN when it overlaps the target section, OUT when it's from the target source but another section, ALT when it's from another source that names the same concept, and OTHER when it's from any other book, whether or not that book also bears on the question. Each grounded-forge quotation is located the same way by [`quotes.py`](quotes.py). A Claude scorer (Opus 5.5 in a fresh context, which read the design, so it knew the hypothesis; brief in [`scores/scoring-brief.md`](scores/scoring-brief.md)) picked each answer's key sentence and applied the design's scores to both arms with the same conventions ([`scores/`](scores/)). [`summary.py`](summary.py) rebuilds every number below.

**The pre-registered primary score measured layout.** It required the answer key's every element within two sentences and a citation on that sentence pointing inside the target section. Long, structured answers spread a definition over a passage: grounded-forge often names its source in the sentence after the definition, and both arms put the key elements under separate headings. The rule found no key sentence in 13 of grounded-forge's 40 answers and 10 of Gemini's, although all 13 grounded-forge answers state the whole key. Two readings were added after scoring and are labelled as such:

- **Lenient:** the passage where the answer first explains the concept, rather than one sentence, credited to the target and cited inside its section.
- **Mechanical:** any citation in the answer that lands inside the target section, with no judgement at all.

Two location fixes were made after a first pass and applied to every answer. A Gemini chunk that starts just before the target section and runs into it was at first marked OUT from its first line. The locator now uses the chunk's whole span, which turned 16 markers IN across both forms. A grounded-forge answer (K09A-2) quotes the target passage as a blockquote without quotation marks, which the quotation extractor missed.

## Results

Runs out of 20, or targets out of 10 where both runs score.

| | Gemini A | Gemini B | grounded-forge A | grounded-forge B |
|---|---|---|---|---|
| Target section cited anywhere (mechanical) | 20 (10) | 20 (10) | 20 (10) | 20 (10) |
| Key passage cited in target section (lenient) | 20 (10) | 20 (10) | 19 (9) | 18 (9) |
| Key sentence cited in target section (pre-registered) | 14 (7) | 12 (5) | 6 (2) | 9 (3) |
| Answer key hit | 20 | 17 | 20 | 20 |
| Unrelated-book credits on the key sentence | 7 | 5 | 0 | 0 |
| Citations per answer | 9.7 | 14.8 | | |
| Share of citations inside the target section | 39% | 16% | | |
| Share of citations to other books (not the target or a listed alternative; support not checked) | 8% | 24% | | |
| Quotations exact / inexact | 3 / 0 | 2 / 2 | 163 / 2 | 140 / 2 |

**Kinds of failure.**

- **grounded-forge's three lenient misses are all one target.** In K01A-2 and both K01B runs, it explained normalization of deviance from the Columbia report's chapter 8 ("history as cause"), which treats the idea at length, not from section 6.1, where the term is first defined. The target section was narrower than the source's treatment.
- **Gemini's three answer-key misses are all (B) questions.** K04B-1 never says work that fails the Definition of Done isn't released or shown. Both K07B runs name diathesis and stress but not that both are needed or that one trades off against the other.
- **Gemini's unrelated-book credits** on key sentences come from the DOE handbooks on the counterfactual question (K03, all four runs), the Open Practice Library on K10A, and single credits on K01B-2 and K06A-1. The Open Practice Library has its own Stacey Matrix page, so the K10A credits are the right concept in a source the design didn't list as an alternative.
- **Other-book citations, spot-checked.** Whether each citation's chunk supports its sentence wasn't scored. A look at about 20 of the OTHER markers in two (B) answers (K01B-1, K03B-2), each sentence against its chunk, found most on point: Jones on developers ignoring warnings as the false-positive rate rises, the DOE handbook on at-risk practice reinforced by convenience, the Forest Service guide naming practical drift, DOE vol 2 on hindsight and on reconstructing the mindset at the time. Two or three were loose (a nuisance-alarm claim cited to a list of error precursors). The October pattern, markers on chunks that don't carry the claim, didn't show in that sample. A per-marker support score over all 40 answers is the measurement that would settle it, and the captured chunks make it cheap.
- **Inexact quotations.** Both arms reproduced MCDP 1's Clausewitz epigraph as printed rather than as the OCR'd text has it (grounded-forge K02A-2, Gemini K02B ×2). grounded-forge's other two reorder or inflect a few words (K03A-2, K07B-2). Gemini quotes little: 7 quotations across 40 answers, to grounded-forge's 307.
- **File size made no visible difference.** On the six large-file targets, Gemini's other-book share rose from 3% to 25% on (B). On the four small-file targets it held at 22–23%, mostly the Open Practice Library's Stacey page on K10 and other Scrum sources on K04. The target section was cited in every answer on both, so with no retrieval failure there was nothing for chunk size to explain.

**How grounded-forge routed.** [`gf_route.py`](gf_route.py), from each run's tool log ([`scores/gf-routes.tsv`](scores/gf-routes.tsv)): in 18 of the 20 (B) runs it fetched the rows of a topic the target concept is filed under. In the other two it looked the concept up in the index by name: "friction" in one, and in the other a list of words, one from the question ("drawing") beside its own ("latent", "paper"). Many runs that fetched topics also looked up a name they chose: "diathesis", "fixes that fail", "stacey", "equity". On (A) it mostly looked up the concept's name, which the question gave it.

## What it says

This test gives the hypothesis no support. With single-concept questions over 35 sources, Gemini Notebook found the target passage as reliably in a user's words as in the author's: every (B) answer cited the target section, as every (A) answer did. Its pre-registered score fell by 2 targets, between the threshold that would support the hypothesis and the one that would reject it, and that score tracked answer layout as much as retrieval. On the readings that don't, nothing fell. What situation wording did change was the answer's width. Gemini's (B) answers cited half as many chunks again, more of them from other books, as they took in neighbouring ideas; the key claim's citations didn't get worse. Three (B) answers missed part of the answer key, where grounded-forge missed none. grounded-forge didn't depend on wording either: it reached the concept through the index's topics, and by naming the concept itself. Since retrieval didn't fail, this round can't separate wording from chunk size. The October Q2 failure, where every marker pointed at another book, needs an explanation beyond shared words: a corpus eight times larger, a long case asking several things at once, or level-sized bundles. None of those is tested here.

## Caveats

- **Lexical isn't semantic.** Claude wrote the (B) questions knowing each concept's name, and each is a clear scenario for exactly one concept. The overlap check binds the vocabulary, not how strongly a situation evokes the concept, and an embedding retriever is built for paraphrase. A user's case cues the concept less, and usually several concepts at once.
- **Both arms route by meaning.** grounded-forge had Grep over the sources and chose its own lookup words, so its success can't be credited to the concept index rather than to the model naming the concept and searching for it.
- **Claude scored both arms, and one of them is Claude.** The location of every citation and quotation is mechanical. The key sentence and the answer-key hits are judgement.
- **Small n, one public corpus.** Ten targets, two runs, 35 sources, much of it OpenStax, Scrum and safety material dense in both models' training.
- **Single-concept questions.** Each question asks for one idea. The October failure came on a long case asking several things at once.
- **Gemini's capture came from the page.** The answer text was read from the page with its markers, not taken from the copy button. Its wording is Gemini's, but the formatting may differ slightly.

## What changed

- [`../../gemini-notebook-arm.md`](../../gemini-notebook-arm.md) lists this round as run.
- The October round's point 1 and the README's finding 5 say retrieval wasn't grounded-forge's edge, and this round agrees, so neither changes here.
