# TSLA attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-07-02 · -8.03% day · ▼ major
**Tags:** `earnings_pre_print`, `macro_data`, `flow_event`
**Confidence:** high

**发生了什么。**

TSLA -8.03% ($390.83)。Q2 deliveries 480,126 units (+25% YoY)，beat 华尔街共识 406K 和 Deutsche Bank 416K est ~15%。数字是好数字。但股票大跌。

**为什么一个 beat 会跌 -8% — 四层因素叠加:**

**第 1 层: Sell-the-news 是预设的 (贡献约 -3~5%)**

过去三天 6/29-7/1 累计涨 +13% (6/29 +8.5%, 6/30 +2.1%, 7/1 +1.2%)。这 13% 就是市场在 price in "交付会 beat"。480K 确实 beat 了 — 但买的人三天前就已经买了。当利好兑现时，这些人获利了结。这就是 sell-the-news 的机制: 不是数字不好，而是 **知道数字好的人已经在价格里了**。

7/1 归因里预测 "480K inline → sell-the-news -3~5%" — 这部分完全对了。问题是: 为什么实际跌了 -8%? 多出来的 -3~5% 是什么?

**第 2 层: NFP +57K 宏观 shock 叠加 (贡献约 -2~3%)**

7/2 同一天早盘公布 June NFP +57K (预期 115K, prior 172K) — 四个月最弱。市场的解读分裂:
- 债市/黄金读作 "降息来了" (gold +1.5%, DXY -0.5%)
- 股市读作 "growth fear" → 经典 Dow-over-Nasdaq rotation: Dow +0.45%, Nasdaq -1.25%

TSLA 是 Nasdaq 里 beta 最高的个股之一 — macro growth fear 对高估值 growth stock 的杀伤力不成比例。如果今天没有 NFP miss，TSLA 可能只跌 -4~5% (纯 sell-the-news)。**NFP 把一个 routine 的 sell-the-news 升级成了一次 growth-fear rotation。**

**第 3 层: Michael Burry 做空 narrative anchoring**

6/30 13F 披露 Burry 新建 TSLA + NVDA 空头 (framing 为 "AI bubble")。这本身不是 timing signal (Burry 历史上常早 6-12 个月)，但在 +13% 快速拉升后 + NFP miss 叠加的环境下，它成了**卖方 narrative anchor** — 给犹豫要不要获利了结的人提供了一个 "理由": "连 Burry 都在做空了"。不是 cause，是 catalyst amplifier。

**第 4 层: Trefis $227 fair value 同日发布**

Trefis 在交付数据出来后同日发布 TSLA fair value $227 (当前价 -46%)。在一个已经在卖的日子里，一个 -46% 的 fair value 目标为空方提供了弹药。不是独立催化剂，但在多空博弈中改变了叙事平衡。

**关键逆向检验: RIVN +8%**

Rivian 同日也是交付日，也 beat — 而且涨了 +8%。这是极重要的反例: 如果今天是 "EV sector 被砸"，RIVN 应该一起跌。RIVN 逆势涨证明: **今天的跌是 TSLA-specific 的仓位/估值事件，不是 EV 行业逻辑恶化。** 市场没有在卖 "EV 未来不好了" — 它在卖 "TSLA 太贵了 + 利好兑现了"。

**为什么预测低估了幅度:**

7/1 预测 -3~5% 只考虑了 "sell-the-news" 单一因素。但 7/2 是三个 independent 催化剂同时发生:
- sell-the-news (TSLA-specific)
- NFP miss (macro, affects all growth)  
- Burry + Trefis narrative (TSLA-specific amplifier)

经验教训: **binary events 叠加宏观 data release 时，standard single-factor 预测幅度会被 50-100% overshoot。** 以后遇到 "催化剂日 + macro data 同日" 的情况，预测幅度应 ×1.5~2。

**什么会证伪 / 反转条件:**
- 7/22 Q2 earnings: auto GM ex-credits ≥ 18% + FSD revenue 首次 breakout → 确认 "数字好" 而不只是 "交付量大"
- 如果 7/22 auto GM < 15% → 交付量增长靠降价 → 利润质量差 → 这次 -8% 就不只是 sell-the-news 而是早期 warning

