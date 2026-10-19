
# CISA, the Secure Software Development Attestation Form: Warranting Agent-Built Software Distillation

**Source:** Cybersecurity and Infrastructure Security Agency (CISA), US Department of Homeland Security, "Secure Software Development Attestation Form Instructions", containing the Secure Software Development Attestation Form, Version 1.0. OMB Control #: 1670-0052, expiration date 03/31/2027. A 10-page fillable PDF; no issue date printed (PDF metadata: created 2024-04-23). US federal government work, recorded by the operator; the document states no licence terms. Scope: open. Cited as (Form, item or section, printed page).

**Applicability gate (Pass G.0): clear yes, for five of the eight phases.** (1) The form asks the axis's central question in legal form: what exactly does the accountable person put their name to, on what knowledge, and what happens when a practice is missing or lapses? Its signer attests to practices in *present consistent use*, not to outcomes, and must notify when use stops. (2) Its content lands in Phase 2 (what the attestation covers: which software, whose code, which components), Phase 4 (practice 1's six environment controls; practices 2 and 3 on supply chain and provenance), Phase 5 (practice 4 and 4a, checks run on an ongoing basis and before releases), Phase 7 (who signs, on what basis, and the routes when a practice can't be attested: POA&M, third-party assessment) and Phase 8 (4c's disclosure programme; the duty to notify; attestations binding future versions). It says nothing to Phase 1 (specifying the change), Phase 3 (locking the tests) or Phase 6 (independent review of a change); those phases get no rows. (3) It frames against no position, but its structure (one signature over a fixed minimum, no per-practice box) is the axis's stance that a warranty must say what it does and does not stand on. Two limits govern every use here. The form governs US federal agencies' use of covered software; for any other client it is not a requirement, and its use as a model of a practice warranty is this distillation's transfer, marked *by transfer* where it carries weight. And the form names no AI or coding agent: treating agent-written code as code developed by the producer, an agent session as a development environment, or an MCP server as a software product in that environment is also transfer.

**Phase mapping.** Phase 2, Triaging risk: the three conditions that put software in scope (continuous delivery among them); the four categories out of scope; the producer's own code versus third-party components; company-wide, product or version attestations. Phase 4, Building in the sandbox: practice 1a–1f (separated environments, audited trust relationships, MFA and conditional access, documented and minimised risky software products, encrypted credentials, monitoring and incident response); practice 2 (trusted source code supply chains); practice 3 (provenance). Phase 5, Gating deterministically: practice 4 and 4a (automated vulnerability checks, ongoing and before every release); consistent use. Phase 7, Warranting the change: the signer and the basis of the signature; incomplete forms refused; practice 4b (a policy for discovered vulnerabilities before release); POA&M, extension or waiver; third-party assessment; minimum requirements, agency addenda and the reference-only mapping. Phase 8, Releasing and operating: practice 4c (vulnerability disclosure programme); 1f's incident response; the duty to notify; attestations binding future versions.

**Trigger match:** 8 of the 41 seed triggers addressed, in Phases 4, 5, 7 and 8; 18 trigger extensions logged. No trigger-mismatch flag.

## Warranting Agent-Built Software Relevance

The form is the corpus's one worked example of a signed warranty of development practice. Its purpose is "to provide the Federal Government assurances that software used by agencies is securely developed" [V] (Form, Privacy Act Statement, p. 1). It does this with one statement, signed by a person who can bind the company, that the producer *presently makes consistent use* of four practices derived from the SSDF, plus a promise to tell every agency that received the form if that stops [AP] (Form, Section III, pp. 6–7). The builder warranting agent-built software faces the same shape of commitment, by transfer: what the signature covers is the practices the harness runs, not a guarantee about the code, and the signature stays true only while the practices keep running. The form makes three things concrete that the axis otherwise argues for in the abstract. The object of the warranty is practice in present use, so a run of good releases is not what is signed. The signer's knowledge has a legal edge: willfully false or misleading information may be a criminal violation (Form, Privacy Act Statement, p. 1) [AP]. And a gap has a defined route: name the practice you can't attest to, document the mitigations, submit a plan of actions and milestones (Form, Additional Information, p. 4) [AP].

For a client that is a US federal agency, the form applies directly when the software is in scope, and one of its three scope conditions is continuous delivery: a producer that delivers continuous changes needs an attestation (Form, p. 3) [AP]. A factory where agents ship changes continuously therefore sits under the attestation with every change, and the attestation binds future versions until the producer notifies otherwise (Form, Section I, footnote 4, p. 5) [AP]. For other clients, the form's four practices are a short, public list a warranty pack can be held against, by transfer; its appendix maps each to SSDF tasks, but only "for reference purposes" [V] (Form, Appendix, p. 9).

