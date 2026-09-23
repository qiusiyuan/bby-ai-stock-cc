# AMD attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-09-23 · -1.68% day · ▼ minor
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** AMD -1.68%（1w +19.67%，watchlist 最大周涨幅，触发 5d≥10% 门槛）。今日跌幅温和，是三个前期涨幅最大名字里最抗跌的一个（对照 SNDK -3.62%、INTC -2.86%）。无公司级新闻；驱动为 10Y 破 5.12% 的折现率冲击。

**Sources.**
- : [10-year Treasury yield hits highest level since 2007 as market prices in another Fed rate hike](https://finance.yahoo.com/quote/%5ETNX/)

**Cross-assets.** SPY CHANGE -0.74% · VIX 15.34 · TEN YEAR 5.12 · WTI 91.41 · DXY 101.19 · QQQ CHANGE -1.01%

**Agent read.** 3mo +18.0%，距 thesis-break $380 缓冲 +61.4%。带 1w +19.67% 的涨幅进入 11-03 财报，同 SNDK 的『涨幅透支』判据适用——好数字可能被打折。相对强势值得记录：同一回吐日里跌幅最小，说明其涨幅的买盘质量高于 SNDK/INTC。
 · Snapshot at `dashboard/2026-09-23.md`

---
### 2026-09-21 · +9.95% day · ▲ extreme
**Tags:** `sector_rotation`, `ai_demand`, `macro_rates`, `macro_oil`, `index_inclusion`
**Confidence:** medium

**Primary cause.** AMD +9.95% 到 $615.52, 2.19x 量, **首破 $1 万亿市值 + 历史新高** — 是三大 mover 里唯一站在 52 周高点之上的 (INTC 和 META 都还在高点之下)。30d +27.34% 是三者最强。四条链: (1) agentic 推理 = CPU 需求 (与 INTC 共享, Meta Muse read-through)。**AMD 在这条链上站位优于 INTC** — 同时是 EPYC (agent 编排负载直接受益) 和 MI 系列 (加速器) 供应商, 若 agentic 是增量而非替代则两头受益。(2) $1T 门槛的自我强化: 触发「只投 $1T+」机构筛选器 + 媒体覆盖跳升 + 指数/ETF 权重重算, 头条把突破与 SOX 指数四只新成分事件绑在一起说 (「AMD Breaks Out」) — 典型动量买盘自我强化结构, 约 2pp 纯心理/机械无基本面。(3) 芯片涨价 10% 报道 (与 INTC 的 10/05 DigiTimes 传闻同一条产业线索, 整个 x86 阵营涨价; 对 AMD 比 INTC 更正面因无亏损 foundry 拖累, 但同样未被公司确认)。(4) 宏观 beta ~4pp (WTI -8.31% → 10Y 4.963% → SMH +4.02%)。**最重要的逆向信号: TSM 仅 +2.41%。** AMD 的 MI 系列全部由 TSMC 代工; 若市场真信 AMD 加速器份额要跳到 bull case 所需的 20%+ hyperscaler GPU 支出, TSM 必须供出这些晶圆和 CoWoS 封装。TSM 只给 beta 级反应 = **产能端对 AMD 的份额假设投了弃权票**。NVDA 仅 +2.30% 且有头条专写「3 Reasons Nvidia Sat Out the AI Rally」= 市场在定价零和抢份额而非市场整体扩大。

**Sources.**
- Yahoo: [AMD Joins the $1 Trillion Market Cap Club](https://finance.yahoo.com/quote/AMD/news/)
- Yahoo: [AMD Storms Into $1 Trillion Club as Chip Stocks Charge Higher](https://finance.yahoo.com/quote/AMD/news/)
- Yahoo: [AMD Hits $1 Trillion Market Cap: 3 Reasons Nvidia Sat Out the AI Rally](https://finance.yahoo.com/quote/AMD/news/)
- IBD: [Chip Stocks Rise As Four New Names Join SOX Index. AMD Breaks Out.](https://finance.yahoo.com/quote/AMD/news/)
- Yahoo: [AMD Rises 5% as Report Flags 10% Chip Price Increase](https://finance.yahoo.com/quote/AMD/news/)
- Barron's (via Yahoo): [Intel, AMD, and Arm Stock Are Jumping. Thank Meta's Muse AI Agent.](https://finance.yahoo.com/quote/AMD/news/)
- _Corroboration:_ 关键逆向: TSM +2.41% — MI 系列的唯一代工方对份额假设弃权投票。10/15 TSM 财报比 AMD 自己 11/03 早 19 天, AMD 的产能上限答案会由 TSM 先给出

**Cross-assets.** SPY +1.55% · QQQ +2.77% · SMH +4.02% · INTC +12.14% · NVDA +2.30% · TSM +2.41% · AVGO +1.41% · MRVL +5.38% · META +11.34% · VIX 14.87 · TEN YEAR 4.963 · WTI -8.31% · FWD PE 39.53

**Agent read.** **8/4 的记录几乎逐条适用, 但有三个差别。** 8/4 AMD +9.3% (与今天 +9.95% 几乎同幅), 当时归因写: 「AMD 在别人的财报上涨了 9.3%, 在自己财报前几小时。这把门槛抬高了 — 一份仅仅符合预期的财报很可能把这个 move 还回去。」今天同构: 又一次在别人的产品新闻 (Meta Muse) 上涨 ~10%, 走向 11/03 财报。差别: (1) **量比 2.19x vs 8/4 的 0.92x — 买盘真实度高 2.4 倍**, 这是今天优于 8/4 的地方; (2) 位置 $1T + 历史新高 vs 当时刚回到 50 日均线、30d -4.0% — 起点高得多, 容错小得多; (3) 财报还有 43 天 vs 当晚 — 预期有更长时间膨胀或消退。校准: 7/31 时 AMD 还是「唯一没吃到 AMZN 利好的大型 AI 芯片股 (5d -6.09%)」, 52 天后成了 $1T 市值 + 30d +27.34% 的全场焦点 — 这个速度本身值得警惕。thesis 框架 Bull 30%($700+)/Base 45%($550-600)/Bear 25%($300-): **当前 $615.52 已越过 base 上限 2.6%**, 市场为 base 付完钱正在为 bull 付定金。bull 四条件里最难的是「ROCm 缩小 CUDA 差距」— 纯软件生态问题, 历史上从未被任何 NVIDIA 挑战者解决。reverse-DCF 在 $537 时称「不像 NVDA 峰值那样定价完全 bull 情景, 通过前瞻倍数还有安全边际」; $615.52 已涨 14.6%, 那个边际被消耗大部分。thesis 原文还写着「最近 280% YTD 涨幅和一位分析师'涨太远太快'的警告意味着下次财报若失望会有回调风险」。**裁决顺序很重要: 10/15 TSM (产能上限, 早 19 天) → 11/03 AMD 自己 → 11/17 NVDA (零和读法裁决)。**
 · Snapshot at `dashboard/2026-09-21.md`

---
### 2026-09-17 · +6.19% day · ▲ material
**Tags:** `sector_rotation`, `macro_rates`, `ai_demand`
**Confidence:** medium

**Primary cause.** **无单一公司级催化 — 这是板块 beta 领涨。** 半导体反弹进入第三个交易日（'AMD Jumps 7% as Semiconductor Rebound Reaches a Third Session; Broadcom Rises 3%, NVIDIA Edges Higher'、'AMD Leads Chip Stocks Higher Amid Sector Rebound'）。AMD 是大市值半导体里 beta 最高的名字之一，在 VIX 单日崩 12.03% 到 15.58、10Y 从 5.00% 回落到 4.951% 的日子天然领涨。**唯一的公司消息是生态层面而非营收层面**：ROCm 支持扩展到 RISC-V 数据中心服务器（'Advanced Micro Devices (AMD) Expands ROCm Support To RISC V Datacenter Servers'）— 软件生态扩张，不影响近期营收。另有 Nebius 宣布上调 NVDA GPU 和 AMD CPU 的租用价格（'Nebius announces higher rates for Nvidia GPUs and AMD CPUs'）— 这是需求侧的间接正面信号（租金上涨 = 供不应求）。Cramer 当日喊 'Buy It'（情绪，非基本面）。

**Sources.**
- Yahoo: [AMD Jumps 7% as Semiconductor Rebound Reaches a Third Session; Broadcom Rises 3%, NVIDIA Edges Higher](https://finance.yahoo.com/)
- Yahoo: [AMD Leads Chip Stocks Higher Amid Sector Rebound](https://finance.yahoo.com/)
- Yahoo: [Nebius announces higher rates for Nvidia GPUs and AMD CPUs](https://finance.yahoo.com/)
- Yahoo: [Advanced Micro Devices (AMD) Expands ROCm Support To RISC V Datacenter Servers](https://finance.yahoo.com/)
- _Corroboration:_ 板块同涨：INTC +9.34% (1.12x) / MRVL +5.37% / TSM +2.90% / NVDA +2.55% / AVGO +2.51%。**AMD 和 INTC 是今天唯二量比 >1.0x 的半导体名字（1.09x / 1.12x）— 只有这两个有真实资金**
- _Data:_ 量比 1.09x。距 thesis-break $380 缓冲 +43.1%。下一催化 11/03 Q3 财报 ()

**Cross-assets.** SPY +1.11% · QQQ +1.63% · VIX 15.58 · TEN YEAR 4.951 · DXY 100.24 · WTI 101.85

**Agent read.** **confidence 定 medium 是因为归因诚实：这次涨幅无法归因到 AMD 自身的任何新信息。** 1.09x 量比 + 无公司级新闻 = **仓位调整，不是叙事变化**。这不是负面判断，只是要求不要把它读成基本面改善。**一个值得注意的对照**：今天全部半导体名字里只有 AMD (1.09x) 和 INTC (1.12x) 的量比超过 1.0x，其余（NVDA 0.50x / AVGO 0.53x / MRVL 0.66x / TSM 0.65x）全部缩量。**AMD 有真实资金但无叙事，INTC 有叙事（传闻）也有资金** — 两者是不同性质的买盘。**Cramer 当日的两条评论构成一个有意思的组合**：一边说 AMD 'Buy It'，一边写 'Jim Cramer Turns on the Two Kings of AI: If You Want to Destroy Trust, You Couldn't Find a Better Way' — 名嘴同日既唱多具体标的又质疑 AI 双龙头，这是情绪面混乱的表征，不构成信息。**关键跟踪项是 11/03 Q3 财报** — 今天的 +6.19% 是 beta，财报是唯一能把 beta 变成 alpha 的地方。**INTC 与 AMD 的份额之争是本次两者同涨背后被掩盖的矛盾**：INTC thesis 的 disconfirming event 里明确写着「AMD 继续拿 Xeon 服务器 CPU 份额」，两家同日大涨说明市场在交易共同的板块因子，还没交易份额归属 — 这会在 10/22 (INTC) 和 11/03 (AMD) 两份财报之间被拉开。距 thesis-break $380 缓冲 +43.1%，无风险。
 · Snapshot at `dashboard/2026-09-17.md`

---
### 2026-09-10 · -3.36% day · ▼ material
**Tags:** `macro_inflation`, `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** 无个股催化剂, 纯板块 beta。八月 PPI +5.4% 超预期 + WTI +8.16% 破 $103 推高收益率 (2Y +13.3bp / 10Y +11.7bp 至 4.96%), SOXX -3%, 半导体跌幅约为大盘科技 (QQQ -1.06%) 的 3 倍。AMD 位于『卖铲子』一侧, fwd PE 32.2, 缩量下跌 (0.73x)。5d 仍 +10.18% — 今天是回吐而非破坏。

**Sources.**
- 247wallst: [Intel Sinks 6% as Profit Taking Hits a Parabolic Run; NVIDIA and AMD Retreat 3%](https://247wallst.com/investing/2026/09/10/intel-sinks-6-as-profit-taking-hits-a-parabolic-run-nvidia-and-amd-retreat-3/)
- _Corroboration:_ 同日 AMD Q2 基本面参照 (来自同一篇): 营收 $11.54B, 数据中心 +107% YoY — 需求侧无恶化。跌幅来自折现率而非需求。

**Cross-assets.** SPY -0.58% · VIX 17.84 · TEN YEAR 4.944 · WTI 103.83

**Agent read.** 距 thesis-break $380 缓冲 +32.5%。AMD 与 NVDA 今日无任何个股新闻, 是判断『今天是板块级折现率事件』的干净对照组 —— 它们的跌幅 (-3.36% / -2.37%) 定义了纯 beta 的基线, INTC 超出这个基线的 2.6 个百分点才是个股 alpha。
 · [Snapshot](snapshots/2026-09-10.md)

---
### 2026-09-08 · +6.25% day · ▲ material
**Tags:** `sector_rotation`, `executive_comment`, `competitor_news`
**Confidence:** medium

**Primary cause.** 与 INTC (+9.67%) 同日大涨, 但故事不同。AMD 侧的可见驱动是『AI 繁荣推动 MI450 / Helios / 服务器 CPU 增长』这条三线增长叙事 (Yahoo: Advanced Micro Devices Sees AI Boom Fueling MI450, Helios and Server CPU Growth), 属于叙事而非新公告。板块层面 SOXX +2.0%; 但 AMD 涨幅是 SOXX 的 3.1 倍, 因此大部分是个股/主题 alpha。**最重要的结构性观察不在 AMD 自身, 而在它与 INTC 同日大涨这个事实。**

**Sources.**
- Yahoo Finance: Advanced Micro Devices Sees AI Boom Fueling MI450, Helios and Server CPU Growth
- IBD: TSMC, IBD Stock Of The Day, Rises Above Early Buy Point As Chip Stocks Rally
- _Corroboration:_ AMD 与 INTC 是 x86 市场的直接竞争对手, 同日分别 +6.25% / +9.67%。若市场在做『Intel 涨价 = 抢回份额』这笔交易, AMD 应该下跌。两者同涨说明资金买的是『x86 + 加速器阵营整体』而不是在两家之间选边 — 即市场在给 x86 平台的整体定价权改善定价, 而不是给份额转移定价。
- _Corroboration:_ 逆向检验: NVDA 同日 -2.06%, 是唯一下跌的芯片股。AMD 是 NVDA 在加速器上的直接对手, 因此 AMD +6.25% / NVDA -2.06% 这一对可能包含份额叙事; 但 INTC/TSM 同涨说明主导因素是『非 NVDA 的 AI 芯片』这个更广的轮动而非 AMD 特有的份额故事。

**Cross-assets.** SPY -0.48% · VIX 15.3 · TEN YEAR 4.8 · SOXX +2.00% · INTC +9.67% · NVDA -2.06% · TSM +2.69%

**Agent read.** 置信度 medium 因为驱动是叙事文章而非新公告 — MI450/Helios 的指引不是今天新出的信息。真正有价值的一条是**同涨的含义**: INTC 宣布涨价而 AMD 同日大涨, 排除了『Intel 涨价 = 从 AMD 手里抢份额』这个读法。更一致的解释是本报告『本周回顾』tab 建立的定价权框架 — 整个 x86 平台的成本 (内存等) 在上升, 两家都能转嫁, 因此都受益。这也意味着如果 10/22 INTC 财报显示涨价没转化为毛利率扩张, 对 AMD 的读法也应该同步下调。估值对照: AMD fwd PE 32.7x vs INTC 51.4x vs NVDA 14.5x — AMD 在中间, 30 日仅 +2.52% (三者最弱), 说明今天的涨幅更像是补涨而非趋势延续。AMD 不在 focus 名单但本周 +7.8% 且是 AI capex cluster 里唯一非 focus 的大权重标的, 已建议加入 focus。11/3 财报是下一个硬信息点。


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
