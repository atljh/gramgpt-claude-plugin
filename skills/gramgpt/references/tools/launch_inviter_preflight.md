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
