# Changelog

## 1.2.0 — 2026-11-12

- New tool `get_account_activity` — what an account did: actions and errors per
  module, PeerFlood days, spamblock / freeze events. In the tool map, the rules and
  the health-check recipe.
- REST section covers the whole API: login by phone, blocklists, avatar library,
  prompts, projects and roles, webhook redelivery, the LZT exchange and selling on
  the marketplace. Buying recipe falls back to the exchange.
- Rules match the MCP server's: `no_subscription`, `read_only_key`, `quota_exceeded`
  are not fixed by retrying.
- Reference refreshed: MassReact never reacts to channel posts; broadcast `chain`
  items take their own `pause_min` / `pause_max`; `list_accounts` and
  `pick_healthy_accounts` no longer skip `pm_aggregation_enabled` accounts.
- The weekly reference refresh bumps the patch version, so installed plugins
  pick it up.

## 1.1.2 — 2026-11-11

- MCP requests carry `X-Client: gramgpt-plugin/<version>`, so GramGPT can tell plugin
  installs from hand-added MCP connections. No key, account or prompt data is in it.

## 1.1.1 — 2026-11-10

- Key field explains what to paste: the full 41-character key shown once at creation,
  not the short prefix from the key list, without `Bearer`.

## 1.1.0 — 2026-11-10

- Tool reference: one page per tool with every input and `config` key, generated from
  the live API schema; refreshed by CI every Monday.
- Recipes: account health check, warming, find → filter → comment, inbox triage,
  buying accounts, following a long task.
- Commands: `/gramgpt:status`, `/gramgpt:launch`, `/gramgpt:task`.
- `launch_account_op` has no dry run — the skill asks before running it instead.

## 1.0.0 — 2026-11-10

- First release: GramGPT MCP server with the API key asked at install
  (secure storage), skill with working rules and a tool map.
