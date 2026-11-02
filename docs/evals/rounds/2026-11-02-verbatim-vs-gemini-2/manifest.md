# Round 2 source manifest: what each arm could read

Exported 2 November 2026 from each notebook's source panel, before the first question, and matched against the corpus's `references/slug-table.json`. The AARBuddy notebook's file names were matched through the upload record of 19–22 October (`corpus.local/aarbuddy/projects/gemini-notebook-arm/upload-manifest.csv`), which maps each uploaded file to its slug.

## Question 1 and 2: the `aarbuddy` corpus and the AARBuddy notebook

- **Notebook:** `fa973698-94ab-4e51-b831-d3c3adb873e9`, 291 sources. For the round, 290 were ticked: *Come Prepared to Die* was unticked before question 2 and re-ticked afterwards. Question 1's Gemini answer is round 1's, asked with all 291 ticked.
- **Corpus:** 337 slugs in `slug-table.json`.
- **In both:** 329 corpus sources. 283 are one notebook file each; two of those files each merge several parts of one source. The other 48 are one course's session notes, uploaded as four bundles.
- **In the corpus, not in the notebook (8):** four whose upload failed with a bare error, two ingested after the notebook was built, and two not uploaded, for no reason the upload record gives.
- **In the notebook, not in the corpus (4):**
  - *Come Prepared to Die: An Engineering Leader's Field Guide to the Leadership Paradigms AI Is Exposing*, Chris's own book, a Google Doc. Unticked for question 2. Round 1's Gemini answer cites it twice.
  - A synthetic incident case written for an earlier round's live-facilitation question.
  - Two lens specs uploaded as sources for an earlier round.

## Question 3: the `demo` corpus and the demo notebook

- **Notebook:** `corpus.commons`, `2deb121e-2dec-48f7-903e-66219b10377a`, 35 sources, all ticked.
- **Corpus:** 31 slugs.
- **In both:** all 31. 30 are one notebook file each; `ssdl-systems-thinking-foundations` is five (ssdl-accumulations, ssdl-characteristics-of-complex-problems, ssdl-mental-models, ssdl-system-archetypes, ssdl-understanding-systems-from-a-feedback-perspective).
- **In one only:** none.

## The forge arm

The forge arm reads the corpus through its references and converted text, so its library is the corpus row of each table above. It did not read *Come Prepared to Die*, the synthetic case or the lens specs, none of which are corpus sources.
