---
name: refresh-thesis
description: Use annually or when the thesis feels stale ("refresh NVDA thesis", "redo PLTR research", "annual review on AMD"). Re-runs the deep-dive from scratch (re-read 10-K, fresh competitive scan, redo reverse-DCF), then merges into thesis.md while preserving Stands & Updates verbatim.
---

# refresh-thesis

## When invoked

The user wants the thesis re-grounded. Examples:
- "refresh NVDA thesis"
- "redo PLTR research"
- "annual review on AMD"
- "is my thesis on SHOP still right"

## Steps

1. **Read existing `thesis.md`** (the whole file). Take note of:
   - The current one-line thesis
   - Bull/base/bear weights
   - Existing Stands & Updates entries (these MUST be preserved verbatim)

2. **Pull fresh company overview FIRST.** Run with `--no-cache` to force a re-pull (annual refresh is exactly when you want fresh data, not cached):
   ```bash
   uv run --project scripts scripts/fetch_overview.py {TICKER} --no-cache
   ```
   Use the overview's profile, Wikipedia summary, news, and reference links. Do NOT trust training data for facts that change. If you need a specific metric, use WebFetch on the linked Wikipedia/IR/EDGAR pages and cite the source.

3. **Pull current pricing data:**
   ```bash
   uv run --project scripts scripts/fetch.py {TICKER}
   ```

4. **Re-research the company from a blank-slate perspective.** Use the fresh overview + news headlines + WebFetch on the latest 10-K from EDGAR (link is in `overview.links.edgar_10k`). Specifically reassess:
   - Industry & TAM — has the market grown / shrunk / changed?
   - Bull / base / bear scenarios — do the old probabilities still hold?
   - Moat — is the 7 Powers picture intact? Any erosion?
   - Management — any changes? Capital allocation track record holding up?
   - Valuation — fresh multiples comparison + reverse-DCF
   - Balance sheet — any new red flags?
   - Key metrics — are the right things still being measured?
   - Catalysts — what's on the calendar for the next 12 months?
   - Disconfirming events — does the kill list still match the risks?

4. **Write a "Refresh delta"** at the top of `stocks/{TICKER}/snapshots/reviews/{YYYY}-annual.md`:

   ```markdown
   # {TICKER} — Annual refresh {YYYY-MM-DD}

   ## What changed in the thesis

   - One-line: {old} → {new, if updated}
   - Probability weights: bull {old}→{new}, base {old}→{new}, bear {old}→{new}
   - Targets: {old → new}
   - Moat: {still intact / weakening / strengthening — and why}
   - Risk profile: {key new risks; killed risks no longer relevant}

   ## Verdict
   {Continue / Reduce conviction / Exit candidate}, with one-sentence reason.
   ```

5. **Rewrite `thesis.md` in place with the updated content.** This is the one place the agent edits an existing thesis section freely (except Stands & Updates, which is append-only).
   - All sections except "Stands & Updates" are rewritten with fresh content.
   - "Stands & Updates" is preserved verbatim. Append a new entry at the bottom noting the refresh.

6. **Append to Stands & Updates:**
   ```markdown
   ### {YYYY-MM-DD}  Annual refresh
   {2-4 sentence summary of the delta. Verdict line. Link to the review file.}
   ```

7. **Review and propose updates to `triggers.yaml`** — but require user confirmation before writing. Propose new thesis_break_price, kill_conditions, re_read_triggers; show diff; ask "apply?"

8. **Update `state.yaml`:** `last_annual_refresh: {YYYY-MM-DD}`.

9. **Tell the user.** Path to refresh file, verdict line, and the proposed triggers.yaml diff.

## Behavioral guards

- **Stands & Updates is sacred.** Never edit, never reorder, only append.
- **No silent triggers.yaml edits.** Always require user confirmation for any change to pre-committed triggers.
- **Be willing to recommend exit.** If the refresh shows the thesis is dead, say so. The point of an annual refresh is to find dead theses.
