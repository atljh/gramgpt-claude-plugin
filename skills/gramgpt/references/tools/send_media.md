# send_media

Send a voice / video_note / photo / video / document from `media_id` (POST /media/) or an http(s) `url`. Use Idempotency-Key.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `kind` | `voice` \| `video_note` \| `photo` \| `video` \| `document` | **required** |  |
| `media_id` | string |  |  |
| `url` | string |  | max len `2048` |
| `caption` | string |  | max len `4096` |
| `parse_mode` | `markdown` \| `html` \| `none` |  |  |
| `reply_to_msg_id` | integer |  |  |
