# set_dialog_flags

Set the DM pinned / unread / archived / muted.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `pinned` | boolean |  |  |
| `unread` | boolean |  |  |
| `archived` | boolean |  |  |
| `muted` | boolean |  |  |