## Key Concepts for Warranting Agent-Built Software

1.  **The signature covers practices in present, consistent use.** The attestation statement reads: "On behalf of the above-specified company, I attest that, to the best of my knowledge, [software producer] presently makes consistent use of the following practices, derived from the secure software development framework (SSDF)" [V] (Form, Section III, p. 6). The object is practice, now, not a record of past outcomes. The form does not define *consistent use* [AP] (deep reference, notes on what the form does not state). The pack has to say what consistent use means for this harness.

2.  **What puts software in scope, and what doesn't.** Software needs an attestation if it was developed after September 14, 2022, if older software was modified by major version changes after that date (the form's example: 2.5 to 3.0), or if "The producer delivers continuous changes to the software code (as is the case for software-as-a-service products or other products using continuous delivery/continuous deployment)" [V] (Form, pp. 2–3). Out of scope: software developed by federal agencies, open-source software an agency obtains freely and directly, third-party open source and proprietary components incorporated into the end product, and freely obtained, publicly available software [AP] (Form, p. 3; repeated in Section I, p. 5). An attestation can be company-wide, for one product, or for several products or specific versions [AP] (Form, Section I, p. 5).

3.  **The producer's own code, and the risk of relying on components.** "In signing this attestation, software producers are attesting to adhering to the secure software development practices outlined in Section III for code developed by the producer." [V] (Form, Section I, p. 5). Components are out of scope as products, but a producer that uses them must attest to having taken the Section III steps to minimise the risks of relying on them [AP] (Form, p. 3). By transfer, code an agent writes inside the factory is code developed by the producer; the form has no category that takes it out.

4.  **Practice 1: secure development and build environments, six actions at a minimum.** Separating and protecting each environment (1a); regularly logging, monitoring and auditing trust relationships used for authorisation and access, both to the environments and among components within each (1b); MFA and conditional access across the environments (1c); taking consistent and reasonable steps to document, and minimise use or inclusion of, software products that create undue risk in those environments (1d); encrypting sensitive data such as credentials, to the extent practicable and based on risk (1e); defensive practices, including continuous monitoring of operations and alerts and, as necessary, responding to suspected and confirmed cyber incidents (1f) [AP] (Form, Section III, items 1a–1f, pp. 6–7). By transfer, where an agent runs is a development environment, and the tools, extensions and servers it loads are software products in it.

5.  **Practices 2 and 3: trusted source code supply chains, and provenance.** The producer makes a good-faith effort to maintain trusted source code supply chains, using automated tools or comparable processes to address the security of internal code and third-party components and manage related vulnerabilities (item 2); and maintains provenance for internal code and third-party components incorporated into the software, to the greatest extent feasible (item 3) [AP] (Form, Section III, p. 7). Both are hedged in the form's own words: *good-faith effort*, *to the greatest extent feasible*.

6.  **Practice 4 and 4a: checks that run, ongoing and before every release.** The producer employs automated tools or comparable processes that check for security vulnerabilities, and operates them "on an ongoing basis and prior to product, version, or update releases" [V] (Form, Section III, items 4 and 4a, p. 7). The form names no tool; it names when the checks run.

7.  **Practice 4b: a written way to handle what the checks find, before release.** "The software producer has a policy or process to address discovered security vulnerabilities prior to product release" [V] (Form, Section III, item 4b, p. 7). The policy is what is attested, not a clean result.

8.  **Practice 4c: a disclosure programme with timelines kept.** The producer operates a vulnerability disclosure programme and accepts, reviews and addresses disclosed vulnerabilities in a timely fashion and according to any timelines the programme or applicable policies specify [AP] (Form, Section III, item 4c, p. 7).

9.  **The duty to notify, and attestations that bind the future.** "I further attest that the software producer will notify any agency to which it has submitted this form if and when the producer ceases to make consistent use of the practices identified above in developing the software." [V] (Form, Section III, p. 7). Attestations bind future versions of the named product unless and until the producer notifies the agencies that its practices no longer conform [AP] (Form, Section I, footnote 4, p. 5). A practice that lapses after signing does not lapse quietly.

10.  **Who signs, on what knowledge, and the edge on it.** The CEO, or a designee who is an employee of the producer with authority to bind the corporation, signs; by signing, that person attests that the software is developed in conformity with the form's practices [AP] (Form, p. 4). The signature is to the best of their knowledge (Form, Section III, p. 6) [AP], and "Willfully providing false or misleading information may constitute a violation of 18 U.S.C. § 1001, a criminal statute." [V] (Form, Privacy Act Statement, p. 1). All fields must be appropriately completed, and incomplete forms will not be accepted [AP] (Form, p. 3). The form has no field or checkbox beside the individual practices: one signature covers all of them [AP] (Form, p. 7; from the form's field list, per the deep reference).

