# list_accounts

List your Telegram accounts. Accounts with pm_aggregation_enabled=True are not returned. Optionally filter by status.

## Input

| field | type | | notes |
|---|---|---|---|
| `status` | string |  |  |
| `project` | ['integer', 'string'] |  | Project id or exact name; "none" = no project. |
| `limit` | integer |  | default `50`, min `1`, max `200` |
