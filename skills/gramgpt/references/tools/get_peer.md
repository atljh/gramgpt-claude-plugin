# get_peer

Profile of a user: names, username, about, premium, stories, birthday, status, personal channel, small photo as a signed `photo_url`.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `with_photo` | boolean |  | default `true` |
