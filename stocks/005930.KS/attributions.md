# 005930.KS attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-26 · -1.16% day · ▼ minor
**Tags:** `competitor_news`, `memory_pricing`, `earnings_pre_print`, `analyst_downgrade`
**Confidence:** medium

**Primary cause.** **记录本条不是因为 -1.16% 够大 (不够), 而是因为一条对三星直接有利的消息出现当天它是组内唯一下跌, 且成交量全组最低。**||**具名利好: Bernstein 称三星 3Q26 的 HBM 营收已反超 SK Hynix** (The Korea Herald 10/26 / Investing.com 10/22), 另 Chosunbiz 10/20「Samsung narrows SK hynix lead as HBM4 delays curb Korea chip gains」。这条消息对 10/15 建立的「三星既是内存卖方又是手机 OEM, 承受双向打击」要加一层: **若 HBM 已反超, 则卖方侧的收益比此前估计的大, 双向打击里利好的那一向被低估了。**||**而价格方向相反, 且量比 0.65x 为内存组最低。** 两种读法: (a) **10/27 财报前减风险** (比 SK Hynix 早一天) + 高盛下调 KOSPI 目标 25%; (b) 市场尚未消化 Bernstein 的说法。**量比 0.65x 更支持 (b)** —— 既没有人在买这条利好, 也没有人在恐慌卖。**一条本应重要的消息在零成交量下被忽略, 这本身是「市场尚未定价」的证据, 而不是「市场否决了它」的证据。**||**⚠️ 日期不确定**: 三星 Q3 完整业绩日期无法确认。10/08 已发布 preliminary guidance (Samsung Global Newsroom); yfinance 给 10/27; 去年完整业绩为 2025-10-30。本报告标为「10/27 (未核实)」。||**位置: ₩213,000, 30d -20.96%, 低于 MA50 16.28%, 远期 PE 2.95x。** 30d 跌幅介于 SK Hynix 本线 (-28.89%) 与 DRAM ETF (-11.81%) 之间。

**Sources.**
- The Korea Herald: Bernstein: Samsung overtook SK hynix in HBM revenue in 3Q26
- Chosunbiz: Samsung narrows SK hynix lead as HBM4 delays curb Korea chip gains
- Yahoo/Korea press: Goldman Sachs cuts Kospi target by 25% amid AI stock selloff
- Yonhap News Agency: Samsung Electronics, SK hynix set to report Q3 earnings this week
- Yahoo Finance: Why South Korea’s stock market represents the purest AI trade

**Cross-assets.** SPY +0.71% · VIX 18.39 · TEN YEAR 4.99 · FIVE YEAR 4.82 · THIRTY YEAR 5.3 · WTI 101.32 · BRENT 115.3 · DXY 102.018 · GOLD 4027.5 · SILVER 53.97 · BTC 79704.67 · USDKRW 1325.31

**Agent read.** 三星现在是两场裁决里更早的那一场 (10/27 vs SK Hynix 10/28), 且因为 Bernstein 的说法, 它对 HBM 份额的表述与 SK Hynix 的同等重要 —— 这是对此前「SK Hynix 的财报是 CXMT 的免费裁决场」逻辑的修正: 裁决现在需要两场, 而三星那场免费提前一天。日期本身未核实是一个需要在 10/27 当天确认的风险。
 · Snapshot at `dashboard/2026-10-26.md`

---
### 2026-10-15 · -9.48% day · ▼ extreme
**Tags:** `competitor_news`, `memory_pricing`, `sector_rotation`
**Confidence:** high

