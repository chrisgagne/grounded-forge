---
name: creating-corpus
description: Scaffold a new corpus under corpus.commons/ or corpus.local/: walk the operator through tier, naming, and task axes, then hand off to scripts/create-corpus.py for the filesystem work. The output is a self-contained corpus tree (sources, references, distillations, lenses, dist, distros) ready to receive material into sources/ingest/.
argument-hint: "[optional: rough corpus name or domain]"
---

# Creating Corpus

A corpus is the unit of self-contained material the matrix operates on: sources, references, distillations, lenses, builds, and packaged releases all live inside one folder. This skill scopes a new corpus—tier, domain, naming, task axes—and then invokes `scripts/create-corpus.py` to do the deterministic filesystem scaffold.

Dialogue skill, not a generator. The operator is in the conversation throughout. The skill produces scoping decisions captured in the corpus-level `README.md`; the script produces the directory tree.

## When to use

- The operator is forking the repo and wants to start a new corpus for their own domain.
- The operator already has one corpus and wants to start a second under a different domain or scope.
- The operator is unsure whether the work belongs in `corpus.commons/` or `corpus.local/` and wants to talk through the tier decision before committing.
- The operator has rough idea of what they want to read into a corpus but hasn't named the task axes yet.

## When not to use

- The operator already has the scoping decisions made (corpus name, tier, task axes) and wants to skip the dialogue. Run `python scripts/create-corpus.py {target} --tasks t1,t2` directly.
- The operator wants to ingest a single source: that's `ingesting-resources`, not this skill.
- The operator wants to add a *task axis* to an existing corpus: that's `creating-tasks` (scope the axis) plus `creating-applications` (assemble the application), not this skill.

## Inputs

- Optional: a rough corpus name or domain ("a coaching corpus", "management sciences", "anthropic-cookbook").
- Optional: existing related corpora; the new corpus might overlap with `corpus.commons/demo/` or with an operator's existing `corpus.local/` corpora.

## Output

Three things, in order:

1. **Scoping decisions** confirmed in the dialogue: tier, slug, task axes, scope range, intended first sources.
2. **`scripts/create-corpus.py` invocation** the operator runs (or the skill runs with operator confirmation): produces the corpus tree with stub indexes and a corpus-level README.
3. **The corpus-level `README.md`** with the dialogue's scoping decisions captured: domain, owner, scope, licence, task axes, intended first sources.

## Phase 0: Frame the work

State what's coming. Read aloud to the operator:

> A corpus is a self-contained directory: sources, references, distillations, lenses, builds, packaged releases, all inside one folder. The first decision is *tier*: `corpus.commons/` is tracked and shareable, `corpus.local/` is gitignored and private. The second is *task axes*: what does this corpus help its consumer *do*? After this dialogue we'll invoke the deterministic scaffolder; you'll fill in sources separately via the ingesting-resources skill.

Confirm the operator wants to proceed.

## Phase 1: Tier decision

The corpus lives in one of two tiers:

- **`corpus.commons/`**: tracked in git; ships when the repo ships. **Admission rule:** everything in `corpus.commons/` must be redistributable under an open or open-nc licence. Future contributors PR new corpora here.
- **`corpus.local/`**: gitignored; never enters the public repo. Any scope is fine (operator's call). The operator's working corpora live here.

Three diagnostic questions sharpen the choice:

a. **Is every source you intend to ingest covered by an open or open-nc licence?** If yes, `corpus.commons/` is admissible. If no, or if any source is `copyrighted`, `confidential`, or `personal`, the corpus belongs in `corpus.local/`.

b. **Do you have explicit permission to redistribute the *derived artefacts* (deep references, distillations) as well as the sources?** Some licences allow citation but not redistribution of substantive paraphrase. If unclear, default to `corpus.local/` and decide later. *Folder moves between tiers* are the only re-tier operation; nothing structural changes.

c. **Is this corpus material you want to make available to other operators?** Even open-licensed material doesn't have to go in `corpus.commons/`: that tier is for material the operator is willing to vouch for under their handle as part of the public repo's contribution surface. `corpus.local/` is fine for "this is open-licensed but I don't want to maintain it as a public artefact."

Commit the tier in one short paragraph: which tier, and why. The tier is provisional through Phase 2; if the scope discovery in Phase 4 surfaces material above the tier's admission ceiling, restart this phase.

## Phase 2: Domain and naming

Every corpus has a domain. Name it in verbs and nouns: what does this corpus help its consumer *do*? Not "a coaching corpus": that's a genre. *"A corpus for facilitating blameless incident reviews and post-action retrospectives in engineering teams, grounded in resilience-engineering and adjacent organisational-behaviour material (Dekker, Edmondson, Cook, Rasmussen)."*: that's a domain.

Slug conventions:

- **`corpus.commons/{contributor-or-org}-{domain}/`**: the contributor's handle or organisation prefixes the slug for namespacing. *"chrisgagne-management-sciences"*, *"anthropic-cookbook"*. PRs vouch for the corpus under the contributor's name.
- **`corpus.local/{any-slug}/`**: operator's choice. No namespacing required; the tier is private.

The dialogue's task: produce a one-paragraph domain statement and confirm the slug.

## Phase 3: Task axes

A task axis is what the consumer of the corpus *does* with it. One source can be projected onto multiple task axes; each projection is a distinct distillation. Choose deliberately.

Discipline:

- **One is the minimum.** A corpus with no task axis is unprojected source material.
- **Two or three is typical.** Most corpora serve a handful of related task domains.
- **More than four is usually unmerged task axes.** If the operator names six, push back: are some sub-modes of one task? *"Decision-making"* covers *"choosing a strategy"*, *"choosing a hire"*, *"choosing a vendor"*: those are sub-modes.

Each task axis is a verb-and-noun job (matches the `creating-tasks` discipline). *"Decision-making"* is acceptable. *"Strategy"* is not.

The dialogue's task: name the task axes as comma-separated slugs (kebab-case), confirm each is a verb-and-noun job, and check the count is in [1, 4] unless the operator explicitly defends more.

The scaffold stops at slugs and directory stubs; full task scoping is downstream work in `creating-tasks`. Stubs include placeholders for both routing layers (phase-routing macro, runtime listener micro); if `creating-tasks` later produces a task spec with a field-2a seed table, `creating-applications` seeds the listener-table placeholders from it.

## Phase 4: First sources (optional)

If the operator has a clear set of first sources in mind, name three to five. The point isn't to ingest them now (that's `ingesting-resources`); it's to:

