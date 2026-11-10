# set_account_role

Assign a panel role to accounts. `role` is a role id, a name (created if you have no role with that name yet), or null to detach. Roles: GET /roles/.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | min items `1`, max items `1000` |
| `role` | ['integer', 'string', 'null'] | **required** | Role id, role name, or null to detach. |