**Primary cause.** **三星今天的量比 2.06x 是全书 38 个标的里最高的一个, 且跌幅 -9.48% 仅次于 SK Hynix。** 但三星今天的暴露和 SK Hynix 有一个关键差别, 这个差别今天第一次变得重要: **三星既是内存卖方, 又是手机 OEM。** **🔴 今天存储叙事从单侧变成双侧 —— 这是本轮下跌四天里最重要的性质变化.** 10/12-10/15 四天的全部跌幅建立在一个**供给侧预期**上: 中国 CXMT 把更密的 DRAM 设计对准服务器内存 → 未来供给增加 → 价格周期提前见顶。10/14 报告的核心批评是这个假设至今零技术细节 (❌无制程节点 ❌无位密度 ❌无 DDR5/HBM 指认 ❌无时间表 ❌无产能数字 ❌无第三方良率验证); 今天是第 4 天 / 自 9/21 首次出现算起是**第 25 天**, 这六项**仍然一项未动**。||今天新增的证据性质完全不同, 它从**需求侧**攻击同一个论点: **Counterpoint Research — 2026 年第三季度全球智能手机出货量同比 -20%, 是 2012 年以来最弱的第三季度, 直接归因于 DRAM 与 NAND 价格飙升推高整机成本。** 重要性在于论点类型变了: CXMT 是一个**预期** (未来可能有更多供给, 无法验证, 可以持续数季不被回答); 手机出货 -20% 是一个**已发生的事实** (涨价已经消灭了需求, 单位数据已在账上)。||内存多头论点的核心是「定价权」, 而定价权的边界条件就是需求弹性。手机是 DRAM/NAND 最大单一终端市场之一, -20% 的出货降幅 + 14 年来最弱 Q3 + 第三方研究机构直接归因于内存涨价 —— **这是本 workspace 记录以来第一次看到内存涨价的代价以单位需求的形式被量化。** 配合巴克莱下调 Dell/HPE 的理由 (内存成本过账虚增服务器营收, 不带毛利), 产业链里的分配机制也被点明: 内存涨价不是纯增量, 而是从下游转移。||**因此对存储组的态度需要修正**: 在今天之前合理的态度是「跌幅建立在一个无证据的供给预期上, 等 10/26 免费拿答案」; 今天之后 —— **跌幅里现在有一部分建立在一个有证据的需求事实上。即使 10/26 把 CXMT 完全否掉, 需求弹性这一侧的坏消息不会被同时否掉。**||因此 Counterpoint 的手机出货 -20% 对三星是**双向打击**: (1) 作为内存厂, 它的最大终端市场之一在萎缩 → 未来定价权受限; (2) 作为手机 OEM, 它自己的出货量也在那 -20% 里, 而它的 BOM 成本正被它自己所在的内存行业推高。**SK Hynix 只承受第一种, 三星承受两种。** 这解释了为什么三星的量比 (2.06x) 高于 SK Hynix (1.96x), 尽管三星的 HBM 份额远低于 SK Hynix、理论上对 CXMT 的 HBM 威胁暴露更小。||对照 10/14: 当日三星 **0.00%** (持平) 而 SK Hynix -1.66%。一天之后三星跌 9.48% 跑在前面 —— **这个次序倒转和需求侧证据今天出现的时点一致**, 是支持「今天的新驱动是需求破坏而非 CXMT」的一条独立线索。||裁决点: 10/27 三星 Q3 财报 (SK Hynix 本线 10/26 先行一天)。||**宏观共因 (今天的共因只有一个, 但它的形状是反直觉的).** 九月 PPI (Producer Price Index, 生产者物价指数 — BLS 每月发布, 衡量生产者卖出价格, 通常领先 CPI 一到两个季度) 环比 **+1.3%** (8月 +0.5% / 7月 +0.2%, 2022年3月 +1.7% 以来最大单月), 同比 **+6.3%** (2022年12月 +6.4% 以来最大年度涨幅); 核心 (除食品/能源/贸易服务) 环比 +0.5% / 同比 +5.0%; 商品 +2.6% 其中**能源 +10.8% / 汽油 +20.3%**。接在 10/14 CPI 同比 3.7% (共识 3.6%) 之后, 是连续两天的下游+上游双向确认。零售销售同时跳升、失业申领保持稳健 —— 三项数据同向意味着经济不弱而价格在涨, 这是加息路径最不利的组合。||**❗但长端的反应方向和教科书相反, 本条必须作为限定随附**: 3M (^IRX) 4.088% **仅 +0.3bp**, 5Y 4.903% **-8.9bp**, 10Y 5.089% **-10.1bp**, 30Y 5.424% **-10.1bp**, TLT +1.52% (5d +2.85%)。**前端一动不动而 5年到30年平行下行 10bp —— 这个形状不可能是 Fed 政策定价 (政策定价必先动前端), 只能是对久期本身的避险需求。** 当天新闻口径直接说出了这件事 ('Tech slumps as AI financing worries grow, investors flock to bonds')。||**⭐ 方法论升级 (改写 10/05、10/07、10/08、10/14 四份报告的同一条限定)**: 那四天记录的都是「长端**不动**」—— 即对利空/利多都无响应, 属于零信息的否证, 只能说明「没有反证」。**今天长端第一次动了, 而且方向是下行**, 也就是折现率给了权益一个**顺风**, 权益却继续跌。结论因此从「无反证」升级为「有正面证据」: 折现率通道今天是负贡献 (利好), 跌幅必须由风险溢价**全额**解释。||**横截面否证「加息打击高倍数/长久期股」—— 本周第三次**: PE 从 SKHY 9.74x / DRAM 9.84x / MU 12.79x 一直到 AMD 148.2x / PLTR 172.0x / TSLA 340.0x, 跨 35 倍; 跌幅区间只有 -0.26% ~ -4.14% 且与倍数**无关** (TSLA 340x 跌 1.84% 却轻于 DRAM 9.8x 的 3.18%)。真正把跌幅排序出来的是「是否在 AI 供给/融资链上」。||**参与度限定 (与 10/14 相反)**: 38 只标的量比中位数 **0.755x**, 仅 11 只过 1.0x, 4 只过 1.5x。10/14 为中位数 1.02x / 17-of-32, 当时记为「本轮下跌序列第一个全参与度日」—— **一天后没有延续, 那是一个点不是趋势**。且今天放量的位置极度集中在韩国两条本线 (2.06x / 1.96x) + DRAM ETF (1.55x) + TSM (1.52x 财报日), 美国大型科技几乎无成交 (MSFT 0.54x / AMZN 0.54x / TSLA 0.47x / GOOG 0.39x / META 0.36x)。**这是对一个特定位置的定向抛售, 不是广泛降风险。**||**指数层面第一次方向分离**: QQQ -0.61% (跌破 MA50 $726.34) vs Dow +0.86% vs IWM +0.74%, 裂口 1.47pp。前四个下跌日 (10/07、10/08、10/13、10/14) 都是全指数同向。30d 口径 QQQ +2.26% vs IWM -6.77% 裂口从 10/14 的 12.4pp 收窄到 9.0pp, **且是用纳指跌、小盘涨的方式收窄 —— 轮动而非普跌的硬证据**。落点新闻一致: Moderna +6% (资金流入医疗) / Walmart +3% (德银上调) / Opendoor-Zillow +7% (长端回落直接利好住房)。VIX 16.88 (+0.06%) 几乎零反应, 第五次确认「不是系统性恐慌」。

