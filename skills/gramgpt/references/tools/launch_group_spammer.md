# launch_group_spammer

Launch the group broadcaster: post a message chain into chats, by target list or folder links.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `targets` | string[] |  | Chats to post in (@username, link or id). |
| `chain` | object[] |  | Message items sent in order. |
| `folder_links` | string[] |  | Telegram folder invite links to take chats from. |

## config

Module config. Same shape as the DM broadcaster: `chain` of message items plus targets (or `folder_links` to pull chats from a folder). Also honours accountProtectionEnabled / accountProtectionLevel and the schedule keys (start_at, stop_at, active hours, days_of_week).

| field | type | | notes |
|---|---|---|---|
| `accountProtectionEnabled` | boolean |  | Enable AI Account Protection (requires the paid module). |
| `accountProtectionLevel` | `careful` \| `balanced` \| `aggressive` |  | Protection level; defaults to balanced. |
| `min_delay_seconds` | integer |  | Min pause between targets, seconds (default 30). |
| `max_delay_seconds` | integer |  | Max pause between targets, seconds (default 90). |
| `unwarmed_pace_factor` | number |  | Auto-throttle for accounts younger than 14 days: the pause between targets is multiplied by this (default 2.0). Pass 1 to disable it and keep the delays exactly as given. |
| `start_at` | string |  | ISO-8601: the task waits until then before the first send. |
| `stop_at` | string |  | ISO-8601: no new targets after it; the task ends. |
| `active_hours_start` | integer |  | Working window start hour 0-23 (with active_hours_end). |
| `active_hours_end` | integer |  | Working window end hour 1-24, exclusive; 22→6 = overnight. |
| `days_of_week` | integer[] |  | ISO weekdays to work on: 1=Mon … 7=Sun. |
| `timezone` | string |  | IANA timezone of the schedule and of the daily plan (default Europe/Moscow). |
