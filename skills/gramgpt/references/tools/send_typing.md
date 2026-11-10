# send_typing

Show «typing…» / recording voice / video note to `peer` (~5 s; repeat while composing).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `action` | `typing` \| `record_voice` \| `record_round` \| `cancel` |  | default `"typing"` |
