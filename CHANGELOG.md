# Changelog

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
