# Known architectural limits

Three properties of the matrix architecture are not gaps to be filled in a later release. They are intrinsic to what the design *is*, and naming them is part of the discipline of shipping a bounded tool. This document explains each in the terms architectural-limits deserve: what the limit is, why the architecture has it, and what the operator can and cannot do about it.

These are distinct from *operational* limits (image classification incomplete for some sources, eval harness still maturing, individual scripts needing forker-side adjustment). Operational limits live at [`docs/reference/known-limitations.md`](../reference/known-limitations.md) and are addressable in subsequent releases. The limits below are not.

## Symbolic brittleness on out-of-distribution queries

The matrix's pre-projected distillations answer well within the task domains they were projected for. The reference-axis × task-axis structure carves the corpus into a finite set of intersections, each of which has been deliberately authored. For questions that fall outside those intersections, the architecture has nothing to fall back on. The projection layer is the wrong tool when the task at hand is not one of the task axes the corpus has been organised around.

This is the same shape of limit Lucy Suchman named in *Plans and Situated Actions* (1987): pre-specified plans hold under the conditions they were specified for, and break under conditions they were not. Suchman's argument was about Xerox copiers and human-machine interaction; the same shape applies to a pre-projected matrix. The matrix is a plan for retrieval, and like all plans, it works inside its scope and not outside it.

The honest implication: the matrix is the wrong tool for open-domain Q&A. An assistant built on this architecture should refuse questions whose task domain is not in its column-set, or should fall back to a different retrieval surface (standard RAG, web search) and label that fallback explicitly. The architecture cannot smooth over the discontinuity between the projected territory and the unprojected.

## Classification axes as world-making

The choice of *which task domains to project onto* is itself a substantive claim about how the work is organised. A library that ships with `decision-making` and `stakeholder-engagement` axes silently encodes a particular model of consulting work: useful, but not neutral. A fork that picks different axes will surface different concepts as central and different concepts as marginal, regardless of what's in the source corpus. Two corpora ingesting the same sources but projecting onto different task axes will produce systematically different assistants.

This is the *infrastructural inversion* Geoffrey Bowker and Susan Leigh Star named in *Sorting Things Out* (1999): classification systems are not neutral lookup tables, they are infrastructure that shapes what becomes visible and what recedes. Hacking's *looping effect* is the sharper version for the matrix: operators using `decision-making` and `stakeholder-engagement` as the cuts will, over time, learn to *see* their work through those cuts. The classification doesn't merely describe the work; it remakes it.

The architecture's decision to pre-project at the task axis is the operator's most consequential design call, and the one most easily mistaken for a neutral organising principle. The honest framing: the operator chooses what becomes visible. The architecture cannot make that choice neutrally on the operator's behalf.

Lisanne Bainbridge's *Ironies of Automation* (Automatica 19(6), 1983) is the structural version of this point: the more thorough the automation, the more consequential and harder-to-audit the residual human role. Applied here: the more aggressive the pre-projection at ingestion, the rarer the runtime decisions and the longer-lived the design choices that produced them. A well-projected matrix removes most query-time judgement and makes the operator's task-axis decisions load-bearing for the lifetime of the corpus. The successful pre-projection earns the operator the right to think harder about what the axes *should be*; it does not relieve them of the thinking.

## Corpus-to-world fidelity is not a property of this architecture

Pass I of the 9-pass ingestion protocol verifies fidelity to source. It does not, and cannot, verify the source's relation to the world. A 9-pass source-only protocol against a derivative or fashionable corpus produces a faithful projection of derivative or fashionable content. The architecture is *defensible* for the claim *"this answer is grounded in this source"* and *not defensible* for the claim *"this source is grounded in reality."* Source selection is the operator's job and the rule the protocol does not enforce.

The Bender et al. critique in *On the Dangers of Stochastic Parrots* (FAccT 2021) names the limit of fluency-as-a-proxy-for-truth: an LLM can produce coherent prose about topics it has no grounded understanding of. The matrix architecture answers half of that critique by tying every claim to a passage in a source the operator selected. The other half, whether that source itself is grounded, is unaddressed by the architecture. The operator's source-selection is the unit of accountability.

This is why the [source-integrity rule](source-integrity.md) is named with the exact qualifier it carries: *fidelity to source*, not *fidelity to truth*. The architecture is precise about what it does and does not warrant.

## See also

- [`source-integrity.md`](source-integrity.md): the source-only audit discipline that holds the architecture against training-prior drift at ingestion. Names the *fidelity-to-source-not-truth* qualifier directly.
- [`projection-time.md`](projection-time.md) §*When the matrix is the wrong tool*: the operational version of the symbolic-brittleness limit (which corpus shapes the matrix is the wrong tool for).
- [`docs/reference/known-limitations.md`](../reference/known-limitations.md): operational limits in the current release (what ships partial, what's pending).
