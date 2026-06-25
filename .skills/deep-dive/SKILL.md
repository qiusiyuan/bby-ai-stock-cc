---
name: deep-dive
description: Use when the user wants to know WHY a stock moved today, not just the number ("why is NVDA up", "what's driving DRAM", "explain SU's drop", "attribute today's move", "find sentiment on SPCX"). Searches news + online sentiment, attributes the move with cited sources, and distinguishes facts from inferences.
---

# deep-dive

Generic skill: explain a stock's price action with cited sources, not vibes. The user wants signal, not numbers.

## When invoked

- "why is NVDA up today"
- "what's driving DRAM"
- "explain SU's drop"
- "attribute today's move on TSM"
- "find what people are saying about SPCX"
- AUTOMATICALLY when running `watchlist`, `watchlist`, or any watch report and a stock has moved >3% on the day OR >10% in 5 days OR has unusual volume (>1.5× avg).

## Steps

1. **Pull current quote + news.** `uv run --project scripts scripts/fetch.py {TICKER}` returns 72h headlines from Yahoo RSS. That's the starting set.

2. **Pull sector context.** Get the sector ETF's day move and the macro line (SPY, VIX, 10Y, oil if energy). Distinguish **stock-specific** drivers from **sector** or **macro** drivers. A stock can be up because the whole sector is up — that's a different story than a company-specific catalyst.

3. **Pull commodity / cross-asset reads when relevant.**
   - Energy stocks → check WTI (`CL=F`), USO ETF, oil-services indices
   - Memory/chip stocks → check competitor moves (MU, AVGO), HBM news, Apple/hyperscaler signals
   - Auto stocks → check competitor delivery numbers, recall news
   - Bank stocks → check the 10Y curve, credit spreads
   - Recently-IPO'd stocks → check lock-up math, index inclusion timing, post-IPO float dynamics

4. **WebFetch the most-relevant headlines** — but expect 30-50% of Yahoo article URLs to 404 (they expire fast). Fall back to:
   - Wikipedia for company-specific structural facts
   - Motley Fool (`www.fool.com` — usually durable)
   - SEC EDGAR for filings
   - Issuer pages (e.g. globalx.ca for the ETF)
   - Reuters / Bloomberg / CNBC mirrors when accessible

5. **Search sentiment when asked.** For "what people say":
   - Try Reddit search via Google: `site:reddit.com {TICKER} {topic}`
   - Try Stocktwits: `stocktwits.com/symbol/{TICKER}` — note this is sentiment data, treat with skepticism
   - Don't pretend to have access to private posts or paywalled content

6. **Synthesize attribution with explicit confidence levels.** Use this structure:

   ```markdown
   ## What moved {TICKER} today  ({±%} on the day, {±%} 5d)

   ### Direct catalysts (cited)
   - **{Headline}** — {source} [link]. {1-line summary}.
   - **{Headline}** — {source} [link].

   ### Sector / macro context
   - {Sector ETF} {±%} today; {macro factor (oil, rates, dollar, geopolitics)}.

   ### What investors are saying (sentiment)
   - {Direct quote from article / forum / sentiment source}, attributed.

   ### My read (inferred — not cited)
   {1-2 short paragraphs distinguishing what's clearly happening (cited above) from your interpretation of why it matters.}

   ### Confidence
   - **High:** {direct catalyst with clean attribution}
   - **Medium:** {sector / macro driver but not company-specific}
   - **Low:** {flows / sentiment / unattributable}
   ```

7. **NEVER fabricate sources.** If a URL 404s, say "Article URL no longer accessible — falling back to Wikipedia / Fool / etc." If sentiment isn't accessible (paywall, login required, blocked), say so plainly.

8. **PERSIST the attribution.** After producing the analysis, record it to memory. This is mandatory whenever the move clears the threshold. Build a JSON object matching the schema in `attributions/README.md` and pipe it to:

   ```bash
   uv run --project scripts scripts/record_attribution.py
   ```
   (reads JSON from stdin)

   This atomically:
   - Appends to `stocks/{TICKER}/attributions.md` (human-readable log, replaces today's entry if re-run)
   - Upserts the matching JSON line to `attributions/index.jsonl` (queryable index, keyed by date+ticker)

   **Tag discipline.** Use ONLY tags from the vocabulary in `attributions/README.md`. If nothing fits, use `unattributed`. Inventing new tags pollutes the index.

   **Confidence honesty.** `high` = direct cited catalyst. `medium` = sector/macro driver but not company-specific. `low` = flows/sentiment/unattributable. Don't inflate.

9. **Output rule.**
   - **Inline in chat** for single-stock quick attribution if the answer is short (≤8 lines).
   - **Append to today's per-day file** for multi-stock attribution reports or anything with tables / multiple sources:
     - Open or create `dashboard/{YYYY-MM-DD}.md`
     - Append a new `## Attribution` H2 section (if one already exists from earlier today, replace it in place — same rule as morning)
     - Use H3 (`###`) for ticker-level subsections inside the Attribution block
     - Re-render the per-day file:
       ```bash
       uv run --project scripts scripts/render.py dashboard/{YYYY-MM-DD}.md --title "{YYYY-MM-DD}"
       ```
     The renderer auto-generates browser tabs from each H2 in the day file. The user sees one URL per day, growing tabs as the session progresses, instead of one new browser tab per skill.

10. **When a similar setup appears later, query first.** Before writing fresh analysis, run [[find-similar-moves]] to surface analogs from history. The agent gets smarter as the index grows. Cite past analogs in new attributions where relevant.

## Hard rules

- **Cite. Always.** A claim without a source is worth nothing in this skill. If you can't cite, say so.
- **Distinguish stated from inferred.** "Reuters said X" ≠ "I think X happened because of Y." Both are useful — but they get different weight.
- **Don't overweight retail sentiment.** Reddit/Stocktwits is what retail thinks now. It is rarely the explanation.
- **Volume matters.** A 5% move on 0.5× volume is a different story than 5% on 2× volume. Note volume in the attribution.
- **Distinguish the move's CAUSE from its CONFIRMATION.** If TSM is up 7% and AVGO is up 6% on the same day, neither caused the other; both reacted to the same underlying signal. Identify the signal.
- **For ETF moves, attribute to the largest holdings' moves.** DRAM up 9% likely tracks SK Hynix / Samsung / Micron's moves — pull each holding's day to confirm.

## Skill linkage

- Called automatically from [[watchlist]] and [[watchlist]] when threshold conditions hit (>3% day, >10% 5d, vol >1.5×).
- Called directly when user asks "why" / "what's driving" / "explain" / "attribute" / "what are people saying".
- Findings get appended as a `## Attribution` H2 section in `dashboard/{YYYY-MM-DD}.md` (auto-rendered as a tab). Per-stock snapshot under `stocks/{TICKER}/snapshots/{date}.md` still gets the same content under `## Attribution` for stock-level lookup.
