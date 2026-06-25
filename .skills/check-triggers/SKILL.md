---
name: check-triggers
description: Helper skill called from inside watchlist and watchlist. Given a ticker and the latest snapshot data, evaluates triggers.yaml and returns a structured result the caller uses to format alerts. Not typically invoked directly by the user.
---

# check-triggers

## When invoked

Almost always called from another skill (watchlist, watchlist). User can invoke directly with "evaluate triggers for NVDA" — useful when triggers were just edited.

## Inputs

- Ticker
- Latest fetched data (price, change_pct_30d, etc. — from fetch.py JSON)

## Steps

1. **Read `stocks/{TICKER}/triggers.yaml`.** If missing, return `{ "status": "no_triggers" }` and suggest the user run add-stock or refresh-thesis to set them.

2. **Evaluate `thesis_break_price`:**
   - If `price <= thesis_break_price`: status `breach`. Severity 🔥. Message: "Price ${price} is at or below thesis-break ${thesis_break_price}. Re-read thesis or sell."
   - If `price <= 1.05 * thesis_break_price`: status `near`. Severity ⚠. Message: "Price ${price} is within 5% of thesis-break ${thesis_break_price}."

3. **Evaluate `re_read_triggers`** — these are written as natural-language strings, so the agent has to interpret. Common patterns:
   - "Stock down >X% on no obvious news" → check `change_pct_30d` and assess news (was there a clear catalyst?)
   - "Missed quarter" → check whether `last_earnings_eps_actual < last_earnings_eps_estimate`
   - "Cluster insider selling" → out of scope for daily fetch (Tier-2 data)
   - For any trigger that requires data not in the JSON, return `status: "needs_review"` and surface to the user.

4. **Evaluate `kill_conditions`** — these are usually qualitative ("CFO departure under controversial circumstances"). Surface them in the snapshot for the user to evaluate; do not auto-decide.

5. **Return structure:**
   ```yaml
   status: ok | near | breach | needs_review | no_triggers
   severity: 🔥 | ⚠ | ✅
   alerts:
     - kind: thesis_break_near
       message: "..."
     - kind: re_read_trigger
       message: "..."
   ```

## Hard rules

- Never edit `triggers.yaml` from this skill. Triggers are user-committed; only the user can change them.
- If a trigger is ambiguous, surface it to the user — do not assume.
