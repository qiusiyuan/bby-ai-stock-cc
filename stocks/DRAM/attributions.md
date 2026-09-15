# DRAM attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

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
