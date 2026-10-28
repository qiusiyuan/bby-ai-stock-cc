# DRAM attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-28 · +5.57% day · ▲ material
**Tags:** `sector_rotation`, `flow_event`, `earnings_print`
**Confidence:** high

**Primary cause.** **ETF 层 +5.57%, 低于韩国本线 (000660.KS +16.63% / 005930.KS +13.62%) 也低于两只美国纯内存成分 (SNDK +5.60%) 但高于 MU (+4.28%) —— 篮子含 WDC/MU/SNDK 等非纯 HBM 名字, 所以被稀释。** 驱动是 SK Hynix Q3 创纪录 + 「售罄至 2029」+「缺口到 2030」(完整内容见同日 000660.KS 条目)。||「Micron Climbs 4% as Bank of America Grows More Positive on Memory; Western Digital Rises 5%, SanDisk Gains 3%」、「AMD, Broadcom, and Micron stocks lead chip sector higher for third day in a row」、「Nasdaq Lags Despite Memory Chip Surge. Tech Earnings Can't Come Soon Enough.」||**最后一条标题是今天最准确的大盘描述: 内存大涨而纳指 (QQQ +0.38%) 几乎不动, 且 QQQ 仍在 MA50 下方 -0.15% 连续第三天。内存的修复没有外溢到指数层面。**||**量比 0.76x —— 连续第三份报告里 ETF 层量比在 0.7-1.2x 区间, 但今天必须加口径警告: 本记录写于 ET 14:43 (已走完约 73% 交易时段, 未含收盘集合竞价), 所有量比系统性偏低约 25-30%。全场盘中中位数 0.595x, 时段折算全日等效约 0.81x。因此今天不作「参与度半量」这类结论 —— 过去几份报告的「连续三天半量」判断如果同样基于盘中数据, 需在收盘后复核。** 今天唯一不受影响的量比结论是相对排序: SKHY 1.79x 与 GEV 1.77x 是全场唯二过 1.5x, 且两者都是今天出财报的标的。||30d 仍 **-3.61%** / MA50 下方 -5.12% / 距 52w 高 -34.43% / 距 52w 低 +104.02%。**组内四只 (本线 -8.72% / DRAM -5.12% / SKHY -3.03% / MU -1.19%) 在 +12~+17% 的单日涨幅之后全部仍在 MA50 下方 —— 今天修复的幅度不足以改变趋势结构。**||注: `stocks/DRAM/triggers.yaml` 无 thesis_break_price (ETF, 按 tracker 流程管理)。**接下来 56 天内存组零个公司级硬日历** (MU 12/23, SKHY 2027-01-27)。

**Sources.**
- 24/7 Wall St.: Micron Climbs 4% as Bank of America Grows More Positive on Memory; Western Digital Rises 5%, SanDisk Gains 3%
- Barron's: Nasdaq Lags Despite Memory Chip Surge. Tech Earnings Can't Come Soon Enough.
- (aggregated): AMD, Broadcom, and Micron stocks lead chip sector higher for third day in a row

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-10-27 · +4.41% day · ▲ material
**Tags:** `sector_rotation`, `flow_event`, `earnings_pre_print`
**Confidence:** high

**Primary cause.** **ETF 层涨幅 (+4.41%) 高于其任一美国成分股 (MU +2.77% / SKHY +1.92% / SNDK +3.92%), 说明涨幅主要来自韩国本线权重 (000660.KS +5.18% / 005930.KS +4.23%)。**||驱动是补 10/26 美股的 Anthropic S-1 反弹 (Reuters: 「Global chip, AI stocks surge on Anthropic IPO cheer」) + BofA 转多内存 + SK Hynix 3Q26 创纪录 (韩国时间 10/28, 美股 10/27 收盘后)。另: 「Money Surges into APAC ETFs as Investors Diversify」。||**量比 1.21x —— 连续第二份报告里 ETF 层的成交量高于其美国成分股 (MU 0.87x / SNDK 0.82x), 这是「买板块不买个股」的形态。** 对照 SKHY ADS 1.24x: 换手集中在**美国可交易的载体** (ADS + ETF) 而非韩国本线 (0.92x / 0.82x), 与「被动跟随前夜美股」一致。||30d -8.80% / MA50 下方 -10.47% / 距 52w 高 -37.96% / 距 52w 低 +93.0%。||注: `stocks/DRAM/triggers.yaml` 无 thesis_break_price (ETF, 按 tracker 流程管理)。其预设触发条件之一「DRAM 5 日跌超 15%」在 10/14-10/22 期间曾接近, 现 5d 为 +5.74%, 已远离。

**Sources.**
- Reuters: Global chip, AI stocks surge on Anthropic IPO cheer
- 24/7 Wall St.: Micron Climbs 4% as Bank of America Grows More Positive on Memory; Western Digital Rises 5%, SanDisk Gains 3%
- ETF Trends: Money Surges into APAC ETFs as Investors Diversify

**Cross-assets.** SPY +0.57% · VIX 17.52 · TEN YEAR 4.993 · FIVE YEAR 4.84 · THIRTY YEAR 5.305 · WTI 100.66 · BRENT 110.07 · DXY 102.344 · GOLD 4075.9 · SILVER 54.45 · BTC 80650.73

**Agent read.** ETF 的量比连续两天高于美国成分股 = 板块层面的被动买入, 而非个股选择。这个形态配合「换手集中在美国可交易载体」的观察, 支持 SKHY 溢价的结构性解释 (美国资金只能通过 ADS/ETF 表达对韩国内存的看法)。
 · Snapshot at `dashboard/2026-10-27.md`

---
### 2026-10-22 · -6.97% day · ▼ material
**Tags:** `memory_pricing`, `flow_event`, `competitor_news`, `sector_rotation`
**Confidence:** high

**Primary cause.** 内存组 ETF，组内 beta。**本组唯一量比过 1.0x 的成员 (1.13x) —— 说明仍有被动卖盘在出，而个股 (MU 0.79 / SKHY 0.73 / SNDK 0.90) 都是半量。这个分布形状意味着今天内存组的卖压更多来自 ETF 层面的赎回，而非个股层面的主动减仓。**||**成本侧证据链今天拿到第三层 (客户官方指引) 与第四层 (设备厂官方口径):** (1) 10/15 Counterpoint — Q3 全球手机出货同比 -20%, 2012 年来最弱 Q3, 直接归因 DRAM/NAND 涨价; (2) 10/15 巴克莱下调 Dell/HPE — 内存成本过账虚增服务器营收不带毛利; (3) **10/22 NOK 下调自由现金流指引 + CEO 称供应挤压是「结构性成本上升，不只是短缺」并计划因成本通胀涨价 (客户自己的账, 最硬)**; (4) **10/22 Lam Research -9%, 点名「供应链约束」限制指引; AMAT -6% / ASML -4%**。Lam 这条让成本故事自我强化: 设备交不出 → 产能扩不上 → 内存价格维持高位更久 → 下游需求破坏继续。**今天市场在「价格 vs 数量」里明确选了数量。**||**CXMT 第 31 天 (自 9/21 首现)，六项技术细节仍然一项未动** —— ❌制程节点 ❌位密度 ❌DDR5/HBM 指认 ❌量产时间表 ❌产能数字 ❌第三方良率验证。而 DRAM ETF 自 9/22 峰值已打掉 **-28.1%**; 距 52w 高 $81.34 为 **-43.77%**; vs MA50 $56.82 偏离 **-19.5%**。||**一个零技术细节、已持续 31 天的供给预期，和一个已在账上的需求事实，现在共同支撑同一段跌幅。10/26 SK Hynix 本线财报是前者的免费裁决日。**||**宏观共因已被排除为跌因**: 2Y -17.3bp / 10Y -18.1bp 平行下行、TLT +2.03%、债市撤回加息押注 — 折现率给了近 20bp 顺风而权益仍跌, 跌幅必须由风险溢价全额解释。**参与度限定: 全场量比中位数 0.79x, 仅 10/35 过 1.0x、2/35 过 1.5x (NOK 1.83 / GEV 1.75, 两只都有具名新闻)。方向可信, 幅度不可信。**

**Sources.**
- Yahoo Finance: Chip stocks fall as equipment maker Lam Research cites 'supply chain constraints'
- TIKR/Stocktwits: Nokia cuts cash flow view; CEO calls supply squeeze a structural cost increase
- {"type": "computed", "title": "\u672c\u7ec4\u552f\u4e00\u91cf\u6bd4\u8fc7 1.0x (1.13x) vs \u4e2a\u80a1 0.73-0.90x \u2014 ETF \u5c42\u9762\u8d4e\u56de\u800c\u975e\u4e2a\u80a1\u51cf\u4ed3", "publisher": "workspace"}
- {"type": "computed", "title": "CXMT \u7b2c 31 \u5929\u516d\u9879\u6280\u672f\u7ec6\u8282\u5168\u90e8\u4ecd\u4e3a \u274c; ETF \u81ea 9/22 \u5cf0\u503c -28.1%", "publisher": "workspace"}

