# delete_messages

Delete our own messages in the DM (up to 100); others' ids are skipped.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `message_ids` | integer[] | **required** | min items `1`, max items `100` |
| `revoke` | boolean |  | default `true` |
