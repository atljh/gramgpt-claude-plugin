# launch_spam_pm

Launch the DM broadcaster: send a message chain to a target list. Requires send_mode and chain inside config.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `targets` | any[] |  | Raw target identifiers (@username, phone or id), or {peer, account_id} to pin a target to one of account_ids (the next message then goes from the same account into the same dialog). Unpinned strings are spread round-robin. |
| `chain` | object[] |  | Message items sent in order to each target. Shapes: {"type": "text", "text"}; {"type": "photo"\|"video"\|"gif"\|"voice"\|"document", "media_url", "text" (caption, optional)}; {"type": "video_note", "media_url"}; media_url is a public http(s) link or "gg-media:<media_id>" for a file uploaded via POST /api/v1/media/ (needed for voice and video_note); {"type": "inline_bot", "post_id"} sends a post with URL buttons via the GramGPT inline bot. post_id is the UUID of an Inline post saved in the panel (DM broadcaster, message type «Inline-пост»). Add "bot_username" (e.g. "PostBot" or the client's own bot) to send via a third-party inline bot instead: post_id is then the inline query, the first result is sent; {"type": "forward", "post_link"} forwards a channel/group post (t.me/<channel>/<id> or t.me/c/<id>/<id>) with the "Forwarded from" header — the account must see the source. Any item may add "pause_min"/"pause_max" (seconds, 0..600): its own pause before that item instead of inter_msg_delay_*; one bound = fixed. Items 2+ always; item 1 only in send_mode=trigger (pause after the person replies). |
| `send_mode` | `direct` \| `trigger` |  | direct — send the whole chain now; trigger — wait for a reply. |

## config

Module config. Required inside it: `send_mode` (direct\|trigger) and `chain` (list of message items; or `chain_variants`). Knobs: work_mode, max_messages, concurrent_sends, greeting (trigger mode), min_delay_seconds / max_delay_seconds / unwarmed_pace_factor, accountProtectionEnabled / accountProtectionLevel, plus the schedule and daily-plan keys below. Waiting (schedule, daily plan, followups) is bounded by the task lifetime of 48 h; a multi-day campaign is relaunched daily.

| field | type | | notes |
|---|---|---|---|
| `accountProtectionEnabled` | boolean |  | Enable AI Account Protection (requires the paid module). |
| `accountProtectionLevel` | `careful` \| `balanced` \| `aggressive` |  | Protection level; defaults to balanced. |
| `min_delay_seconds` | integer |  | Min pause between targets, seconds (default 30). |
| `max_delay_seconds` | integer |  | Max pause between targets, seconds (default 90). |
| `unwarmed_pace_factor` | number |  | Auto-throttle for accounts younger than 14 days: the pause between targets is multiplied by this (default 2.0). Pass 1 to disable it and keep the delays exactly as given. |
| `start_at` | string |  | ISO-8601: the task waits until then before the first send. |
| `stop_at` | string |  | ISO-8601: no new targets after it; the task ends. |
| `active_hours_start` | integer |  | Working window start hour 0-23 (with active_hours_end). |
| `active_hours_end` | integer |  | Working window end hour 1-24, exclusive; 22→6 = overnight. |
| `days_of_week` | integer[] |  | ISO weekdays to work on: 1=Mon … 7=Sun. |
| `timezone` | string |  | IANA timezone of the schedule and of the daily plan (default Europe/Moscow). |
| `daily_limit_per_account` | integer |  | New targets per account per day. On reaching it the task waits for the next day instead of failing. Replies and followups don't count. |
| `daily_limit_total` | integer |  | New targets per day across all accounts of the task. |
| `ramp` | object |  | {start, step_per_day, max}: per-account daily limit = start + step_per_day × account age in days, capped by max. |
| `followups` | object[] |  | [{after_hours, if: "no_reply", chain}] — nudge those who did not reply, from the same account in the same dialog. after_hours counts from the previous touch, max 47. |
| `chain_variants` | object[] |  | [{weight, chain}] — A/B test: each target gets one weighted variant; its index (from 0) is in history.variant and in dm.received.variant. |
| `skip_already_messaged` | boolean |  | Skip targets any of your accounts already messaged (default true). |
| `skip_contacted_days` | integer |  | Limits skip_already_messaged to the last N days; ignored when skip_already_messaged is false. |
| `notify_on_reply` | boolean |  | Ping the owner in the GramGPT Telegram bot on a target's first reply. |
| `delete_negative_replies` | boolean |  | Delete the dialog on the account's side when the target's first reply is negative (stop/spam/abuse); no chain is sent to them. |
| `positive_reply_folder` | boolean |  | Put dialogs with a positive first reply into a Telegram folder. |
| `positive_reply_folder_name` | string |  | Folder title for positive replies (default "Отклики").; max len `12` |
