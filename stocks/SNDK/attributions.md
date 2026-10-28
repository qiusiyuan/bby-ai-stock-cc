# SNDK attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-28 · +5.60% day · ▲ material
**Tags:** `sector_rotation`, `earnings_pre_print`
**Confidence:** medium

**Primary cause.** **+5.60% 是 read-through, SNDK 自身零公司新闻 —— 而 read-through 的口径有问题: SK Hynix 的「售罄至 2029」指引是 DRAM/HBM, SNDK 是 NAND, 两者周期不同步。** 置信度记 medium 而非 high 正是因为这个口径错配。「SKHY Stock: ...Company's Q3 Beat Uplifts MU, SNDK, WDC」。||**🎯 明天 (10/29) 是 state.yaml::earnings_watchlist 的 scoring_date, status=pending。** claim 原文: 「SNDK 从 NAND 周期股 re-rate 为结构性现金牛 —— FY27 指引 ($10.3-10.8B rev / $44-46 EPS) 兑现 + 半数营收转 FCF 模型可信 + 毛利率 (84.6% 峰值) 不快速回落」。||**8/06 的 sell-the-news 判据 (带 >30% 的 5 日涨幅进财报 = 好数字被打折) 本次仍不适用: 5d 为 -0.02%, 不是 +30%。所以风险全在数字本身, 不在仓位拥挤度。** 注意 5d -0.02% 意味着本周涨幅**全部集中在今天这一天**。||**今天新增一条直接相关的逆风证据, 而且来自内存行业最权威的一方: SK Hynix 宣布放弃 Solidigm 的纳斯达克 IPO。** CEO Kwak Noh-jung 原话「鉴于市场状况, 此时难以完全实现预期收益」。Solidigm 是 SK Hynix 2020 年从 Intel 收购的 NAND/SSD 业务。**一家内存龙头在内存最热的一天 (自己营业利润率 79.7%、宣布售罄到 2029) 判断旗下 NAND 资产不是上市的好时机 —— 这是对「NAND 与 DRAM 周期不同步」最强的行为证据, 而 SNDK 今天 +5.60% 的跟涨部分正是建立在两者同步的假设上。**||其余口径: 「Did The Market Read SanDisk Stock Right?」、「Sandisk Stock Is Down 45% From Its High. History Suggests This Is What Happens Next.」、「Is Western Digital's Nightmare 3 Months Over? A Wall Street Pro Says Its Price Will Increase 130%」、「Lumentum vs. Sandisk: Which Tech Stock Is the Better Buy in November?」—— 全部是估值/历史类比, 零条公司事实。||风控: thesis_break $1,200, 缓冲 **+14.8%** (10/27 为 +8.7%, 两天放松 6.1pp)。MA50 下方 **-12.30%** (组内最深) / MA200 上方 +10.19% / 距 52w 高 **-41.47%** / 远期 PE 5.17x / put/call 0.76。||**kill conditions 四条里第一条「Non-GAAP 毛利率连续两季压缩 (84.6% 峰值开始回落) = NAND 周期见顶」明天直接裁决。** 第四条「HBF 到 2027 年中仍未拿下任何具名 design win = 重定价 call option 归零」明天是第一个检查点。SNDK 的触发器是本工作簿少数**正确覆盖当前真正在定价的风险**的一组 (10/22 曾记录此判断)。

**Sources.**
- (aggregated): SKHY Stock: Analyst Sees 175% Upside Potential For SK Hynix, Company's Q3 Beat Uplifts MU, SNDK, WDC
- Korea Herald: SK hynix's AI memory 'sold out' through 2029 as profits soar (Solidigm Nasdaq IPO dropped)
- Motley Fool: Sandisk Stock Is Down 45% From Its High. History Suggests This Is What Happens Next.

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-10-27 · +3.92% day · ▲ material
**Tags:** `analyst_upgrade`, `earnings_pre_print`, `sector_rotation`
**Confidence:** medium

**Primary cause.** **财报与 🎯 评分日前两天 (10/29), 跟随内存板块反弹但 5d 仍为负。**||驱动是 BofA 转多内存 —— 同一篇报道点名「Micron Climbs 4% as Bank of America Grows More Positive on Memory; **Western Digital Rises 5%, SanDisk Gains 3%**」。另有多条财报前瞻: 「SanDisk's report could reignite the AI trade — or signal a warning」; 「Sandisk Stock Has Been Cut Nearly in Half Since June. Should You Buy It Before Thursday's Report?」; 「Chip Stocks Find Support Before Key Reports From Intel, Sandisk」。confidence 记 medium —— 板块驱动明确但无 SNDK 公司级事实。||**风控位置: thesis_break $1,200 缓冲由 10/26 的 +4.6% 松到 +8.7%** (今天 +3.92%), 但仍是未击穿名单里第二近的 (最近的 NOK 已击穿, 其次 SNDK +8.7%, 再次 GOOG +13.2%)。5d **-4.43%** / 30d -14.77% / 距 52w 高 **-44.58%** / MA50 下方 -17.50%。||**🎯 10/29 评分卡 (state.yaml::earnings_watchlist, status: pending, 窗口自 10/22 已开)**, thesis_claim 原文: 「SNDK 从 NAND 周期股 re-rate 为结构性现金牛 —— FY27 指引 ($10.3-10.8B rev / $44-46 EPS) 兑现 + 半数营收转 FCF 模型可信 + 毛利率 (84.6% 峰值) 不快速回落」。Tier 1 六项: 营收、EPS、non-GAAP 毛利率轨迹、数据中心增速、半数营收转 FCF 首个数据点、HBF design win 进展。||**8/06 的 sell-the-news 判据 (带 >30% 的 5d 涨幅进财报 = 好数字打折) 本次不适用 —— 5d 是 -4.43%。所以风险全在数字本身, 没有仓位拥挤的折扣效应。**||**一个有利的日历结构: SK Hynix 的 3Q26 创纪录读数已在 10/28 韩国时间给出 (营收首破 100 万亿韩元, 利润七倍), 即 SNDK 评分前有一份免费的 read-through。** 但两者口径不同 —— SK Hynix 是 DRAM/HBM 主导, SNDK 是 NAND。NAND 的毛利率轨迹是整个内存超级周期「价格能维持多久」的最早读数, 这是 10/29 最该看的单一数字。

**Sources.**
- 24/7 Wall St.: Micron Climbs 4% as Bank of America Grows More Positive on Memory; Western Digital Rises 5%, SanDisk Gains 3%
- Yahoo Finance: SanDisk's report could reignite the AI trade — or signal a warning
- Motley Fool: Sandisk Stock Has Been Cut Nearly in Half Since June. Should You Buy It Before Thursday's Report?

**Cross-assets.** SPY +0.57% · VIX 17.52 · TEN YEAR 4.993 · FIVE YEAR 4.84 · THIRTY YEAR 5.305 · WTI 100.66 · BRENT 110.07 · DXY 102.344 · GOLD 4075.9 · SILVER 54.45 · BTC 80650.73

**Agent read.** 评分前两天的最后一条可操作提醒: 门槛已预先承诺, 不能事后调整。5d 为负意味着 sell-the-news 判据不适用, 风险全在数字。最该看的单一数字是 non-GAAP 毛利率轨迹 —— 它是内存周期价格持续性的最早读数, 且 SK Hynix 的 DRAM 口径不能替代。
 · Snapshot at `dashboard/2026-10-27.md`

---
### 2026-10-26 · +1.42% day · ▲ minor
**Tags:** `analyst_upgrade`, `memory_pricing`, `earnings_pre_print`, `sector_rotation`
**Confidence:** medium

**Primary cause.** **记录本条是因为风控线与评分日同时逼近, 不是因为 +1.42% 够大。**||**⏰ 评分日 10/29, 还有 3 天 (评分窗口自 10/22 已开)。** 待评命题 (state.yaml::earnings_watchlist, status: pending): 「SNDK 从 NAND 周期股 re-rate 为结构性现金牛 —— FY27 指引 ($103-108亿 营收 / $44-46 EPS) 兑现 + 半数营收转 FCF 模型可信 + 毛利率 (84.6% 峰值) 不快速回落」。Tier 1 还含数据中心增速维持与 HBF design win 进展。||**🚨 风控: $1,255.58 距 thesis_break $1,200 仅 +4.6%** —— 全书第二近 (仅次于已击穿的 NOK)。10/15 时为 +12.1%, 10/22 为 +4.2%, **一周内几乎没有松动**。这是全书少数「kill condition 正确覆盖了当前真正在定价的风险」的标的: 预设的「毛利率快速回落」正是市场在定价的东西, 对照 NOK (实际杀伤是成本过账) / GEV (客户融资) / AVGO (倍数+信用) 三者的 kill condition 全是「需求崩塌/执行失败」型。||**两条方向相反的证据:**||🔴 逆风 (10/15 记录, 至今有效): **Counterpoint Q3 全球手机出货同比 -20%, 2012 年以来最弱 Q3, 直接归因 DRAM/NAND 涨价。** 这对「毛利率 84.6% 峰值不快速回落」这一条是**直接逆风** —— 需求破坏是已发生的事实而非预期。||🟢 顺风 (今天): **BofA 转多内存** (SPY 口径「Western Digital Rises 5%, SanDisk Gains 3%」), 但性质是卖方动作、零运营事实, 且 SNDK 实际收盘仅 +1.42% 为内存组涨幅最小。||**8/06 设下的 sell-the-news 判据本次不适用。** 原判据: 「带 >30% 的 5 日涨幅进财报 = 好数字打折」。今天 5d **-8.43%**, 方向与该判据设定的前提相反 —— **所以 10/29 不存在「涨太多打折」的风险, 风险全在数字本身。** 这与 10/08 的记录一致 (当时 5d -10.78%)。||**位置: 低于 MA50 20.82% (全组最深), 30d -19.10%, 远期 PE 4.71x, 距 52w 高 -46.7%。**

**Sources.**
- MT Newswires/Yahoo: Micron Climbs 4% as Bank of America Grows More Positive on Memory; Western Digital Rises 5%, SanDisk Gains 3%
- Yahoo Finance: Sandisk Earnings Preview: What to Expect
- Counterpoint Research: Counterpoint: Q3 全球手机出货同比 -20%, 2012 年以来最弱 Q3, 直接归因 DRAM/NAND 涨价 (10/15 记录, 至今有效)

**Cross-assets.** SPY +0.71% · VIX 18.39 · TEN YEAR 4.99 · FIVE YEAR 4.82 · THIRTY YEAR 5.3 · WTI 101.32 · BRENT 115.3 · DXY 102.018 · GOLD 4027.5 · SILVER 53.97 · BTC 79704.67

**Agent read.** 三天后评分, 而风控线缓冲一周未松动 (+4.2% → +4.6%)。两条证据方向相反但等级不同: 需求破坏是已发生事实 (hard), BofA 转多是卖方动作 (soft)。8/06 的 sell-the-news 判据不适用 (5d 为负), 所以 10/29 的全部风险在数字本身 —— 这实际上是好事: 判据干净、无情绪污染。SNDK 是本周三场连续裁决 (10/27 三星 / 10/28 SK Hynix / 10/29 SNDK) 的最后一场, 也是唯一一场同时结清一个预设评分卡的。
 · Snapshot at `dashboard/2026-10-26.md`

---
### 2026-10-22 · -9.31% day · ▼ major
**Tags:** `memory_pricing`, `competitor_news`, `earnings_pre_print`, `analyst_downgrade`, `sector_rotation`
**Confidence:** high

