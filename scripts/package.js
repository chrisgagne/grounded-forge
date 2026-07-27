#!/usr/bin/env node

/**
 * Package a compiled app — or an emitted OKF bundle — as a versioned,
 * scope-labelled tarball.
 *
 * Usage:
 *   node scripts/package.js <app-name>
 *   node scripts/package.js decision
 *   node scripts/package.js decision --okf     Package the app's OKF bundle
 *   node scripts/package.js matrix             okf: only profiles package
 *                                              their bundle automatically
 *   node scripts/package.js --all
 *
 * App mode reads the app at corpus.commons/{corpus}/apps/{app-name}/,
 * computes the most-restrictive scope across its references, writes a
 * manifest of every reference's licence + scope into the bundle, and
 * produces corpus.commons/{corpus}/distros/{app-name}-v{version}-{scope}.tar.gz
 *
 * OKF mode tars the emitted bundle at corpus.commons/{corpus}/okf/{app-name}/
 * (which already carries its LICENCE-MANIFEST.md; the scope label is read
 * from it) into {app-name}-okf-v{version}-{scope}.tar.gz.
 *
 * Hard refusals (build/operator bug, never an intentional ship):
 *   - secrets present (.env, credentials.json, *.pem)
 *   - operator-only artefacts present (_audit/, _planning/, _ingest_*)
 *   - reference with no parseable Scope: line / bundle with no manifest
 *
 * Labels (constraint travels with artefact, recipient sees in filename):
 *   - bundle's most-restrictive scope → filename suffix
 *   - per-reference licence + scope → LICENCE-MANIFEST.md in tarball root
 */

const fs = require("fs");
const os = require("os");
const path = require("path");
const tar = require("tar");
const yaml = require("js-yaml");

const REPO_ROOT = path.resolve(__dirname, "..");
const CONFIG_FILE = "builds.yaml";

const SCOPE_RANK = {
  open: 0,
  "open-nc": 1,
  copyrighted: 2,
  confidential: 3,
  personal: 4,
};

const SECRET_PATTERNS = [/^\.env/, /credentials\.json$/, /\.pem$/, /\.key$/];
const OPERATOR_ARTEFACTS = [/^_audit\//, /^_planning\//, /\/_audit\//, /\/_planning\//, /_ingest_/];

function readVersion() {
  const pkg = JSON.parse(
    fs.readFileSync(path.join(REPO_ROOT, "package.json"), "utf8")
  );
  return pkg.version;
}

function loadBuildsConfig() {
  const text = fs.readFileSync(path.join(REPO_ROOT, CONFIG_FILE), "utf8");
  const config = yaml.load(text) || {};
  if (!config.builds) config.builds = {};
  // Merge per-corpus builds.yaml (mirrors build.js's discovery) so packaging
  // works for corpus.commons / corpus.local profiles, not only substrate ones.
  // Collision policy: keep the substrate profile, skip the corpus version.
  for (const tier of ["corpus.commons", "corpus.local"]) {
    const tierDir = path.join(REPO_ROOT, tier);
    if (!fs.existsSync(tierDir)) continue;
    for (const entry of fs.readdirSync(tierDir, { withFileTypes: true })) {
      if (!entry.isDirectory()) continue;
      const corpusConfig = path.join(tierDir, entry.name, "builds.yaml");
      if (!fs.existsSync(corpusConfig)) continue;
      const loaded = yaml.load(fs.readFileSync(corpusConfig, "utf8"));
      if (!loaded || !loaded.builds) continue;
      for (const [name, profile] of Object.entries(loaded.builds)) {
        if (!config.builds[name]) config.builds[name] = profile;
      }
    }
  }
  return config;
}

function resolveAppDir(appName, config) {
  const profile = config.builds?.[appName];
  if (!profile) {
    throw new Error(
      `Unknown app: '${appName}'. Run 'npm run list' to see available profiles.`
    );
  }
  const appDir = path.resolve(REPO_ROOT, profile.output_dir);
  if (!fs.existsSync(appDir)) {
    throw new Error(
      `App not built: ${appDir}\nRun 'npm run build:${appName}' first.`
    );
  }
  return { appDir, profile };
}

function walk(dir, base = dir) {
  const out = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    const rel = path.relative(base, full);
    if (entry.isDirectory()) {
      out.push(...walk(full, base));
    } else {
      out.push(rel);
    }
  }
  return out;
}

