# SSPC attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

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
