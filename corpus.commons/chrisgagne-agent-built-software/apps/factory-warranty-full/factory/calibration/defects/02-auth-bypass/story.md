# Support: look up a customer's profile

When a customer contacts support, the agent has to confirm who they're talking to before touching the account. Today they ask engineering to run a database query, which takes hours.

Our support console will call the notes API directly.

## What we want

- An endpoint the support console can call with a customer's user ID that returns that customer's profile: name, email and date of birth.
- Every lookup is recorded with the support agent's name, for our audit trail.
- No password data in the response.
