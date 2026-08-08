# Superseded: the 2026-07-28 OKF round

This round was published on 2026-07-28 and removed on 2026-08-02 in the same commit that retired the corpus's 99.4% self-audit figure, because parts of its record leaned on that figure's in-context audit receipts. The removal left the round's defensible findings without a public home; this notice restores the trail.

What replaced it:

- The full producer head-to-head — including this round's arms D, E, F, and G, the cross-family fidelity audits, and the fresh-context Pass I discovery that retired the 99.4% figure — is published whole at [`../2026-08-08-producer-head-to-head/`](../2026-08-08-producer-head-to-head/).
- The corpus-wide independent re-audit and repair that followed is at [`corpus.commons/demo/references/_audit/`](../../../../corpus.commons/demo/references/_audit/).

The original round's captures and judge runs remain in git history (`dbf70e1` through `f44058c`, removed at `b3ac1cd`). Findings from that round that survive unchanged: conformance is a container property (three conformant bundles with three different fidelity profiles); the naive-splitter baseline is grounding-safe but loses on coverage and synthesis; and preference rubrics cannot detect fabrication. Findings superseded: any use of the 99.4% figure as a fidelity guarantee, and the fidelity-addendum framing that treated the in-context Pass I receipts as an audit-of-record.
