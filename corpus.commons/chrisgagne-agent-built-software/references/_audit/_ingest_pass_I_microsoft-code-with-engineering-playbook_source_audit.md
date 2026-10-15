# Pass I source audit: microsoft-code-with-engineering-playbook

- **Date:** 2026-10-15
- **Auditor:** claude-opus-5-5, fresh subagent, same family as the generator (claude-opus-5-5). The cross-family leg (codex) runs blind in parallel on a frozen copy and is not reflected here.
- **Mode:** fix in place. The deep reference is **not stamped** by this leg; the driver stamps once every leg is done. The "Pass I. Audit pending." line (deep line 520) is left as is.
- **Deep reference:** `references/microsoft-code-with-engineering-playbook-deep.md`, 520 lines, read in full (1–520).
- **Tape:** `sources/converted/microsoft-code-with-engineering-playbook.md`, 2727 lines, read in full (1–2727). 26,177 words and sha256 `9263ae06…14f7`, both matching the deep's integrity notes. 28 `<!-- file: -->` markers, matching the 28 pages in **Structure**.
- **Original:** not available; worked from the tape alone. No page renders (the source is Markdown, so there are no pages to render).
- **Calibration:** protocol Pass I and the failure-mode reference read; fixtures 01, 07 and 12 read before the cold read.

## Verbatim check

`check-verbatim.py` before the audit: no findings (116 `[V]` markers; 1 figure claim not checked). After the edits: no findings, 0 figure claims not checked. So no quotations needed correcting.

## Coverage gate (TOC vs anchors)

The frontmatter declares `coverage: partial — operator-approved 2026-10-14` for a 28-page subset. All 28 files in **Structure** are anchored in the body (Parts I–VII), and the tape holds exactly those 28 files. Pass.

## Counts

