"""scripts/ci-verbatim.py: the baseline ratchet blocks new verbatim findings and only those."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("civ", Path(__file__).resolve().parent.parent / "scripts" / "ci-verbatim.py")
civ = importlib.util.module_from_spec(spec)
spec.loader.exec_module(civ)


def f(kind, quote, file="corpus.commons/demo/apps/x/distillations/t/a-t.md", line=3):
    return {"file": file, "line": line, "kind": kind, "quote": quote}


old = f("near", "an old   mismatch")
baseline = {civ.key(old)}

# A baselined finding that moved lines and changed whitespace is still the same finding.
new, gone, _ = civ.judge([f("near", "an old mismatch", line=40)], [], baseline)
assert new == [] and gone == [], (new, gone)

# A new failing finding blocks; a non-failing kind doesn't.
new, _, _ = civ.judge([old, f("missing", "invented words"), f("apostrophe", "it's")], [], baseline)
assert [x["kind"] for x in new] == ["missing"], new

# The same quote with a different failing kind is new.
new, _, _ = civ.judge([f("page", "an old mismatch")], [], baseline)
assert len(new) == 1

# A repaired finding is reported as resolved.
_, gone, _ = civ.judge([], [], baseline)
assert gone == sorted(baseline)

# Shipped files: app distillations only, without indexes, READMEs or underscore files.
files = civ.shipped()
assert files and all("/apps/" in p and "/distillations/" in p for p in files)
assert not any(Path(p).name in ("README.md",) or Path(p).name.startswith("_") or "INDEX" in Path(p).name.upper()
               for p in files)
print("ok")