**Cross-assets.** SPY -1.44% · VIX 19.37 · TEN YEAR 4.957 · TWO YEAR 4.65 · WTI 99.19 · DXY 101.6 · GOLD 4055.4 · BTC 81063

**Agent read.** ETF 是本组唯一放量的成员, 形状指向被动赎回。CXMT 预期进入第 31 天仍零技术细节, 而成本/需求侧已有四层证据 — 10/26 的本线财报会把两者分开。
 · Snapshot at `dashboard/2026-10-22.md`

---
### 2026-10-15 · -3.18% day · ▼ material
**Tags:** `memory_pricing`, `flow_event`, `sector_rotation`, `competitor_news`
**Confidence:** high

**Primary cause.** **ETF 层面的主题级赎回: 量比 1.55x 高于它最大的美国成分股 (MU 1.00x / SNDK 1.01x / SKHY 1.21x), 而跌幅 -3.18% 也高于 MU (-0.26%) 与 SKHY (-2.72%)。** ETF 同时跌得比成分股多**且**成交比成分股活跃, 是「有资金在整体撤出『内存』这个主题」的标准形态, 而不只是在调整个股权重。||**这是本 workspace 第四次记录同一个 flow_event 形态** (9/10、9/15 各一次, 10/14 一次)。9/15 那条归因写得最清楚: 当日 ETF -0.18% / 5d -10.47%, 而 5d 跌幅「比它任何一个主要成分股都差 (MU 5d -7.79% / SKHY 5d -6.48%)」。今天同一形态在更大的量级上重现。||但今天和前三次有一个机制上的差别, 必须记下: **前三次的归因机制是「纯折现率通道」** (9/10 是八月 PPI +5.4% + WTI 破 $103 → 10Y 4.96%; 9/15 是 10Y 破 5.00% 为 2007 年 7 月以来最高; 两次当日公司级新闻全部为正却仍跌 5%, 所以归因只剩折现率)。**今天折现率是顺风 (长端 -10bp) 而 ETF 仍跌 3.18% —— 所以今天不是同一个机制, 是第一次由基本面坏消息驱动的主题赎回。**||**🔴 今天存储叙事从单侧变成双侧 —— 这是本轮下跌四天里最重要的性质变化.** 10/12-10/15 四天的全部跌幅建立在一个**供给侧预期**上: 中国 CXMT 把更密的 DRAM 设计对准服务器内存 → 未来供给增加 → 价格周期提前见顶。10/14 报告的核心批评是这个假设至今零技术细节 (❌无制程节点 ❌无位密度 ❌无 DDR5/HBM 指认 ❌无时间表 ❌无产能数字 ❌无第三方良率验证); 今天是第 4 天 / 自 9/21 首次出现算起是**第 25 天**, 这六项**仍然一项未动**。||今天新增的证据性质完全不同, 它从**需求侧**攻击同一个论点: **Counterpoint Research — 2026 年第三季度全球智能手机出货量同比 -20%, 是 2012 年以来最弱的第三季度, 直接归因于 DRAM 与 NAND 价格飙升推高整机成本。** 重要性在于论点类型变了: CXMT 是一个**预期** (未来可能有更多供给, 无法验证, 可以持续数季不被回答); 手机出货 -20% 是一个**已发生的事实** (涨价已经消灭了需求, 单位数据已在账上)。||内存多头论点的核心是「定价权」, 而定价权的边界条件就是需求弹性。手机是 DRAM/NAND 最大单一终端市场之一, -20% 的出货降幅 + 14 年来最弱 Q3 + 第三方研究机构直接归因于内存涨价 —— **这是本 workspace 记录以来第一次看到内存涨价的代价以单位需求的形式被量化。** 配合巴克莱下调 Dell/HPE 的理由 (内存成本过账虚增服务器营收, 不带毛利), 产业链里的分配机制也被点明: 内存涨价不是纯增量, 而是从下游转移。||**因此对存储组的态度需要修正**: 在今天之前合理的态度是「跌幅建立在一个无证据的供给预期上, 等 10/26 免费拿答案」; 今天之后 —— **跌幅里现在有一部分建立在一个有证据的需求事实上。即使 10/26 把 CXMT 完全否掉, 需求弹性这一侧的坏消息不会被同时否掉。**||PE 9.84x 是全书最低倍数之一, 距 52w 高 $81.34 已 **-40.3%**。**低倍数在今天没有提供任何保护** —— DRAM (9.84x) 跌 3.18% 重于 TSLA (340x) 的 1.84%, 这是今天横截面否证的一部分。||**宏观共因 (今天的共因只有一个, 但它的形状是反直觉的).** 九月 PPI (Producer Price Index, 生产者物价指数 — BLS 每月发布, 衡量生产者卖出价格, 通常领先 CPI 一到两个季度) 环比 **+1.3%** (8月 +0.5% / 7月 +0.2%, 2022年3月 +1.7% 以来最大单月), 同比 **+6.3%** (2022年12月 +6.4% 以来最大年度涨幅); 核心 (除食品/能源/贸易服务) 环比 +0.5% / 同比 +5.0%; 商品 +2.6% 其中**能源 +10.8% / 汽油 +20.3%**。接在 10/14 CPI 同比 3.7% (共识 3.6%) 之后, 是连续两天的下游+上游双向确认。零售销售同时跳升、失业申领保持稳健 —— 三项数据同向意味着经济不弱而价格在涨, 这是加息路径最不利的组合。||**❗但长端的反应方向和教科书相反, 本条必须作为限定随附**: 3M (^IRX) 4.088% **仅 +0.3bp**, 5Y 4.903% **-8.9bp**, 10Y 5.089% **-10.1bp**, 30Y 5.424% **-10.1bp**, TLT +1.52% (5d +2.85%)。**前端一动不动而 5年到30年平行下行 10bp —— 这个形状不可能是 Fed 政策定价 (政策定价必先动前端), 只能是对久期本身的避险需求。** 当天新闻口径直接说出了这件事 ('Tech slumps as AI financing worries grow, investors flock to bonds')。||**⭐ 方法论升级 (改写 10/05、10/07、10/08、10/14 四份报告的同一条限定)**: 那四天记录的都是「长端**不动**」—— 即对利空/利多都无响应, 属于零信息的否证, 只能说明「没有反证」。**今天长端第一次动了, 而且方向是下行**, 也就是折现率给了权益一个**顺风**, 权益却继续跌。结论因此从「无反证」升级为「有正面证据」: 折现率通道今天是负贡献 (利好), 跌幅必须由风险溢价**全额**解释。||**横截面否证「加息打击高倍数/长久期股」—— 本周第三次**: PE 从 SKHY 9.74x / DRAM 9.84x / MU 12.79x 一直到 AMD 148.2x / PLTR 172.0x / TSLA 340.0x, 跨 35 倍; 跌幅区间只有 -0.26% ~ -4.14% 且与倍数**无关** (TSLA 340x 跌 1.84% 却轻于 DRAM 9.8x 的 3.18%)。真正把跌幅排序出来的是「是否在 AI 供给/融资链上」。||**参与度限定 (与 10/14 相反)**: 38 只标的量比中位数 **0.755x**, 仅 11 只过 1.0x, 4 只过 1.5x。10/14 为中位数 1.02x / 17-of-32, 当时记为「本轮下跌序列第一个全参与度日」—— **一天后没有延续, 那是一个点不是趋势**。且今天放量的位置极度集中在韩国两条本线 (2.06x / 1.96x) + DRAM ETF (1.55x) + TSM (1.52x 财报日), 美国大型科技几乎无成交 (MSFT 0.54x / AMZN 0.54x / TSLA 0.47x / GOOG 0.39x / META 0.36x)。**这是对一个特定位置的定向抛售, 不是广泛降风险。**||**指数层面第一次方向分离**: QQQ -0.61% (跌破 MA50 $726.34) vs Dow +0.86% vs IWM +0.74%, 裂口 1.47pp。前四个下跌日 (10/07、10/08、10/13、10/14) 都是全指数同向。30d 口径 QQQ +2.26% vs IWM -6.77% 裂口从 10/14 的 12.4pp 收窄到 9.0pp, **且是用纳指跌、小盘涨的方式收窄 —— 轮动而非普跌的硬证据**。落点新闻一致: Moderna +6% (资金流入医疗) / Walmart +3% (德银上调) / Opendoor-Zillow +7% (长端回落直接利好住房)。VIX 16.88 (+0.06%) 几乎零反应, 第五次确认「不是系统性恐慌」。

