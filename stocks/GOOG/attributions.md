# GOOG attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-28 · +1.60% day · ▼ major
**Tags:** `earnings_print`, `earnings_post_print`
**Confidence:** high

**Primary cause.** **正常时段收 $321.89 / +1.60%, 但盘后财报后 $291.61 / −9.41% (ET 17:08 快照; 另一源 $294.40 / −9.39%)。方向与幅度按盘后记。** 数据取自 SEC 8-K Ex-99.1 原文 (accession 0001652044-26-000080), 非媒体转述。||**🔴 EPS「miss」不是经营问题, 这是本条归因最重要的一点。** 共识 EPS $3.02 实际 $2.12 (差 $0.90, −29.8%), 而同一份报表里**营业利润 +30% 至 $405.76亿、营业利润率由 31% 升到 31.8%、营收 +25% 至 $1,275.77亿 (第 13 个连续双位数增长季)**。差额全在一行: **`Other income (expense), net` 由上年同期 +$127.59亿 变成 −$82.21亿, 单季摆动 −$209.80亿**; 现金流量表给出构成: `Loss (gain) on debt and equity securities, net` 本季为 **+$90.48亿亏损** (上年同期 −$108.55亿收益)。这是 ASC 321 持有股权投资按市价重估, 不是业务事件。||**由此得出对估值直接有用的推论: GOOG 尾随 PE 16.09x 被投资收益美化。** 同表显示**今年前九个月 `Loss (gain) on debt and equity securities, net` 累计为 −$1,267.55亿收益**, 而前九个月净利 $2,012.39亿 → **今年至今报表利润约 63% 来自证券重估而非经营**。远期 21.11x 才是可用数字。||**🔴 三条媒体口径与 8-K 原文直接矛盾, 必须随记录保存**: (a)「revenue miss」(Reuters 框架) —— 实际营收 $1,275.77亿 vs 共识 $1,272.2亿 = **小幅超预期**; (b)「Search growth slows」(IBD 标题) —— 实际 Google Search & other **+12% 至 $633.50亿**, 且 Pichai 原话「**our year-over-year query growth rate is the highest it's been in the last five years**」= **反向错**; (c)「ad slowdown」(AFP) —— Google 广告合计 **+10.6%** 至 $820.12亿, YouTube 广告 +9.2%, 订阅/平台/设备 +11.0%。**而有一家说对了: Reuters 另一条标题「Alphabet's heavy cloud spending drives bigger-than-expected cash burn」, 与报表和 −9.41% 完全一致。** → **市场反应对的是正确的东西(现金消耗), 大部分媒体给的理由是错的。形态值得记: 盘后报道在半小时内写成, 取的是「EPS vs 共识」这个最容易拿到的数字, 而真正驱动价格的在现金流量表第二页。今后遇到「营收超预期 + EPS 大幅 miss」的组合, 第一个查的不是新闻, 是 Other income (expense), net 与 capex÷经营现金流。**||**真正的驱动是自由现金流: Q3 经营现金流 $422.90亿 (同比 −12.6%)、capex $513.55亿 (同比 +114%) → 自由现金流 −$90.65亿。季度轨迹: Q4 2025 +$245.51亿 → Q1 2026 +$101.16亿 → Q2 2026 −$58.55亿 → Q3 2026 −$90.65亿 = 连续两季为负且在加深; TTM 仍为 +$197.47亿。capex ÷ 经营现金流 = 121.4%。** 同季外部融资: **ATM 增发 12M Class A ($43亿) + 24M Class C ($81亿) = $124亿** (剩余额度 $276亿) + **高级无抵押债净募集 $287亿** = 本季 **$411亿**, 另有强制可转换优先股 (Series A/B, 季度股息 $15.63/股)。折旧 $83.69亿 vs $56.11亿 = +49% (capex 开始压 P&L)。||**经营层实际是一份强于 MSFT 的财报**: Google Cloud **+103% 至 $307.09亿** (创纪录; GCP 企业 AI 基础设施与解决方案驱动, 且**「TPU systems sales were also a meaningful contributor」**), Cloud 营业利润 **$111.21亿 vs $35.94亿 = +209%**, 利润率 **36.2% vs 23.7% 跳升 12.5pp**。Google Services +11% 至 $963.02亿。Alphabet-level activities (共享 AI 研发) 支出 −$76.55亿 vs −$44.67亿 = +71%。员工 204,757 vs 190,167。Pichai: 已达半万亿美元营收年化运行率; Gemini app 达 10 亿用户; 第一方模型 API 每分钟处理近 320 亿 token (同比 4 倍); YouTube Music+Premium 超 1.5 亿订阅。||**🚨 风控: thesis_break $280, 盘后 $291.61 → 缓冲 +4.15%, 进入 5% 危险区**, 成为 NOK (+0.9%) 之外第二只。盘中报告记录的缓冲是 +14.5%。注意**逼近的机制与风控线设定理由不同**: thesis.md 原文设 $280 的理由是「~24% below current; near bear-case scenario price」即度量「市场放弃成长定价」, 而今天逼近它的是自由现金流为负 + 投资重估亏损, 两条都不在设定时的情景里 —— **与 NOK 结构相同(击穿线的是成本过账能力, 触发器写的是需求与竞争)**。||**🔴 kill-condition 错配第十例, 且形态最极端 —— 不是「没触发」而是「被主动证伪」。** 三条原文逐条: #1「Search query **volume** declines YoY for two consecutive quarters」→ **被 Pichai 具名否定(查询量增速五年最高), 推得最远**; #2「DOJ wins structural remedy」→ 今天无进展; #3「Google Cloud loses market share to AWS/Azure for two consecutive quarters」→ **被数据直接否定(Cloud +103% vs Azure +48%, 增速 2.1 倍, 利润率跳升 12.5pp)**。**三条里两条在同一天被具名否定, 朝着更安全的方向走, 而价格跌进风控区。** 真正打穿价格的机制(capex 超过经营现金流→FCF 转负→需要外部资本)在三条里完全不存在, **与同日 META 的缺口是同一类型** → **建议给 GOOG 与 META 加同一条 kill condition(措辞统一便于横向比较): 「自由现金流(经营现金流−capex)连续两个季度为负, 或 capex ÷ 经营现金流连续两季超过 100%」。按此 GOOG 今天已触发(Q2 −$58.55亿 + Q3 −$90.65亿, 比率 121.4%), META 触发一半(首次为负待第二季确认)。这是本工作簿第一次有一条拟议触发器在提出当天就能回溯判定为已触发。**||未取到: Alphabet 全年 capex 指引 (电话会 16:30 ET 已开始但检索窗口内未取到指引数字) —— 连续两季负 FCF 之后, 管理层对 2027 capex 的口径决定 −9.41% 是一次性重定价还是趋势起点。

