---
name: find-similar-moves
description: Use when the user wants to compare today's move/news to historical analogs ("how did NVDA react last time HBM news hit?", "show similar moves to today's DRAM run", "any precedent for this kind of SU drop?", "find all earnings_print attributions on TSM"). Queries the attribution index and surfaces cited matches with full context.
---

# find-similar-moves

The attribution index (`attributions/index.jsonl`) is structured memory. Every meaningful past move is tagged and queryable. This skill turns "I think this looks like the last time" into "here are 3 cited precedents."

## When invoked

- "how did {TICKER} react last time {topic}"
- "show similar moves to today's {TICKER}"
- "is there precedent for this {kind of move}"
- "find all attributions tagged X on {TICKER}"
- AUTOMATICALLY at the start of [[deep-dive]] before writing fresh analysis (so today's read can cite past analogs).

## Steps

1. **Translate the question into filters.** The user's English maps to flags on `find_attributions.py`:

   | User intent | Flags |
   |---|---|
   | "Last time NVDA had earnings" | `--ticker NVDA --tag earnings_print` |
   | "Big drops on SU" | `--ticker SU --direction down --magnitude major` |
   | "Memory pricing news on DRAM" | `--ticker DRAM --any-tag memory_pricing,executive_comment` |
   | "Any TSM regulatory event" | `--ticker TSM --any-tag regulatory_positive,regulatory_negative,policy_us,policy_china` |
   | "Recent high-confidence calls" | `--confidence high --since 2026-01-01` |
   | "Major moves across the watchlist" | `--magnitude major --limit 30` |

2. **Run the query:**
   ```bash
   uv run --project scripts scripts/find_attributions.py [flags]
   ```
   Output is JSON, sorted newest-first.

3. **If 0 matches:** say so plainly. "No precedent in the index for {description}. The index has been collecting since {first date}." Suggest the user record today's move so future-them has the precedent.

4. **If matches found:** present them. Format depends on count:
   - **1-3 matches:** inline in chat, with the full primary cause + agent-read for each, and direct links to the snapshot + log.
   - **4-10 matches:** small table in chat (date, ticker, magnitude, primary cause, confidence) + offer to render the full HTML report.
   - **>10 matches:** render to HTML and open. Format with `kpi` strip showing aggregate stats (count, win/loss, avg magnitude) followed by a `compare` table.

5. **Compare today vs. the analog.** Don't just list the past. Pull cross-asset and price data for both today and the matching date, and show the deltas. This is the actual signal:

   ```markdown
   ## Today vs. {past date} ({ticker})

   |                | Today | {past date} | Delta |
   |----------------|------:|------------:|------:|
   | %1d            | +X%   | +Y%         | ...   |
   | Vol ratio      | X.Xx  | Y.Yx        | ...   |
   | SPY %1d        | ...   | ...         | ...   |
   | VIX            | ...   | ...         | ...   |
   | Sector ETF %1d | ...   | ...         | ...   |
   | Primary tag    | ...   | ...         | ...   |

   **What's different.** {1-2 paragraphs distinguishing this setup from the analog.}
   ```

6. **Suggest the next analytical step.** Examples:
   - "Last time this happened, {ticker} ran another +X% over the next {N} days, then gave back Y% on {event}. The current setup looks {similar/different} because {reason}."
   - "The analog was a head-fake — {ticker} dropped 8% in the following week. Worth tightening stops here."
   - "No clean analog. This is novel; record carefully and re-evaluate after the next earnings."

## Hard rules

- **Cite the index entry.** Always include the `(date, ticker)` pair so the user can pull up the original log.
- **Don't pretend to remember.** If `find_attributions.py` returns nothing, the agent has no memory of the event. Say so.
- **Don't extrapolate.** Past analogs are evidence, not predictions. Use phrases like "in the analog, {what happened}" — never "this means X will happen."
- **Update tag vocabulary cautiously.** If you find yourself wanting a new tag for a new query, propose adding it to `attributions/README.md` first; don't silently extend the schema.
