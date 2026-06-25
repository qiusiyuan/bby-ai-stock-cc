---
name: brief
description: "Module 5 of the daily brief — the AI synthesis tab. Visual + scannable (NOT a long essay). Reads pulse / watchlist / timeline / cluster outputs from dashboard/{date}.md and writes a synthesis that's mostly visual blocks: 1-line headline, top-mover kpi, per-cluster verdict table, 7-day timeline focus, scenarios bar, do/don't callout. Triggers: 'brief', 'tldr', 'summary', 'synthesis', 'AI judgment'. Runs LAST in /report after all other modules."
---

# /brief

Module 5. **The synthesis tab — visual-first, not essay-first.** Earlier iteration was too prose-heavy; this version reads like a scannable dashboard.

## When invoked

- "brief" / "tldr" / "summary" / "synthesis"
- "AI judgment" / "what do you think today"
- "just the conclusion"
- AUTOMATICALLY as the last module of [[report]]

## Steps

### 1. Read the day's markdown

Open `dashboard/{date}.md`. Extract from each existing H2 section:
- **Pulse & Macro** → today's tape headline, top 2 macro signals
- **Watchlist & Movers** → top 3 movers (gainers + losers)
- **Timeline 30d** → events in next 7 days
- **Focus: {cluster}** for each cluster → that cluster's verdict pill

### 2. Pull supporting data

- Run [[find-similar-moves]] for each big mover → grab dates of past analogs (1 each, max)
- Read `stocks/{T}/thesis.md` bull/base/bear for the top 1-2 movers — just the % probabilities, not the full text

### 3. Write the H2 — visual blocks > prose

Replace any existing `## Brief` H2 in place. Boundary: `## Brief` to next `## ` or EOF.

**STRICT TEMPLATE** — keep it tight, no long paragraphs:

```markdown
## Brief

```callout {info|warn|danger}
**{One sentence headline. The compressed truth of the day.}**
```

### 今日 tape
```kpi
SPY | {price} / {1D%} | {1-line read}
VIX | {value} | {risk pulse: low/elevated/high}
Top mover | {ticker} {±%} | {1-line driver}
Most at risk | {ticker} | {distance to thesis-break or trigger fired}
```

### 各 cluster 状态
```compare
| Cluster | 今日故事 (≤ 12 字) | Verdict | Next catalyst
| TSLA    | ...                  | watch   | 6/30 Q2 deliveries
| SpaceX  | ...                  | hold    | 12/9 lockup
| DRAM/HBM| ...                  | hold    | 6/24 MU Q3
| AI capex| ...                  | watch   | 7/29 MSFT/META
| 能源    | ...                  | watch   | 7/31 PCE
```
(Pull the verdicts directly from each cluster's `## Focus: ...` H2.)

### 下个 7 天的决定性 catalyst
```timeline
{date} 🔥 | {event} — {why it's decisive}
```
(Max 4 entries. Pulled from Timeline 30d red tier.)

### 概率分布 (整体 / 你最大暴露的股票)
```scenarios
Bull | {%} | {target/level} | {1-line trigger}
Base | {%} | {target/level} | {1-line trigger}
Bear | {%} | {target/level} | {1-line trigger}
```
(Use the top mover's thesis bull/base/bear, OR the most thematic cluster's outlook.)

### Don't / If acting
```callout warn
**Don't**: {1 concrete don't}.
**If acting**: {what unblocks action — usually a specific upcoming data point with date}.
```

### 一句话总结
> {One italicized sentence. The thing to remember when you close the tab.}
```

**That's it. No more than ~40 lines of markdown total.** The visual blocks carry the weight; prose is minimal connective tissue.

### 4. Don't render — /report renders dashboard/{date}.md at the end

## Hard rules

- **Visual blocks > prose**. Use `kpi`, `compare`, `timeline`, `scenarios`, `callout`. Avoid multi-paragraph sections.
- **Cite specific signals/stocks** with names. Never write "the macro environment is uncertain" — say which signal.
- **Use probability for forward judgments** — bull/base/bear with explicit % is the user's preferred frame.
- **One don't, one if-acting** — actionable or it's useless.
- **Refer to thesis** — top mover's analysis should reference its bull/base/bear %.
- **Cite analogs sparingly** — if find-similar-moves found a past case, mention date + outcome in 1 line max.
- **No fabrication** — `n/a` if missing; never invent.
- **Section boundary**: `## Brief` to next `## ` or EOF.

## What changed from prior version (2026-06-23 redesign)

The prior brief was 5 prose sections that read like a memo. User feedback: not scannable. New version is **visual-first**:
- Single-sentence headline callout
- 4-cell KPI strip
- Per-cluster verdict table (one row per cluster)
- 7-day timeline highlight (3-4 events)
- Bull/base/bear bars
- Don't / if-acting box
- One-sentence summary

Should fit on one screen without scrolling.
