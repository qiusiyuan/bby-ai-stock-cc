# SNDK attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

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