function refuseOnSecrets(files) {
  const hits = files.filter((f) =>
    SECRET_PATTERNS.some((p) => p.test(path.basename(f)))
  );
  if (hits.length) {
    throw new Error(
      `Refusing to package: secrets detected in app bundle.\n  ${hits.join("\n  ")}`
    );
  }
}

function refuseOnOperatorArtefacts(files) {
  const hits = files.filter((f) => OPERATOR_ARTEFACTS.some((p) => p.test(f)));
  if (hits.length) {
    throw new Error(
      `Refusing to package: operator-only artefacts in app bundle.\n  ${hits.join("\n  ")}`
    );
  }
}

function parseScope(filePath) {
  const text = fs.readFileSync(filePath, "utf8");
  const m = text.match(/^\*\*Scope:\*\*\s*(\S+)/m);
  return m ? m[1] : null;
}

function parseLicence(filePath) {
  const text = fs.readFileSync(filePath, "utf8");
  // Accept "Licence:", "License:", or "licensed:" (case-insensitive). The
  // licence string is usually wrapped in bold immediately after; fall back
  // to plain inline if no bold form is present.
  const bold = text.match(/licen[cs]e[d]?:\s*\*\*([^*]+)\*\*/i);
  if (bold) return bold[1].trim();
  const inline = text.match(/licen[cs]e[d]?:\s*([^.\n]+)/i);
  return inline ? inline[1].trim() : "unknown";
}

function inspectReferences(appDir) {
  const refsDir = path.join(appDir, "references");
  if (!fs.existsSync(refsDir)) {
    return { scopes: [], rows: [] };
  }
  const deepRefs = fs
    .readdirSync(refsDir)
    .filter((f) => f.endsWith("-deep.md"))
    .map((f) => path.join(refsDir, f));

  const rows = [];
  const missing = [];
  for (const ref of deepRefs) {
    const slug = path.basename(ref, ".md");
    const scope = parseScope(ref);
    const licence = parseLicence(ref);
    if (!scope) {
      missing.push(slug);
      continue;
    }
    rows.push({ slug, scope, licence });
  }

  if (missing.length) {
    throw new Error(
      `Refusing to package: ${missing.length} reference(s) missing **Scope:** line.\n  ${missing.join("\n  ")}`
    );
  }
  return { rows };
}

function readDistillationSources(appDir) {
  // Dist-only apps ship no references/. build.js records each shipped
  // distillation's source scope + licence in distillation-sources.json;
  // that is the authority for the bundle's distribution scope. Prefer it;
  // fall back to a legacy references/ walk; never silently default to open.
  const manifestPath = path.join(appDir, "distillation-sources.json");
  if (fs.existsSync(manifestPath)) {
    const data = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
    const rows = (data.sources || []).map((s) => ({
      slug: s.slug,
      scope: s.scope,
      licence: s.licence || "unknown",
    }));
    return { rows, scope: mostRestrictiveScope(rows) };
  }
  const refsDir = path.join(appDir, "references");
  if (fs.existsSync(refsDir)) {
    const { rows } = inspectReferences(appDir);
    return { rows, scope: mostRestrictiveScope(rows) };
  }
  throw new Error(
    `Refusing to package: no distillation-sources.json manifest and no references/ in\n  ${appDir}\n` +
      `Rebuild the app (npm run build) so build.js emits the scope manifest. ` +
      `Packaging without it would mislabel the bundle's distribution scope as 'open'.`
  );
}

function mostRestrictiveScope(rows) {
  if (rows.length === 0) return "open";
  let maxScope = "open";
  let maxRank = -1;
  for (const r of rows) {
    const rank = SCOPE_RANK[r.scope];
    if (rank === undefined) {
      throw new Error(
        `Refusing to package: reference '${r.slug}' has unknown scope '${r.scope}'. Valid: ${Object.keys(SCOPE_RANK).join(", ")}`
      );
    }
    if (rank > maxRank) {
      maxRank = rank;
      maxScope = r.scope;
    }
  }
  return maxScope;
}

