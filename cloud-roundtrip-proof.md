# Codex Cloud CLI round-trip proof — Shortcut story 312

- **Request nonce:** `3e256efd-72e2-47a5-9ec8-22b8255522c8`
- **UTC run time:** `2026-09-25T12:58:30Z`
- **Checked-out Git commit:** `bea35fe714cb116afda580a339ee4c8cec97cefa`
- **Python version:** `3.12.13`

## Checked files

| Path | Present | Bytes | SHA-256 |
|---|---:|---:|---|
| `AGENTS.md` | yes | 4730 | `f0af3e10133c43940e77782339f342778de81af1b5fbbf2a6585ec5d3e4bb85f` |
| `CLAUDE.md` | yes | 16399 | `2c9b1acdb65240fb769cafbd70241e84d8e59822e804546f1909cb9ba30fdcbb` |
| `README.md` | yes | 46280 | `584d3c664556278408a3fbef444d80f783d52c4ffa3ab3d3cd57460b7783135b` |
| `package.json` | yes | 1923 | `9dab7bacc26a032d869eb48d6fa6df29573159d3fdb1e418e1f90df33803573b` |
| `.gitignore` | yes | 3407 | `1f8c907aa7854e9ad486a8e72818ba693806686c20b6a2ef1d944571a2d6910c` |

All requested files were present. Hashes and byte counts were computed from file bytes with Python's `hashlib.sha256`; none were estimated.

## npm scripts

I parsed `package.json` as JSON and found these script names: `build`, `build:decision`, `build:stakeholder`, `build:software-business`, `build:aar-mode`, `build:retro-mode`, `build:matrix`, `clean`, `list`, `test:lens-visibility`, `test:derived-provenance`, `package`, `package:all`, `create-corpus`, `remove-corpus`, `remove-corpus:openstax`, `setup-chroma`, `setup-chroma:check`, `setup-chroma:rebuild`, `audit-deep-refs`, `audit-deep-refs:local`, `audit-deep-refs:all`, `slug-table:demo`, `slug-table:demo:check`.

## Ignore check

I ran `git check-ignore --no-index corpus.local/cloud-proof-placeholder` without creating the placeholder. Exit code: `0`. Standard output: `corpus.local/cloud-proof-placeholder`. Standard error: `(empty)`.

## Validation and operational limit

After writing the artifacts, I ran:

```sh
python3 -c "import hashlib,json,pathlib; d=json.load(open('cloud-roundtrip-proof.json')); assert d['request_nonce']=='3e256efd-72e2-47a5-9ec8-22b8255522c8'; assert all((not x['present']) or (len(b:=pathlib.Path(x['path']).read_bytes())==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256']) for x in d['files']); print('PASS: JSON parsed; nonce and source hashes verified')"
```

Observed result: `PASS: JSON parsed; nonce and source hashes verified` (exit code 0).

This smoke test verifies execution against the public repository checkout, command execution in the cloud environment, and creation of returned artifacts. It does **not** verify or access private job-search data, perform external submissions, contact people, or establish recurring scheduling.

## Summary

Artifacts: `cloud-roundtrip-proof.md` and `cloud-roundtrip-proof.json`. Actual checks: checkout commit and Python version capture; deterministic source-file hashes and byte counts; npm-script enumeration; ignore-rule inspection; and parsed-JSON nonce/hash validation.
