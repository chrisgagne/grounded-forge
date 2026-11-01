# Verbatim mode against Gemini Notebook, round 2: the same comparison with a stricter rubric

**Status: designed, not run.** Questions are still to be chosen.

[Round 1](../2026-11-02-verbatim-vs-gemini/) asked one question. Both blind judges preferred the forge answer: every quotation was exact, and its claims took a half to a third of the judge operations to check. Sol's review of that design found six weaknesses that only a different rubric can fix. Round 2 is that rubric, run on the pandemic question again (both answers reused) and on new questions the generator was never tuned on.

## What changed from round 1, and why

| Round 1 | Round 2 | Why |
|---|---|---|
| Each judge drew its own claim boundaries, and uncited prose went unscored | One pass ([`claims-brief.md`](claims-brief.md)) splits each answer into atomic claims, uncited ones included, and labels each one. Every judge scores the same list | Exact quotations could surround an unsupported recommendation that escaped scoring. Judges could also split compound sentences differently |
| Each judge read both answers | Each judge sees one answer only, in a fresh session. Each answer gets two judges | A passage found for one answer made the other cheaper to check |
| One support score per claim | Two: support as delivered (the answer's own pointer or shown passage) and support as recovered (the judge's own search) | A judge's search could quietly rescue a bad citation |
| `partly` covered every near miss | `partly` is split into reworded, narrower and overstated, and `no` into absent and contradicted | Different failures got the same score |
| No limit on searching | 6 judge operations per claim, then `not found` | Without a stopping rule, effort figures depend on each judge's patience |
| Library parity rested on the forge arm's five sources being in the notebook | A source manifest for both arms, and the notebook's one source outside the corpus (Chris's *Come Prepared to Die*) unticked | Gemini cited a source the forge arm could not have used |

The forge package changed too. Each fix came from a defect the round-1 judges found:

- **Built in the same step as the page.** `render.py` now writes `answer.md` through [`flatten.py`](../../../../scripts/verbatim/flatten.py), from the same data as the page. In round 1 the package was built before the data was replaced, and one pointer named an endnotes page.
- **Highlight drawn into the image.** The hit page's PNG now carries the highlight itself, so it shows wherever the image is opened. Before, only the report page drew it.
- **Paragraph context restored.** Some PDF conversions dropped the blank lines between paragraphs. The resolver now finds the paragraph ends those conversions lost, so a span's paragraph is a paragraph again, not a 2,000-word block.

## Design

- **Questions.** The pandemic question from round 1, with both arms' answers reused unchanged, plus two new questions. Each new question gets a fresh forge run with `generate.py` and a fresh Gemini answer.
- **The two arms' libraries.**
  - Forge: the private `aarbuddy` corpus.
  - Gemini: the AARBuddy notebook, with *Come Prepared to Die* unticked. Before the first question, export the notebook's source list and match it against the corpus's `slug-table.json` into `manifest.md`, listing what is in one and not the other.
- **Gemini arm.** Each question is asked once, in a cleared chat, at Default style and length. Restore the notebook's custom chat setting afterwards. Capture every citation popup in full, without picking among them.
- **Forge arm.** `generate.py --model opus --joins both`. The evaluated deliverable is `answer.md` as `render.py` writes it, with its paths rewritten to the judges' neutral path (`flatten.py --base`).
- **Identity masking.** Judges reach the files through a neutral symlink, and nothing names either tool. The two arms still differ in form: pointer blocks and page images against citation popups. Judges record a guess at which tool made the answer, after scoring.
- **Judges' library.** The original of every source either answer cites, or converted text where no original is held. A source with neither is scored from the passage the answer shows, and marked as such.

## Procedure, per question

1. **Claims.** One Opus agent runs [`claims-brief.md`](claims-brief.md) on each answer separately and writes `claims-A.md` and `claims-B.md`. Chris or the orchestrating session spot-checks the split before judging.
2. **Judges.** Four fresh Opus agents, each running [`judge-brief.md`](judge-brief.md) on one answer and its claim list. Two judge answer A and two judge answer B.
3. **Results.** For each answer, report:
   - quotation fidelity, with its denominator;
   - support for substantive claims, delivered and recovered, each with its denominator;
   - the uncited claims, by type;
   - judge operations per claim, separately for claims checked and claims not found;
   - the completion rate;
   - where the two judges of the same answer disagree.

   Steps are judge operations under the brief's counting rule, not human effort.

## What this round still cannot show

- Two or three questions are still a handful. They can show whether round 1's result repeats, not how often it holds.
- Judges are Opus with shell tools. A person with a PDF reader would find different steps cheap.
- The pandemic question is a development example: the resolver and renderer were fixed on its run.
