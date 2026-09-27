# Independent Pass I — nist-ssdf-1-1, 2026-09-27

The one demo deep reference added after the 2026-08-08 census, audited with two blind legs.

| Leg | Auditor | Read | Claims | Findings |
|---|---|---|---|---|
| Same-family | Claude Opus, fresh subagent | deep 1–228 of 228, source 1–2298 of 2298 | 189 | 1 MINOR-DRIFT |
| Cross-family | `gpt-5.6-sol`, reasoning effort xhigh, read-only | deep 1–228 of 228, source 1–2298 of 2298 | 163 | none |

Both legs audited the frozen deep reference recorded in `nist-ssdf-1-1.packet.json` against `sources/converted/nist-ssdf-1-1.md`, following `BRIEF.md`. Neither leg saw the other's findings.

**The one finding (F001, deep line 209, MINOR-DRIFT).** The Connections entry reported footnote 2 ("the SSDF practices do not map to" CSF Functions, Categories and Subcategories) without noting that Table 1 still lists NISTCSF subcategory references against 14 tasks (e.g., ID.GV-3 for PO.1.1). Verified at source lines 400–401 and 545. With one finding and no disagreement between legs, it was verified directly against the source instead of through a cross-family reconcile.

**Repair.** The deep reference and the light reference's Key Connections entry now carry the Table 1 note. The software-business distillation does not state the claim and needed no change. Both derived artefacts were re-stamped with `scripts/check_derived_provenance.py --stamp`.

With this, all 28 demo deep references have an independent cross-family audit.
