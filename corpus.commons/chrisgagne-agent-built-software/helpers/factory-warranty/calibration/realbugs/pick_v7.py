"""PREREG-v7's sample: every ReviewBench pull request outside the test set, v5's cost probe and v6's sample, with at most
2,000 changed lines, whose golden set holds at least one true high-severity finding. Reads only each golden finding's
`tp_fp` and `severity` labels. Writes v7-cases.json, in manifest order.

  python pick_v7.py /path/to/ReviewBench   # at commit 12e9d1a
"""
import json
import sys
from pathlib import Path

rb = Path(sys.argv[1])
here = Path(__file__).resolve().parent
manifest = json.loads((rb / "corpus" / "manifest.json").read_text())
seen = {(t["repo"], str(t["pr_number"])) for t in json.loads((rb / "corpus" / "test" / "test.json").read_text())}
seen |= {(c["repo"], str(c["pr_number"])) for c in json.loads((here / "v6-cases.json").read_text())["cases"]}
seen.add(("https://github.com/AgentParadise/agent-paradise-standards-system", "61"))


def serious(m) -> bool:
    hits = list((rb / "golden").glob(f"{m['nwo'].replace('/', '_')}_{m['pr_number']}-*.json"))
    return bool(hits) and any(f.get("tp_fp") == "tp" and f.get("severity") == "high"
                              for f in json.loads(hits[0].read_text())["findings"])


picked = [m for m in manifest if (m["repo"], str(m["pr_number"])) not in seen
          and int(m["lines_added"]) + int(m["lines_removed"]) <= 2000 and serious(m)]
cases = [{"id": f"rd{i:02d}", "kind": "pr", "project": m["nwo"].replace("/", "_"), "repo": m["repo"],
          "pr_number": int(m["pr_number"]), "base": m["base"], "head": m["head"], "title": m["title"],
          "body": m.get("body") or "", "language": m.get("language")} for i, m in enumerate(picked, 1)]
(here / "v7-cases.json").write_text(json.dumps({"method": __doc__.strip(), "cases": cases}, indent=1))
print(len(cases), "picked;", sorted({c["language"] for c in cases}))
