# set_dialog_folder

Put the DM with `peer` into the folder `folder_name` (created if absent); `remove: true` takes it out.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | username, int telegram_id, or phone — as in reply_in_dm |
| `folder_name` | string | **required** | max len `12` |
| `remove` | boolean |  | default `false` |
