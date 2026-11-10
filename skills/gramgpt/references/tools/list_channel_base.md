# list_channel_base

Read your channel base: channels and groups with folders, liveness and filters, to pass into launch_* tools.

## Input

| field | type | | notes |
|---|---|---|---|
| `folder` | string |  | all (default) \| none (unsorted) \| folder id. |
| `type` | `channel` \| `group` |  |  |
| `status` | `live` \| `weak` \| `dead` \| `none` |  | Liveness by last post; none — not checked yet. |
| `q` | string |  | Search in title, @username, invite link. |
| `lang` | string |  | Detected language code, e.g. ru. |
| `category` | string |  |  |
| `source` | `parsing` \| `similar` \| `db_parser` \| `link` \| `import` |  |  |
| `comments` | `open` |  | open — only where you can write (groups, channels with comments). |
| `no_ban` | `1` |  | 1 — drop channels where your accounts were kicked. |
| `subs_min` | integer |  | min `0` |
| `subs_max` | integer |  | min `0` |
| `ppd_min` | number |  | Min posts per day. |
| `apc_min` | number |  | Min average comments per post. |
| `ordering` | `-added_at` \| `added_at` \| `-participants` \| `participants` \| `-my_sent` \| `title` \| `-ppd` \| `-apc` |  | default `"-added_at"` |
| `offset` | integer |  | default `0`, min `0` |
| `limit` | integer |  | default `100`, min `1`, max `200` |