11.  **When a practice can't be attested: name it, mitigate it, plan it.** "In the event that an agency cannot obtain a completed self-attestation from the software producer, an agency may still decide to use the producer’s software if the producer identifies the practices to which they cannot attest, documents practices they have in place to mitigate associated risks, and submits a plan of actions and milestones (POA&M) to the agency." [V] (Form, Additional Information, p. 4). The agency is then responsible for requesting an extension or waiver from OMB (p. 4) [AP]. The form gives no content, format or timeline for a POA&M [AP] (deep reference, notes on what the form does not state).

12.  **Third-party assessment in place of the signature, on conditions.** A producer may instead submit a third-party assessment, performed by a Third Party Assessor Organization (3PAO) that is FedRAMP certified or approved in writing by an appropriate agency official, using a baseline that includes every element of the form; the producer checks the box, attaches the assessment and need not sign, and the agency keeps the assessment from being posted publicly [AP] (Form, p. 4; Section III, p. 7). The form calls itself a minimum: agencies may add requirements, and conformance to them may be attached as an addendum [AP] (Form, pp. 3–4).

## Questions to Ask During Warranting Agent-Built Software

### Phase 2: Triaging risk

| Need | Question | Source-tag |
|---|---|---|
| In scope at all | Is the client a US federal agency using this software, and does any of the three conditions hold (new since September 2022, a major version change since then, or continuous delivery)? | pp. 2–3 |
| Every change under it | If the factory ships continuously, have we treated every change, not only the major releases, as made under the attestation? | p. 3; footnote 4, p. 5 |
| Whose code | Is all the code the agents write counted as code the producer developed, with the Section III practices applied to it? (by transfer) | Section I, p. 5 |
| Components | For third-party components in the change: they need no attestation of their own, but which Section III steps did we take to minimise the risk of relying on them? | p. 3 |
| Attestation type | Is our attestation company-wide, for one product, or for named versions, and does this change fall inside it? | Section I, p. 5 |

### Phase 4: Building in the sandbox

| Need | Question | Source-tag |
|---|---|---|
| Separation | Is the environment where the agent works separated and protected from every other environment, including production? (by transfer) | 1a |
| Trust relationships | When did anyone last review the logs of what the agent's identity, the build runners and connected services were trusted to access, and what they accessed? | 1b |
| Access control | Does every human and service path into the repository, CI and agent platform go through MFA and conditional access? | 1c |
| Risky software products | Is every tool, extension, plugin and MCP server in the agent's environment on a written list, and is each one needed? (by transfer) | 1d |
| Credentials | Are credentials in the agent's environment encrypted, or sitting in plain text in an env file, a config file or shell history? | 1e |
| Alerts | Who watches the build environment's alerts, and what happens on a suspected incident? | 1f |
| Supply chain | Which automated tool or comparable process checks the security of the components the agent added? | 2 |
| Provenance | Can we say where each piece of internal code and each component in this change came from? | 3 |

### Phase 5: Gating deterministically

| Need | Question | Source-tag |
|---|---|---|
| Checks ran | Did the vulnerability checks run against this build, before this release, and not only against an earlier one? | 4, 4a |
| Ongoing | Do the checks run on an ongoing basis, or only when someone remembers? | 4a |
| Consistent use | If a check was skipped or switched off, do we still make consistent use of the practice, and who decided that, in writing? | Section III, pp. 6–7 |

### Phase 7: Warranting the change

| Need | Question | Source-tag |
|---|---|---|
| Basis for the signature | What does the signer know about each practice, and from what record, beyond the agent's own summary? | Section III, p. 6; p. 1 |
| Authority | Is the signer the CEO, or an employee designee with authority to bind the company? | p. 4 |
| Discovered vulnerabilities | Is there a written policy for security vulnerabilities found before release, and was it applied to this one? | 4b |
| A practice we can't attest to | Is there a practice the factory doesn't meet for this software, and if so, have we named it, documented the mitigations and written a POA&M with dated milestones and owners, rather than signing over it? | p. 4 |
| Independent assessment | If an outside assessment is offered instead of a signature, does the assessor qualify, does its baseline cover every element of the form, and is the assessment attached and kept from public posting? | p. 4; p. 7 |
| Beyond the minimum | Has the client added requirements beyond the form, and where is our conformance to them recorded? | pp. 3–4 |
| Complete | Is every field complete? | p. 3 |

