#!/usr/bin/env python3
"""quotes.py without a target: list every quotation of five words or more in a text and where it sits.

    GF_CONVERTED=... python3 quotes_free.py ANSWER.md

Prints one line per quotation: found slug:line, or MISSING.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from locate import find  # noqa: E402
from quotes import quotations  # noqa: E402


def main():
    text = Path(sys.argv[1]).read_text()
    rows = [(part, find(part)) for part in quotations(text)]
    print(f"{len(rows)} quotations, {sum(1 for _, h in rows if h)} found")
    for part, hits in rows:
        where = ", ".join(f"{s}:{l}" for s, l in hits[:3])
        print(f"  {'found' if hits else 'MISSING':8} {where:45} {part[:100]}")


if __name__ == "__main__":
    main()
