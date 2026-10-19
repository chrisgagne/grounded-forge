
# Souppaya, Scarfone and Dodson, Secure Software Development Framework v1.1: Warranting Agent-Built Software Distillation

**Source:** Murugiah Souppaya, Karen Scarfone and Donna Dodson (2022), *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of Software Vulnerabilities*, NIST Special Publication 800-218, February 2022, https://doi.org/10.6028/NIST.SP.800-218. United States public domain; reprint and derivative-work permission under NIST Technical Series Publications policy. Scope: open. Cited as (SSDF, section or Table 1 task ID, printed page).

**Applicability gate (Pass G.0): clear yes.** All three gate questions land. (1) The framework asks the axis's own questions in its own terms: what the security requirements are and where they are written (PO.1), what evidence shows a practice was performed (PO.3.3), what criteria a security check uses and who recorded the exceptions (PO.4), what the build environment can reach (PO.5), who changed which code (PS.1), and what happens after a vulnerability ships (RV). (2) Its four groups land in all eight phases, most heavily in Phases 2, 4, 5 and 8. (3) Its one explicit contrarian position (the practices are a risk-based basis for planning, not a checklist or a sequence) is the axis's stance against rote gating, and shapes how a warranty pack should cite it. The framework predates coding agents and says nothing about AI. Every application of a practice to an agent (the agent as a toolchain component, an agent session as a development environment, an agent's commit as a change to protected code) is this distillation's transfer, marked *by transfer* where it carries weight.

**Phase mapping.** Phase 1, Specifying: software security requirements written and maintained; terms the adopter defines. Phase 2, Triaging risk: risk modelling concentrated on high-risk areas; data classification; earlier vulnerability reports; recorded risk responses and exception rationales. Phase 3, Locking the tests: security-feature and regression tests; criteria and records protected from alteration (by transfer). Phase 4, Building in the sandbox: separated, protected, enumerated environments; hardened, dedicated endpoints; least privilege; third-party components and provenance; account-attributed changes. Phase 5, Gating deterministically: toolchain artefacts as evidence; criteria for security checks; recorded exceptions; warnings as errors; build-tool integrity; secure defaults under change control. Phase 6, Reviewing independently: design review by people not involved and/or automation; review type chosen by policy; findings recorded and triaged; history of earlier vulnerabilities. Phase 7, Warranting: artefacts as evidence; named owners and an accountable leader; shared responsibility with providers; release integrity and provenance; the selection, not a checklist. Phase 8, Releasing and operating: gathering and confirming vulnerability reports; risk-based response; root cause, pattern analysis, class sweeps and process change; disclosure programme.

**Trigger match:** 25 of the 41 seed triggers addressed, in all eight phases; 15 trigger extensions logged. No trigger-mismatch flag.

## Warranting Agent-Built Software Relevance

The SSDF is a common vocabulary of secure-development outcomes, organised in four groups: prepare the organisation (PO), protect the software (PS), produce well-secured software (PW), and respond to vulnerabilities (RV) [AP] (SSDF, §2, p. 4). For the accountable builder it does two jobs. First, it is a ready-made list of what a harness around coding agents should be able to *show*: requirements written down, tools configured to leave artefacts that record what was done, criteria for each security check, exceptions recorded and reviewed, environments separated so a build session cannot reach production, every change attributed to an account, components checked and their provenance kept, findings recorded and triaged, and root causes fed back into the process [AP] [AE] (SSDF, Table 1, pp. 5–19). Its toolchain practice says outright that automation should also document that practices were performed, and that someone is assigned to produce the evidence tools cannot [AP] [AE] (SSDF, Table 1, PO.3, PO.3.3, pp. 7–8). That is the demonstrated-versus-asserted ledger in a federal standard's words.

Second, the framework speaks to outcomes, not mechanisms: "The focus is on the outcomes of the practices rather than on the tools, techniques, and mechanisms to do so." [V] (SSDF, Executive Summary, p. vi). It does not ask that a human read every line; code review is human review and/or tool-based analysis chosen by policy and the software's stage [AP] (SSDF, Table 1, PW.7.1, p. 14). So it neither forbids agent-built software nor excuses it: an agent-built change meets the framework when the harness produces the outcomes and the records. Its limits matter as much. It recommends practices; it states no measured reduction in vulnerabilities from adopting them. Its examples are notional, and none is required [AP] (SSDF, §2, p. 4). It predates coding agents, so it names none of the agent-specific risks (prompt injection, tool misuse, an agent editing its own tests); those come from other sources in this corpus.

## Key Concepts for Warranting Agent-Built Software

1.  **Outcomes, selected by risk, not a checklist.** "The intention of the SSDF is not to create a checklist to follow, but to provide a basis for planning and implementing a risk-based approach to adopting secure software development practices." [V] (SSDF, §1, p. 3). Implementation is tailored by risk, cost, feasibility, applicability and automatability; the table's order implies no priority or sequence; no example or combination of examples is required; some practices are foundational and others depend on them [AR] [AP] (SSDF, Executive Summary, p. vi; §1, pp. 2–3; §2, p. 4). For the warranty pack, an SSDF claim is a *selection with reasons*, not a tick against every task.

2.  **Written security requirements, in the builder's own defined terms.** Requirements for development infrastructure and processes, and the software's own security requirements, are identified, documented, maintained and reviewed at least annually or after relevant changes or incidents [AP] [AE] (SSDF, Table 1, PO.1.1–PO.1.2, p. 5). The framework leaves terms such as *sensitive data*, *qualified person* and *well-secured* to the adopter, and asks the adopter to name its environments (development, build, test, production and so on) [AP] (SSDF, §2, p. 4). An agent's spec can only be checked against requirements that exist on paper.

3.  **Toolchain artefacts are the evidence.** Automation is meant to reduce human effort, improve reproducibility and comprehensiveness, *and* document that practices were performed [AP] (SSDF, Table 1, PO.3, p. 7). Tools are configured to generate artefacts showing the organisation's practices are followed, with audit trails, retention policies, and an assigned person for evidence tools cannot generate [AP] [AE] (SSDF, Table 1, PO.3.3, pp. 7–8). The framework adapts its definition of an artefact as a piece of evidence [BT] (SSDF, Table 1, footnote 6, p. 7). An agent's report is not an artefact in this sense; a tool's run record is.

4.  **Criteria set in advance, decisions recorded, records protected.** Security-check criteria are defined and tracked across the life cycle, including security in the Definition of Done, with approvals, rejections and exception requests recorded; the supporting information is gathered automatically where possible and safeguarded by restricting access and preventing alteration or deletion [AP] [AE] (SSDF, Table 1, PO.4.1–PO.4.2, p. 8). Approved exceptions are reviewed periodically [AE] (SSDF, Table 1, PO.1.2, p. 5).

5.  **Separated, protected, enumerated environments.** Development environments are separated and protected: segmentation, restricted ingress and egress, minimised direct human access to toolchains, minimised use of production software and services from non-production environments, audited trust relationships and privilege use [AP] [AE] (SSDF, Table 1, PO.5.1, pp. 8–9). Endpoints are hardened with least functionality and least privilege, and dedicated to development, apart from endpoints used for other tasks [AE] (SSDF, Table 1, PO.5.2, p. 9). Enumerating environments is necessary to secure them, especially against an attacker's lateral movement between them [AP] (SSDF, §2, p. 4). By transfer, an agent's session is a development environment, and its reach is what this practice limits.

6.  **Every change attributed; others' code needs its owner.** All forms of code (source, executable, configuration as code) are stored under least privilege to prevent accidental or intentional unauthorised changes; examples include version history attributed to accounts, commit signing, and code owners reviewing and approving all changes others make to their code [AP] [AE] (SSDF, Table 1, PS.1–PS.1.1, p. 9). Naming code owners appears again under roles [AE] (SSDF, Table 1, PO.2.1, p. 6).

7.  **Third-party components vetted for their use and through their life.** Components are reviewed in the context of their expected use, with provenance analysed and approved versions maintained, and verified against requirements throughout their life cycles: known vulnerabilities checked automatically, ongoing maintenance confirmed, end-of-life planned [AP] [AE] (SSDF, Table 1, PW.4.1, PW.4.4, pp. 12–13). Reuse of well-secured components is argued to lower cost and reduce newly introduced vulnerabilities, especially for security functions such as cryptography [AR] (SSDF, Table 1, PW.4, p. 12).

8.  **Release integrity and provenance the acquirer can check.** Integrity-verification information (hashes, signatures) is made available to acquirers; each release is archived with its integrity and provenance data; provenance for every component (for example, in an SBOM) is kept, shared by policy and updated whenever components change [AP] [AE] (SSDF, Table 1, PS.2.1, PS.3.1–PS.3.2, p. 10). Provenance is defined, by borrowing, as the chronology of a component's origin, development, ownership, location and changes, possibly including the people and processes that modify it [BT] (SSDF, Table 1, footnote 5, p. 6).

9.  **Risk modelled where it matters, and every response recorded.** Risk modelling (threat modelling, attack modelling, attack-surface mapping) is concentrated on high-risk areas, uses earlier vulnerability reports and classifies data [AP] [AE] (SSDF, Table 1, PW.1.1, p. 11). Risk responses, mitigation plans and exception rationales are recorded, carried into requirements, retained for audit and maintenance, and periodically reconsidered [AP] [AE] (SSDF, Table 1, PW.1.2, p. 11).

10.  **Review by someone not involved, and/or by the toolchain, chosen by policy.** The design is reviewed by qualified people who were not involved with it and/or by automated processes in the toolchain [AP] (SSDF, Table 1, PW.2.1, p. 12). Code is reviewed by people and/or analysed by tools according to policy and the software's stage, and findings and remediation recommendations are recorded and triaged in the team's workflow; examples include static analysis with human handling of its findings, and experts looking for backdoors [AP] [AE] (SSDF, Table 1, PW.7.1–PW.7.2, pp. 14–15). A developer reviewing their own code is listed as a complement to other people and tools, not a replacement [AE] (SSDF, Table 1, PW.5.1, p. 13).

11.  **Warnings as errors; build tools under change control.** Build configuration enables warnings and treats them as errors, except for identified false positives or irrelevant warnings; approved settings are continuously verified; compilers, interpreters and build tools are kept current, put under change management, audited for unexpected changes, and validated for authenticity and integrity [AE] (SSDF, Table 1, PW.6.1–PW.6.2, p. 14). Secure defaults are documented and kept under change control [AE] (SSDF, Table 1, PW.9.1–PW.9.2, p. 16).

12.  **Root cause, the class, then the process.** Vulnerability reports are gathered and investigated on an ongoing basis, risk is calculated from exploitability and impact, and responses (remediate, accept, transfer, temporary mitigation) are planned and recorded [AP] [AE] (SSDF, Table 1, RV.1.1–RV.2.2, pp. 16–18). Root causes are identified, analysed over time for patterns, whole classes of similar vulnerabilities are proactively found and fixed rather than waiting for outside reports, and the development process is reviewed and updated if appropriate to prevent recurrence [AP] [AE] (SSDF, Table 1, RV.3.1–RV.3.4, pp. 18–19).

## Questions to Ask During Warranting Agent-Built Software

### Phase 1: Specifying the change

| Need | Question | Source-tag |
|---|---|---|
| Written security requirements | Which of our written security requirements does this change have to meet, and is the list current (reviewed in the last year, or since the last relevant incident)? | PO.1.1–PO.1.2 |
| Defined terms | Have we defined, for this client, what counts as sensitive data, a qualified reviewer and well-secured, so the agent and the reviewer use the same meaning? | §2, p. 4 |
| Security in done | Is security part of this change's Definition of Done, as a criterion a check can apply, not a note in the agent's prompt? | PO.4.1 |
| Defaults that must not weaken | Does the spec say which secure default settings the change must leave as they are? | PW.9.1 |

### Phase 2: Triaging risk

| Need | Question | Source-tag |
|---|---|---|
| Selection with reasons | Which SSDF tasks apply to this kind of change, and why, by live task ID (not a retired one such as PW.3 or PW.4.3)? | §1, p. 3; Table 1, pp. 12–13 |
| High-risk areas | Does the change touch an area where rigorous risk modelling should be concentrated (authentication, authorisation, data handling)? | PW.1.1 |
| Data classification | What class of data does the change store or move, by our own definition of sensitive data? | PW.1.1; §2 |
| History | Have we read earlier vulnerability reports and root-cause notes for the code this change touches? | PW.1.1; RV.3.1 |
| Recorded response | For each risk we found, is there a recorded response: a mitigation, an exception with its rationale, an acceptance or a transfer? | PW.1.2; RV.2.2 |
| Standard services | Is the agent writing its own version of a security function (crypto, authentication) where a standard, well-secured one exists? | PW.1.3; PW.4 |

### Phase 3: Locking the tests

| Need | Question | Source-tag |
|---|---|---|
| Security tests chosen | Which test types does this change need: functional tests of its security features, regression tests for earlier vulnerabilities, fuzzing, or penetration testing for a high-risk scenario? | PW.8.1–PW.8.2 |
| Tests run on every change | Do the automated vulnerability tests run on every change and for every supported release, or only on request? | PW.8.2; RV.1.2 |
| Criteria out of reach | By transfer: can the agent session that is judged by a check also edit the check, its threshold or its record? | PO.4.2; PS.1.1 |

### Phase 4: Building in the sandbox

| Need | Question | Source-tag |
|---|---|---|
| Reach | From the agent's environment, what production software, services, data or credentials can be reached, and could that reach be removed? | PO.5.1 |
| Lateral movement | Have we named every environment (development, build, test, production) and the paths between them, so we know where an agent could move? | §2, p. 4; PO.5.1 |
| Dedicated endpoint | Does the agent run on a hardened endpoint used only for development, with least privilege and least functionality? | PO.5.2 |
| Tool assessment | By transfer: was the agent, and each tool or plugin it uses, assessed and deployed as a toolchain component, with its configuration as code and its logs monitored? | PO.3.2 |
| Attribution | Is every agent commit attributed to an account that identifies it, and does a change to code someone else owns wait for that owner's approval? | PS.1.1 |
| New components | For each dependency the agent added: was it reviewed for this use, is its provenance known, is it maintained, does it have known vulnerabilities, and is it an approved version? | PW.4.1; PW.4.4 |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| Artefacts, not narrative | For each gate, which tool produced the record, where is it retained, and who is assigned to provide evidence the tools cannot? | PO.3.3 |
| Criteria set before | Were the gate's criteria defined before this change, and is any skip recorded as an exception request with its approval or rejection? | PO.4.1 |
| Records protected | Can the record of a gate's result be altered or deleted by the session it judged? | PO.4.2 |
| Warnings | Are warnings treated as errors, and is every suppression an identified false positive with a reason? | PW.6.2 |
| Build tools | Did a compiler, interpreter, build image or CI action change version, and was the change expected, audited and validated? | PW.6.1 |
| Same artefact | Can we show the integrity and provenance of the artefact that ships, and that it is the one the gates judged? | PO.3.2; PS.1.1; PS.3.1 |
| Defaults | Did the change weaken a secure default, and did that go through change control? | PW.9.1–PW.9.2 |

### Phase 6: Reviewing independently

| Need | Question | Source-tag |
|---|---|---|
| Not involved | Was the design reviewed by a qualified person not involved in it, or by an automated process in the toolchain, and did the review confirm each security requirement? | PW.2.1 |
| Review by policy | What does our policy say this kind of change at this stage needs: human review, tool-based analysis, or both? | PW.7.1 |
| Findings triaged | Are the review's and the tests' findings recorded and triaged in the workflow, each with a remediation recommendation or a reason it was dismissed? | PW.7.2; PW.8.2 |
| Self-review as complement | Is the agent's own review of its code counted only as a complement to other reviewers and tools? | PW.5.1 |
| Lessons searched | Did the reviewer search the recorded root causes and lessons for this area? | PW.7.2; RV.3.1 |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Evidence in the pack | Does each claim in the pack point to an artefact the toolchain generated, or a named person's recorded evidence? | PO.3.3; PW.8.2 |
| Owners | Who owns each selected task, inside the harness and among the providers (agent platform, model provider, hosting), and how does each provider attest to its share? | §1, p. 3; PO.1.3 |
| Accountable leader | Who is accountable for the whole secure-development process, including the release decision? | PO.2.3 |
| Design records | Are the design decisions and risk records for this change retained where a maintainer can find them after the agent session ends? | PW.1.2 |
| Integrity for the client | Can the client verify this release's integrity (hashes, signatures), and is the release archived with its provenance? | PS.2.1; PS.3.1–PS.3.2 |
| The claim's form | If the pack cites the SSDF, does it show the tasks selected and the reasons, rather than claim the framework as a checklist? | §1, p. 3; §2, p. 4 |

### Phase 8: Releasing and operating

| Need | Question | Source-tag |
|---|---|---|
| Reports in | Where do vulnerability reports from the client, users and public sources arrive, and who investigates them? | RV.1.1; RV.1.3 |
| Continuous checking | Are automated analysis and testing running regularly for every supported release, not only the latest? | RV.1.2 |
| Risk response | For a confirmed vulnerability: what are its exploitability and impact, and what is the response (fix, temporary mitigation, acceptance, transfer, advisory)? | RV.2.1–RV.2.2 |
| Root cause and class | What is the root cause, where else does the same class occur, and what toolchain detection or process change stops it recurring? | RV.3.1–RV.3.4 |
| Components ageing | Which production components have lost maintenance or are near end of life? | PW.4.4 |
| Playbook exercised | Has the response playbook been exercised? | RV.1.3 |

## What to Look For

**The pack cites the framework as a checklist.**
- *Signal:* The warranty pack says *SSDF compliant* with no list of selected tasks, no reasons, or a list of every task ticked.
- *Diagnosis:* The framework rejects the checklist reading; it is a basis for a risk-based approach, and its examples are neither required nor exhaustive [AP] (SSDF, §1, p. 3; §2, p. 4).
- *Follow-up:* Return it for the selection record: live task IDs, why each applies, how each was implemented, what was not done and why.

**The only record of a gate is the agent's summary.**
- *Signal:* The ledger says *scan clean* or *tests passed* and links to nothing a tool produced.
- *Diagnosis:* The toolchain practice exists partly to document that practices were performed, through artefacts the tools generate [AP] (SSDF, Table 1, PO.3, PO.3.3, pp. 7–8). A summary is not an artefact.
- *Follow-up:* Configure the gate to emit and retain its run record; assign a person for any evidence a tool cannot produce.

**The gate moved inside the change it judged.**
- *Signal:* The diff edits a check's criteria, a threshold, a suppression list or a test the agent was asked to pass, or the session can write to the gate log.
- *Diagnosis:* By transfer: criteria are defined and tracked, and the supporting information is safeguarded by restricting access and preventing alteration or deletion [AP] [AE] (SSDF, Table 1, PO.4.1–PO.4.2, p. 8).
- *Follow-up:* Hold the change; move criteria and logs out of the agent's write access; any criterion change goes through its owner as a separate, recorded decision.

**The build session can reach production.**
- *Signal:* Production credentials, data or services are reachable from where the agent runs, or the agent runs on a machine used for other work.
- *Diagnosis:* The framework asks for minimised use of production software and services from non-production environments, restricted ingress and egress, and dedicated development endpoints [AE] (SSDF, Table 1, PO.5.1–PO.5.2, pp. 8–9).
- *Follow-up:* Remove the reach, not the instruction. Name the environments and the paths between them.

**An unrequested dependency.**
- *Signal:* The lockfile grew and nobody asked for the new package.
- *Diagnosis:* Components are reviewed in the context of their expected use, their provenance analysed and their maintenance confirmed [AE] (SSDF, Table 1, PW.4.1, PW.4.4, pp. 12–13).
- *Follow-up:* Check provenance, maintenance and known vulnerabilities; prefer an approved version or a well-secured component already in use; update the SBOM.

**Silenced warnings.**
- *Signal:* New suppression comments or lowered warning levels in the diff.
- *Diagnosis:* Warnings are treated as errors except for identified false positives [AE] (SSDF, Table 1, PW.6.2, p. 14); static-analysis findings get human handling [AE] (SSDF, Table 1, PW.7.2, p. 15).
- *Follow-up:* Each suppression carries an identified-false-positive reason, reviewed; otherwise fix it.

**A skip with no record.**
- *Signal:* A gate did not run on this change and nothing on the ledger says so.
- *Diagnosis:* Exception requests are recorded, and approved exceptions reviewed periodically [AE] (SSDF, Table 1, PO.4.1, p. 8; PO.1.2, p. 5).
- *Follow-up:* Record it as an exception with its rationale and approver, and show it on the pack.

**The same bug, again.**
- *Signal:* A vulnerability type fixed before turns up in a new change.
- *Diagnosis:* The instance was fixed but not the class or the process; the framework asks for pattern analysis over time, class sweeps and process changes [AP] [AE] (SSDF, Table 1, RV.3.2–RV.3.4, pp. 18–19).
- *Follow-up:* Add an automated detection to the toolchain, sweep for the class, and change the practice that let it in.

## When to Use This Reference

- Reach for it when the question is *what should the harness be able to show?* It is the corpus's broadest catalogue of secure-development outcomes, and the base the corpus's attestation form and AI profile build on.
- Reach for it to structure a warranty pack's security section: requirements, environments, components, review, testing, release integrity and response, by task ID.
- Reach for it after release: its RV group is the corpus's practice frame for handling reports, prioritising by risk and closing the loop through root cause and process change.
- Reach for another source for anything agent-specific. The framework names no agent or AI risk: use `owasp-agentic-top10-2026`, `owasp-agentic-threats-mitigations` and `owasp-llm-top10-2026` for the threats, `openssf-finding-fixing-vulnerabilities-ai` for running the practices with AI, and `nist-sp-800-218a` for AI model development.
- Reach for another source for the requirement list itself (`owasp-asvs-5-0`), for test strength (`egashira-testsuitebench-2026`), and for review mechanics (`microsoft-code-with-engineering-playbook`).
- Read its examples as notional. The framework requires none of them, and its frequencies are illustrative [AP] (SSDF, §1, p. 3; §2, p. 4).

## Worked Example

A two-person studio uses coding agents to build a customer portal for a small insurer. The client's procurement team asks whether the studio follows the SSDF. The next change adds document upload to the claims form.

**Phase 2: what applies, and why.** The builder resists answering *yes, we follow it*. The framework's own words rule that reading out: "The intention of the SSDF is not to create a checklist to follow, but to provide a basis for planning and implementing a risk-based approach to adopting secure software development practices." [V] (SSDF, §1, p. 3). So the pack will carry a selection. Upload handling is a high-risk area for rigorous risk modelling, and claim documents are sensitive data by the studio's written definition [AE] (SSDF, Table 1, PW.1.1, p. 11; §2, p. 4). The studio's root-cause notes record an earlier path-traversal fix in the storage module, so the risk model reads that report [AE] (SSDF, Table 1, PW.1.1, p. 11).

**Phase 4: where the agent ran, and what it added.** The session log shows the agent added an image-processing library nobody asked for. The builder checks it as the framework asks of any third-party component: reviewed for this use, provenance analysed, maintenance confirmed, known vulnerabilities checked [AE] (SSDF, Table 1, PW.4.1, PW.4.4, pp. 12–13). It is maintained, but a standard library already in the stack does the same job, so the agent is told to use that. The agent's environment held a read-only production database URL from an earlier debugging session; it comes out, because the framework asks for minimised use of production services from non-production environments [AE] (SSDF, Table 1, PO.5.1, pp. 8–9).

**Phase 5: what the gates show.** The diff includes a new suppression for a static-analysis warning about unchecked file size. The framework's examples treat warnings as errors except for identified false positives, and give static-analysis findings human handling [AE] (SSDF, Table 1, PW.6.2, p. 14; PW.7.2, p. 15). This one is not a false positive; it is a real gap, and the fix adds a size limit. The malware scan on uploads was skipped because its container failed to start. It goes on the ledger as an exception request with a rationale, not as a pass [AE] (SSDF, Table 1, PO.4.1, p. 8).

**Phase 6: who reviewed.** A reviewer agent in a fresh session, which did not design the change, acts as an automated review process in the toolchain (by transfer) and checks the design against the written requirements, and its findings go into the tracker with a triage decision each [AP] [AE] (SSDF, Table 1, PW.2.1, p. 12; PW.7.2, pp. 14–15). The studio's policy for this risk class adds a human pass over the upload path; the framework leaves that choice to policy [AP] (SSDF, Table 1, PW.7.1, p. 14).

**Phase 7: the pack.** Each claim points to a tool's run record, the framework's sense of an artefact [AP] (SSDF, Table 1, PO.3.3, pp. 7–8). The pack lists the selected tasks by ID, the skipped scan (rerun and clean before release), the provider split (the hosting provider owns its platform's patching; the studio owns the rest), and the release hashes the insurer can check [AP] [AE] (SSDF, §1, p. 3; Table 1, PS.2.1, p. 10). The builder's answer to procurement is the selection, not the slogan, and it rests on the framework's outcome-first framing:

> "The focus is on the outcomes of the practices rather than on the tools, techniques, and mechanisms to do so."
> (SSDF, Executive Summary, p. vi) [V]

Agents wrote the code; the outcomes and their records are what the studio warrants.

**Phase 8: after release.** Three weeks later a user reports that a renamed file bypasses the type check. The response follows the RV group: record it, rate it by exploitability and impact, ship a temporary mitigation, then find the root cause (type checked by extension, not content), sweep the other upload paths for the same class, and add an automated detection to the toolchain [AP] [AE] (SSDF, Table 1, RV.2.1–RV.2.2, pp. 17–18; RV.3.1–RV.3.4, pp. 18–19).

## Anti-patterns This Reference Helps Avoid

- **Compliance by slogan.** *Signal:* "SSDF compliant" with no task list. *Why it fails:* the framework is not a checklist and requires no particular example (SSDF, §1, p. 3; §2, p. 4), so the claim says nothing checkable. *Counter:* a selection record by live task ID, with reasons and gaps.
- **Narrative as evidence.** *Signal:* the gate's result is a sentence in the agent's report. *Why it fails:* the framework's evidence is artefacts the toolchain generates, with a named person for what tools cannot show (SSDF, Table 1, PO.3.3, pp. 7–8). *Counter:* every gate emits and retains its record.
- **The agent as everyone.** *Signal:* one session designs, writes, reviews and approves, under a person's account. *Why it fails:* design review is by people not involved and/or the toolchain, self-review is only a complement, and changes are attributed to accounts with owners approving others' changes (SSDF, Table 1, PW.2.1, p. 12; PW.5.1, p. 13; PS.1.1, p. 9). *Counter:* a distinct identity for each agent, a reviewer outside the writing session, and an owner's approval where the code is someone else's.
- **Reach by convenience.** *Signal:* the build environment can see production "for debugging". *Why it fails:* environment separation and minimised production use from non-production are the framework's first environment practice (SSDF, Table 1, PO.5.1, pp. 8–9). *Counter:* remove the reach and name the environments.
- **Unvetted components.** *Signal:* dependencies arrive in agent diffs without review. *Why it fails:* components are vetted for their expected use and through their life cycles (SSDF, Table 1, PW.4.1, PW.4.4, pp. 12–13). *Counter:* a component gate and an updated SBOM on every change that alters components.
- **Silent exceptions.** *Signal:* a skipped gate leaves no trace. *Why it fails:* exception requests are recorded and approved exceptions reviewed (SSDF, Table 1, PO.4.1, p. 8; PO.1.2, p. 5). *Counter:* skips show on the pack with a rationale and an approver.
- **Fixing the instance.** *Signal:* a patch for the reported input only. *Why it fails:* the RV group asks for the class and the process, not only the instance (SSDF, Table 1, RV.3.3–RV.3.4, pp. 18–19). *Counter:* root cause, class sweep, toolchain detection, process change.

## Integration with Other References

| Reference | Relationship |
|---|---|
| `nist-sp-800-218a` | Extension. The Profile augments SSDF 1.1 for AI model development and says it should not be used without SP 800-218; it is the corpus's route from these practices to AI-specific risks. It shares the framing as a risk-based starting point, not a checklist, and does not treat AI-generated code differently: all source code is to be evaluated before use. It departs on priority (see the index rows' named disagreements). |
| `cisa-secure-software-attestation-form` | Downstream use. The form's four attested practices derive from the SSDF, and its appendix maps them to SSDF tasks by code (for example, secure environments to PO.5.1 and PO.5.2). A producer attests that it *presently makes consistent use* of the practices and must notify agencies if it stops. The SSDF selection and its artefacts are what such an attestation would stand on. |
| `owasp-asvs-5-0` | The written list. The SSDF asks for software security requirements to be identified and documented (PO.1.2); ASVS supplies a verifiable requirement list at three levels. The SSDF's 2022 bibliography maps to ASVS 4.0.3 [BT]; the corpus holds 5.0, so use it directly. On automated tooling the two differ (see the named disagreements). |
| `openssf-finding-fixing-vulnerabilities-ai` | Same life cycle, different grain. The SSDF's RV practices (gather and investigate reports, prioritise by risk, analyse root causes and patterns, sweep the class) are the practice frame; the OpenSSF guide is the AI-era procedure for running them at volume, and adds what the SSDF predates: gates outside the AI, agents as distinct principals, findings as claims until validated. |
| `owasp-agentic-top10-2026` | Agent-specific detail for PO.5. The SSDF's environment separation and least privilege become, for agents, no keys held by agents and no direct agent-to-production paths; its third-party component practice meets the list's runtime agentic supply chain (models, tools, plug-ins, MCP interfaces composed at run time). |
| `owasp-agentic-threats-mitigations` | Threat behind PO.5's privilege examples. Its privilege-compromise threat (agents inheriting permissions) is why auditing trust relationships and privilege use matters more when the developer is an agent. |
| `owasp-llm-top10-2026` | Sharpens PS.2 and PW.4. The LLM list's supply-chain entry names slopsquatting of hallucinated package names, an agent-specific route for the unrequested dependency, and holds that signing proves integrity and origin, not safety, so release-integrity checks are combined with release gates and behavioural evaluation. |
| `microsoft-code-with-engineering-playbook` | Mechanics for PW.7 and PW.8, with one difference. The playbook's branch policies, small pull requests, and a full regression plan that includes every previously fixed bug give concrete form to recorded review and regression tests for earlier vulnerabilities. It asks reviewers to read every changed line; the SSDF leaves human versus tool review to policy (see the named disagreements). |
| `uk-duck-book-qa-of-code` | Agreement on outcome-based trust. The Duck Book's position that a manager need not read the code to trust it, given an appropriate team approach and proportionate assurance, parallels the SSDF's outcome focus and policy-chosen review. Its golden rule that the person who generated LLM code is responsible for it fills the gap the SSDF leaves on AI. |
| `uk-aqua-book-2025` | Agreement on proportion, difference on independence. Assurance proportionate to risk and complexity matches the SSDF's risk-based tailoring. The Aqua Book requires the assurer and the analyst to be independent; the SSDF's design review allows uninvolved people *and/or* automated processes. |
| `he-cursor-velocity-complexity-2025` | Evidence the SSDF's warnings practice addresses a real drift. In projects adopting an agentic coding tool, static-analysis warnings and complexity rose and stayed. PW.6.2 (warnings as errors) and PW.7.2 (static-analysis findings handled by humans) are the framework's counter for the warnings half; it says nothing on complexity. |
| `egashira-testsuitebench-2026` | Fills a gap in PW.8. The SSDF asks for tests to be scoped, designed, run and documented, but gives no way to judge whether a suite is strong; TestSuiteBench measures agent-written suites against seeded faults, one requirement at a time. |
| `jimenez-swe-bench` | Shared logic for evidence. SWE-bench judges an agent's change by tests run against it, not by the agent's account; that is the SSDF's artefact-as-evidence stance applied to correctness. |
| `dora-ai-assisted-swdev-2025` | Outcome measure the SSDF lacks. The framework offers no measure of results; DORA's finding that higher AI adoption goes with higher instability as well as throughput gives a delivery-stability signal to watch alongside the RV practices. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The framework draws its practices from existing standards and maps each task to them; it does not introduce new practices [AR] (SSDF, Abstract, p. ii; §1, p. 1). The mapped secure-development guidance in Table 1 and the References, the NIST publications that supply its definitions of provenance, artefact and evidence, and the getting-started works in footnote 4 are cited by the source and were not read for this corpus; definitions borrowed from them are marked `[BT]`. Of its OWASP mappings, only ASVS is in this corpus, and in a later edition (5.0, against the source's 4.0.3); the integration table points to the corpus edition independently. The executive order context in Appendix A is the source's own account [AP] [BT].