**Sources.**
- {"type": "cross_stock", "title": "ETF \u91cf\u6bd4 1.55x > \u6210\u5206\u80a1 (MU 1.00x / SNDK 1.01x / SKHY 1.21x), \u8dcc\u5e45 -3.18% > MU -0.26% / SKHY -2.72% \u2014 \u4e3b\u9898\u7ea7\u8d4e\u56de\u5f62\u6001", "publisher": "workspace"}
- Counterpoint Research via American News Group: A 20% Drop in Smartphone Shipments Shows Who Wins When Memory Gets Expensive (Counterpoint Q3 -20% YoY)
- Barclays via Yahoo: Dell Falls 8%, Hewlett Packard Enterprise Drops 4% as Barclays Cuts Both to Hold — 理由是内存成本虚增服务器营收
- {"type": "cross_stock", "title": "\u5386\u53f2\u540c\u5f62\u6001: 9/10 DRAM -4.9% / 9/15 5d -10.47% \u2014 \u4e24\u6b21\u5747\u4e3a\u7eaf\u6298\u73b0\u7387\u901a\u9053, \u4eca\u5929\u6298\u73b0\u7387\u53cd\u5411 (\u957f\u7aef -10bp) \u5374\u4ecd\u8dcc = \u673a\u5236\u4e0d\u540c", "publisher": "workspace"}

**Cross-assets.** SPY +0.09% · VIX 16.88 · TEN YEAR 5.089 · WTI 96.58 · DXY 102.101 · GOLD 4168.2 · BTC 82171

**Agent read.** 第四次记录 ETF 跌幅超成分股的主题赎回形态, 但第一次是在折现率顺风的日子里发生 — 前三次归因为纯折现率通道, 今天必须归因为基本面 (需求破坏硬数据 + OEM 营收质量被质疑)。机制换了。


---
### 2026-10-14 · -5.11% day · ▼ major
**Tags:** `memory_pricing`, `competitor_news`, `macro_inflation`, `sector_rotation`, `flow_event`
**Confidence:** high

