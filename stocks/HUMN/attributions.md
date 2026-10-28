# HUMN attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-28 · +3.54% day · ▲ material
**Tags:** `unattributed`, `flow_event`
**Confidence:** low

**Primary cause.** **+3.54% 零个具名催化剂, 且今天 TSLA 是下跌的 (-1.31%) —— 完整的第四次自然实验分析见同日 CROB 条目。** confidence 记 low。||**put/call 0.05 —— 本质上没有期权市场, 连续两份报告同一读数。量比 0.42x。MA200 下方 -9.15%** (三只里最深), MA50 下方 -0.34%。距 52w 高 -26.01% / **距 52w 低 +13.78% —— 全部 active 标的里距 52 周低点最近的一只** (个股里最近的是 META +17.40%)。||**30 天 +1.54%, 与 KOID (+1.26%) 和 CROB (+0.60%) 相差不到 1pp, 而 TSLA +12.30% —— 裂口 10.8pp。三只内部高度一致是「它们跟踪人形行业 beta 而非 Optimus alpha」的核心证据。**||**建议 (同 CROB): 停止日度捕获率计算, 本 cluster 改事件驱动。日度读数的信息含量已低于噪音 (put/call 0.05 + 量比 0.42x + 30d 走平)。** 唯一能把 beta 变成 alpha 的事件类型是**具名订单** —— Optimus/Cybercab 的具名客户订单、具名交付量, 或任一成分股拿到 Tesla 确认订单。时间表承诺 (「年底交付」「进入生产」) 在过去四次实验里零次产生可测量的外溢。||90 天内零硬催化剂。groups.yaml 已记录核心错配: UBTech (9880.HK) 与 Unitree (未上市)、谐波减速器 (中国 A 股) 全部美股账户不可及。

**Sources.**
- (none)

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-10-22 · -3.33% day · ▼ material
**Tags:** `sector_rotation`, `production_milestone`
**Confidence:** high

**Primary cause.** **今天是 humanoid 组的一次干净自然实验，结果对 Optimus thesis 的载体假设不利。** TSLA 财报同时确认 **Optimus 已进入生产**、**Cybercab 年底交付客户** —— 这正是 cluster watch_items 里「Optimus Gen3/V3 发布」「Fremont 量产确认」的实质内容，是本组等待的那种硬消息。||**结果: HUMN -3.33% / KOID -4.23% / CROB -0.71%，没有一只上涨；TSLA 只跌 2.61% 且 5d +3.84% / 30d +3.52%。市场把 Optimus 量产的价值完全给了 TSLA，零外溢到供应链 ETF。**||**这给 memory 里记的 Optimus 错配 thesis 提供了第一个价格证据，而方向比原假设更不利:** 原记录是「内容最纯的 (中国减速器供应链 / UBTech / Unitree) 买不到，买得到的内容最稀」。今天显示的不是「内容稀」，而是「**买得到的那些标的根本没有参与 Optimus 的定价**」。若该关系持续，三只 ETF 提供的是**人形机器人行业的 beta**，不是 **Optimus 的 alpha** —— 这是两件不同的事，之前混在一起了。表达 Optimus 观点的最有效可及载体可能就是 TSLA 本身 (代价是同时带 EV 业务周期性与合并条款的不确定性)。**需要下一次 Optimus 硬消息时重复这个对照才能定论，单日不足。**||**久期框架 (reference/duration_rate_framework) 第二次被修正，而且这次更强。** 框架按「远近 × 确定性」双轴，humanoid 三只属于「最远 × 最不确定」象限 —— 按久期逻辑，今天 2Y -17.3bp / 10Y -18.1bp 的下行应该给它们全市场最大的顺风。实际三只全跌。对照: 近 × 确定的 MSFT -2.02% 且 30d +6.04% 为唯一仍在 MA50 上方的 AI 标的; 近 × 确定 × 非 AI 的 AAPL **+0.60%**。||**10/15 已记录过一次「风险偏好收缩时『确定性』轴压倒『久期』轴」。今天版本更强: 10/15 的利率下行只有 10bp 且前端未动, 今天是 18bp 且前端带着走 —— 顺风加倍, 结果不变。结论可从「压倒」升级为: 在风险偏好收缩的环境里, 久期轴不只是被压倒, 它的符号可以反过来。这条应作为限定写回 reference。**||🚨 **位置风险: HUMN $26.41 距 52 周低点 $25.47 仅 +3.7%，是本组唯一接近技术破位的标的**; vs MA50 $29.49 偏离 -10.4%; 距 52w 高 $39.17 为 -32.58%。量比 0.91x。

