# Pass I quotations audit: openstax-business-law (2026-10-15)

**Mode:** quotations. Deep reference read in full (955 of 955 lines). Source: `corpus.commons/demo/sources/converted/openstax-business-law.md` (8,202 lines; passages read around each hit). Scope open-nc, so `[V]` must match the converted source word for word.

**Work list:** `check-verbatim.py` report over the deep ref, the light ref and the three distillations (decision-making, software-business, stakeholder-engagement), plus the human triage of that run. As a supplement, every double-quoted span in all five files (marked or not) was matched against the normalised source with a throwaway script; that turned up the two light-ref quotations and the deep 943 quotation below, which the checker does not test because they carry no `[V]`.

## Counts

- Actionable checker lines worked: 10 (6 near, 2 interrupted, 2 no-quote).
- Quotation-corrected: 7 lines in the deep ref (195, 201, 261, 262, 714, 818, 943); 3 lines in the derived tier (light 167, light 169, stakeholder-engagement 40).
- Marker-corrected: 3 lines in the deep ref (922, 923, 934: `[V, BT]` → `[BT]` on cited-person entries).
- Stripped: 0.
- Left as is (conversion noise): 3 lines.

## Changes, deep reference

| Line | Finding | Change | Source |
|---|---|---|---|
| 195 | near: Commerce Clause quote wrapped the source's own quotation in nested marks and dropped its closing period | Quote now only the Constitution's words: the power to "regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes" [V] | src 2228–2231 (Ch 4.1) |
| 201 | near: *Lopez* quote nested, same pattern | Now had "nothing to do with commerce, or any sort of enterprise" [V] | src 2291–2292 (Ch 4.1) |
| 261 | no-quote (triage): FCPA clause is the source's words with no quotation marks under `[V]` | Marks added: the Foreign Corrupt Practices Act "prohibits bribery payments by U.S. companies to foreign government officials" [V] | src 2813–2814 (Ch 5.1) |
| 262 | near: money-laundering quote capitalised "Taking", elided the source's own gloss, nested 'clean' without its period | Now Taking "dirty" money, "or money obtained through criminal activities, and passing it through otherwise legitimate businesses so that it appears 'clean.'" [V]. The source prints `“dirty”money` glued; quoting "dirty" alone avoids carrying the glue | src 2829–2830 (Ch 5.1) |
| 714 | near: FTC Act Section 5(a) quote nested, same pattern as 195 | Now prohibits "unfair or deceptive acts or practices in or affecting commerce" [V] | src 6190–6191 (Ch 12.1) |
| 818 | no-quote (triage): "Joseph P. Kennedy was the first chairperson" is a paraphrase under `[V]` | Replaced with the source's sentence, quoted: "The first chairperson of the SEC was Joseph P. Kennedy" [V] | src 7143 (Ch 14.2) |
| 922, 923 | `[V, BT]` on cited-person entries (Savitz, Okhakume) that quote nothing; not flagged by the checker | `[V, BT]` → `[BT]`. Both quotations stay `[V, BT]` in the body (185, 181) | src 1960, 1971 |
| 934 | `[V, BT]` on the Truman cited-person entry; the deep ref never quotes Truman | `[V, BT]` → `[BT]`. The source does quote Truman (1945, via Cheeseman) | src 6476–6479 (Ch 13.1) |
| 943 | unmarked quote "a rejection of laissez faire" is not in the source (source: "The rejection of laissez faire was part of…"); the second quote was cut mid-sentence before "that had become commonplace" | Now presented as a break with laissez-faire policy: "The rejection of laissez faire was part of a larger social shift that opposed the long hours, unsafe working conditions, and child labor that had become commonplace as a result of the Industrial Revolution" | src 7133–7138 (Ch 14.2) |

## Changes, derived tier

- `references/openstax-business-law.md:167`: the quote "may not be used to compel… personal service, since doing so…" put the source's two pieces in reverse order (the source opens "Personal service, however, may not be used to compel specific performance"). Now Personal service "may not be used to compel specific performance, since doing so would constitute forced labor, i.e. slavery, which is in violation of the U.S. Constitution." (src 3950–3952). Unmarked; the light ref carries no `[V]`.
- `references/openstax-business-law.md:169`: same "a rejection of laissez faire" misquote as deep 943; same fix (src 7136–7138).
- `distillations/stakeholder-engagement/openstax-business-law-stakeholder-engagement.md:40`: same nested FTC Act quote as deep 714 (checker near); same fix.
- Propagation grep of the light ref and all three distillations for "regulate Commerce", "nothing to do", "unfair or deceptive", "dirty", "foreign government officials", "first chair", "Kennedy", "laissez", "forced labor", "Savitz", "Okhakume", "Truman": no other copy of a wrong quotation or marker. Light 91 quotes the FTC Act phrase un-nested with the source's period and matches; light 109 gives "first chair Joseph P. Kennedy" as unmarked paraphrase; decision-making 156 and software-business 164 quote the forced-labour clause correctly; stakeholder-engagement 191 already lists Savitz as `[BT]`.
- No change alters a claim the light ref or a distillation carries. The stakeholder-engagement evidence-continuity note (204) stays true: `[BT]` still travels with Savitz, Thomas-Kilmann, Kionka and Cheeseman. The deep ref's content hash has changed, so the derived-provenance stamps on the light ref and distillations need re-stamping by the parent.

## Left as is (conversion noise)

- **Deep 241** (interrupted): the commerce-clause quote runs across the running header `**48   5 • Criminal Liability**` between "as long as some" and "economic transaction is involved" (src 2665–2671). The words are contiguous on the page.
- **Deep 437** (near): the source's bold markup leaves `**Uniform Commercial Code** ( **UCC** )was`, misplacing the spaces around the parenthesis (src 4164). The quote's "(UCC) was" is the printed text.
- **Deep 851** (interrupted): "a minimum of 40 days before the / shareholders' meeting" runs across the running header `**138   14 • Securities Regulation**` (src 7069–7075).
- Also noticed, no fix needed: deep 306 and 945 quote words the converted text prints with a dropped ligature ("plaintif", "qualifcations"); deep 778 runs across `**Access for free at openstax.org**` (src 6628–6633); deep 56 quotes the source's own typo "seeks to maximum the gain" (src 973).

## Triage cross-check

- **Deep 261** (no-quote, 'companies to foreign government officials' unquoted): fixed; quotation marks added around the source's clause, `[V]` kept.
- **Deep 818** (no-quote, 'Kennedy was the first chairperson' paraphrase under `[V]`): fixed; replaced with the source's sentence, quoted, `[V]` kept.

Every triage row was fixed.

## Checker counts

- Before: 19 apostrophe, 11 initial, 6 near, 2 interrupted, 2 no-quote; 45 figure claims not checked (10 failing).
- After: 19 apostrophe, 11 initial, 1 near, 2 interrupted; 45 figure claims not checked (3 failing, all conversion noise listed above).

## Open

- Stamp left as is (quotations mode). No commit made, no build run.
- Outside a quotations pass: the Key statistics table (deep 859–906) marks 46 rows `[V]` on unquoted cells; the checker counts 45 figure claims across the five files that it does not test. Some cells are derived rather than printed, e.g. "195 (193 full members + 2 observers)" (the source says "all but two participating as full members", src 6599) and "9-30 months". A full Pass I should check them or move derived cells to `[AP]`.
- Outside a quotations pass: many quotations in the deep ref carry no marker at all (e.g. 27, 56–59, 65, 92, 96, 302, 380–384). The supplementary script found them all in the source apart from the 943 case fixed above.
