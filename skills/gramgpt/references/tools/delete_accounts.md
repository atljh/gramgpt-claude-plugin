# delete_accounts

Move accounts to the trash, like Delete in the panel: they leave /accounts/ and free their slots; purged after 2 days unless restored. Requires confirm: true.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | min items `1`, max items `1000` |
| `confirm` | boolean | **required** | Must be true — guards against a stray call. |
