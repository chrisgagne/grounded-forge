# LinkedIn post: introducing grounded-forge

Plain text below (LinkedIn does not render markdown). The first two lines are
the hook — LinkedIn truncates around there, so they carry the click.

---

Your AI assistant doesn't give you the best thinking available. It gives you the most-published.

Here's the mechanism. Original thought leaders write slowly and rarely. Displaced managers become coaches, coaches become consultants, consultants become prolific content producers — and that derivative layer outwrites the primary sources by an order of magnitude. LLMs are trained on that written record, so they inherit the ratio. When your team asks a general-purpose model how to run an incident review or structure a hard decision, the default answer is the consultant-frequency consensus, not the sources you'd stake a real decision on. Web search doesn't fix it; it samples the same distribution.

I've open-sourced grounded-forge, my working answer to that problem — and a hands-on example of the principle I build everything around: LLMs where they earn their place, deterministic where consistency, auditability, and cost win.

The architecture: you pick the sources you trust. An LLM reads each one in full — not chunked — under a structured 9-pass protocol that produces verbatim-cited references and pre-projects each source onto every task domain your assistant serves: decision-making, stakeholder engagement, after-action review. A source-only audit checks every claim against the text before anything ships. At runtime there's no per-query synthesis and no hallucination lottery: the assistant routes to a pre-projected, pre-audited artefact and cites back to the source. You pay for the LLM's synthesis once, under audit. Every query after that is selection.

The demo ships 26 sources projected onto five task domains — 111 distillations, roughly 3,080 audited claims, 99.4% clean at first audit — compiled into five distributable assistants from one build command.

The evaluation results are published too, including where the architecture loses. On canonical public material, simpler approaches win and the matrix is overhead. It earns its keep where your organisation's knowledge actually lives: the non-public material — engagement documents, incident histories, your own frameworks — that no training run has seen and no model can route without help.

That's what AI transformation looks like above the coder-tooling layer: not a chatbot rollout, but deciding what your organisation treats as authoritative and building the machinery that holds the line.

Repo: https://github.com/chrisgagne/grounded-forge

If this is the conversation happening at your leadership table, I take fractional and advisory engagements — details in my About.

---

## Posting notes

- Confirm the repo is public before posting; the link 404s otherwise.
- No hashtags by design — the post targets C-level readers, not feed algorithms; add 2–3 niche ones (#AIStrategy #OperatingModel) only if reach matters more than register.
- The 99.4% figure measures internal consistency of the source-only protocol (same model family audits its own output), per README §Audit receipts and evals. If a commenter probes, that's the honest answer — and a good comment-thread moment, not a weakness.
- Strong first-comment candidate: the `diff -rq apps/decision apps/stakeholder` snippet from the README — two shipped assistants differing only by their task projection proves the matrix in three lines of terminal output.
