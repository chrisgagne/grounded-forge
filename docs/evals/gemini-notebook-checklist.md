# Gemini Notebook arm: operator checklist

The operator's side of [Method N](gemini-notebook-arm.md), run in their own Google account. Claude doesn't sign in. About an hour, most of it the e10 citation legend. Everything you save goes under `_evals/manual-gemini/raw/` in your grounded-forge clone (gitignored).

## Set up (once)

1. Pull `main`, then make the folder:

   ```bash
   mkdir -p _evals/manual-gemini/raw
   ```

2. In Gemini Notebook, create a notebook named `grounded-forge demo eval`.
3. **Add sources → Upload.** From `corpus.commons/demo/sources/converted/`, select these 31 files (every `.md` except `IMAGES-README.md`); upload in batches if it asks:

   `approach-perfect-field-guide-scrum-events.md`, `barbrook-johnson-systems-mapping.md`, `caib-report-vol1.md`, `doe-hpi-handbook-vol1.md`, `doe-hpi-handbook-vol2.md`, `flo-facilitation-guide.md`, `jones-evidence-based-sweng.md`, `letaw-handbook-sweng-methods.md`, `lfuo-learning-review-guide-2024.md`, `liberating-structures-handbook.md`, `mcdp1-warfighting.md`, `nhs-just-culture-guide.md`, `nist-ssdf-1-1.md`, `open-kanban.md`, `open-practice-library.md`, `openstax-accounting-vol1.md`, `openstax-accounting-vol2.md`, `openstax-business-ethics.md`, `openstax-business-law.md`, `openstax-economics-3e.md`, `openstax-entrepreneurship.md`, `openstax-introduction-business.md`, `openstax-organizational-behavior.md`, `openstax-principles-finance.md`, `openstax-principles-management.md`, `openstax-principles-marketing.md`, `openstax-psychology-2e.md`, `org-topologies-primer-2025.md`, `scrum-guide-2020.md`, `ssdl-systems-thinking-foundations.md`, `tc-25-20-army-aar.md`

4. Check the source panel shows **31 sources, all selected, no error badges**. Add no web or Discover sources.
5. Open `openstax-economics-3e` in the source viewer and scroll to the very end. The last line should be **`Zero elasticity 115`**. If it isn't there, or any upload failed, stop and tell Claude: the arm would be partial.
6. In the chat settings, leave the style on Default with no custom instructions; set response length to **Default**.

## Each prompt: p01 first, then e10

For `p01-decision-cognitive-process`, then `e10-aar-process` (`{stem}` below):

1. **Delete the chat history**, so the chat starts empty. For e10 only, set response length to **Longer**.
2. **Paste** everything below the `---` line in `docs/evals/harness/prompts/{stem}.md`, and nothing else. Send it and note the time.
3. When the answer finishes, note the wall time. Click the **copy** button under the answer and paste into **`_evals/manual-gemini/raw/{stem}-N.md`**. Don't edit it.
4. **Citation legend.** Click each citation number in order. The source opens with the passage highlighted. Add one line per number to **`_evals/manual-gemini/raw/{stem}-N.citations.md`**:

   ```
   [1] | openstax-organizational-behavior | first ~15 words of the highlighted passage, copied exactly
   ```

   Check that the highest number in the legend matches the highest `[n]` in the answer.
5. **Screenshots** of the whole answer, top to bottom: `_evals/manual-gemini/raw/{stem}-N-01.png`, `-02.png`, and so on.
6. **Meta**, in **`_evals/manual-gemini/raw/{stem}-N.meta.md`**: date and NZ time, plan tier (free), style and length settings, wall time, the model name if the page shows one, and any quota, error or "sources not used" message.
7. If the answer stops partway or hits a quota limit, write that in the meta file and don't retry in the same chat. A retry is a second run: save it as `{stem}-N2.*` and say so in its meta file.

**Optional, if quota allows:** a second fresh run of each prompt saved as `{stem}-N2.*`. It shows run-to-run variance.

## Hand back

Tell Claude "N captured", with the folder path. Claude then captures C and D, builds the judge copies, runs the claim audit and the judge, and drafts the round write-up. Keep the notebook unshared until the round is published.
