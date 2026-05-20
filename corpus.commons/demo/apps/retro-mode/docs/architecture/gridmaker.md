# The Gridmaker

*A short note on the older language this architecture is built in. The engineering reading is in [`overview.md`](overview.md), [`projection-time.md`](projection-time.md), and [`matrix-pattern.md`](matrix-pattern.md); read those first if you want to know what the matrix does.*

## The architectural rule

**Lenses are windows, not selves.** A lens spec describes how looking happens through it — what gets foregrounded, what recedes, what vocabulary the reader notices. It does not describe a someone doing the looking. The operator is always the one looking. The lens is always a way of looking.

This is the discipline that shapes `corpus.commons/{corpus}/lenses/`. The named-real-person lens kind exists (see [`.claude/skills/creating-lenses/SKILL.md`](../../.claude/skills/creating-lenses/SKILL.md), Phase 1 branch (a)), but its grounding contract carries an explicit anthropomorphism guard and an as-if clause: *reads as if X were reading, given what X's public material reveals; it is not X*. The same discipline scales to self-lenses produced by [`gridmaker-interview`](../../.claude/skills/gridmaker-interview/SKILL.md): *reads as if {operator}-at-time-T were reading; it is not {operator}-now*.

The rule is small and load-bearing. Confusing the window with the seer is the failure mode the lens artefacts prevent at authoring time, through the skill's grounding-contract requirements.

## Where the language comes from

Beatrice Bruteau, *The Psychic Grid* (1979), names what the engineering vocabulary nearly misses: every read of every source goes through a *grid* — a perception-conception-language-behaviour pattern that selects what gets through. She calls the agent-self that frames grids and is itself not changed by any grid the **Gridmaker**.

Three passages carry the load.

On the *necessity* of grids — that they are the condition of legibility, not a betrayal of source:

> "There is no such thing as 'raw' experience, experience that is unfiltered, unsorted, unevaluated. What registers with us as actual conscious experience is always the product of both the incoming stimulus and the significance we attach to it by the operation of our psychic grid."
> — Bruteau, *The Psychic Grid*, Ch 3

Her illustration is Luria's case of S the Mnemonist — a man who could not forget. Without the selective operation of a grid, *everything is presented to the mind with equal value. No pattern is discernible.* Forgetting — selection — is what permits experience to organise into meaning.

On the *inheritance* of grids — that we do not author them privately:

> "Everyday reality is con-sensus reality, reality sensed together... The community holds together by these shared convictions. In the unity of its common psychic grid, it is essentially a conviction community."
> — Bruteau, *The Psychic Grid*, Ch 4

And on the *agent-self* that frames grids and is not modified by any grid:

> "We construct these psychic grids through which we interact with the universe. We are not victims of the psychic grids. Although our worlds are made by them, we in turn are the Gridmakers."
> — Bruteau, *The Psychic Grid*, Ch 8

## What this has to do with the matrix

Bruteau's claim is that we are always looking through grids — inherited from our conviction communities, mostly invisible to us as grids. Most AI assistants operate at the level of grid-inheritance: they hand the user a pre-baked grid (the vendor's training corpus, the vendor's product framing) disguised as neutrality, and the user looks through the window without knowing it is a window.

The matrix architecture does the inverse. It hands the operator the *components* of a grid — corpora, task axes, lenses, visibility ceilings — and asks them to assemble. Every act of running `creating-applications` is an act of assembly:

- The corpus chosen is *which conviction communities' work is being inherited* (references with their authors, traditions, evidence-classification markers, borrowed-through flags — provenance preserved).
- The task axis chosen is *what slice of work is being framed for* (decision-making, stakeholder-engagement, after-action review — each a structural commitment about what the assistant is for).
- The lenses chosen are *which reader-positions reshape what is salient* (each a window with named *notices-first*, *recedes*, and *native vocabulary*).
- The visibility ceiling chosen is *which audience the assembled grid is being shaped for* (open, open-nc, copyrighted, confidential, personal).

The compiled application is the assembled grid. The 9-pass ingestion protocol, the source-integrity rule, the evidence markers, the borrowed-through flags — these are the technical form of *don't confuse the window with the seer, and don't pretend the window was given when you assembled it*. They are how a deliberate grid-maker stays honest about what their windows are doing.

## What this borrowing does and does not include

Bruteau supplies *vocabulary* and the *seeing/seen distinction*. The architecture takes both.

What Bruteau supplies that the architecture does *not* inherit: her wrongness criteria for grids (the extinction principle, the community-viability test in *The Psychic Grid* Ch 1 and Ch 6). The architecture swaps in audit-fidelity to source — a different test, and a narrower one. Pass I checks that a deep reference's claims trace to the source it cites. It does not check that the source itself was well-chosen, nor that the assembled grid is generative rather than corrosive. Audit-fidelity is *necessary-but-not-sufficient* for what Bruteau is after: a grid can be source-faithful and still corrosive — sources well-cited, sources themselves consultant-derivative (the Larman/LLM-epistemology corollary at [`llm-epistemology.md`](llm-epistemology.md) is the same inheritance). The fidelity check rules out fabrication. It does not rule out faithful reproduction of a wrong corpus. That further check stays the operator's job. The architecture makes the job tractable; it does not do the job for you. The matrix is grid-assembly infrastructure with a fidelity-to-source check; it is not a contemplative practice and does not claim Bruteau's full ethical apparatus.

The persona/window claim above is a contemplative-tradition reading of why this architecture refuses personas as a lens kind. It runs parallel to a longer engineering tradition on the same point — Weizenbaum's 1976 ELIZA observation that users construct intentionality for systems whether or not the systems warrant it; Suchman's *Plans and Situated Actions* (1987) on how users improvise intent attribution from sparse cues — which arrives at compatible discipline by a different route. The architectural rule is overdetermined; this doc names the Bruteau route because it is the one that supplies the *vocabulary* (window, seer, conviction community) the engineering literature does not.

## Sources

- Beatrice Bruteau, *The Psychic Grid: How the Mind Operates*, Quest Books, 1979. In corpus at `references/bruteau-psychic-grid.md` (light) and `bruteau-psychic-grid-deep.md` (deep). Chapter citations above resolve there.
- Joseph Weizenbaum, *Computer Power and Human Reason*, W.H. Freeman, 1976.
- Lucy Suchman, *Plans and Situated Actions*, Cambridge University Press, 1987.
