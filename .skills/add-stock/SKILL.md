---
name: add-stock
description: Use when the user wants to start tracking a new stock ("add NVDA", "I want to track Palantir", "research SHOP for me"). Performs a deep investor-grade dive and writes thesis.md, state.yaml, and triggers.yaml for the new ticker.
---

# add-stock

Add a new stock to the workspace. The output is a complete investment memo the user could re-read in 6 months and remember where they stood.

## When invoked

The user has named a ticker or company and wants it tracked. Examples:
- "add NVDA"
- "I want to track Palantir"
- "research SHOP"
- "let's add Hims to the watchlist"

Resolve the company name to a ticker if needed (PLTR for Palantir, etc.). Confirm with the user if ambiguous.

## Steps

1. **Check for duplicate.** If `stocks/{TICKER}/` already exists, ask if the user wants to refresh instead (point to refresh-thesis skill) or overwrite. Do not silently overwrite.

2. **Ask 1–2 clarifying questions.** Skip these only if the user already volunteered the angle.
   - "What's your angle on this stock — what made you want to track it?"
   - If the user mentioned a thesis, skip and use it.

3. **Pull company overview FIRST.** Run:
   ```bash
   uv run --project scripts scripts/fetch_overview.py {TICKER}
   ```
   This is mandatory and non-negotiable. Do NOT trust training-data knowledge for facts that change (status, IPO dates, valuation, executives, ARPU, sub counts, etc.). The overview gives you yfinance profile, Wikipedia summary, 7-day news, and reference links to EDGAR/Macrotrends/StockAnalysis/OpenInsider/WhaleWisdom.

   If a company-specific fact you need isn't in the overview output (e.g., a specific metric like Starlink subscriber count), use WebFetch on the Wikipedia URL or the company IR website from `links.yahoo_profile`. **Always cite the source for time-sensitive facts.**

   **If `profile.quoteType` is ETF, INDEX, or MUTUALFUND**, stop here and dispatch to [[add-tracker]] instead — the thesis schema is wrong for passive/leveraged products.

4. **Pull current pricing data.** Run:
   ```bash
   uv run --project scripts scripts/fetch.py {TICKER}
   ```
   Use the JSON for the Snapshot section (price, market cap, etc.) and to ground the analysis in current reality.

5. **Research the company in depth.** Combine the overview output + pricing data + news headlines + (if needed) WebFetch on Wikipedia/IR/EDGAR. Cover:
   - What the company does (plain English, 2–4 sentences)
   - Industry & TAM
   - Bull / Base / Bear scenarios with rough probabilities (sum to 100) and price targets
   - Moat — use Helmer's 7 Powers as an internal checklist (scale, network, counter-positioning, switching costs, branding, cornered resource, process power) but write the conclusion as a paragraph, not a checklist
   - Management & capital allocation (CEO tenure, ROIC, buyback discipline, M&A track record)
   - Valuation: multiples sanity check (current P/E vs 5-year median + peers) AND a reverse-DCF — compute what growth and margin the current price implies and report it as a sentence ("at $X, the market is pricing in roughly Y% growth and Z% margins")
   - Balance sheet (only flag if there's real risk)
   - Key metrics to watch (3–6 specifics)
   - Catalysts (with dates)
   - Disconfirming events — what would make the user sell

6. **Write `stocks/{TICKER}/thesis.md`** following the schema in the spec (§5). Plain English. Use frameworks behind the scenes; never lecture the reader on terminology.

7. **Write `stocks/{TICKER}/state.yaml`:**
   ```yaml
   ticker: {TICKER}
   active: true
   tags: []  # ask the user if they want tags, or leave empty
   added: {YYYY-MM-DD}
   last_checked: {YYYY-MM-DD}
   last_quarterly_review: null
   last_annual_refresh: {YYYY-MM-DD}  # add-stock counts as the first refresh
   max_weight_pct: null  # leave for the user to fill in
   ```

8. **Write `stocks/{TICKER}/triggers.yaml`** as a pre-commitment device. Propose values based on the thesis, then **explicitly ask the user to confirm or edit**. Reason: pre-commitment only works if the user actually commits.
   ```yaml
   thesis_break_price: null  # propose a value below the bear-case target
   kill_conditions:
     - "..."  # 2-3 events that would make the thesis untenable
   re_read_triggers:
     - "Stock down >15% on no obvious news"
     - "Missed quarter (revenue or EPS)"
     - "..."  # 1-2 stock-specific triggers
   ```

9. **Create `stocks/{TICKER}/snapshots/` directory** (empty for now — first snapshot comes from watchlist).

10. **Generate the digest.** Immediately after writing thesis.md, follow the [[digest]] skill to write `stocks/{TICKER}/digest.md` (the visual one-pager) and render it to HTML. Open the digest, NOT the thesis — the digest is the user's primary view.

11. **Tell the user what was written and what's next.** One line: "Added {TICKER}. Digest open in browser; full thesis at stocks/{TICKER}/thesis.md. Confirm triggers before next check."

## Behavioral guards (apply here)

- Do not ask for or record cost basis or position size in dollars.
- Do not write a "Stands & Updates" entry for the user — that's their voice. Leave the section header in thesis.md and let `update-thesis` handle additions.
- Position section in thesis.md should have target / thesis-break / max-weight only. Never an entry price.

## Output format

After writing files, give the user a 4–6 line summary in chat:
- One-line thesis
- Bull/base/bear probability split
- Reverse-DCF takeaway
- Three numbers to watch
- "Triggers proposed; confirm thesis_break_price and kill_conditions before continuing."
