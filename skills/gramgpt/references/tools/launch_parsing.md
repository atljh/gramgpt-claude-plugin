# launch_parsing

Launch a parser. kind=channels\|groups search by keywords; kind=users\|messages\|comments extract from given targets.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `kind` | `auto` \| `channels` \| `comments` \| `groups` \| `messages` \| `users` | **required** | What to parse. |
| `targets` | string[] |  | Required for users/messages/comments — what to parse from. |
| `search_keywords` | string[] |  | Required for groups (and for channels in search mode). |
