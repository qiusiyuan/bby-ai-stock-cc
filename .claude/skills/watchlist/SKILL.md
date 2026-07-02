---
name: watchlist
description: "Module 2 of the daily brief — Watchlist + Movers, split into FOCUS (重点观察, detailed) and REGULAR (常规持仓, compact). Use when the user wants a snapshot of tracked stocks plus flags on today's movers. Triggers: 'watchlist', '持仓', 'check all', 'movers', '今天的 move', 'alerts', 'who moved today'. Sub-triggers: 'watchlist focus' (only 重点), 'watchlist all' (展开全部), '重点观察 X' (add to focus), 'X 移出重点' (remove). Writes '## Watchlist & Movers' H2 to dashboard/{date}.md."
---

# /watchlist

Module 2. Two-tier per-stock grid: **focus (重点)** in detail, **regular (常规)** compact, plus movers identification.

## When invoked solo

- "watchlist" / "持仓" / "check all"
- "movers" / "今天的 move" / "alerts" / "who moved today"
- "watchlist focus" / "重点" — only focus group, skip regular
- "watchlist all" / "展开全部" — expand all stocks (no folding)
- "重点观察 NVDA" / "NVDA 加入重点" — add ticker to `focus.members` in `groups.yaml`
- "NVDA 移出重点" / "把 NVDA 从重点拿掉" — remove from focus
- AUTOMATICALLY as module 2 of [[report]]

## Steps

### 1. Read both tiers from groups.yaml + state.yaml

```yaml
focus:
  members: [MU, TSLA, SPCX, DRAM]   # 重点 — detailed render
```

Read `stocks/*/state.yaml`, filter `active: true`. Split into:
- **focus tier**: in `focus.members`
- **regular tier**: active but not in focus

### 2. Fetch fresh quotes in parallel

```bash
for t in $ACTIVE_TICKERS; do
  uv run --project scripts scripts/fetch.py "$t" > "/tmp/wl_$t.json" 2>/dev/null &
done; wait
```

### 3. Compute per-stock fields

For each stock parse the JSON and extract:
- `price`, `change_pct_1d`, `change_pct_5d`, `change_pct_30d`, `volume_ratio`
- Distance from `stocks/{T}/triggers.yaml::thesis_break_price` (as % buffer)
- Next earnings/catalyst date (read `timeline.yaml`)
- Signal flag: 🔥 (`|1D%| >= 5%` or `volume_ratio >= 1.5x`) / ⚠ (`|1D%| >= 3%`) / ✅ (quiet)

**Null handling**: `fetch.py` returns `null` for any field not available (recent IPOs, ETFs, indices). Render `null` as `"n/a"` in `kpi`/`compare` blocks. Don't drop the row — show what you have.

### 4. Auto-promote movers to focus (today only)

Any stock that hit 🔥 in step 3 gets **temporarily rendered in the focus section** for today's report, even if not in `focus.members`. Mark with `[mover]` tag. **Do NOT modify `groups.yaml`** — temporary promotion only.

### 5. Auto-suggestion logic

Agent flags to user but doesn't auto-edit:
- **Promote suggestion**: any non-focus stock with ≥3 attribution-worthy moves in last 7 days → suggest "加入 focus?"
- **Demote suggestion**: any focus stock with 0 movement-flags for 7+ days → suggest "移到常规?"

Surface as a single line at top of the H2: `Suggested focus changes: add NVDA (3 active days), drop IBM (7 quiet days). Confirm?`

### 6. Check triggers

Run [[check-triggers]] logic for each stock. Any within 5% of `thesis_break_price` gets a `callout warn` (within 10%) or `callout danger` (within 5%) block.

### 6b. Earnings scorecard check (MANDATORY)

For every active stock, parse `stocks/{T}/state.yaml::earnings_watchlist`. If the block exists AND `status: pending` AND today is within `scoring_window` of `scoring_date`:

- **Today == scoring_date** (the print day): Add a 🎯 flag to that stock's row and emit a `callout danger` block at the top of the focus section:
  > 🎯 **{TICKER} 财报评分日 — 「{thesis_claim}」打分。** 打开 `{scorecard}` 对 Tier 1 指标逐行评分，写入 dashboard 的 `## Earnings scorecard: {TICKER}` H2，并把 verdict 追加到 `stocks/{T}/thesis.md` Stands & Updates。打分完后把 `state.yaml::earnings_watchlist.status` 改为 `scored`。
- **Within ±7d of scoring_date**: Emit a `callout warn` block:
  > ⏰ **{TICKER} 财报临近 ({scoring_date}, 还有 N 天)。** 评分卡在 `{scorecard}`。提前重读，确保 Tier 1 门槛清晰。

Surface these alerts *before* any normal per-stock detail — they're the highest priority signal in the section.

### 7. Identify threshold-crossings → deep-dive candidates

Apply attribution thresholds from [[deep-dive]]:
- `|change_pct_1d| >= 3%`
- `|change_pct_5d| >= 10%`
- `volume_ratio >= 1.5`

These get a "Deep-dive candidate" flag for the orchestrator menu.

### 8. Write the H2 section

Replace any existing `## Watchlist & Movers` H2 in place. Section boundary: from `## Watchlist & Movers` line to the next line starting with `## ` or EOF (do NOT match `### `).

Structure:

```markdown
## Watchlist & Movers

{One-line suggestion if any: "Suggested focus changes: ..."}

### 🔥 重点 ({N} focus + {M} auto-promoted movers)

For each focus / auto-promoted stock — detailed KPI card:
{ticker} | ${price} / {1D%} | {signal} {one-line read}

Then per ticker (only when relevant):
- Trigger distance: "距 thesis-break ${X} 缓冲 +Y%"
- Next catalyst: "{date} {event}" from timeline.yaml
- Recent attribution: link to most recent entry in stocks/{T}/attributions.md

### 常规持仓 ({N} stocks, sorted by signal)
| Ticker | Price | 1D% | 5D% | 30D% | Vol | Signal | Next catalyst
| ...    | ...   | ... | ... | ...  | ... | ...    | ...

(quiet ✅ stocks folded into a sub-table at the end)

### Threshold-crossings → deep-dive candidates
{table only if any crossed}

### Trigger breaches
{callout warn/danger only if any in danger zone}
```

### 9. Mode flags

- `"watchlist focus"` / `"重点"` — skip 常规持仓 section
- `"watchlist all"` / `"展开全部"` — expand all 常规 stocks (no folding)
- Default: show both, fold quiet 常规

### 10. Don't render here — orchestrator renders dashboard/{date}.md at the end

## Hard rules

- **Sort by signal severity** — 🔥 always first
- **Quiet stocks fold** — don't waste prime real estate
- **Flag threshold-crossings explicitly** — these become menu options for deep-dive in the orchestrator
- **Inactive stocks excluded**
- **No cost basis ever** (workspace rule)
