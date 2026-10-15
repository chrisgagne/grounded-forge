# Summarise this warranty pack in plain language

The accountable person reads a warranty pack before deciding whether to sign a change off or return it. The pack is `$draft`. The ledger it was built from is `$ledger`; every event in it has an id like e012.

Write a short summary, 5 to 12 lines, for someone who won't read code: what the change does, what was shown by running things, what is only the builder's claim, what blocked or was accepted, and what risk remains.

Rules:

- Every line cites at least one ledger event id in square brackets, like [e012], for the evidence it rests on. Lines without a valid citation are deleted before anyone sees the pack.
- Cite only ids that exist in the ledger, and say nothing the ledger doesn't record.
- Report what the builder said as "the builder says", never as fact.
- Leave the decision to sign or return to the accountable person; recommend neither.

Your final message is only the summary lines, one per line, each starting "- ".