**Named limits of the source.** (1) It is a framework of recommendations and notional examples; it states no measured effect of adopting the practices. Its recommendations are assertions [AP], its examples illustrations [AE], and no example is required. (2) It predates coding agents and names no AI-specific risk; every application here to an agent is this distillation's transfer, marked *by transfer* where it carries weight. Its AI companion is `nist-sp-800-218a`, for model development. (3) It does not define sensitive data, qualified person, well-secured or the environment names; it leaves them to the adopter (SSDF, §2, p. 4). (4) It names future work on DevOps and other methodologies, transition from current practice, and open-source use; it does not settle those (SSDF, §1, p. 1). (5) Several identifiers are retired or moved (PW.3, PW.4.3, PW.4.5, PW.5.2); its Table 1 and change log describe the PW.4.5 move differently, and the deep reference keeps both (SSDF, Table 1, pp. 12–13; Appendix C, p. 27). Cite live task IDs only.

**Evidence-marker continuity.** The two `[V]` quotations (Executive Summary, p. vi; §1, p. 3) are copied from the deep reference's audited passages; they are the only verbatim passages the deep reference carries, so everything else is paraphrase with the deep reference's markers: `[AP]` for the framework's practices and tasks, `[AE]` for its notional examples, `[AR]` for its arguments (shift-left, reuse), `[BT]` for borrowed definitions and mappings. Phrases such as *presently makes consistent use* in the integration table are paraphrase in italics, not quotation. Italic phrases in What to Look For, the Worked Example and the Anti-patterns are this distillation's wording. The worked example's studio, insurer and change are invented; each framework claim within it is cited to a task.

