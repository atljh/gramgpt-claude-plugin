# launch_story_mentions

Launch Story Mentions: post stories that tag target users, or only open empty dialogs with them.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `targets` | string[] |  | Users to tag (@username, phone or id). |
| `media_pool` | object[] |  | Story images/videos, picked in turn. media_url is "gg-media:<media_id>" from POST /api/v1/media/; mime is its mime_type (video/* posts a video story). Not needed with prime_only. |
| `caption_template` | string |  | Story caption, spintax {a\|b} allowed; {username} marks where the mentions go, otherwise they are appended. |

## config

Module config. Each target is tagged once per campaign. Knobs: target_source (manual\|contacts), mentions_per_story (1-10, default 3), max_stories_per_day (per account across tasks, default 10), period (story lifetime: 21600\|43200\|86400\|172800 s), link_url / link_style (visible\|invisible) / link_text / link_y — link sticker, media_fit (cover\|fit), uniquify_media (default true: own photo/video file per account), prime_only (true = no stories, only empty dialogs; max_primes_per_day, min_prime_delay_seconds / max_prime_delay_seconds), min_delay_seconds / max_delay_seconds between stories (default 60/300), flood_wait_sleep_seconds / flood_wait_max_count. Volume: work_mode (count\|time), max_messages (people, default 100), duration_minutes (time mode, 0 = no limit). start_at (ISO-8601) delays the start; unwarmed_pace_factor (default 2.0) slows accounts younger than 14 days, 1 turns it off. Waiting (schedule, daily plan, followups) is bounded by the task lifetime of 48 h; a multi-day campaign is relaunched daily.

| field | type | | notes |
|---|---|---|---|
| `allow_spamblock` | boolean |  | Also run the selected accounts that are in spamblock (off by default). Only accounts listed in account_ids are affected. |
