#!/usr/bin/env python3
"""Copy a rendered verbatim-mode report into a folder fit to publish (a repo's docs/, GitHub Pages).

    python3 scripts/verbatim/publish.py <report-folder> <dest-folder> \
        --converted-url https://github.com/{owner}/{repo}/blob/main/{corpus-root} [--passages]

Refuses a report with any source above open-nc: copyrighted, confidential or personal text is
never published. Of what the report folder holds, the copy keeps:

- the page and its data (preview.html, bundle.json, report.json, answer.md, vendor/);
- one page image per span, the page with the passage highlighted (pages/), not the pages
  either side;
- no original files, which a repo may not be allowed to redistribute (an NC source's original
  never ships) and which are large; the page's "original" link greys out;
- no converted text: each span's "converted text, line N" link points at the tracked file in
  the repository instead, opening at that line.

Deterministic: no model in the loop.
"""
import argparse, json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from flatten import flatten   # noqa: E402

OPEN = ("open", "open-nc")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", type=Path)
    ap.add_argument("dest", type=Path)
    ap.add_argument("--converted-url", required=True, help="URL of the corpus root in the repository's file view; each source's converted path is appended")
    ap.add_argument("--passages", action="store_true", help="open with pointed paraphrases shown as the author's passages")
    args = ap.parse_args()
    src, dest = args.report.resolve(), args.dest.resolve()
    report = json.loads((src / "report.json").read_text())
    bundle = json.loads((src / "bundle.json").read_text())

    closed = {k: s.get("scope") for k, s in bundle["sources"].items() if s.get("scope") not in OPEN}
    if closed:
        raise SystemExit(f"not published: sources above open-nc: {closed}")

    if dest.exists():
        shutil.rmtree(dest)
    (dest / "pages").mkdir(parents=True)
    shutil.copytree(src / "vendor", dest / "vendor")
    for s in bundle["sources"].values():
        s["served"] = None
        s["converted_local"] = f"{args.converted_url.rstrip('/')}/{s['converted']}?plain=1"
    for sp in bundle["spans"].values():
        sp["pages"] = [p for p in sp.get("pages", []) if p["boxes"]]
        for p in sp["pages"]:
            shutil.copyfile(src / p["png"], dest / p["png"])
    (dest / "bundle.json").write_text(json.dumps(bundle, ensure_ascii=False, indent=1))
    (dest / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1))

    init = {"verbatim": 1.0, "joins": report.get("mode", {}).get("joins", "essay"), "ctx": "paras:1", "ship": False, "passages": args.passages}
    html = (HERE / "template.html").read_text()
    for marker, value in (("/*__REPORT__*/", report), ("/*__BUNDLE__*/", bundle), ("/*__INIT__*/", init)):
        html = html.replace(marker, json.dumps(value, ensure_ascii=False).replace("</", "<\\/"))
    (dest / "preview.html").write_text(html)
    (dest / "answer.md").write_text(flatten(dest)[0])
    pages = sum(len(sp["pages"]) for sp in bundle["spans"].values())
    print(f"published {dest}: {len(bundle['spans'])} spans, {pages} page images, no originals, converted text linked", file=sys.stderr)


if __name__ == "__main__":
    main()
