# launch_inviter_preflight

Dry-run the Inviter: destination, main account rights, mode and targets — nothing is joined or invited.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `destination` | string | **required** | Same as launch_inviter. |
| `targets` | string[] |  | Users you plan to invite. |
| `invite_mode` | `admin` \| `direct` |  |  |

## config

Only the first of account_ids is used — the main account. Config: target_source (manual\|contacts\|chats), candidate_account_ids (your helper accounts to check rights for).

| field | type | | notes |
|---|---|---|---|
| `allow_spamblock` | boolean |  | Also run the selected accounts that are in spamblock (off by default). Only accounts listed in account_ids are affected. |
