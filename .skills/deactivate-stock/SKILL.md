---
name: deactivate-stock
description: Use when the user is done tracking a stock for now ("I'm done with SHOP", "deactivate PLTR", "drop NVDA from the dashboard"). Flips state.yaml.active to false. The folder stays in place — nothing is deleted or moved. Reactivate by running this skill again or saying "reactivate".
---

# deactivate-stock

## When invoked

The user wants a stock excluded from `watchlist` / dashboard but doesn't want to delete the history. Examples:
- "I'm done with SHOP"
- "drop PLTR from the dashboard"
- "deactivate AMD"

To reactivate:
- "reactivate NVDA"
- "I'm watching SHOP again"

## Steps

1. **Find the ticker.** If `stocks/{TICKER}/` doesn't exist, tell the user it's not tracked.

2. **Read `state.yaml`.**

3. **Flip the `active` flag** (true → false, or false → true if reactivating). Write it back.

4. **Append a dated entry to thesis.md "Stands & Updates"** noting the change:
   ```markdown
   ### {YYYY-MM-DD}  {Deactivated / Reactivated}
   {Optional 1-line reason if the user gave one.}
   ```

5. **Confirm in chat.** "{TICKER} is now {inactive / active}. Folder stays at stocks/{TICKER}/. It {will / won't} appear in watchlist."

## Hard rules

- **Do not delete or move the folder.** The user's history is sacred.
- **Do not flip flags silently.** Always append the Stands & Updates entry so the deactivation is visible in the log.
- Inactive stocks are still callable via `watchlist {TICKER}` and `refresh-thesis` — the flag only affects `watchlist`.
