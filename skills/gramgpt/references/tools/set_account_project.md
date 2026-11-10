# set_account_project

Assign a panel project to accounts. `project` is a project id, a name (created if you have no project with that name yet), or null to detach. Projects: GET /projects/.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | min items `1`, max items `1000` |
| `project` | ['integer', 'string', 'null'] | **required** | Project id, project name, or null to detach. |
