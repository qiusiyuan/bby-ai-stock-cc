# AMD attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-08-19 · -3.71% day · ▼ material
**Tags:** `sector_rotation`, `competitor_news`
**Confidence:** medium

**Primary cause.** AMD −3.7%（vol 0.68× 低量），与 AVGO(−4.6%) 同向，属 Google-Marvell 定制芯片事件引发的 AI 芯片板块情绪扩散 + 长端利率久期挤压。无 AMD 公司级新闻，非事件直接相关方（AMD 不在 Google TPU 之争中），纯 beta 承压。

**Sources.**
- _Corroboration:_ AVGO −4.6% 事件驱动，AMD 情绪跟随；NVDA 仅 −1% 说明需求端未受损。低量下跌=情绪非基本面。

**Cross-assets.** SPY +0.21% · VIX 14.89 · TEN YEAR 4.65 · WTI 84.32

**Agent read.** 


---
### 2026-08-05 · -6.36% day · ▼ major
**Tags:** `earnings_post_print`, `guidance_inline`, `competitor_news`, `sector_rotation`
**Confidence:** high

**Primary cause.** Q2 2026 财报（8/4 AMC）后回吐。数字创纪录：营收 $11.54B，数据中心 $6.7B 同比 +107%（翻倍）——收入端毫无问题。但股价跌 6.4%，三个原因：(1) 前瞻指引不及预期 + 『令人震惊的 capex』担忧，在 fPE 66x 的估值上被定价为完美执行，一个『优秀但不惊艳』的季度即触发获利了结；(2) 期望被昨天提前打满——AMD 昨天 read-through Palantir 财报涨 9.3%（8/4 记录已预警『in-line 财报很可能吐回涨幅』），标准 buy-rumor-sell-news；(3) 同日『SpaceX 选 NVIDIA』新闻头条『Nvidia 赢下 SpaceX 大单，AMD 下沉』，强化 AI GPU 竞争中 AMD 是老二的叙事，NVDA +4.3%/AMD -6.4% 镜像。

**Sources.**
- Investor's Business Daily: [AMD Stock Tanks After Earnings, But The Dip Isn't Changing Wall Street's Or Retail Investors' Bullish View](https://finance.yahoo.com/quote/AMD/)
- GuruFocus: [Nvidia Just Won a Major SpaceX AI Deal. Stock Jumps as AMD Sinks](https://finance.yahoo.com/)
- _Corroboration:_ Morningstar 维持 FV $530；Susquehanna 7/30 上调 PT $450→$500；分析师均值 PT $579 vs 现价 $486（仍看多）；策略师原话『not an exceptional result』；数据中心 +107% 翻倍到 $6.7B

**Cross-assets.** SPY +0.03% · VIX 15.93 · TEN YEAR 4.62 · WTI 74.53

**Agent read.** 昨日（8/4）agent read 几乎逐字命中今天——原话『AMD 在别人的财报上涨 9.3%……一份仅仅 in-line 的财报很可能把涨幅吐回去』。这不是基本面转坏（数据中心翻倍、营收创纪录、华尔街 PT $579 仍在现价上方 20%），是『优秀财报撞过高期望 + 高 fPE 容错率低 + 竞争叙事』三杀，本质技术性回吐。30d 仅 -6.5% 远好于 MRVL/INTC 之前的 -28%。真正结构信号：供应商内部开始分化，NVDA（拿单龙头）vs AMD（丢单老二）过去两天走出剪刀差——比 supplier-vs-spender 板块轮动更细一层。可复用 takeaway：财报前 read-through 别人好消息大涨=明确卖出预警。
 · Snapshot at `dashboard/2026-08-05.md`

---
### 2026-08-04 · +9.26% day · ▲ major
**Tags:** `earnings_pre_print`, `sector_rotation`, `ai_demand`, `competitor_news`
**Confidence:** medium

**Primary cause.** Read-through from Palantir's blowout print (guided US commercial growth +134%), which validated enterprise-AI monetization and lifted the whole AI compute chain, combined with positioning ahead of AMD's own Q2 2026 report tonight (8/4 AMC). Financial media attributed AMD's gain directly to 'strong results from another key AI player' — i.e. not AMD's own fundamentals. Broad risk-on tape (S&P record high, WTI -5.6%) amplified it. AMD reclaimed its 50MA at $514.55.

**Sources.**
- Motley Fool: [Why AMD Stock Popped Today — The semiconductor specialist is gaining ground thanks to strong results from another key AI player](https://www.fool.com/)
- Investor's Business Daily/Yahoo: [Nvidia Tops Key Level As AMD Heads Into Earnings](https://finance.yahoo.com/)
- Yahoo: [Intel Soars 10%, AMD Jumps 8%, Broadcom Rises 6% as Chip Stocks Ride a Risk-On Rally](https://finance.yahoo.com/)
- _Corroboration:_ Sector-wide: SMH +6.0%, MRVL +13.8%, AVGO +7.4%, INTC +11.0%. Suppliers outran spenders (AMZN -2.4%, META -0.1%) for the first time since July.

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** The important observation is that AMD rose 9.3% on SOMEONE ELSE'S earnings, hours before reporting its own. That raises the bar tonight: the MI300/MI350 ramp numbers now have to clear an expectation set that was marked up 9.3% intraday on a read-through, so a merely in-line print likely gives the move back. volr 0.92x is the highest among today's semi gainers but still below average. Context worth preserving: AMD was flagged in timeline.yaml as 'the only large AI chip name that did not participate in the AMZN rally (5d -6.09% as of 7/31) — a test of whether the semi rebound can broaden'. That test has now resolved affirmatively; AMD went from sector laggard to +16.5% over 5 days and back above its 50MA, with 30d damage of only -4.0%, far milder than MRVL (-28%) or INTC (-28%). The broader structural signal today, corroborated by a headline titled 'Today's Trade Is to Buy Chips and Sell the Magnificent 7', is that capital rotated from AI spenders to AI suppliers for the first time since July — one day does not make a trend, but it is the first reversal of the dominant 30-day pattern in which spenders (MSFT +35%, AMZN +19%) crushed suppliers (NVDA +2%, everything else negative).
 · Snapshot at `dashboard/2026-08-04.md`

---
