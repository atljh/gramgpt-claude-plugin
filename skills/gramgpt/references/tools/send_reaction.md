# send_reaction

Put an emoji reaction on a message in the DM; empty `emoji` removes it.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `message_id` | integer | **required** |  |
| `emoji` | string |  | max len `16` |