**Primary cause.** **ETF 是整个 CXMT 事件最干净的读数 — 它不含公司级噪音 (无爆炸、无 CEO 言论、无资产出售), 5d -16.45% 是纯板块定价。** 量比 1.30x, 在全场中位数 1.02x 之上, 属真实成交。跌破 MA50 $57.31 (低 12.5%)。**关键内部结构: ETF 今日跌幅 -5.11% 超过最大成分股 MU 的 -4.10% → 跌得更多的是尾部成分。** 这与 9/21 的观察符号相反 — 那天记的是「ETF 跑赢大成分股 (MU +2.77% / SKHY +0.73%), 数学上意味着涨的是尾部成分…这是周期后段的典型特征: 资金从质量最高的名字向下扩散到二线…是『这轮涨势质量在下降』的实证」。**现在是 ETF 跑输大成分, 即尾部先崩 — 这是周期恐慌的正常顺序, 与 9/21 的「尾部先涨」构成一个完整的周期内部轮动闭环。** 9/21 设的第二个解锁点原话是「DRAM ETF 相对 MU/SKHY 的持续强弱 (ETF 继续跑赢大成分 = 质量继续下降)」— 今天该指标反转, 按原判据应读为质量下降阶段结束、进入去杠杆阶段。|| CXMT 事件完整叙事 (三个交易日的同一事件): 10/12 CXMT 披露「更密的芯片设计」进展 (MU -4% / SK Hynix -4% / WDC -2%) → 10/13 首尔第五个下跌交易日 (MU -5% / SNDK -4% / SK Hynix -6% / WDC -7% / Seagate -7%) → 10/14 CXMT 把该设计**对准服务器内存 (市场最高毛利段)**。**与 10/07、10/08 两次下跌在性质上完全不同**: 那两次归因都反复确认需求侧无恙 (Samsung 创纪录业绩 / TSMC 九月营收超目标 / MU FQ4 营收 $542.29亿 +379.3% YoY、非GAAP毛利率 87%、FQ1 指引 $615亿), 跌的是折现率与风险偏好。**今天的因在供给侧 — 它直接攻击「供给纪律 + 寡头定价」这个所有存储论点共同的前提。需求再好, 若有第四个玩家在服务器内存上压价, 定价权就不在三家手里。这是结构性变量而非久期变量。** **⭐ 最重要的发现 — 同一类消息三周前让板块涨 3.30%**: 9/21 的归因已记录「中国 CXMT 宣布已实现先进 DRAM 量产, 直接点名挑战三星/SK Hynix/Micron」, 那天 DRAM ETF **+3.30%**、Samsung **+4.98%**, 原话是「今天的实质坏消息被涨势吞掉了」。9/21 当时就设好了判别问题与解锁条件, **今天两个都仍未被满足**, 但市场已为它打掉 15-20%。9/21 原文: 「要把声明和能力分开: 『先进 DRAM』不等于 HBM — HBM 需要先进封装 (TSV 堆叠、混合键合) + 良率 + 客户认证周期 (NVIDIA 认证通常 12-18 个月)。**CXMT 若只在标准 DDR5 上量产, 冲击的是商品 DRAM 价格而非 HBM 溢价。**」解锁点之三: 「**CXMT 的第三方良率验证 (声明免费, 客户 BOM 是硬证据)**」。**今天的报道里: ❌无制程节点 ❌无位密度 ❌无 DDR5/HBM 明确指认 ❌无量产时间表 ❌无产能数字。** 唯一可核实的 CXMT 数据点是 A 股上市首日 +465% 与一笔 $85亿 募资。报道框定的 gating factor 与 9/21 框架一致 — **hyperscaler 认证才是真正的闸门**。**两种读法都站得住, 必须都写**: (A) 市场在为「认证迟早会过」做前瞻定价 — 周期股转折常先于硬数据 6-12 个月; (B) 市场在为一条技术细节不明的声明打掉三家公司 15-20%, 正是 9/21 判断「声明免费」的那类事件 (IBD 当日标题「China's Competitive Threat To Micron Called 'Paper Tiger'」支持这一侧, ⚠️但该文正文在 investors.com 付费墙后, **分析师姓名、机构、技术论证、目标价均未能核实**, 仅作为「存在反方声音」记录, 不作为论据)。**今天的数据不足以裁决 (A) 与 (B)。但关键不对称: (B) 有免费到手的裁决日期, (A) 没有 — 10/26 SK Hynix 财报里, 一个 HBM 份额第一的公司不可能不被问到 CXMT。** **需求侧反方硬证据三条**: MU 9/30 电话会 CEO Sanjay Mehrotra「我们看到 27 年和 28 年的行业紧张程度高于 26 年」+ **2027 年产出 >75% 已通过 26 份战略客户协议锁定, 含 take-or-pay 条款** (最强的一条 — 价格与量在合约里已固定, CXMT 2027 压价无法立刻传导到已签的那 75%); SK Hynix Q2 FY26 初步营收 ₩79.32万亿 (+256.8% YoY)、营业利润 ₩60.54万亿; WDC CEO Irving Tan「超大规模数据中心数据约 80% 在硬盘上」(解释 WDC 跌幅小于 SKHY)。⚠️ 关键限定: **MU 9/30 电话会完全没有提到 CXMT**, 所以「take-or-pay 锁定 75%」不是针对 CXMT 的回应, 是这条消息之前就存在的事实 — 削弱短期影响, 对 2029 年及以后无约束力。**横截面关键证据: 跌幅排序与 HBM 份额排序一致 (SK Hynix 本线 5d -19.97% > MU 5d -15.98% > Samsung 5d -14.71%)。纯 beta 不会按份额排序。** 9/21 曾记「CXMT 消息对份额领先者威胁更大, SK Hynix 在 HBM 是第一」— 今天的排序与此一致。限定: 份额排序同时也是久期/估值排序的近似, 两者无法完全分离。|| 宏观共因 (三个独立的因, 不可压成一个): **(1) 九月 CPI**: 同比 +3.7% (共识 3.6%)、环比 **+0.6% 为过去一年最高**。CPI = Consumer Price Index, BLS 每月发布的美国最主要通胀指标。环比年化约 7.4%, 远高于 Fed 2% 目标。timeline 在今天之前已记 Oxford Economics 的提示 — 九月调查窗口内柴油 +60 美分/加仑、汽油 +20 美分, 油价冲击会进入这份读数, 所以这个数字是可预告的。它接在 9/17 FOMC 转鹰 + 9 月纪要 (10/07 公布) 指向今年再加一次息 (市场当时只给 19%) 之上, 是纪要后第一个硬数据且站在纪要一边。**(2) ❗长端拒绝配合 — 本条必须作为限定随附**: CPI 超预期而 10Y -2.7bp / 30Y -3.8bp / TLT +0.66%。媒体口径写的是 'rate-hike jitters'、'rising bond yields', 债市当天的实际方向与之相反。所以今天的跌**不能用「当天利率上行」解释** — 实现通道是风险溢价 (VIX +10.48%) 与叙事, 不是折现率。这是本月第四次长端对本应推高它的消息不配合 (10/01 失败突破 / 10/02 非农利多无响应 / 10/08 诱因缓解不修复 / 今天 CPI 超预期不涨)。**(3) 横截面否证「加息打击高倍数股」的单一叙事**: 倍数最高的 TSLA (fwd PE 168x) 跌 2.15%, 低于倍数中等的MRVL (33.7x) -8.73%、SNOW (111x) -6.34%、GEV (37x) -6.20%。跌幅与 **30d 涨幅**的相关性明显优于与倍数的相关性(MRVL 30d +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小跌幅)。**今天卖的是一个月里的涨幅, 不是久期。** **⭐ 方法论变化 (改写前三份报告的限定)**: 10/05、10/07、10/08 三份归因都写了同一句「半量里的下跌属『没有买盘』而非『出现卖盘』, 方向可信幅度不可信」。**今天不成立**: 量比中位数 1.02x (10/08 为 0.48x / 10/07 0.79x / 10/05 0.49x), 17/32 过 1.0x (10/08 为 3/34), 放量集中在跌最多的标的 (GEV 1.65x / QQQ 1.53x / TSM 1.45x / KOID 1.39x / MRVL 1.31x / DRAM 1.30x)。**这是这轮下跌序列里第一个全参与度的下跌日 — 幅度本身开始带信息。** 反方限定仍要记: 跌最惨的 MRVL 量比只有 1.31x、MU 只有 1.04x, 「放量」是全场性的而非个别标的清仓。

**Sources.**
- 247wallst via yfinance: SK Hynix Sinks 5% as China's CXMT Aims at Server Memory; Western Digital Drops 4%, Micron Falls 3%
- 247wallst via yfinance (10/12): Memory Stocks Slide as China's CXMT Flags Denser Chip Design: Micron and SK Hynix Fall 4%
- via yfinance DRAM news (10/13): Memory Stocks Extend Slide Following News of Design Breakthrough in China
- Investor's Business Daily (Patrick Seitz) — 正文付费墙, 分析师身份未核实: China's Competitive Threat To Micron Called 'Paper Tiger'
- via yfinance DRAM news: China Spooked Memory Stocks. Investors Picked Their Losers.
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- {"type": "attribution", "title": "2026-09-21 DRAM +3.30% \u2014 \u540c\u4e00\u7c7b CXMT \u6d88\u606f\u88ab\u6da8\u52bf\u541e\u6389, \u5e76\u8bbe\u4e0b DDR5-vs-HBM \u5224\u522b\u95ee\u9898\u4e0e\u7b2c\u4e09\u65b9\u826f\u7387\u9a8c\u8bc1\u89e3\u9501\u70b9", "publisher": "stocks/DRAM/attributions.md"}
- {"type": "research", "title": "SKHY ADS premium structure \u2014 90d lockup analysis (\u590d\u6838\u7ebf: \u6ea2\u4ef7 <+10%)", "publisher": "stocks/SKHY/research/2026-07-31-ads-premium-structure.md"}
- 247wallst via yfinance (CPI 3.7% YoY vs 3.6% 共识; MoM +0.6% 年内最高): Trump Media and Rumble Decline 5% as September Inflation Runs Above Forecasts; Reddit Slides 2%
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- IBD via yfinance: Stock Market Today: Nasdaq Dives On Rate Hike Jitters, AI Woes; Taiwan Semi Earnings On Deck
- Yahoo Finance video (Baird 策略师 Ted Mortonson): CoreWeave, Intel, Micron, & other tech stocks are plummeting. Here's why.

**Cross-assets.** SPY -1.08% · QQQ -1.97% · IWM -1.93% · DIA -0.11% · VIX 16.87 (+10.48%) · TEN YEAR 5.190% (-2.7bp) · THIRTY YEAR 5.525% (-3.8bp) · TLT +0.66% · WTI +1.16% · BRENT $106.06 (30d +12.05%) · GOLD -1.23% · SILVER -5.81% · DXY 102.530 (+0.34%) · BTC -1.81% · ETH -3.40% · BREADTH 32 只中 26 跌 / 6 涨 (含 2 只反向) · VOLUME MEDIAN 量比中位数 1.02x · 17/32 过 1.0x (10/08 为 0.48x · 3/34)

**Agent read.** ETF 跌幅超过第一大成分股这个事实, 比 -5.11% 本身信息量大。它把 9/21 建立的「ETF vs 大成分」监测指标走完了一个完整周期: 9/21 尾部先涨 (质量下降) → 10/14 尾部先崩 (去杠杆)。该指标有效, 应继续监测。


---
### 2026-10-08 · -5.32% day · ▼ material
**Tags:** `memory_pricing`, `sector_rotation`, `flow_event`, `macro_rates`
**Confidence:** high

**Primary cause.** **ETF 的 30d +0.76% 是今天存储组最值得读的一个数字。** 组内个股 30d 全为正 (MU +11.16% / SKHY +6.47% / SNDK +6.38% / Samsung +1.95%), 篮子却几乎归零 → 说明 ETF 里权重最大的成分不在这四只里, 或组内非持仓成分 (Western Digital / Seagate / 二线 DRAM 模组厂) 整月为负。**「存储周期」作为板块主题在过去 30 天并没有赚钱; 赚钱的是四只被单独挑出来的名字。** 这是对「买板块就行」思路的直接反驳 — 组内按质量分化比方向判断更重要, 也意味着不应用板块 ETF 表达存储观点。今天 -5.32% / 量比 0.75x, 随组同向无独立驱动。 || 宏观共因 (已按盘中时序校正, 勿用收盘涨跌读因果): **触发是地缘** — 美国据报考虑扩大对伊朗打击, 叠加一艘油轮遇袭。当日标题: 'Oil surges, stocks sink as US reportedly eyes new Iran strikes' / 'U.S. Stocks Slip, Oil Rises on Fresh Tanker Attack' / 'Dow Tumbles, Oil Surges, and Yields Rise to New 24-Year Highs as Trump Considers Ramping Up Iran Attacks' / 'Nasdaq Slumps On War Worries'。盘中路径: WTI 开 89.86 → 冲 **93.08** → 收 90.97; 10Y 盘前 **5.331** → 收 5.239; 30Y 开 5.695 (24 年高位区) → 收 5.615; QQQ 开 754.29 → 高 756.93 → 收 **745.35** (贴当日低 744.39)。**关键: 两个诱因 (油/长端) 当天都缓解了, 权益却收在当日低点附近 —— 纯 beta 事件应在诱因缓解时修复, 今天没有。** 只看收盘 (10Y -2.5bp / 30Y -4.4bp / TLT +0.77%) 会误读成「利率转松而久期资产崩盘」; 利率今天是上午推手、下午缓解项, 不是反常项。对照 10/01 (长端失败突破日 SKHY +5.08% / GEV +3.89% / MU +3.03% 全线反打): 同样的利率先冲后落路径, 那天权益修复了, 今天没有。**差异在「不修复」, 不在利率方向。** **第二段 (不修复) 的 AI 侧候选解释**: Broadcom 为 OpenAI 芯片安排 >$500亿 融资 (Apollo/Blackstone 参与), SPCX $400亿, Oracle 同期发债, 三家抢同一批买家; 媒体口径从 'war worries' 转为 'growing AI caution'; Michael Burry 称市场处于 'denial'。**但有一条有力反证, 不应略过: 同日 Anthropic 宣布计划在云与算力上支出 $5,180亿 — 量级极大的 AI capex 利多, 整组没涨。** → 可读成「信用担忧压过需求利多」, 也可读成「市场今天对任何 AI 消息都不反应」(情绪/风险偏好)。**诚实结论: 地缘是因, AI 谨慎是让它不修复的那一层, 但今天的数据不足以把信用与纯 beta+情绪分开。判别点在 10/15 TSM 指引与 10/28 capex 指引。** 跌幅分布事实 (排他性因果不成立): 开支方 GOOG -0.43%/AMZN -0.78%/META -0.87%/MSFT -0.95% vs 供给方 NVDA -2.30%/TSM -3.24%/AVGO -3.35%/INTC -5.53%/MRVL -5.89%, 两簇不重叠 — 但战争风险日里单纯 beta 差异足以产生同样分裂。**量能限定 (双向适用)**: 全书 34 只量比中位数仅 0.48x, 仅 3 只过 1.0x → 半量里的 5% 级下跌, 属「没有买盘」而非「出现卖盘」, 方向可信幅度不可信。**同日两个反向硬数据**: Samsung 发创纪录营收/利润初步业绩、TSMC 九月营收超目标 — 供应链两个独立层级同日确认需求, 价格全部反向 → 需求侧无恙。

**Sources.**
- via yfinance MU news: Micron Stock Drops—and Not Even Samsung's Record Profit Can Give It a Lift
- via yfinance AMD news: TSMC Gives AI Trade Upbeat Signal—AMD and Other Chip Stocks Fall Anyway
- via yfinance TSM news: Chip Foundry TSMC Beats September Sales Target
- via yfinance DRAM news: The Memory Trade Cools After Samsung's Preliminary Results Disappoint
- via yfinance DRAM news: Why Memory Stocks Are Sitting Out the Stock Market Rally

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-09-23 · -2.99% day · ▼ minor
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** DRAM ETF -2.99%（1w +11.55%，触发 5d≥10% 门槛），跟随整个 memory/HBM 复合体。无独立催化剂——作为 ETF 载体，其功能是确认『复合体整体同向』而非提供增量信号。同日 SKHY -3.21% / MU -2.23%，全部缩量（DRAM 0.28x 为最低）。驱动为 10Y 5.12%（2007 年以来最高）的折现率冲击。

**Sources.**
- : [10-year Treasury yield hits highest level since 2007 as market prices in another Fed rate hike](https://finance.yahoo.com/quote/%5ETNX/)

**Cross-assets.** SPY CHANGE -0.74% · VIX 15.34 · TEN YEAR 5.12 · WTI 91.41 · DXY 101.19 · QQQ CHANGE -1.01%

**Agent read.** trailing PE 13.1x，3mo -10.8%。作为 cluster 内独立信息量最低的成员，建议考虑移出 focus——它与 MU/SKHY 相关性极高，三者同占 focus 席位属冗余（已在当日报告中提出，待用户确认）。
 · Snapshot at `dashboard/2026-09-23.md`

---
### 2026-09-21 · +3.30% day · ▲ material
**Tags:** `memory_pricing`, `sector_rotation`, `competitor_news`, `macro_rates`
**Confidence:** medium

**Primary cause.** DRAM ETF +3.30% 到 $61.58, 5d +12.37%, 30d +21.70%。**关键观察: ETF 跑赢了它最大的两个成分股 (MU +2.77%、SKHY ADS +0.73%)。** 数学上这意味着涨的是尾部成分 — 小的、更边缘的存储标的涨得更多。这是周期后段的典型特征: 资金从质量最高的名字向下扩散到二线。不是立即卖出信号, 但是「这轮涨势质量在下降」的实证。板块内部分化更值得注意: **三星 (005930.KS) +4.98% vs SK Hynix 韩股 (000660.KS) +0.59% — 同一个韩国交易时段, 4.4 个百分点分化。** 可能解释: (a) 三星 HBM 认证追赶预期 (三星一直是 HBM 竞赛落后方, 任何追赶迹象都是低基数修复); (b) 今天的 CXMT 消息对份额领先者威胁更大, SK Hynix 在 HBM 是第一; (c) 三星 fwd PE 3.89 是链内最便宜, 风险偏好回归时最便宜的先动。**今天的实质坏消息被涨势吞掉了: 中国 CXMT 宣布已实现先进 DRAM 量产, 直接点名挑战三星/SK Hynix/Micron。** 但要把声明和能力分开: 「先进 DRAM」不等于 HBM — HBM 需要先进封装 (TSV 堆叠、混合键合) + 良率 + 客户认证周期 (NVIDIA 认证通常 12-18 个月)。CXMT 若只在标准 DDR5 上量产, 冲击的是商品 DRAM 价格而非 HBM 溢价, 这正对应另一条头条「How Much Of Micron Revenue Has A Price Ceiling?」的分界线。

**Sources.**
- (none)

**Cross-assets.** SPY +1.55% · QQQ +2.77% · SMH +4.02% · VIX 14.87 · TEN YEAR 4.963 · WTI -8.31% · INTC +12.14% · AMD +9.95% · META +11.34% · NVDA +2.30%

**Agent read.** 存储链今天是配角而非主角: SMH +4.02% 的一天里 MU 只 +2.77%、SKHY +0.73%。便宜的资产在风险偏好回归时不是最先被买的, 叙事性最强的才是 — 四个标的 fwd PE 是 3.89/3.98/5.57/6.57 全部单位数, 对照今天的 CPU 明星 INTC 59.06 / AMD 39.53。这是多头最有力的事实, 也是理解今天为什么没领涨的关键。但周期股在利润峰值时看起来永远最便宜, 单位数 fwd PE 正是周期顶部的典型读数。与 9/17 (4 天前) 的组合几乎相同 (memory_pricing + executive_comment + partnership_news + sector_rotation, 当时驱动是 Intel-SK Hynix 俄亥俄代工谈判) 但强度更弱 — 同一条叙事线第二次触发, 边际效应递减。三个解锁点: 9/30 MU 财报的 FY27 指引口吻; DRAM ETF 相对 MU/SKHY 的持续强弱 (ETF 继续跑赢大成分 = 质量继续下降); CXMT 的第三方良率验证 (声明免费, 客户 BOM 是硬证据)。
 · Snapshot at `dashboard/2026-09-21.md`

---
### 2026-09-17 · +4.57% day · ▲ material
**Tags:** `memory_pricing`, `executive_comment`, `partnership_news`, `sector_rotation`
**Confidence:** high

**Primary cause.** 板块 ETF 机械跟随存储链两条催化：**(1) Intel CEO 称存储价格已上涨超过 500%**（买方口径的涨价确认，可信度高于卖方喊涨价）；**(2) SK Hynix 与 Intel 就俄亥俄园区代工存储芯片重启谈判**。成分股全线上涨：MU +5.37% / SKHY +5.24% / SNDK +5.90% / Samsung (005930.KS) +1.61% / SK Hynix 韩本 +3.25%。ETF 加权后 +4.57%，天然跑输个股。宏观公因子：加息后 10Y 5.00%→4.951%，VIX -12.03% 到 15.58。**量比 0.46x 是今天全 watchlist 最低之一** — ETF 是被动跟随，不含独立信号。**另有一条需要存档的结构性风险新闻：'U.S. Export Controls on Chinese Memory Chips Could Make or Break CRAM in 2026'** — 对中国存储芯片的美国出口管制是这个 ETF 的双向风险源：管制收紧 = 非中国供应商（MU/SKHY/Samsung）受益；引发中国反制 = 全链受损。

**Sources.**
- MT Newswires/Yahoo: [Intel Jumps 8%, SK Hynix Climbs 5% as Ohio Memory Talks Reignite; Micron Rises 6%](https://finance.yahoo.com/)
- Yahoo: [The Memory Shortage Is Not Over: More Upside for Micron and Sandisk?](https://finance.yahoo.com/)
- Yahoo: [U.S. Export Controls on Chinese Memory Chips Could Make or Break CRAM in 2026](https://finance.yahoo.com/)
- _Corroboration:_ 成分股全涨：MU +5.37% (0.62x) / SKHY +5.24% (0.68x) / SNDK +5.90% (0.53x) / SK Hynix 韩本 +3.25% (0.75x) / Samsung +1.61% (0.58x)。**Samsung 明显跑输 — 新出现的链内分化**
- _Data:_ 量比 0.46x — 全 watchlist 最低。7/07 时 DRAM ETF 曾进入熊市（距 ATH >20%），现已 30d +7.57% 收复 ()

**Cross-assets.** SPY +1.11% · QQQ +1.63% · VIX 15.58 · TEN YEAR 4.951 · DXY 100.24 · WTI 101.85

**Agent read.** **ETF 层面的价值在于确认这是全行业价格因子而非个股故事** — 五个成分（含韩股）全涨，说明今天的驱动是共同的。但 **0.46x 量比（全 watchlist 最低）说明连被动资金都没进场**，这与个股的 0.53-0.68x 一起构成一个统一诊断：**无机构 conviction。** **7 月的完整循环值得回顾**：7/07 这个 ETF 因 Samsung Q2 预告 + SK Hynix $280 亿 ADS 融资引发的「周期顶 + 过度投资」恐慌而进入熊市（距 ATH >20%），今天 30d +7.57% 已收复。**那次恐慌的核心错误是用「一家公司融资扩产」推断「全行业供给过剩」** — 而今天 Intel CEO 的「涨价 500%」是对那个推断的直接反证。**新增的结构性观察：链内开始分层。** Samsung +1.61% 明显跑输 SK Hynix 韩本 +3.25%（同一市场同一天）。如果俄亥俄谈判推进，Samsung 在美国客户前的关税劣势被放大。**这意味着 ETF 的分散化在这个阶段可能是劣势** — 它同时持有受益方（SK Hynix）和相对受损方（Samsung）。**出口管制这条线是 ETF 特有的风险**：作为多国持仓的载体，它同时暴露于「管制收紧利好非中国供应商」和「中国反制打击全链」两个相反方向，个股无法完全复制这个双向敞口。无 thesis_break_price 设定（ETF），无触发风险。
 · Snapshot at `dashboard/2026-09-17.md`

---
### 2026-09-15 · -0.18% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`, `memory_pricing`, `flow_event`
**Confidence:** medium

**Primary cause.** 内存 ETF 今天几乎没动 (-0.18%), 但 **5 日 -10.47% 触发阈值, 且这个数字比它任何一个主要成分股都差 (MU 5d -7.79% / SKHY 5d -6.48%)。ETF 跌得比成分股更多, 通常意味着 ETF 层面的赎回压力 —— 有资金在整体撤出「内存」这个主题, 而不只是在调整个股权重。** 这与 9/10 归因里给 DRAM 打上 flow_event 标签一致, 是同一现象的延续。跌破 MA50 ($55.81), 距 52 周高 $81.34 已 -32.7%。归因机制: 无板块级公司利空, 纯折现率通道。10Y 今天破 5.00% (2007 年 7 月以来最高, 30d +6.7%), 明天 FOMC 定价加息。同日亚洲时段 SK Hynix 韩股 -6.73% / Samsung -4.24%, 美国时段 MU -0.18% / SKHY -1.20% —— 韩美之间 5.5pp 缺口尚未收敛, 意味着这个 ETF 明天也有补跌压力。**三次同模式对照 (机制完全一致): 8/18 DRAM -7.97% (10Y 停 52w 高 4.71% + WSJ 内存定价报道); 9/10 DRAM -4.9% (八月 PPI +5.4% + WTI 破 $103 → 10Y 4.96%); 今天 5d -10.47% (10Y 破 5.00% + WTI $106)。** 9/10 那次的归因写得最透: 当日公司级新闻全部为正 (JPMorgan 给内存 Overweight、顶级分析师称内存涨价「数年不缓解」、Samsung-OpenAI 合作扩展、ASML 扩大 High-NA 合作), 利好满仓仍跌 5% = 归因只剩折现率通道。今天是同一结论的第三次确认。

**Sources.**
- {"type": "cross_stock", "title": "MU 5d -7.79% / SKHY 5d -6.48% / SNDK 5d -12.74% / Samsung 5d -7.96% \u2014 \u4e94\u4e2a\u6807\u7684\u4e00\u5468\u5168\u90e8\u63a5\u8fd1\u6216\u8d85\u8fc7\u4e24\u4f4d\u6570\u4e0b\u8dcc", "publisher": "workspace", "url": ""}
- CNBC: 10-year Treasury yield hits highest level since 2007

**Cross-assets.** SPY -0.47% · VIX 17.46 · TEN YEAR 5.0 · WTI 105.95 · DXY 99.64 · GOLD 4342.5 · BTC 75913

**Agent read.** ETF 跌幅超过成分股 = 主题级赎回 (flow_event), 不只是个股调整。这是本 workspace 第三次记录同一折现率机制打击内存复合体。


---
### 2026-09-10 · -4.90% day · ▼ material
**Tags:** `macro_inflation`, `macro_rates`, `sector_rotation`, `memory_pricing`, `flow_event`
**Confidence:** high

**Primary cause.** 八月 PPI +5.4% YoY (预期 5.3%, 前值 4.8%; 核心 4.6% vs 前值 4.3%, 三个月最强) 叠加 WTI +8.16% 破 $103, 把 2Y 推高 13.3bp 至 4.56%、10Y 推高 11.7bp 至 4.96% —— 短端涨幅大于长端 = 市场定价 Fed 加息而非增长放缓。内存股 fwd PE 5-6 看似极便宜, 但这些倍数隐含的是周期高点盈利可维持多年, 折现率上升直接压缩『多年』的现值, 因此低 PE 不是保护。当日公司级新闻全部为正 (JPMorgan 给内存 Overweight、顶级分析师称内存涨价『数年不缓解』、Samsung-OpenAI 合作扩展到下一代芯片、MU 距 DRAM 第二仅差 1.6 个百分点、ASML 扩大 High-NA 合作), 唯一负面是 Intel 支持的初创进入内存市场 (对三年内格局无实质含义)。利好满仓仍跌 5% = 归因只剩折现率通道。 DRAM 作为 ETF 机械跟踪成分股, -4.90% 与 MU -4.90% 完全同幅度, 是『板块级而非个股级』最干净的证据 — ETF 与最大成分股同幅度意味着没有任何个股 alpha。成交量 0.71x 为复合体内第二低, 配置资金缺席。

**Sources.**
- 247wallst: Memory Stocks Slide as Rates and Oil Swamp JPMorgan's Overweight Call: SK Hynix Sinks 5%, Western Digital Drops 3%, Micron Slips
- Yahoo: Top Chip Analyst: Memory Prices Won't Ease 'For Years' and Even Apple Can't Dodge It
- Yahoo/MT Newswires: [Update: US Equity Indexes Fall as Hot Producer Prices, Soaring Crude Oil Boost Treasury Yields](https://finance.yahoo.com/economy/articles/us-equity-indexes-fall-hot-195114785.html)
- _Corroboration:_ 决定性反证: SK Hynix 韩国本土 000660.KS 仅 -0.16%、Samsung 005930.KS -0.19%, 而 SKHY ADS -5.20% — 同一公司同一天差 5.04 个百分点, 排除公司层面与 HBM 周期层面解释, 归因锁定美股时段折现率定价。
- _Corroboration:_ 历史对照 2026-08-31: 同类供给侧利好 (SK Hynix CEO 警告短缺到 2030 + Samsung 锁定 70% HBM 产能到 2031) 在 10Y 4.76% 时令复合体全线上涨 (SNDK +5.02/MU +2.53/SKHY +2.34/DRAM +1.78)。今日 10Y 4.944%, 同类利好换来 -4~5% — 18bp 之内供给侧利好的定价能力翻符号。7/31 SMH 预测的『供给侧例外条款』失效。
- _Corroboration:_ 成交量全部低于均量 (MU 0.82x / SKHY 0.95x / DRAM 0.71x / SNDK 0.62x) = 无机构 capitulation; 涨幅最大的 SNDK (30d +66.6%) 反而跌最少, 与『纯获利了结』形态矛盾 (对照 8/18 SNDK -8.9% 领跌)。

**Cross-assets.** SPY -0.58% · VIX 17.84 · TEN YEAR 4.944 · WTI 103.83

**Agent read.** 今日 -4.9% 在这个 ETF 的历史下杀序列里最温和 (6/23 -12.62%, 7/1 -9.9%, 7/15 -9.5%, 8/18 -8.0%), 且量能最低。低量下跌在此复合体历史上 (6/23 vol 0.65x, 7/15 vol 0.55x, 8/18) 每次都不是趋势终点; 8/18 同类折现率下杀两周内全部收复。
 · [Snapshot](snapshots/2026-09-10.md)

---
### 2026-09-08 · +3.32% day · ▲ material
**Tags:** `commodity_move`, `sector_rotation`, `flow_event`
**Confidence:** medium

**Primary cause.** 内存 ETF, 跟随成分股而非独立驱动。同源驱动: 内存合约价上行 + 『AI 把内存从手机端抽走』(详见同日 SKHY / SNDK 归因)。板块爆发日 9/4 (DRAM 单日 +6.6%)。**幅度居中值得记一笔: DRAM 5 日 +8.4% 明显小于 SNDK +14.6% / SKHY +13.7%, 大于 MU +5.8% — 说明篮子里含有非纯内存成分, 稀释了主题 beta。** 数据缺口: 具体合约价读数未取到, 置信度 medium。

**Sources.**
- _Corroboration:_ 成分股同日: SKHY +5.68% / SNDK +3.20% / MU -0.27% / Samsung -0.19%。ETF +3.32% 落在成分股中位数附近, 无独立 alpha。
- _Corroboration:_ 对手方 AAPL -1.38% (内存涨价的成本承受方) 为整个板块归因提供交叉验证。
- _Corroboration:_ 板块完全脱离宏观: 同日 10Y 触及 52 周新高 4.80%、SPY -0.48%、Dow -1.14%。

**Cross-assets.** SPY -0.48% · VIX 15.3 · TEN YEAR 4.8 · SKHY +5.68% · MU -0.27% · SNDK +3.20%

**Agent read.** 作为 ETF, DRAM 的价值在于它给出板块的『无个股噪声』读数。本周它说明的是: 板块整体 +8.4%, 而个股离散度极大 (SNDK +14.6% 到 MU +5.8%, Samsung +3.3%)。**离散度大 = 板块内部有真实的质量/时序分化, 不是一次无差别的流动性涨潮** — 这与纯 beta 行情不同, 也意味着选股在这个板块里当前是有回报的。用 ETF 表达这个主题会同时买到最强 (SNDK/SKHY) 和最弱 (Samsung) 的一环, 稀释后的收益低于板块领头。下一裁决点是 9/25-9/30 MU 财报, 那会给出合约价上行到底转化了多少盈利的第一个可验证数字。


---
### 2026-08-18 · -7.97% day · ▼ major
**Tags:** `sector_rotation`, `macro_rates`, `memory_pricing`
**Confidence:** medium

**Primary cause.** 内存复合体 US 名字单日重挫 (DRAM ETF −8.0 / MU −7.1 / SNDK −8.9 / SKHY −8.2)。三重驱动：(1) 一份 WSJ 内存定价报道令 SanDisk/Micron/WDC 集体下挫（报道全文需 WSJ 订阅，未能独立核实，但多家二手来源确认其为催化）；(2) 10Y 停 52w 高 (4.71%) 的久期资金外流；(3) 前 5 日抛物线上涨后的技术性获利回吐——DRAM/MU/SNDK 5d 仍分别 +9.2/+8.2/+28%。**关键分化证据：Samsung 005930.KS 今日仅 −2.2%（5d +16.7%），远小于 US 名字的 −7~−9%。若为全球内存需求/定价的基本面利空，韩国链应同步重挫；它没有——说明是 US-specific 催化 + 久期挤出 + 获利回吐，而非周期拐点。** 昨日 (8/17) SNDK +9.6%/+45%5d 的 extreme 归因已警告 memory cycle 进入 stage-2/3、追高即风险，今日反转是该警告的兑现。

**Sources.**
- secondary (WSJ 原文未核实): [WSJ Report Sends Memory Stocks Down. SanDisk Down 9%, Micron Down 7%, Western Digital Down 5%](https://finance.yahoo.com/)
- secondary: [Micron Falls 5%, SanDisk Sinks 6%, Western Digital Drops 7% as Higher Rates Test the Memory Boom](https://finance.yahoo.com/)
- _Corroboration:_ 分化证据：Samsung 005930.KS −2.2% vs US 名字 −7~−9%；SPY −0.52 大盘平稳，跌幅集中在半导体；全线缩量 (MU 0.53x / DRAM 0.68x)——板块间搬家非新钱恐慌抛售。

**Cross-assets.** SPY -0.52% · VIX 15.66 · TEN YEAR 4.71 · WTI 84.14

**Agent read.** 


---
### 2026-08-13 · n/a day · ▲ +5.33%
**Tags:** `memory_pricing`, `guidance_raise`, `sector_rotation`
**Confidence:** high

**Primary cause.** SanDisk Investor Day: multi-year financial model (revenue CAGR / margin / capital return) all raised. Market reads 'NAND supply side won't price-cut' -> read-through to HBM. Entire memory sector +5-15% same day.

**Sources.**
- Yahoo Finance: Sandisk Unveils Multi-Year Financial Model and Growth Strategy, Memory Stocks Soar
- Yahoo Finance: Memory Stocks Open Flat Then Soar: Micron Up 6%, SK Hynix 8%, SanDisk Up 15%
- Yahoo Finance: Lam Research, Applied Materials Rise After SanDisk Issues Bullish Financial Targets

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-08-12 · +8.15% day · ▲ major
**Tags:** `sector_rotation`, `ai_demand`, `memory_pricing`, `flow_event`
**Confidence:** medium

**Primary cause.** 存储 ETF 跟随复合体集体 re-rating。催化: CoreWeave/Supermicro Q2 强财报 -> AI infrastructure surge, 存储瓶颈联动。作为 ETF 直接反映整个 DRAM/HBM 板块情绪, MU/SKHY/DRAM 三名 +7~9% 同步。

**Sources.**
- Yahoo: AI infrastructure stocks surge after strong earnings from CoreWeave, Supermicro
- _Corroboration:_ 复合体联动: MU +7.3%, SKHY +8.6%, DRAM +8.2%

**Cross-assets.** SPY +0.37% · VIX 14.53 · TEN YEAR 4.68

**Agent read.** 板块 beta 的纯 ETF 表达。30d 仍 -16.4%, 本轮是超跌反弹 + AI 需求财报催化, 非趋势反转。


---
### 2026-08-06 · -3.66% day · ▼ material
**Tags:** `competitor_news`, `memory_pricing`, `ai_demand`, `sector_rotation`
**Confidence:** medium

**Primary cause.** DRAM ETF -3.66%，与 SKHY -4.59% 同步，同一驱动：NVIDIA Rubin Ultra 减 HBM 用量传闻（192GB vs Rubin 288GB，-33%）。ETF 层面反映整个内存板块对『HBM 单位需求叙事出现裂缝』的定价。属延续 6/24 以来下行通道（30d -26%），今日只是老趋势加了一条新叙事，非新趋势起点。成分内部分化：SKHY 领跌（HBM 敞口最大 + 低流通盘放大），MU 抗跌（估值已出清）。

**Sources.**
- Tech Times / MSN: [NVIDIA Rubin Ultra AI chip may deliver less HBM than Rubin (192GB vs 288GB, -33%)](https://www.msn.com/en-us/money)
- _Corroboration:_ SKHY -4.59% 同步；MU +0.04% 抗跌。ETF 无 vol 异常 (0.62x)，属情绪性回调非恐慌抛售

**Cross-assets.** SPY -0.15% · VIX 15.18 · TEN YEAR 4.67

**Agent read.** ETF 是 cluster 情绪温度计。今日 -3.66% 在低量能下（0.62x）发生，说明不是恐慌抛售而是买盘缩手 + 传闻驱动的情绪性回调。cluster 从 6/24 高点起持续下行，Rubin 传闻是第一次『需求侧』叙事介入。8/26 NVDA 财报是方向裁决点。参见同日 SKHY 归因的完整逻辑链。
 · Snapshot at `dashboard/2026-08-06.md`

---
### 2026-08-04 · +7.92% day · ▲ major
**Tags:** `sector_rotation`, `memory_pricing`, `ai_demand`, `tech_breakthrough`, `flow_event`
**Confidence:** medium

**Primary cause.** Mechanical follow-through of constituent moves after the SNDK + SK Hynix HBF (High Bandwidth Flash) AI memory standard launch and accompanying Wall Street price-target hikes across the memory group. Constituents: SNDK +11.7%, MU +8.4%, SKHY +7.8%. Broad risk-on tape (S&P record high on US-Iran draft deal, WTI -5.6%) amplified the beta.

**Sources.**
- Yahoo: [Semiconductor ETFs Surge up to 19% in Huge Rally as the AI Trade Ramps Back Up](https://finance.yahoo.com/)
- Yahoo: [MU, SNDK, DRAM Stocks Advance Premarket: Samsung Reclaims DRAM Lead, Micron Narrows Gap With SK Hynix](https://finance.yahoo.com/)
- _Corroboration:_ ETF tracked constituents faithfully: SNDK +11.7%, MU +8.4%, SKHY +7.8%, DRAM +7.9%. Whole complex bottomed 7/29 and has now rallied six sessions.

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** The ETF is the cleanest read on the memory complex as a whole, and its message is that this is a rebound, not a repair: +7.9% today only lifts 30-day performance from about -37% to -31.6%, still 11% below the 50MA ($61.89) and -32% from the 52-week high ($81.34). The complex bottomed on 7/29 and has rallied six sessions, with SNDK up roughly 41% off that low versus MU up 22% — the dispersion shows the market paying specifically for SNDK's HBF-driven re-classification rather than for a generic cycle bounce. volr 0.57x means no volume confirmation. Two verification points land tomorrow, 8/5: the SNDK Q4 FY26 print (first cash-flow test of the HBF narrative) and the Korean open for 000660.KS (tests whether the SKHY ADS premium reflects fundamentals or one-sided US sentiment). Both confirming would materially raise the credibility of the complex rebound and improve the outlook for MU's 9/23 scorecard; both disappointing would mark today as a one-day sentiment bounce with the 7/29 low still in play.
 · Snapshot at `dashboard/2026-08-04.md`

---
### 2026-07-01 · -9.90% day · ▼ major
**Tags:** `ai_demand`, `memory_pricing`, `sector_rotation`
**Confidence:** high

**Primary cause.** ETF mechanically tracks MU/SK Hynix/Samsung selloff triggered by OpenAI efficiency announcement. 8天内第二次-10%级别(6/23 -12.6%)。

**Sources.**
- _Corroboration:_ MU -9.3%, SK Hynix -3.4%, Samsung -5.8% — ETF 加权跟踪

**Cross-assets.** SPY +0.08% · MU -9.30% · SKHYNIX -3.40% · SAMSUNG -5.80%

**Agent read.** ETF机械跟踪。注意SK Hynix仅-3.4%远小于MU -9.3% — 如果efficiency thesis真的结构性削弱HBM需求，SKH作为50% HBM份额应跌更多。MU跌幅>SKH说明今天更多是US投机头寸获利了结。
 · Snapshot at `dashboard/2026-07-01.md`

---
### 2026-06-29 · +0.08% day · ▼ major
**Tags:** `memory_pricing`, `sector_rotation`, `thesis_debate`
**Confidence:** high

**Primary cause.** EOD update: DRAM 5d -10.88% (盘中曾 -12.37%, 尾盘 +0.08% 转涨)。USER 6/23 预测「跌穿 $62」仍然 FAIL;AGENT counter「守住 $62」PASS。底部支撑 $69-70 经过 4 次测试 (6/23-6/29) 已经站稳。今天 EOD MU $1145.28 +1.14% 也确认派发完毕;6/25 -> 6/29 (-5.6%) 是 6/24 baseline_print Q3 FY26 blowout 之后 sell-on-the-news 正常 mean-reversion,不是 thesis-break。Vol 1.27x = persistent 关注但非 capitulation。下个 truth event 9/25 Q4 FY26 评分日。

**Sources.**
- Yahoo: [Micron Slides. Are Memory-Chip Makers Illegally Price-Gouging Customers?](https://finance.yahoo.com/)
- Yahoo: [OpenAI's Wild Week: A Custom Chip, 40% of the World's DRAM, and a $500 Million Bet](https://finance.yahoo.com/)
- Yahoo: [Micron Stock: Let's Talk About Those Long-Term Contracts](https://finance.yahoo.com/)

**Cross-assets.** SPY PCT +1.65% · QQQ PCT +2.49% · MU PCT +1.14% · MRVL PCT +4.12% · VOLUME RATIO 1D 1.27

**Agent read.** 
 · Snapshot at `dashboard/2026-06-29.md`

---
### 2026-06-23#agent-counter-mu-dram · n/a day · ▼ minor
**Tags:** `prediction_recorded`, `thesis_debate`
**Confidence:** medium

**Primary cause.** AGENT COUNTER-PREDICTION (6/23 record): DRAM 在 6/24-6/27 窗口最低不破 $62 (即 -10% 内). 路径 A (财报 beat + capex 不上调) 概率 ~40%; 路径 B (财报 beat + capex 拖累) ~35% 但下行 -5~-12% 已 priced-in; 历史 leverage unwind 3-5 天接近尾声.

**Sources.**
- (none)

**Cross-assets.** n/a

**Agent read.** 用户 thesis 方向正确但概率高估. 关键反驳: (1) MU Q3 财报通常不给 next-fiscal-year capex guide (是 Q4 事), 所以 'capex commentary' 影响小于用户预期; (2) put/call 1.70 已说明买方深度对冲, 大幅下跌已 priced-in, 真正 surprise 风险在 upside; (3) BofA 跌势中抬 PT 到 $1500 是极强反向信号, 通常意味着卖方有 whisper info; (4) DRAM 30d +31% 不是 'still high', 是 'normal after 4-week leg up', cycle peak 通常需要 6-8 周 momentum. 我 agent 的预测: DRAM 最低 $63-67 区间触底反弹, 6/27 收盘 $65-72. 用户 50% 出清是合理 hedge 即使我赢, 因 thesis 错也只承担 -3% 机会成本.


---
### 2026-06-23#user-pred-mu-dram · n/a day · ▼ major
**Tags:** `prediction_recorded`, `thesis_debate`, `memory_pricing`, `user_stand`
**Confidence:** medium

**Primary cause.** USER PREDICTION (6/23 record): MU 财报 beat 也会因 capex guide 上调被市场惩罚，结合 KOSPI 抛售延续，DRAM ETF 财报后 3 个交易日 (6/24-6/27) 会大幅下跌。Trigger 决策: 等今晚 (6/23 19:30 ET, 韩股周三开盘) 验证韩国是否延续抛压, 然后明日盘前决定是否减仓 DRAM。

**Sources.**
- _Data:_ DRAM 当前 $69.22, 30d +31.1%, vol 1.76x. 距 $62 ($69.22 × -10.4%) 需要继续跌 -10.4%. ()
- _Data:_ MU capex 历史: FY2025 capex $14B + FCF -$0.9B (已负). 2022 周期顶建厂 → 2023 净亏 $5.8B 的 anchor 仍在. ()
- _Data:_ KOSPI 当日 vol: SK Hynix 1.40x, Samsung 1.29x — 真去杠杆已发生. ()
- _Corroboration:_ 市场情绪指标: GOOG 30d -12.78%, MSFT -9.7%, META -7.7% — capex 担忧主导叙事.

**Cross-assets.** n/a

**Agent read.** 用户判断 path B (35% 概率 in 我之前的场景表), 把概率主观抬到 65%. 主要论据: capex commentary 拖累 + KOSPI 延续, 联合作用. 缺陷: (a) MU Q3 通常不给 next-year capex guide, 这是 Q4 (9月) 的事 — 风险是叙述被市场过度解读; (b) DRAM 30d 仍 +31%, $62 需要 -10.4%, 是显著下行幅度; (c) 历史 leverage unwind 一般 3-5 天, 现在已第 2 天. 但用户的判断在 capex narrative 方向上有市场情绪 + 数据双重支撑.
 · Snapshot at `dashboard/2026-06-23.md`

---
### 2026-06-23 · -12.62% day · ▼ extreme
**Tags:** `memory_pricing`, `sector_rotation`, `ai_demand`, `flow_event`
**Confidence:** high

**Primary cause.** Korean memory crash 蔓延全球: SK Hynix -7.56%, SanDisk -11%, WD -10%, MU -11.09%。ETF 持仓机械跟标的物，DRAM -12.62% ≈ 加权(SK Hynix 25-30% × -7.56% + MU ~10% × -11.09% + Samsung + WD/SanDisk × -10%)。30d 仍 +33.59% — 这是 6/19-6/22 板块 +27.58% 5d 涨幅的第一个消化日，非趋势反转。叙事未碎 (HBM3E NVIDIA 独占、HBM4 leadership、MU-Anthropic 协议均无负面更新)，BofA/Wedbush 同日仍唱多。

**Sources.**
- 247WallSt: [SanDisk Plunges 11%, Micron and Western Digital Slide 10% as Korean Market Crash Hits Memory Chips](https://247wallst.com/investing/2026/06/23/sandisk-plunges-11-micron-and-western-digital-slide-10-as-korean-market-crash-hits-memory-chips/)
- _Data:_ SK Hynix 000660.KS -7.56% 1d / +11.67% 5d / +54.5% 30d. ETF holdings 主力跟跌核心。 ()
- _Corroboration:_ SanDisk -11%, WD -10%, MU -11.09%, Samsung 同步下挫
- _Data:_ vol_ratio 1.40x — 当日放量但 MU vol_ratio 0.65 (低) — ETF 流动性折价 ()

**Cross-assets.** SPY -0.97% · VIX 18.75 · TEN YEAR 4.49 · SKHYNIX -7.56% · MU -11.09% · WTI 73.11

**Agent read.** Stage-2 memory cycle 第一个消化日，非结构性破裂。三个关键观察：(1) 量未爆 — MU vol_ratio 0.65 说明无机构 capitulation；(2) 卖方未反水 — BofA/Wedbush 同日 reiterate 买入；(3) 龙头 SK Hynix 仍 30d +54.5% — 趋势完整。距 thesis-break $650 还有 +66% 缓冲。下一个真正信号: vol_ratio 升至 1.5x 以上或卖方下调评级。类比 6/22 attribution (HBM 三层 winner 结构) — 今天是该叙事被市场临时质疑，但没有催化击穿基本面。
 · Snapshot at `dashboard/attribution-2026-06-23.md`

---
### 2026-06-18 · +9.66% day · ▲ major
**Tags:** `executive_comment`, `memory_pricing`, `ai_demand`, `sector_rotation`
**Confidence:** high

**Primary cause.** Tim Cook flagged 'unavoidable' memory price hikes during Apple disclosure; SanDisk +11%, WD +7% confirm sector reaction

**Sources.**
- Yahoo: [SanDisk Jumps 11%, Western Digital Rises 7% After Apple Flags 'Unavoidable' Memory Price Hikes](https://finance.yahoo.com/)
- _Corroboration:_ SanDisk +11%, WD +7%, MU well bid same day; TSM +6.94% confirms broader AI hardware confirmation cycle
- Motley Fool: [Prediction: These Will Be Micron's and Sandisk's Stock Prices by the End of 2027](https://www.fool.com/)

**Cross-assets.** SPY +0.40% · VIX 14.2 · TEN YEAR 4.31 · WTI 75.57

**Agent read.** Stage-2 of memory cycle: AI demand bleeding into consumer-product margins. Stage-1 was hyperscaler buyers (NVDA / cloud capex 2024-2025). Stage-2 marker is consumer products absorbing memory cost — Apple's 'unavoidable' is canonical. Stage-3 historically: broader pass-through, supply response, then crash. We're early stage-2. AUM $17.5B in 75d of trading is structural inflow, not momentum. Risk is entry, not thesis: +57% in 30d at 52w high is the textbook moment to NOT add.
 · [Snapshot](snapshots/2026-06-18.md)

---
