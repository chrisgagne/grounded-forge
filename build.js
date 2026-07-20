#!/usr/bin/env node

/**
 * grounded-forge build system
 *
 * Compiles each profile in builds.yaml into apps/{profile-name}/.
 *
 * Apps ship distillations as the source-grounded product. The reference
 * tier (light + deep) stays at corpus level as the audit-of-record but
 * does not travel with the compiled application. Each profile is a slice
 * of the matrix: ONE task-domain's distillation directory (per-task
 * distillation index, lenses, skills, CLAUDE.md). Same sources behind
 * the scenes; different task projections per profile.
 *
 * Usage:
 *   node build.js [profile]   Build one profile
 *   node build.js --all       Build all profiles
 *   node build.js --list      List profiles
 *   node build.js --clean     Remove apps/
 */

const fs = require("fs");
const path = require("path");
const yaml = require("js-yaml");

const CONFIG_FILE = "builds.yaml";

// Distribution scope taxonomy. Lower rank = lower distribution risk.
// A profile's max_scope sets the ceiling; distillations whose source's
// Scope: rank exceeds the ceiling are excluded from that profile's app/.
// `personal` has rank 4 and no max_scope value admits it: personal
// material is mechanically unshippable. Scope is read from the deep ref
// frontmatter at build time (the deep ref is a build-time input, not a
// runtime artefact — apps ship distillations only).
const SCOPE_RANK = {
  open: 0,
  "open-nc": 1,
  copyrighted: 2,
  confidential: 3,
  personal: 4,
};
const ADMITTABLE_SCOPES = ["open", "open-nc", "copyrighted", "confidential"];
const DEFAULT_MAX_SCOPE = "open-nc";

// Lens-visibility taxonomy. Borrowed verbatim from reference Scope: the same
// five levels, the same monotonic risk gradient, applied to lens specs. A
// profile's max_visibility sets the ceiling; lenses whose visibility: rank
// exceeds the ceiling do not ship in that profile's app. `personal` lenses
// ship in no profile by default; an operator opts in with an explicit
// max_visibility: personal. See docs/architecture/capability-binding.md for
// the parallel with Scope.
const VISIBILITY_RANK = {
  open: 0,
  "open-nc": 1,
  copyrighted: 2,
  confidential: 3,
  personal: 4,
};
const ADMITTABLE_VISIBILITIES = [
  "open",
  "open-nc",
  "copyrighted",
  "confidential",
  "personal",
];
const DEFAULT_MAX_VISIBILITY = "open-nc";
// Visibilities above this rank cannot live under corpus.commons/; the
// spec-location gate refuses to start the build if any do.
const COMMONS_MAX_VISIBILITY_RANK = VISIBILITY_RANK["open-nc"];

class MatrixBuilder {
  constructor(configPath) {
    this.config = yaml.load(fs.readFileSync(configPath, "utf8"));
    // repoRoot is always the directory builds.yaml sits in — that's where
    // the substrate lives (skills, docs, root README). Build-profile
    // templates are corpus-bound and live under {source_dir}/build-profiles/.
    this.repoRoot = path.resolve(path.dirname(configPath));
    // Default source dir from the file-level defaults block. Profiles can
    // override with their own `source_dir:` key to point at a different
    // corpus (e.g. a private corpus under corpus.local/ while
    // corpus.commons/demo serves the open-source profiles).
    const configuredSrc = this.config.defaults?.source_dir || ".";
    this.defaultSourceDir = path.resolve(this.repoRoot, configuredSrc);
    this.sourceDir = this.defaultSourceDir;

    // Discover per-corpus builds.yaml files and merge their `builds:` entries
    // into the substrate profile set. Substrate builds.yaml carries only the
    // public profile set; private profiles travel inside their corpus root
    // and stay behind the corpus.local/ gitignore boundary. Conflict policy:
    // log and skip — name collisions are configuration bugs.
    this._mergePerCorpusProfiles();
  }

  _mergePerCorpusProfiles() {
    if (!this.config.builds) this.config.builds = {};
    const tierGlobs = [
      path.join(this.repoRoot, "corpus.commons"),
      path.join(this.repoRoot, "corpus.local"),
    ];
    for (const tier of tierGlobs) {
      if (!fs.existsSync(tier)) continue;
      const corpora = fs
        .readdirSync(tier, { withFileTypes: true })
        .filter((e) => e.isDirectory())
        .map((e) => path.join(tier, e.name));
      for (const corpus of corpora) {
        const corpusConfig = path.join(corpus, "builds.yaml");
        if (!fs.existsSync(corpusConfig)) continue;
        const loaded = yaml.load(fs.readFileSync(corpusConfig, "utf8"));
        if (!loaded || !loaded.builds) continue;
        for (const [name, profile] of Object.entries(loaded.builds)) {
          if (this.config.builds[name]) {
            console.warn(
              `[builds] WARN: profile '${name}' from ${path.relative(this.repoRoot, corpusConfig)} collides with substrate profile; skipping the corpus version.`
            );
            continue;
          }
          this.config.builds[name] = profile;
        }
      }
    }
  }

  async buildProfile(profileName) {
    const profile = this.config.builds[profileName];
    if (!profile) {
      throw new Error(`Unknown build profile: ${profileName}`);
    }

    if (profile.source_dir) {
      this.sourceDir = path.resolve(this.repoRoot, profile.source_dir);
    } else {
      this.sourceDir = this.defaultSourceDir;
    }

    console.log(`\n${"=".repeat(60)}`);
    console.log(`Building: ${profileName}`);
    console.log(`Description: ${profile.description}`);
    console.log(`Source:      ${path.relative(this.repoRoot, this.sourceDir) || "."}`);
    console.log("=".repeat(60));

    const outputDir = path.resolve(this.repoRoot, profile.output_dir);

    if (fs.existsSync(outputDir)) {
      fs.rmSync(outputDir, { recursive: true });
    }
    fs.mkdirSync(outputDir, { recursive: true });

    await this.buildCorpusIndexes(profile, outputDir);
    await this.buildDistillations(profile, outputDir);
    await this.buildLenses(profile, outputDir);
    await this.buildSkills(profile, outputDir);
    await this.buildAgents(profile, outputDir);
    await this.buildClaudeMd(profile, outputDir);
    await this.buildAgentsMd(profile, outputDir);
    await this.buildDocs(profile, outputDir);
    await this.copyMisc(profile, outputDir, profileName);

    await this.validate(profile, outputDir, profileName);

    console.log(`\nComplete: ${outputDir}`);
    return outputDir;
  }

