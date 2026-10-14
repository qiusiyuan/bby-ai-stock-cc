# SSPC attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-14 · +5.38% day · ▲ major
**Tags:** `macro_inflation`, `sector_rotation`, `flow_event`
**Confidence:** high

**Primary cause.** **SPCX 2x 反向 ETF 的机械对应 (SPCX -2.80%), 无独立信息。** 量比 0.83x 低于全场中位数 — 即使在反向产品上涨的一天也没有真实参与。**信息在 30d -21.26%: 做空 SPCX 在一个月尺度上仍大幅亏损 (SPCX 30d +6.98%)。** ⚠️ 杠杆反向 ETF 的波动衰减会额外侵蚀净值, **不能用 SSPC 的涨幅反推 SPCX 的弱度**。对照 10/08: 当日 SSPC +7.40% 而 30d 为 -31.86%; 今天 30d 改善到 -21.26%, 说明空头在深水区的喘息已持续约一周。|| 宏观共因 (三个独立的因, 不可压成一个): **(1) 九月 CPI**: 同比 +3.7% (共识 3.6%)、环比 **+0.6% 为过去一年最高**。CPI = Consumer Price Index, BLS 每月发布的美国最主要通胀指标。环比年化约 7.4%, 远高于 Fed 2% 目标。timeline 在今天之前已记 Oxford Economics 的提示 — 九月调查窗口内柴油 +60 美分/加仑、汽油 +20 美分, 油价冲击会进入这份读数, 所以这个数字是可预告的。它接在 9/17 FOMC 转鹰 + 9 月纪要 (10/07 公布) 指向今年再加一次息 (市场当时只给 19%) 之上, 是纪要后第一个硬数据且站在纪要一边。**(2) ❗长端拒绝配合 — 本条必须作为限定随附**: CPI 超预期而 10Y -2.7bp / 30Y -3.8bp / TLT +0.66%。媒体口径写的是 'rate-hike jitters'、'rising bond yields', 债市当天的实际方向与之相反。所以今天的跌**不能用「当天利率上行」解释** — 实现通道是风险溢价 (VIX +10.48%) 与叙事, 不是折现率。这是本月第四次长端对本应推高它的消息不配合 (10/01 失败突破 / 10/02 非农利多无响应 / 10/08 诱因缓解不修复 / 今天 CPI 超预期不涨)。**(3) 横截面否证「加息打击高倍数股」的单一叙事**: 倍数最高的 TSLA (fwd PE 168x) 跌 2.15%, 低于倍数中等的MRVL (33.7x) -8.73%、SNOW (111x) -6.34%、GEV (37x) -6.20%。跌幅与 **30d 涨幅**的相关性明显优于与倍数的相关性(MRVL 30d +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小跌幅)。**今天卖的是一个月里的涨幅, 不是久期。** **⭐ 方法论变化 (改写前三份报告的限定)**: 10/05、10/07、10/08 三份归因都写了同一句「半量里的下跌属『没有买盘』而非『出现卖盘』, 方向可信幅度不可信」。**今天不成立**: 量比中位数 1.02x (10/08 为 0.48x / 10/07 0.79x / 10/05 0.49x), 17/32 过 1.0x (10/08 为 3/34), 放量集中在跌最多的标的 (GEV 1.65x / QQQ 1.53x / TSM 1.45x / KOID 1.39x / MRVL 1.31x / DRAM 1.30x)。**这是这轮下跌序列里第一个全参与度的下跌日 — 幅度本身开始带信息。** 反方限定仍要记: 跌最惨的 MRVL 量比只有 1.31x、MU 只有 1.04x, 「放量」是全场性的而非个别标的清仓。

**Sources.**
- 247wallst via yfinance (CPI 3.7% YoY vs 3.6% 共识; MoM +0.6% 年内最高): Trump Media and Rumble Decline 5% as September Inflation Runs Above Forecasts; Reddit Slides 2%
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- IBD via yfinance: Stock Market Today: Nasdaq Dives On Rate Hike Jitters, AI Woes; Taiwan Semi Earnings On Deck
- Yahoo Finance video (Baird 策略师 Ted Mortonson): CoreWeave, Intel, Micron, & other tech stocks are plummeting. Here's why.

**Cross-assets.** SPY -1.08% · QQQ -1.97% · IWM -1.93% · DIA -0.11% · VIX 16.87 (+10.48%) · TEN YEAR 5.190% (-2.7bp) · THIRTY YEAR 5.525% (-3.8bp) · TLT +0.66% · WTI +1.16% · BRENT $106.06 (30d +12.05%) · GOLD -1.23% · SILVER -5.81% · DXY 102.530 (+0.34%) · BTC -1.81% · ETH -3.40% · BREADTH 32 只中 26 跌 / 6 涨 (含 2 只反向) · VOLUME MEDIAN 量比中位数 1.02x · 17/32 过 1.0x (10/08 为 0.48x · 3/34)

**Agent read.** 


---
### 2026-10-05 · -13.17% day · ▼ extreme
**Tags:** `flow_event`, `analyst_upgrade`
**Confidence:** high

