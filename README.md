# GramGPT for Claude Code

Plugin that connects Claude Code to your [GramGPT](https://gramgpt.io) account:
the MCP server with all GramGPT tools (accounts, GGR, parsers, warming, modules,
task progress) plus a skill with the tool map and working rules — Claude dry-runs
every launch and asks you before anything irreversible.

## Install

1. Create a key: gramgpt.io → Settings → API keys.
2. In Claude Code:

```
/plugin marketplace add atljh/gramgpt-claude-plugin
/plugin install gramgpt@gramgpt
```

Claude Code asks for the key during install and keeps it in secure storage.
Restart Claude Code — the `gramgpt` tools show up in every project.

Change the key later: `/plugin` → gramgpt → configure.

> Already connected GramGPT with `claude mcp add`? Remove that one
> (`claude mcp remove gramgpt -s user`) so the tools don't show up twice.

---

## Установка (RU)

1. Создайте ключ: gramgpt.io → Настройки → API-ключи.
2. В Claude Code:

```
/plugin marketplace add atljh/gramgpt-claude-plugin
/plugin install gramgpt@gramgpt
```

Claude Code спросит ключ при установке и сохранит его в защищённом хранилище.
Перезапустите Claude Code — инструменты GramGPT появятся во всех проектах.

Если раньше подключали через `claude mcp add` — удалите его
(`claude mcp remove gramgpt -s user`), чтобы инструменты не задвоились.

## Docs

- API and MCP: https://gramgpt.io/api/v1/docs/
- What changed: https://gramgpt.io/api/v1/changelog/