  // Apps ship distillations as the source-grounded product. The reference
  // tier (light + deep) stays at corpus level as the audit-of-record but
  // does not travel with the compiled application. This method ships only
  // the runtime JSON indexes that remain meaningful in a dist-only app:
  //
  //   - slug-table.json: id ↔ slug map, still needed for distillation
  //     file-path resolution (slug → distillations/{task}/{slug}-{task}.md).
  //   - concept-index.json: dist-only variant — pointers into distillation
  //     files, not deep refs. Built by scripts/build_indexes/.
  //
  // reference-index.json is not shipped: per-source attribution is carried
  // in the distillation prose (each distillation names author + title in
  // its first paragraph). Light and deep .md references are not shipped.
  //
  // Scope filtering moves to buildDistillations: a distillation inherits
  // the scope of its source's deep ref (read at build time from the
  // corpus, which has all deep refs as build-time inputs).
  async buildCorpusIndexes(profile, outputDir) {
    // Validate scope ceiling up-front so the per-distillation filter in
    // buildDistillations has a vetted maxRank to compare against.
    const maxScope = profile.max_scope ?? DEFAULT_MAX_SCOPE;
    if (!ADMITTABLE_SCOPES.includes(maxScope)) {
      throw new Error(
        `Invalid max_scope '${maxScope}' in profile. Must be one of: ${ADMITTABLE_SCOPES.join(", ")}`
      );
    }

    // slug-table.json lives under references/ in the source corpus; ship
    // it at the app root since the references/ directory no longer exists
    // in the app. Path consumers in skills need to be updated accordingly.
    const slugTableSrc = path.join(this.sourceDir, "references", "slug-table.json");
    if (fs.existsSync(slugTableSrc)) {
      fs.copyFileSync(slugTableSrc, path.join(outputDir, "slug-table.json"));
    }
    // concept-index.json lives at the corpus root; ship a stripped
    // variant at app root. The corpus-level index carries (section,
    // md_line) pointers into deep refs — useful for operators but dead
    // pointers in dist-only apps. Strip those fields here; the runtime
    // resolves the concept inside the distillation itself (distillations
    // are small enough to full-read). A future build step can rebuild
    // pointers into distillation files for in-source-section routing.
    const conceptIndexSrc = path.join(this.sourceDir, "concept-index.json");
    if (fs.existsSync(conceptIndexSrc)) {
      const raw = JSON.parse(fs.readFileSync(conceptIndexSrc, "utf8"));
      const stripped = this.stripConceptIndexPointers(raw);
      fs.writeFileSync(
        path.join(outputDir, "concept-index.json"),
        JSON.stringify(stripped, null, 2)
      );
    }

    console.log(`  Corpus indexes: shipped (max_scope: ${maxScope}; references not shipped)`);
  }

  async buildDistillations(profile, outputDir) {
    const distConfig = profile.distillations;
    if (!distConfig || !distConfig.include?.length) {
      console.log("  Distillations: 0 (none configured)");
      return;
    }

    // Scope-ceiling check. Apps don't ship references, so the scope gate
    // runs on distillations: a distillation inherits its source's scope,
    // read from the deep ref's frontmatter at corpus level. The deep ref
    // is a build-time input, not a runtime artefact. Distillations whose
    // source exceeds max_scope are skipped.
    const maxScope = profile.max_scope ?? DEFAULT_MAX_SCOPE;
    const maxRank = SCOPE_RANK[maxScope];
    const refDir = path.join(this.sourceDir, "references");

    // Scopes whose deep refs are not openly redistributable. Distillations
    // from sources at these scopes must NOT carry [V] verbatim quotes in
    // the shipped app — paraphrased prose with [AP] attribution only.
    // The deep ref still carries audited [V] passages at corpus level for
    // Pass D audit; what changes here is what travels with the app.
    const VERBATIM_RESTRICTED_SCOPES = new Set([
      "copyrighted",
      "confidential",
      "personal",
    ]);
    // The [V] marker is the verbatim guarantee — its presence in a
    // distillation means the surrounding quoted text is exact source text,
    // copied from a Pass-D-audited deep-ref passage. The other markers
    // ([AP] paraphrase, [AR] argument, [AE] example, [BT] borrowed-through)
    // attribute claims without guaranteeing exact source text.
    const VERBATIM_MARKER_RE = /\[V\]/;

    let total = 0;
    const skippedReasons = [];
    const verbatimViolations = [];
    // Provenance of the shipped distillations' sources, keyed by slug.
    // Dist-only apps carry no references/, so this is how the packager
    // learns the bundle's distribution scope (see below, and package.js).
    const shippedSources = new Map();
    for (const taskDir of distConfig.include) {
      const srcDir = path.join(this.sourceDir, "distillations", taskDir);
      const destDir = path.join(outputDir, "distillations", taskDir);

      if (!fs.existsSync(srcDir)) {
        console.log(`    Warning: distillation dir '${taskDir}' not found`);
        continue;
      }

      fs.mkdirSync(destDir, { recursive: true });

      const excludes = distConfig.exclude || [];
      const candidates = fs
        .readdirSync(srcDir)
        .filter(
          (f) =>
            f.endsWith(".md") &&
            fs.statSync(path.join(srcDir, f)).isFile()
        )
        .filter((f) => !excludes.includes(f));

      for (const file of candidates) {
        // Index files and READMEs are not source-projected distillations;
        // ship them through without a scope check.
        const isProjection = /^[a-z0-9].*-[a-z-]+\.md$/.test(file)
          && file !== "README.md"
          && !/-DISTILLATION-INDEX\.md$/i.test(file);

        if (isProjection) {
          // Strip the task suffix to get the source slug: e.g.
          // openstax-business-ethics-decision-making.md → openstax-business-ethics
          const taskSuffix = `-${taskDir}.md`;
          if (!file.endsWith(taskSuffix)) {
            // Lens-variant or other shape (e.g. {slug}-{task}-{lens}.md);
            // skip the scope check for now. Lens-variant scope handling
            // is a follow-up.
          } else {
            const slug = file.slice(0, -taskSuffix.length);
            const deepRefPath = path.join(refDir, `${slug}-deep.md`);
            if (fs.existsSync(deepRefPath)) {
              const body = fs.readFileSync(deepRefPath, "utf8");
              const m = body.match(/^\*\*Scope:\*\*\s*(\S+)/m);
              const scope = m ? m[1] : null;
              if (scope === null) {
                skippedReasons.push(`scope missing on source ${slug}: ${taskDir}/${file}`);
                continue;
              }
              if (!(scope in SCOPE_RANK)) {
                skippedReasons.push(`scope unknown '${scope}' on source ${slug}: ${taskDir}/${file}`);
                continue;
              }
              if (scope === "personal" || SCOPE_RANK[scope] > maxRank) {
                skippedReasons.push(`scope ${scope} > ${maxScope} on source ${slug}: ${taskDir}/${file}`);
                continue;
              }
              // Record the source's scope + licence for the app's provenance
              // manifest. The app ships no references/, so without this the
              // packager cannot compute the bundle's scope and would mislabel
              // a copyrighted bundle as 'open'.
              // Licence value follows "Licence:"/"License:" (the label may be
              // bold-wrapped, `**License:**`). Capture to end-of-line only, then
              // strip markdown and trailing prose so a one-line value survives
              // and a multi-line deep-ref body cannot leak in.
              const licM = body.match(/licen[cs]e[d]?:\*{0,2}\s*([^\n]+)/i);
              let licence = "unknown";
              if (licM) {
                const cleaned = licM[1]
                  .replace(/\*+/g, "")
                  .split(/\s{2,}|\.\s|;/)[0]
                  .replace(/[.\s]+$/, "")
                  .trim();
                if (cleaned && cleaned.length <= 80) licence = cleaned;
              }
              shippedSources.set(slug, { slug, scope, licence });
              // Verbatim gate: when the source's scope is not openly
              // redistributable, [V] markers in the distillation are a
              // copyright / confidentiality leak. The deep ref keeps the
              // audited verbatim at corpus level; the app cannot.
              if (VERBATIM_RESTRICTED_SCOPES.has(scope)) {
                const distBody = fs.readFileSync(path.join(srcDir, file), "utf8");
                if (VERBATIM_MARKER_RE.test(distBody)) {
                  verbatimViolations.push({
                    slug,
                    scope,
                    file: `${taskDir}/${file}`,
                  });
                }
              }
            }
            // If the deep ref doesn't exist at corpus level, the
            // distillation is an orphan — ship it but flag it (a real
            // ingestion would have produced the deep before the
            // distillation; this branch covers borrowed-through-only
            // distillations and pre-Pass-G drafts).
          }
        }

        const raw = fs.readFileSync(path.join(srcDir, file), "utf8");
        const stripped = this.stripVerificationArtifacts(raw);
        const rewritten = this.rewriteCorpusPaths(stripped);
        fs.writeFileSync(path.join(destDir, file), rewritten);
        total++;
      }

      // Ship the per-axis runtime task-index alongside the .md distillations.
      const taskIndexSrc = path.join(srcDir, "task-index.json");
      if (fs.existsSync(taskIndexSrc)) {
        fs.copyFileSync(taskIndexSrc, path.join(destDir, "task-index.json"));
      }
    }

    // Emit the provenance manifest the packager reads for scope labelling.
    // The bundle's scope is the most-restrictive scope across the SHIPPED
    // distillations' sources — recorded here, consumed by scripts/package.js.
    const provenanceRows = [...shippedSources.values()].sort((a, b) =>
      a.slug.localeCompare(b.slug)
    );
    let mrScope = "open";
    let mrRank = -1;
    for (const s of provenanceRows) {
      const rank = SCOPE_RANK[s.scope];
      if (rank > mrRank) {
        mrRank = rank;
        mrScope = s.scope;
      }
    }
    fs.writeFileSync(
      path.join(outputDir, "distillation-sources.json"),
      JSON.stringify(
        { most_restrictive_scope: mrScope, sources: provenanceRows },
        null,
        2
      ) + "\n"
    );

    if (skippedReasons.length > 0) {
      console.log(`  Distillations: ${total} files copied (${skippedReasons.length} skipped by scope ceiling: ${maxScope})`);
      for (const r of skippedReasons) console.log(`    ${r}`);
    } else {
      console.log(`  Distillations: ${total} files copied (max_scope: ${maxScope})`);
    }

    if (verbatimViolations.length > 0) {
      const lines = [
        `Verbatim-scope violation in ${verbatimViolations.length} distillation(s).`,
        `Pass G must not write [V] markers when the source's Scope: is copyrighted,`,
        `confidential, or personal. Paraphrase with [AP] attribution instead.`,
        `See .claude/skills/creating-distillations/projection-protocol.md`,
        `(§Citation discipline → Scope gates the verbatim register).`,
        ``,
        `Offending files:`,
      ];
      for (const v of verbatimViolations) {
        lines.push(`  - ${v.file} (source ${v.slug}, Scope: ${v.scope})`);
      }
      throw new Error(lines.join("\n"));
    }
  }