## Runtime triggers this source addresses

### Phase 1: Specifying the change

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The story's acceptance criteria are prose ("works well", "handles errors") with no runnable check | Security half only: software security requirements are identified and documented, and security goes into the Definition of Done as a tracked criterion (SSDF, Table 1, PO.1.2, p. 5; PO.4.1, p. 8) | Name which written security requirements this change must meet and put them in done as checks. Functional criteria need another source. |
| The agent is asked to "build X like Y" with no statement of what must not change | Security requirements maintained and carried into the design record; a secure default baseline that the change must not weaken (SSDF, Table 1, PO.1.2, p. 5; PW.1.2, p. 11; PW.9.1, p. 16) | Write down which security requirements and secure defaults must survive the change. *Like Y* is not a requirement. |

### Phase 2: Triaging risk

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The diff touches login, sessions, tokens or permissions | Rigorous risk modelling concentrated on high-risk areas; standard security services rather than proprietary ones; functional tests of security features (SSDF, Table 1, PW.1.1, PW.1.3, p. 11; PW.8.2, p. 15) | This is a high-risk area: model the risk, use the standard auth service rather than an agent-written one, and test the security feature itself. |
| The change stores or moves personal data | Data classified as part of risk modelling; sensitive data defined by the adopter (SSDF, Table 1, PW.1.1, p. 11; §2, p. 4) | Classify the data by our written definition first; the class decides which requirements and tests apply. |
| The change is business-critical, or complex enough that nobody can predict its effects | Tailoring by risk; rigorous assessment for high-risk areas; penetration testing for high-risk scenarios if resources permit (SSDF, §1, p. 3; Table 1, PW.1.1, p. 11; PW.8.2, p. 15) | Scale the practices to the risk: more modelling and stronger testing here, recorded as a choice. |

