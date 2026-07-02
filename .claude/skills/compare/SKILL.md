---
name: compare
description: Use when the user wants a side-by-side ("compare NVDA vs AMD", "which of my AI stocks looks best", "rank my semi names"). Reads multiple theses + latest snapshots and writes a comparison.
---

# compare

## When invoked

User wants a cross-stock view at the thesis level. Examples:
- "compare NVDA vs AMD"
- "which of my AI stocks looks best right now"
- "rank my semi names by conviction"

## Steps

1. **Resolve the set.** Either explicit tickers ("NVDA vs AMD") or a tag-based filter ("AI stocks" → all active stocks with tag `ai` in state.yaml).

2. **For each, read:**
   - `stocks/{TICKER}/thesis.md`
   - `stocks/{TICKER}/state.yaml`
   - The latest snapshot in `stocks/{TICKER}/snapshots/` (most recent dated file)

3. **Optional fresh-pull.** If the latest snapshot is more than 7 days old, ask the user: "Snapshots are old — pull fresh data first?" Run watchlist on each if confirmed.

4. **Write a comparison report and open in browser.** Comparisons are always reports — render them. Append a `## Compare {A} vs {B}` H2 section to today's per-day file `dashboard/{YYYY-MM-DD}.md` (create the file with `# {YYYY-MM-DD}` if it doesn't exist; replace an existing same-titled H2 in place — the rule is the same across all skills). Use H3/H4 for inner structure. Then re-render the day file:
   ```bash
   uv run --project scripts scripts/render.py dashboard/{YYYY-MM-DD}.md --title "{YYYY-MM-DD}"
   ```
   In chat: just the verdict line + "Opened comparison in browser." Exception: if the user asks for "just the verdict" or "one-liner", skip the file and reply in chat.

   ```markdown
   # Comparison — {TICKER A} vs {TICKER B}  ({YYYY-MM-DD})

   |                  | {A} | {B} |
   |------------------|-----|-----|
   | One-line thesis  | ... | ... |
   | Bull/base/bear   | 30/50/20 | 25/55/20 |
   | Price vs break   | $X (8% above) | $Y (1% above ⚠) |
   | P/E forward      | ... | ... |
   | Reverse-DCF gap  | "implies 25% growth, plausible" | "implies 20% growth, tight" |
   | Moat strength    | high (process power + switching) | medium (scale only) |
   | Catalysts in 90d | ... | ... |
   | Last quarter     | beat | in-line |
   | Stands trend     | bullish | neutral |

   ## Synthesis

   {2–4 paragraphs. Which one has the better risk/reward at current prices? Where are the theses diverging? Any stock that's clearly "dead to me" by its own kill conditions? Acknowledge what you can't see (cost basis, sizing decisions).}

   ## Verdict
   {If user asked "which looks best": one explicit pick with the reasoning. If they asked for comparison only: short summary, no pick.}
   ```

5. **Behavioral guards.**
   - The comparison must reference each stock's *own* thesis, not a generic frame. NVDA's bear case isn't "AI cools"; it's whatever the user wrote.
   - Don't compare on cost basis or P&L (workspace doesn't track them anyway).
   - If a kill condition has been hit on one of the stocks, surface it loudly even if the user didn't ask.
