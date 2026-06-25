---
name: intraday-chart
description: "Intraday line chart showing today's tape with pre/post-market. Use when the user asks: 'show me today's chart', '今天一天的走势', 'intraday', 'minute chart', '分时图', 'pre-market'/'post-market', or wants to analyze how the tape moved within a session. Different from [[chart]] which is 30d daily. Outputs a ```chart``` markdown block; supports multi-ticker overlays."
---

# /intraday-chart

Today's price action (or last 5 days) at minute / 5-min granularity, **including pre-market and post-market**. Use whenever you need to see how a session unfolded — earnings reactions, intraday reversals, post-market gap, etc.

## When to use

- "Show me today's MU chart" / "今天的走势"
- "How did the tape move?" / "盘中怎么走的"
- "Did MU rally hold into the close?"
- "What does post-market look like?" / "盘后什么情况"
- Analyzing intraday reversals, capitulation candles, news reaction
- Comparing intraday correlation between stocks (e.g. MU vs SK Hynix today)

## Difference from [[chart]]

| `chart` (daily 30d) | `intraday-chart` (1d / 5d) |
|---|---|
| One point = one trading day close | One point = 1m/5m/15m bar |
| 30 points typically | 100-400 points typically |
| Use for trend + return | Use for tape reading + session structure |
| No pre/post | **Includes pre-market + post-market** |
| Default for `/morning`, `/watchlist`, `/report` | Used for **today's deep dive** or session analysis |

## Steps

### 1. Generate the chart block

```bash
# Single ticker, today's 5-min bars (default), includes pre/post
uv run --project scripts scripts/build_intraday_chart.py MU --title "MU 今日 intraday"

# Multi-ticker overlay, normalized for comparison
uv run --project scripts scripts/build_intraday_chart.py MU "000660.KS" --normalize --title "MU vs Hynix 今日"

# Higher resolution (1-minute bars) for very recent action
uv run --project scripts scripts/build_intraday_chart.py MU --interval 1m --title "MU 今日 1m"

# Last 5 days at 15m resolution
uv run --project scripts scripts/build_intraday_chart.py MU --interval 15m --period 5d

# No pre/post — just RTH (regular trading hours)
uv run --project scripts scripts/build_intraday_chart.py MU --no-prepost
```

Paste the output into the markdown report.

### 2. Read the summary

`fetch_intraday.py` returns a summary block. Always cite the key numbers:

- `regular_change_pct` — RTH session change (open → 4pm)
- `post_change_pct` — change from RTH close to last post-market print
- `session_high` / `session_low` — full-day range including pre/post
- `regular_high` / `regular_low` — RTH-only range

### 3. Mark the session transitions in commentary

Don't rely on chart alone — call out specifically:
- "Pre-market opened at $X, ranged $Y-$Z"
- "RTH open $X, low $Y at HH:MM (capitulation), close $Z"
- "Post-market: jumped to $X on earnings; settled at $Y"

The chart shows the shape; the commentary explains the structure.

## Interval / period guide

| Use case | Interval | Period |
|---|---|---|
| Today's tape reading | 5m | 1d |
| Earnings reaction (high detail) | 1m | 1d |
| Last week's pattern | 15m | 5d |
| Multi-day swing | 30m | 5d |

Yfinance limits: 1m only for past 7 days; 5m for past 60 days; intervals ≤ 1h for ≤ 30 days.

## Multi-ticker correlations

For correlated names (MU + SK Hynix; SU + WTI; SPY + QQQ), pass multiple tickers + `--normalize`. The chart shows whether they moved together or diverged within the session — useful for confirming "is this idiosyncratic or sector-wide?"

## Hard rules

- **Don't fabricate values.** Always use `build_intraday_chart.py` so data is real.
- **Lead with the summary.** Charts are visual; the user wants the numbers extracted too.
- **Always include pre/post unless the user says RTH only.** That's the whole point — to see the full picture.
- **For news-driven days, run AGAIN after the news.** Intraday is fast-moving; a 14:00 ET chart is stale by 16:30.
- **Don't re-fetch every minute.** Yfinance has rate limits; refetch on demand or every 15-30 min.

## Skill linkage

- [[deep-dive]] — major moves get an intraday chart at the top
- [[brief]] — when summarizing today's action, include an intraday chart
- [[chart]] — for 30d / multi-week views (the other chart skill)
- [[deep-dive]] on earnings days — must include intraday + post-market

## Quick CLI cheatsheet

```bash
# The most common — what did today look like, full session
uv run --project scripts scripts/build_intraday_chart.py MU

# Compare two stocks today
uv run --project scripts scripts/build_intraday_chart.py MU "000660.KS" --normalize

# Just past 30 mins resolution (1m)
uv run --project scripts scripts/build_intraday_chart.py MU --interval 1m
```
