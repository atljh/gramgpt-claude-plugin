# mark_account_dead

Mark account as dead. Status set to 'banned', 'deactivated', 'session_revoked', or 'frozen'.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `reason` | `banned` \| `deactivated` \| `session_revoked` \| `frozen` |  | default `"banned"` |
| `note` | string |  | max len `500` |
