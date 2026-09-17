# INTC attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-09-17 · +9.34% day · ▲ major
**Tags:** `executive_comment`, `partnership_news`, `sector_rotation`, `macro_rates`
**Confidence:** high

**Primary cause.** 两条来自 Intel 自身的消息叠加风险偏好修复。(1) **SK Hynix 与 Intel 就俄亥俄园区代工存储芯片重启谈判** — 这是 Intel Foundry 第一个 Apple 之外的具名重量级潜在客户，thesis 里明确写着「18A 客户资格认证进展（gating factor）；任何 Apple 之外的具名客户胜利都验证 thesis」。历史重量在于角色反转：Intel 2021 年把 NAND 业务卖给 SK Hynix，现在 SK Hynix 可能反过来用 Intel 的美国晶圆厂。对 SK Hynix 的真实价值不是产能增量而是**在美国关税/出口管制墙内获得 HBM 产能**（这也解释了 SKHY ADS +5.24% vs 韩本 +3.25% 的 1.6 倍差）。(2) **CEO 称存储价格已上涨超过 500%** — 对 INTC 自身是成本利空（Intel 采购存储做服务器/PC 平台，而毛利率从 40% 恢复到 50%+ 是 thesis 关键指标），但市场只交易了「所以代工存储的经济性成立」，完全忽略了采购成本这一面。(3) 宏观公因子：加息后 10Y 从 5.00% 回落到 4.951%，VIX -12.03% 到 15.58，高 beta 半导体第三个交易日反弹（AMD +6.13%、MRVL +5.37%）。**盘中形态确认是消息驱动**：5 分钟数据显示盘前和上午前段在 $102-106 缓慢爬升，上午出现约 $3 跳空（$106.14 → $109.045），随后 $109-111 高位横盘到收盘 — 典型的「消息落地→快速重定价→新水位横盘」，不是全天资金持续买入。1.12x 量比也支持：若是机构建仓量比会在 1.5x 以上。**关键风险：这是谈判不是签约。** 一篇分析标题直接点破 'Intel Stock Jumps 4% on SK Hynix Rumor, But Here's Why the Real Win Is Years Away' — 晶圆厂改造成存储产线是多年工程（存储与逻辑芯片的制程/设备/洁净室要求都不同）。今天涨的是期权价值不是现金流。另有一篇 'Intel (INTC) Could Be 80% Undervalued After SK Hynix Fab Talks' — 基于一次谈判传闻推出 80% 低估，记下来是为了识别顶部信号：当卖方开始用传闻做 DCF，情绪已领先事实。

