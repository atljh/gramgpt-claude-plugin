# get_task_results

Read the full result list of a parser or checker task page by page (same data as GET /tasks/{id}/results/).

## Input

| field | type | | notes |
|---|---|---|---|
| `task_id` | string | **required** |  |
| `item_type` | string |  | Parsers: channels \| groups \| users (default: whatever the task produced). Checkers need it explicitly: check_numbers — on_telegram \| inactive \| not_on_telegram \| errors; check_links — links; check_channels — passed \| failed \| errors; check_stories — targets; add_contacts — added \| not_found \| errors. |
| `offset` | integer |  | default `0`, min `0` |
| `limit` | integer |  | default `200`, min `1`, max `1000` |
