# cancel_task

Cancel a ScriptTask. Idempotent.

## Input

| field | type | | notes |
|---|---|---|---|
| `task_id` | string | **required** |  |
| `force` | boolean |  | Cancel a running task outright (no ack wait).; default `false` |
