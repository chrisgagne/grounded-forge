#!/usr/bin/env node

/**
 * grounded-forge build system
 *
 * Compiles each profile in builds.yaml into apps/{profile-name}/.
 * Each profile is a slice of the matrix: all references plus ONE
 * task-domain's distillation directory (which includes the per-task
 * distillation index). Same sources, different projections, the
 * matrix architecture made visible.
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
// A profile's max_scope sets the ceiling; references whose Scope: rank
// exceeds the ceiling are excluded from that profile's app/. `personal`
// has rank 4 and no max_scope value admits it: personal material is
// mechanically unshippable. Light references inherit their paired deep
// reference's scope (if a deep is excluded, the light is excluded too).
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

    await this.buildReferences(profile, outputDir);
    await this.buildDistillations(profile, outputDir);
    await this.buildLenses(profile, outputDir);
    await this.buildSkills(profile, outputDir);
    await this.buildAgents(profile, outputDir);
    await this.buildClaudeMd(profile, outputDir);
    await this.buildDocs(profile, outputDir);
    await this.copyMisc(profile, outputDir, profileName);

    await this.validate(profile, outputDir, profileName);

    console.log(`\nComplete: ${outputDir}`);
    return outputDir;
  }

  async buildReferences(profile, outputDir) {
    const refConfig = profile.references || {};
    const srcDir = path.join(this.sourceDir, "references");
    const destDir = path.join(outputDir, "references");

    if (!fs.existsSync(srcDir)) {
      console.log("  References: source dir missing");
      return;
    }

    const includes = refConfig.include_patterns || ["*.md"];
    const excludes = refConfig.exclude_patterns || [];

    const maxScope = profile.max_scope ?? DEFAULT_MAX_SCOPE;
    if (!ADMITTABLE_SCOPES.includes(maxScope)) {
      throw new Error(
        `Invalid max_scope '${maxScope}' in profile. Must be one of: ${ADMITTABLE_SCOPES.join(", ")}`
      );
    }
    const maxRank = SCOPE_RANK[maxScope];

    const allFiles = fs
      .readdirSync(srcDir)
      .filter(
        (f) =>
          f.endsWith(".md") && fs.statSync(path.join(srcDir, f)).isFile()
      );

    const patternFiltered = allFiles
      .filter((f) => includes.some((p) => this.matchGlob(f, p)))
      .filter((f) => !excludes.some((p) => this.matchGlob(f, p)));

    // Build set of excluded slugs from deep refs whose Scope: exceeds
    // max_scope (or is missing/unknown). A slug = filename minus the
    // -deep.md suffix, e.g. "openstax-business-law". The paired light
    // reference (slug + .md) inherits exclusion: shipping a light without
    // its deep would break the citation chain.
    const excludedSlugs = new Set();
    const skippedReasons = [];
    for (const f of patternFiltered) {
      if (!f.endsWith("-deep.md")) continue;
      const slug = f.replace(/-deep\.md$/, "");
      const body = fs.readFileSync(path.join(srcDir, f), "utf8");
      const m = body.match(/^\*\*Scope:\*\*\s*(\S+)/m);
      const scope = m ? m[1] : null;
      if (scope === null) {
        excludedSlugs.add(slug);
        skippedReasons.push(`scope missing: ${f}`);
        continue;
      }
      if (!(scope in SCOPE_RANK)) {
        excludedSlugs.add(slug);
        skippedReasons.push(`scope unknown '${scope}': ${f}`);
        continue;
      }
      if (scope === "personal" || SCOPE_RANK[scope] > maxRank) {
        excludedSlugs.add(slug);
        skippedReasons.push(`scope ${scope} > ${maxScope}: ${f}`);
      }
    }

    const final = patternFiltered.filter((f) => {
      const slug = f.endsWith("-deep.md")
        ? f.replace(/-deep\.md$/, "")
        : f.replace(/\.md$/, "");
      return !excludedSlugs.has(slug);
    });

    if (final.length > 0) {
      fs.mkdirSync(destDir, { recursive: true });
      for (const file of final) {
        const srcPath = path.join(srcDir, file);
        const destPath = path.join(destDir, file);
        if (srcPath.endsWith(".md")) {
          const raw = fs.readFileSync(srcPath, "utf8");
          const stripped = this.stripVerificationArtifacts(raw);
          const rewritten = this.rewriteCorpusPaths(stripped);
          fs.writeFileSync(destPath, rewritten);
        } else {
          fs.copyFileSync(srcPath, destPath);
        }
      }
    }

    // Ship runtime JSON indexes alongside the .md references.
    // slug-table.json lives in references/; reference-index.json and
    // concept-index.json live one directory up at the corpus root.
    fs.mkdirSync(destDir, { recursive: true });
    const slugTableSrc = path.join(srcDir, "slug-table.json");
    if (fs.existsSync(slugTableSrc)) {
      fs.copyFileSync(slugTableSrc, path.join(destDir, "slug-table.json"));
    }
    for (const jsonFile of ["reference-index.json", "concept-index.json"]) {
      const src = path.join(this.sourceDir, jsonFile);
      if (fs.existsSync(src)) {
        fs.copyFileSync(src, path.join(outputDir, jsonFile));
      }
    }

    const skippedCount = patternFiltered.length - final.length;
    if (skippedCount > 0) {
      console.log(
        `  References: ${final.length} files copied (${skippedCount} skipped by scope ceiling: ${maxScope})`
      );
      for (const r of skippedReasons) console.log(`    ${r}`);
    } else {
      console.log(`  References: ${final.length} files copied (max_scope: ${maxScope})`);
    }
  }

  async buildDistillations(profile, outputDir) {
    const distConfig = profile.distillations;
    if (!distConfig || !distConfig.include?.length) {
      console.log("  Distillations: 0 (none configured)");
      return;
    }

    let total = 0;
    for (const taskDir of distConfig.include) {
      const srcDir = path.join(
        this.sourceDir,
        "distillations",
        taskDir
      );
      const destDir = path.join(outputDir, "distillations", taskDir);

      if (!fs.existsSync(srcDir)) {
        console.log(`    Warning: distillation dir '${taskDir}' not found`);
        continue;
      }

      fs.mkdirSync(destDir, { recursive: true });

      const excludes = distConfig.exclude || [];
      const files = fs
        .readdirSync(srcDir)
        .filter(
          (f) =>
            f.endsWith(".md") &&
            fs.statSync(path.join(srcDir, f)).isFile()
        )
        .filter((f) => !excludes.includes(f));

      for (const file of files) {
        const raw = fs.readFileSync(path.join(srcDir, file), "utf8");
        const stripped = this.stripVerificationArtifacts(raw);
        const rewritten = this.rewriteCorpusPaths(stripped);
        fs.writeFileSync(path.join(destDir, file), rewritten);
      }
      total += files.length;

      // Ship the per-axis runtime task-index alongside the .md distillations.
      const taskIndexSrc = path.join(srcDir, "task-index.json");
      if (fs.existsSync(taskIndexSrc)) {
        fs.copyFileSync(taskIndexSrc, path.join(destDir, "task-index.json"));
      }
    }

    console.log(`  Distillations: ${total} files copied`);
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
    fs.mkdirSync(destDir, { recursive: true });

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
        copied++;
      } else {
        console.log(`    Warning: skill '${skill}' not found in corpus or substrate`);
      }
    }

    console.log(`  Skills: ${copied} copied`);
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

    let copied = 0;
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
    }

    console.log(`  Agents: ${copied} copied`);
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
      if (ignoreDangling.some((p) => this.matchGlob(d.target, p))) {
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
            /^[a-z0-9]/.test(f)
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

    const contentDirs = [
      "references",
      "distillations",
    ];
    const present = contentDirs.filter((d) =>
      fs.existsSync(path.join(outputDir, d))
    );
    if (present.length === 0)
      fails.push("No content directories (references / distillations)");

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

    // Repo-rooted paths in inline code or markdown links: `references/foo.md`,
    // [text](docs/bar.md). These resolve against the output dir directly.
    // The dist's content roots are references/, distillations/, lenses/, plus
    // docs/ and .claude/.
    const rootedPatterns = [
      /`((?:references|distillations|lenses|docs|\.claude)\/[^\s`]+)`/g,
      /\]\(((?:references|distillations|lenses|docs|\.claude)\/[^\s)]+)\)/g,
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
        // Skip repo-rooted paths (already handled above).
        if (/^(?:references|distillations|lenses|docs|\.claude)\//.test(p)) continue;
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
  // roots are flat — references/, distillations/, lenses/ — because each
  // app ships one corpus. Source-repo docs and skills that name the
  // corpus by its full source path would dangle inside the app; this
  // rewrite fixes them at copy time. Matches both tiers (commons + local)
  // so substrate skills referencing either tier are handled uniformly.
  rewriteCorpusPaths(content) {
    let rewritten = content.replace(
      /corpus\.(?:commons|local)\/[a-zA-Z0-9_-]+\/(references|distillations|lenses)\//g,
      "$1/"
    );
    // Top-level corpus JSON indexes live at the corpus root and ship
    // unchanged to the app root.
    rewritten = rewritten.replace(
      /corpus\.(?:commons|local)\/[a-zA-Z0-9_-]+\/(reference-index|concept-index|lens-index)\.json/g,
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
