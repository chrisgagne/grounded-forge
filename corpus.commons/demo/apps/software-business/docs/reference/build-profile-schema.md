# Build profile schema

The fields of a `builds.yaml` profile entry. Authoritative source for forkers writing their own profile.

## Top-level shape

```yaml
defaults:
  source_dir: corpus.commons/demo
  output_base: ./corpus.commons/demo/apps

builds:
  {profile-slug}:
    description: "..."
    output_dir: ...
    max_scope: ...
    max_visibility: ...
    references: {...}
    distillations: {...}
    lenses: {...}
    skills: {...}
    agents: {...}
    claude_md: {...}
    docs: {...}
    validation: {...}
```

## Fields

### `defaults.source_dir`

Type: path (relative to repo root).
Required: yes.

The corpus root this build operates against. `corpus.commons/demo` for the shipped demo; a forker points this at their own corpus.

### `defaults.output_base`

Type: path (relative to repo root).
Required: yes.

The directory under which each profile's compiled app lands. Typically `./corpus.commons/{corpus}/apps/`. The packaging script (`npm run package`) writes tarballs to the sibling `distros/` directory.

### `description`

Type: string.
Required: yes.

One-sentence statement of what this app is for. Surfaced in `npm run list` output and in the compiled app's metadata.

### `output_dir`

Type: path (relative to repo root).
Required: yes.

Where this profile's compiled app lands. Conventionally `{output_base}/{profile-slug}`.

### `max_scope`

Type: one of `open` | `open-nc` | `copyrighted` | `confidential`.
Required: no. Default: `open-nc`.

The distribution-scope ceiling for this profile. References whose `**Scope:**` line exceeds this rank are excluded at build time. `personal` is never admissible at the build's `max_scope` filter (it can be authored as a frontmatter value but the build will refuse to ship it). See [`scope-taxonomy.md`](scope-taxonomy.md).

### `max_visibility`

Type: one of `open` | `open-nc` | `copyrighted` | `confidential`.
Required: no. Default: `open-nc`.

The lens-visibility ceiling for this profile. Lenses whose `visibility:` frontmatter exceeds this rank are excluded at build time. Parallel to `max_scope` but filters lenses (which carry their own visibility frontmatter), not references (which carry `Scope:`). `personal` is never admissible. The full visibility taxonomy mirrors the scope taxonomy.

### `references`

```yaml
references:
  include_patterns:
    - "*.md"
  exclude_patterns:
    - "_ingest_pass_*"
    - "_ingest_*"
```

Type: object.
Required: yes.

Glob patterns matched against files in `{source_dir}/references/`. `include_patterns` is the allow-list (typically just `*.md`). `exclude_patterns` removes audit scaffolding (`_ingest_*`) that lives alongside the references in the source repo but should not ship.

The build also unconditionally copies the runtime JSON indexes that sit at corpus root or alongside the references: `slug-table.json` (into `apps/{profile}/references/`), `reference-index.json` (into `apps/{profile}/`), and `concept-index.json` (into `apps/{profile}/`). These are not glob-filtered; they ship with every profile because the runtime skills inside the app read them on every query.

### `distillations`

```yaml
distillations:
  include:
    - decision-making
```

Type: object with `include` array.
Required: yes.

Names of task-axis subdirectories under `{source_dir}/distillations/` to ship. Each entry copies the full directory including the per-task distillation markdown index *and* its `task-index.json` runtime sibling. Typically one entry. Each app ships one column of the matrix.

### `lenses`

```yaml
lenses:
  include: true
```

Type: object with `include` boolean.
Required: no. Default: `false`.

If `true`, ships every lens spec at `{source_dir}/lenses/` plus the `LENS-INDEX.md`. Lenses are per-distillation modifiers shared across task axes; either you ship the library or you don't.

### `skills`

```yaml
skills:
  include:
    - matching-references
    - answer-from-corpus
```

Type: object with `include` array.
Required: no. Default: empty.

Names of skills under `.claude/skills/` to ship into the compiled app's `.claude/skills/`. Runtime skills (used by the assistant in the compiled app) go here. Maintainer skills (`ingesting-resources`, `creating-tasks`, etc.) stay in the source repo and should not be listed.

### `agents`

```yaml
agents:
  include:
    - aar-facilitator
```

Type: object with `include` array.
Required: no. Default: empty.

Names of agent definitions under `{source_dir}/.claude/agents/` (corpus-bound) to ship into the compiled app. Practitioner-role agents specialised for a task domain. In the demo, `aar-mode` ships `aar-facilitator` and `retro-mode` ships `retro-facilitator`; the three task-axis projection profiles (`decision`, `stakeholder`, `software-business`) ship none.

### `claude_md`

```yaml
claude_md:
  template: decision
```

Type: object with `template` string.
Required: yes.

Name of the profile template under `{source_dir}/build-profiles/{template}.md` (corpus-bound). The template ships into `{output_dir}/CLAUDE.md`. Briefs the assistant on the task domain and retrieval order.

### `docs`

```yaml
docs:
  include:
    - docs/architecture
    - docs/reference
```

Type: object with `include` array.
Required: no.

Paths under `docs/` to ship into the compiled app. The two demo-profile defaults are `docs/architecture` (so a reader of the compiled app can audit the pattern they're using) and `docs/reference` (vocabulary lookups for shipped lens specs).

### `validation.ignore_dangling`

Type: array of glob patterns.
Required: no.

Markdown links inside shipped files that the integrity check should *not* treat as broken. Use for legitimate dangling references: paths to the source repo that are not in the dist, cross-profile distillation directories, citations into a sibling library, etc.

The build's referential-integrity check reads every shipped markdown file, extracts each link, and checks that the target exists inside the dist. Patterns in `ignore_dangling` allow-list paths that intentionally do not resolve.

## See also

- The build itself at [`build.js`](../../build.js).
- The profile templates at `corpus.commons/demo/build-profiles/` (and `corpus.local/{corpus}/build-profiles/` for private corpora).
- The `creating-applications` skill at [`.claude/skills/creating-applications/SKILL.md`](../../.claude/skills/creating-applications/SKILL.md), which produces a new profile entry as part of authoring a new app.