**Sources.**
- {"type": "filing", "title": "Alphabet Announces Third Quarter 2026 Results (SEC 8-K Ex-99.1, accession 0001652044-26-000080)", "publisher": "SEC EDGAR"}
- Reuters: Alphabet's heavy cloud spending drives bigger-than-expected cash burn
- MT Newswires: Alphabet Third-Quarter Results Miss Estimates as Capital Spending More Than Doubles
- Investor's Business Daily: Google Earnings Miss As Cloud Computing Booms, Search Growth Slows
- (aggregated): Alphabet Stock Falls 8% Even as Cloud Sales Double: Is AI Spending the Problem?

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-10-22 · -3.36% day · ▼ material
**Tags:** `sector_rotation`, `earnings_pre_print`
**Confidence:** high

**Primary cause.** AI 开支方整组下跌，无 GOOG 自身负面消息。||**今天的公因子是融资。** META 上调 2026 capex 下沿至 $1,350-1,450亿 + 季度 FCF 转负 + 新设无投票权股融资 → -7.91%; **四家大科技 (META/AMZN/GOOGL/MSFT) CDS 创数月新高 — 融资担忧第一次从边缘搬到投资级核心**。同时 2Y -17.3bp / 10Y -18.1bp 平行下行、TLT +2.03%、债市撤回加息押注 → 折现率给了近 20bp **顺风**而权益仍跌, 跌幅必须由风险溢价全额解释。参与度: 全场量比中位数 0.79x, 仅 10/35 过 1.0x。||**新判别轴「内生融资 vs 需要外部资本」**: MSFT (内生充裕、无增发信号) -2.02% 且是十只 AI 标的里**唯一仍在 MA50 上方的** (+2.8%, 30d +6.04%); GOOG -3.36%; AMZN -4.82%; META (FCF 转负 + 融资股票) -7.91%; SPCX (FY27 FCF -$670亿) -8.94%。**这解释了 MSFT 的例外 —— 不是因为便宜 (远期 22.0x 比 AVGO 16.7x / TSM 17.6x 贵)，也不是久期短，而是 capex 全部由内生现金流覆盖。10/28 MSFT 的 capex 口径是这个轴能否保留的直接检验。**||**市值口径: 自 10/06 以来 GOOG -$2,430亿，是 Mag7 里第二大的绝对流出** (NVDA -$6,230亿 第一)。同期 AAPL +$1,630亿 / LLY +$1,500亿 / WMT +$1,000亿 —— 轮动的来源与落点都已具名。||**🎯 10/28 财报与 MSFT capex 指引、GEV 财报、FOMC 同日 (四重叠加)。GOOG 要在已经知道「META 因上调 capex 下沿 + FCF 转负被罚 7.91%」的情况下给自己的数字 —— 这是一个罕见的、管理层拥有完整前例信息的指引日。** 具体看点与 MSFT 相同: (1) capex 是否上调; (2) 是否提及任何外部融资安排。||一条口径对照值得记: D.A. Davidson 的 Luria 在解释 META 时说 META「正在从 Google 抢份额」，广告销售增速在 20% 以上。**所以同一篇分析里 META 的基本面被认为强于 GOOG，而 META 跌 7.91%、GOOG 跌 3.36% —— 再次说明今天定价的不是竞争地位，是融资结构。**||位置: vs MA50 $340.03 偏离 -5.9%; 距 52w 高 $404.47 为 -20.92%; 远期 PE 20.8x。||5d -7.27% 是开支方里第二差 (仅好于 META -12.81%)，说明 GOOG 的卖压在 META 财报前就已经开始累积。