**Sources.**
- Counterpoint Research via American News Group: A 20% Drop in Smartphone Shipments Shows Who Wins When Memory Gets Expensive (Counterpoint: Q3 -20% YoY, 2012 年以来最弱 Q3)
- Yahoo: The Nikkei Crashed Nearly 5% Overnight — 韩国 KOSPI 跌幅更大
- {"type": "cross_stock", "title": "10/14 \u4e09\u661f 0.00% vs SK Hynix -1.66%; 10/15 \u4e09\u661f -9.48% vs SK Hynix -11.06% \u2014 \u6b21\u5e8f\u5012\u8f6c\u4e0e\u9700\u6c42\u4fa7\u8bc1\u636e\u51fa\u73b0\u7684\u65f6\u70b9\u4e00\u81f4", "publisher": "workspace"}

**Cross-assets.** SPY +0.09% · VIX 16.88 · TEN YEAR 5.089 · WTI 96.58 · DXY 102.101 · GOLD 4168.2 · BTC 82171

**Agent read.** 全书最高量比 (2.06x) 出现在唯一同时暴露于「内存卖方」与「手机 OEM」两侧的标的上, 且与 10/14 的次序倒转时点吻合 — 这是今天的驱动已从 CXMT 供给预期切换到需求破坏的最好的单一证据。


---
### 2026-09-23 · +3.25% day · ▲ material
**Tags:** `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** Samsung 韩股收 +3.25%（1w +13.1%），与同日美股 SKHY -3.21%、MU -2.23%、DRAM -2.99% 方向相反。**归因结论：时区错位，非基本面分歧。** 韩国股市收盘发生在美国 10Y 收益率升至 5.12%（2007 年以来最高）的重定价之前，因此未反映当日的折现率冲击。Samsung 当日无独立公司级催化剂。

**Sources.**
- : [10-year Treasury yield hits highest level since 2007 as market prices in another Fed rate hike](https://finance.yahoo.com/quote/%5ETNX/)
- : [Stocks, Bonds Slip as Oil Jump Fuels Fed-Hike Bets (Bloomberg)](https://finance.yahoo.com/quote/CL%3DF/)

**Cross-assets.** SPY CHANGE -0.74% · VIX 15.34 · TEN YEAR 5.12 · WTI 91.41 · DXY 101.19 · QQQ CHANGE -1.01%

**Agent read.** 这是今天最容易被误读的数据点。不应读成『Samsung 强于 SK Hynix』——两者同行业高度相关，单日 6.5 个百分点反向差在无公司新闻时几乎只能由交易时段错位解释。明确的次日验证点：韩股开盘若补跌，时区解释成立并可作为未来同类情形的标准判据；若 Samsung 不跌，则存在被遗漏的独立变量，需重新归因整个 DRAM/HBM cluster 的当日结论。记录此条的目的正是为了让这个验证可被回溯。
 · Snapshot at `dashboard/2026-09-23.md`

---