### Phase 3: Locking the tests

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The agent proposes changing a test so the build goes green | By transfer: criteria defined and tracked, supporting records protected from alteration; code owners approve others' changes (SSDF, Table 1, PO.4.1–PO.4.2, p. 8; PS.1.1, p. 9) | The test is a criterion, and its owner is not the agent. Block, and route any change to the owner as a recorded decision. |
| The suite takes minutes, so it runs rarely | Dynamic vulnerability tests in automated suites; automated analysis and testing run regularly or continuously for all supported releases (SSDF, Table 1, PW.8.2, p. 15; RV.1.2, pp. 16–17) | Tests that don't run on every change can't be cited for it. Automate them into the pipeline. |

### Phase 4: Building in the sandbox

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| "Skip permissions, it's been fine for months" | By transfer: least privilege and least functionality on development endpoints; audited trust relationships and privilege use (SSDF, Table 1, PO.5.1–PO.5.2, pp. 8–9) | Months without trouble isn't a control. Least privilege is the practice; keep the permission prompts or a sandbox that enforces them. |
| The agent's environment can reach production credentials or data | Separate and protect environments; minimise use of production software and services from non-production; enumerate environments to stop lateral movement (SSDF, Table 1, PO.5.1, pp. 8–9; §2, p. 4) | Remove the reach. If the build session can see production, so can anything that hijacks it. |
| The agent adds a dependency nobody asked for | Components reviewed for their expected use, provenance analysed, approved versions, verified through their life; provenance kept per component (SSDF, Table 1, PW.4.1, PW.4.4, pp. 12–13; PS.3.2, p. 10) | Vet it before accepting: provenance, maintenance, known vulnerabilities. Prefer what we already approved. |
| The agent runs for an hour unattended and reports success | Evidence is what the toolchain records: automation documents that practices were performed; artefacts and audit trails (SSDF, Table 1, PO.3, PO.3.3, pp. 7–8) | The report is a claim. Open the run records; what the tools didn't record didn't happen. |

