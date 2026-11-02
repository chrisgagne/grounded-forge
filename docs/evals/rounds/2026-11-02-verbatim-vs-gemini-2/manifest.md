# Round 2 source manifest: what each arm could read

Exported 2 November 2026 from each notebook's source panel, before the first question, and matched against the corpus's `references/slug-table.json`. The AARBuddy notebook's file names were matched through the upload record of 19–22 October (`corpus.local/aarbuddy/projects/gemini-notebook-arm/upload-manifest.csv`), which maps each uploaded file to its slug.

## Question 1 and 2: the `aarbuddy` corpus and the AARBuddy notebook

- **Notebook:** `fa973698-94ab-4e51-b831-d3c3adb873e9`, 291 sources. For the round, 290 were ticked: *Come Prepared to Die* was unticked before question 2 and re-ticked afterwards. Question 1's Gemini answer is round 1's, asked with all 291 ticked.
- **Corpus:** 337 slugs in `slug-table.json`.
- **In both:** 329 corpus sources. 283 are one notebook file each (two of those files merge several parts of one source: the ten MindTime style chapters, and Retromat volumes 1–5). 48 are the Aletheia course sessions, uploaded as four level bundles (L1 sessions 1–12, L2 sessions 0–14, L3 sessions 1–12 plus the Diamond Body practices, L3 Year 2 sessions 1–8).
- **In the corpus, not in the notebook (8):**
  - `conger-body-recovery`: its upload failed with a bare error (no text layer, or none given)
  - `enns-win-without-pitching`: ingested 23 October, after the notebook was built
  - `kaplan-oneness-separateness`: its upload failed with a bare error (no text layer, or none given)
  - `learning-science`: in the corpus before the notebook was built, but not uploaded; the upload record gives no reason
  - `porges-polyvagal`: in the corpus before the notebook was built, but not uploaded; the upload record gives no reason
  - `port-book-yourself-solid`: ingested 30 October, after the notebook was built
  - `rasmussen-srk-risk`: its upload failed with a bare error (no text layer, or none given)
  - `weinberg-design-stable-systems`: its upload failed with a bare error (no text layer, or none given)
- **In the notebook, not in the corpus (4):**
  - *Come Prepared to Die: An Engineering Leader's Field Guide to the Leadership Paradigms AI Is Exposing*, Chris's own book, a Google Doc. Unticked for question 2. Round 1's Gemini answer cites it twice.
  - *Larchwood incident notes*, a synthetic case written for an earlier round's live-facilitation question.
  - Two lens specs uploaded as sources for an earlier round: `chris-gagne-consultant-coach.md` and `sean-mcgrail-revenue-leader.md`.

## Question 3: the `demo` corpus and the demo notebook

- **Notebook:** `corpus.commons`, `2deb121e-2dec-48f7-903e-66219b10377a`, 35 sources, all ticked.
- **Corpus:** 31 slugs.
- **In both:** all 31. 30 are one notebook file each; `ssdl-systems-thinking-foundations` is five (ssdl-accumulations, ssdl-characteristics-of-complex-problems, ssdl-mental-models, ssdl-system-archetypes, ssdl-understanding-systems-from-a-feedback-perspective).
- **In one only:** none.

## The forge arm

The forge arm reads the corpus through its references and converted text, so its library is the corpus row of each table above. It did not read *Come Prepared to Die*, the Larchwood case or the lens files, none of which are corpus sources.
