#!/usr/bin/env node
/**
 * Helpers: code an app ships beside its skills and agents. A corpus keeps it at
 * helpers/{profile}/; the build copies it into the app, leaving local
 * environments and caches behind, and the link check doesn't read its docs.
 *
 * Usage: node tests/helpers.test.js (from the repo root)
 */
const fs = require("fs");
const os = require("os");
const path = require("path");
const { MatrixBuilder } = require("../build.js");

function assert(cond, msg) {
  if (!cond) throw new Error(`assertion failed: ${msg}`);
}

async function main() {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "gf-helpers-"));
  try {
    const corpus = path.join(tmp, "corpus");
    const helper = path.join(corpus, "helpers", "demo-app");
    for (const [rel, body] of Object.entries({
      "README.md": "See [the design](DESIGN.md).\n",
      "DESIGN.md": "# Design\n",
      "pkg/__init__.py": "",
      "pkg/__pycache__/x.cpython-312.pyc": "",
      ".venv/bin/python": "",
      "tests/test_x.py": "def test_x(): pass\n",
    })) {
      fs.mkdirSync(path.dirname(path.join(helper, rel)), { recursive: true });
      fs.writeFileSync(path.join(helper, rel), body);
    }
    const out = path.join(tmp, "app");
    fs.mkdirSync(out);
    const builder = Object.create(MatrixBuilder.prototype);
    builder.sourceDir = corpus;
    await builder.buildHelpers({ helpers_dir: "factory" }, "demo-app", out);

    const shipped = path.join(out, "factory");
    assert(fs.existsSync(path.join(shipped, "pkg", "__init__.py")), "the package is copied");
    assert(fs.existsSync(path.join(shipped, "tests", "test_x.py")), "its tests are copied");
    assert(!fs.existsSync(path.join(shipped, ".venv")), "a local venv stays behind");
    assert(!fs.existsSync(path.join(shipped, "pkg", "__pycache__")), "caches stay behind");
    const md = builder.collectMdFiles(out).map((f) => f.relPath);
    assert(md.length === 0, `the link check skips the helper's docs (saw ${md.join(", ")})`);

    const none = path.join(tmp, "app2");
    fs.mkdirSync(none);
    await builder.buildHelpers({}, "no-such-profile", none);
    assert(fs.readdirSync(none).length === 0, "a profile without helpers gets nothing");
    console.log("ok: helpers");
  } finally {
    fs.rmSync(tmp, { recursive: true, force: true });
  }
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
