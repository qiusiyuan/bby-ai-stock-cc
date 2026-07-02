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

## Output checklist (每次 Pulse 必须包含以下所有 block — 缺一不可)

- [ ] **Indices**: SPY, QQQ, Dow, VIX, 10Y yield — `kpi` block
- [ ] **Commodities**: WTI oil, Gold, Silver — `kpi` block
- [ ] **Crypto**: BTC, ETH (每天); IBIT/MSTR/COIN (当 BTC |1d|≥5%) — `kpi` block
- [ ] **货币/FX**: DXY + USD/CAD + USD/CNY + 换汇判断 — `kpi` block + 短评
- [ ] **重大宏观事件** (如有): NFP/CPI/FOMC/地缘 → 完整四步解读
- [ ] **Headlines**: 当天 top 5-8 新闻
- [ ] **政策/地缘快扫**: Fed, 美伊, 中国, EU, 其他
- [ ] **Cross-ref**: 每个 signal → 影响哪些持仓

**如果 subagent 执行此 skill: prompt 里必须逐条列出以上 8 个 block 的要求。** 不要假设 subagent 会自己去读 skill 文件。

---

## Steps

### 1. Pull indices and risk proxies in parallel

**Mandatory daily coverage:**
- Indices: SPY QQQ + VIX + 10Y + DXY
- Commodities: WTI oil, gold, silver (every day, even when quiet)
- **FX**: USD/CAD, USD/CNY (small block; user holds USD and wants timing signals for converting to CAD or RMB)
- **Crypto**: BTC + ETH (daily price check); IBIT / MSTR / COIN (weekly or when |1d| ≥ 5%). Crypto is a leading risk-asset indicator — BTC typically leads SPY 2-4 weeks; user does not directly hold crypto but wants the risk-hierarchy signal.

```bash
for t in SPY QQQ DIA IWM ^VIX ^TNX "DX-Y.NYB" "USDCAD=X" "USDCNY=X" GLD SLV GC=F SI=F USO CL=F TLT ITA KWEB BTC-USD ETH-USD; do
  uv run --project scripts scripts/fetch.py "$t" > "/tmp/pulse_$t.json" 2>/dev/null &
done; wait
```

For crypto-specific deeper view (when BTC moves >5% 1d OR > 15% 5d), also pull: IBIT (BlackRock spot BTC ETF), MSTR (Saylor leveraged proxy), COIN (Coinbase, US-regulated exchange).

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

### 3b. 重大宏观事件深度解读 (MANDATORY when triggered)

**触发条件:** 当天有以下任一事件时，必须在 Pulse & Macro section 内插入一个独立的 `callout` + 详细解读块:
- NFP / jobless claims 数据发布
- CPI / PPI / PCE 数据发布
- FOMC 决议 / 点阵图 / Powell 讲话
- 地缘冲突状态变化 (战争升级/停火/新制裁)
- 重大行政命令 / 关税变动 (>5%)
- 重大公司事件影响整个市场 (e.g. 大型 hyperscaler 宣布改变 capex 策略)

**解读结构 (每个重大事件都要走完这四步):**

1. **是什么 (What):** 全称 + 一句话解释这个数据/事件衡量什么。不假设读者知道缩写含义。
   - ❌ "NFP +57K miss" 
   - ✅ "Non-Farm Payrolls (非农就业): 美国劳工部每月第一周五发布，衡量当月非农部门新增就业人数。今天报 +57K (预期 115K, 前值 172K) — 是预期的一半。"

2. **为什么重要 (Why it matters today):** 对比预期/前值 + 处于什么趋势 + 为什么市场此刻格外在乎。
   - 第几连月增长/下降? 趋势加速还是减速?
   - 当前市场最关心的叙事是什么? (e.g. "到底是 soft landing 还是 recession")
   - 这个数字对 Fed 下次决策意味着什么?

3. **市场的推理路径 (How it transmits):** 画出传导图 — 不是所有持仓受同方向影响。
   - 数字 → 对利率预期的影响 → 美元/债市反应 → 风险偏好变化 → 各板块差异化影响
   - 明确哪些持仓受益、哪些受损、哪些不受影响、以及为什么
   - 如果市场解读分裂 (e.g. "降息预期利好 growth" vs "经济放缓利空 growth")，把两面都写出来并说明今天实际走了哪一面

4. **对每个持仓的具体影响 (Position impact map):**
   用 compare 或 table 格式映射:
   ```
   | 持仓 | 影响方向 | 传导逻辑 |
   | TSLA | ⬇️ 利空 | 高 beta growth, NFP weak = growth fear rotation |
   | SU/CVX | ⬆️ 利好 | 降息预期 + value rotation bid |
   | NVDA | ⬇️ 中性偏空 | duration 资产, 但 AI 需求独立于就业 |
   | MSFT/AMZN | ⬆️ 利好 | defensive growth + 降息利好 |
   ```

**原则:** 宏观事件是当天所有个股 move 的 "公因子"。不解释清楚这个公因子，后面每个个股归因都缺根基。所以 Pulse 里的宏观解读是全天分析的地基 — 要写扎实。

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

### 🪙 Crypto (daily — leading risk-asset indicator)

BTC + ETH every day. **BTC typically leads SPY by 2-4 weeks** — significant BTC drawdown without SPY follow-through is a yellow flag. Surface IBIT/MSTR/COIN proxies when BTC moves >5% 1d or >15% 5d, or when crypto-specific headlines (regulation, ETF flows, Saylor positioning) emerge.

```kpi
BTC | $X / +-Y% | 距 ATH / 52w low / MA200 status
ETH | $X / +-Y% | BTC 对照
IBIT (or MSTR/COIN when notable) | $X / +-Y% | 机构 / 杠杆 proxy
```

Flag as `callout danger` when ANY of:
- BTC breaks below 52w low or MA200
- MSTR < 52w low (Saylor leverage stress)
- BTC 30d down > 15% AND SPY 30d down < 5% (risk-hierarchy divergence)
- Coinbase / Strategy / Binance regulatory action announced

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
