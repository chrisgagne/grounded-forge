# Scoring brief: Open Notebook answers, per cited sentence

Read `packet.md` in full. It holds one answer from Open Notebook, a notebook tool, to the question at its top. Each `[slug]` in the answer is a citation of that whole source; the tool cites sources, not passages. The converted text of every source is in the folder named in the packet header, as `{slug}.md`.

## Unit: one cited sentence

Every sentence (or list item) that carries one or more `[slug]` markers is one cited sentence. Sentences that begin "My inference:" carry no marker and are not graded.

## Grade per cited sentence

Search the converted text of the source or sources the sentence cites for its claim (Grep key terms in several phrasings, then read the region), and grade the sources together:

- `supports`: every part of the claim, as stated, is in at least one of the cited sources. Specific numbers, named mechanisms, causal links and qualifiers must each be there.
- `partial`: the cited sources carry the topic and some of the claim, but at least one part (a number, a cause, a qualifier, the strength of the statement, the situation it is applied to) is in none of them.
- `none`: the claim is not in any cited source after searching.

Grade the claim as written. A sentence that applies a source's point to the question's company is `supports` only if the general point is there and the sentence presents the application as such. Grade down on doubt. For each sentence that is not `supports`, name the part no cited source carries.

Also record `wrong_book`: `yes` if the sentence names an author, work or organisation and none of the cited sources is that one.

## Output

Write `score.json` in this folder:

```json
{"id": "...", "sentences": [{"n": 1, "claim": "first 200 characters", "cited": ["slug"], "support": "supports|partial|none", "missing": "", "wrong_book": "yes|no"}], "note": "one or two lines"}
```

Grade every cited sentence, not a sample. End your final message with counts only: cited sentences, supports, partial, none, wrong_book.
