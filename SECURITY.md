# Security

Found a vulnerability in this plugin or in the GramGPT MCP server? Please report it
privately: **Security → Report a vulnerability** on this repository. Don't open a
public issue.

If your API key leaked, revoke it right away at gramgpt.io → Settings → API keys and
create a new one; then run `/plugin configure gramgpt@gramgpt`.

The plugin stores the key only in Claude Code's secure storage and sends it only to
`https://gramgpt.io/mcp/`.
