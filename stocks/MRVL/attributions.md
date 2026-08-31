# MRVL attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-08-31 · -2.25% day · ▼ minor
**Tags:** `earnings_post_print`, `flow_event`, `sector_rotation`
**Confidence:** medium

**Primary cause.** 8/27 beat+raise 财报后连续第三个交易日下跌, 5d -11.89%。今天的新信息是: 在半导体板块普涨的背景下 MRVL 独跌 — 同日 SNDK +5.02%, MU +2.53%, SKHY +2.34%, NVDA +1.32%, AMD +1.14%, AVGO +0.49%。这意味着卖压已从板块效应转为个股层面的持续压力。消息面今天全部偏正面且与股价方向脱节: 'Could Marvell Be the Next $100 Billion AI Stock?', 'Marvell and Google: Misplaced Fear Should Drive Your Purchase Decision', 分析师看 +34.31% 上行空间。催化剂与价格背离通常指向仓位驱动而非观点驱动的卖出 — 即财报后的持仓再平衡/减仓仍在进行, 而不是有新的坏消息。距 triggers.yaml 的 thesis_break_price $200 只剩 +5.9% 缓冲 (8/28 时为 +8.7%, 三个交易日收窄 2.8pp)。

**Sources.**
- _Data:_ MRVL $211.73, 1d -2.25%, 5d -11.89% (由 5m intraday bar 重建真实日收盘; 上游 yfinance 日线缺失 2026-08-28 bar)。距 thesis_break_price $200 缓冲 +5.87%。成交量比 0.82x — 低于均量, 卖压持续但不放量。 ()
- _Corroboration:_ 逆向检验坐实为个股问题: 同日半导体全线上涨 (SNDK +5.02, MU +2.53, SKHY +2.34, NVDA +1.32, AMD +1.14, AVGO +0.49), 仅 MRVL 与 TSM (-0.41%) 为负, 而 MRVL 跌幅是 TSM 的 5 倍。若为板块或利率原因, MRVL 不应独跌。『四绿一黑』判据成立。
- Yahoo Finance: Could Marvell Be the Next $100 Billion AI Stock?
- Yahoo Finance: Marvell and Google: Misplaced Fear Should Drive Your Purchase Decision
- Yahoo Finance: Wall Street Analysts Believe Marvell (MRVL) Could Rally 34.31%: Here's is How to Trade

**Cross-assets.** SPY -0.35% · VIX 15.01 · TEN YEAR 4.76 · WTI 85.94 · SECTOR ETF +1.78%

**Agent read.** 这是当前持仓里最接近预先承诺触发点的名字, 且方向持续不利。三个交易日内缓冲从 +8.7% 收窄到 +5.9%, 若延续同样速度将在下周内触及 $200。关键观察: 卖压与消息面完全脱节 (今日消息全正面, 分析师看 +34% 上行), 这通常意味着卖方是财报后的仓位再平衡而非观点转变 — 这类卖压的特征是会自行耗尽, 但耗尽前不可预测持续多久, 且成交量 0.82x 低于均量说明还没到抛售高潮。MRVL 现在是 8 月『好财报换不来上涨』序列里最极端的样本 (beat+raise 却 5d -11.9%), 因此它对 9/2-9/3 AVGO 财报有直接的预示价值: 若连 AVGO 这个期望透支最少的名字也被卖, 则问题在 regime 层面。行动纪律: $200 是 triggers.yaml 里已写入的预先承诺线 — 触及时应按预先约定重新审视论点, 而不是等更低价格再决定。这正是预先承诺机制存在的目的。
 · Snapshot at `dashboard/2026-08-31.md`

---
### 2026-08-28 · -10.32% day · ▼ major
**Tags:** `earnings_print`, `guidance_raise`, `macro_rates`, `sector_rotation`, `prediction_passed`
**Confidence:** high

**Primary cause.** Q2 FY27 财报 beat+raise (data center 强劲, 指引上调到~50%增长, AWS Trainium ramp 兑现) 仍暴跌 -10.3% —— 教科书 sell-the-news, 三链叠加: (1)估值链: 年内曾+196%好消息已 priced in, 达预期≠超预期; (2)regime链: Warsh 同日 Jackson Hole 抬升利率预期, 10Y 逼近52w高, 鹰派下高倍数不再享受降息加成, 好财报换不来 rally 反触发倍数压缩; (3)稀释链: 8/19 Google $12B 订单 warrant 稀释担忧前置压制, 财报未彻底盖过。跌幅超普通财报(-10% vs ±5%)因宏观(高预期+高久期双杀)+光网络板块级估值重定叠加。现价$217从 base($330-350)贴近 bear($180)=基本面交出base但倍数压到bear定价。

