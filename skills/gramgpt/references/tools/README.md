# Tool reference

61 tools, generated from the live API schema by `scripts/gen_reference.py` — don't edit by hand.

| tool | what it does |
|---|---|
| [`add_targets`](add_targets.md) | Add targets to a running DM/group broadcast. |
| [`block_peer`](block_peer.md) | Block `peer` from `account_id`, or unblock with `unblock: true`. Does not touch the dialog itself. |
| [`cancel_task`](cancel_task.md) | Cancel a ScriptTask. Idempotent. |
| [`check_account_ggr`](check_account_ggr.md) | Run GGR ondemand check on an account. Returns risk score, tier, lifespan-median, top SHAP factors, use-case recommendation. |
| [`check_balance`](check_balance.md) | Read your token wallet balance and active-subscription status (with expiry). |
| [`click_button`](click_button.md) | Press a bot's inline button by `row`/`col` from get_dialog `buttons`; returns the bot's answer. URL buttons are not pressed, their `url` is returned. |
| [`delete_accounts`](delete_accounts.md) | Move accounts to the trash, like Delete in the panel: they leave /accounts/ and free their slots; purged after 2 days unless restored. Requires confirm: true. |
| [`delete_dialog`](delete_dialog.md) | Delete the DM dialog with `peer` from `account_id`'s chat list; `revoke` also wipes it for the other side. |
| [`delete_messages`](delete_messages.md) | Delete our own messages in the DM (up to 100); others' ids are skipped. |
| [`edit_message`](edit_message.md) | Edit the text of our own message in the DM. |
| [`get_account_detail`](get_account_detail.md) | Get one of your Telegram accounts by id (status, spamblock, geo, proxy, timestamps). |
| [`get_dialog`](get_dialog.md) | Read one DM conversation: up to `limit` messages newest-first, older pages via `before_id`, optional `mark_read`. Attachments carry `media_type`/`duration`/`file_name`/`mime_type`/`size`, our messages `read`, bot messages inline `buttons` (for click_button). |
| [`get_media`](get_media.md) | Download a message attachment as a signed 10-min `url` (+ type, duration, size); voice/video notes get Telegram's `transcript` when available. |
| [`get_peer`](get_peer.md) | Profile of a user: names, username, about, premium, stories, birthday, status, personal channel, small photo as a signed `photo_url`. |
| [`get_stories`](get_stories.md) | Active stories of a peer (id, date, type, caption). Does not mark them viewed. |
| [`get_task_progress`](get_task_progress.md) | Read current status + result snapshot of a ScriptTask. |
| [`get_task_results`](get_task_results.md) | Read the full result list of a parser or checker task page by page (same data as GET /tasks/{id}/results/). |
| [`import_accounts`](import_accounts.md) | Import Telegram accounts from Telethon StringSessions (bulk, up to 200). Pass a proxy per account to auto-verify. For tdata, use POST /api/v1/accounts/import-tdata/ (multipart). |
| [`launch_account_op`](launch_account_op.md) | Run a bulk account operation: check, check_spamblock, reauthorize, generate_profiles, appeal_spamblock, set_2fa, reset_sessions (needs confirm: true), privacy, leave_chats, create_channels (a personal channel on each account, public and pinned by default). generate_profiles, create_channels and similar operations skip accounts busy with another task and run on the rest: see `skipped_accounts` and `account_results[].busy_with` in the task result. If every account is busy, the task fails with `account_overlap`. |
| [`launch_add_contacts`](launch_add_contacts.md) | Add phone numbers to the accounts' contacts. |
| [`launch_bulk_join`](launch_bulk_join.md) | Join a list of channels/chats with the given accounts. Optionally collects them into a folder. |
| [`launch_check_channels`](launch_check_channels.md) | Filter a list of channels by size, comments and activity — no joins. |
| [`launch_check_links`](launch_check_links.md) | Check which links/usernames are alive — resolve only, no joins. |
| [`launch_check_numbers`](launch_check_numbers.md) | Check which phone numbers have a Telegram account — feeds the DM broadcaster. |
| [`launch_check_stories`](launch_check_stories.md) | Find which users have an active story right now. |
| [`launch_group_spammer`](launch_group_spammer.md) | Launch the group broadcaster: post a message chain into chats, by target list or folder links. |
| [`launch_inviter`](launch_inviter.md) | Launch the Inviter: add target users into your channel or group — via helpers promoted by the main admin account, or directly as members. |
| [`launch_inviter_preflight`](launch_inviter_preflight.md) | Dry-run the Inviter: destination, main account rights, mode and targets — nothing is joined or invited. |
| [`launch_mass_looking`](launch_mass_looking.md) | Launch MassLooking: view (and optionally like) targets' stories. Honours accountProtectionEnabled / accountProtectionLevel inside config. |
| [`launch_mass_react`](launch_mass_react.md) | Launch MassReact module: accounts react to recent posts in target channels. |
| [`launch_neuro_chatting`](launch_neuro_chatting.md) | Launch NeuroChatting module: accounts hold conversations in target chats. Heavier than NeuroCommenting. |
| [`launch_neuro_commenting`](launch_neuro_commenting.md) | Launch NeuroCommenting module on accounts targeting channels. Returns task_id; poll via get_task_progress. |
| [`launch_neuro_dialogs`](launch_neuro_dialogs.md) | Launch NeuroDialogs: accounts keep AI conversations going in their own DMs. Honours accountProtectionEnabled / accountProtectionLevel inside config. |
| [`launch_neuro_shilling`](launch_neuro_shilling.md) | Launch NeuroShilling: accounts hold a scripted promo dialogue in target chats. |
| [`launch_neuro_shilling_preflight`](launch_neuro_shilling_preflight.md) | Dry-run NeuroShilling targets: which chats are alive and usable — no joins. |
| [`launch_parsing`](launch_parsing.md) | Launch a parser. kind=channels\|groups search by keywords; kind=users\|messages\|comments extract from given targets. |
| [`launch_spam_pm`](launch_spam_pm.md) | Launch the DM broadcaster: send a message chain to a target list. Requires send_mode and chain inside config. |
| [`launch_story_mentions`](launch_story_mentions.md) | Launch Story Mentions: post stories that tag target users, or only open empty dialogs with them. |
| [`launch_warming`](launch_warming.md) | Launch auto-warming module: accounts read dialogs / join channels / scroll feed to simulate organic activity. |
| [`list_accounts`](list_accounts.md) | List your Telegram accounts. Accounts with pm_aggregation_enabled=True are not returned. Optionally filter by status. |
| [`list_channel_base`](list_channel_base.md) | Read your channel base: channels and groups with folders, liveness and filters, to pass into launch_* tools. |
| [`list_folders`](list_folders.md) | List the account's Telegram chat folders in their current order (id, title, kind, peer count). |
| [`mark_account_dead`](mark_account_dead.md) | Mark account as dead. Status set to 'banned', 'deactivated', 'session_revoked', or 'frozen'. |
| [`pause_task`](pause_task.md) | Pause a running DM/group broadcast before its next target. |
| [`pick_healthy_accounts`](pick_healthy_accounts.md) | Return up to N account_ids with status=valid, spamblock clear or unknown (not checked yet), pm_aggregation_enabled=False. MVP: oldest-first ordering. |
| [`read_inbox`](read_inbox.md) | Fetch latest DMs for `account_id` (up to `limit`, newest-first), or for up to 10 accounts at once via `account_ids`. |
| [`remove_targets`](remove_targets.md) | Remove targets from a running DM/group broadcast. |
| [`reply_in_dm`](reply_in_dm.md) | Send a Telegram DM from `account_id` to `peer`. Returns the sent message id. Optional `parse_mode`, `schedule_at` (Telegram scheduled send). |
| [`resolve_links`](resolve_links.md) | Check up to 10 links / @usernames / invite links without joining: kind, title, members, open (false = join by request), comments, parsable. |
| [`restore_accounts`](restore_accounts.md) | Restore accounts from the trash (see delete_accounts); per-account result or reason. |
| [`resume_task`](resume_task.md) | Resume a task paused with pause_task. |
| [`send_media`](send_media.md) | Send a voice / video_note / photo / video / document from `media_id` (POST /media/) or an http(s) `url`. Use Idempotency-Key. |
| [`send_reaction`](send_reaction.md) | Put an emoji reaction on a message in the DM; empty `emoji` removes it. |
| [`send_typing`](send_typing.md) | Show «typing…» / recording voice / video note to `peer` (~5 s; repeat while composing). |
| [`set_account_project`](set_account_project.md) | Assign a panel project to accounts. `project` is a project id, a name (created if you have no project with that name yet), or null to detach. Projects: GET /projects/. |
| [`set_account_role`](set_account_role.md) | Assign a panel role to accounts. `role` is a role id, a name (created if you have no role with that name yet), or null to detach. Roles: GET /roles/. |
| [`set_dialog_ai`](set_dialog_ai.md) | Take one DM dialog away from NeuroDialogs AI (ai_enabled=false) or hand it back — the panel's ✦ button; a running task picks it up at once. |
| [`set_dialog_flags`](set_dialog_flags.md) | Set the DM pinned / unread / archived / muted. |
| [`set_dialog_folder`](set_dialog_folder.md) | Put the DM with `peer` into the folder `folder_name` (created if absent); `remove: true` takes it out. |
| [`set_folder_order`](set_folder_order.md) | Reorder the account's folder tabs by name; first = leftmost. Use "all_chats" for the built-in tab. |
| [`update_task`](update_task.md) | Change a running broadcast's chain, limits and delays without restarting it. |
