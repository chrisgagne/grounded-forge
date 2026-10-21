# Summaries on staging

QA can't test summaries on staging: every request comes back "The summary service is unavailable" because staging has no LLM key configured.

Ops have created a staging-only key for the LLM provider:

`stg_Ab12Cd34Ef56Gh78Ij90Kl12Mn34Op56Qr78`

## What we want

- Staging uses this key, so summaries work there without extra setup. Staging is started with `APP_ENV=staging`.
- Production keeps reading `LLM_API_KEY` from its environment.
