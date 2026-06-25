---
name: update-thesis
description: Use when the user is recording an evolving view on a tracked stock ("I'm bullish on NVDA after earnings", "I'm worried about PLTR competition", "moved to neutral on AMD"). Appends a dated entry to thesis.md "Stands & Updates" section. NEVER edits prior entries.
---

# update-thesis

## When invoked

User volunteers a stand, view shift, or new piece of information about a tracked stock. Examples:
- "I'm bullish on NVDA after earnings"
- "I'm worried PLTR's growth is decelerating"
- "Trimmed my view on AMD — competitive pressure"
- "Reading the Hims 10-K, more confident in the LTV story"

If the user is *checking* the stock, not stating a view, use watchlist instead.

## Steps

1. **Identify the ticker.** If ambiguous ("the AI stock"), ask which.

2. **Read existing `stocks/{TICKER}/thesis.md`.** Find the `## Stands & Updates` section. If it doesn't exist (legacy thesis), append it at the very bottom.

3. **Capture the user's view in their own words.** Don't editorialize. If the user said "bullish after earnings," don't expand to "extremely bullish given the magnitude of the beat" — write what they said and add at most one sentence of context.

4. **Append a dated entry.** Format:
   ```markdown
   ### {YYYY-MM-DD}  {tone tag — Bullish / Bearish / Neutral / Risk flag / Note}
   {1–4 sentences. The user's view, in their voice. Optional one-sentence context line citing the news/event/snapshot that prompted it.}
   ```

5. **Cross-check against triggers.** If the user's stand contradicts the thesis (e.g., they said "bearish on NVDA" but `triggers.yaml` doesn't reflect this), ask: "Want me to update `triggers.yaml` (kill conditions / thesis-break) to match?" Don't edit triggers without confirmation.

6. **Confirm in chat.** Print: "Appended {date} {tone} entry to {TICKER} thesis."

## Hard rules — these cannot be violated

1. **Append-only.** Never edit prior entries in "Stands & Updates". Even typos. Even if the user contradicts an old entry — append a new one, leave the old.
2. **No agent commentary in the user's voice.** If the agent has its own analytical view, that goes in a `watchlist` snapshot, not in Stands & Updates.
3. **No cost basis.** If the user says "I'm down 12% on NVDA" — record the sentiment, not the number.
