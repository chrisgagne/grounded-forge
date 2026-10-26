#!/usr/bin/env python3
"""Remove one ingested source from a corpus, as if it had never been ingested.

The mechanical half of the `removing-resources` skill. Dry run by default;
``--apply`` makes the changes, ``--audit`` has a fresh reviewer check the
skill's rewrites afterwards, ``--restore`` undoes them.

    python3 scripts/remove-source.py --corpus demo {slug} [--reason "superseded by X"] [--also "Short Name"] [--apply]
    python3 scripts/remove-source.py --corpus demo {slug} --audit [--family codex|claude] [--model M]
    python3 scripts/remove-source.py --corpus demo {slug} --restore

What it does, in order:

1. Moves ``sources/original/{slug}.*`` (the sidecar and any binary) to
   ``sources/removed/{slug}/``, stamping the sidecar with ``removed:`` and
   ``removed_reason:``.
2. Deletes the source's own artefacts: light and deep references, its
   distillations on every task axis, the converted text and its image folder,
   its own audit files under ``references/_audit/`` (other sources' audit
   files that mention it are history and stay), and its gitignored working
   files under ``_planning/`` (extracted, refs and discovery records, Pass I
   driver folder) and ``docs/images/``.
3. Drops its entries from ``IMAGE-INDEX.yaml`` and ``extraction-manifest.json``.
4. Edits each ``{TASK}-DISTILLATION-INDEX.md``: a row or bullet whose only
   distillation is this source's goes; a row shared with other sources loses
   this source's file and is listed for the skill to rewrite.
5. Takes the source off every concept row, so a row it alone credited goes,
   and a topic left with no rows goes too. With Pass H staging (the corpus's
   ingest machine) it edits ``decisions.json`` and ``topics.json`` through
   ``refile_sources`` and reassembles. Without it (a fresh clone: ``_planning/``
   is gitignored) it rebuilds the concept index from the shipped runtime and
   deep files with the same writer, so the output is what reassembly would give.
6. Retires its slug-table ID (the slug becomes ``null``; IDs are never reused)
   and drops it from ``reference-index.json`` (rebuilt from staging when there
   is staging, edited by ID when there isn't).
7. Rebuilds each axis's ``task-index.json`` from its edited operator view (the
   build ships them as committed), then runs the topic and slug-table checks.
   ``npm run build`` regenerates the apps and OKF bundles; the skill runs it
   after the cross-reference sweep.
8. Writes ``_planning/removals/{corpus}/{slug}.json``: every file outside the
   removed source's own that still names it by slug, title or ``--also`` name or
   term, across the corpus, the repo's top-level files, ``docs/``, ``deploy/``
   and the agent and skill folders.
   The skill works through that list.

Git restores tracked files. Every untracked file the run changes or deletes
(all of ``_planning/``, gitignored images, a whole ``corpus.local/`` corpus) is
first saved under ``_planning/removals/{corpus}/{slug}/backup/``; ``--restore``
puts those back and removes what the run created. Then ``git restore`` the
tracked half (the skill starts from a clean tree, so that is the whole diff).
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.build_indexes import refile_sources  # noqa: E402
from scripts.build_indexes.build_concept_index import _write_schema3  # noqa: E402
from scripts.build_indexes.common import corpus_root, staging_dir  # noqa: E402

# Where other files may still name the source. Audit records (under
# references/) and eval rounds are history and are left as they were. Under sources/ only the sidecars are
# the operator's own prose; converted and original texts are the sources'.
# Other sources' references describe their own source, never this one's
# contribution, so they are never edited.
SWEEP_EXCLUDE = ("/references/", "/apps/", "/okf/", "/distros/", "/chroma/", "/docs/evals/",
                 "/sources/removed/", "/node_modules/", "/.git/", "/worktrees/")
SWEEP_SUFFIXES = {".md", ".json", ".yaml", ".yml", ".txt", ".toml", ".js", ".mjs", ".py", ""}
# Repo-level places that name sources: top-level files, docs, deploy configs,
# and the agent and skill folders the harnesses read.
SWEEP_ROOTS = ("docs", "deploy", "tests", ".claude", ".codex", ".agents", ".claude-plugin", ".codex-plugin")
CODEX_CANDIDATES = ("/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex",
                    "/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex")
# Generated or rebuilt files the audit diff leaves out.
AUDIT_SKIP = ("/apps/", "/okf/", "task-index", "concept-index", "reference-index.json", "slug-table.json",
              "topic-payload.jsonl", "/_planning/removals/")
# Rebuilt from their inputs, so never edited by hand.
DERIVED = {"slug-table.json", "reference-index.json", "concept-index.json", "concept-index-deep.json",
           "task-index.json", "lens-index.json", "package-lock.json"}


def owns(name: str, slug: str, longer: list[str] = ()) -> bool:
    """Is this file one of the source's own artefacts? Its name is the slug,
    starts with ``{slug}-`` (a distillation, ``-deep``, an audit record), or
    carries the slug as an underscore-bounded token (pass artefacts). ``longer``
    is every other slug in the corpus that starts with ``{slug}-``: a file that
    belongs to one of those is not this source's."""
    stem = name.split(".")[0]
    if any(stem == o or stem.startswith(f"{o}-") or f"_{o}_" in f"_{stem}_" for o in longer):
        return False
    return stem == slug or stem.startswith(f"{slug}-") or f"_{slug}_" in f"_{stem}_"