**Primary cause.** SPCX 的 2x 反向 ETF, 机械跟随 SPCX +5.57%。但本条的信息价值不在方向而在成交量: vol 1.96x 是当日 32 只跟踪标的里唯一显著放量的 (其余只有 HXE.TO 1.31x / SPCX 1.14x 过 1.0x, 中位数 0.49x)。放量下跌在反向 ETF 上的读法是空头头寸在被挤出平仓, 而不是机构建立新空仓 —— 10/02 已记录同样结构 (SSPC -11.57% 接近完全对称, 判为反向 ETF 持有者平仓)。连续三天的空头挤出是 SPCX 能在利率完全不配合 (10Y 回到距 52 周高 3.8bp) 的情况下延续涨幅的动能来源。推论: 这是挤仓动能不是估值重估, 挤仓会结束; SSPC 量比回落到 1.0x 以下即为空头挤出完成的信号, SPCX 届时失去这个动能来源。路径依赖损耗: SPCX 30d +22.52% 对应理论 2x 反向 -45%, SSPC 实际 -39.91%, 差额来自每日重置 —— 持有反向 ETF 跨越趋势期会系统性损耗。当前 $6.79 距 52 周低点 $6.00 仅 13.2%。

**Sources.**
- _Data:_  ()
- Yahoo Finance: [SpaceX Stock Surges as Morgan Stanley Says Stock 'Cheap and Getting Cheaper'](https://finance.yahoo.com/)

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-09-23 · +4.89% day · ▲ material
**Tags:** `macro_rates`, `flow_event`
**Confidence:** high

**Primary cause.** SSPC +4.89%（SPCX 的 2x 反向 ETF），是 SPCX -2.55% 的机械镜像，无独立信息量。记录仅为索引完整性。

**Sources.**
- : [10-year Treasury yield hits highest level since 2007](https://finance.yahoo.com/quote/%5ETNX/)

**Cross-assets.** SPY CHANGE -0.74% · VIX 15.34 · TEN YEAR 5.12 · WTI 91.41 · DXY 101.19 · QQQ CHANGE -1.01%

**Agent read.** 3mo -29.1% 而同期 SPCX 仅 -3.4%——这个差距是波动率损耗（volatility decay）的实证：即使标的季度跌幅很小，2x 反向产品仍损失近三成。结论：此类工具不适合作为长期对冲载体，只在明确的短期方向性判断下有意义。
 · Snapshot at `dashboard/2026-09-23.md`

---
### 2026-09-15 · +5.59% day · ▲ material
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** high

**Primary cause.** **无独立信息量 —— SSPC 是 SPCX 的 2 倍反向 ETF, 今天 +5.59% 精确对应 SPCX 的 -2.92%。** 记录它是因为触发 1d≥3% 与 5d≥10% 双阈值, 但它的作用仅是 SPCX 方向的确认读数。SPCX 今天下跌的归因是纯折现率税: 10Y 破 5.00% (2007 年 7 月以来最高), 而 SPCX 是组合内对折现率敏感度最高的资产 (零当期盈利 + 全部价值在远期现金流, fwd PE 82.5x)。**值得单独记的是 30 日数字: SPCX 30d +25.57%, SSPC 30d -51.73%。理论上 2 倍反向的 30 日应为约 -51.14%, 实际 -51.73% —— 差额约 0.6 个百分点就是杠杆 ETF 每日重置的波动率磨损 (volatility decay)。这是「杠杆反向 ETF 不适合长期持有」的一个干净实证, 也是本 workspace 记录这个标的的主要价值。** 现价 $9.925, 52 周区间 $6.00–$24.66; MA50 $14.01 (远低于), MA200 n/a (上市不足 200 日)。

**Sources.**
- {"type": "cross_stock", "title": "SPCX -2.92% (5d -6.29%, 30d +25.57%) \u2014 SSPC \u4e3a\u5176 2x \u53cd\u5411", "publisher": "workspace", "url": ""}
- CNBC: 10-year Treasury yield hits highest level since 2007

**Cross-assets.** SPY -0.47% · VIX 17.46 · TEN YEAR 5.0 · WTI 105.95 · DXY 99.64 · GOLD 4342.5 · BTC 75913

**Agent read.** 零独立信息; 唯一价值是 30d -51.7% vs 理论 -51.1% 的差额量化了杠杆磨损。作为 SPCX 的镜子使用, 不作独立信号。


---
### 2026-08-04 · -20.01% day · ▼ extreme
**Tags:** `flow_event`, `earnings_pre_print`, `sector_rotation`
**Confidence:** high

**Primary cause.** Mechanical inverse response: SSPC is a 2x inverse ETF on SPCX, which rose +9.81% on short-covering ahead of SpaceX's first-ever earnings report tonight. The -20.01% move is leverage-consistent with roughly twice SPCX's gain, indicating inverse positions being liquidated into the binary event.

**Sources.**
- _Corroboration:_ SPCX +9.81% versus SSPC -20.01% — consistent with 2x inverse mechanics. Broad inverse-ETF liquidation across the tape: SQQQ -10.6% on QQQ +3.6%.
- Yahoo: [Elon Musk issues ominous warning as SpaceX short interest hits danger zone](https://finance.yahoo.com/)

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** No independent information content — SSPC is a pure mechanical mirror of SPCX and its move is fully explained by 2x leverage. Its diagnostic value is confirming that today's SPCX advance was position-driven short-covering rather than news-driven: a clean inverse relationship at full leverage ratio is what forced liquidation looks like. Worth preserving as context: SSPC is still +28.4% over 30 days, meaning shorting SPCX through the inverse ETF was highly profitable during July's collapse. It also carries the standard leveraged-ETF volatility-decay penalty, which is why 30-day +28.4% understates the gain a direct short would have captured over the same window. Tonight's earnings will produce another mechanical 2x move in the opposite direction of SPCX.
 · Snapshot at `dashboard/2026-08-04.md`

---
