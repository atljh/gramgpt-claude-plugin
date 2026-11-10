# set_folder_order

Reorder the account's folder tabs by name; first = leftmost. Use "all_chats" for the built-in tab.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `folders` | string[] | **required** | Folder titles in the wanted order; "all_chats" names the built-in All chats tab.; min items `1` |
