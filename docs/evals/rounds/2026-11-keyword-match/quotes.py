#!/usr/bin/env python3
"""List every quotation of five words or more in an answer, and where it sits in the corpus.

    python3 quotes.py K01B ANSWER.md [ANSWER.md ...]

For each quotation: the source and line where it is found word for word (after
locate.py's normalisation), whether that line is inside the target's section,
or MISSING. An ellipsis inside a quotation splits it, and each part of five
words or more is located on its own. The question's own text is skipped, so a
quotation of the user's words isn't counted.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from locate import find, norm  # noqa: E402

# curly and straight pairs separately, within one line, so a stray mark can't pair across text
QUOTE = re.compile(r"“([^“”\n]{10,}?)”|\"([^\"\n]{10,}?)\"")


def quotations(text):
    for m in QUOTE.finditer(text):
        for part in re.split(r"\s*(?:\.\.\.|…|\[…\]|\[\.\.\.\])\s*", m.group(1) or m.group(2)):
            if len(norm(part).split()) >= 5:
                yield part.strip()


def main():
    qid, files = sys.argv[1], sys.argv[2:]
    q = next(x for x in json.loads((HERE / "questions.json").read_text()) if x["id"] == qid)
    t = next(x for x in json.loads((HERE / "targets.json").read_text()) if x["id"] == q["target"])
    asked = norm(q["question"])
    for f in files:
        text = Path(f).read_text()
        rows = []
        for part in quotations(text):
            if norm(part) in asked:
                continue
            hits = find(part)
            if not hits:
                rows.append(("MISSING", "", part))
                continue
            inside = any(s == t["slug"] and t["section"]["start"] <= l <= t["section"]["end"] for s, l in hits)
            where = ", ".join(f"{s}:{l}" for s, l in hits[:3])
            rows.append(("IN-SECTION" if inside else "found", where, part))
        exact = sum(r[0] != "MISSING" for r in rows)
        print(f"== {f}: {len(rows)} quotations, {exact} exact, {sum(r[0] == 'IN-SECTION' for r in rows)} in target section")
        for r in rows:
            print(f"  {r[0]:10} {r[1]:45} {r[2][:90]}")


if __name__ == "__main__":
    main()
