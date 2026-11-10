# set_dialog_ai

Take one DM dialog away from NeuroDialogs AI (ai_enabled=false) or hand it back — the panel's ✦ button; a running task picks it up at once.

## Input

| field | type | | notes |
|---|---|---|---|
| `account_id` | integer | **required** |  |
| `peer` | ['string', 'integer'] | **required** | peer_id, @username or phone |
| `ai_enabled` | boolean | **required** |  |
