# get_account_activity

What one of your accounts did over the last N days (default 30, max 90): actions and errors per module, PeerFlood days, Telegram request load, spamblock/freeze events (last 10), peak day. For a bought account — only since your purchase. Free.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `days` | integer |  | default `30`, min `1`, max `90` |