### Phase 8: Releasing and operating

| Need | Question | Source-tag |
|---|---|---|
| Disclosure | Is there a published way for anyone outside the factory to report a vulnerability, with timelines, and are we meeting them? | 4c |
| Incident response | When a suspected or confirmed incident happens, who responds, and how? | 1f |
| Lapse | Has any attested practice stopped since we signed, and have we notified everyone who received the form? | Section III, p. 7; footnote 4, p. 5 |

## What to Look For

**The signer is asked to sign on the agent's summary.**
- *Signal:* The accountable person is given a statement of the factory's practices to sign, and the only basis is a summary an agent wrote.
- *Diagnosis:* The signer attests to the best of their own knowledge that the producer presently makes consistent use of each practice (Form, Section III, p. 6) [AP], and on the form willfully false or misleading information may be a criminal violation (Form, p. 1) [AP]. A summary isn't knowledge of practice.
- *Follow-up:* Send it back for per-practice records: for each item, what runs, where its record is, and since when.

**A gap signed over.**
- *Signal:* One practice isn't in place (no disclosure programme yet, credentials not yet encrypted), and the plan is to sign the full attestation anyway because there's no box to leave unticked.
- *Diagnosis:* The form gives one signature for all the practices, with no per-practice field [AP] (Form, p. 7; field list). Its route for a gap is to name the practice, document the mitigations and submit a POA&M (Form, p. 4) [AP].
- *Follow-up:* Don't sign the full attestation. Write the POA&M; the form sets no format or timeline, so set dated milestones and owners.

**A practice that quietly stopped.**
- *Signal:* A dependency audit was switched off as noisy, a vulnerability scan stopped running in CI, or a new build runner joined without MFA, and releases kept going.
- *Diagnosis:* The attestation binds future versions until the producer notifies, and the signer attested that the producer will notify when it stops making consistent use of the practices (Form, footnote 4, p. 5; Section III, p. 7) [AP]. The form leaves *consistent use* undefined.
- *Follow-up:* Decide, in writing, whether the factory still makes consistent use. If not, restore the practice or notify.

**A scan of the wrong build.**
- *Signal:* The release's vulnerability scan record belongs to an earlier build, or nothing has been scanned since the last change.
- *Diagnosis:* The attested practice runs the checks on an ongoing basis and before product, version or update releases (Form, item 4a, p. 7) [AP].
- *Follow-up:* Run the check against the build being released and attach the run record.

**Software products in the agent's environment nobody listed.**
- *Signal:* The agent installed or enabled an MCP server, skill, plugin or tool package, or the diff edits the agent's own tool definitions or configuration.
- *Diagnosis:* By transfer, these are software products in the development environment; documenting and minimising those that create undue risk is one of practice 1's minimum actions (Form, item 1d, pp. 6–7) [AP].
- *Follow-up:* Put it on the environment's inventory with a reason, and keep it only if it is needed.

**Plain-text credentials where the agent works.**
- *Signal:* Tokens or keys in an env file, a config file or shell history the agent can read.
- *Diagnosis:* Encrypting sensitive data such as credentials, to the extent practicable and based on risk, is a minimum action (Form, item 1e, p. 7) [AP].
- *Follow-up:* Move them to encrypted storage, and record the risk call where encryption isn't practicable.

**"Components aren't in scope, so they're not our problem."**
- *Signal:* An agent-added library is waved through because the form excludes third-party components.
- *Diagnosis:* The component needs no attestation of its own, but the producer attests to the Section III steps that minimise the risk of relying on it: supply-chain tooling and provenance (Form, p. 3; items 2–3, p. 7) [AP].
- *Follow-up:* Run the supply-chain check and record the component's provenance.

**The mapping offered as evidence.**
- *Signal:* The warranty pack cites the form's appendix mapping to SSDF tasks as proof the practices are performed.
- *Diagnosis:* The mapping is provided for reference purposes (Form, p. 9) [AP]. It shows where a practice comes from, not that it ran.
- *Follow-up:* Replace it with the run records for each practice.

## When to Use This Reference

