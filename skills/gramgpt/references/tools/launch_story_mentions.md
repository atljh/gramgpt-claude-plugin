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
