---
name: quarterly-review
description: Use after each earnings print to re-score the thesis ("quarterly NVDA", "review NVDA after earnings", "Q2 review"). Re-scores bull/base/bear probabilities, redoes reverse-DCF, updates key metrics, and writes snapshots/reviews/{YYYY-Qn}.md. Appends a quarterly note to thesis.md Stands & Updates.
---

# quarterly-review

## When invoked

User wants a thesis-level re-score after fresh earnings data. Examples:
- "quarterly NVDA"
- "review NVDA after earnings"
- "Q2 review on Palantir"

## Steps

1. **Read existing `thesis.md`, `state.yaml`, `triggers.yaml`.** Identify current bull/base/bear weights and price targets.

2. **Pull current data:**
   ```bash
   uv run --project scripts scripts/fetch.py {TICKER}
   ```

3. **Read the earnings release** if linked from news headlines or available on the company IR site. Use the news section of fetch.py output as a starting point — find the headline link to the release and fetch it. If transcript is paywalled, work from the release alone and note the gap.

4. **Re-score bull/base/bear:**
   - Did the print confirm the bull case, base case, or surface a bear-case risk?
   - Adjust probability weights (must still sum to 100).
   - Update price targets if needed.
   - Write the scoring as plain prose, with old vs new weights side by side.

5. **Redo reverse-DCF.** Compute what current price implies for revenue growth and margins given the new data. If the implied numbers no longer pencil (e.g., requires growth above the historical max), flag it.

6. **Update key metrics with the latest reported numbers.** Plain numerical update.

7. **Write `stocks/{TICKER}/snapshots/reviews/{YYYY-Qn}.md`:**

   ```markdown
   # {TICKER} — Quarterly review {YYYY-Qn}

   ## Earnings summary
   - Revenue: ${X}B vs ${Y}B est ({beat/miss} {%})
   - EPS: ${X} vs ${Y} est
   - Guide: {raised / maintained / cut}
   - Key segment: {segment metric, e.g. DC revenue +94% YoY}

   ## Thesis re-score

   |              | Prior | New |
   |--------------|------:|----:|
   | Bull weight  | 30%   | 35% |
   | Base weight  | 50%   | 50% |
   | Bear weight  | 20%   | 15% |

   What changed: {plain-English why the weights moved}

   ## Reverse-DCF re-run
   At ${current_price}, the market is now pricing in roughly {X}% revenue growth and {Y}% margins. {Plausibility judgment.}

   ## Key metrics — updated
   - {metric}: {value} ({direction vs prior})

   ## Triggers — any updates?
   {Comment on whether thesis-break or kill conditions need editing. Don't auto-edit; suggest if needed.}

   ## Verdict
   {Hold / Trim / Add / Re-read full thesis}, with one-sentence reason.
   ```

8. **Append to `thesis.md` Stands & Updates:**
   ```markdown
   ### {YYYY-MM-DD}  Quarterly review — {YYYY-Qn}
   {2–4 sentence summary of the re-score and verdict. Link to the review file.}
   ```

9. **Update `state.yaml`:** `last_quarterly_review: {YYYY-Qn}`.

10. **Tell the user.** Paths + the verdict line.

## Behavioral guards

- Append-only Stands & Updates. The quarterly entry goes at the bottom, never edits prior entries.
- If reverse-DCF implies numbers no longer plausible, recommend re-reading the full thesis or sizing down — but don't tell the user to sell. Decisions are theirs.
- If the print fundamentally breaks the thesis (a kill condition was hit), say so plainly. Don't soften.
