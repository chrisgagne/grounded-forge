# Open Notebook on Claude Opus 5.5: an open-source notebook against the same cases

**Status: run 6 November 2026.** Open Notebook, the open-source Notebook alternative (lfnovo/open-notebook, MIT), answered the case-citations round's two public cases twice each, in its Ask mode, with Claude Opus 5.5 for every model role and the strict chat style pasted at the top of each question. Graded at book level by Opus 5.5 and Sol, 93% of its cited sentences were carried by the books they cite, and 129 of its 134 quotations were in a source word for word. In the [pooled-coverage round](../2026-11-05-pooled-coverage/) it carried more supported ideas per answer than any Gemini setup and fewer than grounded-forge's.

## Why this round

Gemini Notebook answers with Google's model; grounded-forge with Claude Opus 5.5. This round puts an open-source notebook tool on the same model as grounded-forge, under the same instructions Gemini got, to separate what the model and the instructions buy from what grounded-forge's design buys.

## Setup

- **Open Notebook** `v1-latest` in Docker on a Mac, every port bound to the Mac only. Language model: `claude-opus-5-5` through Chris's Anthropic API key, for the strategy, answer and final-answer roles. Embeddings: `nomic-embed-text` v1.5 in LM Studio running natively on the Mac. (Ollama inside Docker had no GPU and was too slow: 110 seconds per 50 chunks, past Open Notebook's 60-second batch limit.)
- **Library:** the 31 public demo sources as the deterministic converted text grounded-forge reads (`corpus.commons/demo/sources/converted`), embedded in Open Notebook's notebook "demo-public"; no insights or other transformations. Gemini got the original files, so Open Notebook started with cleaner text.
- **Mode:** Ask, Open Notebook's retrieval mode, which searches the embedded chunks and answers with citations. Its Chat mode sends every source in full with each message (about 6 million tokens for this library) and wasn't used.
- **Questions:** C1 and C2 from [`../2026-11-case-citations/cases.json`](../2026-11-case-citations/cases.json), twice each, with "Answer here in the chat." and the [strict style](../2026-11-05-gemini-strict-style/style.txt) pasted at the top ([`ask.py`](ask.py)). Answers in [`runs/`](runs/); `source-ids.json` maps Open Notebook's source IDs to slugs.

## Scoring

Open Notebook cites a whole source (`[source:…]`), not a passage, so each cited sentence was graded at book level: the scorer searched the cited books' converted text for the claim, the grain `answer-from-corpus` was graded at in the case-citations round. Opus 5.5 and Sol (`gpt-6.1-sol`), both at effort high, graded every cited sentence with [`brief.md`](brief.md); scores in [`work/`](work/), tally in [`tally.py`](tally.py). Quotations were located with the keyword-match round's `quotes_free.py`.

## Results

| Answer | Words | Cited sentences | Sources cited | "My inference:" | Carried (Opus / Sol) | Quotations found |
|---|---|---|---|---|---|---|
| C1-1 | 1,587 | 29 | 11 | 21 | 28 / 28 | 32 of 35 |
| C1-2 | 1,719 | 36 | 9 | 23 | 33 / 33 | 34 of 35 |
| C2-1 | 1,367 | 33 | 7 | 12 | 31 / 31 | 31 of 31 |
| C2-2 | 1,397 | 39 | 7 | 13 | 35 / 36 | 32 of 33 |
| All | | 137 | | | **127 (93%) / 128 (93%)** | **129 of 134** |

- **No citation missed outright** in either family's grading; the rest were `partial`. The partials are subtle: "senior stakeholders" where the guide says "key business stakeholders", the Facilitated Learning Analysis's "without recommendations" credited to the Learning Review, a quotation present but put to a use the source doesn't make.
- **Coverage.** In the pooled count (14 blind answers per public case), Open Notebook carried 32.0 supported ideas per answer in Opus's pooling and 39.5 in Sol's, against `answer-from-corpus`'s 36.8 and 46.5 at about the same length, and Gemini's default chat's 26.8 and 34.0.
- **Time:** about three to three and a half minutes per answer. The API cost wasn't recorded per answer.

## Compared with the other arms

| Public cases | Cited sentences carried | Grain | Quotations exact | Supported ideas per answer (Opus / Sol) |
|---|---|---|---|---|
| grounded-forge, verbatim mode (round 3b) | 96% (Opus) / 89% (Sol) of citations | passage | 147 of 147 | 40.5 / 48.8 |
| grounded-forge, `answer-from-corpus` | 95% / 86% | book | 142 of 146 | 36.8 / 46.5 |
| Open Notebook, Opus 5.5, strict | 93% / 93% | book | 129 of 134 | 32.0 / 39.5 |
| Gemini Notebook, strict style | 64% / 67% of sentences | chunk | 9 of 11 | 22.2 / 29.2 |

On the same model and under strict instructions, an ordinary chunk-and-embed notebook cites about as reliably as grounded-forge at book level. What separates them here is the grain of the citation (a book against a passage on the printed page), quotations exact by construction against exact by care, and about 15% more supported ideas per word for `answer-from-corpus`. `answer-from-corpus` ran without the strict instructions.

## Limits

Four answers on one library, two cases: a direction, not a rate. Book-level grading is easier than passage-level or chunk-level, so the 93% isn't directly comparable with Gemini's figure. Open Notebook got the cleaner converted text. Only Ask mode and one embedding model were tested.
