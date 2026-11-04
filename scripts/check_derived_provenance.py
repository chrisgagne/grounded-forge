#!/usr/bin/env python3
"""Verify derived artefacts (light refs, distillations) are current with the
audited deep reference they were derived from.

The 9-pass ingestion protocol derives the light ref (Pass F) and distillations
(Pass G) *before* Pass I audits and edits the deep reference in place. Nothing
re-checks the derived tier after Pass I, so a strip at Pass I can leave the
light ref and distillations carrying content the deep no longer supports (the
private-corpus incident: Pass I stripped a fabricated cross-reference
table from the deep, but the light ref and distillations kept it). This tool
closes that gap: each derived artefact records the sha256 of the deep it was
derived from, and a mismatch means the deep moved and the derived artefact is
stale.

Stamp format — one HTML-comment line near the top of a derived artefact:

    <!-- derived-from-deep: sha256:<64-hex> -->

The stamp records the hash of the *deep* file (which carries no stamp of its
own), so there is no self-reference: editing the deep changes its hash and
invalidates every derived artefact's stamp until they are re-derived and
re-stamped. That is the point — it makes "derived from the verified deep"
mechanically testable rather than a prose promise.

A distillation draws on more than its own deep, so it carries two more lines:

    <!-- derived-from-task: sha256:<64-hex> -->
    <!-- derived-from-neighbours: <slug>@<16-hex> <slug>@<16-hex> ... -->

The task line hashes the task spec at `tasks/{task}.md` (omitted when the corpus
has no spec for that task). The neighbours line hashes, truncated to 16 hex, the
deep of every other source the distillation names: its cross-reference rows say
what those sources say, so a neighbour's deep moving can leave a row wrong while
the distillation's own deep is untouched. `none` records a distillation that
names no neighbour. Neighbours are found by slug in the text, the same way a
reader finds them.

Usage:
    python3 scripts/check_derived_provenance.py --corpus <name>
        Check mode. Exit 1 if any derived artefact carries a STALE stamp
        (present but != the current hash of its deep, task spec or a stamped
        neighbour; a stamped neighbour whose deep is gone also reads STALE).
        UNSTAMPED artefacts or stamp lines warn (adoption is gradual; new
        ingestions stamp going forward), as does a neighbour the text names but
        the stamp does not.

    python3 scripts/check_derived_provenance.py --corpus <name> --stamp [--slug S ...]
        Stamp mode. Write / refresh the stamps on derived artefacts with the
        current hashes. Restrict to specific sources with --slug (repeatable).
        Only stamp artefacts you have verified current with their deep, task
        spec and neighbours: stamping asserts the artefact is up to date.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
# The trailing class is horizontal whitespace only. `\s*$` under MULTILINE
# swallows the newlines after the stamp, so re-stamping an artefact deleted the
# blank line between the stamp and the H1 that every file in the corpus carries.
STAMP_RE = re.compile(
    r"^<!--[ \t]*derived-from-deep:[ \t]*sha256:([0-9a-f]{64})[ \t]*-->[ \t]*$",
    re.MULTILINE,
)
TASK_RE = re.compile(
    r"^<!--[ \t]*derived-from-task:[ \t]*sha256:([0-9a-f]{64})[ \t]*-->[ \t]*$",
    re.MULTILINE,
)
NEIGHBOURS_RE = re.compile(
    r"^<!--[ \t]*derived-from-neighbours:[ \t]*(.*?)[ \t]*-->[ \t]*$",
    re.MULTILINE,
)
NEIGHBOUR_HEX = 16


def corpus_root(name: str) -> Path:
    """Resolve a corpus by name, commons before local (matches common.py)."""
    for tier in ("corpus.commons", "corpus.local"):
        candidate = REPO_ROOT / tier / name
        if candidate.is_dir():
            return candidate
    raise SystemExit(
        f"corpus '{name}' not found under corpus.commons/ or corpus.local/"
    )


def deep_hash(deep_path: Path) -> str:
    return hashlib.sha256(deep_path.read_bytes()).hexdigest()


def read_stamp(text: str) -> str | None:
    m = STAMP_RE.search(text)
    return m.group(1) if m else None


def read_task_stamp(text: str) -> str | None:
    m = TASK_RE.search(text)
    return m.group(1) if m else None


def read_neighbours_stamp(text: str) -> dict[str, str] | None:
    """{slug: 16-hex} from the neighbours line, {} for `none`, None if absent."""
    m = NEIGHBOURS_RE.search(text)
    if not m:
        return None
    body = m.group(1).strip()
    if body == "none":
        return {}
    return dict(tok.split("@", 1) for tok in body.split())


def slug_pattern(slugs: list[str]) -> re.Pattern[str]:
    """Match any slug as a whole token. Longest first, so a slug that extends
    another (`foo-bar` vs `foo`) wins at the same position; a trailing hyphen is
    allowed so `{slug}-{task}.md` file links count."""
    alts = "|".join(re.escape(s) for s in sorted(slugs, key=len, reverse=True))
    return re.compile(rf"(?<![a-z0-9-])({alts})(?![a-z0-9])")


def cited_neighbours(text: str, own: str, pattern: re.Pattern[str]) -> set[str]:
    return {m.group(1) for m in pattern.finditer(text)} - {own}


def derived_artefacts(root: Path, slug: str) -> list[Path]:
    """Light ref plus one distillation per task dir for a given source slug."""
    out: list[Path] = []
    light = root / "references" / f"{slug}.md"
    if light.exists():
        out.append(light)
    dist_root = root / "distillations"
    if dist_root.is_dir():
        for task_dir in sorted(dist_root.iterdir()):
            if not task_dir.is_dir():
                continue
            dist = task_dir / f"{slug}-{task_dir.name}.md"
            if dist.exists():
                out.append(dist)
    return out


def upsert_line(text: str, pattern: re.Pattern[str], line: str, after: re.Pattern[str] | None) -> str:
    """Replace the line `pattern` matches, or insert it after the line `after`
    matches (else after a leading generation-header comment, else at the top)."""
    if pattern.search(text):
        return pattern.sub(lambda _: line, text, count=1)
    lines = text.split("\n")
    anchor = after.search(text) if after else None
    if anchor:
        insert_at = text.count("\n", 0, anchor.start()) + 1
    else:
        insert_at = 1 if lines and lines[0].lstrip().startswith("<!--") else 0
    lines.insert(insert_at, line)
    return "\n".join(lines)


def write_stamp(
    path: Path,
    h: str,
    task_h: str | None = None,
    neighbours: dict[str, str] | None = None,
) -> None:
    """Stamp the deep hash; for a distillation also the task spec (when one
    exists) and neighbours (always, `none` when it names no other source)."""
    text = path.read_text(encoding="utf-8")
    text = upsert_line(text, STAMP_RE, f"<!-- derived-from-deep: sha256:{h} -->", None)
    last = STAMP_RE
    if task_h is not None:
        text = upsert_line(text, TASK_RE, f"<!-- derived-from-task: sha256:{task_h} -->", last)
        last = TASK_RE
    if neighbours is not None:
        body = " ".join(f"{s}@{neighbours[s]}" for s in sorted(neighbours)) or "none"
        text = upsert_line(text, NEIGHBOURS_RE, f"<!-- derived-from-neighbours: {body} -->", last)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--corpus", help="corpus name (e.g. demo, aarbuddy)")
    ap.add_argument(
        "--root",
        help="explicit corpus root path, bypassing --corpus name resolution "
        "(the regression test points this at a fixture corpus)",
    )
    ap.add_argument("--stamp", action="store_true", help="write/refresh stamps")
    ap.add_argument(
        "--slug", action="append", default=[], help="restrict to source slug(s)"
    )
    args = ap.parse_args()

    if args.root:
        root = Path(args.root).resolve()
        if not root.is_dir():
            raise SystemExit(f"--root path not found: {root}")
    elif args.corpus:
        root = corpus_root(args.corpus)
    else:
        ap.error("one of --corpus or --root is required")
    deep_files = sorted((root / "references").glob("*-deep.md"))
    slug_filter = set(args.slug)
    deep_hashes = {d.name[: -len("-deep.md")]: deep_hash(d) for d in deep_files}
    pattern = slug_pattern(list(deep_hashes)) if deep_hashes else None

    ok: list[str] = []
    unstamped: list[str] = []
    stale: list[str] = []
    stamped: list[str] = []

    for slug, h in deep_hashes.items():
        if slug_filter and slug not in slug_filter:
            continue
        for art in derived_artefacts(root, slug):
            try:
                rel = art.relative_to(REPO_ROOT).as_posix()
            except ValueError:
                # --root may point outside the repo (e.g. a test fixture); artefacts
                # are always under root, so fall back to a root-relative display path.
                rel = art.relative_to(root).as_posix()
            text = art.read_text(encoding="utf-8")
            is_dist = art.parent.parent.name == "distillations"
            task_h = cited = None
            if is_dist:
                spec = root / "tasks" / f"{art.parent.name}.md"
                task_h = deep_hash(spec) if spec.exists() else None
                cited = cited_neighbours(text, slug, pattern) if pattern else set()
            if args.stamp:
                neighbours = (
                    {n: deep_hashes[n][:NEIGHBOUR_HEX] for n in cited} if is_dist else None
                )
                write_stamp(art, h, task_h, neighbours)
                stamped.append(rel)
                continue
            reasons: list[str] = []
            missing: list[str] = []
            s = read_stamp(text)
            if s is None:
                missing.append("deep")
            elif s != h:
                reasons.append(f"deep: stamp {s[:12]}… != {h[:12]}…")
            if is_dist:
                ts = read_task_stamp(text)
                if task_h is not None and ts is None:
                    missing.append("task")
                elif ts is not None and ts != task_h:
                    reasons.append("task spec moved" if task_h else "task spec gone")
                ns = read_neighbours_stamp(text)
                if ns is None:
                    missing.append("neighbours")
                else:
                    for n, nh in sorted(ns.items()):
                        if n not in deep_hashes:
                            reasons.append(f"neighbour {n}: deep gone")
                        elif deep_hashes[n][:NEIGHBOUR_HEX] != nh:
                            reasons.append(f"neighbour {n} moved")
                    extra = sorted(cited - set(ns))
                    if extra:
                        missing.append("neighbours " + ", ".join(extra))
            if reasons:
                stale.append(f"{rel}  ({'; '.join(reasons)})")
            elif missing:
                unstamped.append(f"{rel}  (no stamp for {'; '.join(missing)})")
            else:
                ok.append(rel)

    if args.stamp:
        for p in stamped:
            print(f"stamped  {p}")
        if slug_filter and not stamped:
            print(f"(no derived artefacts found for slug(s): {', '.join(sorted(slug_filter))})")
        print(f"\nStamped {len(stamped)} derived artefact(s).")
        return 0

    for p in ok:
        print(f"OK       {p}")
    for p in unstamped:
        print(f"WARN     unstamped  {p}")
    for p in stale:
        print(f"STALE    {p}")
    print(
        f"\n{len(ok)} current, {len(unstamped)} unstamped (warn), {len(stale)} STALE."
    )
    if stale:
        sys.stderr.write(
            "\nStale derived artefacts: a deep, task spec or neighbour moved after "
            "this artefact was derived.\nRe-derive (Pass F / Pass G) or re-check "
            "the rows that draw on what moved, then re-stamp with --stamp.\n"
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
