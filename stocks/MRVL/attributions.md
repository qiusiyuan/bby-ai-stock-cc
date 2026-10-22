# MRVL attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-22 · -9.72% day · ▼ major
**Tags:** `competitor_news`, `sector_rotation`, `guidance_cut`
**Confidence:** high

**Primary cause.** **MRVL 没有任何公司新闻，30d 口径仅 -2.61% —— 它今天是第一次被卖，这使它成为今天「新增卖压落在哪里」的最干净样本。**||具名驱动: **Lam Research 下跌 9%，点名「供应链约束」限制其指引**; AMAT -6% / ASML -4%; 当天口径 "Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7%" 与 "Optics Stocks Tumble as Tech Selloff Deepens Ahead of Earnings: Coherent -12%, Applied Optoelectronics -10%, Lumentum -9%"。**MRVL 同时吃两条: 作为 AI 定制硅/互联 (Trainium SerDes) 吃芯片供应约束，作为光互联吃光模块组的抛售。**||**今天有两个独立机制同时为负，不能混成一个:** (a) **融资故事** (META capex 下沿上调 + FCF 转负 + 四家大科技 CDS 创数月新高) 说的是「买方出不出得起钱」; (b) **Lam 的供应约束**说的是「卖方交不交得出货」。**两者对供给方的含义相反** —— 融资紧张 = 订单可能减少 (利空); 供给约束 = 产能受限、价格维持 (对有产能的人利多, 对需要扩产的人利空)。**今天市场把两件事都定价成利空，说明对设备约束的读法是「它会限制整条链的增长上限」而不是「它会支撑价格」。**||**「卖一个月里的涨幅」规律今天在 MRVL 身上以例外的形式成立。** 10/15 记录的有效规律是「跌幅与 30d 涨幅正相关」(当时 MRVL 30d +14.71% → 跌 3.45%)。今天最大的跌幅集中在 30d 已经跌最多的标的 (NOK -25.80 / SNDK -26.16 / SKHY -29.37 / DRAM -21.90 / INTC -14.37) —— **性质从 profit-taking 变成 capitulation**。MRVL (-9.72 / 30d -2.61)、AMD (-7.94 / 30d +1.04)、META (-7.91 / 30d -0.24)、SPCX (-8.94 / 30d -2.11) 是四个例外，**而四个例外全部是当天有具名新闻的标的 —— 这正好说明规律的分界: 有新闻的按新闻跌, 没新闻的按已有亏损继续跌。**||位置: vs MA50 $242.73 偏离 **-9.0%**; 距 52w 高 $329.88 为 -33.01%; 远期 PE 30.2x; 下次财报 **12/01 (40 天后)**。||**宏观共因已被排除为跌因**: 2Y -17.3bp / 10Y -18.1bp 平行下行、TLT +2.03%、债市撤回加息押注 — 折现率给了近 20bp 顺风而权益仍跌, 跌幅必须由风险溢价全额解释。**参与度限定: 全场量比中位数 0.79x, 仅 10/35 过 1.0x、2/35 过 1.5x (NOK 1.83 / GEV 1.75, 两只都有具名新闻)。方向可信, 幅度不可信。**

**Sources.**
- MT Newswires/Yahoo: Chip Stocks Fall as Supply Warning Deepens AI Selloff: Marvell and AMD Sink 8%, Intel Drops 7%
- MT Newswires/Yahoo: Lam Research Sinks 9% as Supply Constraints Cap Outlook; Applied Materials Drops 6%, ASML Holding Falls 4%
- MT Newswires/Yahoo: Optics Stocks Tumble as Tech Selloff Deepens Ahead of Earnings: Coherent Tumbles 12%, Applied Optoelectronics Drops 10%, Lumentum Falls 9%
- {"type": "computed", "title": "30d \u4ec5 -2.61% \u800c 1d -9.72% \u2014 \u56db\u4e2a\u300c\u6709\u65b0\u95fb\u624d\u8dcc\u300d\u7684\u4f8b\u5916\u4e4b\u4e00 (\u53e6\u4e09: AMD/META/SPCX)", "publisher": "workspace"}

**Cross-assets.** SPY -1.44% · VIX 19.37 · TEN YEAR 4.957 · TWO YEAR 4.65 · WTI 99.19 · DXY 101.6 · GOLD 4055.4 · BTC 81063

**Agent read.** MRVL 是今天新增卖压的最干净样本 — 30d 几乎没跌, 今天才被卖, 且驱动具名 (Lam 供应约束 + 光模块组抛售, 两条都打到它)。今天存在两个方向相反的机制 (融资紧张 vs 供给约束), 市场把两者都读成利空, 说明设备约束被理解为增长上限而非价格支撑。
 · Snapshot at `dashboard/2026-10-22.md`

---
### 2026-10-15 · -3.45% day · ▼ material
**Tags:** `sector_rotation`, `ai_demand`
**Confidence:** medium