**Sources.**
- Decrypt: Tesla's Profit Drops 43% as Musk Starts Building Robots — Optimus 已进入生产, Cybercab 年底交付客户
- Investopedia: Elon Musk Hints at Exciting New Capabilities for Tesla's Optimus Robots
- {"type": "cross_stock", "title": "Optimus \u91cf\u4ea7\u786e\u8ba4\u5f53\u65e5: TSLA -2.61% (5d +3.84%) vs HUMN -3.33% / KOID -4.23% / CROB -0.71% \u2014 \u5b9a\u4ef7\u96f6\u5916\u6ea2", "publisher": "workspace"}
- {"type": "computed", "title": "\u4e45\u671f\u987a\u98ce 18bp (\u524d\u7aef\u5e26\u52a8) \u4e0b\u6700\u957f\u4e45\u671f\u8d44\u4ea7\u4ecd\u8dcc; \u5bf9\u7167 MSFT 30d +6.04% / AAPL +0.60%", "publisher": "workspace"}
- {"type": "research", "title": "research/sectors/2026-08-17-optimus-supply-chain.md \u2014 \u8f7d\u4f53\u9519\u914d\u5047\u8bbe\u9700\u6309\u4eca\u5929\u7ed3\u679c\u4fee\u6b63", "publisher": "workspace"}

**Cross-assets.** SPY -1.44% · VIX 19.37 · TEN YEAR 4.957 · TWO YEAR 4.65 · WTI 99.19 · DXY 101.6 · GOLD 4055.4 · BTC 81063

**Agent read.** 今天是一次干净的自然实验: Optimus 拿到最硬的两条确认, 三只 ETF 零参与。若下一次硬消息重复这个结果, 应把三只正式重新归类为行业 beta 工具, 并把 Optimus 观点的载体改为 TSLA。同时久期框架需要加一条限定 — 风险偏好收缩时久期轴的符号可以反过来。HUMN 距 52 周低点仅 +3.7%, 是本组最近破位的一只。
 · Snapshot at `dashboard/2026-10-22.md`

---
### 2026-10-15 · -3.19% day · ▼ material
**Tags:** `sector_rotation`, `macro_rates`
**Confidence:** medium