**Sources.**
- {"type": "credit", "title": "META / AMZN / GOOGL / MSFT \u56db\u5bb6 CDS \u521b\u6570\u6708\u65b0\u9ad8", "publisher": "Yahoo Finance"}
- {"type": "computed", "title": "\u81ea 10/06 \u5e02\u503c -$2,430\u4ebf, Mag7 \u7b2c\u4e8c\u5927\u7edd\u5bf9\u6d41\u51fa", "publisher": "Yahoo Finance"}
- {"type": "analyst", "title": "D.A. Davidson (Luria): META \u6b63\u5728\u4ece Google \u62a2\u4efd\u989d, \u5e7f\u544a\u589e\u901f 20% \u4ee5\u4e0a \u2014 \u800c META \u8dcc\u5e45\u662f GOOG \u7684 2.4 \u500d", "publisher": "Yahoo Finance"}

**Cross-assets.** SPY -1.44% · VIX 19.37 · TEN YEAR 4.957 · TWO YEAR 4.65 · WTI 99.19 · DXY 101.6 · GOLD 4055.4 · BTC 81063

**Agent read.** 同一篇卖方分析认为 META 基本面强于 GOOG, 而 META 跌幅是 GOOG 的 2.4 倍 — 这是今天「定价的不是竞争地位而是融资结构」的一个干净对照。10/28 GOOG 会在拥有完整前例信息的情况下给指引, 这让它的口径选择本身成为信息。
 · Snapshot at `dashboard/2026-10-22.md`

---
### 2026-09-23 · -3.71% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`, `macro_inflation`
**Confidence:** high

**Primary cause.** GOOG -3.71%，全持仓当日最大个股跌幅，且同日跌破 MA50 ($343.3) 与 MA200 ($336.5)。无任何公司级催化剂——无评级调整、无目标价变动、无反垄断或监管动作。驱动是两条叠加：(1) 10Y 收益率升至 5.12%、2007 年以来最高（+16bps，^FVX +3.86% 领涨确认为加息预期而非财政溢价），折现率冲击打击久期最长的大盘科技；(2) 大盘科技内部轮动——同日 META +1.82%（放量 1.06x，距 52w 高仅 1.8%）、MSFT +0.38%，媒体框架为 'AI Rotation Splits Big Tech'，资金自 GOOG 流向 META。Yahoo Chart of the Day 'AI growth rests on Big Tech cash flow tripling to $2 trillion' 提供分母端质疑燃料。上游成因是油价：白宫权衡柴油出口禁令 + 伊朗总统强硬表态推 WTI 盘中 +0.98%，通胀预期上修 → 加息定价。

