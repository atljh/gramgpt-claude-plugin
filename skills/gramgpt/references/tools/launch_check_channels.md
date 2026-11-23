# launch_check_channels

Filter a list of channels by size, comments and activity — no joins.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `targets` | string[] |  | What to check (max 10000).; min items `1`, max items `10000` |

## config

Module config. Knobs: min_participants, require_comments, max_inactive_days, exclude_boards (drop chats that look like ad boards), inter_delay_min / inter_delay_max.

| field | type | | notes |
|---|---|---|---|
| `allow_spamblock` | boolean |  | Also run the selected accounts that are in spamblock (off by default). Only accounts listed in account_ids are affected. |
