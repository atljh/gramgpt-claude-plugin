# launch_mass_looking

Launch MassLooking: view (and optionally like) targets' stories. Honours accountProtectionEnabled / accountProtectionLevel inside config.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `peers` | string[] |  | Users/chats whose stories to view. |

## config

Module config. Knobs: peers, delay_min / delay_max, max_stories_per_peer, max_total_views, like_enabled, like_probability, accountProtectionEnabled / accountProtectionLevel.

| field | type | | notes |
|---|---|---|---|
| `accountProtectionEnabled` | boolean |  | Enable AI Account Protection (requires the paid module). |
| `accountProtectionLevel` | `careful` \| `balanced` \| `aggressive` |  | Protection level; defaults to balanced. |