### Phase 5: Gating deterministically

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| A gate was skipped "just this once" | Exception requests recorded with approvals and rejections; approved exceptions reviewed; exception rationales retained (SSDF, Table 1, PO.4.1, p. 8; PO.1.2, p. 5; PW.1.2, p. 11) | Log it as an exception with a reason and an approver, and show it on the pack. |
| The pipeline builds different artefacts for test and for production | Reproducible builds and provenance and integrity verification in the toolchain; hashes and signing; releases archived with integrity and provenance data (SSDF, Table 1, PO.3.2, p. 7; PS.1.1, p. 9; PS.3.1, p. 10) | We warrant what ships, so show that what ships is what the gates judged. Building once is the harness rule; the integrity record is the SSDF's. |
| Lint and type errors are suppressed rather than fixed | Warnings treated as errors except identified false positives; linters; static-analysis findings handled by humans (SSDF, Table 1, PW.6.2, p. 14; PW.5.1, p. 13; PW.7.2, p. 15) | A suppression needs an identified false positive and a reviewer. Otherwise it's a finding. |
| The secrets scan or dependency audit is "noisy" so it was turned off | Dependency half: known vulnerabilities checked automatically through components' life cycles; findings recorded and triaged; continuous automated analysis (SSDF, Table 1, PW.4.4, p. 13; PW.7.2, p. 15; RV.1.2, pp. 16–17) | Triage the noise, don't drop the check. The audit is how we know components stay safe. |