**Primary cause.** **🚨 两条线同时收紧到全书最紧，而且是在一个没有公司新闻的日子里。** (1) 价格 $1,249.88 距 thesis_break_price $1,200 **仅 +4.2%** —— 10/15 时为 +12.1%，**一周压缩 7.9pp**; (2) **10/29 是预设的财报评分日 (state.yaml::earnings_watchlist, status: pending)，评分窗口 ±7d 自今天 (10/22) 正式打开。**||今天 -9.31% 的驱动有两条，都是外部的: (a) **Cramer 两天前 (10/20) 的具名警告** —— 「如果数据中心容量萎缩，SNDK 和 WDC 是最危险的持仓」，并指出它们的 YTD 涨幅使风险不对称; (b) 今天 NOK 与 Lam 共同确认的成本结构性上升。||**成本侧证据链今天拿到第三层 (客户官方指引) 与第四层 (设备厂官方口径):** (1) 10/15 Counterpoint — Q3 全球手机出货同比 -20%, 2012 年来最弱 Q3, 直接归因 DRAM/NAND 涨价; (2) 10/15 巴克莱下调 Dell/HPE — 内存成本过账虚增服务器营收不带毛利; (3) **10/22 NOK 下调自由现金流指引 + CEO 称供应挤压是「结构性成本上升，不只是短缺」并计划因成本通胀涨价 (客户自己的账, 最硬)**; (4) **10/22 Lam Research -9%, 点名「供应链约束」限制指引; AMAT -6% / ASML -4%**。Lam 这条让成本故事自我强化: 设备交不出 → 产能扩不上 → 内存价格维持高位更久 → 下游需求破坏继续。**今天市场在「价格 vs 数量」里明确选了数量。**||**🔴 这直接撞上 SNDK 评分卡的一条 Tier 1 门槛: 「non-GAAP 毛利率 (84.6% 峰值) 不快速回落」。** 内存/NAND 涨价对 SNDK 这个卖方是**卖价顺风**，但 NOK 的财报证明下游在被挤压并开始涨价转移给终端，而 Counterpoint 证明终端已经在萎缩 (手机出货 -20%)。**所以同一件事对 SNDK 是「价格好、数量坏」—— 10/29 的毛利率和出货量是唯一能把这两者分开的数据点。**||**一条已建立判据今天不适用，必须明说: 8/6 建立的 sell-the-news 判据 (带 >30% 5d 涨幅进财报 = 好数字打折) 本次不适用 —— 5d 为 -10.39%，是带着大幅下跌进财报，不是带着涨幅。** 这反而意味着好数字有被定价不足的空间，与 8/6 的情形相反。||**估值与位置**: 远期 PE **4.7x** (另有卖方按 10/19 价格算出 17.6 倍 trailing，对照 S&P 中位数 22.7x); 距 52w 高 $2,354.39 为 **-46.91%**; vs MA50 $1,599.03 偏离 **-21.8%**; 30d -26.16% 为本组第二差 (仅好于 SKHY -29.37%)。||**kill conditions 状态**: (1)「non-GAAP 毛利率连续两季压缩 (84.6% 峰值开始回落) = NAND 周期见顶」—— **10/29 是第一个检查点，今天无数据**; (2)「FY27 指引被下修，或『半数营收转 FCF』模型被悄悄放弃/walk back」—— 10/29 检验。**与今天的其他标的不同，SNDK 的 kill conditions 恰好覆盖了当前的实际风险 (毛利率与现金流转换)，这是全书少数触发器设计正确的案例。**||**宏观共因已被排除为跌因**: 2Y -17.3bp / 10Y -18.1bp 平行下行、TLT +2.03%、债市撤回加息押注 — 折现率给了近 20bp 顺风而权益仍跌, 跌幅必须由风险溢价全额解释。**参与度限定: 全场量比中位数 0.79x, 仅 10/35 过 1.0x、2/35 过 1.5x (NOK 1.83 / GEV 1.75, 两只都有具名新闻)。方向可信, 幅度不可信。**

