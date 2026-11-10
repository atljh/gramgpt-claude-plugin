# get_stories

Active stories of a peer (id, date, type, caption). Does not mark them viewed.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
