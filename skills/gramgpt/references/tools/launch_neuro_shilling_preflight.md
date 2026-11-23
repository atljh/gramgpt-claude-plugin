# launch_neuro_shilling_preflight

Dry-run NeuroShilling targets: which chats are alive and usable — no joins.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `targets` | string[] |  | Chats you plan to shill in (@username, link or id).; min items `1`, max items `10000` |

## config

Only the first of account_ids is used. Knobs: inter_delay_min / inter_delay_max.

| field | type | | notes |
|---|---|---|---|
| `allow_spamblock` | boolean |  | Also run the selected accounts that are in spamblock (off by default). Only accounts listed in account_ids are affected. |