**Primary cause.** **零公司级新闻日 —— 跌幅 100% 是 beta。但「是 beta」这个结论今天产生了一个有价值的矛盾, 它修正了这个 cluster 一直使用的久期框架。**||humanoid cluster 在 workspace 里被定义为「纯长久期主题, 无当期盈利, 对利率/风险偏好极敏感」。**按久期框架, 今天长端 -10bp 应该是顺风。实际结果是三只全跌 2.2-3.2%, 跑输 SPY (+0.09%) 2.3-3.3pp (HUMN -3.19% / CROB -2.49% / KOID -2.20%)。**||对照已记录的久期/利率敏感度框架 —— 其双轴是「久期光谱」×「远近 × 确定性」。**今天的结果说明在风险偏好收缩的日子里, 第二个轴 (确定性) 压倒第一个轴 (久期)。** HUMN 的现金流不仅**远**, 而且**不确定**。折现率下行对「远但确定」的现金流是实质利好 (今天 MSFT +1.08% 以及住房股 Opendoor/Zillow +7% 就是这一类), 但对「远且不确定」的现金流几乎无帮助, 因为它们的估值主要由**风险溢价**而非无风险利率决定。||**这是今天跨 cluster 最一致的一条线**: 同一个机制 (风险溢价上行、折现率下行) 同时解释了 (a) 供给方芯片全跌而开支方全平、(b) humanoid 三只在利率顺风下仍跌、(c) 长端 -10bp 却伴随权益下跌。**三个独立观察指向同一个因子。**||组内分化: HUMN 今日最弱 (-3.19%), 符合它是三只里最纯的 OEM + 执行器暴露 (beta 最高); KOID 最抗跌 (-2.20%) 且是唯一放量 (1.48x), 更广的「物理 AI」使能层分散了纯人形风险; **CROB 量比 0.21x 为全书最低而 30d -17.85% 为三只最差 —— 「无人交易的持续下跌」, 典型的流动性枯竭形态, 比放量下跌更难退出。**||Optimus 侧今天零输入: 无 Gen3/V3 发布、无 Fremont 量产确认、无任一供应商拿到 Tesla 确认订单。唯一相关内容是一篇 10/14 的 ETF 板块综述 (「用这些 ETF 把握物理 AI 浪潮」), 不是催化剂。||`research/sectors/2026-08-17-optimus-supply-chain.md` 记录的核心错配今天依然成立 —— 内容最纯的 (中国减速器供应链) 买不到, 买得到的内容最稀; **且 CROB 的流动性枯竭使「用美股 ETF 表达中国机器人主题」这条路径的质量进一步下降。**||价格位置: $25.90, 已在 MA50 $30.10 下方 14.0%; 距 52w 高 $39.17 **-33.9%**; PE 26.23x。||**宏观共因 (今天的共因只有一个, 但它的形状是反直觉的).** 九月 PPI (Producer Price Index, 生产者物价指数 — BLS 每月发布, 衡量生产者卖出价格, 通常领先 CPI 一到两个季度) 环比 **+1.3%** (8月 +0.5% / 7月 +0.2%, 2022年3月 +1.7% 以来最大单月), 同比 **+6.3%** (2022年12月 +6.4% 以来最大年度涨幅); 核心 (除食品/能源/贸易服务) 环比 +0.5% / 同比 +5.0%; 商品 +2.6% 其中**能源 +10.8% / 汽油 +20.3%**。接在 10/14 CPI 同比 3.7% (共识 3.6%) 之后, 是连续两天的下游+上游双向确认。零售销售同时跳升、失业申领保持稳健 —— 三项数据同向意味着经济不弱而价格在涨, 这是加息路径最不利的组合。||**❗但长端的反应方向和教科书相反, 本条必须作为限定随附**: 3M (^IRX) 4.088% **仅 +0.3bp**, 5Y 4.903% **-8.9bp**, 10Y 5.089% **-10.1bp**, 30Y 5.424% **-10.1bp**, TLT +1.52% (5d +2.85%)。**前端一动不动而 5年到30年平行下行 10bp —— 这个形状不可能是 Fed 政策定价 (政策定价必先动前端), 只能是对久期本身的避险需求。** 当天新闻口径直接说出了这件事 ('Tech slumps as AI financing worries grow, investors flock to bonds')。||**⭐ 方法论升级 (改写 10/05、10/07、10/08、10/14 四份报告的同一条限定)**: 那四天记录的都是「长端**不动**」—— 即对利空/利多都无响应, 属于零信息的否证, 只能说明「没有反证」。**今天长端第一次动了, 而且方向是下行**, 也就是折现率给了权益一个**顺风**, 权益却继续跌。结论因此从「无反证」升级为「有正面证据」: 折现率通道今天是负贡献 (利好), 跌幅必须由风险溢价**全额**解释。||**横截面否证「加息打击高倍数/长久期股」—— 本周第三次**: PE 从 SKHY 9.74x / DRAM 9.84x / MU 12.79x 一直到 AMD 148.2x / PLTR 172.0x / TSLA 340.0x, 跨 35 倍; 跌幅区间只有 -0.26% ~ -4.14% 且与倍数**无关** (TSLA 340x 跌 1.84% 却轻于 DRAM 9.8x 的 3.18%)。真正把跌幅排序出来的是「是否在 AI 供给/融资链上」。||**参与度限定 (与 10/14 相反)**: 38 只标的量比中位数 **0.755x**, 仅 11 只过 1.0x, 4 只过 1.5x。10/14 为中位数 1.02x / 17-of-32, 当时记为「本轮下跌序列第一个全参与度日」—— **一天后没有延续, 那是一个点不是趋势**。且今天放量的位置极度集中在韩国两条本线 (2.06x / 1.96x) + DRAM ETF (1.55x) + TSM (1.52x 财报日), 美国大型科技几乎无成交 (MSFT 0.54x / AMZN 0.54x / TSLA 0.47x / GOOG 0.39x / META 0.36x)。**这是对一个特定位置的定向抛售, 不是广泛降风险。**||**指数层面第一次方向分离**: QQQ -0.61% (跌破 MA50 $726.34) vs Dow +0.86% vs IWM +0.74%, 裂口 1.47pp。前四个下跌日 (10/07、10/08、10/13、10/14) 都是全指数同向。30d 口径 QQQ +2.26% vs IWM -6.77% 裂口从 10/14 的 12.4pp 收窄到 9.0pp, **且是用纳指跌、小盘涨的方式收窄 —— 轮动而非普跌的硬证据**。落点新闻一致: Moderna +6% (资金流入医疗) / Walmart +3% (德银上调) / Opendoor-Zillow +7% (长端回落直接利好住房)。VIX 16.88 (+0.06%) 几乎零反应, 第五次确认「不是系统性恐慌」。

