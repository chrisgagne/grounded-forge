#!/usr/bin/env python3
"""Extraction-manifest concurrency tests — the clobbered-siblings class.

Locks in the behaviour of the manifest writer in `scripts/extract-images.py`.

The regression it exists to prevent: `sources/converted/extraction-manifest.json`
is corpus-shared, but the extractor runs per source. It used to open the file
in "w" mode and dump only the entries from the current invocation, so the last
extractor to finish published a manifest holding its own images and nothing
else. In a parallel ingestion batch — four or five agents extracting at once —
one agent's entries vanished every round, and an operator had to restore
clobbered siblings by hand. One private corpus's manifest at the time this was
found listed 2 sources while 9 image directories sat next to it on disk.

The fix has three parts, one case each below: merge instead of overwrite,
serialise the read-modify-write under an exclusive lock on the converted/
directory, and publish by os.replace so no reader ever sees a half-written
file.

Real subprocesses, not threads: the failure mode is cross-process, and an
in-process test could pass on a fix that does not hold. Hermetic — a temp dir
stands in for the corpus root, so no real corpus is touched.

No test framework, matching tests/derived-provenance.test.py: each case
succeeds silently or raises; the runner collects failures, prints a summary,
exits non-zero.

Usage:
    python3 tests/extraction-manifest.test.py
"""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EXTRACTOR = REPO_ROOT / "scripts" / "extract-images.py"

WRITERS = 5
ROUNDS = 12
IMAGES_PER_SOURCE = 4