**Sources.**
- 247wallst: [Cramer warns SanDisk and Western Digital are worst stocks if data center capacity shrinks](https://247wallst.com/investing/2026/10/20/cramer-warns-sandisk-and-western-digital-are-worst-stocks-if-data-center-capacity-shrinks/)
- TIKR/Stocktwits: Nokia cuts cash flow view; CEO: supply squeeze is 'a structural cost increase, not just a shortage'
- Yahoo Finance: Chip stocks fall as equipment maker Lam Research cites 'supply chain constraints'
- {"type": "computed", "title": "thesis_break $1,200 \u7f13\u51b2\u4e00\u5468\u5185\u7531 +12.1% \u538b\u7f29\u5230 +4.2% (\u538b\u7f29 7.9pp); \u8bc4\u5206\u7a97\u53e3 10/22 \u6253\u5f00, \u8bc4\u5206\u65e5 10/29", "publisher": "workspace"}
- {"type": "research", "title": "8/6 sell-the-news \u5224\u636e\u672c\u6b21\u4e0d\u9002\u7528 \u2014 5d \u4e3a -10.39% \u800c\u975e >+30%", "publisher": "workspace"}
- Trefis: Could SanDisk Be The Value Stock For Your Portfolio? — 17.6x trailing vs S&P 中位 22.7x (按 10/19 价格)

**Cross-assets.** SPY -1.44% · VIX 19.37 · TEN YEAR 4.957 · TWO YEAR 4.65 · WTI 99.19 · DXY 101.6 · GOLD 4055.4 · BTC 81063

**Agent read.** SNDK 是今天风控上最紧的标的: 价格缓冲 +4.2% (全书最紧) 加上 10/29 评分日, 两条线同时到期。与其他标的不同, 它的 kill conditions (毛利率压缩 / FCF 模型 walk back) 恰好覆盖当前的实际风险, 所以 10/29 的评分是有意义的 — 不像 NOK/GEV/META 那样触发器与机制不重叠。8/6 的 sell-the-news 判据本次不适用, 这反而给好数字留了被定价不足的空间。
 · Snapshot at `dashboard/2026-10-22.md`

---
### 2026-10-15 · -4.10% day · ▼ material
**Tags:** `memory_pricing`, `earnings_pre_print`, `sector_rotation`
**Confidence:** high

**Primary cause.** **SNDK 今天取代 MU 成为存储组美国侧最弱的一环, 而且它的暴露在今天的新证据下是组内最直接的。** -4.10% 为组内 (剔除韩国本线) 今日最大跌幅, 5d -16.38% 为组内最差, 30d -13.55%。||**🔴 今天存储叙事从单侧变成双侧 —— 这是本轮下跌四天里最重要的性质变化.** 10/12-10/15 四天的全部跌幅建立在一个**供给侧预期**上: 中国 CXMT 把更密的 DRAM 设计对准服务器内存 → 未来供给增加 → 价格周期提前见顶。10/14 报告的核心批评是这个假设至今零技术细节 (❌无制程节点 ❌无位密度 ❌无 DDR5/HBM 指认 ❌无时间表 ❌无产能数字 ❌无第三方良率验证); 今天是第 4 天 / 自 9/21 首次出现算起是**第 25 天**, 这六项**仍然一项未动**。||今天新增的证据性质完全不同, 它从**需求侧**攻击同一个论点: **Counterpoint Research — 2026 年第三季度全球智能手机出货量同比 -20%, 是 2012 年以来最弱的第三季度, 直接归因于 DRAM 与 NAND 价格飙升推高整机成本。** 重要性在于论点类型变了: CXMT 是一个**预期** (未来可能有更多供给, 无法验证, 可以持续数季不被回答); 手机出货 -20% 是一个**已发生的事实** (涨价已经消灭了需求, 单位数据已在账上)。||内存多头论点的核心是「定价权」, 而定价权的边界条件就是需求弹性。手机是 DRAM/NAND 最大单一终端市场之一, -20% 的出货降幅 + 14 年来最弱 Q3 + 第三方研究机构直接归因于内存涨价 —— **这是本 workspace 记录以来第一次看到内存涨价的代价以单位需求的形式被量化。** 配合巴克莱下调 Dell/HPE 的理由 (内存成本过账虚增服务器营收, 不带毛利), 产业链里的分配机制也被点明: 内存涨价不是纯增量, 而是从下游转移。||**因此对存储组的态度需要修正**: 在今天之前合理的态度是「跌幅建立在一个无证据的供给预期上, 等 10/26 免费拿答案」; 今天之后 —— **跌幅里现在有一部分建立在一个有证据的需求事实上。即使 10/26 把 CXMT 完全否掉, 需求弹性这一侧的坏消息不会被同时否掉。**||**为什么手机出货 -20% 对 SNDK 的打击重于 MU**: SNDK 是 NAND 纯标的, 而 **NAND 在手机里的内容权重大于它在服务器里的权重** (手机是 NAND 最大的单一终端应用之一, 而 AI 数据中心的增量需求主要落在 DRAM/HBM 上)。MU 有 DRAM + HBM + NAND 三条腿, 其中 HBM 完全不受手机影响; SNDK 的腿更少且更偏手机。||**🎯 两条线同时逼近, 这是今天 SNDK 最该记的事:** **(1) 风控线** — 价格 $1,345.77 距 `thesis_break_price` $1,200 仅 **+12.1%** 缓冲, 全书第二近 (仅次于 NOK 的 +3.9%)。该线由用户于 8/7 确认, 定在震荡低位附近、高于 7/29 低点 $1,016, 作为更早预警的安全垫。5d -16.38% 的斜率在压它。**(2) 评分日** — `state.yaml::earnings_watchlist` 的 `scoring_date` 为 **2026-10-29** (已按 yfinance 从 11/04 校正), `status: pending`, 评分窗口 ±7d 已于 **10/22 打开**。||要打分的 claim 是: 「SNDK 从 NAND 周期股 re-rate 为结构性现金牛 —— FY27 指引 ($10.3-10.8B 营收 / $44-46 EPS) 兑现 + 半数营收转 FCF 模型可信 + 毛利率 (84.6% 峰值) 不快速回落」。**今天的手机出货 -20% 数据是对这个 claim 中「毛利率不快速回落」一项的直接逆风**, 因为终端需求萎缩会同时压 NAND 出货量与价格。评分前必须把这条读进 Tier 1 门槛, 否则会在一个已经被公开数据削弱的门槛上给出「兑现」的判定。||另一条已记录的判据仍有效: 8/6 的 sell-the-news 规律 —— 带 >30% 的 5d 涨幅进财报 = 好数字打折。**今天 5d 是 -16.38%, 方向完全相反, 所以该判据在本次不适用; 反过来说, 低位进财报意味着好数字的弹性更大。**||价格位置: 距 52w 高 $2,354.39 已 **-42.8%**; 跌破 MA50 $1,591.26 (-15.4%); PE 19.27x。||**宏观共因 (今天的共因只有一个, 但它的形状是反直觉的).** 九月 PPI (Producer Price Index, 生产者物价指数 — BLS 每月发布, 衡量生产者卖出价格, 通常领先 CPI 一到两个季度) 环比 **+1.3%** (8月 +0.5% / 7月 +0.2%, 2022年3月 +1.7% 以来最大单月), 同比 **+6.3%** (2022年12月 +6.4% 以来最大年度涨幅); 核心 (除食品/能源/贸易服务) 环比 +0.5% / 同比 +5.0%; 商品 +2.6% 其中**能源 +10.8% / 汽油 +20.3%**。接在 10/14 CPI 同比 3.7% (共识 3.6%) 之后, 是连续两天的下游+上游双向确认。零售销售同时跳升、失业申领保持稳健 —— 三项数据同向意味着经济不弱而价格在涨, 这是加息路径最不利的组合。||**❗但长端的反应方向和教科书相反, 本条必须作为限定随附**: 3M (^IRX) 4.088% **仅 +0.3bp**, 5Y 4.903% **-8.9bp**, 10Y 5.089% **-10.1bp**, 30Y 5.424% **-10.1bp**, TLT +1.52% (5d +2.85%)。**前端一动不动而 5年到30年平行下行 10bp —— 这个形状不可能是 Fed 政策定价 (政策定价必先动前端), 只能是对久期本身的避险需求。** 当天新闻口径直接说出了这件事 ('Tech slumps as AI financing worries grow, investors flock to bonds')。||**⭐ 方法论升级 (改写 10/05、10/07、10/08、10/14 四份报告的同一条限定)**: 那四天记录的都是「长端**不动**」—— 即对利空/利多都无响应, 属于零信息的否证, 只能说明「没有反证」。**今天长端第一次动了, 而且方向是下行**, 也就是折现率给了权益一个**顺风**, 权益却继续跌。结论因此从「无反证」升级为「有正面证据」: 折现率通道今天是负贡献 (利好), 跌幅必须由风险溢价**全额**解释。||**横截面否证「加息打击高倍数/长久期股」—— 本周第三次**: PE 从 SKHY 9.74x / DRAM 9.84x / MU 12.79x 一直到 AMD 148.2x / PLTR 172.0x / TSLA 340.0x, 跨 35 倍; 跌幅区间只有 -0.26% ~ -4.14% 且与倍数**无关** (TSLA 340x 跌 1.84% 却轻于 DRAM 9.8x 的 3.18%)。真正把跌幅排序出来的是「是否在 AI 供给/融资链上」。||**参与度限定 (与 10/14 相反)**: 38 只标的量比中位数 **0.755x**, 仅 11 只过 1.0x, 4 只过 1.5x。10/14 为中位数 1.02x / 17-of-32, 当时记为「本轮下跌序列第一个全参与度日」—— **一天后没有延续, 那是一个点不是趋势**。且今天放量的位置极度集中在韩国两条本线 (2.06x / 1.96x) + DRAM ETF (1.55x) + TSM (1.52x 财报日), 美国大型科技几乎无成交 (MSFT 0.54x / AMZN 0.54x / TSLA 0.47x / GOOG 0.39x / META 0.36x)。**这是对一个特定位置的定向抛售, 不是广泛降风险。**||**指数层面第一次方向分离**: QQQ -0.61% (跌破 MA50 $726.34) vs Dow +0.86% vs IWM +0.74%, 裂口 1.47pp。前四个下跌日 (10/07、10/08、10/13、10/14) 都是全指数同向。30d 口径 QQQ +2.26% vs IWM -6.77% 裂口从 10/14 的 12.4pp 收窄到 9.0pp, **且是用纳指跌、小盘涨的方式收窄 —— 轮动而非普跌的硬证据**。落点新闻一致: Moderna +6% (资金流入医疗) / Walmart +3% (德银上调) / Opendoor-Zillow +7% (长端回落直接利好住房)。VIX 16.88 (+0.06%) 几乎零反应, 第五次确认「不是系统性恐慌」。

**Sources.**
- Counterpoint Research via American News Group: A 20% Drop in Smartphone Shipments Shows Who Wins When Memory Gets Expensive — Counterpoint: Q3 2026 全球手机出货同比 -20%, 2012 年以来最弱 Q3, 归因 DRAM/NAND 涨价
- Motley Fool via Yahoo: Why Is Sandisk Stock Still Dropping? Investors are still selling Sandisk stock today
- Yahoo: AI Trade Takes Another Hit Thursday as Tech Sell-Off Continues — Memory chip and data storage stocks fell
- {"type": "computed", "title": "\u8ddd thesis_break $1,200 \u4ec5 +12.1% (\u5168\u4e66\u7b2c\u4e8c\u8fd1); scoring_date 2026-10-29 status=pending, \u8bc4\u5206\u7a97\u53e3 10/22 \u5df2\u6253\u5f00", "publisher": "workspace"}

**Cross-assets.** SPY +0.09% · VIX 16.88 · TEN YEAR 5.089 · WTI 96.58 · DXY 102.101 · GOLD 4168.2 · BTC 82171

**Agent read.** SNDK 是今天新证据 (手机出货 -20%) 打击最直接的标的 — NAND 纯标的, 手机内容权重高于服务器。两条线同时逼近: 风控缓冲只剩 +12.1% (全书第二近) 且 10/29 是 pending 评分日。评分时必须把需求破坏读进「毛利率不快速回落」这一 Tier 1 门槛。8/6 的 sell-the-news 判据本次不适用 (5d 为 -16.38% 而非 +30%)。


---
### 2026-10-14 · -5.33% day · ▼ major
**Tags:** `memory_pricing`, `sector_rotation`, `macro_inflation`, `earnings_pre_print`, `unattributed`
**Confidence:** low

**Primary cause.** **SNDK 的 -17.08% (5d) 缺乏独立成因, 这是本条的核心 — 置信度只能给 low。** CXMT 是 DRAM 厂, **NAND 不是它的战场**, 而今天可取到的所有报道里没有任何 SNDK 的公司级消息。所以 -5.33%/-17.08% 要么是存储板块情绪的无差别溢出, 要么另有未被报道的成因。⚠️ 不要把它当作 CXMT 影响 NAND 的证据 — 那是在没有传导链的情况下补一个因果。跌破 MA50 $1,591.35 (低 11.8%)。**距 thesis_break $1,200 缓冲 +16.9%, 是全书第二近 (仅次于 NOK 的 +4.44%)。** **时间点结构非常不利: 10/22 进入评分窗口 → 10/29 财报评分日 (scoring_date, status: pending)。claim 是「NAND 周期股 → 结构性现金牛 — FY27 指引 $10.3-10.8B rev / $44-46 EPS 兑现 + 半数营收转 FCF 模型可信 + 毛利率 (84.6% 峰值) 不快速回落」。** **⭐ 8/6 设的判据在这次不适用, 需在 10/22 重设**: 原判据是「带 >30% 5d 涨幅进财报 = 好数字打折 (sell-the-news)」, 而这次是 **5d -17.08% 的坏价格进财报**, 方向完全相反。原判据只覆盖「高预期」一侧, 不覆盖「低预期」一侧, 所以 10/22 评分窗口开启时必须单独立一条针对低预期进场的判据, 否则 10/29 的价格反应将无从判读。历史背景: SNDK 的 attributions 里已记「CXMT (长鑫存储) 中国扩产是短缺叙事的主要反证来源」, 以及 Solidigm (SK Hynix 的 NAND 事业部) 正准备 $100亿 美国 IPO — 后者是 NAND 供给侧结构性事件, 中期对 SNDK 是竞争信号。|| 宏观共因 (三个独立的因, 不可压成一个): **(1) 九月 CPI**: 同比 +3.7% (共识 3.6%)、环比 **+0.6% 为过去一年最高**。CPI = Consumer Price Index, BLS 每月发布的美国最主要通胀指标。环比年化约 7.4%, 远高于 Fed 2% 目标。timeline 在今天之前已记 Oxford Economics 的提示 — 九月调查窗口内柴油 +60 美分/加仑、汽油 +20 美分, 油价冲击会进入这份读数, 所以这个数字是可预告的。它接在 9/17 FOMC 转鹰 + 9 月纪要 (10/07 公布) 指向今年再加一次息 (市场当时只给 19%) 之上, 是纪要后第一个硬数据且站在纪要一边。**(2) ❗长端拒绝配合 — 本条必须作为限定随附**: CPI 超预期而 10Y -2.7bp / 30Y -3.8bp / TLT +0.66%。媒体口径写的是 'rate-hike jitters'、'rising bond yields', 债市当天的实际方向与之相反。所以今天的跌**不能用「当天利率上行」解释** — 实现通道是风险溢价 (VIX +10.48%) 与叙事, 不是折现率。这是本月第四次长端对本应推高它的消息不配合 (10/01 失败突破 / 10/02 非农利多无响应 / 10/08 诱因缓解不修复 / 今天 CPI 超预期不涨)。**(3) 横截面否证「加息打击高倍数股」的单一叙事**: 倍数最高的 TSLA (fwd PE 168x) 跌 2.15%, 低于倍数中等的MRVL (33.7x) -8.73%、SNOW (111x) -6.34%、GEV (37x) -6.20%。跌幅与 **30d 涨幅**的相关性明显优于与倍数的相关性(MRVL 30d +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小跌幅)。**今天卖的是一个月里的涨幅, 不是久期。** **⭐ 方法论变化 (改写前三份报告的限定)**: 10/05、10/07、10/08 三份归因都写了同一句「半量里的下跌属『没有买盘』而非『出现卖盘』, 方向可信幅度不可信」。**今天不成立**: 量比中位数 1.02x (10/08 为 0.48x / 10/07 0.79x / 10/05 0.49x), 17/32 过 1.0x (10/08 为 3/34), 放量集中在跌最多的标的 (GEV 1.65x / QQQ 1.53x / TSM 1.45x / KOID 1.39x / MRVL 1.31x / DRAM 1.30x)。**这是这轮下跌序列里第一个全参与度的下跌日 — 幅度本身开始带信息。** 反方限定仍要记: 跌最惨的 MRVL 量比只有 1.31x、MU 只有 1.04x, 「放量」是全场性的而非个别标的清仓。

**Sources.**
- 247wallst via yfinance (CPI 3.7% YoY vs 3.6% 共识; MoM +0.6% 年内最高): Trump Media and Rumble Decline 5% as September Inflation Runs Above Forecasts; Reddit Slides 2%
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- IBD via yfinance: Stock Market Today: Nasdaq Dives On Rate Hike Jitters, AI Woes; Taiwan Semi Earnings On Deck
- Yahoo Finance video (Baird 策略师 Ted Mortonson): CoreWeave, Intel, Micron, & other tech stocks are plummeting. Here's why.
- 247wallst via yfinance (10/13): Micron Falls 5% as China's CXMT Targets Server Memory; SanDisk Drops 4%

**Cross-assets.** SPY -1.08% · QQQ -1.97% · IWM -1.93% · DIA -0.11% · VIX 16.87 (+10.48%) · TEN YEAR 5.190% (-2.7bp) · THIRTY YEAR 5.525% (-3.8bp) · TLT +0.66% · WTI +1.16% · BRENT $106.06 (30d +12.05%) · GOLD -1.23% · SILVER -5.81% · DXY 102.530 (+0.34%) · BTC -1.81% · ETH -3.40% · BREADTH 32 只中 26 跌 / 6 涨 (含 2 只反向) · VOLUME MEDIAN 量比中位数 1.02x · 17/32 过 1.0x (10/08 为 0.48x · 3/34)

**Agent read.** 最有价值的产出不是归因 (本条置信度 low), 而是发现 8/6 判据的覆盖缺口: 它只定义了「高预期进财报」的判读规则, 没定义「低预期进财报」。10/22 窗口开启时必须补上, 否则 10/29 评分会在没有预先承诺标准的情况下进行 — 那正是评分卡机制要消除的东西。


---
### 2026-10-08 · -5.76% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`, `memory_pricing`
**Confidence:** medium

**Primary cause.** NAND 侧随存储组同向, 无独立公司消息。1d -5.76% / 5d -10.78%, 量比 0.52x。**对 10/29 评分卡的直接影响**: 8/06 设下的 sell-the-news 判据是「带 >30% 的 5 日涨幅进财报 = 好数字打折」; 今天 5d 是 **-10.78%**, 方向与该判据设想完全相反 → 若这个动能保持到 10/22 (评分窗口开启), 该判据需要重算为反向情形 (低动能进财报 = 好数字弹性更大)。待评 claim 仍为「NAND 周期股 → 结构性现金牛」(FY27 指引 $10.3-10.8B rev / $44-46 EPS / 84.6% 峰值毛利率不快速回落 / 半数营收转 FCF)。距 thesis_break $1,200 缓冲 +32.9%。 || 宏观共因 (已按盘中时序校正, 勿用收盘涨跌读因果): **触发是地缘** — 美国据报考虑扩大对伊朗打击, 叠加一艘油轮遇袭。当日标题: 'Oil surges, stocks sink as US reportedly eyes new Iran strikes' / 'U.S. Stocks Slip, Oil Rises on Fresh Tanker Attack' / 'Dow Tumbles, Oil Surges, and Yields Rise to New 24-Year Highs as Trump Considers Ramping Up Iran Attacks' / 'Nasdaq Slumps On War Worries'。盘中路径: WTI 开 89.86 → 冲 **93.08** → 收 90.97; 10Y 盘前 **5.331** → 收 5.239; 30Y 开 5.695 (24 年高位区) → 收 5.615; QQQ 开 754.29 → 高 756.93 → 收 **745.35** (贴当日低 744.39)。**关键: 两个诱因 (油/长端) 当天都缓解了, 权益却收在当日低点附近 —— 纯 beta 事件应在诱因缓解时修复, 今天没有。** 只看收盘 (10Y -2.5bp / 30Y -4.4bp / TLT +0.77%) 会误读成「利率转松而久期资产崩盘」; 利率今天是上午推手、下午缓解项, 不是反常项。对照 10/01 (长端失败突破日 SKHY +5.08% / GEV +3.89% / MU +3.03% 全线反打): 同样的利率先冲后落路径, 那天权益修复了, 今天没有。**差异在「不修复」, 不在利率方向。** **第二段 (不修复) 的 AI 侧候选解释**: Broadcom 为 OpenAI 芯片安排 >$500亿 融资 (Apollo/Blackstone 参与), SPCX $400亿, Oracle 同期发债, 三家抢同一批买家; 媒体口径从 'war worries' 转为 'growing AI caution'; Michael Burry 称市场处于 'denial'。**但有一条有力反证, 不应略过: 同日 Anthropic 宣布计划在云与算力上支出 $5,180亿 — 量级极大的 AI capex 利多, 整组没涨。** → 可读成「信用担忧压过需求利多」, 也可读成「市场今天对任何 AI 消息都不反应」(情绪/风险偏好)。**诚实结论: 地缘是因, AI 谨慎是让它不修复的那一层, 但今天的数据不足以把信用与纯 beta+情绪分开。判别点在 10/15 TSM 指引与 10/28 capex 指引。** 跌幅分布事实 (排他性因果不成立): 开支方 GOOG -0.43%/AMZN -0.78%/META -0.87%/MSFT -0.95% vs 供给方 NVDA -2.30%/TSM -3.24%/AVGO -3.35%/INTC -5.53%/MRVL -5.89%, 两簇不重叠 — 但战争风险日里单纯 beta 差异足以产生同样分裂。**量能限定 (双向适用)**: 全书 34 只量比中位数仅 0.48x, 仅 3 只过 1.0x → 半量里的 5% 级下跌, 属「没有买盘」而非「出现卖盘」, 方向可信幅度不可信。**同日两个反向硬数据**: Samsung 发创纪录营收/利润初步业绩、TSMC 九月营收超目标 — 供应链两个独立层级同日确认需求, 价格全部反向 → 需求侧无恙。

**Sources.**
- via yfinance SNDK news: Dow Jones Futures Fall As Oil Prices, Treasury Yields Jump; Samsung, Micron, Taiwan Semi, Sandisk In Focus
- via yfinance MU news: Micron Stock Drops—and Not Even Samsung's Record Profit Can Give It a Lift
- via yfinance AMD news: TSMC Gives AI Trade Upbeat Signal—AMD and Other Chip Stocks Fall Anyway

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-09-23 · -3.62% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** SNDK -3.62%，无公司级新闻。同 memory/NAND 复合体一起承受 10Y 破 5.12%（2007 年高位）的久期外流。跌幅与前期涨幅正相关而非与基本面相关：1w +19.66% 是整个 watchlist 最大周涨幅之一，今日回吐最多。缩量 0.39x——机构未在此价格换手，仅买盘缺席。同日 INTC（1w +19.06%）-2.86%、AMD（1w +19.67%）-1.68%，三个前期涨幅最大的名字同步回吐，确认为涨多回吐而非需求端恶化。

**Sources.**
- : [10-year Treasury yield hits highest level since 2007 as market prices in another Fed rate hike](https://finance.yahoo.com/quote/%5ETNX/)
- : [Stocks, Bonds Slip as Oil Jump Fuels Fed-Hike Bets (Bloomberg)](https://finance.yahoo.com/quote/CL%3DF/)

**Cross-assets.** SPY CHANGE -0.74% · VIX 15.34 · TEN YEAR 5.12 · WTI 91.41 · DXY 101.19 · QQQ CHANGE -1.01%

**Agent read.** 距 thesis-break $1,200 缓冲 +51.6%，3mo -7.4%。11-06 Q1 FY27 财报挂载评分卡（『NAND 周期股 → 结构性现金牛』），评分卡内已预置的判据在此生效——『带 >30% 5d 涨幅进财报 = 好数字打折』(8/6 sell-the-news 判据)。今天的回吐实际上降低了财报前的估值透支风险。建议加入 focus（连续活跃 + 挂载评分卡）。
 · Snapshot at `dashboard/2026-09-23.md`

---
### 2026-09-21 · -1.41% day · ▲ material
**Tags:** `memory_pricing`, `sector_rotation`, `earnings_pre_print`
**Confidence:** low

**Primary cause.** SNDK -1.41% 到 $1,766.64 今日收绿, 但 5d +13.83% 触发 5 日阈值, 30d **+45.74%** 是全持仓最强。今天是**全链唯一在存储上涨日收绿的标的** — 头条「SanDisk Falls 2% Despite Memory Rally; Micron Advances 3%, Western Digital Nudges Higher」明确点出这个反常。归因为获利了结, 不是新的负面信息: 量比 0.85x (缩量), 无公司级坏消息。技术位在上方 — 头条「SanDisk Faces a Make-or-Break Test at $1,832」指出关键阻力在 $1,832, 今天 $1,766.64 距该位 -3.6%。fwd PE 6.67 — 30 天涨 45.74% 之后仍是单位数前瞻市盈率。

**Sources.**
- (none)

**Cross-assets.** SPY +1.55% · SMH +4.02% · MU +2.77% · SKHY +0.73% · DRAM ETF +3.30% · VIX 14.87 · TEN YEAR 4.963 · WTI -8.31% · FWD PE 6.67

**Agent read.** **这是一条低置信度归因: -1.41% 在 0.85x 缩量下, 没有任何可引用的公司级催化剂, 纯粹是 30d +45.74% 之后的获利了结。** 记录它的原因是 5d +13.83% 跨过了阈值, 以及它的相对表现 (全链唯一收绿) 本身是信息: 在存储链整体上涨、SMH +4.02% 的一天里独自下跌, 说明最强的那只先被兑现。11/06 是财报评分日 (state.yaml 原记 11-04, yfinance 校正为 11-06), 评「SNDK 从 NAND 周期股 re-rate 为结构性现金牛」。Tier 1: 营收 $10.3-10.8B / EPS $44-46 / non-GAAP 毛利率 (84.6% 峰值) 不快速回落 / 数据中心增速维持 / 半数营收转 FCF 首个数据点 / HBF design win。**评分卡里已写明的判据现在正在应验: 「带 >30% 5d 涨幅进财报 = 好数字打折」(8/6 sell-the-news 判据)。当前 30d +45.74%, 距财报 46 天 — 期望值已经被抬到很高的位置。** 今天的小幅回落可能是这个动态的第一次表达。距 thesis-break $1,200 缓冲 +47.2%。
 · Snapshot at `dashboard/2026-09-21.md`

---
### 2026-09-17 · +5.90% day · ▲ material
**Tags:** `memory_pricing`, `executive_comment`, `sector_rotation`, `macro_rates`
**Confidence:** medium

**Primary cause.** **无独立公司级催化 — 纯跟随存储链的价格叙事。** 驱动是 Intel CEO 称存储价格涨超 500%（买方口径确认，详见同日 MU/INTC 条目）+ 'The Memory Shortage Is Not Over: More Upside for Micron and Sandisk?' 的行业观点 + 加息后 risk-on（10Y 5.00%→4.951%，VIX -12.03%）。**一个必须标注的归因精度问题：SNDK 的 HBM 敞口为零。** SNDK 是纯 NAND flash（从 Western Digital 分拆），Intel CEO 说的 500% 涨价更可能指 DRAM/HBM 而非 NAND。**所以 SNDK 今天的涨幅里有一部分是「存储」这个标签的误伤（正向的）** — 市场把它和 MU/SKHY 放进同一个价格因子交易，但它的产品线不同。这是 confidence 定为 medium 而非 high 的原因。**但有一条正面的分化证据**：同期 Western Digital -4%、Seagate -5%（'Western Digital Falls 4% Despite Its AI Storage Pitch; Seagate Drops 5%, Micron Holds Steady'）。市场把 SNDK 归入 AI 存储受益方，把 WDC/STX 归入传统 HDD。**这个区分对 SNDK 的「NAND 周期股 → 结构性现金牛」re-rate 命题是支持性证据** — 说明市场不是无差别买存储，而是在做产品定位的区分。**5d -4.97% 是存储三家最弱**，今天反弹幅度最大（+5.90%）— 典型的「跌最多、弹最猛」，这也弱化了「基本面重估」的读法。

**Sources.**
- Yahoo: [The Memory Shortage Is Not Over: More Upside for Micron and Sandisk?](https://finance.yahoo.com/)
- Yahoo: [Micron Jumps 5% as Intel CEO Says Memory Prices Have Surged Over 500%](https://finance.yahoo.com/)
- Yahoo/Motley Fool: [Sandisk Is Up More Than 1,700% in a Year and Still 33% Off Its Peak. History Says This is What Happens Next.](https://finance.yahoo.com/)
- Yahoo: [Sandisk $1,500 Stock Price Ignites Fresh Split Frenzy](https://finance.yahoo.com/)
- Yahoo: [Sandisk (SNDK) Refinances Credit Line As Valuation Debate Sharpens](https://finance.yahoo.com/)
- _Corroboration:_ **关键分化证据**：Western Digital -4% / Seagate -5%（传统 HDD）vs SNDK +5.90%（AI 存储）。市场在存储内部按产品定位分层，不是无差别买入。同日 MU +5.37% / SKHY +5.24% / DRAM +4.57%
- _Data:_ 量比 0.53x — 存储三家最低。5.90% 涨幅配 0.53x = 无新增机构资金，是空头减压/做市商调仓形态 ()
- _Data:_ 估值：fwd PE 6.08x / trailing 21.83x。市值 $236B（三家最小）。距 52w 高 $2,354.39 **-31.6%**（三家里离峰值最远），距 52w 低 $93.535 **+1,621%**。MA50 $1,505.44 (+6.9%) / MA200 $1,060.31 ()

**Cross-assets.** SPY +1.11% · QQQ +1.63% · VIX 15.58 · TEN YEAR 4.951 · DXY 100.24 · WTI 101.85

**Agent read.** **归因诚实度：这不是 SNDK 自己的故事。** 它今天涨 5.90% 是因为被打上了「存储」标签，而涨价消息的产品指向更可能是 DRAM/HBM 而非 NAND。所以 confidence 定 medium。**真正有信息量的是 WDC/STX 的反向走势**（-4% / -5%）— 市场在存储内部按「AI 存储 vs 传统 HDD」分层，把 SNDK 放在受益侧。这是对 11/06 那张评分卡（「NAND 周期股 → 结构性现金牛」）的**外部支持证据**：如果市场只把 SNDK 当周期股，它应该和 WDC/STX 同向。**11/06 的 Tier 1 门槛**：营收 $10.3-10.8B、EPS $44-46、non-GAAP 毛利率（84.6% 峰值）不快速回落、半数营收转 FCF 的模型可信度。**两个需要警惕的过热信号：** (1) **拆股狂热** — 'Sandisk $1,500 Stock Price Ignites Fresh Split Frenzy'。拆股讨论是散户情绪指标不是基本面，它出现在一年 +1,700% 之后，是过热的边际信号。(2) **估值辩论在升温** — 'SanDisk Stock Looks Cheap, But Can It Keep Earning This Much?'、'SNDK Rewarded Dip Buyers Before, But Is It Still The Same Company?'、'Sandisk (SNDK) Refinances Credit Line As Valuation Debate Sharpens'。三篇独立文章都在问「这个盈利水平能维持吗」— 这正是 11/06 评分卡要回答的问题。**一个结构性提醒**：距 52w 低 +1,621% 但距 52w 高仍 -31.6% — 这个组合意味着股价经历过一次完整的暴涨和大幅回撤，当前处于中间位置。**在三家里 SNDK 的命题最未经检验**（MU 有 6/24 那份 blowout 做基准，SKHY 有 HBM 领先地位的既成事实，SNDK 的「结构性现金牛」完全是前瞻性主张）。距 thesis-break $1,200 缓冲 +34.1%，无短期风险。
 · Snapshot at `dashboard/2026-09-17.md`

---
### 2026-09-15 · -2.28% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`, `memory_pricing`
**Confidence:** medium

**Primary cause.** **5 日 -12.74% 是全组合最差周线**, 触发 5d≥10% 阈值。今天单日 -2.28%, 媒体把它与 WDC (-4%) / Seagate (-5%) 归为一类「存储链承压」, 同时指出 Micron 相对持平。无 SNDK 公司级利空 —— 归因是折现率通道 + NAND 板块 beta。10Y 今天破 5.00% (2007 年 7 月以来最高), 明天 FOMC 市场定价加息。fwd PE 5.7x 与 MU (5.9x) / SKHY (5.1x) 同属「假性便宜」类别: 倍数隐含周期高点盈利维持多年, 折现率上升压缩的正是「多年」的现值, 因此低 PE 不构成安全边际。**位置上最值得警惕: 股价 $1,516.65 刚好贴在 MA50 ($1,509.45) 上, 而 thesis-break $1,200 的缓冲仅 +26.4%, 是所有重点股里最窄之一 (仅 AVGO +13.3% 与 GEV +25.8% 更窄或相当)。** 用户在设 $1,200 这个位置时明确说过是「更早预警的安全垫」(高于 7/29 低点 $1,016), 而 MA50 破了之后到 $1,200 之间没有明显技术支撑。历史对照: 8/17 SNDK +9.55% / 5d +45% 时的归因明确警告「+57% in 30d at 52w high 是教科书级不该加仓时点」, 次日 (8/18) 即 -8.92% 验证; 9/10 又 -4.06%。现价距 52 周高 $2,354.39 已 -35.6%, 那次警告的完整代价现在可见。下个催化是 2026-11-06 财报 (评分卡 status: pending, 判据是 FY27 指引 $10.3-10.8B rev / $44-46 EPS 是否兑现 + 84.6% 峰值毛利率是否快速回落)。

**Sources.**
- 247wallst: Western Digital Falls 4% Despite Its AI Storage Pitch; Seagate Drops 5%, Micron Holds Steady
- CNBC: 10-year Treasury yield hits highest level since 2007

**Cross-assets.** SPY -0.47% · VIX 17.46 · TEN YEAR 5.0 · WTI 105.95 · DXY 99.64 · GOLD 4342.5 · BTC 75913

**Agent read.** 缓冲 +26.4% 全组合最窄之一, 且刚好贴 MA50 —— 这条线是要盯的位置。8/17 的「不该加仓」警告的完整代价 (-35.6% from 52w high) 现在可见。


---
### 2026-09-10 · -4.06% day · ▼ material
**Tags:** `macro_inflation`, `macro_rates`, `sector_rotation`, `memory_pricing`
**Confidence:** high

**Primary cause.** 八月 PPI +5.4% YoY (预期 5.3%, 前值 4.8%; 核心 4.6% vs 前值 4.3%, 三个月最强) 叠加 WTI +8.16% 破 $103, 把 2Y 推高 13.3bp 至 4.56%、10Y 推高 11.7bp 至 4.96% —— 短端涨幅大于长端 = 市场定价 Fed 加息而非增长放缓。内存股 fwd PE 5-6 看似极便宜, 但这些倍数隐含的是周期高点盈利可维持多年, 折现率上升直接压缩『多年』的现值, 因此低 PE 不是保护。当日公司级新闻全部为正 (JPMorgan 给内存 Overweight、顶级分析师称内存涨价『数年不缓解』、Samsung-OpenAI 合作扩展到下一代芯片、MU 距 DRAM 第二仅差 1.6 个百分点、ASML 扩大 High-NA 合作), 唯一负面是 Intel 支持的初创进入内存市场 (对三年内格局无实质含义)。利好满仓仍跌 5% = 归因只剩折现率通道。 SNDK 侧最反直觉: 30 日 +66.61% 是全场涨幅第一, 却是复合体里跌幅最小的 (-4.06%), 成交量 0.62x 最低。若今天是纯获利了结, 涨最多的应该跌最多 —— 8/18 正是这样 (SNDK -8.9% 领跌复合体)。今天不是, 说明主导机制是压估值倍数 (与前期涨幅无关) 而不是抛获利盘。

**Sources.**
- 247wallst: Memory Stocks Slide as Rates and Oil Swamp JPMorgan's Overweight Call: SK Hynix Sinks 5%, Western Digital Drops 3%, Micron Slips
- Yahoo: Top Chip Analyst: Memory Prices Won't Ease 'For Years' and Even Apple Can't Dodge It
- Yahoo/MT Newswires: [Update: US Equity Indexes Fall as Hot Producer Prices, Soaring Crude Oil Boost Treasury Yields](https://finance.yahoo.com/economy/articles/us-equity-indexes-fall-hot-195114785.html)
- _Corroboration:_ 决定性反证: SK Hynix 韩国本土 000660.KS 仅 -0.16%、Samsung 005930.KS -0.19%, 而 SKHY ADS -5.20% — 同一公司同一天差 5.04 个百分点, 排除公司层面与 HBM 周期层面解释, 归因锁定美股时段折现率定价。
- _Corroboration:_ 历史对照 2026-08-31: 同类供给侧利好 (SK Hynix CEO 警告短缺到 2030 + Samsung 锁定 70% HBM 产能到 2031) 在 10Y 4.76% 时令复合体全线上涨 (SNDK +5.02/MU +2.53/SKHY +2.34/DRAM +1.78)。今日 10Y 4.944%, 同类利好换来 -4~5% — 18bp 之内供给侧利好的定价能力翻符号。7/31 SMH 预测的『供给侧例外条款』失效。
- _Corroboration:_ 成交量全部低于均量 (MU 0.82x / SKHY 0.95x / DRAM 0.71x / SNDK 0.62x) = 无机构 capitulation; 涨幅最大的 SNDK (30d +66.6%) 反而跌最少, 与『纯获利了结』形态矛盾 (对照 8/18 SNDK -8.9% 领跌)。

**Cross-assets.** SPY -0.58% · VIX 17.84 · TEN YEAR 4.944 · WTI 103.83

**Agent read.** 『涨最多却跌最少』是本次归因排除获利了结解释的关键交叉检验。SNDK 的 NAND/HBF 叙事 (8/13 Investor Day 的多年 FCF 模型 + 半数营收转 FCF) 在折现率冲击下表现出比 HBM 叙事更强的抗跌性。11/4 Q1 FY27 财报是『NAND 周期股 → 结构性现金牛』评分卡的打分日; 带 >30% 涨幅进财报 = 好数字打折 的 8/6 判据仍适用, 而 30d +66.6% 已远超该阈值。
 · [Snapshot](snapshots/2026-09-10.md)

---
### 2026-09-08 · +3.20% day · ▲ material
**Tags:** `commodity_move`, `index_inclusion`, `sector_rotation`, `pt_change`
**Confidence:** medium

**Primary cause.** 内存复合体板块上涨的一员, 30 日 +40.5% 为板块最强。两条驱动 + 一条机械因素: (1) 内存合约价上行 (与 SKHY/MU 同源; Barron's 报道新一轮内存芯片价格数据); (2) Goldman 指出 Micron 与 SanDisk 的技术突破信号, 多家给出激进目标价上调; (3) **纳入 S&P 100 带来的被动买盘** — 消息日 SNDK 曾单日 +12%。板块爆发日是 9/4 (SNDK 单日 +11.9%, 1,555 → 1,740)。**数据缺口: 具体合约价读数 (TrendForce/DRAMeXchange) 未取到全文, 置信度 medium。**

**Sources.**
- GuruFocus: Goldman Spots Breakout Signal for Micron, SanDisk Stocks
- Yahoo Finance: Micron, SanDisk get new aggressive price targets from top analyst
- Yahoo Finance: Sandisk Soars Nearly 12% Before Joining the S&P 100
- Motley Fool: SanDisk Stock Has Soared More Than 500% in 2026. Can the Rally Possibly Continue?
- _Corroboration:_ 板块同步: SKHY +5.68 / DRAM +3.32 / MU -0.27。SNDK 是 NAND 而非 DRAM/HBM, 但两者在『AI 挤出消费级存储供给』这条链上同源。对手方 AAPL -1.38% (成本承受方) 提供交叉验证。

**Cross-assets.** SPY -0.48% · VIX 15.3 · TEN YEAR 4.8 · SKHY +5.68% · MU -0.27% · AAPL -1.38%

**Agent read.** 需要把三部分涨幅分开: 合约价 (基本面)、目标价上调 (卖方情绪)、S&P 100 纳入 (机械被动买盘)。第三部分不可持续且已完成, 因此 30 日 +40.5% 的可持续部分小于表面数字。**最关键的一条是评分卡风险: SNDK 的 11/4 评分日 claim 是「NAND 周期股 → 结构性现金牛」, 而 thesis 已明确记录判据『带 >30% 5d 涨幅进财报 = 好数字打折』(8/6 sell-the-news 判据)。当前 30 日 +40.5%、YTD 超过 +500%, 这个风险已经成立。** fwd PE 6.8x 看似便宜, 但和 MU 一样是用周期顶部盈利算的 — 内存/NAND 股在周期顶部的低 PE 是常态而非折价。11/4-11/6 财报的 Tier 1 门槛 (营收 $10.3-10.8B / EPS $44-46 / non-GAAP 毛利率不从 84.6% 峰值快速回落 / 数据中心增速维持 / 半数营收转 FCF 首个数据点 / HBF design win) 是真正的裁决。SNDK 不在 focus 名单但已挂载评分卡, 已建议加入 focus。


---
### 2026-08-31 · +5.02% day · ▲ material
**Tags:** `memory_pricing`, `executive_comment`, `sector_rotation`, `commodity_move`
**Confidence:** medium

**Primary cause.** 内存短缺的官方时间表被延长了两到三年, SNDK 是复合体内弹性最高的标的因此领涨。两条同日消息: (1) SK Hynix CEO 在 $40 亿印第安纳 HBM 工厂动工时公开警告内存短缺将持续到 2030 年; (2) 报道称 Samsung 已锁定其 HBM 产能到 2031 年的 70%。对照工作区 7/31 的记录 — 当时短缺被 Samsung 官方延长到 2028 — 时间表在一个月内从 2028 推到 2030-2031。这是供给侧信息, 同时抬高未来多年的价格假设与确定性, 因此能在折现率上升时仍推高现值。全 cluster 同向: MU +2.53%, SKHY +2.34%, DRAM +1.78%, 而 SNDK +5.02% 幅度最大 (NAND/HBF 弹性最高 + fPE 5.9 最低)。

**Sources.**
- Yahoo Finance: SK Hynix CEO Warns Memory Shortage Will Persist Through 2030 as Chipmaker Builds $4 Billion Indiana Fab
- Yahoo Finance: The Memory Shortage Isn't Close to Ending — Samsung Just Locked Up 70% of HBM Capacity Through 2031
- Yahoo Finance: SK Hynix (NasdaqGS:SKHY) Breaks Ground On $4 Billion Indiana HBM Facility
- _Corroboration:_ 全 cluster 同向确认为板块驱动而非个股 alpha: MU +2.53%, SKHY +2.34%, DRAM ETF +1.78%。但成交量全部低于均量 (SNDK 0.69x, MU 0.51x, SKHY 0.35x, DRAM 0.28x) — 涨幅是消息驱动的重定价, 没有配置资金确认。ETF 量能最低 (0.28x) 是配置资金缺席的直接证据。反例: Samsung 自己约 -2.3% (5d -7.6%, 30d -7.0%) 独跌, 尽管锁定 70% HBM 产能的好消息主角就是它 — 四绿一黑判据指向 Samsung 公司层面问题而非 HBM 周期。
- _Corroboration:_ 本日发生在 10Y 升至 4.76% (逼近 52 周高位) 的同时。这不违反 7/31 记录的 SMH『半导体约束是折现率』预测 (今日机械判定 PASSED) — 该预测的原始 agent_read 已写明例外条件: 『除非出现新维度的信息 (例如供给侧而非需求侧的数据点)』。短缺延长三年正是该例外。

**Cross-assets.** SPY -0.35% · VIX 15.01 · TEN YEAR 4.76 · WTI 85.94 · SECTOR ETF +1.78%

**Agent read.** 这条归因的主要价值是建立 11/4 评分卡的基线。SNDK 的 earnings_watchlist 声明是『从 NAND 周期股 re-rate 为结构性现金牛』, 而今天的上涨来自周期性供需消息 (短缺延长), 不是结构性现金流证据 — 两者需要严格区分, 否则 11/4 打分时会把周期上行误算作结构验证。第二个要点: 涨幅真实但资金确认缺失 (全 cluster 量能 0.28-0.69x, ETF 最低)。一个『短缺延长三年』量级的消息若被真正相信, 应看到配置资金进场尤其是 ETF; 没有看到。月末清淡 + 长周末前的流动性环境解释了一部分, 但仍应把今天视为消息驱动重定价而非仓位建立。第三: 今天成立的机制是供给侧新信息这个明确的例外条件被触发, 不是折现率通道失效 — 把例外读成规律会在下一个无消息的加息日重新受伤。验证今天涨幅真实性的最有用指标不是价格而是 DRAM ETF 成交量能否回到 1x 以上; 最有信息量的解锁点是 9/25 MU 财报 (cluster 内唯一能把『短缺到 2030』换成可验证数字的标的, 看 HBM QoQ 是否 ≥+20% 及 FY27 指引语气)。风险线索: CXMT (长鑫存储) 中国扩产是短缺叙事的主要反证来源。距 thesis-break $1,200 缓冲 +30.0%。
 · Snapshot at `dashboard/2026-08-31.md`

---
### 2026-08-19 · -3.50% day · ▼ material
**Tags:** `sector_rotation`
**Confidence:** low

**Primary cause.** SNDK −3.5% 但 5d +16.71%——带 >30% 近期强势进入的获利回吐，属涨多回调/sell-the-news 前兆而非破位。无公司级利空新闻，成交量 0.97× 接近均量。11/4 Q1 FY27 财报评分（NAND→现金牛 re-rate）为关键节点；带高涨幅进财报=好数字打折的 8/6 判据仍适用。

**Sources.**
- _Corroboration:_ 无个股利空 headline；5d +16.7% 的强势背景下单日 −3.5% 属正常回吐。均量，非恐慌抛售。

**Cross-assets.** SPY +0.21% · VIX 14.89 · TEN YEAR 4.65 · WTI 84.32

**Agent read.** 


---
### 2026-08-18 · -8.92% day · ▼ major
**Tags:** `sector_rotation`, `macro_rates`, `memory_pricing`
**Confidence:** medium

**Primary cause.** SNDK −8.9%，内存复合体领跌。是昨日 (8/17) +9.6%/+45%5d 抛物线顶后的最陡反转——涨最猛、跌最惨的情绪面标的。5d 仍 +28%。同一驱动组合 (WSJ 报道 + 久期外流 + 获利回吐)。昨日 extreme 归因明确警告「+57% in 30d at 52w high 是教科书级不该加仓时点」，今日验证。距 thesis-break $1,200 缓冲 +35.6%。earnings_watchlist ~11/4 (评「re-rate 为结构性现金牛」)。

**Sources.**
- secondary: [Why Did Sandisk Stock Drop Today?](https://finance.yahoo.com/)
- secondary: [Cramer’s Career-Long Trading Rule Just Got Shattered by SanDisk’s Parabolic Run](https://finance.yahoo.com/)

**Cross-assets.** SPY -0.52% · VIX 15.66 · TEN YEAR 4.71 · WTI 84.14

**Agent read.** 


---
### 2026-08-17 (rev. 同日重估) · 5d +45.24% 分段归因 · ▲ extreme
**Tags:** `sector_rotation`, `memory_pricing`, `executive_comment`, `policy_us`, `policy_china`, `ai_demand`, `pt_change`, `thesis_debate`
**Confidence:** medium
**Scoring date:** 2026-11-04 (Q1 FY27 财报 — 「去周期化」论点的首个真实验证点)

**触发。** 有说法称「上周 SNDK 验证了长协的架构，意味着它不再是周期股，这是上周暴涨的原因」。本条为核查结果 + 对同日前一版归因的修正。**append-only：前一条 2026-08-17 记录保留原样，不修改。**

**修正一:5d +45% 必须分两段读。** 前一版把整段涨幅归为「板块轮动+情绪拉升，非公司硬催化」——对 8/17 今日成立，对 8/13–8/14 那一段不成立。
- **第一段(8/13–8/14,公司级实质事件)** — Investor Day 抛出跨 FY28–FY30 多年财务模型:80% 毛利率 / 75% 营业利润率 / mid-to-high-teens 营收增长 / 投资后 100% 超额现金返还。Morgan Stanley 转述管理层称 NAND 正进入 "a new era of long-term AI demand growth"，并称 100% 现金返还是 "a clear positive"。Evercore 点出 "multi-year demand visibility, margin expansion"。8/16 卖方系统性上调:JPMorgan 恢复 Overweight PT $2,250、Wells Fargo $1,400→$1,550、RBC $1,300→$1,600。
- **第二段(8/17 今日,政策+情绪)** — 商务部长 Howard Lutnick 周末表态(TipRanks 将今日 ~10% 直接归因于此，**这是前一版遗漏的最直接催化**);Trump 政府推 Apple 弃用中国内存芯片(Barron's: "Getting Its Mojo Back Amid China Memory-Chip Move");Musk 喊「内存瓶颈」;Bernstein 称 HBF 是 "Game Changer for AI"(当日一度 +3.5%)。

**修正二:估值口径。** fwd P/E 实为 **8.34 @ $1,789**，前一版记的 ~6x 取自 thesis.md 在 $1,634 时的过期口径。trailing P/E 24.27、营收 ttm $20.25B(+175.3%)、净利 $11.43B、EPS 73.76、市值 $266.63B、YTD +656%、52w $43.20–$2,354.39、PT 共识 $2,094.41(23 位分析师，Buy)。

**修正三:定性。** 从「三者里质量最低 / 最投机 / 经典周期陷阱」改为「**分布最宽的一只**」。8/13 多年模型 + 8/4 已落地的 HBF 标准，把论点从「NAND 商品周期股」换轨为「结构性 AI 内存参与者」。若模型成立，8.3x fwd P/E 是三者中最便宜;若不成立，回撤空间也最大。同时**撤回**「84.6% 毛利率几乎确定是周期峰值」这一断言——公司指引 FY30 仍维持 80%，该判断现在是有争议的而非确定的。

**「长协/LTA」核查结果:查无实据。** 遍查 stockanalysis.com SNDK 全量新闻流(8/13–8/17 约 25 条)+ workspace 内 `stocks/SNDK/` 全部历史归因与 thesis，检索 `长协 / long-term agreement / LTA / 合约定价 / committed capacity / take-or-pay` **零命中**。thefly.com 与 tipranks 单篇原文返回 403/404，Bing/DuckDuckGo/Google 本次均无法返回有效结果页。故「可及来源内无」≠ 确证不存在。**这一环最关键也最缺失:** 若真有 X% 产能被多年固定价格锁定的官方披露，去周期化就是可验证的会计事实;「管理层给了三年毛利率目标」只是预测——两者证据等级差一个量级。目前只有后者。

**反方论点(压力测试,记录以备 11/4 评分)。**
1. 每轮内存周期顶部都伴随一次「这次不一样」的结构性叙事:2017-18「数据中心结构性需求」、2021「云 capex 永久上台阶」，两次都在 12–18 个月内均值回归。本轮候选叙事是「AI 推理需求」。
2. 公司自述模型 ≠ 已验证。80%/75% 是**三年后**目标;首个可验证数据点 ~11/4 只验一个季度的 FCF 转化，不验 FY30。
3. **PT 上调最猛的 Wells Fargo($1,550)与 RBC($1,600)仍维持中性评级**(Equal Weight / Sector Perform)——模型可信度足以调价，不足以变买入。真 bullish 的只有 JPMorgan。
4. 对冲基金分裂(TipRanks: "Hedge Funds Are Split After Its 656% Rally");Situational Awareness(被称 'AI stock god')在 SNDK+MU 建 $5B+ 仓位后于 7 月爆仓——**同一结构性论点已让一位重仓专业投资者出局过一次。**
5. 对 NAND 厂商而言 75% 营业利润率是历史上从未出现的水平，应作高不确定性输入(且该数字来自 Evercore 转述，原文摘录被截断)。

**Sources.**
- TipRanks: Why Did SanDisk (SNDK) Stock Rally 10% Today, 8/17/26? — 归因 Lutnick 周末表态
- Barron's: Sandisk Stock Is Getting Its Mojo Back Amid China Memory-Chip Move
- TheFly: Evercore flags multi-year demand visibility, margin expansion in SanDisk outlook
- TheFly: SanDisk targets mid-to-high teens revenue growth for FY28-FY30 / expects to return 100% of excess cash
- TheFly: SanDisk 100% cash return 'a clear positive,' says Morgan Stanley
- TipRanks: SNDK Jumps 3.5% as 5-Star Bernstein Analyst Calls SanDisk's High Bandwidth Flash a "Game Changer for AI"
- TipRanks: Hedge Funds Are Split on SanDisk (SNDK) Stock After Its 656% Rally
- Business Insider: Leopold Aschenbrenner's Situational Awareness bet big on SanDisk and Micron before it blew up
- TheFly: SanDisk model suggests Micron EPS to $230+ by FY30, says BofA — 结构性论点已扩散到全板块
- _核查边界:_ thefly/tipranks 单篇 403/404;三家搜索引擎不可用;sandisk.com/company/newsroom 返回空内容。LTA 结论限于可及来源。

**Agent read.** 「不再是周期股」给一半分:方向部分成立(8/13 多年模型 + 8/4 HBF 标准是真实结构性事件)，但具体机制被记错了(是 Investor Day 模型，不是 LTA)，且零季度验证。质量排序(按已验证程度)SKHY > MU > SNDK 维持;分布宽度排序反向。11/4 看两件事:FCF 转化率、毛利率是否守住 80%+。真正的周期属性测试是 FY27 全年能否穿越一次 NAND 价格回调。另一个独立判据:HBF 是否出现 SNDK/SK Hynix 之外的第三方采用——标准变生态的分水岭。参见 [[SNDK 2026-08-04]] HBF 标准发布、[[SNDK 2026-08-14]] Investor Day 首日反应、[[MU 2026-08-17]] [[SKHY 2026-08-17]] 同日同故事。 · Snapshot at `dashboard/2026-08-17.md` (Semi Deep Dive §4)

---

### 2026-08-17 · +9.55% day · ▲ extreme
**Tags:** `sector_rotation`, `memory_pricing`, `executive_comment`, `policy_us`, `ai_demand`
**Confidence:** medium
> ⚠️ 同日 rev. 条目已修正本条的三处内容(5d 分段归因、fwd P/E 8.34 非 ~6x、定性从「最投机」改为「分布最宽」)。本条按 append-only 原则保留原文。

**Primary cause.** SNDK +9.6% 今日 / +45% 5d（extreme 级），但这是板块轮动+情绪拉升，非公司硬催化。三条量化证据：(1) 反向共振——同日大盘平台股 MSFT −2.4%/META −3.0%/AMZN −0.8% 在跌、指数几乎不动(S&P −0.17%)，即资金板块间搬家非新钱入场；(2) 全线缩量——SNDK vol 0.71x、MU 0.45x、DRAM 0.49x 均低于均值，说明存量换仓+空头回补+情绪追逐而非机构放量 conviction；(3) 全球内存链齐涨——Samsung 5d +19%/SK Hynix 韩股 5d +16%/DRAM ETF +7.3% 同向，整条链一起动=宏观叙事(AI 内存超级周期)重定价。软催化：Trump 政府推 Apple 弃中国内存芯片(policy，真实，直接利好 MU/内存链)+ Musk 喊'内存瓶颈'(名人喊话，情绪)。SNDK 涨最猛因它 beta 最高、纯 NAND 最投机、空头最多(回补最凶)——恰恰是三者里质量最低的：84.6% 毛利率近周期峰值，fwd P/E 6x 是峰值盈利上的低倍数=经典周期陷阱。三者质量排序 SKHY>MU>SNDK，弹性/风险排序反过来。

**Sources.**
- Yahoo: [SanDisk Rallies 8%, Western Digital Rises 6%, Micron Gains 5% as Elon Musk Flags a Memory Bottleneck](https://finance.yahoo.com/quote/SNDK/)
- Yahoo/Barron's: [Investors Remember Why They Love Memory-Chip Stocks](https://finance.yahoo.com/)
- _Corroboration:_ 反向共振：MSFT −2.4%/META −3.0%/AMZN −0.8% 同日下跌，指数 S&P −0.17% 走平=板块轮动而非普涨。全球链同向：Samsung 5d +19%/SK Hynix 000660 5d +16%。
- _Data:_ 全线缩量：SNDK vol 0.71x / MU 0.45x / DRAM 0.49x 均低于均值。SNDK fwd P/E ~6x on 84.6% 峰值毛利=周期陷阱信号。 ()

**Cross-assets.** SPY -0.17% · VIX 15.0 · TEN YEAR 4.3

**Agent read.** 板块轮动+情绪拉升，非三家各自新基本面。用户直觉两点都对：是轮动、且三者基本面不同(SKHY=HBM 质量龙头/MU=综合体时序领先/SNDK=纯 NAND 最投机)。短期唯一硬催化 NVDA 8/26 财报，传导强度 SKHY>MU>SNDK(NVDA 是 SKHY 头号 HBM 客户，不直接买 SNDK 的 NAND)。三只带大涨+缩量进财报=高 sell-the-news 风险，SNDK 最脆弱。中长期分化：SKHY 靠 2027 HBM 稀缺(结构最实)，MU 靠 9/25 证明份额升级，SNDK 押 HBF 标准(期权而非股票)。关键警惕：缩量上涨+全市场看多内存超级周期=拥挤信号。参见 [[MU 2026-08-17]] [[SKHY 2026-08-17]] 同日同故事。
 · Snapshot at `dashboard/2026-08-17.md`

---
### 2026-08-14 · +6.93% day · ▲ major
**Tags:** `analyst_upgrade`, `pt_change`, `ai_demand`, `memory_pricing`, `sector_rotation`
**Confidence:** high

**Primary cause.** SNDK +6.9% today / +34.8% 5d，续涨源自 8/13 SanDisk Investor Day 的卖方模型重定价（非财报——8/6 财报已 sell-the-news −5.4%）。核心催化：管理层给出 multi-year FCF 模型『Guided to Turning Half Its Revenue Into Free Cash Flow Through 2030』，把 NAND 龙头从周期股重定价为结构性现金牛。分析师上调：JPMorgan 目标价 $2,250(+38%)、RBC『长期目标高于预期，定价模型可持续』、一位分析师喊 $100B 回购。这是 analyst upgrade + 叙事升级驱动的 re-rating，read-through 拉动全 memory 板块（8/13: SNDK +15.3%/SKHY +8.3%/MU +6.28%）。今天续涨 +6.9% 证明不是一日情绪。技术位置：现价 $1634 卡在 MA50 $1655 下方 −1.3%，距 52w高 $2354 仍 −31%，距 7/29 低点 $1016 已 +61%（两周），vs MA200 $903 达 +81%。估值 pe_fwd 6.2（vs pe_ttm 19.5）——极低但完全建立在 FY27 EPS $44-46 指引兑现上。

**Sources.**
- Yahoo: [Sandisk Stock Soars as JPMorgan Targets $2,250 After Bullish Investor Day](https://finance.yahoo.com/quote/SNDK/)
- Yahoo/Motley Fool: [Sandisk Just Guided to Turning Half Its Revenue Into Free Cash Flow Through 2030](https://finance.yahoo.com/)
- Yahoo: [Sandisk Long-Term Targets Above Estimates, Pricing Model Sustainable, RBC Says](https://finance.yahoo.com/)
- Yahoo: [Why one analyst says investors should be cautious on the memory stock rally](https://finance.yahoo.com/)
- _Data:_ price $1634, pe_fwd 6.2 / pe_ttm 19.5, MA50 $1655 (−1.3%), MA200 $903 (+81%), 距52w高 −31%, off 7/29低$1016 +61%, volr 1.06 ()

**Cross-assets.** SPY -0.22% · VIX 14.32 · TEN YEAR 4.3

**Agent read.** 关键警告：这波是『叙事/分析师重定价』不是『新硬数据』驱动——涨的是估值倍数不是已证明的现金流。历史刚给过教训：8/6 SNDK 带 +38.9% 5d 涨幅进财报，beat 被读成 measured 直接 −5.4%（可复用判据：任何 memory 股带 >30% 5d 涨幅时好数字要打折，AMD/SPCX/SNDK 三样本已验证）。这次没有财报兑现，燃料是纯叙事——更脆。平衡点 = MA50 $1655：站稳放量→$1900+ 填缺口，JPM $2,250 是天花板；反复被压回→$1450 甚至 $1350(8月震荡区)消化两周 +61% 透支。pe_fwd 6.2 是『如果 FY27 指引成真』的便宜——若 NAND 消费段疲软(8/6 消费段 −32%)打折指引，pe_fwd 瞬间翻倍。下一硬验证要等 ~11 月下季财报兑现 FCF 转化模型。若无持仓，+61% off low 追高风报比差；持有则 MA50 失守放量=第一减仓信号。注意 NAND(SNDK/WDC)与 DRAM/HBM(MU/SKHY)是两个不同供需结构，SNDK Investor Day 是叙事共振非 HBM 定价直接利好。SNDK 工作区尚无完整 thesis（仅 attributions.md），建议 add-stock 建档以便 11 月评分。
 · Snapshot at `dashboard/2026-08-14.md`

---
### 2026-08-06 · -5.40% day · ▼ major
**Tags:** `prediction_passed`, `earnings_post_print`, `guidance_inline`, `memory_pricing`, `ai_demand`
**Confidence:** high

**Primary cause.** SNDK Q4 FY26 财报后 sell-the-news，精准验证 8/5 记录的基准情形(45%)。实际：EPS $39.25 (beat 13.5% vs $34.59)、营收 $8.97B (beat 6.5% vs $8.42B)、non-GAAP 毛利率 84.6% (去年同期 26.4%——爆炸性经营杠杆)、数据中心营收环比 +103% 到 $2.98B。Q1 FY27 指引营收 $10.3-10.8B / EPS $44-46——强但被读成 'measured/in-line' 而非大幅上行惊喜。盘后一度 -12%，8/6 收 -5.4%。机制完全如预测：带 5d +38.9% 涨幅进财报，beat 只是清算被抬高的期望，好数字要打折。read-through 检查点：SNDK -5.4% + WDC -5.36%(同为 NAND) 但 MU +0.06%/SKHY -2.2%/DRAM -2.1%——NAND 双雄独跌、DRAM/HBM 相对抗跌，说明是 NAND 个股期望透支 + 消费段疲软(-32%)问题，不是 AI 存储需求叙事被证伪，对 MU 9/25 评分卡无负面传导。

**Sources.**
- _Data:_ SNDK Q4 FY26: EPS $39.25 (beat 13.5%), 营收 $8.97B (beat 6.5%), non-GAAP GM 84.6% (vs 26.4% YoY), 数据中心 +103% QoQ 到 $2.98B, 消费段 -32% 到 $556M; Q1 FY27 指引 营收 $10.3-10.8B/EPS $44-46 (Investing.com) ()
- Yahoo: [SNDK Stock Dips After-Hours As Sandisk's Q1 FY27 Outlook Misses Expectations Despite Memory-Driven Q4 Profit](https://finance.yahoo.com/quote/SNDK/)
- Motley Fool: [Sandisk Earnings Soar, but the Stock Is Still Dropping](https://finance.yahoo.com/)
- _Corroboration:_ Read-through: SNDK -5.4% + WDC -5.36% (NAND 双雄) 独跌，MU +0.06%/SKHY -2.2%/DRAM -2.1% 相对抗跌——NAND 个股问题非 AI 存储需求证伪；vr 0.99 接近均值(比 8/4 的 0.76x 更实)

**Cross-assets.** VIX 15.93 · TEN YEAR 4.62

**Agent read.** 干净的预测验证：8/5 基准情形(45%)几乎逐字命中——beat 但 sell-the-news、-5~12% 回吐不破位、毛利率爆表但焦点转向 in-line 指引。三个同周活样本(AMD 8/5 -6.4%、SPCX 8/5 -10.8%、SNDK 8/6 -5.4%)共同确认『>30% 5日涨幅进财报好数字打折』的可复用判据。关键 nuance：Q1 FY27 指引其实很强(营收环比再 +15%)，跌是纯预期问题不是基本面转坏——SNDK 30d 仍 -31% 深度恢复位，中期空间判断(比 AMD 多)待后续验证。消费段 -32% 是唯一真实瑕疵但占比小。纯跟踪无持仓。
 · Snapshot at `dashboard/2026-08-05.md`

---
### 2026-08-05 · -1.13% day · ● minor
**Tags:** `prediction_recorded`, `earnings_pre_print`, `ai_demand`, `memory_pricing`, `sector_rotation`
**Confidence:** medium

**Primary cause.** 财报前瞻预测（Q4 FY26 今晚 8/5 AMC）。收入端：几乎必 beat（连续三季 40-65% beat，Q3 EPS $23.41 vs $14.17 est，营收 +251% YoY，NAND 上行周期 + HBF 标准 re-rate）。支出端是胜负手：毛利率周期位置 + capex 纪律 vs 扩产。结合今日市场：AMD(-6.4%) 与 SPCX(-10.8%) 均在强数字上因期望透支被卖出，SNDK 带 5d +38.9% 进财报踩同一陷阱。关键区别：SNDK 30d 仍 -28%、距 52w 高点 40%，是从 7 月 -47% 崩盘的恢复位而非高位，故短期 sell-the-news 但中期比 AMD 有更多向上空间。

**Sources.**
- _Data:_ Q3 FY26 EPS $23.41 vs $14.17 est (beat 65%), 营收 $5.95B +251% YoY (MarketBeat); TTM rev $13.18B +83%; fPE 6.6 vs trailing 47; 23 analysts Buy 均值 PT $2,218 ()
- Barron's/Yahoo: [Sandisk Just Had Its Worst Month Ever. Earnings Should Prove AI Demand Is Here to Stay.](https://finance.yahoo.com/quote/SNDK/)
- _Corroboration:_ 同日活样本：AMD -6.4% 与 SPCX -10.8% 均强数字被卖出；memory cluster 5d 同步走强 MU +24% SKHY +20% DRAM +22% WDC +18%

**Cross-assets.** SPY +0.03% · VIX 15.93 · TEN YEAR 4.62 · WTI 74.53

**Agent read.** 延续昨日(8/4)SNDK agent read 的核心担忧：'expectations elevated INTO tomorrow print, must beat a raised bar; fPE 6.8 vs trailing 49 implies EPS 7x growth'。今日新增两个同构活样本(AMD/SPCX)强化 sell-the-news 基准。收入端不是问题，支出端(毛利率指引+capex)是胜负手。SNDK 恢复位属性给它 AMD 没有的中期空间。研究详见 stocks/SNDK/research/2026-08-05-earnings-preview.md。纯跟踪无持仓。
 · [Snapshot](research/2026-08-05-earnings-preview.md)

---
### 2026-08-04 · +11.68% day · ▲ major
**Tags:** `tech_breakthrough`, `partnership_news`, `pt_change`, `memory_pricing`, `ai_demand`, `sector_rotation`, `earnings_pre_print`
**Confidence:** high

**Primary cause.** SNDK + SK Hynix jointly launched the HBF (High Bandwidth Flash) AI memory standard — a common memory architecture letting AI systems using different vendors' processors (NVDA/AMD/custom ASIC) interoperate. Wall Street hiked price targets across the board. The event re-classifies SNDK from 'NAND commodity cycle stock' to 'AI memory architecture participant', which carries far more valuation elasticity than a single-quarter number. Amplified by risk-on tape (S&P record high on US-Iran draft deal) and Q4 FY26 earnings due 8/5.

**Sources.**
- Yahoo: [SNDK, SKHY Stocks Gain After Launching New AI Memory Standard – Wall Street Hikes Price Targets](https://finance.yahoo.com/)
- Motley Fool: [Why Sandisk Stock Soared Today — Did Sandisk and SK Hynix just solve the HBM supply crisis?](https://www.fool.com/)
- Yahoo: [Sandisk Jumps 8%, Micron Gains 6%, SK Hynix Climbs 4% as Wall Street Hikes Price Targets on AI Memory Boom](https://finance.yahoo.com/)
- _Corroboration:_ Full memory complex moved together: MU +8.4%, SKHY ADS +7.8%, DRAM ETF +7.9%. SNDK's 1.4x beta vs MU confirms it is the highest-leverage AI-memory expression.
- _Data:_ Counterpoint Q2 DRAM share: Samsung reclaimed #1 at 39%, MU narrowed gap with SK Hynix — competitive backdrop for the SNDK+SKHY standards alliance. ()

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** Quality of this move rates 7/10. The catalyst is a genuine industry-standard event (real, structural, not a rumor) and it changes SNDK's valuation category rather than just its quarterly numbers — that is why SNDK (+11.7%) outran MU (+8.4%) by 1.4x. Two flaws: (a) volr only 0.76x — no volume confirmation, the move is short-covering plus sell-pressure exhaustion after July's -47% collapse; (b) expectations now elevated INTO tomorrow's 8/5 Q4 FY26 print, so the report must beat a raised bar. Forward PE 6.8 vs trailing 49.2 implies EPS must grow ~7x — that assumption is what tomorrow tests. Key structural note: SNDK is the best available thermometer for market confidence in AI memory demand (highest beta, 58x 52-week range), NOT a directional indicator for the sector. If SNDK drops hard post-print while MU holds, it is idiosyncratic; if both fall together, the AI-memory demand narrative is being falsified — a material negative read-through to MU's 9/23 scorecard on the 'MU is the next NVDA' claim.
 · Snapshot at `dashboard/2026-08-04.md`

---
### 2026-06-26 · -6.69% day · ▼ major
**Tags:** `sector_rotation`, `competitor_news`, `flow_event`
**Confidence:** high

**Primary cause.** SK Hynix 韩股盘前 -8.36% 收 ₩2,673,000 (vs ₩2,917,000) → 美股 memory cluster 联动 mean-reversion。触发新闻「Samsung, SK Hynix Slide 9% Before $646 Billion Investment Update」+「Micron, SanDisk, and Western Digital Fall 7% as Memory Rally Cools」。SNDK 作为「美国版 SK Hynix 替代品」最敏感传感器，单日同步砸盘 — 但传导系数从 6/23 的 1.67x 缩小到今天的 0.96x，说明市场已学习。盘前 $2,230 → $2,137 低点 (-8.48%) → 开盘 $2,173 反弹 → 早盘 $2,178.79，vol 0.12 极低 = 流动性主导非 capitulation。MU -7.04%, DRAM ETF -7.08% 同向印证。同时 Mag-7 出现 reversal：AAPL +0.33% / MSFT +1.29% / META +0.17% 不跟跌 + Barron's「Apple/MSFT face bigger problems than memory prices」narrative 翻面。基本面（HBM3E/HBM4/Anthropic-MU/8/24 Q4 财报）无任何实质变化。

**Sources.**
- {"title": "Samsung, SK Hynix Slide 9% Before $646 Billion Investment Update", "url": "https://finance.yahoo.com/", "type": "news"}
- {"title": "Micron, SanDisk, and Western Digital Fall 7% as Memory Rally Cools", "url": "https://finance.yahoo.com/", "type": "news"}
- {"title": "Semiconductor stocks retreat over worries about memory costs", "url": "https://finance.yahoo.com/markets/article/semiconductor-stocks-retreat-over-worries-about-memory-costs-131508185.html", "type": "news"}
- {"title": "Apple, Sandisk, Marvell, and More Stocks That Explain Today's Market", "url": "https://barrons.com/", "type": "news"}
- {"title": "Apple, Microsoft Face Bigger Problems Than Micron's Memory Prices", "url": "https://barrons.com/", "type": "news"}

**Cross-assets.** SPY -0.92 · QQQ -1.77 · VIX 20.46 · 10Y 4.41 · MU -7.04 · 000660.KS -8.36 · DRAM -7.08 · NVDA -2.22 · TSM -3.36 · AAPL 0.33 · MSFT 1.29 · WTI -2.78

**Agent read.** Smoking gun: Hynix 韩股 -8.36% 隔夜 + Samsung/SK Hynix $646B 投资公告前置 de-risking。SNDK 作为美股 memory cluster 第二敏感标的 (vol 0.12 = 早盘流动性盘) 砸 -6.69%，但传导效率较 6/23 大幅下降 (1.67x → 0.96x)。盘前 W-bottom 形态在 $2,137 测试两次未破 = 第一道 confluence 支撑。Mag-7 出现反向 narrative reversal (AAPL/MSFT 反弹 + Barron's 头条「他们有比 memory 更大的问题」) — narrative 24h 内已三度翻面：(1) bull memory + bull terminal (6/25 早) → (2) bull memory + bear terminal (6/25 收) → (3) bear memory + bull terminal (6/26 早盘)。本质上是单日 +22% 后的 mean-reversion + cluster contagion 二次释放。基本面 anchor 未变：8/24 Q4 财报。**SNDK 缺 thesis.md** 是当前最大 gap — 4 天内成为 memory cluster 第二号噪音放大器，无 thesis-break 监控机制。建议本周建一份 thesis brief。下一观察窗口：(1) $2,137 是否守住；(2) 韩股 6/27 收盘走势；(3) 7/10 ADR 前是否还会有二次 cluster reset。


---
### 2026-06-23 · -14.01% day · ▼ extreme
**Tags:** `regulatory_negative`, `policy_korea`, `flow_event`, `sector_rotation`
**Confidence:** high

**Primary cause.** Korean FSS 总裁 Lee Chan-jin 公开'后悔'5月底批准 16 只 2x 杠杆单股 ETF (标的 Samsung/SK Hynix, AUM 4周翻三倍到 $9B+)，冷却警告反而引爆抛售。SanDisk 自身无公司层面催化 — Fool 明确指出两条传导: (1) 同类杠杆 ETF 担忧蔓延; (2) 之前作为'美国版 SK Hynix 替代品'被买入，今天反向解仓。SNDK 52 周累计 +4700%，今天 -14% 在此斜率前是 mean-reversion 而非趋势反转。

**Sources.**
- Motley Fool: [Why Sandisk Stock Suddenly Crashed Today](https://www.fool.com/investing/2026/06/23/why-sandisk-stock-suddenly-crashed-today/)
- CNN: [Wall Street is getting trampled by an AI sell-off. South Korean market plunges 10%](https://www.cnn.com/2026/06/23/business/stock-market-kospi-dow-nasdaq-ai)
- Axios: [AI bubble fears send tech stocks plunging](https://www.axios.com/2026/06/23/tech-stocks-ai-bubble)
- 247WallSt: [SanDisk Plunges 11%, Micron and Western Digital Slide 10% as Korean Market Crash Hits Memory Chips](https://247wallst.com/investing/2026/06/23/sandisk-plunges-11-micron-and-western-digital-slide-10-as-korean-market-crash-hits-memory-chips/)
- _Data:_ FSS Governor Lee Chan-jin 公开声明: 16 只 2x 杠杆 ETF 是 'high-risk products', AUM 4 周翻三倍到 $9B+. KOSPI 半导体板块 -10%, SK Hynix -7.56%, Samsung 005930.KS -12.43%. ()
- _Corroboration:_ MU -11.09% (vol 0.65), WDC -8.86% (vol 0.96), DRAM ETF -12.62% (vol 1.40). 同向但 SNDK 跌幅最大 = 杠杆/替代品最重。
- _Data:_ SNDK 52w +4700% ($40.10 → $2354 high)。今天 -14% / 30d 仍 +25.15%。vol_ratio 0.79 (低) — 散户/算法砸盘，无机构 capitulation。 ()

**Cross-assets.** SPY -0.97% · VIX 18.75 · TEN YEAR 4.49 · SKHYNIX -7.56% · SAMSUNG -12.43% · MU -11.09% · WDC -8.86% · DRAM ETF -12.62%

**Agent read.** Smoking gun: 韩国 FSS 监管警告 16 只 2x 杠杆 ETF (Samsung/SK Hynix 标的, AUM 4周翻三倍至 $9B+)。冷却警告反而引爆去杠杆抛售，KOSPI 半导体 -10%。SanDisk 是美股传导最严重的标的 — 既因 leverage ETF 担忧蔓延，也因前期被资金当作'美国版 SK Hynix 替代品'追涨。三层因果链清晰: 监管动作 → 韩股去杠杆 → 美股替代品/代理共振。这不是 stock-specific 也不是 AI-fundamentals-specific，而是 LEVERAGE-specific。类比 2020-09 SoftBank Nasdaq whale 反向案 和 2024-08 Yen carry unwind 的小型版。基本面（HBM3E NVIDIA 独占、HBM4 leadership、Anthropic-MU 协议）未受任何冲击。下一观察窗口: (1) FSS 是否对 16 只 ETF 进一步采取行动（强制赎回/限制申购）; (2) 韩国本土散户是否回补; (3) 卖方主流叙事是否从 'rotation' 转向 'bubble pop'。
 · Snapshot at `dashboard/attribution-2026-06-23.md`

---
