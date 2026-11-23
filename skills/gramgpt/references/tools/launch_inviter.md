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

## config

Module config. invite_mode: admin (default) — the FIRST of account_ids is the main account, it must already be an admin of the destination with add_admins + invite_users rights and briefly promotes the other accounts (helpers, at least 1) to invite; direct — every account invites as a regular member, 1 account is enough (the only mode for a basic, non-super group). target_source: manual (default, `targets`), contacts, or chats (members of `source_chats`, up to 20; `targets` is then an optional filter). Knobs: invites_per_call (1-5, default 1), max_invites_per_account (per run, default 15), max_invites_per_day (per account across tasks, 0 = no limit), max_attempts_per_account (0 = no limit), slippage_streak_limit (default 12), min_delay_seconds / max_delay_seconds between invite cycles (30-900, default 60/120), flood_wait_sleep_seconds / flood_wait_max_count. Volume: work_mode (count\|time), max_messages (people, default 100), duration_minutes (time mode, 0 = no limit). start_at (ISO-8601) delays the start; unwarmed_pace_factor (default 2.0) slows accounts younger than 14 days, 1 turns it off. Waiting (schedule, daily plan, followups) is bounded by the task lifetime of 48 h; a multi-day campaign is relaunched daily.

| field | type | | notes |
|---|---|---|---|
| `allow_spamblock` | boolean |  | Also run the selected accounts that are in spamblock (off by default). Only accounts listed in account_ids are affected. |
