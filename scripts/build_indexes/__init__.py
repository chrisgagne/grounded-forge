"""JSON runtime-index builders for the mechanical-index migration (Phase 3).

Three artefacts per corpus:

- ``reference-index.json``: file catalogue. Per-source fields come from a
  Sonnet semantic pass over the deep-ref frontmatter (free-form prose, not
  amenable to regex); mechanical fields (slug-table ID, ``**Scope:**``,
  light/deep line counts) are merged in by Python.
- ``concept-index.json``: concept axis. Built from per-source extraction
  artefacts at ``_planning/extracted/{corpus}/{slug}.json`` plus a Sonnet
  cross-link pass that decides aliasing/merging against the library's
  existing concept vocabulary.
- ``task-index.json``: per-task situation router. Replaces the
  ``{TASK}-DISTILLATION-INDEX.md`` artefacts.

The Phase-3 runtime contract: JSON ships *alongside* the existing ``.md``
indexes. Phase 4 will switch the retrieval skills to read JSON.
"""
