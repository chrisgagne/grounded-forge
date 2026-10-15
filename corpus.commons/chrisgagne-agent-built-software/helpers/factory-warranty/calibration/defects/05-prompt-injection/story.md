# Ask the notes assistant for what you need

Today the assistant does one thing: summarise my notes, and email that summary to me if I tick the box. People want to ask it for specific things:

- "What did I promise Sam this week?"
- "Turn my standup notes into a status update and email it to my manager at dana@acme.com."

## What we want

- `POST /notes/summary` takes an optional free-text `request`. Without it, the assistant summarises, as today.
- The assistant can email its answer to whoever the person names in their request, not only to themselves.
- Existing clients that send `email: true` keep working.
