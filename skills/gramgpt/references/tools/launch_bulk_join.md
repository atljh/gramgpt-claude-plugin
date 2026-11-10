# launch_bulk_join

Join a list of channels/chats with the given accounts. Optionally collects them into a folder.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `channels` | string[] |  | Channels/chats to join. |