**Sources.**
- Yahoo/AFP: [Tesla global auto sales jump 25% in 2nd quarter, beating expectations](https://finance.yahoo.com/markets/stocks/articles/tesla-global-auto-sales-jump-164033967.html)
- Yahoo: [Tesla Second-Quarter Deliveries Top Views; Shares Fall Intraday](https://finance.yahoo.com/markets/stocks/articles/tesla-second-quarter-deliveries-top-165145095.html)
- TheStreet: [Michael Burry's newest short reveals what really worries him about AI](https://www.thestreet.com/investing/michael-burrys-newest-short-reveals-what-really-worries-him-about-ai)
- Trefis/Yahoo: [Why Patience Is The Real Catalyst For Tesla Stock (fair value $227)](https://www.trefis.com/articles/605509/why-patience-is-the-real-catalyst-for-tesla-stock/2026-07-02)
- BLS: June NFP +57K (vs est 115K, prior 172K)
- _逆向检验:_ RIVN +8.08% (同日交付 beat) — EV sector 没问题，是 TSLA-specific

**Cross-assets.** SPY -0.51% · Nasdaq -1.25% · Dow +0.45% · VIX 16.75 · RIVN +8.08% · Gold +1.5% · DXY -0.5%
 · Snapshot at `dashboard/2026-07-02.md`

---
### 2026-07-01 · +1.20% day · ▲ major
**Tags:** `earnings_preview`, `risk_on`
**Confidence:** high

**Primary cause.** Q2 delivery pre-positioning; 3rd consecutive up day (6/29 +8.5%, 6/30 +2.1%, 7/1 +1.2%) into 7/2 delivery report. Gary Black: rising oil prices boosted Q2 expectations. Independent from semi selloff — Tesla is AI deployer not chip seller.

**Sources.**
- Yahoo: Tesla Stock Rides a 10% Weekly Gain Into a High-Stakes Delivery Report
- Yahoo: Gary Black Dismisses FSD Hype, Says Rising Oil Prices Boosted Q2 Delivery Expectations
- Yahoo: YPF to Collaborate With Tesla on Energy Storage + Fast-Charging
- _Corroboration:_ Michael Burry shorts TSLA+NVDA (6/30 confirmed) — first named contrarian signal

**Cross-assets.** SPY +0.08% · VIX 16.37 · TEN YEAR 4.47 · RIVN PCT weak · NIO PCT weak

**Agent read.** 5d +13.3%全押Q2交付。Binary event 7/2: >=480K确认bull看7/22; 406-480K inline可能sell-the-news -3~5%; <=445K部分回吐5-8%。Vol从1.21x→0.89x→0.5x递减=追涨热度降低。Burry做空是记录但非timing信号(历史早6-12mo)。距thesis-break $250缓冲+70%。
 · Snapshot at `dashboard/2026-07-01.md`

---
### 2026-06-30 · +2.13% day · ▲ minor · Q2 季度截止日（非交付发布日）
**Tags:** `earnings_preview`, `risk_on`, `thesis_debate`
**Confidence:** medium

**Primary cause.** 收 +2.13% 到 $420.60（5d +10.2%，连同 6/29 的 +8.46% 两日强势）。risk-on（道指收新高）+ Q2 交付预设利好。**时点澄清：6/30 是 Q2 季度截止日，不是发布日 —— Tesla Q2 P&D 预计 7/2 公布（"on or around July 2"），华尔街共识 bar 406,024。** 今天市场在预期上买，数字未出。vol 0.89x 接近均值，有真实买盘（比早盘 0.42x 放大）。

**Sources.**
- Yahoo: [Michael Burry bets against Tesla, Nvidia in new AI bubble short positions](https://finance.yahoo.com/)
- Yahoo: [SpaceX and Tesla Shares Are Trading Like Twins](https://finance.yahoo.com/)
- Yahoo: [Tesla Stock Falls After Big Gains as Auto Industry Wrestles With Copper Prices](https://finance.yahoo.com/)

**Cross-assets.** SPY +0.79% · QQQ +1.70% · DJI 收历史新高 · vol_ratio 0.89

**Agent read.** **首个有名望逆向信号：Michael Burry 新建 TSLA + NVDA "AI bubble" 空头。** 历史上 Burry 做空 megacap 常早 6-12 个月，不是即时 timing 信号，但值得记录——这是 6 月以来第一个 named 的逆向押注。"SpaceX/Tesla trading like twins" 说明被当同一 Musk-AI 叙事交易，Burry 情绪若蔓延会波及 SPCX。交付数字是真正判定点：≥480k 确认强势看 7/22 财报；≤445k 则今天涨是"卖事实"前夜。距 thesis-break $250 缓冲 +68%。维持 watch，数字明朗前不加减。
 · Snapshot at `dashboard/2026-06-30.md`

---

### 2026-06-29 · +8.46% day · ▲ major
**Tags:** `risk_on`, `macro_geopolitics`, `short_covering`
**Confidence:** medium

**Primary cause.** EOD update: TSLA 收盘 +8.46% (盘中曾 +7.7%, 尾盘加速)。Beta + 6/30 Q2 交付预设利好 + 30d -7.7% 后空头回补;Vol 1.21x (升至均值之上,首次有 institutional 加码迹象) — 与盘中 0.79x 相比信号变了。新闻面 idiosyncratic 仍偏负 (Rivian quality, fierce new rival);涨幅完全靠 macro + 交付 expectation。明天交付数据是真正判定点;共识 ~460k,>=480k = 确认,<=445k = 大幅回吐。

**Sources.**
- Yahoo: [US Equity Indexes Rise as Communication Services Tops Sector Charts, Trump Sends Envoys to Qatar for Iran Talks](https://finance.yahoo.com/)
- Yahoo: [Tesla Faces Fierce New Rival in Self-Driving Race](https://finance.yahoo.com/)
- Yahoo: [Comcast, Charter, Rocket Lab, SpaceX, Tesla, and More Stocks That Explain Today's Market](https://finance.yahoo.com/)

**Cross-assets.** SPY PCT +1.65% · QQQ PCT +2.49% · VIX 17.65 · TNX 4.37 · VOLUME RATIO 1D 1.21

**Agent read.** 
 · Snapshot at `dashboard/2026-06-29.md`

---
### 2026-06-23 · -4.81% day · ▼ material
**Tags:** `regulatory_negative`, `safety_recall`
**Confidence:** high

**Primary cause.** Texas fatal crash 引发联邦调查 (NHTSA probe)。这是独立于今日 chip selloff 的单一公司事件 — FSD/Robotaxi 期权价值的重新定价 trigger。一条对冲性正面新闻 (NatPower Megapack 订单) 未能抵消监管风险权重。

**Sources.**
- Yahoo: [Tesla pushes back as fatal Texas crash reignites self-driving scrutiny](https://finance.yahoo.com/markets/stocks/article/tesla-pushes-back-as-fatal-texas-crash-reignites-self-driving-scrutiny-173130065.html)
- Yahoo: [Tesla faces federal probe into fatal crash: What it means for Robotaxi & full self-driving](https://finance.yahoo.com/video/tesla-faces-federal-probe-fatal-173000695.html)
- Yahoo: [Tesla Faces New Crash Probe](https://finance.yahoo.com/markets/stocks/articles/tesla-faces-crash-probe-161420002.html)
- Yahoo: [Tesla Locks In a Major European Megapack Deal With NatPower (对冲新闻 — 未抵消)](https://finance.yahoo.com/energy/articles/tesla-locks-major-european-megapack-170940018.html)

**Cross-assets.** SPY -0.97% · VIX 18.75 · TEN YEAR 4.49

**Agent read.** FSD/Robotaxi optionality 重新定价。对比 6/18 attribution (Sweden EU 阻力 + Waymo recall = 净 +1%)，今天没有对冲新闻 + 国内联邦介入 = -4.81%。说明监管负面催化的市场权重显著上升。历史 NHTSA 调查反应路径: (1) 调查初期 -5% 到 -8% 单日 (今天对得上); (2) 后续两周窄幅震荡; (3) 调查结果决定方向 — hardware recall 则另 -10%, 软件 OTA 则迅速回血。vol_ratio 0.60 = 同样没有大规模机构 capitulation。距 thesis-break $250 仍有 +54% 缓冲。下个催化: 联邦调查初步结论 (估 2-3 周) 或下次 robotaxi 进展。
 · Snapshot at `dashboard/attribution-2026-06-23.md`

---
### 2026-06-18 · +1.04% day · ▲ minor
**Tags:** `regulatory_negative`, `competitor_news`
**Confidence:** low

**Primary cause.** Mixed: Sweden EU FSD friction (negative) absorbed against Waymo recall (competitive positive); net up 1% suggests market weighted Waymo competitive read more

**Sources.**
- Yahoo/IBD: [TSLA Stock: Major Roadblock For Tesla FSD As Sweden Reportedly Opposes EU-Wide Approval](https://finance.yahoo.com/)
- Yahoo: [Waymo Has a Tesla-Like Recall. What It Means for Alphabet Stock](https://finance.yahoo.com/)

**Cross-assets.** SPY +0.40% · VIX 14.2 · TEN YEAR 4.31

**Agent read.** Classic post-rally consolidation between $289 floor and $499 high. Today's headlines were a wash. Stock up 1% on net-negative-to-mixed news = bullish-leaning absorb. Autonomy option still pricing the optionality. Bear probability remains 35%. Nothing today changes the thesis.
 · [Snapshot](snapshots/2026-06-18.md)

---