def needle_pattern(term: str) -> re.Pattern:
    """A sweep term matches after a word boundary, so a stem still finds its
    endings. A short term or an acronym needs a boundary after it too, and an
    acronym matches case: "FLO" finds "FLO)" but not "flow"."""
    acronym = term.isupper() and len(term) > 1
    tail = r"(?![A-Za-z0-9])" if acronym or len(term) <= 5 else ""
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term) + tail, 0 if acronym else re.I)


def topics_from_runtime(runtime: dict, concepts: dict[str, dict]) -> dict:
    """Rebuild a topics.json-shaped doc from a schema-3 runtime index, keyed by
    topic ID, so ``_write_schema3`` can rewrite the index without staging."""
    by_name = {rec["name"]: key for key, rec in concepts.items()}
    topics, by_id = [], {}
    for line in runtime["topics"]:
        tid, name, synonyms, boundary, kind, broader = line[:6]
        topic = {"id": tid, "key": tid, "name": name, "synonyms": synonyms, "boundary": boundary,
                 "kind": kind, "broader": broader, "concepts": [], "examples": []}
        if kind == "debate":
            topic["positions"] = [{"label": label, "concepts": []} for label in line[8]]
        topics.append(topic)
        by_id[tid] = topic
    doc = {"topics": topics, "synonyms": {}, "unplaced": []}
    for row in runtime["concepts"]:
        name, kind, kept, _, refs = row[:5]
        key = by_name[name]
        if kept != concepts[key]["aliases"]:
            doc["synonyms"][key] = kept
        for ref in refs:
            tid, _, side = ref.partition(".")
            if side:
                by_id[tid]["positions"][int(side) - 1]["concepts"].append(key)
            else:
                by_id[tid]["concepts" if kind == "concept" else "examples"].append(key)
    return doc


def drop_empty_topics(topics_doc: dict) -> list[str]:
    """A topic left with no rows is a dead end for retrieval: it goes, and a
    topic that named it as broader loses the link."""
    def members(t: dict) -> int:
        return len(t.get("concepts", [])) + len(t.get("examples", [])) + sum(
            len(p.get("concepts", [])) for p in t.get("positions", []))
    gone = [t for t in topics_doc["topics"] if not members(t)]
    keys = {t["key"] for t in gone}
    topics_doc["topics"] = [t for t in topics_doc["topics"] if t["key"] not in keys]
    for t in topics_doc["topics"]:
        if t.get("broader") in keys:
            t["broader"] = ""
    return [t["name"] for t in gone]


def write_schema2(path: Path, header: dict, concepts: dict[str, dict]) -> None:
    """The compact runtime index for a corpus without topics, as assembly writes it."""
    rows = []
    for key in sorted(concepts):
        rec = concepts[key]
        row: list = [key, rec["name"], rec["aliases"], [s["id"] for s in rec["sources"]]]
        contexts = {s["id"]: s["context"] for s in rec["sources"] if "context" in s}
        if contexts:
            row.append(contexts)
        rows.append(json.dumps(row, ensure_ascii=False, separators=(",", ":")))
    head = "".join(f"{json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},\n" for k, v in header.items())
    path.write_text("{\n" + head + '"concepts": [\n' + ",\n".join(rows) + "\n]}\n", encoding="utf-8")


def write_deep(path: Path, doc: dict) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)


