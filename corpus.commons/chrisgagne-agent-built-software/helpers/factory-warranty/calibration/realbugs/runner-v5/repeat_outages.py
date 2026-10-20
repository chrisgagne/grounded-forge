"""Amendment 2 (PREREG-v4): move each trial whose Amendment 1 re-run also failed on an outage to infra-failures-repeat/,
so the next `replay run` runs it again. Uses the pinned harness's own outage marker. Prints the count moved."""
import json, sys
from pathlib import Path
from factory.replay import infra_failure
out = Path(sys.argv[1]); n = 0
for p in sorted((out / "trials").glob("*.json")):
    rec = json.loads(p.read_text())
    marker = infra_failure(rec)
    if marker and (out / "infra-failures" / p.name).exists():
        d = out / "infra-failures-repeat"; d.mkdir(exist_ok=True)
        k = 1 + len(list(d.glob(f"{p.stem}.*.json")))
        rec["infra_marker"] = marker
        (d / f"{p.stem}.{k}.json").write_text(json.dumps(rec, indent=1)); p.unlink(); n += 1
print(n)
