# Pass I quotations audit: ssdl-systems-thinking-foundations (2026-10-15)

**Mode:** quotations. Deep reference read in full (395 of 395 lines). Source: `corpus.commons/demo/sources/converted/ssdl-systems-thinking-foundations.md` (1,545 lines; passages read around each hit). Scope open, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the five distillations (aar, decision-making, retro, software-business, stakeholder-engagement), plus the human triage of that run.

## Counts

- Actionable checker lines worked: 32 (3 glyph, 13 near, 10 interrupted, 3 missing, 3 no-quote).
- Quotation-corrected: 3 lines in the deep ref (4 quotes), 2 in a distillation, 6 in the light ref (unmarked quotes found wrong during the propagation grep).
- Marker-corrected: 3 in the deep ref.
- Quotation marks removed from the reference's own wording: 1 in the deep ref.
- Stripped: 0.
- Left as is (conversion noise): 22 checker lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 17 | near: "X causes Y" drops the source's quote marks round X and Y | Now "'X' causes 'Y'" (the source's "X" causes "Y", nested) | src 593–594 |
| 17 | glyph: "is a hypothesis — there…" uses an em dash; the source has an en dash | Em dash → en dash, matching line 139 and 352 | src 675 |
| 202 | no-quote (triage): the sequence names and verbs are listed in italics under `[V]`, not quoted | First `[V]` → `[AP]`; the sentence describes the section's layout. The second sentence's two quoted prompts keep their `[V]` | src 948–982 |
| 250 | near: `[...]` in the Drifting Goals example stands where the converted text has nothing (the words are lost in conversion, src 1330–1334); the checker reads a bracket as an insertion standing for source text | `[...]` → `…`, and the trailing note now says the ellipsis marks the gap | src 1329–1342 |
| 303 | no-quote: "Seven (1.01 through 1.07)" under `[V]` is a count, not a quotation | `[V]` → `[AP]`; the citation now says each about-the-series footer lists the other six briefs by title and number. The count is derived from that list | src 186–207 |
| 320 | missing (triage): "not prescriptive" in quote marks; the source's heading reads "System archetypes should not be used prescriptively:" | Now ("should not be used prescriptively"; "may not be necessary") `[V]` | src 1422–1423, 1430 |
| 321 | no-quote: Visual-tools row under `[V]` is a summary across four briefs | `[V]` → `[AP]` | — |
| 376 | missing: "archetypes apply uniquely or primarily to education systems" sits in quote marks but is the reference's own wording of a position the source does not take | Quote marks removed ("the position that archetypes apply uniquely or primarily to education systems"); the `[V]` quote that follows stays | src 1106 |

## Changes, derived tier

- `distillations/stakeholder-engagement/…-stakeholder-engagement.md:18`: "all around us — in schools" → "all around us - in schools", the source's spaced hyphen (src 1106). Same wording as deep 212.
- `distillations/stakeholder-engagement/…-stakeholder-engagement.md:42`: "despite our best efforts — why" → "– why", the source's en dash (src 600).
- Light ref (unmarked quotations, found wrong in the propagation grep; corrected the same way as the deep ref):
  - 13: "X causes Y" → "'X' causes 'Y'" (src 593–594).
  - 25: "if we take action on X, … effect on Y." → "'X'" and "'Y'" restored (src 587–589); `Feedback thinking "looks for causal relationships…"` → `Feedback thinking looks "for causal relationships in both directions"` (the source reads "we look for", src 595–596).
  - 51: "four-archetypes" → "four archetypes", the source's words (src, Brief 1.07 + CONCEPT: "some even argue that four archetypes can explain all the other archetypes").
  - 52: ("not prescriptive", …) → ("should not be used prescriptively", …), as deep 320.
  - 80: `archetypes "have the potential to reinforce…"` → `using archetypes "has the potential to reinforce…"`; the source reads "has" (subject: "Jumping in to use archetypes", src 1431–1434).
- Propagation grep of the light ref and all five distillations for "X causes Y", "hypothesis —", "not prescriptive", "[...]", "Seven", "Practice Diagramming", "Share Out", "uniquely or primarily", "Visual tools", "all around us —", "best efforts —", "four-archetypes", "have the potential": no other copy. The aar distillation's continuity note (127) says the not-prescriptive and may-not-be-necessary cautions are `[V]` in the deep ref; that stays true (deep 278, 280). No distillation describes the markers changed at deep 202, 303 or 321.
- No change alters a claim the light ref or a distillation carries; the light-ref edits correct quoted wording only. The deep ref's content has changed, so the derived-provenance stamps need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 23, 280, 356; decision-making 66; retro 38; software-business 68; stakeholder-engagement 60** (near): the source reads "expert vs.novice", the space lost in conversion (src 1433–1434). Deep 280 also differs only in the italic markup of the lead-in (`_…:_`).
- **Deep 59** (missing, 23 of 24 words): a stray "4" sits inside the sentence, "characteristics of 4 / complex problems" (src 149), a superscript or column fragment from the PDF, not the authors' words.
- **Deep 73** (interrupted): footnote markers glued to "everyday life12." (src 324).
- **Deep 148** (near, triage): the source reads "loop?Try", the space lost in conversion (src 696–699). The quote is otherwise word for word.
- **Deep 149** (interrupted, triage): the source reads "causeeffect", the line-break hyphen lost (src 700–701); the same brief prints "cause-effect" at src 585.
- **Deep 160** (near): footnote marker glued to "increase,1" and a stray space in "bathtub ." (src 843).
- **Deep 190; decision-making 50** (near): footnote marker glued to "once2" (src 932).
- **Deep 222 (first quote); decision-making 68, 117; software-business 66; stakeholder-engagement 58** (interrupted): the SSDL contributions footer ("Specific contributions for each author are as follows…") is interleaved inside "eight to twelve core archetypes" (Brief 1.07, + CONCEPT).
- **Deep 222 (second quote), 328** (interrupted): the source reads "highleverage", the line-break hyphen lost (src 1153–1154).
- **Deep 234** (interrupted): page rule and "PAGE TWO" running footer between "higher-level reading" and "group, nominated" (src 1224–1233).

## Triage cross-check

- **Deep :202** (no-quote, paraphrase under `[V]`): fixed; `[V]` → `[AP]` on the descriptive sentence. See table.
- **Deep :320** (missing, "not prescriptive" not in source): fixed; now quotes "should not be used prescriptively". Same fix carried to light ref 52.
- **Deep :148** (near): conversion noise, "loop?Try" (src 698). No edit.
- **Deep :149** (interrupted): conversion noise, "causeeffect" (src 701). No edit.

Every triage row was addressed.

## Checker counts

- Before: 26 apostrophe, 23 initial, 3 glyph, 13 near, 10 interrupted, 3 missing, 3 no-quote (32 failing).
- After: 26 apostrophe, 23 initial, 11 near, 10 interrupted, 1 missing (22 failing, all the conversion noise listed above).

## Open

- Stamp left as is (quotations mode). No commit made; no build run.
- Derived-provenance stamps for the light ref and five distillations are stale against the edited deep ref; the parent re-stamps.
- Deep 250: the words lost between "a" and "and the gap would close" in the Drifting Goals example can be recovered only from the PDF, not the converted text.