**Sources.**
- : 
- {"type": "reverse_check", "note": "AVGO \u540c\u65e5\u4ec5 -1.2% \u672a\u5927\u8dcc \u2192 \u975e\u7eaf ASIC \u677f\u5757\u5d29, \u662f MRVL \u4e2a\u80a1\u9ad8\u9884\u671f+\u5149\u7f51\u7edc\u677f\u5757\u4f30\u503c\u91cd\u5b9a"}
- {"type": "prediction_score", "note": "\u8bc4\u5206 8/21 \u8bb0\u5f55\u7684 prediction (score_date 8/27): \u4e8c\u5143\u88c1\u51b3\u7b2c\u4e8c\u5206\u652f(sell-the-news, \u9e70\u6d3e regime \u597d\u8d22\u62a5\u2260\u597d\u53cd\u5e94)\u5750\u5b9e \u2192 PASSED\u3002\u7ee7 NVDA 8/26 \u4e4b\u540e\u540c\u4e00 regime \u5224\u65ad\u7b2c\u4e8c\u6b21\u72ec\u7acb\u786e\u8ba4\u3002"}

**Cross-assets.** SPY -0.19% · VIX 14.46 · 10Y 4.71 · AVGO -1.22% · NVDA -3.31% · DXY +0.47%

**Agent read.** high 质量归因。3天内第二只 AI 芯片好财报被卖(继 NVDA)。距 break $200 缓冲仅+8.7%(warn区)。9/3 AVGO 是芯片端 de-rating 三连的决定性第三探针。


---
### 2026-08-21 · -5.33% day · ▼ material
**Tags:** `secondary_offering`, `competitor_news`, `earnings_pre_print`
**Confidence:** high

**Primary cause.** 8/19 Google $12B定制芯片订单的利好反转,三条相互强化: (1)订单附带认股权(warrant)稀释,摊薄每股价值,净效应由正转负,市场卖出部分8/19涨幅; (2)竞争叙事分裂,一派认为Alphabet宣布后AVGO仍是更好买入,质疑MRVL份额持续性; (3)8/27财报前去风险,年内已+196%,高预期+不确定性下部分资金落袋。但5d仍+7%,核心利好未被完全否定,只被稀释和不确定性打折。

**Sources.**
- : 
- {"type": "reverse_check", "note": "AVGO\u540c\u65e5+0.7%\u672a\u8ddf\u8dcc \u2192 MRVL\u4e2a\u80a1(\u7a00\u91ca)\u4e8b\u4ef6\u975eASIC\u677f\u5757\u666e\u8dcc"}
- _Corroboration:_ 关联8/19已记录归因(partnership_news+competitor_news),今天是同一事件链第二幕:利好→稀释重定价

**Cross-assets.** SPY +0.38% · VIX 15.29 · 10Y 4.74 · WTI 87.27

**Agent read.** 利好反转+财报前去风险,三催化相互强化成-5.3%,但5d+7%说明Google大单核心逻辑未破。距break $200缓冲+19%。8/27财报前波动加大,关注PRICE REACTION不是数字本身。


---
### 2026-08-19 · +9.85% day · ▲ major
**Tags:** `partnership_news`, `competitor_news`
**Confidence:** high

**Primary cause.** MRVL +9.85%（vol 1.86× 放量），Google 以约 $12B warrant/股权把 Marvell 纳入其定制 AI 芯片(TPU)设计供应 bench。头条一致：「Marvell Stock Rises 10% on Google Warrant Deal」「Inside Google's $12B Stake in Marvell—Why It's Bad News for Broadcom」。市场解读：MRVL 获巨型高确定性新客户订单流，直接做多定制芯片 TAM。**这是对昨日(8/18) MRVL −8.24% 宏观(升息)抛售的 V 型反转——个股硬催化压过 macro_rates 逆风**，说明份额型 partnership 新闻的权重高于利率 beta。8/27 Q2 FY27 财报双重加载：刚 +10% 带催化进财报，管理层强动机讲胜利故事。距 thesis-break $200 缓冲 +18.6%。