**Sources.**
- {"type": "cross_stock", "title": "\u4e09\u53ea\u5168\u8dcc\u4e14\u8dd1\u8f93 SPY (+0.09%): HUMN -3.19% / CROB -2.49% / KOID -2.20%, \u800c\u957f\u7aef\u4eca\u5929 -10bp \u662f\u6298\u73b0\u7387\u987a\u98ce", "publisher": "workspace"}
- {"type": "cross_stock", "title": "\u91cf\u6bd4\u5206\u5316: KOID 1.48x (\u552f\u4e00\u653e\u91cf, \u6700\u6297\u8dcc) / HUMN 0.95x / CROB 0.21x (\u5168\u4e66\u6700\u4f4e, 30d -17.85% \u6700\u5dee = \u6d41\u52a8\u6027\u67af\u7aed)", "publisher": "workspace"}
- Zacks via Yahoo: Grab These ETFs to Capitalize on the Physical AI Wave
- {"type": "research", "title": "research/sectors/2026-08-17-optimus-supply-chain.md \u2014 \u6838\u5fc3\u9519\u914d: \u5185\u5bb9\u6700\u7eaf\u7684\u4e70\u4e0d\u5230, \u4e70\u5f97\u5230\u7684\u5185\u5bb9\u6700\u7a00", "publisher": "workspace"}

**Cross-assets.** SPY +0.09% · VIX 16.88 · TEN YEAR 5.089 · WTI 96.58 · DXY 102.101 · GOLD 4168.2 · BTC 82171

**Agent read.** 零新闻 100% beta, 但在折现率顺风日仍跌 — 这修正了久期框架: 风险偏好收缩时「确定性」轴压倒「久期」轴。这也是今天跨 cluster 最一致的一条线 (供给方全跌/humanoid 逆风/长端下行伴随权益跌 = 同一个风险溢价因子)。唯一的新风险事实是 CROB 量比 0.21x + 30d -17.85% 的流动性枯竭。


---
### 2026-10-14 · -3.37% day · ▼ material
**Tags:** `macro_inflation`, `sector_rotation`
**Confidence:** low