  async buildLenses(profile, outputDir) {
    const lensConfig = profile.lenses;
    if (!lensConfig || lensConfig.include !== true) {
      console.log("  Lenses: 0 (not configured for this profile)");
      return;
    }

    const srcDir = path.join(this.sourceDir, "lenses");
    const destDir = path.join(outputDir, "lenses");

    if (!fs.existsSync(srcDir)) {
      console.log("  Lenses: source dir missing");
      return;
    }

    const maxVisibility = profile.max_visibility ?? DEFAULT_MAX_VISIBILITY;
    if (!ADMITTABLE_VISIBILITIES.includes(maxVisibility)) {
      throw new Error(
        `Invalid max_visibility '${maxVisibility}' in profile. Must be one of: ${ADMITTABLE_VISIBILITIES.join(", ")}`
      );
    }
    const maxRank = VISIBILITY_RANK[maxVisibility];

    // The explicit exclude: list is a secondary override for one-off cases.
    // Primary admission is visibility-driven.
    const excludes = lensConfig.exclude || [];
    const candidates = fs
      .readdirSync(srcDir)
      .filter(
        (f) =>
          f.endsWith(".md") && fs.statSync(path.join(srcDir, f)).isFile()
      )
      .filter((f) => f !== "LENS-INDEX.md" && f !== "README.md")
      .filter((f) => !excludes.includes(f));

    const shipped = [];
    const skippedReasons = [];
    for (const f of candidates) {
      const visibility = this.readLensVisibility(path.join(srcDir, f));
      if (visibility === null) {
        throw new Error(
          `Lens ${path.join(srcDir, f)} is missing 'visibility:' in frontmatter. Required field.`
        );
      }
      if (!(visibility in VISIBILITY_RANK)) {
        throw new Error(
          `Lens ${path.join(srcDir, f)} has unknown visibility '${visibility}'. Must be one of: ${Object.keys(VISIBILITY_RANK).join(", ")}.`
        );
      }
      if (VISIBILITY_RANK[visibility] > maxRank) {
        skippedReasons.push(`visibility ${visibility} > ${maxVisibility}: ${f}`);
        continue;
      }
      shipped.push({ file: f, visibility });
    }

    if (shipped.length === 0) {
      const skippedNote = skippedReasons.length > 0
        ? ` (${skippedReasons.length} skipped by visibility ceiling: ${maxVisibility})`
        : "";
      console.log(`  Lenses: 0 files matched${skippedNote}`);
      for (const r of skippedReasons) console.log(`    ${r}`);
      return;
    }

    fs.mkdirSync(destDir, { recursive: true });
    for (const { file } of shipped) {
      this.copyFileRewriting(
        path.join(srcDir, file),
        path.join(destDir, file)
      );
    }

    // Regenerate LENS-INDEX.md from the shipped set so the table reflects
    // only the lenses that travelled. Copy-then-filter approach: read the
    // source LENS-INDEX, add a Visibility column header, keep only rows
    // whose slug matches a shipped lens, drop rows for lenses that did not
    // ship. Adds the visibility cell from the shipped lens's frontmatter.
    const sourceIndexPath = path.join(srcDir, "LENS-INDEX.md");
    if (fs.existsSync(sourceIndexPath)) {
      const rewritten = this.regenerateLensIndex(sourceIndexPath, shipped);
      fs.writeFileSync(path.join(destDir, "LENS-INDEX.md"), rewritten);
    }

    // Ship the runtime lens-index.json alongside the .md lens specs.
    // It lives one directory up at the corpus root (siblings:
    // reference-index.json, concept-index.json).
    const lensIndexSrc = path.join(this.sourceDir, "lens-index.json");
    if (fs.existsSync(lensIndexSrc)) {
      fs.copyFileSync(lensIndexSrc, path.join(outputDir, "lens-index.json"));
    }

    const skippedCount = skippedReasons.length;
    if (skippedCount > 0) {
      console.log(
        `  Lenses: ${shipped.length} files copied (${skippedCount} skipped by visibility ceiling: ${maxVisibility})`
      );
      for (const r of skippedReasons) console.log(`    ${r}`);
    } else {
      console.log(`  Lenses: ${shipped.length} files copied (max_visibility: ${maxVisibility})`);
    }
  }

