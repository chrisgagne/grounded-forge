# Claims brief

You are splitting one answer into the claims a judge will check. You are not judging them.

Question: {question}

Answer: `{answer_path}`

Read the whole answer. Then list, in order, every sentence or clause that says something could be true or false, or recommends a course of action. Split a compound sentence where its parts could be scored differently: "X found A, and so B" is two claims. One claim cites no more sources than the sentence it came from.

Label each claim with exactly one type:

- `quotation`: words in quotation marks, attributed to a source.
- `attributed`: a paraphrase or summary credited to an author or source, by name or by a citation marker.
- `application`: the answer applies a source to the question, for example "for New Zealand, this means…". Note whether the answer marks it as its own reasoning (`marked`) or presents it as what the source says (`unmarked`).
- `uncited fact`: a factual statement with no source attached.
- `uncited recommendation`: advice with no source attached.
- `framing`: a sentence that orders or introduces the answer and makes no claim of its own, such as "Three things follow." Framing is listed but not scored.

Write a table:

| # | Claim (in full, as written) | Type | Marked? (applications only) | Citations attached (marker or pointer number) |
|---|---|---|---|---|

Under the table, give the count of each type. Copy each claim exactly as the answer has it, quotation marks and markers included. Write the result to `{out_path}`. Keep to the file named here.
