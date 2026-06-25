---
name: chart
description: "Line chart block — the canonical way to show daily price action. Use whenever a report shows price/return movement for one or more tickers. Replaces verbose '1d/5d/30d' text grids in KPI/compare blocks. Triggers: '加 chart', 'show chart', 'plot', '画图', '走势图', or any time you'd otherwise list prices over time. Also used internally by /pulse, /watchlist, /report — every per-ticker tab should lead with a chart."
---

# /chart

A `chart` markdown block is the standard daily-price visualization. Inline SVG line chart, multi-series, dark-theme aware, dates on x-axis, % return in legend. **Use it instead of text-only price grids whenever the report contains prices that move over time.**

## When to use

- Daily report — top of any per-ticker tab (MU, TSLA, etc.) shows a 30d chart
- Compare reports — multi-series chart for "MU vs SK Hynix" / "AI memory cluster"
- Macro / pulse — DXY/USD-CAD/USD-RMB or SPY/QQQ/VIX over 30d
- Any time the user asks "show me X over time"
- Whenever you would otherwise write `Price | $X | +Y% 1d / +Z% 30d` — that grid is obsolete; chart-first

## Markdown format

```
```chart
@title 标题文字 (optional)
@xlabels 06-01,06-02,06-03,... (optional; if omitted shows t0/tN)
Label1 | v1,v2,v3,... | optional note
Label2 | v1,v2,v3,... | optional note
```
```

**Rules:**
- First column = series name (will color-coded in legend)
- Second column = comma-separated values (no spaces required)
- Third column (optional) = note shown next to legend item
- Up to 7 series per chart (then colors cycle)
- All series should have the same x-axis length when possible

## Generating data — use `build_chart.py`

The helper script wraps `fetch.py` + formats the markdown block:

```bash
# Single ticker
uv run --project scripts scripts/build_chart.py MU --title "MU 30d"

# Multi-ticker, rebased to 100 for return comparison
uv run --project scripts scripts/build_chart.py MU "000660.KS" TSM --normalize --title "AI memory 30d returns"

# Reuse already-fetched JSON (no re-fetch — fast)
uv run --project scripts scripts/build_chart.py --from-json /tmp/m_MU.json /tmp/m_NVDA.json --title "..."
```

Paste the output directly into the markdown report.

## When to normalize

- **Normalize (`--normalize`)** when comparing **multiple tickers with very different prices** (e.g. MU $1,048 vs Hynix ₩2,580,000). Rebase to 100 → chart shows pure % return.
- **Don't normalize** when showing **single ticker** or **same-asset class** (e.g. SPY vs QQQ are both ~$700, comparable as-is).

## Skill linkage

- [[pulse]] — every pulse report should include 1 macro chart: SPY/QQQ/VIX 30d
- [[watchlist]] / [[report]] — every per-ticker tab leads with a chart, then KPIs/news below
- [[deep-dive]] — chart at top, possibly two charts (price + comparable peer)
- [[compare]] — chart is the primary visual; --normalize is the default

## Backward compatibility — when to keep KPI/compare

Keep `kpi` and `compare` blocks for:
- Snapshot-style "current numbers" without time dimension (vol_ratio, P/E, market cap)
- Categorical comparisons (Bull threshold vs Bear threshold, support vs press)
- Threshold lists (阈值穿越)

The rule: **if it's "over time" → chart. If it's "right now" → kpi/compare.**

## Hard rules

- **Do not hand-type chart values.** Always use `build_chart.py` so the data is fresh. Inventing values = data drift.
- **Always include `@xlabels`** for multi-week charts so the user can pin dates.
- **Last point gets a dot** (renderer does this automatically) — emphasizes "current".
- **Idempotent re-runs.** The skill can be invoked multiple times to refresh — just regenerate and replace the existing chart block in the markdown.
