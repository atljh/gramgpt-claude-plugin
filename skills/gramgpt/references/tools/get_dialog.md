# get_dialog

Read one DM conversation: up to `limit` messages newest-first, older pages via `before_id`, optional `mark_read`. Attachments carry `media_type`/`duration`/`file_name`/`mime_type`/`size`, our messages `read`, bot messages inline `buttons` (for click_button).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `limit` | integer |  | default `50`, min `1`, max `200` |
| `before_id` | integer |  | Return messages older than this id (pagination). |
| `mark_read` | boolean |  | default `false` |
