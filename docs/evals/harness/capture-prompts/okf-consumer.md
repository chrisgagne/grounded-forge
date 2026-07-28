# Generic OKF-consumer capture prompt (methods E and F)

The session prompt for capturing the OKF arms. Used verbatim for both E (the emitted, audited bundle) and F (the naive baseline) so the consumer is a constant and the bundle is the only variable. Open Claude Code bare in the bundle directory — no CLAUDE.md, no skills — paste the block below, then the eval prompt.

---

You are answering from the knowledge bundle in this directory.

1. Read `index.md` at the bundle root first, and route to the relevant concept files through the index files rather than scanning the tree. Links beginning with `/` are relative to the bundle root.
2. Ground every claim in a concept file you actually read, and name the file. If the bundle does not support a claim, say so rather than supplying it from general knowledge.
3. Where material you cite carries evidence markers (`[V]`, `[AP]`, `[AR]`, `[AE]`, `[BT]`), preserve them in your citations.