- Reach for it when the question is *what exactly am I signing, and what keeps the signature true?* It is the corpus's one source that sets out a practice warranty as a signed, legally weighted statement with a duty to notify.
- Reach for it when the client is a US federal agency, or asks for the common form: it is then a requirement, and the continuous-delivery condition puts every agent-shipped change under it.
- Reach for it when a practice can't be attested: its POA&M, extension-or-waiver and third-party-assessment routes are the corpus's only defined paths for a partial warranty.
- Reach for it as a short checklist of build-environment controls (1a–1f) to hold an agent's sandbox against, by transfer.
- Reach for the SSDF (`nist-ssdf-1-1`) for what each practice means in detail: the form states its practices in a few lines, cites the SSDF by task code, and carries none of the SSDF's text.
- Reach for another source for anything agent-specific: the form names no AI risk. Use `owasp-agentic-top10-2026` and `owasp-agentic-threats-mitigations` for agent supply chain and identity threats, and `openssf-finding-fixing-vulnerabilities-ai` for running vulnerability checks and disclosure with AI.

## Worked Example

A three-person studio uses coding agents to build and run a case-management service for a US federal agency. It deploys several times a day. The agency's contracting officer asks for the common attestation form.

**Phase 2: does it apply, and to what?** The studio delivers continuous changes, which is one of the three conditions (Form, p. 3) [AP], so the service needs an attestation and every deploy is made under it. The CEO chooses an individual-product attestation (Form, Section I, p. 5) [AP]. Someone asks whether the agent-written code counts. The form's note settles the frame:

> "In signing this attestation, software producers are attesting to adhering to the secure software development practices outlined in Section III for code developed by the producer."
> (Form, Section I, p. 5) [V]

The agents work for the studio, so their code is the studio's code (by transfer). The open-source libraries need no attestation of their own, but the studio attests to the steps it takes to minimise the risk of relying on them (Form, p. 3) [AP].

**Phase 4: the agent's environment, held against practice 1.** The builder walks the six actions. The agent installed an MCP server for the issue tracker last month; nobody listed it. It goes on the environment inventory with a reason (Form, item 1d, pp. 6–7) [AP]. A deploy token sits in plain text in the agent's env file; it moves to encrypted storage (Form, item 1e, p. 7) [AP]. Nobody has reviewed what the CI runner's identity is trusted to reach; a monthly review of those logs starts (Form, item 1b, p. 6) [AP]. The agent platform account has MFA; one service account into the repository doesn't, and is fixed (Form, item 1c, p. 6) [AP].

**Phase 5: the check that stopped.** The dependency audit was switched off two weeks ago as noisy, and eleven deploys went out since. Practice 4a runs the checks on an ongoing basis and before releases (Form, p. 7) [AP]. The studio turns it back on, tunes it, scans the current build, and records the gap and the decision that the lapse ended before signing.

**Phase 7: the signature.** The CEO is handed a two-page summary an agent wrote of the studio's practices. She sends it back for a record per practice, because she is the one attesting to the best of her knowledge, and the form is plain about the stakes:

> "Willfully providing false or misleading information may constitute a violation of 18 U.S.C. § 1001, a criminal statute."
> (Form, Privacy Act Statement, p. 1) [V]

The records show one gap: the studio has no vulnerability disclosure programme (Form, item 4c, p. 7) [AP]. There is no box to leave unticked (Form, p. 7; field list) [AP], so she doesn't sign the full attestation. The studio names the practice, documents what it has in place (the client's security contact receives reports by email), and submits a POA&M with a dated milestone to publish a disclosure policy and its timelines (Form, p. 4) [AP]. The agency, not the studio, then asks OMB for the extension or waiver (Form, p. 4) [AP].

**Phase 8: keeping it true.** The disclosure policy goes live with stated response times, and the studio meets them (Form, item 4c, p. 7) [AP]. The CEO signs. Six months later the studio moves to a new CI provider and the build environment briefly shares credentials with staging. The attestation still binds every new version, and the studio attested that it will notify any agency it sent the form to if it stops making consistent use of the practices (Form, footnote 4, p. 5; Section III, p. 7) [AP]. The builder restores the separation and records whether it lapsed long enough to count as ceasing consistent use, a line the form leaves undefined.

## Anti-patterns This Reference Helps Avoid

