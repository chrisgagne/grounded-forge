const v = process.argv[2];
const { applyPatch } = await import(`./${v}/src/patch/apply.js`);
const { structuredPatch } = await import(`./${v}/src/patch/create.js`);
const r = (x) => JSON.stringify(x);
// 1. A parsed new-file patch, text form
const p1 = "--- /dev/null\n+++ b\n@@ -0,0 +1,2 @@\n+a\n+b\n";
console.log(v, "parsed new file:", r(applyPatch("", p1)));
// 2. Insert at the top of a non-empty file, text form
const p2 = "--- a\n+++ b\n@@ -0,0 +1,1 @@\n+top\n";
console.log(v, "parsed insert at top:", r(applyPatch("x\ny\n", p2)));
// 3. Structured patch built in memory with oldStart 0
const sp = { hunks: [{ oldStart: 0, oldLines: 0, newStart: 1, newLines: 1, lines: ["+top"], linedelimiters: ["\n"] }] };
console.log(v, "object oldStart 0 on x,y:", r(applyPatch("x\ny\n", sp)));
// 4. structuredPatch's own hunk for a new file (it starts at line 1, so the deleted guard can't fire)
console.log(v, "structuredPatch hunk:", r(structuredPatch("a", "b", "", "a\nb\n").hunks.map(h => [h.oldStart, h.oldLines])));