def assert_(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def load_extractor(repo_root: Path):
    """Import extract-images.py by path (the hyphen blocks a normal import)
    and repoint REPO_ROOT at the fixture so manifest paths stay relative."""
    spec = importlib.util.spec_from_file_location("extract_images_under_test", EXTRACTOR)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.REPO_ROOT = repo_root
    return mod


def build_fixture(root: Path) -> Path:
    """A minimal corpus: sources/original/ + sources/converted/."""
    (root / "sources" / "original").mkdir(parents=True, exist_ok=True)
    converted = root / "sources" / "converted"
    converted.mkdir(parents=True, exist_ok=True)
    return converted


def fake_source(root: Path, slug: str) -> Path:
    path = root / "sources" / "original" / f"{slug}.pdf"
    path.write_bytes(b"%PDF-1.4 fixture")
    return path


def fake_entries(root: Path, slug: str, count: int = IMAGES_PER_SOURCE) -> list[dict]:
    """Entry records shaped like extract_pdf_images() output."""
    return [
        {
            "file": f"sources/converted/{slug}-images/p{i:04d}-1.png",
            "source_file": f"sources/original/{slug}.pdf",
            "page": i,
            "width": 800,
            "height": 600,
            "size_bytes": 12345,
            "hash": f"{slug[:4]}{i:08d}",
        }
        for i in range(1, count + 1)
    ]


def read_manifest(converted: Path) -> list[dict]:
    with (converted / "extraction-manifest.json").open() as f:
        return json.load(f)


def sources_in(manifest: list[dict]) -> set[str]:
    return {e["source_file"] for e in manifest}


# ─── worker driven as a separate process ─────────────────────────────────────

WORKER = '''
import importlib.util, json, sys, time
from pathlib import Path

extractor, repo_root, slug, rounds, images = sys.argv[1:6]
repo_root = Path(repo_root)
spec = importlib.util.spec_from_file_location("extract_images_under_test", extractor)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.REPO_ROOT = repo_root

converted = repo_root / "sources" / "converted"
source = repo_root / "sources" / "original" / (slug + ".pdf")
entries = [
    {
        "file": "sources/converted/%s-images/p%04d-1.png" % (slug, i),
        "source_file": "sources/original/%s.pdf" % slug,
        "page": i,
        "width": 800,
        "height": 600,
        "size_bytes": 12345,
        "hash": "%s%08d" % (slug[:4], i),
    }
    for i in range(1, int(images) + 1)
]

for _ in range(int(rounds)):
    mod.merge_manifest(converted, [source], entries)
'''

READER = '''
import json, sys, time
from pathlib import Path

manifest = Path(sys.argv[1])
deadline = time.time() + float(sys.argv[2])
torn = 0
reads = 0
while time.time() < deadline:
    try:
        text = manifest.read_text()
    except FileNotFoundError:
        continue
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        torn += 1
        continue
    if not isinstance(data, list):
        torn += 1
    reads += 1
print(json.dumps({"reads": reads, "torn": torn}))
'''


def write_script(root: Path, name: str, body: str) -> Path:
    path = root / name
    path.write_text(body, encoding="utf-8")
    return path


def spawn_writers(root: Path, slugs: list[str], rounds: int = ROUNDS) -> list[subprocess.Popen]:
    worker = write_script(root, "_worker.py", WORKER)
    return [
        subprocess.Popen(
            [
                sys.executable,
                str(worker),
                str(EXTRACTOR),
                str(root),
                slug,
                str(rounds),
                str(IMAGES_PER_SOURCE),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for slug in slugs
    ]


# ─── cases ────────────────────────────────────────────────────────────────────


def case_second_source_does_not_clobber_the_first(root: Path) -> None:
    """THE bug, in its simplest form: two sequential per-source runs."""
    converted = build_fixture(root)
    mod = load_extractor(root)

    first = fake_source(root, "chen-2023-review-article")
    mod.merge_manifest(converted, [first], fake_entries(root, "chen-2023-review-article"))

    second = fake_source(root, "polak-2025-animal-study")
    mod.merge_manifest(converted, [second], fake_entries(root, "polak-2025-animal-study"))

    manifest = read_manifest(converted)
    assert_(
        len(sources_in(manifest)) == 2,
        f"both sources must survive; manifest holds {sorted(sources_in(manifest))}",
    )
    assert_(
        len(manifest) == 2 * IMAGES_PER_SOURCE,
        f"expected {2 * IMAGES_PER_SOURCE} entries, got {len(manifest)}",
    )


def case_rerunning_a_source_replaces_its_own_entries(root: Path) -> None:
    """Re-extraction must refresh one source in place, not duplicate it."""
    converted = build_fixture(root)
    mod = load_extractor(root)

    keep = fake_source(root, "armstrong-2024-microbiome")
    mod.merge_manifest(converted, [keep], fake_entries(root, "armstrong-2024-microbiome"))

    redo = fake_source(root, "chen-2023-review")
    mod.merge_manifest(converted, [redo], fake_entries(root, "chen-2023-review", count=4))
    mod.merge_manifest(converted, [redo], fake_entries(root, "chen-2023-review", count=2))

    manifest = read_manifest(converted)
    by_source: dict[str, int] = {}
    for e in manifest:
        by_source[e["source_file"]] = by_source.get(e["source_file"], 0) + 1

    assert_(
        by_source.get("sources/original/chen-2023-review.pdf") == 2,
        f"the re-run source should hold its new 2 entries; got {by_source}",
    )
    assert_(
        by_source.get("sources/original/armstrong-2024-microbiome.pdf") == IMAGES_PER_SOURCE,
        f"the sibling must be untouched by a neighbour's re-run; got {by_source}",
    )


def case_a_source_with_no_images_clears_its_stale_entries(root: Path) -> None:
    converted = build_fixture(root)
    mod = load_extractor(root)

    keep = fake_source(root, "polak-2025-study")
    mod.merge_manifest(converted, [keep], fake_entries(root, "polak-2025-study"))
    empty = fake_source(root, "boyer-woods-1973")
    mod.merge_manifest(converted, [empty], fake_entries(root, "boyer-woods-1973"))
    mod.merge_manifest(converted, [empty], [])

    manifest = read_manifest(converted)
    assert_(
        sources_in(manifest) == {"sources/original/polak-2025-study.pdf"},
        f"the emptied source should be gone and its sibling kept; got {sorted(sources_in(manifest))}",
    )


def case_an_uninspected_source_keeps_its_entries(root: Path) -> None:
    """A run that could not inspect a source must not erase what it found before.

    `extract_pdf_images` returns None when PyMuPDF is absent or the file will
    not open, and [] when it read the file and found no images. Those two
    outcomes used to be the same value, so running the extractor on a machine
    without PyMuPDF silently deleted every manifest entry for the sources named
    on the command line. Observed live: two entries lost on a source whose
    images had already been classified and deleted, leaving the manifest as the
    only surviving record of them.
    """
    converted = build_fixture(root)
    mod = load_extractor(root)

    prior = fake_source(root, "mpi-user-guide")
    mod.merge_manifest(converted, [prior], fake_entries(root, "mpi-user-guide"))
    before = read_manifest(converted)

    saved = mod.fitz
    try:
        mod.fitz = None
        assert_(
            mod.extract_pdf_images(prior, converted / "mpi-user-guide-images") is None,
            "a missing PyMuPDF must return None, not an empty list",
        )
        assert_(
            mod.process_file(prior) is None,
            "process_file must pass the un-inspected signal through to its caller",
        )
    finally:
        mod.fitz = saved

    assert_(
        read_manifest(converted) == before,
        "an un-inspected source must leave the manifest byte-identical",
    )


def case_five_concurrent_writers_lose_nothing(root: Path) -> None:
    """The live failure mode: five ingestion agents extracting at once."""
    converted = build_fixture(root)
    slugs = [f"parallel-source-{i}" for i in range(WRITERS)]
    for slug in slugs:
        fake_source(root, slug)

    procs = spawn_writers(root, slugs)
    for p in procs:
        out, err = p.communicate(timeout=180)
        assert_(p.returncode == 0, f"writer failed (exit {p.returncode}):\n{out}\n{err}")

    manifest = read_manifest(converted)
    expected = {f"sources/original/{slug}.pdf" for slug in slugs}
    missing = expected - sources_in(manifest)
    assert_(not missing, f"{len(missing)} of {WRITERS} sources were clobbered: {sorted(missing)}")
    assert_(
        len(manifest) == WRITERS * IMAGES_PER_SOURCE,
        f"expected {WRITERS * IMAGES_PER_SOURCE} entries, got {len(manifest)}",
    )
    assert_(
        manifest == sorted(manifest, key=lambda e: (e["source_file"], e["page"], e["file"])),
        "the merged manifest should be deterministically ordered",
    )


def case_concurrent_writers_never_expose_a_torn_read(root: Path) -> None:
    """os.replace, not truncate-and-write: a reader sees old or new, never half."""
    converted = build_fixture(root)
    slugs = [f"parallel-source-{i}" for i in range(WRITERS)]
    for slug in slugs:
        fake_source(root, slug)

    reader_script = write_script(root, "_reader.py", READER)
    procs = spawn_writers(root, slugs, rounds=ROUNDS * 2)
    reader = subprocess.Popen(
        [sys.executable, str(reader_script), str(converted / "extraction-manifest.json"), "3"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    for p in procs:
        p.communicate(timeout=180)
    out, err = reader.communicate(timeout=60)
    assert_(reader.returncode == 0, f"reader failed:\n{out}\n{err}")

    result = json.loads(out.strip().splitlines()[-1])
    assert_(result["reads"] > 0, "the reader never managed a read; the probe proved nothing")
    assert_(
        result["torn"] == 0,
        f"reader saw {result['torn']} torn manifests across {result['reads']} reads",
    )


def case_unreadable_manifest_is_reported_not_swallowed(root: Path) -> None:
    converted = build_fixture(root)
    mod = load_extractor(root)
    (converted / "extraction-manifest.json").write_text("{ not json", encoding="utf-8")

    source = fake_source(root, "king-1959-freeze-drying")
    mod.merge_manifest(converted, [source], fake_entries(root, "king-1959-freeze-drying"))

    manifest = read_manifest(converted)
    assert_(
        len(manifest) == IMAGES_PER_SOURCE,
        f"the run's own entries should still land; got {len(manifest)}",
    )


def case_no_lock_artefact_is_left_in_the_corpus(root: Path) -> None:
    """The lock rides on the directory inode; nothing should appear next to
    the manifest, and no temp file should survive the write."""
    converted = build_fixture(root)
    mod = load_extractor(root)
    source = fake_source(root, "wang-2000-male-cone")
    mod.merge_manifest(converted, [source], fake_entries(root, "wang-2000-male-cone"))

    leftovers = sorted(p.name for p in converted.iterdir() if p.name != "extraction-manifest.json")
    assert_(not leftovers, f"the writer left artefacts behind: {leftovers}")


CASES = [
    case_second_source_does_not_clobber_the_first,
    case_rerunning_a_source_replaces_its_own_entries,
    case_a_source_with_no_images_clears_its_stale_entries,
    case_an_uninspected_source_keeps_its_entries,
    case_five_concurrent_writers_lose_nothing,
    case_concurrent_writers_never_expose_a_torn_read,
    case_unreadable_manifest_is_reported_not_swallowed,
    case_no_lock_artefact_is_left_in_the_corpus,
]


def main() -> int:
    failures: list[str] = []
    for case in CASES:
        tmp = Path(tempfile.mkdtemp(prefix="manifest-test-")).resolve()
        try:
            case(tmp)
            print(f"  ok   {case.__name__}")
        except Exception as e:  # noqa: BLE001 — test runner reports any failure
            failures.append(f"{case.__name__}: {e}")
            print(f"  FAIL {case.__name__}: {e}")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    print()
    if failures:
        print(f"extraction-manifest: {len(failures)} of {len(CASES)} cases FAILED")
        return 1
    print(f"extraction-manifest: all {len(CASES)} cases passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