- **Signing on the agent's word.** *Signal:* the accountable person's only evidence of practice is an agent's summary. *Why it fails:* the signer attests to present, consistent use to the best of their own knowledge, and false statements carry legal risk (Form, Section III, p. 6; p. 1). *Counter:* a record per practice, read by the signer.
- **Outcomes in place of practice.** *Signal:* "nothing's gone wrong in ten releases" offered as the reason to sign. *Why it fails:* the attestation's object is practices in present use, not a track record (Form, Section III, p. 6). *Counter:* show each practice running now.
- **Signing over a gap.** *Signal:* the full attestation signed while one practice is missing. *Why it fails:* there is no per-practice box, and the form's route for a gap is the POA&M (Form, p. 4; p. 7, field list). *Counter:* name the practice, document mitigations, plan dated milestones.
- **The quiet lapse.** *Signal:* a check or environment control switched off after signing, with no decision recorded. *Why it fails:* the attestation binds future versions until notice, and the signer promised notice when consistent use stops (Form, footnote 4, p. 5; Section III, p. 7). *Counter:* restore it, or decide and notify.
- **The stale scan.** *Signal:* a release carries a scan of an earlier build. *Why it fails:* the checks run before each release, not once (Form, item 4a, p. 7). *Counter:* scan the build that ships.
- **An unlisted toolbox.** *Signal:* the agent's environment holds tools and servers nobody chose. *Why it fails:* risky software products in the build environment are to be documented and minimised (Form, item 1d, pp. 6–7). *Counter:* an inventory with a reason for each entry (by transfer).
- **Citing the map as the territory.** *Signal:* the SSDF mapping in the appendix offered as evidence. *Why it fails:* the mapping is for reference (Form, p. 9). *Counter:* run records.

## Integration with Other References

| Reference | Relationship |
|---|---|
| `nist-ssdf-1-1` | Upstream framework. The form's four practices are derived from the SSDF, and its appendix maps them to SSDF tasks (secure environments to PO.5.1 and PO.5.2, for instance); the SSDF carries what each task means and the notional examples the form leaves out. The SSDF also asks a tenant to agree with providers who owns each practice and how providers attest to conformance, and lists requiring compliance attestations from suppliers as an example; the form is one such attestation. They differ on how fixed the list is (see the index rows' named disagreements). |
| `nist-sp-800-218a` | Shared responsibility for AI. The Profile, a companion to the SSDF for generative AI and foundation-model development, says an acquirer can set up an agreement specifying which party is responsible for each practice and task and how each will attest to its conformance. Where an agent platform or model provider runs part of the factory's environment, that agreement decides which of the form's practices the studio can attest to on its own knowledge. |
| `owasp-agentic-top10-2026` | Agent-specific content for practices 1d, 1e, 2 and 3. Its agentic supply-chain entry asks for signed and attested manifests, prompts and tool definitions, an inventory of AI components, allowlisting and pinning, and provenance verified before install; one of its example scenarios has coding agents automatically install a compromised package that exfiltrated SSH keys and API tokens. Its rogue-agents entry holds that keys must never be directly available to agents, which sharpens 1e for an agent's environment. |
| `owasp-agentic-threats-mitigations` | Why 1b and 1c matter more with agents. Agents often run under non-human identities, which may lack session-based oversight; the trust relationships the form asks to be logged and audited include those identities. |
| `owasp-llm-top10-2026` | A limit on practice 3. Its supply-chain entry describes a build pipeline compromised from inside: an artefact built and signed by the organisation's own release infrastructure passes downstream provenance checks and internal attestation. Provenance shows where code came from, not that it is safe; pair it with practice 4's checks. |
| `openssf-finding-fixing-vulnerabilities-ai` | Operating practice 4 and 4c with AI. The guide's lesson from programmes flooded by AI-generated reports is a published reporting policy that states the evidence required and asks reporters to validate first; that is the working detail of a disclosure programme that can meet its own timelines. Its rule that invariants are enforced outside the AI fits an attested practice: it lives in a gate, not in the agent's instructions. |
| `uk-duck-book-qa-of-code` | Agreement on who owns agent-written code. Its golden rule that the only person responsible for code generated with an LLM is the person who generated it parallels the form's note that the producer attests for code it develops. |
| `uk-aqua-book-2025` | Difference on independence. The Aqua Book requires the assurer and the analyst to be independent. The form's default is self-attestation by the producer's own CEO or designee; an independent 3PAO assessment is an option, not a requirement (see the named disagreements). |
| `why-language-models-hallucinate-kalai` | Why an agent's summary can't carry a signature. Models trained and evaluated to answer rather than abstain produce confident falsehoods; a fluent account of the factory's practices is not the signer's knowledge of them. |

## Citation and Source-Integrity Notes

**Borrowed-through gaps.** The form draws its authority and its practices from federal law, an executive order, OMB policy and NIST guidance, which it cites; the deep reference marks those passages `[BT]`, and none is held in this corpus except the SSDF (`nist-ssdf-1-1`). The form gives the SSDF practices and tasks by code only; their meaning comes from `nist-ssdf-1-1`, not from this source. The legal consequence on p. 1 and the 3PAO's certification condition on p. 4 are stated as the form states them; this distillation does not interpret the law or the certification scheme behind them.

