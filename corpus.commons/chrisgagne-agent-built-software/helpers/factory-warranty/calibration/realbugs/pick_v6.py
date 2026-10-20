"""PREREG-v6's sample: 20 ReviewBench pull requests nobody here has reviewed. Reads only the manifest and the test set
(never the golden findings): excludes the 25 test-set pull requests and v5's cost probe, keeps those with at most
2,000 changed lines, and draws 20 with random.Random(20261019). Writes v6-cases.json.

  python pick_v6.py /path/to/ReviewBench   # at commit 12e9d1a
"""
import json
import random
import sys
from pathlib import Path

rb = Path(sys.argv[1])
manifest = json.loads((rb / "corpus" / "manifest.json").read_text())
test = {(t["repo"], str(t["pr_number"])) for t in json.loads((rb / "corpus" / "test" / "test.json").read_text())}
probe = ("https://github.com/AgentParadise/agent-paradise-standards-system", "61")
pool = [m for m in manifest if (m["repo"], str(m["pr_number"])) not in test | {probe}
        and int(m["lines_added"]) + int(m["lines_removed"]) <= 2000]
picked = random.Random(20261019).sample(pool, 20)
cases = [{"id": f"rc{i:02d}", "kind": "pr", "project": m["nwo"].replace("/", "_"), "repo": m["repo"],
          "pr_number": int(m["pr_number"]), "base": m["base"], "head": m["head"], "title": m["title"],
          "body": m.get("body") or "", "language": m.get("language")} for i, m in enumerate(picked, 1)]
Path(__file__).with_name("v6-cases.json").write_text(json.dumps({"method": __doc__.strip(), "cases": cases}, indent=1))
print(len(pool), "eligible;", len(cases), "picked;", sorted({c["language"] for c in cases}))