**Primary cause.** **MRVL 今天的位置和 AMD 完全同构, 是「卖一个月里的涨幅」这条规律的第二个样本: 30d +14.71% → 今日 -3.45%, 量比 0.78x (半量)。** 无公司级催化剂, 下次财报 12/01 (47天后) 是供给方里最远的之一。||**今天 AI 融资质疑第一次拿到三个相互独立的具名来源 (10/08 时只有 Burry 的口头警告)**: (1) **Gartner 研究报告** — 预测多数 neocloud (新型 AI 云服务商) 到本十年结束前将失去独立性; 当日 IREN -5% / CoreWeave -5% / Nebius -4%。(2) **Saxo Bank (Charu Chanana)** — 明确表态「尚无充分证据显示存在系统性 AI 信用危机」, 但同时承认「融资挤压可能打到供应链」。注意这是**反驳方**的表态: 连反驳者都承认传导路径存在, 只否认它已经发生。(3) **巴克莱** — 同时下调 Dell 与 HPE 至 Hold (Dell -8% / HPE -4% / Super Micro -5%), 理由明确不是需求崩塌, 而是「供应链里一股安静的力量一直在虚增服务器营收」, 即**内存成本上涨计入 OEM 营收但不带毛利**。另有两条框架层输入: BlackRock CEO Larry Fink 称「若美国数据中心建设停摆将把经济推入衰退」(并提到国债从 2000 年 $8万亿 到今天 $40万亿); Michael Burry 称痛苦交易可以持续、Mag 7 弱势可能加深「红色十月」, 点名 2000 年科技泡沫类比。**Fink 那句话的双向性值得单记**: 表面是警告不要停, 反过来读却承认了「美国经济增长现在实质依赖 AI 资本开支」—— 这正是空头论点的前提。支持方的辩护词可以直接改写成空头论点, 说明这个结构性依赖是双方共识, 分歧只在可不可持续。||**数据中心融资成本审视的第二组证据**: Cipher Digital -9% / Applied Digital -6%, 而广义数据中心基金几乎没动 —— 分化本身指出了哪些公司最暴露于「以未来租金抵押借款」的定价方式。||**MRVL 在 AI capex 链上的具体暴露是 AWS Trainium 的 SerDes/互联**, 也就是说它的需求侧答案不在自己的财报 (12/01), 而在 **10/29 的 AMZN 财报** —— $2,200 亿 capex 的进展与 AWS 营业利润率 (~39%) 是 MRVL 收入的上游。**这是一个时序优势: MRVL 的需求侧信息会在自己交数字前 33 天免费到手。**||对照 10/14: 当日 MRVL -8.73% 是全场最大跌幅之一, 量比 1.31x。今天 -3.45% / 0.78x —— **跌幅与成交量同时减半, 说明 10/14 的集中抛售没有延续**, 今天只是板块跟跌。||价格位置: $236.81, 跌破 MA50 $240.56 (-1.6%); 距 52w 高 $329.88 -28.2%; PE 75.18x。||**宏观共因 (今天的共因只有一个, 但它的形状是反直觉的).** 九月 PPI (Producer Price Index, 生产者物价指数 — BLS 每月发布, 衡量生产者卖出价格, 通常领先 CPI 一到两个季度) 环比 **+1.3%** (8月 +0.5% / 7月 +0.2%, 2022年3月 +1.7% 以来最大单月), 同比 **+6.3%** (2022年12月 +6.4% 以来最大年度涨幅); 核心 (除食品/能源/贸易服务) 环比 +0.5% / 同比 +5.0%; 商品 +2.6% 其中**能源 +10.8% / 汽油 +20.3%**。接在 10/14 CPI 同比 3.7% (共识 3.6%) 之后, 是连续两天的下游+上游双向确认。零售销售同时跳升、失业申领保持稳健 —— 三项数据同向意味着经济不弱而价格在涨, 这是加息路径最不利的组合。||**❗但长端的反应方向和教科书相反, 本条必须作为限定随附**: 3M (^IRX) 4.088% **仅 +0.3bp**, 5Y 4.903% **-8.9bp**, 10Y 5.089% **-10.1bp**, 30Y 5.424% **-10.1bp**, TLT +1.52% (5d +2.85%)。**前端一动不动而 5年到30年平行下行 10bp —— 这个形状不可能是 Fed 政策定价 (政策定价必先动前端), 只能是对久期本身的避险需求。** 当天新闻口径直接说出了这件事 ('Tech slumps as AI financing worries grow, investors flock to bonds')。||**⭐ 方法论升级 (改写 10/05、10/07、10/08、10/14 四份报告的同一条限定)**: 那四天记录的都是「长端**不动**」—— 即对利空/利多都无响应, 属于零信息的否证, 只能说明「没有反证」。**今天长端第一次动了, 而且方向是下行**, 也就是折现率给了权益一个**顺风**, 权益却继续跌。结论因此从「无反证」升级为「有正面证据」: 折现率通道今天是负贡献 (利好), 跌幅必须由风险溢价**全额**解释。||**横截面否证「加息打击高倍数/长久期股」—— 本周第三次**: PE 从 SKHY 9.74x / DRAM 9.84x / MU 12.79x 一直到 AMD 148.2x / PLTR 172.0x / TSLA 340.0x, 跨 35 倍; 跌幅区间只有 -0.26% ~ -4.14% 且与倍数**无关** (TSLA 340x 跌 1.84% 却轻于 DRAM 9.8x 的 3.18%)。真正把跌幅排序出来的是「是否在 AI 供给/融资链上」。||**参与度限定 (与 10/14 相反)**: 38 只标的量比中位数 **0.755x**, 仅 11 只过 1.0x, 4 只过 1.5x。10/14 为中位数 1.02x / 17-of-32, 当时记为「本轮下跌序列第一个全参与度日」—— **一天后没有延续, 那是一个点不是趋势**。且今天放量的位置极度集中在韩国两条本线 (2.06x / 1.96x) + DRAM ETF (1.55x) + TSM (1.52x 财报日), 美国大型科技几乎无成交 (MSFT 0.54x / AMZN 0.54x / TSLA 0.47x / GOOG 0.39x / META 0.36x)。**这是对一个特定位置的定向抛售, 不是广泛降风险。**||**指数层面第一次方向分离**: QQQ -0.61% (跌破 MA50 $726.34) vs Dow +0.86% vs IWM +0.74%, 裂口 1.47pp。前四个下跌日 (10/07、10/08、10/13、10/14) 都是全指数同向。30d 口径 QQQ +2.26% vs IWM -6.77% 裂口从 10/14 的 12.4pp 收窄到 9.0pp, **且是用纳指跌、小盘涨的方式收窄 —— 轮动而非普跌的硬证据**。落点新闻一致: Moderna +6% (资金流入医疗) / Walmart +3% (德银上调) / Opendoor-Zillow +7% (长端回落直接利好住房)。VIX 16.88 (+0.06%) 几乎零反应, 第五次确认「不是系统性恐慌」。