class Removal:
    def __init__(self, corpus: str, slug: str, reason: str, apply: bool, also: list[str]):
        self.corpus, self.slug, self.reason, self.apply, self.also = corpus, slug, reason, apply, also
        self.root = corpus_root(corpus)
        self.dist = self.root / "distillations"
        self.tasks = sorted(d.name for d in self.dist.iterdir() if d.is_dir()) if self.dist.is_dir() else []
        self.actions: list[str] = []
        self.rewrite: list[dict] = []
        self.deleted_rows: list[dict] = []
        self.rows_gone: list[str] = []
        self.rows_kept: list[dict] = []
        self.report_dir = REPO_ROOT / "_planning" / "removals" / corpus
        self.backup = self.report_dir / slug / "backup"
        self.manifest: dict = {"saved": [], "created": []}
        r = subprocess.run(["git", "ls-files"], cwd=REPO_ROOT, capture_output=True, text=True)
        self.tracked = set(r.stdout.splitlines()) if r.returncode == 0 else set()
        table = self.root / "references" / "slug-table.json"
        slugs = json.loads(table.read_text(encoding="utf-8"))["slugs"].values() if table.is_file() else []
        self.longer = [s for s in slugs if s and s != slug and s.startswith(f"{slug}-")]

    def owns(self, name: str) -> bool:
        return owns(name, self.slug, self.longer)

    def rel(self, p: Path) -> str:
        return str(p.relative_to(REPO_ROOT))

    def do(self, message: str, fn=None) -> None:
        self.actions.append(message)
        print(("  " if self.apply else "  [dry run] ") + message)
        if self.apply and fn:
            fn()

    # Backups: git holds tracked files; everything else is saved before it changes.
    def save(self, p: Path, move: bool = False) -> None:
        if not p.exists():
            return
        files = [p] if p.is_file() else [f for f in p.rglob("*") if f.is_file()]
        untracked = [f for f in files if self.rel(f) not in self.tracked]
        for f in untracked:
            rel = self.rel(f)
            dest = self.backup / rel
            if rel not in self.manifest["saved"]:
                dest.parent.mkdir(parents=True, exist_ok=True)
                (shutil.move if move else shutil.copy2)(str(f), dest)
                self.manifest["saved"].append(rel)
            elif move:
                f.unlink()
        self.write_manifest()

    def created(self, p: Path) -> None:
        self.manifest["created"].append(self.rel(p))
        self.write_manifest()

    def write_manifest(self) -> None:
        self.backup.mkdir(parents=True, exist_ok=True)
        (self.backup.parent / "manifest.json").write_text(json.dumps(self.manifest, indent=2) + "\n", encoding="utf-8")

    def remove(self, p: Path) -> None:
        self.save(p, move=True)
        if p.is_dir():
            shutil.rmtree(p)
        elif p.is_file():
            p.unlink()

    def write(self, p: Path, text: str) -> None:
        self.save(p)
        p.write_text(text, encoding="utf-8")

    # 1. The original moves to sources/removed/{slug}/.
    def move_original(self) -> None:
        dest = self.root / "sources" / "removed" / self.slug
        for f in sorted((self.root / "sources" / "original").glob(f"{self.slug}.*")):
            def move(f=f):
                self.save(f)
                dest.mkdir(parents=True, exist_ok=True)
                shutil.move(str(f), dest / f.name)
                self.created(dest / f.name)
                if f.name.endswith(".source.md"):
                    self.stamp(dest / f.name)
            self.do(f"move {self.rel(f)} -> {self.rel(dest / f.name)}", move)

    def stamp(self, sidecar: Path) -> None:
        text = sidecar.read_text(encoding="utf-8")
        lines = [f"removed: {date.today().isoformat()}"]
        if self.reason:
            lines.append(f"removed_reason: {json.dumps(self.reason, ensure_ascii=False)}")
        head, sep, rest = text[3:].partition("\n---")
        sidecar.write_text("---" + head.rstrip("\n") + "\n" + "\n".join(lines) + sep + rest, encoding="utf-8")

    # 2. The source's own artefacts go. Its light and deep references are kept
    # beside the report first: the audit needs them to recognise its content.
    def delete_own(self) -> None:
        refs = self.root / "references"
        for kind, f in (("light", refs / f"{self.slug}.md"), ("deep", refs / f"{self.slug}-deep.md")):
            if f.is_file():
                def keep(f=f, kind=kind):
                    (self.report_dir / self.slug).mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, self.report_dir / self.slug / f"removed-{kind}.md")
                self.do(f"keep a copy of {self.rel(f)} for the audit", keep)
        targets = [refs / f"{self.slug}.md", refs / f"{self.slug}-deep.md",
                   self.root / "sources" / "converted" / f"{self.slug}.md",
                   self.root / "sources" / "converted" / f"{self.slug}-images",
                   REPO_ROOT / "_planning" / "extracted" / self.corpus / f"{self.slug}.json",
                   staging_dir(self.corpus, "refs") / f"{self.slug}.json",
                   REPO_ROOT / "_planning" / "discovery" / f"{self.slug}.json",
                   REPO_ROOT / "_planning" / "pass-i" / self.corpus / self.slug,
                   REPO_ROOT / "docs" / "images" / f"_ingest_image_index_{self.slug}.yaml"]
        for task in self.tasks:
            targets += [f for f in (self.dist / task).glob(f"{self.slug}-{task}*.md") if self.owns(f.name)]
        audit = refs / "_audit"
        if audit.is_dir():
            targets += [f for f in audit.rglob("*") if f.is_file() and self.owns(f.name)]
        for t in targets:
            if t.exists():
                self.do(f"delete {self.rel(t)}{'/' if t.is_dir() else ''}", lambda t=t: self.remove(t))

    # 3. Image index and extraction manifest entries.
    def drop_images(self) -> None:
        converted = self.root / "sources" / "converted"
        index = converted / "IMAGE-INDEX.yaml"
        if index.is_file():
            text = index.read_text(encoding="utf-8")
            # Entries are top-level list items; split before each one.
            parts = re.split(r"(?m)^(?=- )", text)
            keep = [p for p in parts if not re.search(rf"(?m)^  source_ref: ['\"]?{re.escape(self.slug)}['\"]?\s*$", p)]
            if len(keep) != len(parts):
                self.do(f"drop {len(parts) - len(keep)} entries from {self.rel(index)}",
                        lambda: self.write(index, "".join(keep)))
        manifest = converted / "extraction-manifest.json"
        if manifest.is_file():
            entries = json.loads(manifest.read_text(encoding="utf-8"))
            prefix = f"/sources/converted/{self.slug}-images/"
            keep = [e for e in entries if prefix not in "/" + e.get("file", "")]
            if len(keep) != len(entries):
                self.do(f"drop {len(entries) - len(keep)} entries from {self.rel(manifest)}",
                        lambda: self.write(manifest, json.dumps(keep, indent=2, ensure_ascii=False) + "\n"))

    # 4. Operator-view distillation indexes.
    def edit_task_indexes(self) -> None:
        for task in self.tasks:
            for index in (self.dist / task).glob("*-DISTILLATION-INDEX.md"):
                name = f"{self.slug}-{task}.md"
                other = re.compile(r"[a-z0-9-]+-" + re.escape(task) + r"(--[a-z0-9-]+)?\.md")
                out, changed = [], 0
                original = index.read_text(encoding="utf-8").splitlines(keepends=True)
                for n, line in enumerate(original, 1):
                    if name not in line:
                        out.append(line)
                        continue
                    changed += 1
                    first = other.search(line)
                    bullet = not line.lstrip().startswith("|")
                    if not other.search(line.replace(name, "")) or (bullet and first and first.group(0) == name):
                        # A row or bullet that pointed only at this source goes whole, and so does
                        # a bullet about this source that merely mentions another ("pair with ...").
                        # Its need is listed so the skill can re-route it to a remaining source.
                        self.deleted_rows.append({"file": self.rel(index), "line": n, "text": line.strip()})
                        continue
                    if not bullet:
                        # Table row: drop this source's file from each comma-separated cell.
                        cells = line.rstrip("\n").split("|")
                        cells = [", ".join(i.strip() for i in c.split(",") if name not in i) if name in c else c
                                 for c in cells]
                        cells = [f" {c} " if c and not c.startswith(" ") else c for c in cells]
                        stripped = "|".join(cells) + "\n"
                    else:
                        stripped = line.replace(f"`{name}`", "").replace(name, "")
                    out.append(stripped)
                    self.rewrite.append({"file": self.rel(index), "line": n, "text": stripped.strip(),
                                         "why": "shared with other sources; the source's file is gone, its words may remain"})
                was_empty = {(x["text"], x["why"]) for x in self.empty_sections(index, original)}
                self.rewrite += [x for x in self.empty_sections(index, out) if (x["text"], x["why"]) not in was_empty]
                if changed:
                    self.do(f"edit {self.rel(index)}: {changed} lines name {name}",
                            lambda index=index, out=out: self.write(index, "".join(out)))

    def empty_sections(self, index: Path, lines: list[str]) -> list[dict]:
        """A table left with a header and no rows, or a heading left with nothing
        under it before the next heading of its level, means a phase or category
        lost its only source."""
        found, heading = [], ""
        for n, line in enumerate(lines):
            if line.startswith("#"):
                heading = line.strip("# \n")
            if re.match(r"^\|[\s:|-]+\|\s*$", line) and not (n + 1 < len(lines) and lines[n + 1].lstrip().startswith("|")):
                found.append({"file": self.rel(index), "line": n + 1, "text": heading,
                              "why": "this section's table has no rows left"})
        for n, line in enumerate(lines):
            level = len(line) - len(line.lstrip("#"))
            if not level or not line[level:level + 1] == " ":
                continue
            body = []
            for later in lines[n + 1:]:
                deeper = len(later) - len(later.lstrip("#"))
                if deeper and later[deeper:deeper + 1] == " " and deeper <= level:
                    break
                body.append(later)
            if not any(b.strip() and not b.startswith("#") for b in body):
                found.append({"file": self.rel(index), "line": n + 1, "text": line.strip("# \n"),
                              "why": "this section has nothing left under it"})
        return found

    # 5. Concept rows and topics.
    def drop_concepts(self, sid: str) -> None:
        if (staging_dir(self.corpus, "concepts") / "decisions.json").is_file():
            self.drop_concepts_staged(sid)
        else:
            self.drop_concepts_shipped(sid)

    def drop_concepts_staged(self, sid: str) -> None:
        folder = staging_dir(self.corpus, "concepts")
        decisions = json.loads((folder / "decisions.json").read_text(encoding="utf-8"))
        topics = json.loads((folder / "topics.json").read_text(encoding="utf-8"))
        rows = [d["name"] for d in decisions["decisions"]
                if any(s.get("id") == sid or s.get("slug") == self.slug for s in d.get("sources", []))]
        sole = sum(1 for d in decisions["decisions"] if d["name"] in rows and len(d["sources"]) == 1)
        proposal = {"batch": f"remove-{self.slug}",
                    "sources": [{"slug": self.slug, "id": sid, "removals": [{"row": r} for r in rows]}]}
        problems = refile_sources.validate(decisions, topics, [proposal], {self.slug: sid})
        if problems:
            sys.exit("concept removal won't apply:\n  " + "\n  ".join(problems[:20]))
        new_d, new_t, log = refile_sources.apply(decisions, topics, [proposal])
        gone = drop_empty_topics(new_t)
        self.rows_gone = [e["row"] for e in log if "is gone" in e["outcome"]]
        self.rows_kept = [{"row": d["name"], "aliases": d.get("aliases", [])} for d in new_d["decisions"] if d["name"] in rows]

        def run():
            for name, doc in (("decisions.json", new_d), ("topics.json", new_t)):
                self.write(folder / name, json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
            refile = folder / "refile"
            refile.mkdir(parents=True, exist_ok=True)
            applied = refile / f"applied-remove-{self.slug}.json"
            self.write(applied, json.dumps({"files": [], "changes": log, "topics_dropped": gone},
                                           indent=2, ensure_ascii=False) + "\n")
            self.created(applied)
        self.do(f"take {self.slug} off {len(rows)} concept rows in Pass H staging ({sole} rows it alone "
                f"credits go; {len(gone)} topics left empty go{': ' + ', '.join(gone) if gone else ''})", run)

    def drop_concepts_shipped(self, sid: str) -> None:
        runtime_path, deep_path = self.root / "concept-index.json", self.root / "concept-index-deep.json"
        if not deep_path.is_file():
            print("  no concept index in this corpus")
            return
        deep = json.loads(deep_path.read_text(encoding="utf-8"))
        runtime = json.loads(runtime_path.read_text(encoding="utf-8")) if runtime_path.is_file() else None
        concepts = deep["concepts"]
        topics_doc = topics_from_runtime(runtime, concepts) if runtime and runtime.get("schema_version") == 3 else None
        rows = [k for k, rec in concepts.items() if any(s["id"] == sid for s in rec["sources"])]
        sole = [k for k in rows if len(concepts[k]["sources"]) == 1]
        names = {k: concepts[k]["name"] for k in sole}
        for k in rows:
            concepts[k]["sources"] = [s for s in concepts[k]["sources"] if s["id"] != sid]
        filing = refile_sources.Filing(topics_doc) if topics_doc else None
        for k in sole:
            del concepts[k]
            if filing:
                filing.drop_concept(k)
        gone = drop_empty_topics(topics_doc) if topics_doc else []
        self.rows_gone = [names[k] for k in sole]
        self.rows_kept = [{"row": concepts[k]["name"], "aliases": concepts[k]["aliases"]} for k in rows if k in concepts]

        def run():
            self.save(runtime_path)
            self.save(deep_path)
            if topics_doc:
                _write_schema3(runtime_path, runtime["corpus"], concepts, topics_doc)
            elif runtime:
                write_schema2(runtime_path, {k: v for k, v in runtime.items() if k != "concepts"}, concepts)
            write_deep(deep_path, deep)
        self.do(f"take {self.slug} off {len(rows)} concept rows in the shipped index, no Pass H staging "
                f"({len(sole)} rows it alone credits go; {len(gone)} topics left empty go"
                f"{': ' + ', '.join(gone) if gone else ''})", run)

    # 6. Slug-table tombstone and reference index.
    def retire_id(self, table_path: Path, table: dict, sid: str) -> None:
        def run():
            table["slugs"][sid] = None
            self.write(table_path, json.dumps(table, indent=2, ensure_ascii=False) + "\n")
        self.do(f"retire slug-table ID {sid} (slug -> null)", run)
        ref_index = self.root / "reference-index.json"
        if not staging_dir(self.corpus, "refs").is_dir() and ref_index.is_file():
            doc = json.loads(ref_index.read_text(encoding="utf-8"))
            if sid in doc.get("refs", {}):
                def drop():
                    del doc["refs"][sid]
                    self.write(ref_index, json.dumps(doc, indent=2, ensure_ascii=False))
                self.do(f"drop ID {sid} from {self.rel(ref_index)} (no refs staging)", drop)

    # 7. Rebuild what staging feeds, then check.
    def rebuild(self) -> int:
        steps = []
        if staging_dir(self.corpus, "refs").is_dir():
            steps.append(["scripts.build_indexes.build_reference_index", "--corpus", self.corpus])
        # The build ships each axis's task-index.json as committed, so the
        # edited DISTILLATION-INDEX.md views must be turned into JSON here.
        steps.append(["scripts.build_indexes.build_task_index", "--corpus", self.corpus])
        concepts = staging_dir(self.corpus, "concepts")
        if (concepts / "decisions.json").is_file():
            steps += [["scripts.build_indexes.build_concept_index", "--corpus", self.corpus, "--assemble"],
                      ["scripts.build_indexes.build_concept_index", "--corpus", self.corpus, "--emit-topic-payload"],
                      ["scripts.build_indexes.check_topics", "--corpus", self.corpus]]
        failed = 0
        for step in steps:
            self.actions.append("run python3 -m " + " ".join(step))
            if not self.apply:
                print("  [dry run] run python3 -m " + " ".join(step))
                continue
            for p in [self.root / "reference-index.json", self.root / "concept-index.json",
                      self.root / "concept-index-deep.json", concepts / "topics.json", concepts / "topic-payload.jsonl",
                      *self.dist.glob("*/task-index*.json")]:
                self.save(p)
            r = subprocess.run([sys.executable, "-m", *step], cwd=REPO_ROOT, capture_output=True, text=True)
            tail = (r.stdout + r.stderr).strip().splitlines()[-3:]
            print(f"  {'ok  ' if r.returncode == 0 else 'FAIL'} {step[0]} {' '.join(step[3:])}")
            for t in tail:
                print(f"       {t}")
            failed += r.returncode != 0
        r = subprocess.run([sys.executable, "scripts/slug_table.py", "check", "--corpus", self.rel(self.root)],
                           cwd=REPO_ROOT, capture_output=True, text=True)
        if self.apply:
            print(f"  {'ok  ' if r.returncode == 0 else 'FAIL'} slug_table check {(r.stdout + r.stderr).strip()[:300]}")
            failed += r.returncode != 0
        return failed

    # 8. Everything else that still names the source.
    def sweep(self, title: str | None) -> list[dict]:
        needles = [self.slug, *self.also]
        if title:
            bare = re.sub(r"^(the|a|an)\s+", "", title, flags=re.I)
            needles += [title, bare, bare.split(":")[0].strip()]
        patterns = [needle_pattern(x) for x in dict.fromkeys(n.strip() for n in needles if n.strip())]
        hits = []
        files = [p for p in REPO_ROOT.iterdir() if p.is_file()]
        for r in [self.root, *(REPO_ROOT / d for d in SWEEP_ROOTS)]:
            files += [p for p in r.rglob("*") if p.is_file()] if r.is_dir() else []
        for f in files:
            path = "/" + self.rel(f)
            if f.suffix not in SWEEP_SUFFIXES or any(x in path for x in SWEEP_EXCLUDE):
                continue
            if "/sources/" in path and not f.name.endswith(".source.md"):
                continue
            if f.name in DERIVED or self.owns(f.name) or "/removing-resources/" in path:
                continue
            try:
                text = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            lines = [n for n, line in enumerate(text.splitlines(), 1) if any(p.search(line) for p in patterns)]
            if lines:
                hits.append({"file": self.rel(f), "lines": lines})
        return hits

    def run(self) -> int:
        table_path = self.root / "references" / "slug-table.json"
        table = json.loads(table_path.read_text(encoding="utf-8"))
        sid = next((k for k, v in table["slugs"].items() if v == self.slug), None)
        if sid is None:
            sys.exit(f"{self.slug} is not in {self.rel(table_path)}")
        if self.apply and (self.backup.parent / "manifest.json").is_file():
            sys.exit(f"a backup from an earlier run is at {self.rel(self.backup.parent)}; --restore it or delete it first")
        sidecar = self.root / "sources" / "original" / f"{self.slug}.source.md"
        title = None
        if sidecar.is_file():
            m = re.search(r'(?m)^title:\s*"?(.+?)"?\s*$', sidecar.read_text(encoding="utf-8"))
            title = m.group(1) if m else None
        print(f"{'Removing' if self.apply else 'Dry run: removing'} {self.slug} (ID {sid}) from {self.rel(self.root)}")

        self.move_original()
        self.delete_own()
        self.drop_images()
        self.edit_task_indexes()
        self.drop_concepts(sid)
        self.retire_id(table_path, table, sid)
        failed = self.rebuild()

        hits = self.sweep(title)
        report = {"corpus": self.corpus, "slug": self.slug, "id": sid, "title": title,
                  "reason": self.reason, "date": date.today().isoformat(), "applied": self.apply,
                  "actions": self.actions, "concept_rows_gone": self.rows_gone, "concept_rows_kept": self.rows_kept,
                  "index_rows_deleted": self.deleted_rows, "index_rows_to_rewrite": self.rewrite, "still_named_in": hits}
        out = self.report_dir / f"{self.slug}.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"\n{len(self.rewrite)} shared index rows and {len(hits)} files still name the source "
              f"(by slug, title or --also); a dry run's list includes files the run would delete or edit.")
        for h in hits:
            print(f"  {h['file']}: lines {', '.join(map(str, h['lines'][:12]))}{' ...' if len(h['lines']) > 12 else ''}")
        print(f"Report: {self.rel(out)}")
        if self.apply:
            print(f"Untracked files saved: {len(self.manifest['saved'])}, at {self.rel(self.backup)}. "
                  f"Undo: --restore, then git restore the tracked half.")
        else:
            print("Nothing changed. Rerun with --apply.")
        return 1 if failed else 0

    def restore(self) -> int:
        path = self.backup.parent / "manifest.json"
        if not path.is_file():
            sys.exit(f"no backup at {self.rel(self.backup.parent)}")
        manifest = json.loads(path.read_text(encoding="utf-8"))
        for rel in manifest["created"]:
            p = REPO_ROOT / rel
            if p.is_file():
                p.unlink()
                print(f"  delete {rel}")
        for rel in manifest["saved"]:
            dest = REPO_ROOT / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.backup / rel, dest)
            print(f"  restore {rel}")
        shutil.rmtree(self.backup.parent)
        print(f"Restored {len(manifest['saved'])} untracked files. Now restore the tracked half: "
              f"git restore --staged --worktree -- . (from the clean tree the removal started on).")
        return 0

    # Independent audit of the rewrites (the skill's audit step).
    def audit_diff(self) -> str:
        """Every edit to a file that still exists: git for tracked files, the
        run's backups for untracked ones (a corpus.local corpus is all untracked)."""
        r = subprocess.run(["git", "diff", "--diff-filter=M", "--no-color"], cwd=REPO_ROOT, capture_output=True, text=True)
        chunks = [c for c in re.split(r"(?m)^(?=diff --git )", r.stdout)
                  if c and not any(x in c.split("\n", 1)[0] for x in AUDIT_SKIP)]
        path = self.backup.parent / "manifest.json"
        saved = json.loads(path.read_text(encoding="utf-8"))["saved"] if path.is_file() else []
        for rel in saved:
            now = REPO_ROOT / rel
            if any(x in "/" + rel for x in AUDIT_SKIP) or "/_planning/" in "/" + rel or not now.is_file():
                continue
            before = (self.backup / rel).read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
            after = now.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
            if before != after:
                chunks.append("".join(difflib.unified_diff(before, after, f"a/{rel}", f"b/{rel}")))
        return "".join(chunks)

    def audit(self, family: str, model: str | None) -> int:
        work = self.report_dir / self.slug
        light, deep = work / "removed-light.md", work / "removed-deep.md"
        if not deep.is_file():
            sys.exit(f"no copy of the removed deep reference at {self.rel(deep)}; run --apply first")
        packet = work / "audit"
        packet.mkdir(parents=True, exist_ok=True)
        n = len(list(packet.glob("review-*.log"))) + 1  # every attempt, so a failed one isn't overwritten
        shutil.copy2(light if light.is_file() else deep, packet / "removed-light.md")
        shutil.copy2(deep, packet / "removed-deep.md")
        skill = REPO_ROOT / ".claude" / "skills" / "removing-resources"
        shutil.copy2(skill / "SKILL.md", packet / "skill.md")
        (packet / "diff.patch").write_text(self.audit_diff(), encoding="utf-8")
        report = json.loads((self.report_dir / f"{self.slug}.json").read_text(encoding="utf-8"))
        brief = (skill / "audit.md").read_text(encoding="utf-8").format(
            title=report.get("title") or self.slug, slug=self.slug, corpus=self.corpus,
            packet=self.rel(packet), corpus_path=self.rel(self.root))
        (packet / "brief.md").write_text(brief, encoding="utf-8")
        out = packet / f"review-{n}.md"
        prompt = f"Read {self.rel(packet / 'brief.md')} and do exactly what it says. Write your full answer as your final message."
        if family == "codex":
            binary = next((c for c in [os.environ.get("CODEX_BIN"), shutil.which("codex"), *CODEX_CANDIDATES]
                           if c and Path(c).exists()), None)
            if not binary:
                sys.exit("no Codex CLI found: put `codex` on PATH, set CODEX_BIN, or use --family claude")
            cmd = [binary, "exec", *(["-m", model] if model else []), "-s", "read-only",
                   "--skip-git-repo-check", "--ephemeral", "-C", str(REPO_ROOT), "-o", str(out), prompt]
        else:
            cmd = [os.environ.get("CLAUDE_BIN", "claude"), "-p", prompt, "--output-format", "json",
                   "--model", model or "opus", "--disallowedTools", "Edit", "Write", "NotebookEdit"]
        files = (packet / "diff.patch").read_text(encoding="utf-8").count("\n+++ b/")
        print(f"Audit round {n}: {family}{' ' + model if model else ''}, {files} edited file(s)")
        log = packet / f"review-{n}.log"
        with log.open("w") as f:
            code = subprocess.run(cmd, cwd=REPO_ROOT, stdout=f, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL).returncode
        if family == "claude" and not out.exists():
            try:
                out.write_text(json.loads(log.read_text())["result"], encoding="utf-8")
            except (json.JSONDecodeError, KeyError, OSError):
                pass
        if code or not out.is_file():
            print(f"FAIL: the auditor exited {code} and gave no review; see {self.rel(log)}. "
                  f"A failed attempt is not a round; rerun, or use --family claude if Codex is unavailable.")
            return 1
        verdict = re.findall(r"(?m)^Verdict:.*$", out.read_text(encoding="utf-8"))
        print(f"{verdict[-1] if verdict else 'Verdict: (none given)'}\nReview: {self.rel(out)}")
        return 0 if verdict and verdict[-1].strip() == "Verdict: clean" else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("slug")
    parser.add_argument("--corpus", required=True, help="bare corpus name, e.g. demo")
    parser.add_argument("--reason", default="", help="why it goes; stamped on the moved sidecar")
    parser.add_argument("--also", action="append", default=[],
                        help="another name other files use for the source, or a term only it supplies; repeatable")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="make the changes (default: dry run)")
    mode.add_argument("--restore", action="store_true", help="undo an applied run's untracked changes from its backup")
    mode.add_argument("--audit", action="store_true",
                      help="after the rewrite step: have a fresh reviewer audit every edit (exit 0 clean, 2 not clean)")
    parser.add_argument("--family", choices=["codex", "claude"], default="codex",
                        help="audit reviewer: codex (default; another model family) or a fresh claude -p")
    parser.add_argument("--model", help="audit reviewer model (default: the CLI's configured model; opus for claude)")
    args = parser.parse_args(argv)
    if not corpus_root(args.corpus).is_dir():
        sys.exit(f"no corpus named {args.corpus}")
    removal = Removal(args.corpus, args.slug, args.reason, args.apply, args.also)
    if args.audit:
        return removal.audit(args.family, args.model)
    return removal.restore() if args.restore else removal.run()


if __name__ == "__main__":
    sys.exit(main())
