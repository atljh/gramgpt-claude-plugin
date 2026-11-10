# launch_neuro_chatting

Launch NeuroChatting module: accounts hold conversations in target chats. Heavier than NeuroCommenting.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | min items `1` |
| `chats` | string[] | **required** | min items `1` |

## config

Optional module tuning; extra module keys are accepted.

| field | type | | notes |
|---|---|---|---|
| `min_delay_seconds` | integer |  | Min seconds between messages per account.; default `30`, min `0` |
| `max_delay_seconds` | integer |  | Max seconds between messages per account.; default `120`, min `0` |
| `work_mode` | `count` \| `time` |  | 'count' stops after max_messages sent (or cancel_task); 'time' stops after duration_minutes.; default `"count"` |
| `max_messages` | integer |  | work_mode='count' limit; see max_messages_scope.; default `50`, min `1`, max `50000` |
| `max_messages_scope` | `task` \| `per_account` |  | 'task' — max_messages for the whole task; 'per_account' — max_messages for EACH account (an account that sent its share stops, the task ends when all have).; default `"task"` |
| `duration_minutes` | integer |  | Session length; applies only with work_mode='time'.; default `60`, min `1` |
| `reaction_mode` | `interval` \| `keywords` |  | 'interval' replies by reply_probability; 'keywords' needs a `keywords` list.; default `"interval"` |
| `reply_probability` | number |  | Share of messages to reply to in reaction_mode='interval'.; default `1.0`, min `0`, max `1` |
| `keywords` | string[] |  | Substrings to match against incoming messages when reaction_mode='keywords'. |
| `keyword_alert_only` | boolean |  | reaction_mode='keywords' only: on a match, fire a `keyword.matched` webhook (see /api/v1/webhooks/) instead of generating and sending an AI reply. Nothing is posted; chats where posting is restricted are kept.; default `false` |
| `theme_matching_enabled` | boolean |  | Also match topic-related words (static dictionary + one AI call at start). false = only your keywords, no AI.; default `true` |
| `auto_resolve_captcha` | boolean |  | Solve welcome-bot captchas after joining. Unset: on, but off with keyword_alert_only. |
| `reply_to_pms` | boolean |  | Auto-reply to private messages.; default `false` |
| `active_hours_start` | ['integer', 'null'] |  | Working window start hour 0-23 (with active_hours_end). Omit both = round the clock.; min `0`, max `23` |
| `active_hours_end` | ['integer', 'null'] |  | Working window end hour 1-24, exclusive: 9 and 24 = 09:00-23:59; start > end = overnight (22 and 6). Outside the window the task keeps running but posts no comments / chat replies (ND: no DM replies); messages that arrive then are skipped, not answered later. NC/NChat PM auto-replies (reply_to_pms) ignore the window.; min `1`, max `24` |
| `active_hours_timezone` | ['string', 'null'] |  | IANA timezone of the window, e.g. Europe/Moscow (default). |
