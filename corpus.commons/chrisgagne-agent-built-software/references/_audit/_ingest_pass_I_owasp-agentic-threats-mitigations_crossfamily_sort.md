## 1. What I read

Read in full:

- `sort-brief.md`, `pass-i-spec.md` and all three calibration fixtures.
- `blind-findings.md` and `fixer-audit-log.md`.
- `post-audit-deep.md`, lines 1–520.
- `tape.md`, lines 1–1985.
- `source-card.md`, repository `CLAUDE.md` and its required architecture documents.

Compared `frozen-deep.md` with `post-audit-deep.md`: the only changes are at lines 17, 41 and 393. Also checked the protocol’s evidence-marker definitions: `[BT]` means the author cites someone else **for the claim**, rather than merely naming a product.

Inspected PDF metadata and rendered printed pages 6, 10 and 45 of the original: :codex-file-citation{path="_planning/pass-i/chrisgagne-agent-built-software/owasp-agentic-threats-mitigations/source.pdf" purpose="source"}

Independently verified that a fresh `pdftotext -layout` conversion reproduces `tape.md` byte for byte. The supplied post-audit checksum matches:

`63e0605ccafb2b66a2477d7acf9e26b624366ff10fc957756ee2b10d0fb60c23`

This is the sort leg, including independent verification of every raised finding and every fixer edit. It does not claim a fresh, separately enumerated claim-by-claim audit.

No files were changed. The workspace is read-only; this message is the complete report.

## 2. Sorted ledger

All deep-reference line numbers refer to `post-audit-deep.md`.

### Confirmed and fixed

| ID | Deep line | Raised by | Source anchor | Adjudication |
|---|---:|---|---|---|
| F2 | 41 | Fixer | Original PDF, printed p. 6, upper figure; the figure’s connectivity is absent from the tape | The dashed Memory connection branches to both Planning and Reflection. The original description omitted the Reflection branch from its account of dashed connections. The replacement accurately records both destinations. |
| F3 | 393 | Fixer | Tape 1574–1582, printed p. 41 | “Cut their network and system access” strengthened the source’s instruction to “restrict” access into complete withdrawal. Replacing “cut” with “restrict” restores the source’s scope. |

### Confirmed, fix wrong or incomplete

| ID | Deep line | Raised by | Source anchor | Adjudication |
|---|---:|---|---|---|
| B4 / fixer “Left open” | 520; target line 2 | Both | Internal artefact evidence: deep lines 1–3 and 520; no tape passage applies | The instruction to consult “the stamp on line 2” points to a blank line. The fixer explicitly recognised this defect but left it for the driver. The dispatch explains the deferral; it does not repair the supplied post-audit file. Strip the dangling status line. |

The status defect is **not** a blind-only miss: both auditors raised the same problem in the same claim.

### Missed by the fix-in-place audit

| ID | Deep line | Raised by | Source anchor | Adjudication |
|---|---:|---|---|---|
| B1 | 476 | Blind | Tape 178–183 and 231–234, printed pp. 6, 9; p. 6 render | The framework list and popularity description are the document’s own statements. The nearby referral to the OWASP Agentic AI Landscape does not attribute the popularity claim to that guide. `[BT]` should be `[AP]`. |
| B2 | 478 | Blind | Tape 283–285, printed p. 10; rendered patterns table | The table explicitly presents Codex with self-evaluation as its example of a Reflective Agent. It does not borrow the claim from a cited Codex publication. `[BT]` should be `[AE]`. |
| B3 | 490 | Blind | Tape 1714–1719, printed p. 45; p. 45 render | The camera-product statement is the authors’ introductory context for their hypothetical model. No third-party source is cited for it. `[BT]` should be `[AP]`, consistent with deep line 418. |

### Over-flagged

None conclusively established for either auditor. The contested thesis finding below is classified as disputed rather than forced into an over-flag count.

### Disputed

| ID | Deep line | Raised by | Source anchor | Adjudication |
|---|---:|---|---|---|
| F1 | 17 | Fixer | Tape 388–390, 455–469 and 482–485, printed pp. 13–15; additionally 153–156, p. 5; 853–866, p. 24; 1036–1042, p. 28 | Whether “persistence” was an unsupported addition is a genuine paraphrase judgement. Both readings are detailed below. |