- **Sanity-check scope.** If the operator names a copyrighted source while targeting `corpus.commons/`, the tier needs to change or the source needs to go elsewhere. If the operator names a CC-BY-SA source while targeting `corpus.commons/` with `max_scope: open-nc`, the build's scope filter will admit it but the operator should know.
- **Sanity-check the task-axis choice.** If the named sources don't map naturally onto the named task axes, one or the other is wrong.
- **Anchor the corpus-level README.** The intended-first-sources list goes into the README so future readers understand what the corpus was built around.

If the operator doesn't have first sources in mind, that's fine: they can hand off to `finding-resources` to triage candidates after the scaffold. The skill records this as "first sources TBD" in the README.

## Phase 5: Scaffold

Recommend the script invocation. Hand off:

> Run `python scripts/create-corpus.py {target-path} --tasks {comma-separated-slugs}` to scaffold. The script auto-creates the parent tier directory if missing, refuses if the target is non-empty, and lays out the standard tree. The scoping decisions from this dialogue go into the corpus-level README the script generates: paste them in afterwards, or have the skill open the README and edit it directly.

After the operator runs the script (or after the skill runs it with operator confirmation), the corpus exists. The dialogue's last act is to **populate the corpus-level README** with the scoping decisions: domain paragraph, owner, scope range, licence summary, named task axes, intended first sources.

## Phase 6: Hand-off

Name the next steps explicitly:

1. **Drop sources** into `{target-path}/sources/ingest/`. The `finding-resources` skill helps triage candidates before commit.
2. **Run `ingesting-resources`** against each source. The skill runs the 9-pass protocol and lands the source-card sidecar in `sources/original/`, the converted markdown in `sources/converted/`, deep + light references, and per-task distillations.
3. **Configure `builds.yaml`**: point a profile at this corpus when ready to ship.
4. **`npm run build`.** Compiled output lands in `{target-path}/apps/{profile}/`.

## Failure modes to watch in the dialogue

- **Tier ambiguity.** The operator says "I'm not sure" and tries to scaffold under `corpus.commons/` to keep options open. Push back: defaults that leak private material into the public tier are the worst-case outcome. If unsure, scaffold under `corpus.local/`: moving the folder later is cheap.

- **Task axes without verbs.** The operator names axes like *"strategy"* or *"leadership"*. These are domains, not jobs. Ask: *what does the consumer of this corpus do under this axis?* The verb-and-noun answer is the axis name.

- **One axis named twice with different words.** *"Decision-making"* and *"prioritisation"* both name "choosing under constraint." If the diagnostic questions for both axes overlap by more than ~70%, they're one axis.

- **Domain-stuck on the corpus's seed source.** The operator describes the corpus as *"a corpus of Anderson's writing"*. That's not a domain, it's an inventory. Ask: *what does Anderson's writing help the consumer do?* The answer is the domain; Anderson is a means to that domain.

- **Premature ingestion talk.** The operator wants to start dropping PDFs into `sources/ingest/` before the dialogue closes. Hold the dialogue line through Phase 5; the scaffold needs the task axes to lay out the right directories.

## Discipline (binding)

- *Tier decision before scaffold.* The script needs a tier (inferred from path or explicit `--tier`). The skill won't recommend the script invocation until tier is confirmed.
- *At least one task axis.* A corpus with zero task axes is unprojected source material, not a matrix corpus.
- *README captured.* The dialogue's scoping decisions go into the corpus-level README. Future operators (and contributors) read the README to understand what the corpus is for; if it's empty, the corpus has no spine.
