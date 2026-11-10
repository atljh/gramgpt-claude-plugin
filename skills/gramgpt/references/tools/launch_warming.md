# launch_warming

Launch auto-warming module: accounts read dialogs / join channels / scroll feed to simulate organic activity.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | min items `1` |
| `duration_minutes` | integer |  | default `60`, min `5`, max `1440` |
| `channels_to_join` | string[] |  |  |
