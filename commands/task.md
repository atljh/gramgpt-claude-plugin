---
description: Follow a GramGPT task until it finishes and summarise the result
argument-hint: <task_id>
---

Use the gramgpt skill. Follow task $ARGUMENTS:

- `get_task_progress` every 30 s; report only when something changes.
- Finished parser/checker → `get_task_results` and summarise (counts, top items).
- Failed → show `stop_reason` and the last log lines (`GET /api/v1/tasks/<id>/logs/` if `GRAMGPT_API_KEY` is set) and suggest a fix.

Stop at `completed`, `failed` or `cancelled`. Change nothing without asking.
