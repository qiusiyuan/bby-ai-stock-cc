---
name: weekly-review
description: Use weekly or when user asks for Tier-2 signals ("weekly review", "weekly NVDA", "what's the insider activity", "what changed in 13F"). Pulls insider transactions, 13F filing index, short interest, and analyst-revision context. Writes findings into the next daily snapshot or its own file.
---

# weekly-review

## When invoked

User asks for the slower-cadence signals. Examples:
- "weekly review"
- "weekly NVDA"
- "what's insider activity look like"
- "any 13F changes for AMD"

## Steps

1. **Pick scope.** If a single ticker is named, just that one. If "weekly review" with no ticker, run for all active stocks (parallel).

2. **For each ticker, run the Tier-2 fetchers:**
   ```bash
   uv run --project scripts scripts/fetch_insider.py {TICKER} --days 30
   uv run --project scripts scripts/fetch_13f.py {TICKER}
   ```
   Parse the JSON.

3. **Pull short interest.** v1: include a manual link to FINRA's reg SHO daily files: `https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data` and Nasdaq's bi-monthly short interest page. The agent reads no API for this in v1. If the user wants it filled in, suggest doing it manually or upgrading to Koyfin.

4. **Pull analyst revisions.** v1: open `https://finance.yahoo.com/quote/{TICKER}/analysis` and summarize what's there using a fetch tool — recent estimate revisions, PT changes. If unavailable, surface as a gap.

5. **Write findings** to `stocks/{TICKER}/snapshots/{YYYY-MM-DD}-weekly.md`:

   ```markdown
   # {TICKER} — Weekly review {YYYY-MM-DD}

   ## Insider activity (last 30 days)
   - Form 4 filings: {count}
   - Notable: {plain-English summary, e.g. "CEO bought $2.1M at $138 average — first open-market buy in 18 months"}
   - Filings list: see fetch_insider output JSON or [EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={CIK}&type=4)

   ## 13F context
   - {Latest 13F filings count, link to WhaleWisdom for cross-institution view}
   - {Notable changes if user flags or paid source available}

   ## Short interest
   - {Latest from FINRA / Nasdaq, plain text}

   ## Analyst revisions (last 7 days)
   - {Recent PT changes, ratings revisions if found}

   ## Synthesis
   {1–2 paragraphs. Does insider behavior align with the thesis? Any institutional flow that contradicts the user's view? Are analysts moving in the same direction as the thesis?}
   ```

6. **Update state.yaml** with `last_weekly_review: {YYYY-MM-DD}`.

7. **Tell the user.** Path to the file plus 2–3 line summary per ticker.

## Behavioral guards

- Insider buys (especially clusters) and 13F-superinvestor moves are higher-signal than analyst revisions. Weight the synthesis accordingly.
- Don't over-interpret a single insider trade — small option-grant exercises happen routinely.
- Surface gaps honestly: "Short interest data not pulled in v1 — see manual link above."
