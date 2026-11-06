# Pooled-ideas brief

This folder holds one question (`question.md`) and 12 answers to it (`answers/A.md` to `answers/L.md`), written by different tools and runs. You don't know which wrote which, and nothing turns on guessing. The answers were written from a library whose converted source texts are in the converted-sources folder named in `question.md`.

Your job is to count coverage without an answer key: build the pool of distinct ideas that appear across all the answers, check each against the library, and record which answers carry each idea.

## Step 1: read

Read `question.md` and all the answers in full.

## Step 2: pool the ideas

List every distinct substantive idea any answer offers in response to the question. An idea is one point a reader could act on or argue with: a diagnosis of what is going on, a mechanism, a recommendation, a priority and its reason, a named tension or disagreement between sources, or a warning. One idea per row.

- **Grain.** Set it so that two careful readers would split the same way: "WIP limits reduce cycle time" and "limit work in progress per squad" are one idea; "limit WIP" and "dedicate each developer to one squad" are two. A recommendation and the diagnosis it answers are two ideas.
- **Merge paraphrases.** Different words, same point: one row.
- **Not ideas:** restating the question's facts, framing, headings, summaries of an earlier point, statements about the library itself, and bare source names.
- For each idea, list every answer that makes the point, in substance, anywhere in its text. An answer that only gestures at it ("flow matters") does not carry a specific idea ("flow, not utilisation, should be the target metric").

## Step 3: check each idea against the library

For each idea, search the converted sources (Grep key terms in several phrasings, then read the region) and grade:

- `supported`: a source in the library states the idea, or states premises from which the answer's point follows directly with no added specifics.
- `partly`: the library carries the topic but the idea adds a specific (a number, a causal claim, a strength) no source carries.
- `unsupported`: no source carries it. Note whether it is a reasonable inference from the library (`inference`) or goes beyond it (`beyond`).

Applying a source's point to the question's company is fine and counts as supported when the general point is in the library.

## Output

Write `pool.json` in this folder:

```json
{"ideas": [{"id": "I1", "idea": "one sentence", "kind": "diagnosis|mechanism|recommendation|priority|tension|warning", "answers": ["A", "D"], "library": "supported|partly|unsupported", "unsupported_kind": "inference|beyond|", "source": "file name and line where found, or empty", "note": "short"}]}
```

Then a final message with counts only: ideas pooled; supported, partly, unsupported; and per answer, ideas carried and how many of those are supported.
