# resolve_links

Check up to 10 links / @usernames / invite links without joining: kind, title, members, open (false = join by request), comments, parsable.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `links` | string[] | **required** | min items `1`, max items `10` |
