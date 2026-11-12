# Recipes

Tested chains of calls. Read the tool files in `tools/` for exact inputs. Every
`launch_*` goes dry-run → show plan → user agrees → real launch (see SKILL.md).

## Account health check

1. `check_balance` — subscription active? tokens left?
2. `list_accounts` — group by `status`; count valid / spamblock / frozen / no proxy.
   For an account that looks off: `get_account_activity` — what it ran, errors,
   PeerFlood days, spamblock / freeze events.
3. Problems found → offer `launch_account_op` with `op: "check_spamblock"` or `"check"`
   on the affected ids (no dry run for this tool — confirm first).
4. Follow with `get_task_progress`, then summarise: what is healthy, what needs
   `reauthorize`, `appeal_spamblock` or a new proxy (REST `/proxies/`).

## Warm up fresh accounts

1. `pick_healthy_accounts` (`n`, optional `geo`).
2. `check_account_ggr` on each — skip high-risk ones, say why.
3. `launch_warming` with `duration_minutes` (default 60) — dry-run, confirm, launch.

## Find channels → filter → comment

1. `launch_parsing` `kind: "channels"`, `search_keywords: [...]` → `task_id`.
2. Wait for completion (`get_task_progress`), then `get_task_results`
   (`item_type: "channels"`, page with `offset`/`limit` ≤ 1000).
3. `launch_check_channels` with those as `targets` → `get_task_results`
   `item_type: "passed"`.
4. Show the user the passed list; let them cut it down.
5. `launch_neuro_commenting` with `channels` = the approved list — dry-run first,
   show `ignored_keys` and skipped accounts, then launch.

## Join a list of chats

`launch_bulk_join` with `channels` — dry-run, confirm, launch. Big lists: split
across accounts rather than pushing every account through every chat.

## Inbox triage

1. `read_inbox` (`account_ids` ≤ 10, `unread_only: true`).
2. `get_dialog` for the threads that matter; `get_media` for voice/video
   (it returns a transcript when available).
3. Draft replies for the user; send with `reply_in_dm` only after they approve the text.
4. Hand a thread to the AI or take it back: `set_dialog_ai`.

## Buy accounts (REST, spends balance)

1. `GET /api/v1/marketplace/stock/` — countries and price ranges.
2. `GET /api/v1/marketplace/catalog/` or `/pick/` with filters.
3. Show ids, count and total price → explicit yes.
4. `POST /api/v1/marketplace/buy/` (≤ 20 ids) or `POST /api/v1/marketplace/orders/`
   (`count` + `filters` + `max_price`, `external_id` for idempotency).
   Not in stock? `GET /api/v1/marketplace/exchange/` (LZT lots) → same yes →
   `POST /marketplace/exchange/buy/` → poll `/exchange/orders/{id}/` for `result.account_id`.
5. Files: `POST /api/v1/accounts/sessions/export/` → poll its status → `download_url`.

## Following a long task

- Poll `get_task_progress` every 20–60 s, not in a tight loop. On HTTP 429 wait
  for `Retry-After`.
- Report changes, not every poll. Stop when status is `completed`, `failed` or
  `cancelled` and summarise the result.
- For history and logs over REST: `GET /api/v1/tasks/{id}/logs/`.