function writeManifest(appDir, appName, version, scope, rows) {
  const manifestPath = path.join(appDir, "LICENCE-MANIFEST.md");
  const lines = [
    `# Licence manifest`,
    ``,
    `**App:** ${appName}`,
    `**Version:** ${version}`,
    `**Most-restrictive scope:** ${scope}`,
    `**References:** ${rows.length}`,
    ``,
    `## Scope levels`,
    ``,
    `| Scope | Meaning |`,
    `|---|---|`,
    `| open | Public, redistributable, no commercial restriction. |`,
    `| open-nc | Public, redistributable, non-commercial use only. |`,
    `| copyrighted | Single-organisation redistribution; further redistribution requires the right-holder's permission. |`,
    `| confidential | Single-organisation use; not for redistribution. |`,
    `| personal | Single-recipient use; not for sharing. |`,
    ``,
    `The tarball's filename carries the most-restrictive scope across all bundled references. The recipient inherits that constraint.`,
    ``,
    `## References`,
    ``,
    `| Slug | Scope | Licence |`,
    `|---|---|---|`,
    ...rows
      .sort((a, b) => a.slug.localeCompare(b.slug))
      .map((r) => `| ${r.slug} | ${r.scope} | ${r.licence} |`),
    ``,
  ];
  fs.writeFileSync(manifestPath, lines.join("\n"));
  return manifestPath;
}

// Package an emitted OKF bundle. The bundle already carries its
// LICENCE-MANIFEST.md (written by the emitter at build time); the scope
// label is read from it rather than recomputed — refusing to package a
// bundle without one keeps a stale or hand-made tree from shipping
// unlabelled. The tarball's top-level directory is {name}-okf/ so an
// extracted bundle never collides with the same profile's extracted app.
async function packageOkfBundle(appName, profile) {
  const version = readVersion();
  const bundleDir =
    profile.okf === "only"
      ? path.resolve(REPO_ROOT, profile.output_dir)
      : path.resolve(REPO_ROOT, profile.output_dir, "..", "..", "okf", appName);
  if (!fs.existsSync(bundleDir)) {
    throw new Error(
      `OKF bundle not built: ${bundleDir}\nRun 'npm run build:${appName}' first.`
    );
  }

  console.log(`\nPackaging OKF bundle: ${appName}`);
  console.log(`  Bundle dir: ${path.relative(REPO_ROOT, bundleDir)}`);
  console.log(`  Version: ${version}`);

  const distrosDir = path.resolve(bundleDir, "..", "..", "distros");
  fs.mkdirSync(distrosDir, { recursive: true });

  const files = walk(bundleDir);
  refuseOnSecrets(files);
  refuseOnOperatorArtefacts(files);

  const manifestPath = path.join(bundleDir, "LICENCE-MANIFEST.md");
  if (!fs.existsSync(manifestPath)) {
    throw new Error(
      `Refusing to package: no LICENCE-MANIFEST.md in\n  ${bundleDir}\n` +
        `Rebuild the bundle (npm run build:${appName}) so the emitter writes the manifest. ` +
        `Packaging without it would ship the bundle unlabelled.`
    );
  }
  const manifest = fs.readFileSync(manifestPath, "utf8");
  const scopeMatch = manifest.match(/^\*\*Most-restrictive scope:\*\*\s*(\S+)/m);
  if (!scopeMatch || !(scopeMatch[1] in SCOPE_RANK)) {
    throw new Error(
      `Refusing to package: LICENCE-MANIFEST.md in ${bundleDir} has no parseable most-restrictive scope.`
    );
  }
  const scope = scopeMatch[1];
  console.log(`  Most-restrictive scope: ${scope}`);

  // Stage under the collision-safe top-level name, tar, clean up.
  const stagingRoot = fs.mkdtempSync(path.join(os.tmpdir(), "gf-pkg-okf-"));
  const topLevel = `${appName}-okf`;
  fs.cpSync(bundleDir, path.join(stagingRoot, topLevel), { recursive: true });

  const tarballName = `${topLevel}-v${version}-${scope}.tar.gz`;
  const tarballPath = path.join(distrosDir, tarballName);
  try {
    await tar.create(
      { file: tarballPath, gzip: true, cwd: stagingRoot },
      [topLevel]
    );
  } finally {
    fs.rmSync(stagingRoot, { recursive: true, force: true });
  }

  const sizeKb = Math.round(fs.statSync(tarballPath).size / 1024);
  console.log(`\n  Wrote: ${path.relative(REPO_ROOT, tarballPath)} (${sizeKb} KB)`);
  console.log(`\n  Recipient install:`);
  console.log(`    tar -xzf ${tarballName}`);
  console.log(`    okf validate ${topLevel}    # any OKF v0.2 consumer can read it`);

  if (scope !== "open") {
    console.log(`\n  ⚠  Scope is '${scope}'. Distribute only to recipients authorised at this level.`);
  }
}

