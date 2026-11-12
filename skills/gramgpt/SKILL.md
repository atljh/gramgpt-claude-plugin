---
name: gramgpt
description: Work with a GramGPT account (Telegram account management and automation) through its MCP server or REST API v1 — check accounts and GGR, run parsers and checkers, warming, NeuroCommenting, MassReact and other modules, follow task progress and results, manage DMs, buy accounts on the marketplace. Use when the user mentions GramGPT, their Telegram accounts in GramGPT, or a ggk_live_ API key.
---

# GramGPT

GramGPT is a cloud panel for Telegram accounts. The panel's actions are exposed as
tools, two ways:

- **MCP** `https://gramgpt.io/mcp/` — the tools appear in your tool list as `gramgpt` tools.
- **REST** `POST https://gramgpt.io/api/v1/tools/{tool_name}/` with the same JSON input.

Auth for both: `Authorization: Bearer ggk_live_...` (panel → Settings → API keys).
Docs: https://gramgpt.io/api/v1/docs/ · live catalog: `GET /api/v1/tools/` ·
what changed: `GET /api/v1/changelog/`.

## Setup (only if the gramgpt tools are missing)

Installed as the plugin (`/plugin install gramgpt@gramgpt`)? The tools come with it —
if they fail with 401, the key is wrong or revoked: tell the user to set a new one in
`/plugin` → gramgpt → configure. Without the plugin, ask the user for a key and run
(works on macOS, Linux and Windows):

```
claude mcp add -s user --transport http gramgpt https://gramgpt.io/mcp/ --header "Authorization: Bearer ggk_live_..."
```

`-s user` makes it work in every folder. Tell the user to restart Claude Code.
Never echo the key back, and never write it anywhere except that command.

## Rules

1. **Look first.** `check_balance`, then `list_accounts` / `pick_healthy_accounts`.
   Use account ids from them — never invent ids.
2. **Dry-run every launch.** Call `launch_*` with `"dry_run": true` (free) — except
   `launch_account_op`, which has none: describe the operation and ask instead. It returns
   dropped config keys (`ignored_keys`) and busy / dead / proxy-less accounts. Show
   the plan — module, accounts, key settings — and launch only after the user agrees.
3. **Busy accounts** (`accounts_busy`): offer `skip_unavailable: true` (run on the
   free ones) or `queue_if_busy: true` (waits up to 24 h, then fails).
4. **Track the task.** Keep `task_id`; `get_task_progress` for status,
   `get_task_results` for full parser/checker output (pages up to 1000).
   Label launches with `tags` / `external_id`.
5. **Confirm before anything irreversible or sent in the user's name** —
   `cancel_task`, `delete_accounts`, `mark_account_dead`, `launch_account_op`,
   `delete_dialog`, `delete_messages`, `reply_in_dm`, `send_media`, `edit_message`,
   `click_button`, `block_peer`, `import_accounts`, any purchase.
   Name the exact accounts / amount.
6. **Errors.** On `ok: false` read `error_code` and `recovery_hint`. `no_subscription`,
   `read_only_key` and `quota_exceeded` are not fixed by retrying — tell the user.
   Don't repeat a failing call more than once.
7. **Account safety.** Telegram freezes accounts pushed too hard: prefer warmed
   accounts, run `check_account_ggr` and `get_account_activity` before heavy tasks,
   keep module defaults unless the user changes them.

## Reference files

- `references/tools/<tool>.md` — every input and `config` key of each tool with
  types, defaults and limits (generated from the live API schema). **Read the file
  before the first call of a tool in a session** instead of guessing config keys.
- `references/recipes.md` — tested chains: account health check, warming, find →
  filter → comment, inbox triage, buying accounts, following a long task.

Shortcuts the user can type: `/gramgpt:status`, `/gramgpt:launch <what>`,
`/gramgpt:task <task_id>`.

## What to call

