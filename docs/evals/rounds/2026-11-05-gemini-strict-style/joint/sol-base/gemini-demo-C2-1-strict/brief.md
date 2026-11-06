# Joint grading brief

Read `packet.md` in this folder in full. It holds one answer from an AI notebook tool (citation markers written `[n:slug]`), then a list of sentences from that answer, each with the full text of the passage ("chunk") that every marker on it opens.

For each sentence, grade the markers **together**: taken as a set, do the chunks carry the sentence's claim as stated?

- `supports`: every part of the claim is in at least one of the chunks, as stated. Specific numbers, named mechanisms, causal links and qualifiers must each be there; a claim combining A and B is supported if one chunk carries A and another carries B.
- `partial`: the chunks together are on the topic and carry some of the claim, but at least one part (a number, a cause, a qualifier, the strength of the statement, the situation it's applied to) is in none of them.
- `none`: no chunk carries any substantive part of the claim.

Grade the claim as written, not what the author of a chunk would agree with. A sentence that applies a source's general point to the case in the question (a company, a CEO, a team) is `supports` only if the general point is carried and the sentence presents the application as such; if it states as the source's finding something the chunk doesn't say, grade it down. Grade down on doubt.

Some sentences carry one marker only; grade those the same way.

For each sentence that is not `supports`, name the part no chunk carries.

## Output

Your final message is a single JSON object and nothing else:

```json
{"grades": [{"s": "S1", "joint": "supports|partial|none", "missing": "the part no chunk carries, or empty", "used": ["n", "n"]}]}
```

`used` lists the markers whose chunks carry part of the claim. Grade every sentence in the packet.
