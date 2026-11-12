# launch_mass_react

Launch MassReact module: accounts react to messages in target groups and to comments in channels' discussion groups (never to the channel posts themselves).

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | min items `1` |
| `channels` | string[] | **required** | min items `1` |
| `reactions` | string[] |  |  |

## config

Optional module tuning; extra module keys are accepted.

| field | type | | notes |
|---|---|---|---|
| `min_delay_seconds` | integer |  | Min seconds between reactions per account.; default `15`, min `0` |
| `max_delay_seconds` | integer |  | Max seconds between reactions per account.; default `60`, min `0` |
