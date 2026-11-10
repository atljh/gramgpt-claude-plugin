# delete_dialog

Delete the DM dialog with `peer` from `account_id`'s chat list; `revoke` also wipes it for the other side.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `revoke` | boolean |  | Also wipe the history for the other party.; default `false` |
