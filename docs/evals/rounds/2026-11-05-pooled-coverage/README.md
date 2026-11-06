# Pooled coverage: how many supported ideas does each answer carry, with no answer key?

**Status: run 5–6 November 2026.** 57 answers to the case-citations cases, from six arms, pooled into lists of distinct ideas by two model families, with no list written in advance. `answer-from-corpus` and verbatim mode after round 3b's fix carry the most supported ideas per answer, on both libraries and in both families' pooling: about 50–54 per answer in Sol's pooling against Gemini's 38–39 at default, and 33–40 against 21–24 in Opus's. Verbatim mode before that fix carried about as many as Gemini's chat answers. The strict chat style costs Gemini a few ideas and almost all of its unsupported ones.

## Why this round

The [case-citations round](../2026-11-case-citations/) measured coverage against answer keys: 11 and 13 expected ideas for C1 and C2, written before the runs. Claude wrote the keys, and Claude also wrote grounded-forge's answers, so a keyed count partly measures how closely the answers agree with the key's author, and it gives nothing for a good idea the key didn't list. This round drops the keys. It pools every distinct idea that appears in any answer to a case, checks each against the library, and counts what each answer carries.

## Design

- **Answers.** Every answer to the case-citations cases, two runs per arm per case, on both libraries:
  - Gemini Notebook in the chat condition at default style, and under the [strict chat style](../2026-11-05-gemini-strict-style/);
  - Gemini as asked: a Studio report where it wrote one, otherwise its chat answer;
  - grounded-forge `answer-from-corpus`;
  - verbatim mode in [round 3](../2026-11-02-verbatim-case-citations/) (a fixed budget of placed passages) and round 3b (the model sizes the answer; on the private library 3b ran on three answers only).

  Public C1 and C2 have 12 answers each; private C1, C2 and C3 have 11, 12 and 10.
- **Blinding.** [`build.py`](build.py) strips citation markers and pointer blocks, shuffles the answers and labels them A, B, C…; the key to the labels is kept outside the repo. Each pooler may open only its case folder and the converted sources. Form still gives some answers away (a memo header, a gap paragraph).
- **Pooling.** One Opus 5.5 and one Sol (`gpt-6.1-sol`) agent per case, both at effort high, each in a fresh context with [`brief.md`](brief.md): list every distinct substantive idea across the answers (diagnosis, mechanism, recommendation, priority, tension, warning), merge paraphrases, record which answers carry each, and grade each idea against the converted sources as `supported`, `partly` or `unsupported`.
- **Counting.** [`tally.py`](tally.py): per arm, ideas per answer, supported ideas per answer, and supported ideas per 1,000 words of answer.

Public pools are in [`work/`](work/); private ones stay outside the repo.

## Results

Supported ideas per answer (and per 1,000 words):

| Arm | Public, Opus | Public, Sol | Private, Opus | Private, Sol |
|---|---|---|---|---|
| grounded-forge, `answer-from-corpus` | **36.0** (24) | **50.8** (34) | **32.8** (22) | **52.3** (34) |
| grounded-forge, verbatim round 3b | **39.5** (17) | **53.0** (23) | **39.0** (18) | **54.0** (25) |
| grounded-forge, verbatim round 3 | 30.5 (18) | 37.8 (23) | 25.5 (15) | 39.2 (24) |
| Gemini, default chat | 24.2 (20) | 38.0 (31) | 21.2 (15) | 39.0 (27) |
| Gemini, strict chat | 20.2 (17) | 31.5 (27) | 18.3 (17) | 32.8 (31) |
| Gemini, as asked | 26.0 (11) | 44.5 (19) | 25.3 (12) | 44.3 (20) |

Mean words per answer: `answer-from-corpus` about 1,500; verbatim round 3 about 1,650, round 3b about 2,200–2,300; Gemini default chat 1,240–1,430, strict 1,070–1,190, as asked about 2,200–2,300.

- **Sol splits ideas about 1.5 times finer than Opus** (141–186 ideas per case against 78–89), so its counts run higher. The ranking is what the two share.
- **`answer-from-corpus` and verbatim round 3b lead in both families, on both libraries,** by 12–15 supported ideas per answer over Gemini's default chat in Sol's pooling and 12–18 in Opus's. `answer-from-corpus` also leads per word, so its lead is not length; round 3b's is partly length.
- **Verbatim round 3, with its fixed budget of placed passages, carried about as many ideas as Gemini's chat answers** in Sol's pooling and a few more in Opus's. Round 3b's change, letting the model size the answer, is what moved it into the lead: 9–15 more supported ideas per answer.
- **Gemini's Studio reports are long and thin.** In Sol's pooling they carry more ideas than its chat answers, at the lowest density of any arm, and the most `partly` ideas (7–11 per answer in Sol's pooling).
- **The strict style costs Gemini 3–7 supported ideas per answer** and nearly all of its unsupported and `partly` ones; per word it holds about level with the default.
- **Library support.** 76–95% of each pool's ideas were `supported`, except Opus's private C3 pool at 68%; C3, on the contemplative traditions, drew the most unsupported ideas (12–13 per pool).

## Limits

Five cases, two runs per arm, and two poolers per case. Pooling sets its own grain, and the two families set it differently, so per-answer counts compare within a family, not across. Claude wrote grounded-forge's answers and is one of the two poolers; Sol is the check, and the ranking above holds in Sol's pooling. Ideas are counted as present or absent, not weighed for depth or for how well each is argued.
