# block_peer

Block `peer` from `account_id`, or unblock with `unblock: true`. Does not touch the dialog itself.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `unblock` | boolean |  | default `false` |