**Primary cause.** **跌破 MA50 $30.24 达 -11.5%, 是 humanoid 三只里偏离 MA50 最深的; 距 52w 高 $39.17 -31.7%。** 量比 1.02x 恰为全场中位数。无公司/ETF 级消息。纯主题久期工具在 CPI 环比创年内新高日的教科书反应 — **正因为完全符合预期, 它的信息量最低: 今天的跌幅不包含任何关于人形机器人进展的内容。把 ETF 价格当论点读数会持续产生噪音。** 对照: 10/08 时 HUMN 量比 1.36x 曾是「全书唯一真实放量离场」, 今天回到中位数水平, 那次的放量未延续。|| 宏观共因 (三个独立的因, 不可压成一个): **(1) 九月 CPI**: 同比 +3.7% (共识 3.6%)、环比 **+0.6% 为过去一年最高**。CPI = Consumer Price Index, BLS 每月发布的美国最主要通胀指标。环比年化约 7.4%, 远高于 Fed 2% 目标。timeline 在今天之前已记 Oxford Economics 的提示 — 九月调查窗口内柴油 +60 美分/加仑、汽油 +20 美分, 油价冲击会进入这份读数, 所以这个数字是可预告的。它接在 9/17 FOMC 转鹰 + 9 月纪要 (10/07 公布) 指向今年再加一次息 (市场当时只给 19%) 之上, 是纪要后第一个硬数据且站在纪要一边。**(2) ❗长端拒绝配合 — 本条必须作为限定随附**: CPI 超预期而 10Y -2.7bp / 30Y -3.8bp / TLT +0.66%。媒体口径写的是 'rate-hike jitters'、'rising bond yields', 债市当天的实际方向与之相反。所以今天的跌**不能用「当天利率上行」解释** — 实现通道是风险溢价 (VIX +10.48%) 与叙事, 不是折现率。这是本月第四次长端对本应推高它的消息不配合 (10/01 失败突破 / 10/02 非农利多无响应 / 10/08 诱因缓解不修复 / 今天 CPI 超预期不涨)。**(3) 横截面否证「加息打击高倍数股」的单一叙事**: 倍数最高的 TSLA (fwd PE 168x) 跌 2.15%, 低于倍数中等的MRVL (33.7x) -8.73%、SNOW (111x) -6.34%、GEV (37x) -6.20%。跌幅与 **30d 涨幅**的相关性明显优于与倍数的相关性(MRVL 30d +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小跌幅)。**今天卖的是一个月里的涨幅, 不是久期。** **⭐ 方法论变化 (改写前三份报告的限定)**: 10/05、10/07、10/08 三份归因都写了同一句「半量里的下跌属『没有买盘』而非『出现卖盘』, 方向可信幅度不可信」。**今天不成立**: 量比中位数 1.02x (10/08 为 0.48x / 10/07 0.79x / 10/05 0.49x), 17/32 过 1.0x (10/08 为 3/34), 放量集中在跌最多的标的 (GEV 1.65x / QQQ 1.53x / TSM 1.45x / KOID 1.39x / MRVL 1.31x / DRAM 1.30x)。**这是这轮下跌序列里第一个全参与度的下跌日 — 幅度本身开始带信息。** 反方限定仍要记: 跌最惨的 MRVL 量比只有 1.31x、MU 只有 1.04x, 「放量」是全场性的而非个别标的清仓。

**Sources.**
- 247wallst via yfinance (CPI 3.7% YoY vs 3.6% 共识; MoM +0.6% 年内最高): Trump Media and Rumble Decline 5% as September Inflation Runs Above Forecasts; Reddit Slides 2%
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- IBD via yfinance: Stock Market Today: Nasdaq Dives On Rate Hike Jitters, AI Woes; Taiwan Semi Earnings On Deck
- Yahoo Finance video (Baird 策略师 Ted Mortonson): CoreWeave, Intel, Micron, & other tech stocks are plummeting. Here's why.

