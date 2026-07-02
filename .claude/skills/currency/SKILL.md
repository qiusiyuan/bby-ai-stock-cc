---
name: currency
description: "Dedicated currency / rates / Fed tab. Use when the user says: '货币', 'currency', 'FX', '美元', 'dollar', '换汇', '汇率', 'rates tab', 'Fed update'. Writes a '## 货币 / 美元 / 利率' H2 to dashboard/{date}.md. NOT a daily module — runs on demand or when a Fed event / 52w extreme / >1% major-pair move warrants it. Medium-term lens (3-6 weeks of trend), not daily noise."
---

# /currency

A standalone tab for **USD + rates + FX trends**, viewed through a multi-week lens. Not a daily module — it appears in the report only when:

1. User asks for it explicitly (most common)
2. FOMC / dot plot / Fed minutes drop
3. Major pair (USD/CAD, USD/RMB, EUR/USD, USD/JPY) hits a 52w extreme
4. 10Y or 2Y breaks a multi-month range
5. BoC / PBoC / ECB / BoJ surprise action

## Why this tab exists

The user holds USD and is timing conversions to **CAD** and **RMB**. They don't want daily noise — they want a coherent view of:
- Where is the dollar in its cycle (DXY level + trend + 52w position)
- What is the Fed saying / pricing (FOMC, dots, recent speeches)
- Are foreign central banks moving (BoC, PBoC, ECB, BoJ)
- What's the curve telling us (3M vs 2Y vs 10Y)
- Concrete conversion windows: when to act, when to wait

## Steps

### 1. Fetch in parallel

```bash
for t in "DX-Y.NYB" UUP "USDCAD=X" "USDCNY=X" "CADCNY=X" "EURUSD=X" "USDJPY=X" "^IRX" "^FVX" "^TNX" "^TYX" TLT; do
  uv run --project scripts scripts/fetch.py "$t" > "/tmp/cur_$t.json" 2>/dev/null &
done; wait
```

**CAD/CNY is mandatory** — user holds USD but cares about the CAD↔RMB cross because (1) tells them which 2-step path (USD→CAD→RMB vs USD→RMB→CAD) has better purchasing-power transfer, (2) reveals divergence between the two non-USD currencies they care about.

### 2. Read trend, not just today

For each instrument extract: price, 5d, 30d change, 52w low/high, MA50, MA200. The story is in:
- **Position vs 52w range** — touching extremes is information
- **Position vs MA50/MA200** — above both = uptrend; crossing = inflection
- **30d direction** — multi-week trend

### 3. Pull Fed / central-bank news

Use SPY/TLT/UUP news streams. Keyword filter:
```
["fed", "fomc", "powell", "williams", "waller", "dot plot", "rate cut", "rate hike",
 "treasury", "yield", "boc ", "bank of canada", "macklem", "pboc", "ecb", "lagarde",
 "boj", "ueda", "rmb fix", "intervention"]
```

### 4. Write H2 section

```markdown
## 货币 / 美元 / 利率

**[N 周视角]** — one-line headline of the dollar cycle right now.

### 美元位置
```kpi
DXY | X / +-Y% 30d | 52w {low}-{high} · MA50 Z · {at high|mid range|at low}
UUP | X | 52w high check — confirms or contradicts DXY
```

### 美国利率曲线
```kpi
3M (^IRX) | X.XX% | 52w pos · what near-term Fed expectations say
2Y/5Y     | X.XX% | curve belly — inflation persistence
10Y       | X.XX% | duration risk, mortgage anchor
30Y       | X.XX% | term premium / fiscal worry
TLT       | $X    | bond ETF — confirmation
```

```callout {info|warn|danger}
**Curve read.** One sentence: steepening / flattening / inverted; what it says about Fed path.
```

### 主要货币对
```compare
Pair | Now | 30d | 52w pos | MA50 dev | Trend read
USD/CAD | ... | ... | ... | ... | ...
USD/RMB | ... | ... | ... | ... | ...
CAD/RMB | ... | ... | ... | ... | cross — purchasing-power signal between user's two non-USD targets
EUR/USD | ... | ... | ... | ... | ...
USD/JPY | ... | ... | ... | ... | ...
```

**Reading CAD/CNY:** if CAD/CNY is at 52w low (CAD weak vs RMB), then **USD→CAD→RMB path is worse** than USD→RMB direct; conversely if CAD/CNY is at 52w high, CAD has stored purchasing power that converts well to RMB later. This affects whether to split the conversion or do them in different orders.

### Fed / 央行近况
- **Fed:** {last FOMC date} · {next FOMC date}. Last move: {hold/cut/hike}. Recent speeches: {2-3 bullets if any}.
- **BoC:** {last move, next decision date if known}.
- **PBoC:** {RMB fix, recent interventions, any easing signals}.
- **ECB / BoJ:** {only if they moved or are diverging}.

### Conversion windows (the user's purpose)

```callout {info|warn|danger}
**USD → CAD:** wait / act / DCA. Reasoning in 2 sentences.
**USD → RMB:** wait / act / DCA. Reasoning in 2 sentences.
```

Trigger language for "act now" vs "wait":
- USD/CAD: ACT if pair < MA50 AND DXY rolling over. WAIT if pair at 52w high.
- USD/RMB: prefer steady DCA — PBoC manages tightly; trend over level.
- Frame as **windows**, not predictions. E.g. "watch for FOMC on {date}; if dovish wording, USD likely retraces 1-2% in 1-2 weeks → that's the window."
```

### 5. Don't run as part of /morning by default

This is its own thing. The daily /pulse already has a small FX block. This tab is the deeper view.

## Hard rules

- **Multi-week lens.** Don't get distracted by 1-day moves unless they break a range.
- **Always answer the conversion question.** That's why this tab exists.
- **Frame Fed events as windows.** "If FOMC dovish, USD weakens — that's your window" is the right shape.
- **Don't repeat the daily FX block.** Reference it ("see /pulse for today's tick") and go deeper.
- **Idempotent.** Re-running replaces the H2 in place.