**Named limits of the source.** (1) The form is a federal procurement instrument: it binds producers of software that US federal agencies use under the policy it implements, and nothing else. Every application here to a non-federal client is transfer. (2) It names no AI, agent or coding assistant; agent-specific readings are this distillation's, marked *by transfer* where they carry weight. (3) It gives no definition of *consistent use*, no content, format or timeline for a POA&M, and no date by which an attestation is due (deep reference, notes on what the form does not state). (4) It states its practices as requirements to attest to, not as measured controls; it reports no evidence of effect. Its requirements are the form's assertions, marked `[AP]` when paraphrased. (5) Its practice items carry their own hedges (*good-faith effort*, *to the extent practicable and based on risk*, *to the greatest extent feasible*, *in a manner that minimizes security risk*); this distillation keeps them. (6) The form says it, its background and its instructions are subject to change; the OMB control number expires 03/31/2027 (Form, p. 4; p. 8).

**Evidence-marker continuity.** The `[V]` quotations are copied from the deep reference's audited passages: the purpose (p. 1), the continuous-delivery condition (p. 3), the note on code developed by the producer (p. 5), the attestation statement (p. 6), item 4a's timing phrase and item 4b (p. 7), the further attestation (p. 7), the false-information warning (p. 1), the POA&M passage (p. 4) and the mapping's reference-only phrase (p. 9). Everything else is paraphrase with `[AP]`. The form's own item-level hedges appear in italics as paraphrase, not quotation; italic phrases elsewhere (*present consistent use*, *consistent use*) are this distillation's wording of the attested terms. The absence of a per-practice field comes from the deep reference's AcroForm field-list note, not the converted text. The worked example's studio, agency, service and events are invented; each claim about the form within it is cited.

## Runtime triggers this source addresses

### Phase 4: Building in the sandbox

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| "Skip permissions, it's been fine for months" | Access to the environments under MFA and conditional access that minimise security risk; trust relationships used for access regularly logged, monitored and audited; the attestation is to present, consistent use (Form, items 1b–1c, p. 6; Section III, p. 6) | Months without trouble is a track record, not a control. What we'd sign for is access controlled and audited now. |
| The agent's environment can reach production credentials or data | Each environment separated and protected; credentials encrypted, to the extent practicable and based on risk (Form, items 1a, 1e, pp. 6–7) | Separate the agent's environment from production and encrypt what it holds. Both are minimum actions in the form. |
| The agent adds a dependency nobody asked for | Good-faith effort to maintain trusted source code supply chains with automated tools or comparable processes; provenance kept for third-party components to the greatest extent feasible (Form, items 2–3, p. 7) | Run the supply-chain check and record where it came from before it ships. Components need no attestation of their own; our handling of them does. |

### Phase 5: Gating deterministically

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| A gate was skipped "just this once" | The signer attests to present, consistent use of the practices, and to notify agencies if consistent use stops; the form leaves *consistent use* undefined (Form, Section III, pp. 6–7) | Log the skip and decide in writing whether we still make consistent use of that practice. A signature covers what we actually do. |
| The secrets scan or dependency audit is "noisy" so it was turned off | Dependency half: automated vulnerability checks, operated on an ongoing basis and before releases (Form, items 4, 4a, p. 7) | Tune it, don't drop it. A check that stopped running is a practice we no longer use. |

### Phase 7: Warranting the change

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| The client wants it today and the review is still open | Security findings only: a policy or process to address discovered security vulnerabilities before release (Form, item 4b, p. 7) | If the open finding is a security vulnerability, apply our written policy to it before release. If there's no policy, that's the gap. |
| The builder signs because the last ten went fine | The attestation's object is practices in present, consistent use, to the best of the signer's knowledge, not a record of outcomes (Form, Section III, p. 6) | Ten good releases aren't what we sign. Show that each practice is running now. |

### Phase 8: Releasing and operating

| Trigger | Content from this source that addresses it | Teach-in-the-moment script |
|---|---|---|
| Something went wrong after release | Security incidents only: continuous monitoring of operations and alerts, and responding to suspected and confirmed cyber incidents; disclosed vulnerabilities addressed in a timely fashion and within stated timelines (Form, items 1f, 4c, p. 7) | Respond under the incident practice, and if it came in as a report, meet the programme's timelines. |

## Trigger extensions surfaced by this source

