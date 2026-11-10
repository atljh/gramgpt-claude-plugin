# edit_message

Edit the text of our own message in the DM.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `message_id` | integer | **required** |  |
| `text` | string | **required** | max len `4096` |
| `parse_mode` | `markdown` \| `html` \| `none` |  |  |
