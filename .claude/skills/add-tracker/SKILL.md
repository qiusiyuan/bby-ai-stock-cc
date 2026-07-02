---
name: add-tracker
description: Use when adding an ETF, index, or leveraged product to the watchlist (anything that's not a single-company equity). Examples - "add QQQ", "track ^GSPC", "add SQQQ". Writes a lighter tracker.md format (no bull/base/bear, no moat, no reverse-DCF) plus state.yaml. Equities still use add-stock.
---

# add-tracker

ETFs and indexes don't fit the company-thesis schema. They have no management team, no moat, no balance sheet of their own. The tracker format captures what actually matters for passive/index/leveraged exposure: **what it tracks, why it's in the watchlist, what to watch.**

## When invoked

- "add QQQ" / "track ^GSPC" / "add SQQQ to index group"
- Or: from inside add-stock, when fetch_overview returns `quoteType: ETF | INDEX | MUTUALFUND`, dispatch to this skill instead.

## Steps

1. **Pull overview + quote:**
   ```bash
   uv run --project scripts scripts/fetch_overview.py {TICKER}
   uv run --project scripts scripts/fetch.py {TICKER}
   ```

2. **If quoteType is EQUITY, redirect to [[add-stock]].** Tracker format is for ETFs/indexes/funds only.

3. **Write `stocks/{TICKER}/tracker.md`:**

   ```markdown
   # {TICKER} — {Long name}

   > **What it is.** {1-2 sentences. ETF/index, what it tracks, weighting method, expense ratio if known. For leveraged products: state the leverage, the rebalance cadence, and the decay risk plainly.}

   ## Snapshot

   \`\`\`kpi
   Price | ${price} | {±%} today
   YTD | {±%} | vs S&P {±%}
   AUM | ${X}B | (or "—" for indexes)
   Expense ratio | {0.X%} | (or "—" for indexes)
   \`\`\`

   ## Why I'm watching
   {Plain English: what role this plays in your watchlist. Examples: "broad-market read", "Nasdaq sentiment", "energy sector pulse", "hedge instrument", "shorting vehicle".}

   ## Top exposures
   {Top 5-10 holdings if it's an ETF; top sectors/components if an index. Bullet list. Use Yahoo profile or issuer page.}

   ## Key levels to watch
   - Support: ${X}
   - Resistance: ${Y}
   - 52w range: ${low} – ${high}

   ## Risks specific to this product
   {Leveraged-product decay if applicable. Tracking error. Concentration. Currency. Geographic. Liquidity. One short paragraph.}

   ## Stands & Updates  (append-only)
   ### {YYYY-MM-DD}  Initial add
   {Optional context.}
   ```

4. **Write `stocks/{TICKER}/state.yaml`:**
   ```yaml
   ticker: {TICKER}
   asset_type: etf  # or 'index' or 'fund'
   active: true
   tags: []  # set from groups.yaml membership
   added: {YYYY-MM-DD}
   last_checked: {YYYY-MM-DD}
   ```

5. **No triggers.yaml.** Trackers don't have thesis-break levels — they're not theses. Skip.

6. **No digest.md.** Trackers are already short. The tracker IS the digest.

7. **Render and open:**
   ```bash
   uv run --project scripts scripts/render.py stocks/{TICKER}/tracker.md --title "{TICKER} tracker"
   ```

8. **Tell the user.** One line: "Added {TICKER} as {ETF/index}. Open in browser."

## Hard rules

- Trackers do NOT get thesis.md, digest.md, or triggers.yaml. They're not theses.
- For leveraged products (2x/3x/short), the "What it is" section MUST mention decay/rebalance/path-dependence. Don't soft-pedal this.
- ETFs holding the same name as a tracked equity (e.g. you own NVDA and SOXX): note the overlap in "Why I'm watching".