| Phase | Trigger | Content from this source | Teach-in-the-moment script |
|---|---|---|---|
| 2 | The client is a US federal agency, or asks for the common form, and the factory ships continuously | Continuous delivery is one of the three conditions requiring attestation; attestations bind future versions (Form, p. 3; footnote 4, p. 5) | Every change we ship sits under the attestation, not just the major releases. |
| 2 | Someone says third-party components are out of scope, so an agent-added library needs nothing | Components need no attestation of their own, but the producer attests to the Section III steps that minimise the risk of relying on them (Form, p. 3) | Out of scope as a product, in scope as our risk. Run the supply-chain steps. |
| 4 | The agent installs or enables an MCP server, skill or tool package; a tool, extension, plugin or MCP server is added to the development or build environment; or the diff edits the agent's own prompts, instruction or memory files, tool definitions or MCP configuration | By transfer: documenting, and minimising use or inclusion of, software products that create undue risk in development and build environments (Form, item 1d, pp. 6–7) | Put it on the environment's inventory with a reason, and keep it only if it's needed. |
| 4 | Credentials sit in plain text in the agent's environment (an env file, a config file, shell history) | Encrypting sensitive data such as credentials, to the extent practicable and based on risk (Form, item 1e, p. 7) | Move them to encrypted storage, and record the risk call where you can't. |
| 4 | Nobody has reviewed what the agent's identity, the build runners and connected services accessed, or what they trust | Regularly logging, monitoring and auditing trust relationships used for access to the environments and among components within each (Form, item 1b, p. 6) | Pull the access logs and review the trust list on a schedule. |
| 4 | A human or service path into the repository, CI or agent platform has no MFA or conditional access | MFA and conditional access across the environments relevant to developing and building software (Form, item 1c, p. 6) | Close that path behind MFA or conditional access before the next build. |
| 4 | Alerts from the development or build environment go to nobody | Continuous monitoring of operations and alerts; responding to suspected and confirmed incidents as necessary (Form, item 1f, p. 7) | Give the alerts an owner and a response. |
| 5 | A release goes out on a vulnerability scan of an earlier build, or with no scan since the last change | Checks operated on an ongoing basis and before product, version or update releases (Form, item 4a, p. 7) | Scan the build that ships. |
| 5 | A gate that carries an attested practice (a vulnerability check, an environment control) is switched off on shipped changes | Present, consistent use attested; notice owed if it stops; *consistent use* undefined (Form, Section III, pp. 6–7; footnote 4, p. 5) | Decide in writing whether we still make consistent use. If not, restore it or notify. |
| 7 | The accountable person is asked to sign a statement of the factory's practices, and the only basis is the agent's summary | Attestation to the best of the signer's knowledge; willfully false or misleading information may be a criminal violation (Form, Section III, p. 6; p. 1) | Send it back for a record per practice. The signer's knowledge has to be theirs. |
| 7 | Someone who is not the CEO, not an employee, or without authority to bind the company is about to sign | The CEO or an employee designee with authority to bind the corporation signs (Form, p. 4) | Route the signature to someone who can bind the company. |
| 7 | The factory can't meet one practice for this software, and the client wants the attestation | One signature covers all practices, no per-practice box; the route is to name the practice, document mitigations and submit a POA&M; no format or timeline is set (Form, p. 4; p. 7, field list) | Don't sign over the gap. Write the POA&M with dated milestones and owners. |
| 7 | An outside assessment is offered in place of the accountable person's signature | 3PAO FedRAMP certified or approved in writing by an appropriate agency official; baseline covers every element of the form; attached; kept from public posting (Form, p. 4; p. 7) | Check the assessor qualifies and the baseline covers everything before relying on it. |
| 7 | A release is scheduled while a discovered security vulnerability is still open, and no written policy says how it is handled | A policy or process to address discovered security vulnerabilities before release (Form, item 4b, p. 7) | Write the policy, then apply it to this one before release. |
| 7 | The pack offers the form's SSDF mapping as evidence the practices ran | The mapping is provided for reference purposes (Form, p. 9) | The mapping says where a practice comes from. Attach the run records. |
| 7 | The client adds requirements beyond the form | The form is a minimum; agency-specific requirements may be attached as an addendum (Form, pp. 3–4) | Record our conformance to the extras as an addendum, not in the agent's notes. |
| 8 | Nobody outside the factory has a published way to report a vulnerability, or there are no timelines for handling reports | A vulnerability disclosure programme; disclosed vulnerabilities accepted, reviewed and addressed in a timely fashion and within its stated timelines (Form, item 4c, p. 7) | Publish how to report and how fast we respond, then keep to it. |
| 8 | A later release no longer runs on an attested practice | Notice owed to every agency that received the form; attestations bind future versions until then (Form, Section III, p. 7; footnote 4, p. 5) | Restore the practice or notify. The old signature still covers the new version. |