**Cross-assets.** SPY -1.08% · QQQ -1.97% · IWM -1.93% · DIA -0.11% · VIX 16.87 (+10.48%) · TEN YEAR 5.190% (-2.7bp) · THIRTY YEAR 5.525% (-3.8bp) · TLT +0.66% · WTI +1.16% · BRENT $106.06 (30d +12.05%) · GOLD -1.23% · SILVER -5.81% · DXY 102.530 (+0.34%) · BTC -1.81% · ETH -3.40% · BREADTH 32 只中 26 跌 / 6 涨 (含 2 只反向) · VOLUME MEDIAN 量比中位数 1.02x · 17/32 过 1.0x (10/08 为 0.48x · 3/34)

**Agent read.** 


---
### 2026-10-08 · -4.11% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`, `flow_event`
**Confidence:** high

**Primary cause.** **全书唯一的真实放量离场: 量比 1.36x, 在全书中位数 0.48x 的日子里是最高的权益标的** (另外两只过 1.0x 的是 BTC-USD 1.35x 下跌、HXE.TO 1.20x 上涨)。这把 HUMN 与今天其他 5% 级跌幅区分开: NOK 0.50x / MRVL 0.68x / SNDK 0.52x / INTC 0.59x 是薄盘口里的边际定价, HUMN 是有人在量上离场。**humanoid 全组同向: HUMN -4.11% / CROB -4.26% / KOID -3.32%, 且 30d 全负 (CROB -12.70% / HUMN -7.29% / KOID -4.03%) 对照 QQQ 30d +5.11% — 在 AI 叙事上行整月里, 人形机器人板块是负收益, 落后 QQQ 9-18pp。**机制: 全组无当期盈利、现金流在远期 (Optimus 量产与供应链订单都在 2027+)、ETF 规模小流动性差 = 最长久期也最依赖风险偏好的一端。今天的触发是地缘 (美国据报考虑扩大对伊朗打击 + 油轮遇袭, WTI 盘中冲 93.08, 30Y 开在 5.695 的 24 年高位区) — 长端开在 24 年高位对最长久期资产是直接打击, 这一段用利率框架完全解释得通。**但两个诱因当天都缓解了 (10Y 盘前 5.331 → 收 5.239; 油回吐一半), 该组仍以全书最重的放量收跌 — 这一段利率解释不了。** 对无盈利、靠外部融资推进的主题, 信用窗口拥挤 (当日 AVGO >$500亿 / SPCX $400亿 / Oracle 同期发债) 与风险偏好收缩是更可能的留存原因; 但同日 Anthropic $5,180亿 云与算力支出利多全组不涨, 说明「对任何 AI 消息都不反应」的情绪解释也成立, 今天无法排除。组内纯度与波动的直接定价: 跌幅排序 CROB > HUMN > KOID, 即越纯跌得越多, KOID (成分最分散, 含广泛物理 AI 使能层) 提供约 0.8-0.9pp 缓冲。CROB 今天量比仅 0.44x — 跌 4.26% 几乎无成交, 印证 state.yaml 已标注的「AUM 极小、流动性差」, 其回撤深度 (-39.4% 距 52w 高) 不能等同于折价幅度, 因为想离场时同样没有对手盘。**当日全组零公司级/行业级新闻 (HUMN 新闻流为空) → 100% 风险偏好事件, 零基本面信息含量**: 既不构成论点损伤的证据, 也没有任何东西支撑反弹。该板块的结构性问题是它没有自己的日历 — 三只皆 ETF, 无财报无指引, 唯一可预约的信息源是 10/21 TSLA 财报里的 Optimus 部分, 一个它完全不能控制的事件。

**Sources.**
- via yfinance HUMN news: (当日 HUMN/KOID/CROB 新闻流为空 — 无公司级或行业级消息)
- via yfinance AVGO news: SpaceX, Broadcom and Oracle All Want Billions in AI Chip Debt at the Same Time
- via yfinance AVGO news: MARKETS LIVE: US stocks slip on bond and AI debt fears

**Cross-assets.** n/a

**Agent read.** 


---
