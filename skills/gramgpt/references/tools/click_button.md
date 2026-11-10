# click_button

Press a bot's inline button by `row`/`col` from get_dialog `buttons`; returns the bot's answer. URL buttons are not pressed, their `url` is returned.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `message_id` | integer | **required** |  |
| `row` | integer | **required** | min `0` |
| `col` | integer | **required** | min `0` |