async function packageApp(appName, opts = {}) {
  const version = readVersion();
  const config = loadBuildsConfig();
  const profile = config.builds?.[appName];
  if (!profile) {
    throw new Error(
      `Unknown app: '${appName}'. Run 'npm run list' to see available profiles.`
    );
  }
  // okf: only profiles have no app to package; --okf targets a profile's
  // emitted bundle instead of its app.
  if (opts.okf || profile.okf === "only") {
    return packageOkfBundle(appName, profile);
  }
  const { appDir } = resolveAppDir(appName, config);

  console.log(`\nPackaging: ${appName}`);
  console.log(`  App dir: ${path.relative(REPO_ROOT, appDir)}`);
  console.log(`  Version: ${version}`);

  // Distros dir is a sibling of apps/
  const distrosDir = path.resolve(appDir, "..", "..", "distros");
  fs.mkdirSync(distrosDir, { recursive: true });

  // Walk the app, run hard-fail gates.
  const files = walk(appDir);
  refuseOnSecrets(files);
  refuseOnOperatorArtefacts(files);

  // Determine the bundle's most-restrictive scope from the shipped
  // distillations' source provenance (dist-only apps carry no references/).
  const { rows, scope } = readDistillationSources(appDir);
  console.log(`  References: ${rows.length}`);
  console.log(`  Most-restrictive scope: ${scope}`);

  // Write the manifest into the app dir so it lands inside the tarball.
  const manifestPath = writeManifest(appDir, appName, version, scope, rows);
  console.log(`  Manifest: ${path.relative(REPO_ROOT, manifestPath)}`);

  // Tar it. cwd is the apps/ dir; the only entry is the app's folder name,
  // which becomes the top-level directory inside the tarball.
  const tarballName = `${appName}-v${version}-${scope}.tar.gz`;
  const tarballPath = path.join(distrosDir, tarballName);
  await tar.create(
    {
      file: tarballPath,
      gzip: true,
      cwd: path.dirname(appDir),
    },
    [path.basename(appDir)]
  );

  // Remove the manifest from the source tree (it lives inside the tarball only).
  fs.unlinkSync(manifestPath);

  const sizeKb = Math.round(fs.statSync(tarballPath).size / 1024);
  console.log(`\n  Wrote: ${path.relative(REPO_ROOT, tarballPath)} (${sizeKb} KB)`);
  console.log(`\n  Recipient install:`);
  console.log(`    tar -xzf ${tarballName}`);
  console.log(`    cd ${appName}`);
  console.log(`    claude .`);

  if (scope !== "open") {
    console.log(`\n  ⚠  Scope is '${scope}'. Distribute only to recipients authorised at this level.`);
  }
}

async function main() {
  const args = process.argv.slice(2);
  if (args.length === 0 || args.includes("--help") || args.includes("-h")) {
    console.log(`
Usage:
  node scripts/package.js <app-name>          Package one app
  node scripts/package.js <app-name> --okf    Package the app's OKF bundle
  node scripts/package.js --all               Package every built app

Produces corpus.commons/{corpus}/distros/{app}-v{version}-{scope}.tar.gz
(or {app}-okf-v{version}-{scope}.tar.gz in OKF mode). Profiles declared
okf: only always package their bundle.
`);
    return;
  }
  const flags = new Set(args.filter((a) => a.startsWith("--")));
  const names = args.filter((a) => !a.startsWith("--"));
  const config = loadBuildsConfig();
  const targets = flags.has("--all") ? Object.keys(config.builds || {}) : names;

  console.log(`Packaging ${targets.length} target(s)...`);
  for (const t of targets) {
    try {
      await packageApp(t, { okf: flags.has("--okf") });
    } catch (e) {
      console.error(`\nFAILED: ${t}\n  ${e.message}`);
      process.exitCode = 1;
    }
  }
}

main();
