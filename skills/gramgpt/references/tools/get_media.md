# get_media

Download a message attachment as a signed 10-min `url` (+ type, duration, size); voice/video notes get Telegram's `transcript` when available.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `message_id` | integer | **required** |  |
| `transcribe` | boolean |  | default `true` |
