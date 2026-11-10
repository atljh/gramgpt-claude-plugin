# import_accounts

Import Telegram accounts from Telethon StringSessions (bulk, up to 200). Pass a proxy per account to auto-verify. For tdata, use POST /api/v1/accounts/import-tdata/ (multipart).

## Input

| field | type | | notes |
|---|---|---|---|
| `accounts` | object[] | **required** | min items `1`, max items `200` |