**Sources.**
- Saxo Bank via Yahoo: AMD, NVDA, Other Chip Stocks Extend Rout Amid AI Debt Concerns — Saxo Says Financing Squeeze Could Hit Supply Chain
- {"type": "cross_stock", "title": "10/14 MRVL -8.73% / \u91cf\u6bd4 1.31x \u2192 10/15 -3.45% / 0.78x \u2014 \u8dcc\u5e45\u4e0e\u6210\u4ea4\u91cf\u540c\u65f6\u51cf\u534a, \u96c6\u4e2d\u629b\u552e\u672a\u5ef6\u7eed", "publisher": "workspace"}
- {"type": "cross_stock", "title": "30d +14.71% \u2192 \u4eca\u65e5 -3.45%, \u4e0e AMD (30d +20.00% \u2192 -3.92%) \u540c\u6784; AVGO (30d -7.49% \u2192 -2.06%) \u4e3a\u53cd\u5411\u5bf9\u7167", "publisher": "workspace"}

**Cross-assets.** SPY +0.09% · VIX 16.88 · TEN YEAR 5.089 · WTI 96.58 · DXY 102.101 · GOLD 4168.2 · BTC 82171

**Agent read.** 与 AMD 同构的「卖一个月涨幅」样本。相比 10/14 跌幅与量比同时减半 — 集中抛售未延续。结构上最有价值的一点: MRVL 的需求侧答案在 10/29 AMZN 财报 (Trainium 互联), 比自己的 12/01 财报早 33 天免费到手。


---
### 2026-10-14 · -8.73% day · ▼ major
**Tags:** `macro_inflation`, `sector_rotation`, `guidance_inline`, `unattributed`
**Confidence:** medium

