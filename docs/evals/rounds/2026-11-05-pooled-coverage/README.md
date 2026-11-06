# Pooled coverage: how many supported ideas does each answer carry, with no answer key?

**Status: run 5–6 November 2026.** 61 answers to the case-citations cases, from seven arms, pooled into lists of distinct ideas by two model families, with no list written in advance. `answer-from-corpus` and verbatim mode after round 3b's fix carry the most supported ideas per answer, on both libraries and in both families' pooling. Open Notebook on Claude Opus 5.5 comes next, then every Gemini setup. Verbatim mode before round 3b's fix carried about as many as Gemini's chat answers. The strict chat style costs Gemini a few ideas and almost all of its unsupported ones.

## Why this round

The [case-citations round](../2026-11-case-citations/) measured coverage against answer keys: 11 and 13 expected ideas for C1 and C2, written before the runs. Claude wrote the keys, and Claude also wrote grounded-forge's answers, so a keyed count partly measures how closely the answers agree with the key's author, and it gives nothing for a good idea the key didn't list. This round drops the keys. It pools every distinct idea that appears in any answer to a case, checks each against the library, and counts what each answer carries.

## Design

- **Answers.** Every answer to the case-citations cases, two runs per arm per case:
  - Gemini Notebook in the chat condition at default style, and under the [strict chat style](../2026-11-05-gemini-strict-style/);
  - Gemini as asked: a Studio report where it wrote one, otherwise its chat answer;
  - [Open Notebook](../2026-11-06-open-notebook/) on Claude Opus 5.5 under the strict style (public cases only);
  - grounded-forge `answer-from-corpus`;
  - verbatim mode in [round 3](../2026-11-02-verbatim-case-citations/) (a fixed budget of placed passages) and round 3b (the model sizes the answer; on the private library 3b ran on three answers only).

  Public C1 and C2 have 14 answers each; private C1, C2 and C3 have 11, 12 and 10.
- **Blinding.** [`build.py`](build.py) strips citation markers and pointer blocks, shuffles the answers and labels them A, B, C…; the key to the labels is kept outside the repo. Each pooler may open only its case folder and the converted sources. Form still gives some answers away (a memo header, a gap paragraph, "My inference:" lines).
- **Pooling.** One Opus 5.5 and one Sol (`gpt-6.1-sol`) agent per case, both at effort high, each in a fresh context with [`brief.md`](brief.md): list every distinct substantive idea across the answers (diagnosis, mechanism, recommendation, priority, tension, warning), merge paraphrases, record which answers carry each, and grade each idea against the converted sources as `supported`, `partly` or `unsupported`. The public cases were pooled again once Open Notebook's answers existed, so their figures come from 14-answer pools.
- **Counting.** [`tally.py`](tally.py): per arm, ideas per answer, supported ideas per answer, and supported ideas per 1,000 words of answer.

Public pools are in [`work/`](work/); private ones stay outside the repo.

## Results

Supported ideas per answer (and per 1,000 words):

| Arm | Public, Opus | Public, Sol | Private, Opus | Private, Sol |
|---|---|---|---|---|
| grounded-forge, `answer-from-corpus` | **36.8** (25) | **46.5** (31) | **32.8** (22) | **52.3** (34) |
| grounded-forge, verbatim round 3b | **40.5** (17) | **48.8** (21) | **39.0** (18) | **54.0** (25) |
| Open Notebook, Opus 5.5, strict | 32.0 (22) | 39.5 (27) | not run | not run |
| grounded-forge, verbatim round 3 | 31.0 (19) | 36.0 (22) | 25.5 (15) | 39.2 (24) |
| Gemini, default chat | 26.8 (22) | 34.0 (28) | 21.2 (15) | 39.0 (27) |
| Gemini, as asked | 26.0 (11) | 36.5 (16) | 25.3 (12) | 44.3 (20) |
| Gemini, strict chat | 22.2 (19) | 29.2 (25) | 18.3 (17) | 32.8 (31) |

Mean words per answer: `answer-from-corpus` and Open Notebook about 1,500; verbatim round 3 about 1,650, round 3b about 2,200–2,300; Gemini default chat 1,240–1,430, strict 1,070–1,190, as asked about 2,200–2,300.

- **Sol splits ideas finer than Opus** (141–186 ideas per case against 79–113), so its counts run higher. The ranking is what the two share.
- **`answer-from-corpus` and verbatim round 3b lead in both families, on both libraries.** `answer-from-corpus` also leads per word, so its lead is not length; round 3b's is partly length.
- **Open Notebook, on the same model as grounded-forge, sits between grounded-forge and Gemini.** At about the same length as `answer-from-corpus`, it carried 5–7 fewer supported ideas per answer, and 5–10 more than Gemini's chat answers.
- **Verbatim round 3, with its fixed budget of placed passages, carried about as many ideas as Gemini's chat answers.** Round 3b's change, letting the model size the answer, moved it into the lead: 9–15 more supported ideas per answer.
- **Gemini's Studio reports are long and thin.** They carry about as many ideas as its chat answers or more, at the lowest density of any arm, and the most `partly` ideas.
- **The strict style costs Gemini 3–7 supported ideas per answer** and nearly all of its unsupported and `partly` ones.
- **Library support.** Most of each pool's ideas were `supported`; the private C3 pools, on the contemplative traditions, drew the most unsupported ideas (12–13 per pool).

## Limits

Five cases, two runs per arm, and two poolers per case. Pooling sets its own grain, and the two families set it differently, so per-answer counts compare within a family, not across. Claude wrote grounded-forge's answers, ran Open Notebook's, and is one of the two poolers; Sol is the check, and the ranking above holds in Sol's pooling. Ideas are counted as present or absent, not weighed for depth or for how well each is argued.