| User wants | Tool |
|---|---|
| balance, subscription | `check_balance` |
| accounts, their state | `list_accounts`, `get_account_detail`, `pick_healthy_accounts` |
| account risk score | `check_account_ggr` |
| what an account did, its errors, PeerFlood, spamblocks | `get_account_activity` |
| re-check sessions, spamblock, reauth, new profiles | `launch_account_op` |
| warm accounts up | `launch_warming` |
| join channels / chats | `launch_bulk_join` |
| find channels / groups by keywords, collect users, messages, comments | `launch_parsing` (`kind`) |
| filter channels by size and activity | `launch_check_channels` |
| which links are alive | `launch_check_links` |
| which numbers have Telegram | `launch_check_numbers` |
| who has a story now | `launch_check_stories` |
| saved channel base | `list_channel_base` |
| AI comments in channels | `launch_neuro_commenting` |
| AI chatting in chats | `launch_neuro_chatting` |
| AI replies in the accounts' DMs | `launch_neuro_dialogs`, `set_dialog_ai` |
| promo dialogue in chats | `launch_neuro_shilling_preflight` → `launch_neuro_shilling` |
| reactions on group messages and channel discussion comments (not posts) | `launch_mass_react` |
| story views / likes | `launch_mass_looking` |
| tag users in stories | `launch_story_mentions` |
| add users to a group / channel | `launch_inviter_preflight` → `launch_inviter` |
| add numbers to contacts | `launch_add_contacts` |
| DM / group broadcasts | `launch_spam_pm`, `launch_group_spammer`; live: `pause_task`, `resume_task`, `update_task`, `add_targets`, `remove_targets` |
| read and answer DMs | `read_inbox`, `get_dialog`, `get_media` (attachments, voice transcripts), `reply_in_dm`, `send_media`, `send_reaction`, `send_typing`, `click_button`, `edit_message` |
| tidy chats | `list_folders`, `set_dialog_folder`, `set_folder_order`, `set_dialog_flags`, `block_peer`, `delete_dialog`, `delete_messages` |
| look up a user | `get_peer`, `get_stories`, `resolve_links` |
| projects / roles on accounts | `set_account_project`, `set_account_role` |
| add accounts | `import_accounts` (StringSessions) |
| trash / restore accounts | `delete_accounts`, `restore_accounts` |
| stop a task | `cancel_task` |

## REST only (not MCP tools)

Needs the key in a shell variable — ask the user to `export GRAMGPT_API_KEY=ggk_live_...`
and call with `curl -H "Authorization: Bearer $GRAMGPT_API_KEY"`. Exact fields:
https://gramgpt.io/api/v1/docs/.

- Tasks: `GET /api/v1/tasks/` (filter `?tag=`, `?external_id=`), `/tasks/{id}/logs/`
- Stats: `GET /api/v1/stats/accounts/`, `/stats/activity/`; exports: `/history/`,
  `/history/{module}/`
- Accounts in: `POST /api/v1/accounts/import-tdata/`; login by phone —
  `POST /accounts/auth/start/` (sends the code) → `/auth/verify/` (code, 2FA) or
  `/auth/cancel/`. Accounts out: `POST /accounts/sessions/export/` → poll
  `/sessions/export/{id}/` → `download_url`
- `GET /api/v1/me/`, `/projects/`, `/roles/`
- Proxies: `GET/POST /api/v1/proxies/…` — list, check, attach, detach
- Blocklists: `GET /api/v1/blacklists/`, `GET/POST/DELETE /blacklists/{kind}/`
- Avatar library: `/api/v1/photos/` (upload, `random`, `quota`, `bulk-delete`,
  `bulk-update`, `/{id}/use/`); AI prompts: `/api/v1/prompts/`
- `POST /api/v1/media/` — upload a file for `send_media` or a broadcast `chain`
- Webhooks: `/api/v1/webhooks/`, `/webhooks/{id}/deliveries/`,
  `POST …/deliveries/{delivery_id}/redeliver/`
- What changed: `GET /api/v1/changelog/`

**Marketplace — spends balance, confirm the ids / count and total first:**

- Buy stock: `GET /api/v1/marketplace/stock/`, `/catalog/`, `/pick/`,
  `POST /marketplace/buy/` (≤ 20 ids), `GET /marketplace/purchases/`
- Buy orders, any size: `POST /api/v1/marketplace/orders/` (pass `external_id` so a
  retry doesn't buy twice), `GET /orders/`, `GET`/`DELETE /orders/{id}/`,
  `POST /orders/{id}/export/` to download again
- Exchange (LZT lots, priced for you): `GET /api/v1/marketplace/exchange/` →
  `POST /exchange/buy/` → `GET /exchange/orders/{id}/` (`result.account_id`)
- Sell: `POST /api/v1/marketplace/eligibility/` (what can be listed),
  `GET/POST /marketplace/listings/`, `PATCH`/`DELETE /listings/{id}/`,
  `GET /marketplace/sales/`, `GET /marketplace/complaints/`

Over REST, add `Idempotency-Key: <uuid>` to `POST /api/v1/tools/...` calls so a retry
never runs twice.