**Sources.**
- secondary: [Marvell Stock Rises 10% on Google Warrant Deal](https://finance.yahoo.com/)
- secondary: [Inside Google's $12 Billion Stake in Marvell—and Why It's Bad News for Broadcom](https://finance.yahoo.com/)
- _Corroboration:_ 镜像交易：AVGO 同日 −4.6%（vol 1.78×）确认零和份额转移；GOOG +0.12% 平静=市场读为供应链多元化非 capex 失控；TSM 走平=代工层中立。

**Cross-assets.** SPY +0.21% · VIX 14.89 · TEN YEAR 4.65 · WTI 84.32

**Agent read.** 


---
### 2026-08-18 · -8.24% day · ▼ major
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** MRVL −8.2%，AI 芯片供应端领跌。直接叙事：升息 (10Y 停 52w 高) 盖过 UBS 看多 AI 的研报——媒体标题「Rising Treasury Yields Swamp a Bullish UBS AI Note」。作为最高 beta/最高久期的二线 AI 供应端，在「AI 开支质疑」(neocloud 超支恐慌 + META 费用 +55% 被点名) 的一天首当其冲。叠加结构性供给利空：8 月内部人已套现 $632M（股价 +160% 后）。**距 thesis-break $200 仅 +7.5% 缓冲——进入 10% 警戒区**，8/27 Q2 FY27 财报 (AWS Trainium ramp) 定生死。

**Sources.**
- secondary: [Marvell Technology Drops 6% as Rising Treasury Yields Swamp a Bullish UBS AI Note](https://finance.yahoo.com/)
- secondary: [Marvell Insiders Sell $632 Million as Stock Soars 160%](https://finance.yahoo.com/)
- _Corroboration:_ 同日 AI 芯片链齐跌：INTC −7.0/TSM −4.1/AVGO −2.8/NVDA −2.1；但 hyperscaler 开支方 MSFT/AMZN 逆势稳——沿「卖算力 vs 花钱」分化。

**Cross-assets.** SPY -0.52% · VIX 15.66 · TEN YEAR 4.71 · WTI 84.14

**Agent read.** 


---
### 2026-08-10 · -2.49% day · ▲ medium
**Tags:** `sector_rotation`
**Confidence:** medium

**Primary cause.** 5d +10% 由 AI custom silicon (AWS Trainium SerDes) 叙事驱动，但今日 -2.5% 跟随 AI 芯片全线回吐 ($500B 财团报道 = vendor-financing 担忧)。30d 仍 -20%，深坑未填。

**Sources.**
- Barron's/IBD: Wall Street Mobilizes $500 Billion Consortium With Nvidia to Underwrite AI Infrastructure

**Cross-assets.** NVDA -2.17% · INTC -2.58%

**Agent read.** 5d 触发 (+10%) 但今日方向向下。MRVL/INTC 是 AI capex cluster 弱势一端 (30d -20%/-23%)。8/27 财报 (Trainium ramp) 是下一个验证点。


---
### 2026-08-04 · +13.80% day · ▲ major
**Tags:** `policy_us`, `geopolitical_trade`, `policy_china`, `ai_demand`, `sector_rotation`
**Confidence:** high

**Primary cause.** Report that the US plans to restrict Chinese-made data-center components (optical modules / interconnect). Direction is the INVERSE of the usual 'China restriction -> US chip stocks fall' pattern: this time the restricted party is Chinese SUPPLY, so US-domiciled optical-interconnect vendors are the beneficiaries. MRVL's core business is data-center optical interconnect SerDes/DSP, making it the single largest beneficiary. Corning, Lumentum, and Coherent moved together, confirming the mechanism. Secondary contributors: MRVL showcased its AI memory/storage portfolio at the Future of Memory and Storage 2026 conference, and the broad risk-on tape (S&P record high).

**Sources.**
- Barron's/Yahoo: [Marvell Surges as China Ban Report Reignites Optical-Networking Stocks](https://finance.yahoo.com/)
- Yahoo: [Marvell, Sandisk, SK Hynix lead semiconductor stock rally as S&P 500 trades at record highs](https://finance.yahoo.com/)
- _Corroboration:_ Corning, Lumentum, Coherent all rose on the same report — the optical-interconnect basket moved as a group, not MRVL alone. NOK +7.3% also partially attributable (optical network equipment).
- Simply Wall St/Yahoo: [Marvell Technology (MRVL) Could Be 38% Above Fair Value As AI Narrative Builds](https://finance.yahoo.com/)

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** Quality 7/10. This is the most STRUCTURAL of today's catalysts — if the rule is actually promulgated, MRVL's competitive position improves permanently rather than for one quarter, because Chinese optical-module suppliers are its main price competition. That is categorically different from the short-squeeze moves elsewhere in the tape today (INTC +11% with zero company catalyst). Two caveats that must not be lost: (a) this is still a REPORT — no formal rule text has been published, so it should not be priced as fact; (b) volr 0.85x means even the largest single-name gainer among semis lacked volume confirmation. MRVL remains 9% below its 50MA ($240) and -28% over 30 days, so this is repair from a deep hole, not a breakout. Confirmation point is the 8/27 Q2 FY2027 earnings call, where management must both validate the China-restriction tailwind and show the AWS Trainium SerDes ramp. Expectations are now higher going into that print. Also note MRVL was newly added to the workspace watchlist last week (7/30) and is already the second-largest gainer — the timing of that addition looks good but the position is now 26% higher over 5 days, so entry risk has increased.
 · Snapshot at `dashboard/2026-08-04.md`

---
