---
name: digest
description: Use when the user wants the easy-to-read version of a thesis or comparison ("show me the easy version", "digest of NVDA", "summarize the thesis", "explain SPCX in 60 seconds"). Generates a visual one-pager with KPI cards, scenario bars, score meters, callouts, and a timeline — designed to be glanceable, not read.
---

# digest

The digest is the **anti-thesis**: built for catching key takeaways in 60 seconds, not for full study. The thesis remains the source of truth; the digest is a derived, visual view.

## When invoked

User asks for the easy / visual / quick version of a stock's thesis. Examples:
- "show me the easy version of SPCX"
- "digest of NVDA"
- "summarize the SPCX thesis"
- "explain SPCX visually"
- "60-second SPCX"

## Steps

1. **Read `stocks/{TICKER}/thesis.md` and the latest snapshot.** All data comes from the existing thesis — the digest is a presentation transform, not new research. If the thesis is missing, run [[add-stock]] first.

2. **Write `stocks/{TICKER}/digest.md`** using the visual block format below. Almost no prose. Every section uses one of the visual blocks rendered by `scripts/render.py`. Words are reserved for moments of judgment, not exposition.

3. **Render and open in browser:**
   ```bash
   uv run --project scripts scripts/render.py stocks/{TICKER}/digest.md --title "{TICKER} Digest"
   ```

4. **In chat:** one sentence — "Opened {TICKER} digest in browser." Don't restate the digest content.

## Digest format (target: fits on one screen, scannable in 60 seconds)

```markdown
# {TICKER} — {Company} digest

> **One-line thesis.** {The one-line thesis from thesis.md, plain English. The "wrong if X" clause is preserved.}

## Snapshot

\`\`\`kpi
Price | $X | {±%} today
Market cap | $XB | {one-line context}
Revenue (latest) | $XB | {YoY growth %}
{Most-relevant business metric} | {value} | {context, e.g. "12M Starlink subs, +35% YoY"}
\`\`\`

## What it does

{2 short sentences max. Plain English. What the company sells, to whom, and the one thing that makes them different. No jargon.}

## Outlook

\`\`\`scenarios
Bull | {prob%} | ${target} | {one phrase: what has to be true}
Base | {prob%} | ${target} | {what has to be true}
Bear | {prob%} | ${target} | {what has to be true}
\`\`\`

## How I score it

\`\`\`meter
Moat | {0-10} | {one phrase}
Management trust | {0-10} | {one phrase}
Valuation discipline | {0-10} | {one phrase}
Balance sheet | {0-10} | {one phrase}
\`\`\`

## Watch list (next 12 months)

\`\`\`timeline
{YYYY-MM-DD} | {catalyst}
{YYYY-MM-DD} | {catalyst}
{YYYY-MM-DD} | {catalyst}
\`\`\`

## Position

\`\`\`kpi
Target | ${target} | base case
Thesis-break | ${break} | re-read or sell below
Max weight | {X%} | of portfolio
\`\`\`

\`\`\`callout warn
{Single most important risk-or-action sentence. The thing the user needs to remember if they only catch one thing.}
\`\`\`

\`\`\`verdict {hold|add|trim|exit|watch}
{One-phrase verdict. e.g. "Hold; size with valuation discipline."}
\`\`\`

---
_Source: [thesis.md](thesis.md) · last updated {YYYY-MM-DD}_
```

## Score guidance (for the meters)

These are the agent's judgment calls — not the user's. Be calibrated:
- **Moat (0-10):** 9-10 only for textbook process power + scale + switching (NVDA, ASML). 7-8 = strong but contestable. 4-6 = real but narrow. 0-3 = commodity/no moat.
- **Management trust (0-10):** consider voting structure, related-party transactions, ROIC track record, capital allocation discipline. Concentrated control with mixed M&A history = 4-5. Owner-aligned with great track record = 8-9.
- **Valuation discipline (0-10):** 8-10 = trades below or at fair, margin of safety. 5-7 = fairly priced. 1-4 = pricing in the bull case as base; no margin of safety.
- **Balance sheet (0-10):** 9-10 = fortress (net cash, low leverage). 6-8 = healthy. 4-5 = leveraged but serviceable. 0-3 = stress risk.

## Hard rules

- **No new analysis.** The digest is a transform of the thesis, not fresh research. If the thesis is wrong/stale, run [[refresh-thesis]] instead.
- **No jargon-laden tables.** "Reverse-DCF gap" goes into the callout in plain words ("Priced for the bull case to be base") — the meter is "Valuation discipline."
- **Words are emphasis only.** If a section needs more than 2 sentences of prose, that's a sign you should be in the thesis, not the digest.
- **One screen.** A digest that scrolls is a thesis. Cut.