### Phase 6: Reviewing independently

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The same session that wrote the code reviews it | Design review by qualified people not involved and/or automated processes; self-review only as a complement (SSDF, Table 1, PW.2.1, p. 12; PW.5.1, p. 13) | Self-review counts as a complement, never as the review. Bring in a reviewer that wasn't involved. |
| The reviewer's findings are long and nobody sorts them | Findings and remediation recommendations recorded and triaged in the team's workflow (SSDF, Table 1, PW.7.2, pp. 14–15; PW.8.2, p. 15) | Every finding gets a triage decision in the tracker before the pack is built. |
| The builder approves because reading the diff is too slow | Human review and/or tool-based analysis selected by policy and the software's stage (SSDF, Table 1, PW.7.1, p. 14) | The framework doesn't require reading every line; it requires a review policy. Follow it, and record what reviewed the change. |
| The change "looks fine" but touches something with a history of incidents | Earlier vulnerability reports used in risk modelling; regression tests for earlier vulnerabilities; root causes and lessons kept searchable (SSDF, Table 1, PW.1.1, p. 11; PW.8.2, p. 15; RV.3.1, p. 18) | Pull the history: the earlier report, its root cause, and the regression test that should still pass. |

### Phase 7: Warranting the change

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The pack says "all tests pass" with no run record | Artefacts generated by tools as evidence; tests documented (SSDF, Table 1, PO.3.3, pp. 7–8; PW.8.2, p. 15) | No artefact, no claim. Send it back for the run record. |
| A risk is listed with no owner and no rollback | Risk responses and mitigation plans recorded; responses are risk-based decisions to remediate, accept or transfer; an accountable leader (SSDF, Table 1, PW.1.2, p. 11; RV.2.2, pp. 17–18; PO.2.3, p. 7) | Each risk needs a recorded response and someone accountable. The rollback is a harness rule; the record is the SSDF's. |
| The client wants it today and the review is still open | Shipping with an open review is an exception: recorded, approved or rejected, with a rationale (SSDF, Table 1, PO.4.1, p. 8; PW.1.2, p. 11) | If we ship today, it's a recorded exception the accountable person approves, visible on the pack. |
| Nobody could explain how this part works if the agent were unavailable | Code owners named; design decisions and risk records retained for audit and maintenance (SSDF, Table 1, PO.2.1, p. 6; PW.1.2, p. 11) | Name the owner and point to the design record. If neither exists, it isn't ready to sign. |

