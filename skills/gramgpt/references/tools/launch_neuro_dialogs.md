# launch_neuro_dialogs

Launch NeuroDialogs: accounts keep AI conversations going in their own DMs. Honours accountProtectionEnabled / accountProtectionLevel inside config.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |

## config

Module config. Knobs: ai_enabled, ai_prompt_id, language_mode, work_mode (count\|time), max_messages, duration_minutes, min_reply_delay / max_reply_delay, active_hours_start / _end, accountProtectionEnabled / accountProtectionLevel.

| field | type | | notes |
|---|---|---|---|
| `accountProtectionEnabled` | boolean |  | Enable AI Account Protection (requires the paid module). |
| `accountProtectionLevel` | `careful` \| `balanced` \| `aggressive` |  | Protection level; defaults to balanced. |
| `active_hours_start` | ['integer', 'null'] |  | Working window start hour 0-23 (with active_hours_end). Omit both = round the clock.; min `0`, max `23` |
| `active_hours_end` | ['integer', 'null'] |  | Working window end hour 1-24, exclusive: 9 and 24 = 09:00-23:59; start > end = overnight (22 and 6). Outside the window the task keeps running but posts no comments / chat replies (ND: no DM replies); messages that arrive then are skipped, not answered later. NC/NChat PM auto-replies (reply_to_pms) ignore the window.; min `1`, max `24` |
| `active_hours_timezone` | ['string', 'null'] |  | IANA timezone of the window, e.g. Europe/Moscow (default). |