**Primary cause.** **全书今日最大单日跌幅, 而 30d 仍 +16.61% — 跌的是涨幅不是论点。** 具体跌的是 **10/06 那天「管理层设定 FY2031 营收目标 $700-900亿、当日 +6%」所堆起来的预期**。当日报道 (Trefis「Can Marvell Stock Drop From Here?」) 的措辞正是关键: 过去十二个月 MRVL 回报 216% 远超 S&P 的约 18%, 而那个 FY2031 目标「**仍然是一个预测而不是一个结果**, 今天的买家承担 Marvell 达不到的风险」。**一个纯预测 (非结果) 支撑的涨幅, 在风险偏好收缩日里最先被收回 — 这是今天横截面的核心规律的最极端案例** (跌幅与 30d 涨幅相关: MRVL +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小)。**当日有产品级正面消息且完全未被定价: MRVL 宣布成立安全事业组并发布六通道 AI 内存产品** — 后者直接切入今天被打击的存储主题, 股价仍是全书最大跌幅。量比 1.31x 高于全场中位数 1.02x, 属真实成交。险守 MA50 $240.04 (高 2.2%), 距 thesis_break $200 缓冲 +22.6%, fwd PE 33.7x。**时序结构最不利: 下个财报 12/01, 48 天的信息真空。** 决定性旁证可提前到 10/29 AMZN 的 AWS 营业利润率 (Trainium 互联的下游), 提前 33 天。置信度 medium 的理由: 「回吐 10/06 预期」是一个结构性解释而非具名催化剂 — 今天没有任何针对 MRVL 的负面消息, 所以这是用横截面规律反推个股成因, 比具名事件弱一档。|| 宏观共因 (三个独立的因, 不可压成一个): **(1) 九月 CPI**: 同比 +3.7% (共识 3.6%)、环比 **+0.6% 为过去一年最高**。CPI = Consumer Price Index, BLS 每月发布的美国最主要通胀指标。环比年化约 7.4%, 远高于 Fed 2% 目标。timeline 在今天之前已记 Oxford Economics 的提示 — 九月调查窗口内柴油 +60 美分/加仑、汽油 +20 美分, 油价冲击会进入这份读数, 所以这个数字是可预告的。它接在 9/17 FOMC 转鹰 + 9 月纪要 (10/07 公布) 指向今年再加一次息 (市场当时只给 19%) 之上, 是纪要后第一个硬数据且站在纪要一边。**(2) ❗长端拒绝配合 — 本条必须作为限定随附**: CPI 超预期而 10Y -2.7bp / 30Y -3.8bp / TLT +0.66%。媒体口径写的是 'rate-hike jitters'、'rising bond yields', 债市当天的实际方向与之相反。所以今天的跌**不能用「当天利率上行」解释** — 实现通道是风险溢价 (VIX +10.48%) 与叙事, 不是折现率。这是本月第四次长端对本应推高它的消息不配合 (10/01 失败突破 / 10/02 非农利多无响应 / 10/08 诱因缓解不修复 / 今天 CPI 超预期不涨)。**(3) 横截面否证「加息打击高倍数股」的单一叙事**: 倍数最高的 TSLA (fwd PE 168x) 跌 2.15%, 低于倍数中等的MRVL (33.7x) -8.73%、SNOW (111x) -6.34%、GEV (37x) -6.20%。跌幅与 **30d 涨幅**的相关性明显优于与倍数的相关性(MRVL 30d +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小跌幅)。**今天卖的是一个月里的涨幅, 不是久期。** **⭐ 方法论变化 (改写前三份报告的限定)**: 10/05、10/07、10/08 三份归因都写了同一句「半量里的下跌属『没有买盘』而非『出现卖盘』, 方向可信幅度不可信」。**今天不成立**: 量比中位数 1.02x (10/08 为 0.48x / 10/07 0.79x / 10/05 0.49x), 17/32 过 1.0x (10/08 为 3/34), 放量集中在跌最多的标的 (GEV 1.65x / QQQ 1.53x / TSM 1.45x / KOID 1.39x / MRVL 1.31x / DRAM 1.30x)。**这是这轮下跌序列里第一个全参与度的下跌日 — 幅度本身开始带信息。** 反方限定仍要记: 跌最惨的 MRVL 量比只有 1.31x、MU 只有 1.04x, 「放量」是全场性的而非个别标的清仓。

**Sources.**
- 247wallst via yfinance (CPI 3.7% YoY vs 3.6% 共识; MoM +0.6% 年内最高): Trump Media and Rumble Decline 5% as September Inflation Runs Above Forecasts; Reddit Slides 2%
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- IBD via yfinance: Stock Market Today: Nasdaq Dives On Rate Hike Jitters, AI Woes; Taiwan Semi Earnings On Deck
- Yahoo Finance video (Baird 策略师 Ted Mortonson): CoreWeave, Intel, Micron, & other tech stocks are plummeting. Here's why.
- Zacks via yfinance: Why Marvell Technology (MRVL) Dipped More Than Broader Market Today
- Trefis — 12M 回报 216%; 10/06 设 FY2031 营收目标 $700-900亿当日 +6%, 「仍是预测而非结果」: Can Marvell Stock Drop From Here?
- via yfinance: Marvell Technology (MRVL) Forms Security Group And Unveils Six Channel AI Memory
- via yfinance: Astera Labs (ALAB) vs. CRDO and MRVL: Can Surging AI Demand Outpace Valuation Risks?

**Cross-assets.** SPY -1.08% · QQQ -1.97% · IWM -1.93% · DIA -0.11% · VIX 16.87 (+10.48%) · TEN YEAR 5.190% (-2.7bp) · THIRTY YEAR 5.525% (-3.8bp) · TLT +0.66% · WTI +1.16% · BRENT $106.06 (30d +12.05%) · GOLD -1.23% · SILVER -5.81% · DXY 102.530 (+0.34%) · BTC -1.81% · ETH -3.40% · BREADTH 32 只中 26 跌 / 6 涨 (含 2 只反向) · VOLUME MEDIAN 量比中位数 1.02x · 17/32 过 1.0x (10/08 为 0.48x · 3/34)

**Agent read.** MRVL 是今天「跌幅 = 回吐 30d 涨幅」规律的最干净案例, 因为它完全没有负面消息、有正面产品消息、且涨幅来源是一个可明确指认的单日事件 (10/06 的 FY2031 目标)。把它作为该规律的锚点案例保留; 若后续出现「有负面消息但 30d 涨幅低的标的跌更多」, 该规律需修正。


---
### 2026-10-08 · -5.89% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`, `partnership_news`
**Confidence:** high

