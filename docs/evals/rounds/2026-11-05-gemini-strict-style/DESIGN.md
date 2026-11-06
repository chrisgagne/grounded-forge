# Gemini Notebook with a strict chat style: can a prompt fix the citations?

**Status: designed 5 November 2026, before any run.**

## The question

In the [case-citations round](../2026-11-case-citations/), at Gemini Notebook's default chat style, about 40% of Gemini's cited sentences were carried by their markers taken together (39% in Opus 5.5's joint grading, 41% in Sol's), and 9 of about 60 quoted strings were in a source word for word. The failure was overreach: a number, an application to the case or a stronger verb that no chunk carries. Can the user fix that by telling Gemini, in the notebook's own custom chat style, to cite only what a passage says?

## Design

- **Notebook:** the public demo notebook (35 files, all ticked), as in the case-citations round.
- **Chat style:** Custom, with the text in [`style.txt`](style.txt). Length at Default. The notebook goes back to its earlier setting after the last run.
- **Questions:** C1 and C2 from [`../2026-11-case-citations/cases.json`](../2026-11-case-citations/cases.json), each plus the line "Answer here in the chat.", the case-citations round's `chat` condition. Two runs each, chat history deleted and Studio emptied before every run.
- **Capture:** `capture.js` from the case-citations round: the answer with each marker as [n], and every marker's popup in full.
- **Scoring:** the case-citations round's per-marker brief, then the joint per-sentence brief from the default-style re-grade, each by Sol (`gpt-6.1-sol`, reasoning effort high) and Opus 5.5 (effort high). Quotations checked against the converted demo sources with the keyword-match round's `quotes_free.py`.
- **Comparison:** the four default-style public chat answers (demo C1-1, C1-2, C2-1, C2-2), scored the same way.

## What would count

- **The prompt fixes it** if, in both families' joint grading, the share of cited sentences carried by their markers rises to 70% or more, with no fall in key-idea coverage of more than 2 ideas per answer.
- **It helps** if that share rises by 10 points or more in both families.
- **It doesn't** if it rises by less than 10 points in either.
- Quotations are reported as found and exact, against the default style's 9 of about 60.

Four answers on one notebook give a direction, not a rate.