**Reading supporting the fixer:** The cited pp. 13–15 expressly identify memory as an attack vector, reinforcement through memory as a hallucination amplifier, and multi-agency’s complexity and scale as exacerbating risks. The replacement follows those passages more closely. “Persistence” could otherwise be read as an additional, independently asserted mechanism.

**Reading supporting the original:** This is marked author argument, not verbatim quotation. The source defines persistent long-term memory, describes misinformation persisting and escalating through persistent memory and cross-session learning, and explicitly says long-lived, stateful agents capable of persistent action amplify supply-chain threats. “Persistence” therefore need not originate in the ingester’s domain priors. Its absence as that exact word from the cited introductory passage does not by itself establish leakage.

**Disposition:** Retain the fixer’s supported replacement. Do not count the original wording as a confirmed defect or require its restoration.

### Checks on introduced defects and other audit observations

**No new defect introduced by the fixer’s three edits was found.** The revised thesis traces to pp. 13–15; the revised figure description matches the original; and “restrict” matches the mitigation instruction.

The auditors’ “considered and retained” observations are not defect findings. Their supported contrasts at deep lines 494–496 should remain: the methodology contrast is explicit at tape 342–361, and the Navigator repeatedly distinguishes agentic extensions from existing LLM entries.

The fixer’s light-reference re-derivation note concerns a derived artefact outside the supplied deep reference. It is excluded from the ledger’s defect counts. Acquisition history and first-publication metadata remain provenance assertions whose historical accuracy cannot be independently established from the supplied PDF and tape; neither audit established a defect there.

## 3. Remaining edits

Apply these four changes to `post-audit-deep.md`. Line numbers refer to the unchanged supplied file.

1. **Line 476 — correct the framework marker.**

   Current:
   ```markdown
   - Agentic frameworks LangChain/LangFlow, AutoGen, CrewAI (Crew.AI on p. 9): named as popular frameworks [BT] (pp. 6, 9).
   ```

   Replacement:
   ```markdown
   - Agentic frameworks LangChain/LangFlow, AutoGen, CrewAI (Crew.AI on p. 9): named as popular frameworks [AP] (pp. 6, 9).
   ```

2. **Line 478 — correct the example marker.**

   Current:
   ```markdown
   - Codex with self-evaluation: example of the Reflective Agent pattern [BT] (p. 10).
   ```

   Replacement:
   ```markdown
   - Codex with self-evaluation: example of the Reflective Agent pattern [AE] (p. 10).
   ```

3. **Line 490 — correct the camera-context marker.**

   Current:
   ```markdown
   - Amazon Ring, Google Nest Cams, Eufy: commercial cameras with AI detection, context for the IoT example [BT] (p. 45).
   ```

   Replacement:
   ```markdown
   - Amazon Ring, Google Nest Cams, Eufy: commercial cameras with AI detection, context for the IoT example [AP] (p. 45).
   ```

4. **Line 520 — strip the dangling audit-status reference.**

   Current:
   ```markdown
   **Pass I: see the stamp on line 2 and the audit log.**
   ```

   Replacement: **strip**.

Edits 1–3 are verified against the cited source passages. Edit 4 is verified directly against the artefact; it makes no source-content claim.

## 4. Counts

Counts use unique defects, merging the shared status finding.

| Classification | Count |
|---|---:|
| Confirmed and fixed | 2 |
| Confirmed, fix wrong or incomplete | 1 |
| Missed by the fix-in-place audit | 3 |
| **Confirmed defects in total** | **6** |
| Over-flagged — fixer | 0 |
| Over-flagged — blind | 0 |
| Disputed | 1 |
| Defects introduced by fixer edits | 0 |

Four confirmed defects remain unresolved. The fixer captured the figure omission, access-restriction overstatement and dangling status reference. The blind auditor captured the three marker defects and the same status reference. The disputed persistence finding and observations about other files are excluded.

Capture: fixer=3 blind=4 both=1

## 5. Gate verdict once the remaining edits are applied

**Pass for the deep reference after all four remaining edits are applied.**

The confirmed defects will then be resolved, the supported fixer edits can remain, and no introduced defect was found. The disputed original thesis wording does not block passage because its current replacement is source-supported.

The supplied file is **not yet ready to pass**: the four edits remain unapplied. Audit stamping and derived-tier re-derivation/provenance checks remain the driver’s subsequent responsibilities; this report does not certify their completion.