**Primary cause.** 一天打掉整周: 1d -5.89% 而 5d 仅 -0.06%。**消息面当日为正面**, 两条: OCP Global Summit 2026 展示开放 AI 基础设施方案; 公司预测 AI 数据中心驱动增速加快。量比 0.68x → **「利好不涨」的第二个半量样本** (另一个是 SPCX 当日四条利好收 -3.91%)。MRVL 在 AI capex 分界线上属供给方, 且其 AWS Trainium SerDes 互联敞口使它比 AVGO 更依赖单一客户的 capex 节奏 → **10/29 AMZN 财报对 MRVL 的信息量高于对 AVGO**, 关键是 AWS 营业利润率 (当前 ~39%) 与 $2,200亿 capex 的执行节奏。距 thesis_break $200 缓冲 +34.0%。 || 宏观共因 (已按盘中时序校正, 勿用收盘涨跌读因果): **触发是地缘** — 美国据报考虑扩大对伊朗打击, 叠加一艘油轮遇袭。当日标题: 'Oil surges, stocks sink as US reportedly eyes new Iran strikes' / 'U.S. Stocks Slip, Oil Rises on Fresh Tanker Attack' / 'Dow Tumbles, Oil Surges, and Yields Rise to New 24-Year Highs as Trump Considers Ramping Up Iran Attacks' / 'Nasdaq Slumps On War Worries'。盘中路径: WTI 开 89.86 → 冲 **93.08** → 收 90.97; 10Y 盘前 **5.331** → 收 5.239; 30Y 开 5.695 (24 年高位区) → 收 5.615; QQQ 开 754.29 → 高 756.93 → 收 **745.35** (贴当日低 744.39)。**关键: 两个诱因 (油/长端) 当天都缓解了, 权益却收在当日低点附近 —— 纯 beta 事件应在诱因缓解时修复, 今天没有。** 只看收盘 (10Y -2.5bp / 30Y -4.4bp / TLT +0.77%) 会误读成「利率转松而久期资产崩盘」; 利率今天是上午推手、下午缓解项, 不是反常项。对照 10/01 (长端失败突破日 SKHY +5.08% / GEV +3.89% / MU +3.03% 全线反打): 同样的利率先冲后落路径, 那天权益修复了, 今天没有。**差异在「不修复」, 不在利率方向。** **第二段 (不修复) 的 AI 侧候选解释**: Broadcom 为 OpenAI 芯片安排 >$500亿 融资 (Apollo/Blackstone 参与), SPCX $400亿, Oracle 同期发债, 三家抢同一批买家; 媒体口径从 'war worries' 转为 'growing AI caution'; Michael Burry 称市场处于 'denial'。**但有一条有力反证, 不应略过: 同日 Anthropic 宣布计划在云与算力上支出 $5,180亿 — 量级极大的 AI capex 利多, 整组没涨。** → 可读成「信用担忧压过需求利多」, 也可读成「市场今天对任何 AI 消息都不反应」(情绪/风险偏好)。**诚实结论: 地缘是因, AI 谨慎是让它不修复的那一层, 但今天的数据不足以把信用与纯 beta+情绪分开。判别点在 10/15 TSM 指引与 10/28 capex 指引。** 跌幅分布事实 (排他性因果不成立): 开支方 GOOG -0.43%/AMZN -0.78%/META -0.87%/MSFT -0.95% vs 供给方 NVDA -2.30%/TSM -3.24%/AVGO -3.35%/INTC -5.53%/MRVL -5.89%, 两簇不重叠 — 但战争风险日里单纯 beta 差异足以产生同样分裂。**量能限定 (双向适用)**: 全书 34 只量比中位数仅 0.48x, 仅 3 只过 1.0x → 半量里的 5% 级下跌, 属「没有买盘」而非「出现卖盘」, 方向可信幅度不可信。**同日两个反向硬数据**: Samsung 发创纪录营收/利润初步业绩、TSMC 九月营收超目标 — 供应链两个独立层级同日确认需求, 价格全部反向 → 需求侧无恙。

**Sources.**
- via yfinance MRVL news: Marvell to Showcase Open AI Infrastructure Solutions at OCP Global Summit 2026
- via yfinance MRVL news: Marvell Technology Forecasts Accelerating Growth From AI Data Centers
- via yfinance AVGO news: SpaceX, Broadcom and Oracle All Want Billions in AI Chip Debt at the Same Time
- via yfinance AVGO news: MARKETS LIVE: US stocks slip on bond and AI debt fears

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-09-29 · +4.10% day · ▲ material
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** MRVL +4.10% 至 $262.24，无任何公司级催化剂。板块级 relief rally：SOXX +2% vs QQQ +0.29%，买盘集中在芯片而非大盘科技。反弹幅度按前一日跌幅排序（Arm 前日 -9% → 今日 +5%；MRVL 前日 -3.3% → 今日 +4.1%），不按基本面或主题相关性排序。5d 净额 -0.05%，两天互相抹平；成交量仅均量 45%，无放量。

