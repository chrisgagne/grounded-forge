# Disclaimer and warranty

**Supplier.** The Materials are supplied by **Approach Perfect, Limited** (NZ Company Number 7916916), a New Zealand registered company ("the Supplier"). The Supplier provides the Materials in trade, gratis, with no consideration paid by any recipient. Copyright in the Materials is held by Chris Gagné personally and licensed to recipients under `LICENSE` (code and substrate documentation: architecture docs, build profiles, skill specifications, scripts, index frames, vocabulary reference) and `LICENSE-CONTENT` (content: references, distillations, lenses, source sidecars, and long-form prose); the Supplier distributes the Materials under those licences.

**Jurisdiction.** This disclaimer is drafted under the law of New Zealand. The Supplier is based in New Zealand and offers the Materials from New Zealand. Recipients outside New Zealand take the Materials subject to their own local law; nothing in this file is intended to limit any non-excludable consumer right a recipient holds under the law of their own jurisdiction.

**Not legal advice.** This file records the Supplier's intent. It is not legal advice and has not been settled by a New Zealand-qualified solicitor. Anyone relying on it commercially should obtain their own legal advice.

---

## 1. No warranty: the materials are provided "as is"

The code, documentation, references, distillations, lenses, skills, build profiles, indexes, and any other artefact in this repository, and any compiled distribution produced from it (together, the **Materials**), are provided on an "as is" and "as available" basis.

To the maximum extent permitted by law, the Supplier disclaims all warranties, representations, conditions, and guarantees of any kind, whether express, implied, or statutory, including without limitation any warranty or guarantee of:

- accuracy, completeness, currency, or reliability;
- fitness for any particular purpose;
- acceptable quality;
- merchantability;
- non-infringement of third-party rights;
- uninterrupted, error-free, or secure operation; or
- correspondence between the Materials and any description, sample, or demonstration.

The Supplier does not warrant that the Materials are suitable for any specific decision, operational, regulatory, safety, clinical, financial, legal, or coaching context. Users are solely responsible for judging fitness for their own use.

## 2. Consumer Guarantees Act 1993 (NZ): contracting out for in-trade supplies

The Supplier supplies the Materials in trade. Where the Materials are acquired by a person who is also **in trade** (within the meaning of the Consumer Guarantees Act 1993 (NZ)) and that person acquires the Materials for the purposes of a business, the Supplier and that person agree that:

- the Consumer Guarantees Act 1993 does not apply to the supply of the Materials; and
- it is fair and reasonable for the parties to be bound by this clause, having regard to the fact that the Materials are supplied free of charge under open-source and open-content licences for evaluation, study, and self-directed use, with no consideration paid and no commercial relationship between Supplier and recipient.

This clause is intended to engage section 43 of the Consumer Guarantees Act 1993. It does not apply, and is not intended to apply, to any supply to a person who is a **consumer** within the meaning of that Act; the Act's guarantees to consumers cannot lawfully be contracted out of and nothing in this file purports to do so.

## 3. Fair Trading Act 1986 (NZ): contracting out for in-trade supplies

The Supplier supplies the Materials in trade. Where the Materials are acquired by a person who is also in trade and that person acquires the Materials in trade, the Supplier and that person agree, under section 5D of the Fair Trading Act 1986 (NZ), that sections 9, 12A, 13, and 14(1) of that Act do not apply to the supply. The parties agree it is fair and reasonable for them to be bound by this clause, having regard to the same matters set out in clause 2.

This clause does not apply, and is not intended to apply, to any supply to a person who is not in trade. Nothing in this disclaimer has the effect of contracting out of the Consumer Guarantees Act 1993 or the Fair Trading Act 1986 except to the extent permitted by New Zealand law.

## 4. Not professional advice

The Materials include distillations of third-party works covering, among other domains, decision-making, organisational behaviour, just-culture incident review, after-action review, retrospectives, stakeholder engagement, ethics, finance, accounting, marketing, economics, software engineering practice, and adjacent areas. The Materials are intended as a **structured retrieval substrate over source-grounded references**, not as professional advice.

In particular, nothing in the Materials constitutes:

- legal advice;
- medical, psychological, or clinical advice;
- financial, investment, accounting, tax, or actuarial advice;
- engineering, safety, or risk-assessment certification;
- regulatory or compliance advice; or
- coaching, supervision, or therapeutic intervention provided in a regulated capacity.

Anyone needing advice in any of these domains should consult a suitably qualified professional in their own jurisdiction.

## 5. AI-generated and AI-assisted content

The references and distillations in this repository are produced by a documented multi-pass ingestion protocol in which a large language model extracts, classifies, and projects material from verified source texts. The protocol is designed to enforce source-only citation discipline and includes an audit pass, but **no audit eliminates the risk of model error**. Possible failure modes include misattribution, fabricated quotations, dropped qualifiers, misclassified evidence, omitted content, and silent gaps in coverage.

Users should treat every distillation as a structured pointer back to the underlying source. Any claim relied on for an operational, regulatory, or commercial purpose should be verified against the cited source before use.

## 6. Security and large-language-model risk

The Materials are designed to be used with large language models, including hosted models accessed over a third-party API. Use of the Materials in any LLM-mediated workflow carries security and confidentiality risk that does not exist in non-LLM alternatives. In particular:

- **Data leaves your control.** Any text submitted to a hosted LLM, including source content, references, distillations, user input, and any operational data a user mixes into a session, is transmitted to and processed by the model provider under the provider's own terms. The Supplier is not the model provider and has no control over that processing, storage, retention, training-data use, or downstream access.
- **Prompt-injection risk.** Source material, references, distillations, and any third-party text loaded into a session may contain instructions that an LLM treats as authoritative. A malicious or accidental prompt-injection payload embedded in source content can cause the model to exfiltrate context, fabricate citations, ignore the source-only audit, or take actions unintended by the operator. The ingestion protocol does not eliminate this risk.
- **Tool-use and agentic risk.** Where the Materials are used with an agent that has tool access (file read/write, shell, network, third-party APIs), a successful prompt injection or model error can result in unintended file changes, unintended external requests, or unintended disclosure to third parties. Users running the Materials in agentic configurations are responsible for sandboxing, permissioning, and reviewing every action.
- **No security warranty.** The Supplier makes no warranty that the Materials, or any workflow built on them, are secure, confidential, free of injection-attack surface, or suitable for handling sensitive, regulated, or privileged information. Users should not load confidential, personal, health, legal-privileged, or otherwise sensitive material into LLM-mediated workflows built on the Materials without an independent security review.

Users remain solely responsible for choosing what information to expose to an LLM, for the configuration and permissions of any agent built on the Materials, and for the consequences of any disclosure or action that results.

## 7. Limitation of liability

To the maximum extent permitted by law, the Supplier is not liable for any loss, damage, cost, or expense — whether direct, indirect, consequential, incidental, special, exemplary, or punitive, and whether arising in contract, tort (including negligence), equity, under statute, or otherwise — arising out of or in connection with:

- the Materials;
- any use of, or inability to use, the Materials;
- any decision, action, or omission taken in reliance on the Materials;
- any error, omission, inaccuracy, or other defect in the Materials; or
- any disclosure, prompt-injection event, data loss, or third-party processing arising from use of the Materials with a large language model or with any tool-using agent.

Where any liability cannot be excluded by law, the Supplier's total aggregate liability is limited to NZD 100.

## 8. Third-party content

The Materials incorporate references and distillations derived from third-party sources, each under its own upstream licence as recorded in `LICENSE-CONTENT` and in each source sidecar at `corpus.commons/{corpus}/sources/original/{slug}.source.md`. No endorsement of the Supplier or this project by any third-party author or rightsholder is implied. Trademarks and service marks named in the Materials remain the property of their respective owners.

## 9. Severability

If any clause of this disclaimer is held unenforceable in any jurisdiction, the remaining clauses continue in effect, and the unenforceable clause is read down to the minimum extent necessary to make it enforceable.

## 10. Governing law

This disclaimer is governed by the law of New Zealand. The parties submit to the non-exclusive jurisdiction of the New Zealand courts in respect of any dispute arising out of or in connection with the Materials.

---

Copyright © 2026 Chris Gagné. All rights reserved, save as expressly licensed under `LICENSE` (code and substrate documentation) and `LICENSE-CONTENT` (references, distillations, lenses, source sidecars, long-form prose).
