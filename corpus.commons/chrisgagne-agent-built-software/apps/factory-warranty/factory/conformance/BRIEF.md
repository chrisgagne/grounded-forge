# Conformance matrix brief (shared by every matrix agent)

You are writing one part of a conformance matrix for **factory**, a harness that runs AI-built code changes through gates and blind AI review and hands an accountable human a warranty pack to sign. Repo: this repository (the factory's folder). Read `DESIGN.md` and `README.md` in full first, then the module docstrings in `factory/stages/*.py`, `factory/ledger.py`, `factory/isolation.py`, `factory/hooks/guard.py` and `factory/calibrate.py`. List the tests with `grep -n "^def test_" tests/*.py` and the calibration fixtures in `calibration/defects/*/expect.yaml`. Read code where a docstring doesn't settle what a mechanism does.

The reader is a risk owner who does not read code. The yardstick is the standard's own text, never your opinion of what is good enough.

## Three subjects (say which one each row is about)
- **process**: the factory as the producer's development process and tooling (who builds, how changes are checked, what is recorded).
- **product**: the software the factory builds for a client (requirements the built application itself must meet).
- **agent**: the factory itself as an LLM and agentic system (its model legs, tools, prompts and permissions).

## Columns
`| ID | Requirement (paraphrase, cited) | Subject | Factory mechanism | Evidence | Status | Note |`

- **ID**: the standard's own identifier (SSDF task ID like PO.1.1, ASVS 1.2.3, LLM01, ASI01, the CISA form's numbered item).
- **Requirement**: a short faithful paraphrase with its citation (section or page as the source prints it). Quote only the source's exact words and mark them with quotation marks.
- **Factory mechanism**: what in the factory addresses it, by name (stage, check, file). "None" if nothing.
- **Evidence**: concrete and verifiable: a ledger check name (e.g. `gate:secrets`), a test as `tests/file.py::test_name`, a calibration fixture folder, or "instruction only: factory/prompts/x.md". Grep to confirm each one exists before you write it. Never invent a test or check name.
- **Status**, exactly one of:
  - `demonstrated`: the mechanism runs on every change and records a ledger event, AND a test or calibration fixture shows it catching the bad case. Name both.
  - `asserted`: it exists only as an instruction (prompt, review focus, builder brief, doc), or a model's statement, or it runs but nothing shows it works.
  - `gap`: nothing in the factory addresses it.
  - `needs a third party`: by its nature it needs someone independent of the builder, or the operator's own organisation and environment (a pen test, an outside audit, the signer's company controls, a legal attestation).
  - `not applicable`: only with a reason grounded in the standard's own scope statement (cite it).
- **Note**: what would close a gap or raise the status, in one line. Mark any threshold or value you suggest that the standard does not supply as PROPOSED.

## Rules
- Cover every requirement in your assigned scope, one row each, in the standard's own order. Do not group or skip.
- Read every source text named in your dispatch in full (or the exact part your dispatch names). If you cannot, stop and say what you read; never present partial coverage as complete. Your file's header states exactly what you read.
- Be strict. When in doubt between two statuses, choose the lower one and say why in the note.
- Write your part to the file your dispatch names, starting with a header (standard, edition, what you read, date 2026-10-12, your model id), then a count of rows per status, then the table.
- Do not edit anything else. Your final message: the file path, the counts per status, and the five gaps you judge cheapest to close in code.
