# Pass I source audit: openssf-finding-fixing-vulnerabilities-ai

- **Deep reference:** `references/openssf-finding-fixing-vulnerabilities-ai-deep.md` (626 lines)
- **Source (tape):** `sources/converted/openssf-finding-fixing-vulnerabilities-ai.md` (2,060 lines, 36,749 words). No original available; worked from the tape.
- **Date:** 2026-10-15
- **Auditor:** claude-opus-5-5, fresh subagent, same family as the generator. Cross-family leg (codex) runs separately on a frozen copy; this log was written without reading it.
- **Mode:** audit, fix in place. Per dispatch the deep reference is **not stamped** and its "Audit pending" line is left as is; the driver stamps once every leg is done.

## Coverage

- Deep reference read in full: lines 1–626.
- Tape read in full: lines 1–2,061 (bibliography and licence included).
- Page renders: none used. The tape is repository Markdown, not a scan or PDF, and nothing in it is damaged.
- Calibration exemplars read first: fixtures 01, 07, 12.

## Verbatim check

`scripts/check-verbatim.py` ran before and after the audit: **no findings** both times (33 figure claims not checked by the script; the Key statistics figures were checked by hand against the tape).

## Counts

| Item | Count |
|---|---|
| Claims audited | All claims in 626 lines: about 600 claim units (each marker-bearing clause in prose, plus 46 quiz rows, 44 statistics rows, 19 connection rows, 15 positions and 8 integrity notes). Marker tallies after the audit: [V] 304, [AP] 258, [AR] 31, [AE] 2, [BT] 409. |
| Source-anchored | All but the 4 below |
| Stripped | 0 |
| Marker-corrected | 3 (two in line 51, one in line 579) |
| Reworded to match the source | 2 (lines 208, 400) |
| Quotation-corrected | 0 |

TOC-vs-anchors: all ten chapters and every H2/H3/H4 section in the tape appear among the deep reference's anchors. No `coverage:` field, and none needed.

Mechanical claims checked: 141 bibliography keys; 19 uncited keys (the list in Part VII matches exactly); 46 quizzes, with the 1–29 / 30–41 / 42–46 split by chapter correct; 16 figures with alt text and placement correct; 8 linked videos; venue / arXiv labels for every paper the deep reference labels; tape length 2,060 lines and 36,749 words; [Yan2026] as the most-cited key (31 inline citations, then Grinstead2026-05 at 14), which supports line 579.

## Changes

1. **Line 51, "The method follows the chapter order [AR]" → [AP].** The sentence restates the Overview and Call-to-action lists. It is a paraphrase, not an argument.
2. **Line 51, "Two kinds of separation run through these chapters [AR]."** Source-external framing: the guide never pairs these points into two kinds of separation. That grouping is the ingester's synthesis, yet it was marked as the author's argument. Each point listed after it is source-anchored (checked: Separate identifying findings; Tips for validation; Evaluate merge/pull requests; Need for sandboxes; Establish a human gate and kill switch; Reporting to externally maintained projects; Turn findings into durable checks). Reworded to "Two kinds of separation recur across these chapters; the pairing is this reference's grouping of points the guide makes section by section [AP]."
3. **Line 208, "notes both are OpenSSF projects, as is the guide's publisher".** This wording implied the publisher is itself an OpenSSF project. The tape (line 692) says: "They're open source software projects of the OpenSSF, which produces this material." Changed to "notes both are open source projects of the OpenSSF, which produces the guide".
4. **Line 400, "AI-written reports often lack this context".** This shifted the source's point. The tape (line 1557) says: "Often, when AI writes the report, neither the code nor the documentation tells it which deployments are supported." Changed to match.
5. **Line 579, `others "don’t report" [BT]` → `[V] [BT]`.** The quoted words are the guide's own ("Others don't report the same", tape line 1195). They need [V]. [BT] stays for Yan's claim.

## Checked and left as is (not over-flagged)

- Line 85, "because" linking Holley's two quoted clauses: a fair reading of one continuous Holley quotation.
- Line 179, the [BT] on the sentence after Zimmer's quotation: the tape's following sentences are ambiguous between Zimmer and the guide's own voice. Kept the source's ambiguity rather than reassigning it.
- Line 293: the tape's near-duplicate sub-items 2 and 3 under Helping to identify findings are a feature of the source, and line 624 already discloses them.
- Lines 577–597, the stance labels ("approving", "neutral") in Connections: the section states that the groupings are the reference's, and each label matches how the guide uses the source.
- Evaluative-word sweep (strongest, plausible, surprising, robust, importantly): every hit is the source's own wording.

## Left open

- **Key statistics, MDASH row (line 543):** "more than 100 specialised agents" is credited to [Bishop2026]. In the tape (line 638) the sentence sits between a [Bishop2026] citation and a [Kim2026] citation, so its attribution is ambiguous. Body line 202 does not name a key for it. Low stakes; a later pass may want "[Bishop2026] / [Kim2026]".
- **Same-family limit:** this leg shares the generator's model family. Per the protocol, treat the reference as audited-but-unverified until the cross-family leg's sort is done.

## Derived tier

No light reference and no distillations exist for this slug, so there is nothing to re-derive. If they are derived later, none of the five changes above alters a substantive claim about the guide's content except change 4 (the reason AI-written reports need an early deployment-model statement) and change 2 (the separation pairing is now labelled as the reference's own grouping, not the guide's thesis).


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `12ae9c71876f9d4e8f1fd0c8433ea4eafe45a635399560c98d73963422f236ab`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `7fce3c2d99e0f03dacdf3570968b05cf1a40a9b7bd24bc586b1a7783174417de`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_openssf-finding-fixing-vulnerabilities-ai_crossfamily_blind.md`, `_ingest_pass_I_openssf-finding-fixing-vulnerabilities-ai_crossfamily_sort.md`, `_ingest_pass_I_openssf-finding-fixing-vulnerabilities-ai_crossfamily_prompts.md`.

**Sort result:** The sort confirmed 16 defects (4 correctly fixed by the fix-in-place audit, 1 fixed incompletely, 11 missed by it and caught by the blind audit; capture fixer=5, blind=11, both=0), found 0 over-flagged by either auditor and 0 new defects introduced, left 6 finding groups disputed, and gave a pass verdict once its 20 remaining edits were applied.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 5, the blind audit 11, both 0. The Chapman estimate is 71 in all, about 55 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** Of 20 remaining edits, 10 were applied as written, 4 with changed wording (edit 4 quotes the ambiguous PatchBench clause as [V] instead of only paraphrasing it; edit 6 uses the tape's 'challenging' as a parenthetical; edit 9 uses the tape's 'found' and 'show a zero rate'; edit 13 says 'model and service access' and 'an interruption'), and 6 were declined (edits 15-20, disputed B13-B16): the corpus holds the acquisition record (_planning/staging/chrisgagne-agent-built-software/acquisition/openssf-finding-fixing-vulnerabilities-ai.json, with commit, coverage 'the HTML pages are generated from it', word counts 36,745/36,749 and converted_via), the 16 image files at sources/converted/openssf-finding-fixing-vulnerabilities-ai-images/, the source card with the best.openssf.org URL, and the producer receipt (_planning/ingest/chrisgagne-agent-built-software/openssf-finding-fixing-vulnerabilities-ai/producer-receipt.md) recording the 13 read ranges over lines 1-2,060, and the tape's sha256 matches the source card, so the reference's provenance claims stand as written.

**Gate:** pass. Deep reference sha256 `66f98536a92a990e2d8aa05e06dd64b813395c48c6bde1451b6f29caa573aa40`, stamp included.