**Sources.**
- : [10-year Treasury yield hits highest level since 2007 as market prices in another Fed rate hike](https://finance.yahoo.com/quote/%5ETNX/)
- : [Stocks, Bonds Slip as Oil Jump Fuels Fed-Hike Bets (Bloomberg)](https://finance.yahoo.com/quote/CL%3DF/)

**Cross-assets.** SPY CHANGE -0.74% · VIX 15.34 · TEN YEAR 5.12 · WTI 91.41 · DXY 101.19 · QQQ CHANGE -1.01%

**Agent read.** 关键机制是 GOOG 承受双通道利率打击，而多数持仓只承受一条。thesis 已记录 FCF 同比 -47%、总债务 +284% 至约 $900 亿——Google 在借钱投 AI，因此除折现率通道外还有真实利息支出通道，-3.71% 在机制上合理而非过度反应。GOOG 距 thesis-break $280 缓冲 +19.5%，是全持仓最薄（次为 AVGO +18.3%、NOK +18.0%），需单独盯住。下跌可逆（叙事未坏）但缺少可反转的具体事件，须等 10-28 财报——而那天 GOOG/META/MSFT/GEV 财报 + FOMC 五事件撞车，事后无法归因，须事前写预期。深层观察：高利率下市场对『远期更优』（Spark 被认为长期胜 Muse）支付意愿下降，对『当期已有』（Muse）上升。
 · Snapshot at `dashboard/2026-09-23.md`

---
### 2026-07-31 · +5.99% day · ▲ material
**Tags:** `sector_rotation`, `ai_demand`, `competitor_news`
**Confidence:** medium

**Primary cause.** Sector re-rating spillover, not company news. AMZN's AWS +37% raised the market's baseline confidence in the cloud+AI monetization link, so GOOG Cloud's +28% looks acceptable under the new baseline and last week's ~10% overshoot punishment reverses.

**Sources.**
- IBD via Yahoo: Amazon Stock Soars As AI Strategy Sends It To 'Top Of The Cloud Wars'
- Benzinga via Yahoo: RDDT Stock Set For Worst Day On Record — Reddit Advances Copyright Suit Against Perplexity, amid Google search traffic fluctuations
- _Corroboration:_ Volume only 0.76x — low-volume advance = short covering + reversal of last week's overshoot, NOT new institutional buying. MRVL +5.53% same day on the same AMZN-capex read-through.

**Cross-assets.** SECTOR ETF +3.70% · SPY +0.58% · VIX 16.58 · 10Y 4.74 · WTI 84.97

**Agent read.** Low-volume recovery caps the upside at roughly the pre-earnings level (~$360-365) because the actual bear thesis — Search AI monetization opacity — is unimproved. GOOG needs its own evidence, not AMZN's. The July pattern held all month: the market pays only for currently-measurable revenue acceleration (MSFT/AMZN rewarded, GOOG/META punished); today is that same rule applied in reverse when the baseline shifted. Radar item: AI-search erosion of traditional search (Reddit v. Perplexity litigation as a marker) is the long-term structural risk, not today's driver.


---
### 2026-06-29 · +4.96% day · ▲ major
**Tags:** `index_inclusion`, `passive_flows`
**Confidence:** high

**Primary cause.** GOOG 入道指 (DJIA) 首日,替换 Verizon;单日 +168B 市值;被动 Dow ETF/Dow 衍生品 mechanical 买盘。Mag7 入 Dow 时间表:MSFT 1999,AAPL 2015,AMZN 2024-02,NVDA 2024-11,GOOG 2026-06-29 = 今天;META/TSLA 仍未入。委员会偏好转向 AI 复合体,SPCX 可能是 next。VZ -7% 同日下跌完成 swap。30d 仍 -11.5%,今日反弹 ≠ 趋势反转。

**Sources.**
- Yahoo: [Alphabet shares jump after joining Dow Jones Industrial Average](https://finance.yahoo.com/markets/stocks/articles/alphabet-shares-jump-joining-dow-174856455.html)
- Motley Fool: [Alphabet Adds $168 Billion on Dow Debut as Indexes Shake Off Volatility](https://www.fool.com/investing/2026/06/29/alphabet-adds-168-billion-on-dow-debut-as-indexes/)
- Quartz: [Google joins the Dow as index tops 52,000 for first time](https://qz.com/alphabet-dow-jones-52000-record-close-062926)

**Cross-assets.** SPY PCT +1.65% · QQQ PCT +2.49% · DJI PCT +0.59% · VZ PCT -7.00%

**Agent read.** 
 · Snapshot at `dashboard/2026-06-29.md`

---
