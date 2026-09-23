# SSPC attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

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
