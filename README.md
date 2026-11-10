# GramGPT for Claude Code

[![validate](https://github.com/atljh/gramgpt-claude-plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/atljh/gramgpt-claude-plugin/actions/workflows/validate.yml)

Run your [GramGPT](https://gramgpt.io) Telegram accounts from Claude Code: check
account health, run parsers and checkers, warm accounts up, launch modules, follow
tasks — in plain words.

- **MCP server** — all 60+ GramGPT tools, authorised with your API key.
- **Skill** — working rules (dry-run every launch, confirm before anything
  irreversible), a tool map, recipes and a full reference of every tool's inputs,
  regenerated weekly from the live API schema.
- **Commands** — `/gramgpt:status`, `/gramgpt:launch`, `/gramgpt:task`.

## Install

1. Create a key: gramgpt.io → Settings → API keys.
2. In Claude Code:

```
/plugin marketplace add atljh/gramgpt-claude-plugin
/plugin install gramgpt@gramgpt
```

Claude Code asks for the key during install and keeps it in secure storage.
Restart Claude Code — the tools show up in every project.

Change the key later: `/plugin` → gramgpt → configure. Update the plugin:
`/plugin marketplace update gramgpt`.

> Connected GramGPT before with `claude mcp add`? Remove it
> (`claude mcp remove gramgpt -s user`) so the tools don't show up twice.

## What to ask

- "How are my accounts doing?" → `/gramgpt:status`
- "Warm up 10 fresh accounts for two hours"
- "Find crypto channels with open comments, filter out dead ones, show me the list"
- "Start NeuroCommenting on these channels with accounts from the 'crypto' project"
- "What's unread in the inbox of accounts 12 and 15? Draft replies"
- "Follow task 3f2c… and tell me when it's done" → `/gramgpt:task 3f2c…`

Claude dry-runs every launch, shows the plan and asks before starting it. It also
asks before deleting, cancelling, buying or sending anything in your name.

## What's inside

```
.claude-plugin/         plugin + marketplace manifests
.mcp.json               https://gramgpt.io/mcp/ with your key
skills/gramgpt/
  SKILL.md              rules, tool map, REST-only endpoints
  references/recipes.md tested call chains
  references/tools/     one file per tool: inputs, config keys, defaults, limits
commands/               /gramgpt:status, /gramgpt:launch, /gramgpt:task
scripts/gen_reference.py  regenerates references/tools from the public OpenAPI
```

`references/tools/` is generated — don't edit it by hand. Run
`python3 scripts/gen_reference.py` (stdlib only). CI does this every Monday.

## Other clients

Claude Desktop, Cursor, n8n: server `https://gramgpt.io/mcp/` with header
`Authorization: Bearer ggk_live_…` — configs in the
[docs](https://gramgpt.io/api/v1/docs/). The server sends its working rules on
connect, so any MCP client gets them.

---

## По-русски

Плагин подключает Claude Code к вашему аккаунту GramGPT: MCP со всеми
инструментами, скилл с правилами и справочником, команды `/gramgpt:status`,
`/gramgpt:launch`, `/gramgpt:task`.

1. Создайте ключ: gramgpt.io → Настройки → API-ключи.
2. В Claude Code:

```
/plugin marketplace add atljh/gramgpt-claude-plugin
/plugin install gramgpt@gramgpt
```

Ключ спросят при установке и сохранят в защищённом хранилище. Перезапустите
Claude Code. Перед каждым запуском Claude делает dry-run и спрашивает
подтверждение. Перед удалением, покупкой или отправкой от вашего имени тоже.

Подключали раньше через `claude mcp add` — удалите его
(`claude mcp remove gramgpt -s user`), иначе инструменты задвоятся.

## Links

- API and MCP docs: https://gramgpt.io/api/v1/docs/
- API changelog: https://gramgpt.io/api/v1/changelog/
- Privacy: https://gramgpt.io/privacy
