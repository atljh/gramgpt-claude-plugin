# launch_neuro_shilling

Launch NeuroShilling: accounts hold a scripted promo dialogue in target chats.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `targets` | string[] |  | Chats to shill in (@username, link or id).; min items `1` |

## config

Module config. `targets` is required. Common knobs: pool_mode, cooldown_min_sec / cooldown_max_sec, max_msgs_per_acc_per_hour, parallel_shards_count, uniquify_messages, scenario_snapshot.

| field | type | | notes |
|---|---|---|---|
| `allow_spamblock` | boolean |  | Also run the selected accounts that are in spamblock (off by default). Only accounts listed in account_ids are affected. |