- Claims audited: about 430 (prose sentences, list items, table rows and cells, markers, connection and opposition entries, integrity notes).
- Source-anchored as written: about 422.
- Stripped: 1 (an opposition entry).
- Marker-corrected: 2.
- Claim corrected: 5 (two cut author attributions, one misread parenthetical, one overstatement about the page's content, one mislabelled link).
- Quotations corrected: 0.

## Changes (line numbers are post-edit)

1. **L54, thesis: `[AR]` → `[AP]`.** "Unit tests must be reliable, fast and isolated; … fault injection hardens a system against failure" lists what each technique is for, collected across four pages. It reports no claim–warrant–conclusion structure, so it is paraphrase, not argument.
2. **L83, Map of outcomes: Rings parenthetical.** The deep said Rings are "described as 'expanding scopes of coverage'". The source cell reads "Rings (each of these are expanding scopes of coverage)" (tape L50), and "each of these" may refer to the whole list. Rewritten to quote the source's own words: "with the note that 'each of these are expanding scopes of coverage'".
3. **L155, Dependency injection: attribution.** "(a link to Martin Fowler's article)" → "(a link to an article on martinfowler.com)". The tape links the URL without naming an author (tape L396–397). The name came from the URL, not the text.
4. **L383, PR description: overstatement and attribution.**
   - The deep said a required type and short description "enable the features the page mentions". The source says they enable "the features mentioned above" (tape L2246), but the page names no such features. Rewritten to quote the phrase and record the gap.
   - "Fowler's article on feature toggles" → "a 'Feature Flags' article on martinfowler.com". The resource link (tape L2256) carries the label "Feature Flags" and a martinfowler.com URL, with no author named.
5. **L467, Key statistics: uptime row `[V]` → `[AP]`.** The cell ("99% ≈ 3.65 days; …") restates the source's figures in shorthand. It is not a quotation, so `[V]` was a marker mismatch (fixture 07 pattern).
6. **L479, Connections, Martin Fowler entry: attribution.** The deep credited Fowler with the dependency-injection link and the feature-toggle resource. Neither passage names him. The entry now credits Fowler only where the tape does: the definitions and description of test doubles (mocking.md), "Martin Fowler's blog" as a pyramid source (e2e README), and "Contract test from Martin Fowler" (CDC resources). The two unattributed martinfowler.com links are recorded as such.
7. **L495, Connections: SRE resource.** "the Google SRE book's system-tests chapter" → "the Google SRE Book's 'System Tests' section". The link label is "Google SRE Book - System Tests" (tape L1837), and its URL points to an anchor inside the testing-reliability chapter, so it is a section, not a chapter.
8. **L504, Positions framed against: stripped "Big Bang integration for large systems".** The source makes a bounded positive claim: Big Bang "is best for small system as a system too large may be difficult to localize" (tape L1441). It does not frame against a position, so recording it as an opposition invents one. The rest of the entry stays, because it comes from the page's explicit "Things to Avoid" (tape L1465–1467), and its "Big Bang" anchor is dropped.

## Checked and kept (possible over-flags, recorded so the cross-family sort can see the reasoning)

- **L179, parenthetical** "(The integration-testing page, in Part III, advises against testing business logic in integration tests.)". This is a pointer the ingester added, not a connection the author draws. It is kept because it is a factual pointer within the same source (tape L1467), with no claim that the author draws the contrast. The cross-family leg may disagree.
- **L264, Robot Framework `[AE]`** on the authors' comparison of Gauge and Robot ("In our usage…", tape L1609). The authors' own usage counts as their case, so `[AE]` holds; `[AP]` would also be defensible.
- **Resource entries marked `[BT]`** (L126, L183, L245, L336, L342, L383, L393). They list cited works rather than borrowed claims, and the Connections section leaves some neutral resources unmarked, so the markers are slightly inconsistent. Not changed: each entry correctly states that the page cites that work.
- **L192, TDD refactor.** The page's claim that changing `> 8` to `< 8` "does not change what the function returns" is wrong for an input of exactly 8 characters. The deep reports it as the page's own presentation ("which the page presents as"), so it is faithful. No change; the deep does not judge the source.
- **Remaining Positions entries** (mocking frameworks, too many E2E tests, unit testing as sufficient, Things to Avoid, DI overuse, deferring tests, battle of egos, large PRs and huge commits, blocking on out-of-scope issues, narrow DoR items). Each traces to an explicit "avoid", "not acceptable", "not the silver bullet" or "Don't" in the tape.
- **Integrity notes L513–519.** Word count, sha256, line span, the 28-file count and the two malformed tables (tape L1722; tape L2723) all verified against the tape. The "front matter and MDX imports dropped" detail and the author and licence line come from the acquisition record, as the notes themselves say. The tape cannot verify them.

## Derived tier

No light reference and no distillations exist for this slug (checked `references/` and `distillations/`). Nothing to re-derive. Should any be derived later, the changed claims above that a derived artefact might carry are: the Fowler attributions (items 3, 4, 6), the Rings note (item 2) and the Big Bang opposition (item 8).

## Left open

- The cross-family leg's findings are not yet sorted against this log.
- Stamping is deferred to the driver.


## Second leg

**Auditor:** Codex default model via the Codex CLI, read-only sandbox, for both the blind leg and the sort leg.

**Order of work (anti-anchoring):** the second leg audited a frozen copy of the pre-audit deep reference (sha256 `04b9aa334add81f81be6e9e8c6240d2925454265c7d0d21ea34485dbe11b7674`) blind, with the full tape, the original where available and the source card. In a separate run it then read both audits and the post-audit deep reference (sha256 `84259a21dfa531196990a1bf27a5b145ff6dac7c7a9a02e9512885bdebeba533`), checked each finding against the source, and sorted them. Files: `_ingest_pass_I_microsoft-code-with-engineering-playbook_crossfamily_blind.md`, `_ingest_pass_I_microsoft-code-with-engineering-playbook_crossfamily_sort.md`, `_ingest_pass_I_microsoft-code-with-engineering-playbook_crossfamily_prompts.md`.

**Sort result:** The sort counted 11 confirmed defects (7 confirmed and fixed, 0 fixed wrongly, 4 missed by the fixer), 2 over-flagged by the fixer and 0 by the blind auditor, 1 disputed finding from each auditor, and 1 new defect introduced by a fixer edit, with capture fixer=7 blind=4 both=0, and gave a fail verdict for unconditional shipping because the packet did not establish the acquisition declarations.

**Capture-recapture:** of the confirmed deep-reference defects, the fix-in-place audit raised 7, the blind audit 4, both 0. The Chapman estimate is 39 in all, about 28 found by neither leg. It assumes every defect is equally catchable, so defects both legs miss for the same reason make it run low.

**Remaining edits applied (2026-10-15):** All 5 remaining edits were applied as written (L64 restores "can run", L316 restores the recommendation to consider smoke testing, L383 strips the fixer's "names no such features" clause, L401 reads the FAQ's "out of" as reviewing from Visual Studio or VS Code, L452 keeps the source's "Tons of CO2 emissions"), none with changed wording and none declined; D1 (Rings) was kept as the fixer left it, since the quoted parenthetical keeps the source's own ambiguity (tape L50).

**Gate:** accepted by operator. Deep reference sha256 `f9535ee4fa4338b934e599503f028f92621d1ba2c24bae3a78b60fc6990969a6`, stamp included.
