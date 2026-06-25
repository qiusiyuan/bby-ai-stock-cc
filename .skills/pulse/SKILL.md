---
name: pulse
description: "Module 1 of the daily brief — Pulse + Macro combined. Use when the user wants today's market state and macro/policy news in one view. Triggers: 'pulse', 'market', 'tape', 'macro', 'policy', 'Fed', 'Iran', '今天大盘', 'macro update'. Subsumes the old pulse skill. Writes a '## Pulse & Macro' H2 section to dashboard/{date}.md."
---

# /pulse

Module 1. One H2 section combining big-picture market state + macro/policy signals.

## When invoked solo

- "pulse" / "market" / "tape"
- "macro" / "policy" / "Fed news" / "Iran update"
- "any macro signals"
- AUTOMATICALLY as the first module of [[report]]

## Steps

### 1. Pull indices and risk proxies in parallel

**Mandatory daily coverage:**
- Indices: SPY QQQ + VIX + 10Y + DXY
- Commodities: WTI oil, gold, silver (every day, even when quiet)
- **FX**: USD/CAD, USD/CNY (small block; user holds USD and wants timing signals for converting to CAD or RMB)

```bash
for t in SPY QQQ DIA IWM ^VIX ^TNX "DX-Y.NYB" "USDCAD=X" "USDCNY=X" GLD SLV GC=F SI=F USO CL=F TLT ITA KWEB; do
  uv run --project scripts scripts/fetch.py "$t" > "/tmp/pulse_$t.json" 2>/dev/null &
done; wait
```

### 2. Pull policy news from sensitive proxy tickers

Same as the legacy pulse skill. From SPY/USO/GLD/ITA/KWEB news, filter by keyword:

```
KEYWORDS = [
  "trump", "biden", "fed ", "fomc", "rate", "sec ", "doj", "ftc", "tariff",
  "sanction", "export control", "iran", "china", "russia", "ukraine", "israel",
  "taiwan", "korea", "kospi", "nato", "military", "pentagon", "regulat", "policy",
  "treasury", "congress", "senate", "court ruling", "antitrust",
]
```

### 3. Cross-reference with active positions

For each signal:
- **Iran / oil headlines** → SU / CVX / CNQ / HXE.TO / GEV
- **Fed / rates** → all high-duration growth (NVDA, TSLA, SPCX, MSFT, META, GOOG, etc.)
- **US-China / export controls** → TSM, NVDA, AMD, AVGO, MRVL
- **Korea** → SK Hynix, Samsung, DRAM, MU (HBM supply chain)
- **EU regulation** → SPCX, TSLA, GOOG, META
- **Defense / Pentagon** → SPCX (Starshield), GEV

### 4. Write H2 section to dashboard/{date}.md

Replace any existing `## Pulse & Macro` H2 in place. Structure:

```markdown
## Pulse & Macro

```callout {info|warn|danger}
{one-line headline of the day's macro/market state}
```

### Indices
```kpi
SPY | $X / +-Y% | trend note
QQQ | $X / +-Y% | trend note
VIX | X / +-Y% | risk read
10Y | X.XX% / +-bps | rates read
DXY | X.XX / +-Y% | dollar read
```

### Commodities (mandatory every day)
```kpi
WTI | $X / +-Y% | oil — geopolitics / demand read
Gold | $X / +-Y% | safe-haven / real rates / dollar
Silver | $X / +-Y% | industrial + monetary; gold/silver ratio = stress proxy
```

### 货币 / FX (small block; user holds USD, wants timing for converting to CAD/RMB)

Show DXY + USD/CAD + USD/RMB plus any notable Fed / Treasury / BoC / PBoC headline. Keep it small — one kpi block + one short note. Surface as actionable signal ONLY when the pair is at a 52w extreme or moves >1% on the day.

```kpi
DXY | X / +-Y% | dollar index — context for everything below
USD/CAD | X.XXXX / +-Y% | 52w high X / low Y · MA50 Z — Loonie weakness or strength signal
USD/RMB | X.XXXX / +-Y% | 52w high X / low Y · MA50 Z — managed band; small moves matter
```

**Decision lens for the user:**
- DXY at 52w high + USD/CAD at 52w high → **USD overvalued for converting to CAD; wait for pullback**
- DXY rolling over + Fed dovish pivot → **good window to convert USD → CAD/RMB**
- USD/RMB stable around managed band → no urgency either way
- BoC cut / hike news → flag if it shifts the rate-differential narrative

ONLY include this block when there's something to say. Don't pad with "no FX news" filler — drop the section entirely if quiet.

### Morning headlines (mandatory — top 5-8 of the day)

Source from SPY/QQQ news plus any sensitive-proxy news that hits a keyword. Format:

```
- [HH:MM] **headline** — source. 1-line so-what (touches: {tickers if relevant})
```

Lead with the highest-impact items — Fed/FOMC, geopolitics, major earnings, executive orders. Don't pad with filler.

### Policy & geopolitical signals (only if any)
```callout danger
**{signal}** — touches: {tickers}. {1-line context}.
```

### Macro → tracked-position cross-ref
```compare
Signal | 1D move | Touches
{...}  | {...}   | {...}
```
```

### 5. Don't render — that's the orchestrator's job

If invoked solo, render at the end. If invoked from [[report]], the orchestrator renders once at the end.

## Hard rules

- **Only emit `callout warn/danger` for real signals** — don't manufacture drama on quiet days
- **Cross-ref is the value-add** — without it, this is just data dump
- **Idempotent**: same-day re-run = replace H2 in place. Section boundary: from `## Pulse & Macro` to next line starting with `## ` or EOF.
- **Null handling**: `fetch.py` returns `null` for unavailable fields (recent IPOs, ETFs). Render as `"n/a"` — don't drop the row.