**Sources.**
- MT Newswires/Yahoo: [Intel Jumps 8%, SK Hynix Climbs 5% as Ohio Memory Talks Reignite; Micron Rises 6%](https://finance.yahoo.com/)
- Yahoo: [SK Hynix and Intel explore US memory chip partnership](https://finance.yahoo.com/)
- Yahoo: [Intel Stock Jumps 4% on SK Hynix Rumor, But Here's Why the Real Win Is Years Away](https://finance.yahoo.com/)
- Yahoo: [Micron Jumps 5% as Intel CEO Says Memory Prices Have Surged Over 500%](https://finance.yahoo.com/)
- Yahoo: [Intel Considers Rejoining the Memory-Making Biz](https://finance.yahoo.com/)
- _Corroboration:_ SKHY ADS +5.24% / SK Hynix 韩本 (000660.KS) +3.25% / MU +5.37% / SNDK +5.90% / DRAM ETF +4.57% 同日 — 跨标的确认。AMD +6.13% / MRVL +5.37% 同日说明有板块 beta 成分
- _Data:_ 盘中 5m: 盘前 $102.87 → 上午跳空 $106.14→$109.045 → 收盘区间 $109-111。全天区间 $101.05-$111.37 (振幅 10.2%) ()
- _Data:_ 估值更新: fwd PE 53.58x (thesis 撰写时 87x @ $134)。股价 -17.5% 而倍数 -38.4% → 隐含远期 EPS 预期上调约 34% ($1.54 → $2.06)。thesis 的「零安全边际」结论需改为「安全边际薄但不再为零」 ()
- _Data:_ MA50 $97.21 / MA200 $76.82，站上两条均线 +13.7% / +43.8%。距 52w 高 $142.35 -22.4%，距 52w 低 $28.73 +285% ()

**Cross-assets.** SPY +1.11% · QQQ +1.63% · VIX 15.58 · TEN YEAR 4.951 · DXY 100.24 · WTI 101.85

**Agent read.** **形态与 9/8 那次高度相似，这是今天最重要的风险提示。** 9/8 也是 +9.67%、也是未经公司确认的传闻（DigiTimes 的 PC CPU 涨价最多 10% 报道）、之后 9/10 -5.6% + 9/14 -5.6% 把涨幅还掉大半，到 9/16 仅回到 $101。**现在有两个待验证的传闻叠加**，检验点各自明确: (a) **10/05** 是 CPU 涨价传闻的生效日（timeline 已挂）；(b) **10/22 Q3 财报**是俄亥俄谈判的官方口径 — Intel 必须回应。两个日期的权重都因此升高：若 10/05 涨价落地 + 10/22 确认谈判在推进，则 $110 的基础扎实；若任一落空，9/8 和 9/17 两次约 9% 的涨幅都缺乏支撑，回撤空间是 $101（9/16 收盘）甚至 $97（MA50）。**6/30 那次的 agent read 至今有效**：「市场仍将 INTC 当 beta 交易不是 turnaround。Turnaround stories 在 sector panic 时 first to sell — 没有 moat buffer。」今天 1.12x 的温和量比说明这个性质没变。**一个被市场忽略的矛盾值得单独记**：Intel CEO 说存储涨价 500% 对 Intel 自己的毛利率是逆风（它是存储买方），而毛利率恢复到 50%+ 正是 thesis 的关键指标之一。今天市场只交易了「代工存储的机会」，没交易「采购存储的成本」— 10/22 财报的毛利率数字会把两面都摊开。**估值侧有实质改善**：当前 $110.49 在 Base 区间 ($120-140) 下沿 8.6% 处，介于 Base(40%) 和 Bear(35%) 之间，定价大致合理偏保守；而 thesis 撰写时 $134 在 Base 区间中上部且被判为「零安全边际」。距 thesis-break $75 仍有 +47.3% 缓冲，短期无结构性风险。
 · Snapshot at `dashboard/2026-09-17.md`

---
### 2026-09-10 · -5.57% day · ▼ material
**Tags:** `analyst_downgrade`, `pt_change`, `macro_rates`, `macro_inflation`, `sector_rotation`
**Confidence:** high

**Primary cause.** 跌幅第一, 也是当日唯一有具名个股催化剂的追踪标的。两条卖方动作同日: (1) Piper Sandler 的 David O'Connor **首次覆盖**即给 Neutral, 目标价约 $110 (隐含一年内 <10% 上行)。报告的多空拆分很具体 —— 看多: 行业从训练/推理转向 agentic AI 拉动 CPU 服务器需求, CPU 供给紧张 + 需求强劲推高产品价格, 支撑到 2030 年 high-teens 营收 CAGR; 看空 (也是给 Neutral 的理由): 股价一年涨超四倍, 且他估算 **当前市值约 45% 建立在 foundry 夺取全球 CPU 15 个百分点份额这个未兑现假设上**, 若不及预期会抹去过去一年大部分涨幅。(2) Mizuho 把目标价下调至 $92 — 低于现价, 理由是估值担忧, 尽管承认服务器需求更强、执行在改善。两家独立机构同日给出『基本面在改善但价格已透支』的同一结论, 说服力远大于单份报告。放大器: 本周上涨的基础是 DigiTimes 关于 10/5 可能上调 PC CPU 价格最多 10% 的**未经确认报道** (9/8 记录, 当日 +9.67%), 缺乏硬事实对冲。背景: 折现率冲击日 SOXX -3%, INTC fwd PE 49.1 为追踪半导体最高。反向证据: ASML 同日宣布扩大与 Samsung/Intel 的 High-NA EUV 合作, 制程路线图在推进 —— 方向差把归因锁定在估值而非基本面。

**Sources.**
- The Motley Fool: [Why Intel Stock Slumped Today (Piper Sandler David O'Connor initiates Neutral, PT ~$110; 45% of market cap on foundry winning 15 pts of global CPU share; high-teens revenue CAGR to 2030E)](https://www.fool.com/investing/2026/09/10/why-intel-stock-slumped-today/)
- 247wallst: [Intel Sinks 6% as Profit Taking Hits a Parabolic Run; NVIDIA and AMD Retreat 3% (YTD +188%, no company-specific news, price-hike report unconfirmed, consensus Hold / avg PT $115.88, Q3 guide $15.8-16.8B)](https://247wallst.com/investing/2026/09/10/intel-sinks-6-as-profit-taking-hits-a-parabolic-run-nvidia-and-amd-retreat-3/)
- Barchart: [Why 1 Veteran Analyst Just Trimmed His Intel Stock Price Target (Mizuho cuts PT to $92 on valuation despite stronger server demand)](https://www.barchart.com/story/news/4539051/why-1-veteran-analyst-just-trimmed-his-intel-stock-price-target)
- Yahoo: [ASML Expands High-NA Ties With Samsung and Intel as AI Demand Builds](https://finance.yahoo.com/technology/articles/asml-expands-high-na-ties-143900733.html)
- _Corroboration:_ 幅度分解: SOXX -3% (板块 beta, 与 NVDA -2.37% / AMD -3.36% 同档) + 约 2.6 个百分点个股 alpha (两份估值报告)。反例检验: 若纯 beta 应跌约 3%, 实跌 5.57%, 差额有具名个股解释, 归因自洽。
- _Corroboration:_ INTC 在工作区历史上反复是板块 risk-off 日跌最狠的名字 (7/1 -8.10%, 7/2 -5.61%, 8/18 -6.95%, 8/19 -4.02%), 且那四次大多无公司级利空。今天的差异是叠加了具名个股催化剂, 所以跌幅从『与板块同档』变成『板块的 1.9 倍』。

**Cross-assets.** SPY -0.58% · VIX 17.84 · TEN YEAR 4.944 · WTI 103.83

**Agent read.** 估值质疑而非基本面转差 —— ASML High-NA 合作扩大与两份估值报告方向相反, 这决定了反转条件是『时间/盈利追上估值』而非『基本面修复』。最硬的检验点是 10/5 CPU 涨价是否落地: 落地 = 9/8 那波 +9.67% 的基础从未确认报道变成事实; 不落地 = 该涨幅应全部回吐。唯一能直接击中 O'Connor 空头核心的事件是具名 foundry 大客户确认 (尤其 Apple 回归) —— 那会把『15 个百分点份额没有保障』变成合约。技术观察点 $100: 今日盘中低点 $99.34 已短暂失守, 收 $100.32。距 thesis-break $75 缓冲 +33.8%。另: Druckenmiller 已卖出 MU/AVGO/INTC (已披露历史持仓, 非当日催化, 但与估值质疑同向)。
 · [Snapshot](snapshots/2026-09-10.md)

---
### 2026-09-08 · +9.67% day · ▲ major
**Tags:** `analyst_upgrade`, `partnership_news`, `tech_breakthrough`, `sector_rotation`
**Confidence:** high

**Primary cause.** 四条催化剂同日叠加。(1) DigiTimes (Monica Chen) 报道 Intel 准备在 10/5 将 PC CPU 价格上调最多 10% — 年内第二次涨价; The Verge 亦有相近报道。(2) Northland 的 Gus Richard 把评级从 Market Perform 上调至 Outperform, 目标 $120, 理由是 turnaround 有实质进展 + 供应短缺。(3) Intel Foundry 与 ASML 官方发布 (Business Wire, Monterey CA) 合作加速 High-NA EUV 量产就绪; 同期 High-NA 累计产出破百万片晶圆, TSMC 与 Samsung 也承诺采购 — 但 Intel 是最早大规模部署的一家。(4) 美国政府 CHIPS 转股权持股账面浮盈约 $360-390 亿 (结果非原因, 但强化 sovereign put)。另有 Yahoo 标题称分析师认为 Musk 的 Terafab 可给 Intel Foundry 带来规模 — 该条在 stockanalysis 的完整分析师动作列表中查无记录, 无任何一方确认, 归因权重给最低。

**Sources.**
- MT Newswires via Yahoo: Market Chatter: Intel May Raise PC CPU Prices Another 10% in October; Shares Rise in Afternoon Trading
- TheFly / DigiTimes: Intel shares up 5% following report company plans to raise CPU prices (DigiTimes: up to 10% on October 5)
- Business Wire (official): Intel Foundry and ASML Collaborate to Accelerate Industry Readiness for High NA EUV
- stockanalysis.com analyst actions: Northland upgrades Intel to Outperform from Market Perform, price target $120
- Yahoo Finance: Intel Stock Jumps 9% on Chip Price Hike Report, US Stake Gains $36 Billion
- _Corroboration:_ 板块 vs 个股拆解: SOXX +2.0%, beta 2.23 → 板块贡献约 +4.5%, 剩余约 +5% 为个股 alpha。AMD 同日 +6.25% / TSM +2.69% 确认板块联动, 盘中形态两者几乎相同 (逐级推升非跳空)。
- _Corroboration:_ 逆向检验: NVDA 今日 -2.06%, 是唯一下跌的芯片股。若今天是『AI 芯片全面 risk-on』, NVDA 不该跌。说明资金买的是『x86 + 制程 + 能转嫁成本』这个定义, 而 NVDA 不在其中 (故事已于 8/26 财报出清)。
- _Corroboration:_ 仓位结构放大: 48 位分析师共识评级为 Hold, 平均目标 $115.78 (仅 +10%)。共识 Hold 的低配仓位在利好时的回补幅度大于减仓压力 — 这与 8/26 NVDA / 8/28 MRVL / 9/2 AVGO 三次『beat 却跌』(拥挤多头在报表日出清) 是同一机制的相反方向。

**Cross-assets.** SPY -0.48% · VIX 15.3 · TEN YEAR 4.8 · SOXX +2.00% · AMD +6.25% · NVDA -2.06% · TSM +2.69%

**Agent read.** 最重要的一条判断是对涨价性质的修正: MarketWatch 把涨价归因于『上升的供应链成本 (rising supply-chain costs)』, 而不是需求强劲。结合同日 DRAM/HBM 板块的内存合约价上行 (SNDK 周 +14.7 / SKHY +13.7 / MU +5.8), 最可能的成本源头就是内存 — 也就是说这是**成本转嫁型涨价而非 Porter 意义的定价权**。区别在于毛利率会不会扩张, 而 INTC thesis 明确写了判定 Bull 的核心指标是毛利率从约 40% 恢复到 50%+, fwd PE 51-58x 需要的正是这个扩张。10/22 Q3 财报的毛利率是唯一真正的裁决数据。第二条: 现价 $105.06 已接近卖方共识目标 $115.78 (+10%) 和 Northland 目标 $120 (+14%), 后续上涨需要目标价上调而非评级上调。第三条: Terafab 传闻是 INTC 第二次出现『未确认大客户传闻推动股价』的模式 (第一次是 6/18-6/30 的 Apple 回归传闻, 至今未官宣) — 同一模式重复应降低而非提高权重。第四条: trailing 净利润仍为 -$112.9 亿 (EPS -$2.30), 51-58x 建立在『明年大幅盈利』的预测上而该预测尚无实现记录; 但 FY25 亏损同比收窄 98.6% 是实质进展。风险层: beta 2.23 意味着 SOXX 跌 5% 对应 INTC 约 -11%, 而 7/1 的历史 (前日 +7.5% 次日 -8.1%) 是这个机制的实证; 今天四条催化同日出清, 到 10/22 财报之间 44 天无已知新增催化, 而 9/11 CPI + 9/17 FOMC 会双向放大。距 thesis-break $75 缓冲 +40.1%, 无操作压力。


---
### 2026-08-19 · -4.02% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** INTC −4.0%（5d −8.1%，30d −15.8%，本组最弱），半导体久期挤出延续（承接 8/18 −6.95% 的 macro_rates 抛售）。长端利率(30Y 触 2007 高)上冲叠加 AI 芯片板块整体承压（AVGO −4.6%/AMD −3.7% 同向）。无 INTC 公司级新催化，turnaround/foundry 叙事无进展。距 thesis-break $75 缓冲 +23.7%，未破位但趋势承压。

**Sources.**
- _Corroboration:_ 同 AI 芯片链承压：AVGO −4.6%/AMD −3.7%；久期挤出为 8/18 归因的延续。无个股硬催化。

**Cross-assets.** SPY +0.21% · VIX 14.89 · TEN YEAR 4.65 · WTI 84.32

**Agent read.** 


---
### 2026-08-18 · -6.95% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** INTC −7.0%（5d −1.4 / 30d −12.8，本组少数无前期涨幅缓冲的名字）。同 AI 芯片链的久期+AI开支质疑抛售 (见 MRVL 归因)。个股叠加：13F 披露 SoftBank (67% US 组合押 INTC) 与 NVDA ($30B 押注) 的集中持仓，市场在利空日对拥挤交易获利回吐。距 thesis-break $75 缓冲 +28.4%。turnaround/foundry 叙事无新进展。

**Sources.**
- secondary: [Intel and AMD Fall 4% as 13F Filings Reveal Concentrated Chip Bets](https://finance.yahoo.com/)
- secondary: [Nvidia, AMD, Broadcom, Meta Slide as Bond Yields Surge](https://finance.yahoo.com/)

**Cross-assets.** SPY -0.52% · VIX 15.66 · TEN YEAR 4.71 · WTI 84.14

**Agent read.** 


---
### 2026-08-04 · +11.02% day · ▲ major
**Tags:** `sector_rotation`, `flow_event`, `unattributed`, `ai_demand`
**Confidence:** low

**Primary cause.** No identifiable company-specific catalyst. INTC rose purely on risk-on sector rotation and oversold-bounce/short-squeeze mechanics after falling 35% in July. Financial media flagged the disconnect explicitly, noting the biggest winner of the day was 'the one that fell 24% last month and still has no trailing earnings to justify the bounce'. Macro backdrop: S&P record high on US-Iran draft-deal progress, WTI -5.6%, 10Y -1.3%, SQQQ -10.6% signalling systematic short-cover across the tape.

**Sources.**
- Yahoo: [Intel Soars 10%, AMD Jumps 8%, Broadcom Rises 6% as Chip Stocks Ride a Risk-On Rally](https://finance.yahoo.com/)
- Motley Fool: [Why Intel Stock Fell 35% Last Month](https://www.fool.com/)
- _Corroboration:_ Whole-sector move with no INTC news: SMH +6.0%, AMD +9.3%, AVGO +7.4%, MRVL +13.8%. Inverse ETFs crushed (SQQQ -10.6%) confirming short-squeeze mechanics.

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** Quality 2/10 — the lowest-quality large gain in the entire tracked universe today, and confidence is deliberately set to LOW because there is genuinely nothing to attribute it to beyond flows. Three compounding problems. First, zero company catalyst: unlike SNDK (HBF standard), MRVL (China component restriction report), or SKHY (coverage initiations), INTC produced no news at all — a financial-media headline called out this exact incoherence. Second, valuation: forward PE 49 makes INTC the MOST expensive name in a sector where peers trade at 5-38x (MU 5.8, SNDK 6.8, NVDA 16.5, AVGO 21.6, MRVL 35, AMD 38). Paying 49x for the turnaround story while a 16.5x AI leader sits next to it is hard to defend on any framework. Third, volr 0.71x means even this 11% move lacked volume confirmation. The mechanism is almost certainly short-covering: INTC was a crowded short after -35% in July, and inverse-ETF liquidation across the tape (SQQQ -10.6%, SSPC -20.0%) shows systematic de-grossing rather than accumulation. Practical implication: this is the name most likely to give the gains straight back once the squeeze exhausts, because nothing changed about the foundry thesis. Distance to thesis_break_price of $75 is -26%, so no alert, but INTC remains -28% over 30 days and 10% below its 50MA ($112). The genuine INTC questions — 14A process milestones, foundry customer wins, Xeon design wins, US government equity stake actions — all remain unanswered and the next scheduled catalyst is not until the 10/22 print.
 · Snapshot at `dashboard/2026-08-04.md`

---
### 2026-07-15 · n/a day · ▼ major
**Tags:** `sector_rotation`, `china_competition`
**Confidence:** medium

**Primary cause.** MU -10% China DRAM 竞争恐惧 spillover 到全 semi 板块。INTC 作为 high-beta turnaround 票在板块恐慌时优先被卖。讽刺: 同日 HSBC doubled PT + Stifel raised PT 被完全无视。无 INTC-specific 催化剂。

**Sources.**
- Yahoo: Micron Drops 8% on China Competition Fears, Dragging Intel, AMD, and Marvell
- Yahoo: Here's Why HSBC Doubled The PT on Intel (INTC)
- Yahoo: Stifel Raises PT on Intel (INTC)

**Cross-assets.** SPY -0.10% · MU -9.90% · AMD -6.50% · NVDA -2.40%

**Agent read.** 纯 MU drag，非 INTC-specific。HSBC/Stifel 同日上调 PT 被无视 = 市场短期不信 turnaround。但 vol 0.55x 低，非机构出货。7/23 Q2 earnings 是真正 binary event: foundry + 18A + Xeon momentum 验证。距 break $75 缓冲 33%。


---
### 2026-07-02 · -5.61% day · ▼ major
**Tags:** `sector_rotation`, `ai_demand`, `thesis_debate`
**Confidence:** high

**Primary cause.** Day-2 continuation of OpenAI efficiency sector selloff. Zero INTC-specific catalyst — no analyst action, no foundry news, no Apple deal update, no government stake change. INTC -5.61% is worse than AMD -5.06%, TSM -2.32%, NVDA -2.29% — confirming market still treats INTC as high-beta beta ticker with no moat buffer. Narrative headlines ('Lip-Bu Tan magic worn off') are ex-post rationalization, not new information.

**Sources.**
- 24/7 Wall St.: [Has Lip-Bu Tan's Magic Worn Off? Intel Just Gave Back Its Gains](https://247wallst.com/investing/2026/07/02/has-lip-bu-tans-magic-worn-off-intel-just-gave-back-its-gains/)
- 24/7 Wall St.: [Forget Intel: Buy Microsoft Hand Over Fist on the Sector Rotation](https://247wallst.com/investing/2026/07/02/forget-intel-buy-microsoft-hand-over-fist-on-the-sector-rotation/)
- Yahoo/Zacks: INTC Outpaces Industry in a Year: How to Play the Stock? (Zacks #1 Strong Buy)
- _Corroboration:_ SOXX -6.22% today; MU -5.7%, AMD -5.06%, TSM -2.32%, NVDA -2.29% — INTC is 2nd worst semi after MU. No idiosyncratic catalyst found.

**Cross-assets.** SPY -0.54% · VIX 16.75 · TEN YEAR 4.48 · SOX -6.22% · AMD -5.06% · NVDA -2.29% · MU -5.70% · TSM -2.32%

**Agent read.** 2天累计 -13.7% (7/1 -8.1% + 7/2 -5.61%)。市场从 6/30 +7.5% 追高的 Xeon-Rubin/turnaround 叙事完全退潮回到 beta 交易。关键 tell: INTC -5.61% > AMD -5.06% > NVDA -2.29% — turnaround stocks 无 moat buffer, 在 sector panic 中 first to sell。但 vol_ratio 0.58x 依然低 = 无机构 capitulation, 情绪+algo 主导。距 thesis-break $75 仍有 +60% 缓冲, 7/23 Q2 earnings 是真正的判决日。此外 7/2 出现媒体转向 signal: '24/7 Wall St.' 从 6/30 bullish 'INTC AMD Jump 7%' 直接翻转到 7/2 'Lip-Bu Tan magic worn off' — sell-side sentiment 完成 180° 转向, 与 BofA MU flip 同步。
 · Snapshot at `dashboard/2026-07-02.md`

---
### 2026-07-01 · -8.10% day · ▼ major
**Tags:** `ai_demand`, `sector_rotation`
**Confidence:** high

**Primary cause.** Sector-level selloff from OpenAI efficiency + BofA bubble indicator. INTC-specific: complete reversal of yesterday +7.5% (Xeon DGX Rubin); market still treats INTC as beta ticker not fundamental turnaround.

**Sources.**
- Yahoo: Intel Drops 7%, AMD Slides 5%, Taiwan Semiconductor Falls 6% as BoA Flags Bubble Risk
- market: OpenAI efficiency gains hammer chip stocks
- _Corroboration:_ SOX -5%; all semis down; INTC no idiosyncratic catalyst

**Cross-assets.** SPY +0.08% · VIX 16.37 · TEN YEAR 4.47 · NVDA -1.20% · AMD -5.20% · TSM -6.70%

**Agent read.** 昨天+7.5%今天-8.1% net 2d -1.2%。市场仍将INTC当beta交易不是turnaround。Turnaround stories在sector panic时first to sell — 没有moat buffer(对比NVDA -1.2%)。不改长期thesis(break $75, 缓冲+71%)但短期会继续高beta双向。7/23 Q2 earnings是真正的vol事件和turnaround确认点。
 · Snapshot at `dashboard/2026-07-01.md`

---
### 2026-06-30 · +7.5% day · ▲ major
**Tags:** `risk_on`, `ai_demand`, `foundry`, `government_stake`, `thesis_validation`
**Confidence:** high

**Primary cause.** INTC 收盘 +7.5% 到 $141.67，30d +21%（$117 → $141），LBT 上任以来 +~500%。今日精确触发：(1) **Xeon 6 入选 NVIDIA DGX Rubin 主机 CPU**（24/7 Wall St. 当日 headline）；(2) **Q1 Data Center & AI 营收 $5.05B（YoY +22%）** 二次定价；(3) AMD 同日 +7% 印证是 chip risk-on broad bid，但 INTC 在 30d 内 +21% 已经 outperform，说明 idiosyncratic turnaround alpha 在叠加 beta。

**Sources.**
- 24/7 Wall St. (2026-06-30): [Intel, AMD Jump 7% as Chip Stocks Catch a Risk-On Bid](https://247wallst.com/investing/2026/06/30/intel-amd-jump-7-as-chip-stocks-catch-a-risk-on-bid/) — 直接催化报道
- Fortune (2026-06-03): [Intel's new CEO cut management layers in half. The stock is...](https://fortune.com/2026/06/03/intel-ceo-lip-bu-tan-ai-semiconductors-innovation/) — turnaround 框架
- _Data:_ Trump 政府将 $8.9B CHIPS Act 资助转为联邦股权 → 政府成为 Intel 股东 = sovereign put
- _Data:_ NVIDIA $5B 注资 (2025-09) + SoftBank 注资 (规模未披露)
- _Data:_ 管理层 12 → 6（砍一半），出售非核心资产还 $50B 债务
- _Rumor:_ Apple 可能回归 Intel foundry 作客户

**Cross-assets.** SPY +0.71% · QQQ +1.54% · SMH n/a · AMD ~+7% (同日) · NVDA +1.70% · 10Y 4.40%

**Agent read.** 三段式 turnaround 叙事现在完整：(1) 政府背书（$8.9B 股权）= 下行保护；(2) NVDA/SoftBank 注资 = AI ecosystem 反向背书；(3) Lip-Bu Tan restructuring + Xeon-Rubin 中标 + 14A on-track + Apple 回归传闻 = 上行催化。Vol 0.49x 低 → 今天是技术性 follow-through 不是 capitulation buy。**风险**：(a) PE 已被掩盖（trailing PE None = 亏损），市值 $712B vs 当前盈利能力 = 全部押在未来 turnaround 兑现；(b) 30d +21% 已 price in 部分胜利；(c) 政府股权约束 — 联邦股东的存在可能限制激进资本配置（如分拆 foundry）；(d) Apple 回归仍是 rumor，未官宣。下一信号点：7/23 Q2 财报（Data Center 增长是否 sustain ≥ 20% YoY、foundry 客户披露、14A 进展确认）。**今天起 INTC 提升至 focus，加入 AI capex cluster。**
 · Snapshot at `dashboard/2026-06-30.md`

---
