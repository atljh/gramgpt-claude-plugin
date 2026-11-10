---
description: Launch a GramGPT module safely — pick accounts, dry-run, confirm, start
argument-hint: <module> [what to target, e.g. "warming 10 accounts 2h"]
---

Use the gramgpt skill. The user wants to launch: $ARGUMENTS

1. Map the request to a `launch_*` tool; read `references/tools/<tool>.md` from the skill for its inputs and config.
2. Pick accounts with `pick_healthy_accounts` (or ask which ones).
3. Call the tool with `"dry_run": true`. Show: tool, accounts, targets, key config, `ignored_keys`, skipped accounts and why.
4. Ask for an explicit yes. Only then launch for real, with `tags: ["claude"]`.
5. Report the `task_id` and offer to follow it with /gramgpt:task.

`launch_account_op` has no dry run — describe the operation and ask before running it.