  // Read the visibility: field from a lens spec's YAML frontmatter.
  // Returns the value as a string, or null if the field is absent.
  readLensVisibility(filePath) {
    const body = fs.readFileSync(filePath, "utf8");
    if (!body.startsWith("---")) return null;
    const end = body.indexOf("\n---", 3);
    if (end === -1) return null;
    const frontmatter = body.slice(3, end);
    const m = frontmatter.match(/^visibility:\s*(\S+)\s*$/m);
    return m ? m[1] : null;
  }

  // Walk every lens under corpus.commons/ and refuse the build if any
  // carries a visibility above 'open-nc'. The two higher tiers belong
  // under corpus.local/ — a gitignored tree where confidential and
  // personal material lives. The check is a hard gate: it runs before
  // any profile builds, exits non-zero on the first violation.
  enforceCommonsVisibilityGate() {
    const commonsRoot = path.join(this.repoRoot, "corpus.commons");
    if (!fs.existsSync(commonsRoot)) return;
    const violations = [];
    const corpora = fs
      .readdirSync(commonsRoot, { withFileTypes: true })
      .filter((e) => e.isDirectory())
      .map((e) => e.name);
    for (const corpus of corpora) {
      const lensDir = path.join(commonsRoot, corpus, "lenses");
      if (!fs.existsSync(lensDir)) continue;
      const files = fs
        .readdirSync(lensDir)
        .filter(
          (f) =>
            f.endsWith(".md") &&
            f !== "LENS-INDEX.md" &&
            f !== "README.md" &&
            fs.statSync(path.join(lensDir, f)).isFile()
        );
      for (const f of files) {
        const lensPath = path.join(lensDir, f);
        const visibility = this.readLensVisibility(lensPath);
        if (visibility === null) {
          throw new Error(
            `Lens ${lensPath} is missing 'visibility:' in frontmatter. Required field.`
          );
        }
        if (!(visibility in VISIBILITY_RANK)) {
          throw new Error(
            `Lens ${lensPath} has unknown visibility '${visibility}'. Must be one of: ${Object.keys(VISIBILITY_RANK).join(", ")}.`
          );
        }
        if (VISIBILITY_RANK[visibility] > COMMONS_MAX_VISIBILITY_RANK) {
          violations.push({ path: lensPath, visibility });
        }
      }
    }
    if (violations.length > 0) {
      const v = violations[0];
      throw new Error(
        `Lens ${v.path} has visibility=${v.visibility}; lenses above 'open-nc' cannot live under corpus.commons/. Move to corpus.local/.`
      );
    }
  }

