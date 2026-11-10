# launch_neuro_commenting

Launch NeuroCommenting module on accounts targeting channels. Returns task_id; poll via get_task_progress.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | min items `1` |
| `channels` | string[] |  | min items `1` |

## config

Optional module tuning; extra module keys are accepted.

| field | type | | notes |
|---|---|---|---|
| `use_account_subscriptions` | boolean |  | Comment in channels each account is subscribed to (with comments enabled); `channels` is then ignored and may be omitted.; default `false` |
| `enable_comment_visibility_check` | boolean |  | 5 min after sending, check that each comment is still visible.; default `false` |
| `join_max_per_proxy` | integer |  | Max simultaneous joins per proxy (default 2).; min `1`, max `10` |
| `start_at` | string |  | ISO-8601 deferred start: the task is created now and waits until then (max 48 h ahead) before the first comment. |
| `min_delay_seconds` | integer |  | Min seconds between comments per account.; default `30`, min `0` |
| `max_delay_seconds` | integer |  | Max seconds between comments per account.; default `120`, min `0` |
| `work_mode` | string |  | 'count' stops after N comments; 'time' runs for duration_minutes.; default `"count"` |
| `duration_minutes` | integer |  | Run length when work_mode='time'.; default `60`, min `1` |
| `comment_mode` | `all` \| `random` \| `keywords` |  | 'all' comments under every new post; 'random' samples by comment_probability; 'keywords' needs a `keywords` list.; default `"all"` |
| `comment_probability` | number |  | Share of posts to comment on. Required when comment_mode='random'.; min `0`, max `1` |
| `post_source` | `new` \| `existing` \| `both` |  | 'new' monitors posts published after start; 'existing' comments the last existing_posts_count posts per channel, then finishes; 'both' does that catch-up, then keeps monitoring. Posts the account already commented are skipped.; default `"new"` |
| `existing_posts_count` | integer |  | Recent posts per channel for post_source 'existing'/'both'.; default `10`, min `1`, max `100` |
| `active_hours_start` | ['integer', 'null'] |  | Working window start hour 0-23 (with active_hours_end). Omit both = round the clock.; min `0`, max `23` |
| `active_hours_end` | ['integer', 'null'] |  | Working window end hour 1-24, exclusive: 9 and 24 = 09:00-23:59; start > end = overnight (22 and 6). Outside the window the task keeps running but posts no comments / chat replies (ND: no DM replies); messages that arrive then are skipped, not answered later. NC/NChat PM auto-replies (reply_to_pms) ignore the window.; min `1`, max `24` |
| `active_hours_timezone` | ['string', 'null'] |  | IANA timezone of the window, e.g. Europe/Moscow (default). |
