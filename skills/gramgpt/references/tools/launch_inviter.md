# launch_inviter

Launch the Inviter: add target users into your channel or group — via helpers promoted by the main admin account, or directly as members.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `destination` | string | **required** | Where to invite: @username, t.me link or t.me/+ invite link of an existing channel or group. |
| `targets` | string[] |  | Users to invite (@username, phone or id). |
| `invite_mode` | `admin` \| `direct` |  | admin — via helpers promoted by the main account; direct — as members. |