  // Filter the source LENS-INDEX.md table to the shipped lens set and
  // splice in a Visibility column. Rows whose slug does not match any
  // shipped lens are dropped. Non-table content (intro, status, kinds,
  // retrieval discussion) passes through unchanged.
  regenerateLensIndex(sourceIndexPath, shipped) {
    const shippedBySlug = new Map();
    for (const { file, visibility } of shipped) {
      const slug = file.replace(/\.md$/, "");
      shippedBySlug.set(slug, visibility);
    }

    const original = fs.readFileSync(sourceIndexPath, "utf8");
    const lines = original.split("\n");
    const out = [];
    let inTable = false;
    let columnCount = 0;
    let sourceHasVisibility = false;

    for (const line of lines) {
      // Table header row: '| Kind | Slug | Purpose ... |' or '| Kind | Slug | Visibility | Purpose ... |'
      if (/^\|\s*Kind\s*\|/.test(line)) {
        inTable = true;
        sourceHasVisibility = /^\|\s*Kind\s*\|\s*Slug\s*\|\s*Visibility\s*\|/.test(line);
        if (sourceHasVisibility) {
          // Source already carries Visibility; pass header through and count its columns.
          columnCount = (line.match(/\|/g) || []).length - 1;
          out.push(line);
        } else {
          // Splice a Visibility column after Slug (column index 2).
          const cells = line.split("|").slice(1, -1).map((c) => c);
          const newCells = [cells[0], cells[1], " Visibility ", ...cells.slice(2)];
          columnCount = newCells.length;
          out.push("|" + newCells.join("|") + "|");
        }
        continue;
      }
      // Separator row: '|---|---|---|---|---|'
      if (inTable && /^\|[\s\-:|]+\|\s*$/.test(line)) {
        const dashCells = Array(columnCount).fill("---");
        out.push("|" + dashCells.join("|") + "|");
        continue;
      }
      // Data row in table: '| archetype | [slug](slug.md) | ... |'
      if (inTable && line.startsWith("|") && line.trim().endsWith("|")) {
        const cells = line.split("|").slice(1, -1);
        // Slug cell is the second column; extract '[text](path.md)' -> 'text'.
        const slugCell = cells[1] || "";
        const slugMatch = slugCell.match(/\[([^\]]+)\]/);
        const slug = slugMatch ? slugMatch[1] : slugCell.trim();
        if (!shippedBySlug.has(slug)) {
          // Drop the row entirely.
          continue;
        }
        const visibility = shippedBySlug.get(slug);
        let newCells;
        if (sourceHasVisibility) {
          // Source already has Visibility column at index 2; overwrite it with the
          // visibility we read from frontmatter (authoritative; the source-catalogue
          // cell could drift). Other cells pass through.
          newCells = [cells[0], cells[1], ` ${visibility} `, ...cells.slice(3)];
        } else {
          // Splice Visibility cell after Slug.
          newCells = [cells[0], cells[1], ` ${visibility} `, ...cells.slice(2)];
        }
        out.push("|" + newCells.join("|") + "|");
        continue;
      }
      // First non-table line after the table closes — leave alone.
      if (inTable && !line.startsWith("|")) {
        inTable = false;
      }
      out.push(line);
    }
    return out.join("\n");
  }

  async buildSkills(profile, outputDir) {
    const skillsConfig = profile.skills || {};
    const includes = skillsConfig.include || [];
    if (includes.length === 0) {
      console.log("  Skills: 0 (none configured)");
      return;
    }

    const substrateDir = path.join(this.repoRoot, ".claude/skills");
    const corpusDir = path.join(this.sourceDir, ".claude/skills");
    const destDir = path.join(outputDir, ".claude/skills");
    // Dual-runtime: emit the same skills under .agents/skills/ so an
    // AGENTS.md-aware runtime (Codex and others) discovers them without a
    // symlink. Plain copies survive every distribution path (Windows clone,
    // ZIP download, tarball) that a symlink would break in a forked repo.
    const agentsDestDir = path.join(outputDir, ".agents/skills");
    fs.mkdirSync(destDir, { recursive: true });
    fs.mkdirSync(agentsDestDir, { recursive: true });

    let copied = 0;
    for (const skill of includes) {
      const corpusSrc = path.join(corpusDir, skill);
      const substrateSrc = path.join(substrateDir, skill);
      let chosenSrc = null;
      if (fs.existsSync(corpusSrc)) {
        chosenSrc = corpusSrc;
        if (fs.existsSync(substrateSrc)) {
          console.log(`    Warning: skill '${skill}' exists in both corpus and substrate; using corpus version`);
        }
      } else if (fs.existsSync(substrateSrc)) {
        chosenSrc = substrateSrc;
      }
      if (chosenSrc) {
        this.copyDirRecursive(chosenSrc, path.join(destDir, skill));
        this.copyDirRecursive(chosenSrc, path.join(agentsDestDir, skill));
        copied++;
      } else {
        console.log(`    Warning: skill '${skill}' not found in corpus or substrate`);
      }
    }

    console.log(`  Skills: ${copied} copied (.claude/skills + .agents/skills)`);
  }

  async buildAgents(profile, outputDir) {
    const agentsConfig = profile.agents || {};
    const includes = agentsConfig.include || [];
    if (includes.length === 0) {
      console.log("  Agents: 0 (none configured)");
      return;
    }

    // Corpus-bound first, substrate root as back-stop. Mirrors the
    // skill resolver: corpus-bound agents live at
    // {source_dir}/.claude/agents/, substrate-shared agents at the repo
    // root .claude/agents/.
    const corpusDir = path.join(this.sourceDir, ".claude/agents");
    const substrateDir = path.join(this.repoRoot, ".claude/agents");
    const destDir = path.join(outputDir, ".claude/agents");
    fs.mkdirSync(destDir, { recursive: true });

    // Dual-runtime: the Codex form of each agent is a .toml at the sibling
    // .codex/agents/ path, resolved corpus-first exactly like the .md form.
    // When present, it ships alongside the Claude .md so a compiled app is
    // usable from either runtime. Agents without a Codex form still ship
    // their Claude .md — the .toml is optional, not required.
    const codexCorpusDir = path.join(this.sourceDir, ".codex/agents");
    const codexSubstrateDir = path.join(this.repoRoot, ".codex/agents");
    const codexDestDir = path.join(outputDir, ".codex/agents");

    let copied = 0;
    let codexCopied = 0;
    for (const agent of includes) {
      const agentFile = agent.endsWith(".md") ? agent : `${agent}.md`;
      const corpusSrc = path.join(corpusDir, agentFile);
      const substrateSrc = path.join(substrateDir, agentFile);
      let chosenSrc = null;
      if (fs.existsSync(corpusSrc)) {
        chosenSrc = corpusSrc;
        if (fs.existsSync(substrateSrc)) {
          console.log(`    Warning: agent '${agentFile}' exists in both corpus and substrate; using corpus version`);
        }
      } else if (fs.existsSync(substrateSrc)) {
        chosenSrc = substrateSrc;
      }
      if (chosenSrc) {
        this.copyFileRewriting(chosenSrc, path.join(destDir, agentFile));
        copied++;
      } else {
        console.log(`    Warning: agent '${agentFile}' not found in corpus or substrate`);
      }

      // Codex .toml twin, resolved corpus-first, substrate back-stop.
      const agentBase = agentFile.replace(/\.md$/, "");
      const codexFile = `${agentBase}.toml`;
      const codexCorpusSrc = path.join(codexCorpusDir, codexFile);
      const codexSubstrateSrc = path.join(codexSubstrateDir, codexFile);
      let codexSrc = null;
      if (fs.existsSync(codexCorpusSrc)) codexSrc = codexCorpusSrc;
      else if (fs.existsSync(codexSubstrateSrc)) codexSrc = codexSubstrateSrc;
      if (codexSrc) {
        fs.mkdirSync(codexDestDir, { recursive: true });
        this.copyFileRewriting(codexSrc, path.join(codexDestDir, codexFile));
        codexCopied++;
      }
    }

    console.log(
      `  Agents: ${copied} copied` +
        (codexCopied > 0 ? ` (+${codexCopied} Codex .toml)` : "")
    );
  }

  async buildClaudeMd(profile, outputDir) {
    const claudeConfig = profile.claude_md || {};
    const templateName = claudeConfig.template;
    if (!templateName) {
      console.log("  CLAUDE.md: skipped (no template configured)");
      return;
    }

    // Corpus-bound resolution, parallel to skills: look first in the
    // profile's source corpus, then fall back to substrate root if a corpus
    // still carries shared templates. The substrate path is kept as a
    // back-stop for older corpora; new corpora should carry their own
    // build-profiles/ directory.
    const corpusTemplatePath = path.join(
      this.sourceDir,
      "build-profiles",
      `${templateName}.md`
    );
    const substrateTemplatePath = path.join(
      this.repoRoot,
      "build-profiles",
      `${templateName}.md`
    );
    let templatePath = null;
    if (fs.existsSync(corpusTemplatePath)) {
      templatePath = corpusTemplatePath;
    } else if (fs.existsSync(substrateTemplatePath)) {
      templatePath = substrateTemplatePath;
    }
    if (!templatePath) {
      console.log(`  CLAUDE.md: template '${templateName}' not found in corpus or substrate`);
      return;
    }

    this.copyFileRewriting(templatePath, path.join(outputDir, "CLAUDE.md"));
    console.log(`  CLAUDE.md: from template '${templateName}'`);
  }

  // Emit an app-scoped AGENTS.md so an AGENTS.md-aware runtime (Codex and
  // others) lands on the same operating contract Claude Code reads from
  // CLAUDE.md. This is the compiled-app parallel to the repo-root AGENTS.md:
  // it points at the app's own CLAUDE.md, names where the skills live in both
  // runtime layouts, and restates the two floors that hold regardless of
  // vendor (source integrity, dist-only tier discipline). It is static across
  // profiles by design — every app carries the same contract; the per-profile
  // substance lives in the profile's CLAUDE.md, which this file points at.
  async buildAgentsMd(profile, outputDir) {
    const content = `# AGENTS.md — grounded-forge application

This is a compiled application: a corpus subset projected onto a task axis.
Claude Code reads \`CLAUDE.md\`; this file points any AGENTS.md-aware runtime
(Codex and others) at the same operating contract.

## Read first

1. **\`CLAUDE.md\`** in this directory — the operating contract for this app:
   what it is, what it ships, and how to retrieve. Read it in full before
   answering from the corpus.
2. **Skills** ship in two parallel layouts holding identical content:
   \`.agents/skills/{skill}/SKILL.md\` and \`.claude/skills/{skill}/SKILL.md\`.
   Invoke a skill natively where your runtime supports it; otherwise read its
   \`SKILL.md\` and follow it as a written procedure. The retrieval procedure is
   \`answer-from-corpus\`.

## Non-negotiable: Source Integrity

Ground every source-grounded claim in a passage carried by a distillation.
Distillations carry paraphrased prose with parenthetical attribution and
verbatim blockquotes with evidence markers (\`[V]\` / \`[AP]\` / \`[AR]\` / \`[AE]\`
/ \`[BT]\`) preserved in-band. If the distillation does not support a claim, say
so — do not supply it from training-data knowledge of the author. Cite the
distillation before stating the claim.

## What this app ships (dist-only)

- \`distillations/{task}/\` — the source-grounded product. Cite from these.
- Runtime JSON indexes at the app root (\`concept-index.json\`,
  \`slug-table.json\`, \`lens-index.json\`) and \`distillations/{task}/task-index.json\`.
  Read the indexes to route; never cite an index entry as if it were primary
  evidence.
- \`lenses/\` — per-distillation modifiers. Apply when a lens materially
  reweights what is salient.

The reference tier (light + deep) does not travel with this app; it lives at
corpus level as the audit-of-record. The verbatim passages and evidence
markers already in the distillations are what Pass D audited against the
source text — they are your citable provenance.
`;
    const agentsMdPath = path.join(outputDir, "AGENTS.md");
    fs.writeFileSync(agentsMdPath, content, "utf-8");
    console.log("  AGENTS.md: emitted (dual-runtime app contract)");
  }

  async buildDocs(profile, outputDir) {
    const docsConfig = profile.docs || {};
    const includes = docsConfig.include || [];
    if (includes.length === 0) {
      console.log("  Docs: 0 entries");
      return;
    }

    let copied = 0;
    for (const docPath of includes) {
      const src = path.join(this.repoRoot, docPath);
      if (!fs.existsSync(src)) continue;
      const dest = path.join(outputDir, docPath);
      if (fs.statSync(src).isDirectory()) {
        this.copyDirRecursive(src, dest);
      } else {
        fs.mkdirSync(path.dirname(dest), { recursive: true });
        this.copyFileRewriting(src, dest);
      }
      copied++;
    }
    console.log(`  Docs: ${copied} entries copied`);
  }

  async copyMisc(profile, outputDir, profileName) {
    // README resolution, parallel to CLAUDE.md template lookup:
    // corpus-bound `{source_dir}/build-profiles/{profile-name}-README.md`
    // first; substrate root README.md as back-stop. Private corpora
    // ship their own corpus-specific READMEs; demo apps fall back to
    // the grounded-forge root README (which is what they
    // are demonstrating).
    const corpusReadme = path.join(
      this.sourceDir,
      "build-profiles",
      `${profileName}-README.md`
    );
    const rootReadme = path.join(this.repoRoot, "README.md");
    let readmeSrc = null;
    let readmeOrigin = null;
    if (fs.existsSync(corpusReadme)) {
      readmeSrc = corpusReadme;
      readmeOrigin = `corpus template '${profileName}-README.md'`;
    } else if (fs.existsSync(rootReadme)) {
      readmeSrc = rootReadme;
      readmeOrigin = "root";
    }
    if (readmeSrc) {
      this.copyFileRewriting(readmeSrc, path.join(outputDir, "README.md"));
      console.log(`  README: copied from ${readmeOrigin}`);
    }
    for (const legalFile of ["LICENSE", "LICENSE-CONTENT", "DISCLAIMER.md"]) {
      const src = path.join(this.repoRoot, legalFile);
      if (fs.existsSync(src)) {
        this.copyFileRewriting(src, path.join(outputDir, legalFile));
        console.log(`  ${legalFile}: copied from root`);
      }
    }
  }

  // Strip deep-ref pointers (section, md_line) from concept-index source
  // entries so the shipped index is dist-only-coherent. The runtime gets
  // {id, context} per source and resolves the concept inside the
  // distillation by full-reading the distillation file.
  stripConceptIndexPointers(index) {
    const out = {
      schema_version: index.schema_version,
      corpus: index.corpus,
      generated_from: `${index.generated_from} (app: pointers stripped)`,
      concepts: {},
    };
    for (const [slug, entry] of Object.entries(index.concepts || {})) {
      out.concepts[slug] = {
        name: entry.name,
        aliases: entry.aliases || [],
        sources: (entry.sources || []).map((s) => {
          const r = { id: s.id };
          if (s.context) r.context = s.context;
          return r;
        }),
      };
    }
    return out;
  }

  /**
   * Strip internal grounding-audit artefacts before shipping.
   * Distillations and references in the source repo can carry
   * "## Verification" sections, "Generated by:" headers, "Verified:"
   * footers, and other HTML-comment audit trails documenting how the
   * file was generated. Useful in the source repo (integrity record),
   * noise in the shipped distro. HTML comments are non-rendering by
   * definition; stripping all of them is safe and forward-compatible.
   */
  stripVerificationArtifacts(content) {
    content = content.replace(/<!--[\s\S]*?-->\n?/g, "");
    const lines = content.split("\n");
    const out = [];
    let skipping = false;
    for (const line of lines) {
      if (/^## (?:Verification|Self-verification)\b/i.test(line)) {
        skipping = true;
        continue;
      }
      if (skipping && /^#{1,2} /.test(line)) {
        skipping = false;
      }
      if (!skipping) out.push(line);
    }
    let result = out.join("\n");
    return result.replace(/\n{3,}/g, "\n\n").replace(/\s+$/, "\n");
  }

  async validate(profile, outputDir, profileName) {
    console.log(`\n  VALIDATION: ${profileName}`);
    console.log(`  ${"-".repeat(40)}`);

    let failCount = 0;
    let warnCount = 0;

    const ignoreDangling = profile.validation?.ignore_dangling || [];
    const ref = this.checkReferentialIntegrity(outputDir, ignoreDangling);
    if (ref.status === "fail") {
      console.log(
        `    Referential integrity .. FAIL (${ref.danglingFail.length} broken)`
      );
      for (const d of ref.danglingFail.slice(0, 10)) {
        console.log(`      ${d.source}:${d.line} -> ${d.target}`);
      }
      if (ref.danglingFail.length > 10) {
        console.log(
          `      ... and ${ref.danglingFail.length - 10} more`
        );
      }
      failCount++;
    } else if (ref.status === "warn") {
      console.log(
        `    Referential integrity .. PASS (${ref.checked} refs, ${ref.danglingWarn.length} ignored)`
      );
    } else {
      console.log(
        `    Referential integrity .. PASS (${ref.checked} refs checked)`
      );
    }

    const struct = this.checkStructure(outputDir);
    if (struct.status === "fail") {
      console.log(`    Structure .............. FAIL`);
      for (const f of struct.fails) console.log(`      ${f}`);
      failCount++;
    } else if (struct.status === "warn") {
      console.log(`    Structure .............. WARN`);
      for (const w of struct.warns) console.log(`      ${w}`);
      warnCount++;
    } else {
      console.log(`    Structure .............. PASS`);
    }

    const sources = this.checkSourcesPairing();
    if (sources.status === "fail") {
      console.log(`    Sources pairing ........ FAIL`);
      for (const f of sources.fails.slice(0, 10)) console.log(`      ${f}`);
      if (sources.fails.length > 10)
        console.log(`      ... and ${sources.fails.length - 10} more`);
      failCount++;
    } else if (sources.status === "warn") {
      console.log(`    Sources pairing ........ WARN`);
      for (const w of sources.warns) console.log(`      ${w}`);
      warnCount++;
    } else {
      console.log(`    Sources pairing ........ PASS (${sources.checked} pairs)`);
    }

    console.log(`  ${"-".repeat(40)}`);
    if (failCount > 0) {
      console.log(
        `  Result: FAILED (${failCount} error(s), ${warnCount} warning(s))\n`
      );
      process.exit(1);
    } else if (warnCount > 0) {
      console.log(`  Result: PASSED (${warnCount} warning(s))`);
    } else {
      console.log(`  Result: PASSED`);
    }
  }

  checkReferentialIntegrity(outputDir, ignoreDangling) {
    const mdFiles = this.collectMdFiles(outputDir);
    const allDangling = [];
    const checked = new Set();

    for (const { fullPath, relPath } of mdFiles) {
      const content = fs.readFileSync(fullPath, "utf8");
      const lines = content.split("\n");
      for (let i = 0; i < lines.length; i++) {
        const refs = this.extractPathRefs(lines[i], relPath);
        for (const ref of refs) {
          const key = `${relPath}:${ref}`;
          if (checked.has(key)) continue;
          checked.add(key);
          const target = path.join(outputDir, ref);
          if (!fs.existsSync(target)) {
            allDangling.push({ source: relPath, line: i + 1, target: ref });
          }
        }
      }
    }

    const danglingFail = [];
    const danglingWarn = [];
    for (const d of allDangling) {
      // Skills are dual-emitted as identical content into .claude/skills and
      // .agents/skills. A skill-internal link (e.g. a runtime-output example
      // path in a SKILL.md) dangles the same way in both layouts. Profiles
      // enumerate the .claude/skills/* ignore globs by hand; normalise the
      // .agents twin back to its .claude path so those same globs cover it,
      // rather than forcing every profile to duplicate its ignore list.
      const normalisedTarget = d.target.replace(
        /^\.agents\/skills\//,
        ".claude/skills/"
      );
      if (
        ignoreDangling.some(
          (p) => this.matchGlob(d.target, p) || this.matchGlob(normalisedTarget, p)
        )
      ) {
        danglingWarn.push(d);
      } else {
        danglingFail.push(d);
      }
    }

    return {
      status:
        danglingFail.length > 0
          ? "fail"
          : danglingWarn.length > 0
          ? "warn"
          : "pass",
      checked: checked.size,
      danglingFail,
      danglingWarn,
    };
  }

  // Pair-check the corpus's source tier: every sources/converted/{slug}.md
  // must have a sources/original/{slug}.source.md sidecar, and vice versa.
  // The sidecar carries title, URL, scope, licence; the converted markdown
  // is what Pass C reads. A converted file without a sidecar means an
  // unaudited input; a sidecar without converted means a half-finished
  // ingest. Both states are caught here at build time.
  checkSourcesPairing() {
    const convertedDir = path.join(this.sourceDir, "sources", "converted");
    const originalDir = path.join(this.sourceDir, "sources", "original");

    if (!fs.existsSync(convertedDir) || !fs.existsSync(originalDir)) {
      return { status: "warn", checked: 0, fails: [], warns: ["sources/ tree incomplete or missing"] };
    }

    // Converted source mds use lowercase {prefix}-{slug}.md naming.
    // Skip dotfiles, META README-style docs (uppercase first letter),
    // and underscore-prefixed staging or audit files.
    const converted = new Set(
      fs.readdirSync(convertedDir)
        .filter(
          (f) =>
            f.endsWith(".md") &&
            !f.startsWith(".") &&
            !f.startsWith("_") &&
            /^[a-z0-9]/.test(f) &&
            // -images-alt files are image-extraction byproducts (an
            // alt-text sidecar of a source's figures), not source texts;
            // they have no independent .source.md and must not be paired.
            !f.endsWith("-images-alt.md")
        )
        .map((f) => f.replace(/\.md$/, ""))
    );
    const sidecars = new Set(
      fs.readdirSync(originalDir)
        .filter((f) => f.endsWith(".source.md") && !f.startsWith("."))
        .map((f) => f.replace(/\.source\.md$/, ""))
    );

    const fails = [];
    for (const slug of converted) {
      if (!sidecars.has(slug)) {
        fails.push(`converted/${slug}.md has no sidecar at original/${slug}.source.md`);
      }
    }
    for (const slug of sidecars) {
      if (!converted.has(slug)) {
        fails.push(`original/${slug}.source.md has no converted markdown at converted/${slug}.md`);
      }
    }

    const checked = converted.size + sidecars.size;
    return {
      status: fails.length > 0 ? "fail" : "pass",
      checked: converted.size,
      fails,
      warns: [],
    };
  }

  checkStructure(outputDir) {
    const fails = [];
    const warns = [];

    const claudePath = path.join(outputDir, "CLAUDE.md");
    if (!fs.existsSync(claudePath)) fails.push("CLAUDE.md missing");
    else if (fs.statSync(claudePath).size === 0)
      fails.push("CLAUDE.md is empty");

    const readmePath = path.join(outputDir, "README.md");
    if (!fs.existsSync(readmePath)) fails.push("README.md missing");
    else if (fs.statSync(readmePath).size === 0)
      fails.push("README.md is empty");

    // Dual-runtime contract: every app carries an AGENTS.md alongside
    // CLAUDE.md so an AGENTS.md-aware runtime lands on the same rules.
    const agentsMdPath = path.join(outputDir, "AGENTS.md");
    if (!fs.existsSync(agentsMdPath)) fails.push("AGENTS.md missing");
    else if (fs.statSync(agentsMdPath).size === 0)
      fails.push("AGENTS.md is empty");

    // Skill-surface parity: skills are dual-emitted into .claude/skills and
    // .agents/skills. If one layout is present, the other must carry the
    // identical skill set — a broken dual-emit must fail the build, not ship.
    const claudeSkillsDir = path.join(outputDir, ".claude/skills");
    const agentsSkillsDir = path.join(outputDir, ".agents/skills");
    const listSkills = (dir) =>
      fs.existsSync(dir)
        ? fs
            .readdirSync(dir, { withFileTypes: true })
            .filter((e) => e.isDirectory())
            .map((e) => e.name)
            .sort()
        : null;
    const claudeSkills = listSkills(claudeSkillsDir);
    const agentsSkills = listSkills(agentsSkillsDir);
    if (claudeSkills !== null || agentsSkills !== null) {
      if (claudeSkills === null) {
        fails.push(".agents/skills present but .claude/skills missing");
      } else if (agentsSkills === null) {
        fails.push(".claude/skills present but .agents/skills missing");
      } else if (
        claudeSkills.join("\n") !== agentsSkills.join("\n")
      ) {
        fails.push(
          `.claude/skills and .agents/skills carry different skill sets ` +
            `(.claude: [${claudeSkills.join(", ")}] vs .agents: [${agentsSkills.join(", ")}])`
        );
      }
    }

    // Apps ship distillations as the source-grounded product; references
    // stay at corpus level as the audit-of-record. distillations/ must
    // exist; references/ must NOT exist.
    if (!fs.existsSync(path.join(outputDir, "distillations"))) {
      fails.push("No distillations/ directory");
    }
    if (fs.existsSync(path.join(outputDir, "references"))) {
      fails.push("references/ present — apps must ship distillations only");
    }

    return {
      status:
        fails.length > 0 ? "fail" : warns.length > 0 ? "warn" : "pass",
      fails,
      warns,
    };
  }

  collectMdFiles(dir, basePath) {
    basePath = basePath || dir;
    const out = [];
    if (!fs.existsSync(dir)) return out;
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.name === ".git") continue;
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        out.push(...this.collectMdFiles(full, basePath));
      } else if (entry.name.endsWith(".md")) {
        out.push({ fullPath: full, relPath: path.relative(basePath, full) });
      }
    }
    return out;
  }

  extractPathRefs(line, sourceRelPath) {
    const paths = [];

    // Repo-rooted paths in inline code or markdown links: `distillations/foo.md`,
    // [text](docs/bar.md). These resolve against the output dir directly.
    // Apps' content roots are distillations/, lenses/, docs/, .claude/, .agents/
    // (the last two are the dual-runtime skill layouts). The references/
    // directory does not ship in apps (per dist-only rule); any references/
    // path appearing in a shipped file is a stale link.
    const rootedPatterns = [
      /`((?:distillations|lenses|docs|\.claude|\.agents)\/[^\s`]+)`/g,
      /\]\(((?:distillations|lenses|docs|\.claude|\.agents)\/[^\s)]+)\)/g,
    ];
    for (const pattern of rootedPatterns) {
      let match;
      while ((match = pattern.exec(line)) !== null) {
        let p = match[1];
        if (p.includes("{") || p.includes("*") || p.includes("[")) continue;
        p = p.replace(/[),;:]+$/, "");
        p = p.replace(/#\S*$/, "");
        paths.push(p);
      }
    }

    // Relative paths in markdown links: [text](../foo.md), [text](bar/baz.md),
    // [text](audit-results/), [text](sibling.md). These resolve against the
    // source file's directory, which the validator passes in. Without this
    // pass, links like docs/architecture/matrix-pattern.md -> ../references/foo
    // are silently skipped — which is exactly how the broken stub-reference
    // links survived through the v0.1.5 ingestion.
    if (sourceRelPath) {
      const sourceDir = path.dirname(sourceRelPath);
      const relPattern = /\]\(([^)\s][^)\s]*)\)/g;
      let match;
      while ((match = relPattern.exec(line)) !== null) {
        let p = match[1];
        // Skip absolute URLs (http, mailto, etc.) and anchor-only links.
        if (/^(?:[a-z][a-z0-9+.-]*:|#|\/)/i.test(p)) continue;
        // Skip repo-rooted paths (already handled above) and references/
        // links: dist-only apps don't ship the reference tier, so a
        // distillation's link back to its corpus-level deep ref (rewritten
        // from corpus.local/{corpus}/references/... to references/...) points
        // at the audit-of-record, not at a shipped file. Flagging it as
        // dangling is a false positive — the same reason the rooted-pattern
        // pass above omits references/.
        if (/^(?:distillations|lenses|docs|references|\.claude|\.agents)\//.test(p)) continue;
        // Skip glob/template patterns.
        if (p.includes("{") || p.includes("*") || p.includes("[")) continue;
        // Strip trailing punctuation and anchor.
        p = p.replace(/[),;:]+$/, "");
        p = p.replace(/#\S*$/, "");
        if (!p) continue;
        // Resolve against the source file's directory; normalise to handle
        // ../ traversal. The result is an output-dir-relative path.
        const resolved = path.normalize(path.join(sourceDir, p));
        // Skip paths that escape the output dir (different bug class).
        if (resolved.startsWith("..")) continue;
        // Skip references/ links: dist-only apps don't ship the reference
        // tier, so a distillation's ../.. link back to its corpus-level deep
        // ref resolves to references/... and is the audit-of-record, not a
        // shipped file. Checked here on the resolved path because the raw
        // link is still in ../../references/ form at the pre-normalise skip.
        if (/^references[/\\]/.test(resolved)) continue;
        paths.push(resolved);
      }
    }

    return [...new Set(paths)];
  }

  matchGlob(filename, pattern) {
    const regex = pattern.replace(/\./g, "\\.").replace(/\*/g, ".*");
    return new RegExp(`^${regex}$`).test(filename);
  }

  copyDirRecursive(src, dest) {
    fs.mkdirSync(dest, { recursive: true });
    const entries = fs.readdirSync(src, { withFileTypes: true });
    for (const entry of entries) {
      const s = path.join(src, entry.name);
      const d = path.join(dest, entry.name);
      if (entry.isDirectory()) this.copyDirRecursive(s, d);
      else this.copyFileRewriting(s, d);
    }
  }

  // Rewrite corpus-source paths to flat app paths. Each app's content
  // roots are flat — distillations/, lenses/ — because each app ships one
  // corpus. Source-repo docs and skills that name the corpus by its full
  // source path would dangle inside the app; this rewrite fixes them at
  // copy time. Matches both tiers (commons + local) so substrate skills
  // referencing either tier are handled uniformly.
  //
  // The reference tier (references/, reference-index.json) does not ship
  // in apps, but the architecture docs that ship with apps still describe
  // it: rewriting the path keeps the prose locally-coherent (it reads as
  // "references/" relative to the app root), and the validator's
  // per-profile ignore_dangling pattern accepts that those paths refer to
  // the corpus-level tier and dangle in apps by design.
  rewriteCorpusPaths(content) {
    let rewritten = content.replace(
      /corpus\.(?:commons|local)\/[a-zA-Z0-9_-]+\/(distillations|lenses|references)\//g,
      "$1/"
    );
    // Top-level corpus JSON indexes. concept-index, lens-index, slug-table
    // still ship in apps. reference-index does not, but the path is
    // rewritten to keep the prose locally-coherent; the validator's
    // ignore_dangling pattern catches it.
    rewritten = rewritten.replace(
      /corpus\.(?:commons|local)\/[a-zA-Z0-9_-]+\/(concept-index|lens-index|slug-table|reference-index)\.json/g,
      "$1.json"
    );
    return rewritten;
  }

  // Copy a file from source to dest. For markdown files, apply the
  // corpus-path rewrite via rewriteCorpusPaths.
  copyFileRewriting(srcPath, destPath) {
    if (!srcPath.endsWith(".md")) {
      fs.copyFileSync(srcPath, destPath);
      return;
    }
    const original = fs.readFileSync(srcPath, "utf8");
    fs.writeFileSync(destPath, this.rewriteCorpusPaths(original));
  }

  listProfiles() {
    console.log("\nAvailable build profiles:\n");
    for (const [name, profile] of Object.entries(this.config.builds)) {
      console.log(`  ${name}`);
      console.log(`    ${profile.description}`);
      console.log(`    Output: ${profile.output_dir}`);
      console.log("");
    }
  }

  async buildAll() {
    const profiles = Object.keys(this.config.builds);
    console.log(`\nBuilding ${profiles.length} profiles...`);
    for (const p of profiles) {
      await this.buildProfile(p);
    }
    console.log("\n" + "=".repeat(60));
    console.log("All builds complete.");
    console.log("=".repeat(60));
  }

  clean() {
    const appsBase = path.resolve(
      this.repoRoot,
      this.config.defaults?.output_base || "./apps"
    );
    if (fs.existsSync(appsBase)) {
      fs.rmSync(appsBase, { recursive: true });
      console.log(`Cleaned: ${appsBase}`);
    } else {
      console.log("Nothing to clean.");
    }
  }
}

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || args.includes("--help") || args.includes("-h")) {
    console.log(`
grounded-forge build system

Usage:
  node build.js [profile]    Build one profile
  node build.js --all        Build all profiles
  node build.js --list       List profiles
  node build.js --clean      Remove apps/

Examples:
  node build.js decision
  node build.js stakeholder
  node build.js --all
`);
    return;
  }

  if (!fs.existsSync(CONFIG_FILE)) {
    console.error(`Error: ${CONFIG_FILE} not found`);
    process.exit(1);
  }

  const builder = new MatrixBuilder(CONFIG_FILE);

  if (args.includes("--list")) return builder.listProfiles();
  if (args.includes("--clean")) return builder.clean();

  // Lens spec-location gate. Runs before any profile work so the build
  // fails fast when corpus.commons/ harbours a lens above 'open-nc'.
  try {
    builder.enforceCommonsVisibilityGate();
  } catch (e) {
    console.error(`Error: ${e.message}`);
    process.exit(1);
  }

  if (args.includes("--all")) return await builder.buildAll();

  try {
    await builder.buildProfile(args[0]);
  } catch (e) {
    console.error(`Error: ${e.message}`);
    process.exit(1);
  }
}

main().catch((e) => {
  console.error("Fatal error:", e);
  process.exit(1);
});