**Sources.**
- : [Arm Jumps 5% as Chip Selloff Unwinds; Marvell Climbs 4%, Qualcomm Inches Higher](https://247wallst.com/investing/2026/09/29/arm-jumps-5-as-chip-selloff-unwinds-marvell-climbs-4-qualcomm-inches-higher/)
- : [Lumentum Climbs 7% as Optics Selloff Reverses a Day After Citi's $11B Switching Call; Coherent and Corning Rise 5%](https://247wallst.com/investing/2026/09/29/lumentum-climbs-7-as-optics-selloff-reverses-a-day-after-citis-11b-switching-call-coherent-and-corning-rise-5/)
- : [Intel Drops 4% on Oil-Driven Rate Fears, NVIDIA Rises 3% on Record $150B Buyback](https://247wallst.com/investing/2026/09/28/intel-drops-4-on-oil-driven-rate-fears-nvidia-rises-3-on-record-150b-buyback-taiwan-semiconductor-slips/)

**Cross-assets.** SPY CHANGE -0.38% · QQQ CHANGE -0.03% · VIX 16.28 · TEN YEAR 5.281 · WTI 90.33 · DXY 101.582

**Agent read.** 必须排除的误读：Citi 周一发布的『光电路交换 2030 年 $110 亿市场』研报不是原因——(1) 研报未点名 MRVL/AVGO/NVDA；(2) 发布当天(09-28)光通信股反而全线下跌；(3) 涨幅排序与主题相关性不匹配（Arm 与光交换无关却涨幅居前）。历史模式：本条是 2026-09-23 的精确镜像（当日 -1.81%，同样 macro_rates+sector_rotation / medium / 无公司级新闻）。更重要的是与 2026-08-18 构成可重复模式——当 10Y 位于 52 周高位时，看多 AI 的卖方研报在发布当日无效（08-18 UBS 看多 AI 研报被利率盖过；09-28 Citi 研报当天光通信股下跌）。机制：提高远期 TAM 的研报增加的是分子的远期部分，而这正是折现率打击的部分。forward PE 38.1x(09-23)→38.7x(今日)。距 thesis-break $200 缓冲 +31.1%。证伪条件：若未来 3 个交易日 MRVL 跑赢 SOXX 超 3pp，说明存在未识别的公司级驱动。下一裁决点是 10-28/10-29 hyperscaler capex 指引（AWS 是其 Trainium SerDes 的需求端），比 12-01 自家财报早两个月；注意 08-28 先例——beat+raise 当天仍 -10.32%，好数字不足以驱动股价。
 · Snapshot at `dashboard/2026-09-29.md`

---
### 2026-09-23 · -1.81% day · ▼ minor
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** MRVL -1.81%（1w +12.14%，触发 5d≥10% 门槛），无公司级新闻。折现率冲击传导；forward PE 38.1x 属偏高一档。

**Sources.**
- : [10-year Treasury yield hits highest level since 2007 as market prices in another Fed rate hike](https://finance.yahoo.com/quote/%5ETNX/)

**Cross-assets.** SPY CHANGE -0.74% · VIX 15.34 · TEN YEAR 5.12 · WTI 91.41 · DXY 101.19 · QQQ CHANGE -1.01%

**Agent read.** 3mo -7.7%——1w 强势未累积为季度收益，说明 Trainium 互联叙事尚未兑现为持续定价。距 thesis-break $200 缓冲 +28.8%。12-01 财报为下一裁决点，但更早的读数来自 10-28 hyperscaler capex 指引（AWS 是其 Trainium SerDes 的需求端）。
 · Snapshot at `dashboard/2026-09-23.md`

---
### 2026-09-21 · +5.38% day · ▲ material
**Tags:** `tech_breakthrough`, `ai_demand`, `sector_rotation`, `macro_rates`
**Confidence:** high

**Primary cause.** MRVL +5.38% 到 $257.38, 5d +17.62%, 30d +17.68%。公司级催化剂明确: 发布 1.6T 光互联 / 2nm 光学技术, 针对 AI 互联的「铜墙」(copper wall) 瓶颈 — 头条「Marvell Rises Over 3.3% as 2-Nanometer Optics Target AI Copper Wall」、「Marvell just made a move that changes the AI networking story」。这是**产品驱动而非叙事驱动**, 可持续性优于今天 INTC/AMD 的 agentic CPU 叙事。注意量比仅 0.94x (未放量) — 涨幅由信息质量而非资金规模推动。**本 cluster 最被忽视的事实: AVGO 与 MRVL 30 天分化 33 个百分点 (-15.22% vs +17.68%)**, 两家都做定制 AI 芯片和互联, 走向完全相反。MRVL 的路径是产品发布驱动 (今天 1.6T, 9/17 记录过一次 partnership_news), AVGO 的路径是估值消化 (即使有「Anthropic 可能成为最大定制芯片客户」这类利好头条仍 30d -15.22%)。今天板块 beta 是 SMH +4.02%, MRVL 超出约 1.4pp — 超出部分归于自身产品发布。

**Sources.**
- (none)

**Cross-assets.** SPY +1.55% · QQQ +2.77% · SMH +4.02% · VIX 14.87 · TEN YEAR 4.963 · WTI -8.31% · INTC +12.14% · AMD +9.95% · META +11.34% · NVDA +2.30%

**Agent read.** 距 thesis-break $200 缓冲仅 +28.7%, 是全持仓最紧的一个 — 尽管今天涨 5.38%, 这个标的的下行容错空间最小, 值得比其他持仓更密切跟踪。fwd PE 38.06 偏高。今天的产品发布要在 12/01 Q3 财报里给订单 — 那是 71 天后, 是全持仓里「催化剂到验证」间隔最长的之一。中间没有其他公司级检查点, 意味着这 71 天里价格完全由板块 beta 和叙事决定。
 · Snapshot at `dashboard/2026-09-21.md`

---
### 2026-09-17 · +5.37% day · ▲ material
**Tags:** `partnership_news`, `ai_demand`, `sector_rotation`, `macro_rates`
**Confidence:** high

**Primary cause.** **三条独立的公司级催化，全部指向互连层** — MRVL 是今天 AI capex cluster 里催化最密的名字。(1) **AI 光互连拿下更多美国产能**（'Marvell Jumps 5.2% as AI Optics Win More U.S. Capacity'）；(2) **GlobalFoundries SiGe 合作扩大**，用于下一代 AI 数据中心光互连（'GlobalFoundries and Marvell expand SiGe deal for AI data centers'）；(3) **Microsoft 安全平台合作**（'MRVL Stock Climbs After AI Optical Capacity Deal, New Microsoft Security Platform Launch'）。**三条催化的共同方向是最重要的信息**：MRVL 在 AI 数据中心的**互连层**位置在加固，而不只是搭 AWS Trainium 的车（Trainium SerDes 是既有 thesis）。叠加板块 beta：半导体反弹第三个交易日，加息后 10Y 5.00%→4.951%、VIX -12.03% 到 15.58，AMD +6.13% / INTC +9.34% 同日。**跨标的确认**：NOK 今天 +3.65%（量比 1.34x，全 watchlist 第二高量比）也是因为 Microsoft 光网络合作（'From Flip Phones to AI, Nokia's Microsoft Deal Boosts Its Optical Networking Prowess'）— **同一主题的两个独立标的表达，这种跨标的确认比单一新闻可靠得多**。

**Sources.**
- Yahoo: [Marvell Jumps 5.2% as AI Optics Win More U.S. Capacity](https://finance.yahoo.com/)
- Yahoo: [GlobalFoundries and Marvell expand SiGe deal for AI data centers](https://finance.yahoo.com/)
- Yahoo: [MRVL Stock Climbs After AI Optical Capacity Deal, New Microsoft Security Platform Launch](https://finance.yahoo.com/)
- Yahoo: [GlobalFoundries and Marvell expand collaboration for next-generation optical connectivity](https://finance.yahoo.com/)
- _Corroboration:_ **互连主题的跨标的确认**：NOK +3.65%（量比 1.34x）因 Microsoft 光网络合作。两个不同公司、同一天、同一主题（AI 数据中心互连）— 主题确认强于单一新闻
- _Corroboration:_ 板块 beta 成分：AMD +6.13% (1.09x) / INTC +9.34% (1.12x) / NVDA +2.55% (0.50x) / AVGO +2.51% / TSM +2.90%。MRVL 5d +6.32% 是六名异动里最强，说明已有独立动能
- _Data:_ 量比 0.66x。距 thesis-break $200 缓冲 **+21.0% — 今日异动六名里最窄**。下一个硬催化 12/01 Q3 财报，三个月后 ()

**Cross-assets.** SPY +1.11% · QQQ +1.63% · VIX 15.58 · TEN YEAR 4.951 · DXY 100.24 · WTI 101.85

**Agent read.** **MRVL 是今天涨幅里质量最高的一个** — 六个 ≥5% 的名字里，只有它和 INTC 有真实的公司级催化，而 MRVL 的三条催化方向一致（互连层），INTC 的两条是未确认传闻。5d +6.32% 也是六名最强，说明动能不是今天才有。**一个方向性判断值得记下来：AI 数据中心的瓶颈正在从「有多少算力」转向「算力之间怎么连」。** 证据有三层：(a) MRVL 今天三条催化全在光互连/SerDes；(b) NOK 同日因 Microsoft 光网络合作 +3.65%（1.34x 量比）；(c) 对照组是龙头的迟钝 — **NVDA 30d 仅 +0.26%、量比 0.50x（cluster 最低），AVGO 30d -16.69%**。**卖算力的在停滞，卖互连的在加速，卖代工的在修复（TSM/INTC）。这个排序如果持续，意味着 AI 基础设施的投资重心在向互连和产能迁移 — 而这正是产业成熟的典型路径（早期抢算力，中期抢互连和产能）。** 历史对照：8/19 Google 引入 Marvell 作定制 AI 芯片第二供应商时，AVGO -4.61% (vol 1.78x) 而 **MRVL 镜像 +9.85%** — MRVL 的上行多次以 AVGO 的下行为对价。今天 AVGO 也涨了 +2.51%，两者同涨说明这次是板块 beta 而非份额转移，但 30d 口径（MRVL +14.35% vs AVGO -16.69%）显示份额叙事的方向未变。**风险提示：距 thesis-break $200 只有 +21.0% 缓冲，是今日六个异动名字里最窄的，而下一个硬催化远在 12/01（三个月后）。** 中间无法验证，靠叙事支撑。
 · Snapshot at `dashboard/2026-09-17.md`

---
### 2026-09-10 · -3.43% day · ▼ material
**Tags:** `macro_inflation`, `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** 无个股催化剂, 纯板块 beta。八月 PPI +5.4% 与 WTI +8.16% 推高 2Y 13.3bp / 10Y 11.7bp, SOXX -3%; MRVL 作为 fwd PE 33.8 的二线 AI 供应端在『卖铲子』一侧被杀。当日『买铲子 ↔ 卖铲子』轮动第四次干净出现: 买铲子 GOOG +0.61 / MSFT +0.16 / AMZN -0.20 / META -1.42 加权几乎持平, 卖铲子 INTC -5.57 / MRVL -3.43 / AMD -3.36 / NVDA -2.37 / TSM -1.68 / AVGO -0.97, 两侧平均差约 3 个百分点。机制: 买铲子的现金流已在损益表里 (fwd PE 19-24, 有当期盈利地板), 卖铲子的估值溢价压在『AI capex 持续多年』的远端假设上, 折现率上升时前者掉基点、后者掉倍数。

**Sources.**
- Yahoo/MT Newswires: [Update: US Equity Indexes Fall as Hot Producer Prices, Soaring Crude Oil Boost Treasury Yields](https://finance.yahoo.com/economy/articles/us-equity-indexes-fall-hot-195114785.html)
- _Corroboration:_ 轮动确认: 买铲子四家平均约 -0.2%, 卖铲子六家平均约 -2.9%。同日需求侧零负面信号 (TSMC 八月营收 +53% 创纪录、OpenAI 首颗定制 AI 芯片选 AVGO、黄仁勋把网络安全点为 AI 下一条增长线、澳洲计划 AI 算力 +125%)。
- _Corroboration:_ 对照 2026-08-28: Warsh 鹰派推高 10Y 时 MRVL -10.32% (beat+raise 仍暴跌) / NVDA -3.31% 而 AMZN +3.33% — 同一轮动机制的更极端版本。

**Cross-assets.** SPY -0.58% · VIX 17.84 · TEN YEAR 4.944 · WTI 103.83

**Agent read.** ⚠️ 全部持仓里 thesis-break 缓冲最薄: $226.96 距 $200 仅 +13.5%, 是唯一进入 15% 观察带的持仓, 且它同时是本 cluster 波动最大的名字 (8/28 -10.32%, 8/18 -8.24%, 8/4 +13.8%)。若跌破 $210 进入 5% 预警带, 应按 triggers.yaml 重读而非凭感觉持有。今日 5d 仍 +9.92%, 30d +38.9%, 尚无破位迹象。
 · [Snapshot](snapshots/2026-09-10.md)

---
### 2026-09-08 · +2.35% day · ▲ minor
**Tags:** `partnership_news`, `competitor_news`, `sector_rotation`
**Confidence:** medium

**Primary cause.** 记录理由是**具名催化剂**而非幅度 (1d +2.35% / 5d +8.1% 均未过标准阈值)。催化剂: **Google 与 Marvell 达成 custom ASIC 安排**, 从 AVGO 手里分走 TPU 相关的独占叙事。Barron's 在解释 AVGO 9/2 财报后下跌时明确把『Google 与 Marvell 的安排盖过了 Broadcom 稳健的业绩』列为跌因之一。这解释了本周 MRVL +8.1% 与 AVGO -0.4% 的分化 — 两者从『同涨同跌的 custom ASIC 双雄』开始分道。同期 Morgan Stanley 维持 Overweight 并在 AVGO/MRVL 之间偏好 Broadcom。

**Sources.**
- Yahoo Finance: Broadcom vs. Marvell: Which Custom AI Chip Stock Is the Better Buy?
- Barron's: Why Broadcom Stock Couldn't Match Up to Nvidia (cites Google's arrangement with Marvell overshadowing Broadcom's results)
- 24/7 Wall St via Yahoo: Qualcomm Rises 5% on Multi-Generation Amazon AI Silicon Deal
- _Corroboration:_ hyperscaler 去单一化的横向格局: Google → 引入 MRVL (原 AVGO 独家叙事); Amazon → 引入 QCOM (原 MRVL SerDes/互联 + AVGO); Meta MTIA → 仍 AVGO。方向单一, 且经济上必然 — 自研芯片的目的就是摆脱供应商定价权, 因此在合作设计端保留单一供应商是自相矛盾的。

**Cross-assets.** SPY -0.48% · VIX 15.3 · TEN YEAR 4.8 · AVGO +3.04% · GOOG -0.15% · SOXX +2.00%

**Agent read.** **这是本周最需要打问号的一格。** 三条理由。(1) **消息驱动的涨幅回吐速度快于基本面驱动。** 本周 +8.1% 完全建立在『拿到 Google』这一条消息上, 而消息不改变当期财务 (12/1 才是下一份财报)。(2) **MRVL 距 thesis-break $200 缓冲仅 +14.4%, 是全部持仓中最薄的一个。** 如果 9/11 CPI / 9/17 FOMC 走鹰派并引发一次 8-10% 的普跌, MRVL 是最先接近 thesis-break 线的标的; 而它 fwd PE 34.0x 也不提供估值缓冲。(3) **中期同构风险: 今天它在 Google 侧受益, 但在 Amazon 侧同样被 QCOM 稀释。** 去单一化是结构性趋势而非一次性事件, 今天的受益者是明天的被去化者 — AVGO 只是因为份额最高而先被打。历史对照: MRVL 8/28 财报 beat+raise 却跌 -10%, 一周后已收复并 +8.1% (印证『beat 先出清拥挤仓位再涨』的反应函数), 但这也说明它的仓位在 8 月底是拥挤的, 现在又涨回去了。观察点: 12/1 财报里 Google 安排的财务体现, 以及 Trainium 份额被 QCOM 稀释的量化影响。


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
