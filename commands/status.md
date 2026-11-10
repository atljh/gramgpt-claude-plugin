---
description: GramGPT overview — balance, account health, running tasks
---

Use the gramgpt skill. Give the user a short status of their GramGPT account:

1. `check_balance` — subscription and token balance.
2. `list_accounts` — totals by status (valid, spamblock, frozen, banned, …) and how many have no proxy.
3. Running tasks: if `GRAMGPT_API_KEY` is set, `GET https://gramgpt.io/api/v1/tasks/?status=running`; otherwise skip this line.

Answer as a compact table plus at most three suggestions (e.g. accounts to re-check). Change nothing.
