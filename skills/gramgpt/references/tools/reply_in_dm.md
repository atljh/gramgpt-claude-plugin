# reply_in_dm

Send a Telegram DM from `account_id` to `peer`. Returns the sent message id. Optional `parse_mode`, `schedule_at` (Telegram scheduled send).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone |
| `text` | string | **required** | max len `4096` |
| `reply_to_msg_id` | integer |  |  |
| `parse_mode` | `markdown` \| `html` \| `none` |  | Text formatting. Omitted = markdown (as before). |
| `schedule_at` | ['string', 'integer'] |  | Telegram scheduled send: ISO-8601 datetime (UTC if no offset) or unix seconds, up to 365 days ahead. |