### Phase 8: Releasing and operating

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| Warnings and code complexity climb release after release | Warnings half: treated as errors except identified false positives; approved build settings continuously verified (SSDF, Table 1, PW.6.2, p. 14) | Rising warnings mean the warnings gate isn't holding. Restore it. The framework is silent on complexity. |
| Something went wrong after release | Assess and respond by risk; identify the root cause, analyse patterns, sweep the class, update the process (SSDF, Table 1, RV.2.1–RV.2.2, pp. 17–18; RV.3.1–RV.3.4, pp. 18–19) | Fix the instance, then the class, then the practice that let it through, and add a toolchain detection. |

## Trigger extensions surfaced by this source

| Phase | Trigger | Content from this source | Teach-in-the-moment script |
|---|---|---|---|
| 1 | The spec names no security requirement, or none from a written list | Software security requirements identified, documented and maintained (SSDF, Table 1, PO.1.2, p. 5) | Return it: which written requirements does this change meet? |
| 4 | The agent commits under a person's account or a shared identity, or changes code another owner holds without that owner's approval | Version history attributed to accounts; code owners approve others' changes (SSDF, Table 1, PS.1.1, p. 9) | Give the agent its own identity, and route the change to the code's owner. |
| 4 | The agent runs on a machine also used for unrelated work | Dedicated development endpoints, separate from endpoints for other tasks (SSDF, Table 1, PO.5.2, p. 9) | Move the agent to a development-only environment. |
| 4 | A new agent, tool or plugin joins the toolchain with no assessment | By transfer: tools are securely deployed, assessed and maintained, with configuration as code and logs monitored (SSDF, Table 1, PO.3.2, p. 7) | Treat the agent as a toolchain component: assess it, configure it as code, and watch its logs. |
| 5 | A compiler, interpreter, build image or CI action changed version and nobody asked for it | Build tools under change management; unexpected changes audited; authenticity and integrity validated (SSDF, Table 1, PW.6.1, p. 14) | Unexpected tool changes get audited before the build is trusted. |
| 5 | A gate's criteria or threshold are edited in the same change they judge, or the agent session can edit the gate log | Criteria defined and tracked; supporting information safeguarded against alteration or deletion (SSDF, Table 1, PO.4.1–PO.4.2, p. 8) | Criteria and records sit outside the change they judge. |
| 5 | A gate needs evidence no tool produces (a design sign-off, a risk acceptance) and nobody is assigned to give it | Responsibility assigned for evidence tools cannot generate (SSDF, Table 1, PO.3.3, pp. 7–8) | Name the person who provides that evidence, or the gate can't pass. |
| 5 | The change switches a default setting to a weaker value (debug on, a check off, a permissive policy) | Secure default baseline that does not weaken platform security; defaults documented and under change control (SSDF, Table 1, PW.9.1–PW.9.2, p. 16) | Hold the secure baseline; a weaker default is a change-controlled decision, not a side effect. |
| 7 | The pack claims SSDF conformance with no task-selection record | Not a checklist; a basis for a risk-based approach; examples neither required nor exhaustive (SSDF, §1, p. 3; §2, p. 4) | Return it for the selection: tasks, reasons, gaps. |
| 7 | The release changes components and the SBOM or provenance data was not updated | Provenance updated whenever components change; releases archived with integrity and provenance data (SSDF, Table 1, PS.3.1–PS.3.2, p. 10) | Update the SBOM with the release, or the client can't check what they got. |
| 7 | Nobody has said which practices the agent platform, model provider or host owns | Shared responsibility: agree with providers who owns each practice and task, and how they attest (SSDF, §1, p. 3) | Write down the split with each provider, and how each shows its share. |
| 8 | A client, user or public source reports a vulnerability in a shipped release | Gather and investigate credible reports; record and rate by exploitability and impact; plan the response, including temporary mitigation and advisories (SSDF, Table 1, RV.1.1, p. 16; RV.2.1–RV.2.2, pp. 17–18) | Record it, rate it, mitigate now, fix properly, then go after the root cause. |
| 8 | A fixed vulnerability's type shows up again in a later change | Root causes analysed over time for patterns; toolchain detections added; class swept; process updated (SSDF, Table 1, RV.3.2–RV.3.4, pp. 18–19) | A repeat means the process didn't change. Add the detection and sweep the class. |
| 8 | Nobody outside the harness has a published way to report a vulnerability, or the response playbook has never been exercised | An accessible disclosure programme; response processes exercised periodically (SSDF, Table 1, RV.1.3, p. 17) | Publish how to report, and rehearse the response before you need it. |
| 8 | A third-party component in production loses maintenance or reaches end-of-life | Ongoing maintenance confirmed; end-of-life and unavailable components planned for (SSDF, Table 1, PW.4.4, p. 13) | Plan the replacement now; an unmaintained component is a growing risk. |
