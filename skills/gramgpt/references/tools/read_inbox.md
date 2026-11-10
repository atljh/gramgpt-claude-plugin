# read_inbox

Fetch latest DMs for `account_id` (up to `limit`, newest-first), or for up to 10 accounts at once via `account_ids`.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer |  |  |
| `account_ids` | integer[] |  | min items `1`, max items `10` |
| `limit` | integer |  | default `20`, min `1`, max `200` |
| `unread_only` | boolean |  | default `false` |
