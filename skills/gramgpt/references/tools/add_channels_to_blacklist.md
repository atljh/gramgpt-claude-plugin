# add_channels_to_blacklist

Add channels to the NeuroCommenting blacklist of all your accounts (or `account_ids`), like the panel's blacklist Import.

## Input

| field | type | | notes |
|---|---|---|---|
| `channels` | string[] | **required** | @username, t.me/... or invite links; min items `1` |
| `account_ids` | integer[] |  | Only these accounts; omit for all your accounts. |
