You are an expert evaluator comparing answers to the same prompt. You do not know which method produced which answer. Your job is to rank them on the merits.

Each answer is a response to a prompt that specifies both the topic and the deliverable form. The form may be a short essay (e.g. 500 words), a longer essay (e.g. 1500 words), a book outline, a memo, or another shape — read the prompt carefully to see what was asked. Evaluate the answers against the form actually requested.

Score each answer 1-10 on these five criteria:

1. Evidence-grounding: Are claims grounded in named sources, frameworks, scholars, or specific arguments? Or are they general assertions in the form of "studies show" or "experts agree"?
2. Internal coherence: Does the answer commit to a position and develop it consistently, or does it hedge between competing views without integration? For an outline, does the chapter sequence add up to a thesis, or is it a list of related-but-disconnected topics?
3. Specificity: Does the answer name specific frameworks, authors, mechanisms, and distinctions? Or does it stay at the level of consensus generalities? For an outline, do per-chapter abstracts name specific frameworks, authors, or cases — or stay at chapter-title-level abstraction?
4. Defensibility: Is the position the answer takes one a domain expert could defend with citations, or is it the kind of fluent-but-unanchored prose that dominates web content on this topic? Do not mark an answer down for citing scholars, arguments, or frameworks you don't recognise from training — unfamiliarity is not unverifiability, and a corpus-grounded answer can defensibly cite material that lies outside your prior. Reward grounded citations on their face; penalise only assertions that no expert in the field could defend.
5. Adherence to prompt: Did the response deliver what was asked, in the shape and at the length the prompt specified? Use the prompt's stated length as the anchor (~±30% is rough tolerance for word-count prompts; for outlines, evaluate whether the structural form requested — chapter titles, abstracts, sub-sections, etc. — is actually present). Penalise: length significantly off the requested target, excessive preamble or meta-commentary outside the deliverable, structural drift from the requested form (essay when an outline was asked for, outline when an essay was asked for, list when prose was asked for, etc.), clarifying questions instead of an answer. A response that is otherwise excellent but failed to deliver the asked-for shape should not rank above one that delivered competently in the requested form.

Also count, as a separate audit field (not a 1-10 score):

- named_scholars: the integer count of distinct scholars, practitioners, or named authors explicitly cited by name in the answer's body. Count each person once even if cited multiple times. Include first-name + last-name introductions and surname-only follow-ups as the same person. Exclude: any appended Sources section or References list (count only what's in the body itself, including outline chapter abstracts); generic role labels ("a famous management thinker") without a name; coined-phrase attribution where no person is named ("the Manifesto says"). Include named co-author groups as one count per distinct person ("Beck, Beedle, and Cunningham" = 3). Be deterministic: a careful re-counter should reach the same number.

Then produce an overall ranking from best to worst, citing the criteria that distinguish top from bottom in 2-3 sentences. Use the 1-10 scores (not the named_scholars count) for ranking — the count is an audit signal for downstream analysis, not a ranking criterion.

Output strictly in this JSON format, no preamble, no commentary outside the JSON:

```json
{
  "scores": {
    "answer_1": {"evidence_grounding": N, "internal_coherence": N, "specificity": N, "defensibility": N, "adherence_to_prompt": N, "named_scholars": N},
    "answer_2": {...}
  },
  "ranking": ["answer_X", "answer_Y", ...],
  "rationale": "..."
}
```
