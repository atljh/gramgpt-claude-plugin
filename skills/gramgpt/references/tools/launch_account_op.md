# launch_account_op

Run a bulk account operation: check, check_spamblock, reauthorize, generate_profiles, appeal_spamblock, set_2fa, reset_sessions (needs confirm: true), privacy, leave_chats, create_channels (a personal channel on each account, public and pinned by default). generate_profiles, create_channels and similar operations skip accounts busy with another task and run on the rest: see `skipped_accounts` and `account_results[].busy_with` in the task result. If every account is busy, the task fails with `account_overlap`.

## Input

| field | type | | notes |
|---|---|---|---|
| `op` | `appeal_spamblock` \| `archive_channels` \| `check` \| `check_spamblock` \| `copy_stories` \| `create_channels` \| `create_folder` \| `delete_private_chats` \| `generate_profiles` \| `leave_chats` \| `privacy` \| `reauthorize` \| `reset_sessions` \| `set_2fa` \| `unpin_folders` \| `unpin_personal_channel` | **required** | Which operation to run. |
| `account_ids` | integer[] | **required** | Accounts to operate on. Must belong to the caller.; min items `1` |
| `max_concurrent` | integer |  | Accounts processed at once (worker default if omitted).; min `1` |
| `tags` | string[] |  | Your labels for the task; filter with GET /tasks/?tag=.; max items `20` |
| `external_id` | string |  | Your own id for the task; filter with GET /tasks/?external_id=.; max len `128` |
| `confirm` | boolean |  | Required (true) for reset_sessions. WARNING: on fresh accounts imported from tdata, terminating the other sessions kills our own session too (measured: ~12% of such accounts died with 1-2 foreign sessions present). |
