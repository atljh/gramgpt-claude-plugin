# pick_healthy_accounts

Return up to N account_ids with status=valid, spamblock clear or unknown (not checked yet). MVP: oldest-first ordering.

## Input

| field | type | | notes |
|---|---|---|---|
| `n` | integer | **required** | default `5`, min `1`, max `50` |
| `geo` | string |  |  |
