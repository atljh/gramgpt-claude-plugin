# launch_bulk_join

Join a list of channels/chats with the given accounts. Optionally collects them into a folder.

Also takes the common launch options — `dry_run`, `skip_unavailable`, `queue_if_busy`, `strict_config`, `tags`, `external_id` (see SKILL.md).

## Input

| field | type | | notes |
|---|---|---|---|
| `account_ids` | integer[] | **required** | Accounts to run with. Must belong to the caller.; min items `1` |
| `channels` | string[] |  | Channels/chats to join. |

## config

Module config. Knobs: channels, delay_min / delay_max, distribution, per_account_count, shuffle_channels (random split and join order), create_folder, folder_name, folder_append (folder with this name exists: add the new chats to it instead of replacing them), discussion_mode (off \| also: join each channel AND its discussion group, pass its captcha, check the account can write there \| only: the discussion group without subscribing to the channel — saves the 500-channel limit; private invite channels are joined anyway). Per-chat outcome: result channel_outcomes.discussion_ready / discussion_failed / discussion_none.

| field | type | | notes |
|---|---|---|---|
| `allow_spamblock` | boolean |  | Also run the selected accounts that are in spamblock (off by default). Only accounts listed in account_ids are affected. |
