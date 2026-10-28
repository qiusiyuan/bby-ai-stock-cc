# CROB attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-28 · +4.18% day · ▲ material
**Tags:** `unattributed`, `flow_event`
**Confidence:** low

**Primary cause.** **+4.18% 为三只 humanoid ETF 里最强, 量比 1.39x 是连续三份报告垫底 (0.11x → 0.21x → 0.42x) 之后第一次上量 —— 但零个具名催化剂。** 今天唯一相关口径是「Is China Winning the Robotics Race? See Through the ETF Lens」(通用型分析, 非事件)。confidence 记 low。||**🔴 第四次 humanoid 自然实验, 而这次的设置是前三次都没有的: TSLA 下跌 (-1.31%) 而三只 ETF 上涨 (HUMN +3.54% / KOID +1.61% / CROB +4.18%)。前三次三只都与 TSLA 同向, 只是幅度不同。符号相反意味着「捕获率」这个比率不再有意义 (分子分母异号)。**||四次完整记录: 10/22 TSLA -2.61% (Optimus 正面) → 三只 -3.33/-4.23/-0.71, 下行捕获 128%/162%/27%; 10/26 TSLA +5.21% (消息最正面) → +2.52/+1.63/+0.46, 上行捕获 48%/31%/9% (均值 29%); 10/27 TSLA +4.04% → -0.36/+2.19/-2.02, 捕获 -9%/54%/-50% (均值 -1.6%); **今天 TSLA -1.31% (零公司新闻) → +3.54/+1.61/+4.18, 符号相反。**||**结论必须修正: 前三次记为「负向不对称」(下行约 145%、上行约 40%), 10/27 加强为「上行捕获已归零」—— 今天的数据说明这两条都不是在描述一个稳定的 beta 结构, 而是在描述一个 beta 接近零的关系上的噪音。** 证据是 30 天口径: HUMN +1.54% / KOID +1.26% / CROB +0.60% —— **三只几乎完全一致 (相差不到 1pp), 而 TSLA +12.30%, 裂口 10.8-11.7pp。三只之间高度一致、与 TSLA 裂口巨大, 这是「三只跟踪的是同一个东西 (人形行业 beta), 而那个东西不是 TSLA」最干净的证据形式。**||**建议: 停止日度捕获率计算 (四次产生四个互相矛盾的结果, 含符号相反), 把 humanoid cluster 的更新频率从每日降为事件驱动 —— 仅在 (1) Optimus/Cybercab 拿到具名客户订单或具名交付量 (非时间表承诺)、(2) 任一 ETF 持仓重大变更或 AUM 显著上量、(3) UBTech/Unitree 订单或 IPO 进展 时激活。** 10/22 就已写下的结论 (「可及载体是 TSLA 本身, 三只提供人形行业 beta 不是 Optimus alpha」) 在之后三次实验中没有改变, 只是增加了噪音样本。||**另一条修正: 10/27 记录的「humanoid 叙事受益者不在三只 ETF 里」—— 当天把 MU +2.77% 部分归因于 Musk「机器人需要的内存比地球上其他一切加起来都多」的表态。今天没有任何机器人新闻, 而 MU +4.28%, 完整解释是 SK Hynix 的订单簿。因此 10/27 那条归因应下调置信度: 当天 MU 的涨幅更可能也是内存板块自身的, Musk 表态是同日巧合而非驱动。**||**修正后的核心结论: groups.yaml 写明的错配 (「内容最纯的中国减速器供应链买不到, 买得到的内容最稀」) 在价格层面的表现不是「叙事利好流向有当期收入的一端」, 而是更简单的一件事 —— 人形叙事目前在任何可交易标的的日度定价里都不是主要变量。TSLA 的 +12.30% 是 Robotaxi + SpaceX 合并, MU 的 +4.28% 是 HBM 订单, 三只 ETF 的约 +1% 是板块资金流。三者各自有独立驱动, 人形叙事不在其中任何一个的第一位。**||数据质量: MA50 下方 -0.74% / 距 52w 高 -35.71% / 距 52w 低 +17.18% / 无 MA200 数据。**30 天几乎走平而全部在 MA200 下方或接近 = 流动性枯竭下的横盘, 不是筑底。单日上量不改变「该标的日度价格信息含量低」的判断。** 90 天内三只零个硬催化剂 (它们是 ETF, 没有财报)。

**Sources.**
- (aggregated): Is China Winning the Robotics Race? See Through the ETF Lens

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-10-22 · -0.71% day · ▼ minor
**Tags:** `flow_event`, `sector_rotation`
**Confidence:** low

**Primary cause.** **🔴 量比 0.11x —— 全书记录以来最低的单一读数，而且是连续第二份报告腰斩。** 10/15 记录的是「CROB 量比 0.21x 全书最低 + 30d -17.85% 最差 = 流动性枯竭」; 今天降到 **0.11x**，又腰斩一次。||**在这种成交量下，CROB 今天的 -0.71% 完全没有信息量: 它不代表中国机器人标的抗跌，只代表今天几乎没有人交易它。** 本条归因的 confidence 定为 **low**，不是因为找不到原因，而是因为价格本身不可解读 —— 这是诚实的分类，不应为了叙事完整而升级。||**对一个 ETF 而言，0.11x 的持续低量是一个独立于标的内容的风险**: 买卖价差扩大、折溢价偏离净值、极端情况下的清盘可能。这与中国机器人行业的基本面无关，是产品层面的风险。||5d **+6.89%** 为本组最强、30d -11.20% 为本组最差 —— 这两个数字在 0.11x 量比下同样不可解读。||位置: 距 52w 高 $33.01 为 -41.13%; 距 52w 低 $18.11 为 +7.3%。

**Sources.**
- {"type": "computed", "title": "\u91cf\u6bd4 0.11x \u4e3a\u5168\u4e66\u6700\u4f4e; 10/15 \u4e3a 0.21x \u2014 \u8fde\u7eed\u4e24\u4efd\u62a5\u544a\u8170\u65a9", "publisher": "workspace"}
- {"type": "computed", "title": "0.11x \u91cf\u6bd4\u4e0b 1d/5d/30d \u4e09\u4e2a\u53e3\u5f84\u5747\u4e0d\u53ef\u89e3\u8bfb; confidence \u5b9a\u4e3a low \u662f\u5206\u7c7b\u800c\u975e\u5931\u8d25", "publisher": "workspace"}

**Cross-assets.** SPY -1.44% · VIX 19.37 · TEN YEAR 4.957 · TWO YEAR 4.65 · WTI 99.19 · DXY 101.6 · GOLD 4055.4 · BTC 81063

**Agent read.** CROB 的价格已经失去信息含量。应记录的不是今天跌了多少, 而是流动性枯竭本身已经成为一个独立的产品层面风险 (价差、折溢价、清盘可能), 与中国机器人基本面无关。不要用 CROB 的日内走势做任何判断。
 · Snapshot at `dashboard/2026-10-22.md`

---
### 2026-10-14 · -4.18% day · ▼ material
**Tags:** `macro_inflation`, `sector_rotation`, `flow_event`
**Confidence:** low

**Primary cause.** **30d -16.75% 是全书最差, 距 52w 高 $33.01 已 **-43.4%**。** 它是 humanoid 三只里「内容最纯」的 (中国机器人纯标的), 也是跌得最惨的 — **三只的跌幅排序 (CROB -16.75% < HUMN -8.83% < KOID -6.24%) 恰好是主题纯度排序的反向: 越接近主题核心, 跌得越多。这是「主题被弃」而非「主题被选择性定价」的形态。** 延续 10/01 已记录的「humanoid 全组不参与 + CROB 创新低」状态, 两周后未变且恶化。⚠️ **置信度 low 且价格可靠性最低**: state.yaml 已标注「AUM 极小、流动性差」, 今日量比仅 0.85x。一只流动性差的小 ETF 的 -16.75% 可能主要是买卖价差与申赎摩擦, 不应用于任何推断。全组背景: 同期 QQQ 30d +3.12% / MSFT +6.52% / META +27.58%, 而 humanoid 三只是 -6.24% / -8.83% / -16.75% — **这个主题在「AI 资本开支」叙事最热的一个月里是负收益**, 与 project_optimus_humanoid_thesis 记录的核心错配一致 (内容最纯的买不到, 买得到的内容最稀)。|| 宏观共因 (三个独立的因, 不可压成一个): **(1) 九月 CPI**: 同比 +3.7% (共识 3.6%)、环比 **+0.6% 为过去一年最高**。CPI = Consumer Price Index, BLS 每月发布的美国最主要通胀指标。环比年化约 7.4%, 远高于 Fed 2% 目标。timeline 在今天之前已记 Oxford Economics 的提示 — 九月调查窗口内柴油 +60 美分/加仑、汽油 +20 美分, 油价冲击会进入这份读数, 所以这个数字是可预告的。它接在 9/17 FOMC 转鹰 + 9 月纪要 (10/07 公布) 指向今年再加一次息 (市场当时只给 19%) 之上, 是纪要后第一个硬数据且站在纪要一边。**(2) ❗长端拒绝配合 — 本条必须作为限定随附**: CPI 超预期而 10Y -2.7bp / 30Y -3.8bp / TLT +0.66%。媒体口径写的是 'rate-hike jitters'、'rising bond yields', 债市当天的实际方向与之相反。所以今天的跌**不能用「当天利率上行」解释** — 实现通道是风险溢价 (VIX +10.48%) 与叙事, 不是折现率。这是本月第四次长端对本应推高它的消息不配合 (10/01 失败突破 / 10/02 非农利多无响应 / 10/08 诱因缓解不修复 / 今天 CPI 超预期不涨)。**(3) 横截面否证「加息打击高倍数股」的单一叙事**: 倍数最高的 TSLA (fwd PE 168x) 跌 2.15%, 低于倍数中等的MRVL (33.7x) -8.73%、SNOW (111x) -6.34%、GEV (37x) -6.20%。跌幅与 **30d 涨幅**的相关性明显优于与倍数的相关性(MRVL 30d +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小跌幅)。**今天卖的是一个月里的涨幅, 不是久期。** **⭐ 方法论变化 (改写前三份报告的限定)**: 10/05、10/07、10/08 三份归因都写了同一句「半量里的下跌属『没有买盘』而非『出现卖盘』, 方向可信幅度不可信」。**今天不成立**: 量比中位数 1.02x (10/08 为 0.48x / 10/07 0.79x / 10/05 0.49x), 17/32 过 1.0x (10/08 为 3/34), 放量集中在跌最多的标的 (GEV 1.65x / QQQ 1.53x / TSM 1.45x / KOID 1.39x / MRVL 1.31x / DRAM 1.30x)。**这是这轮下跌序列里第一个全参与度的下跌日 — 幅度本身开始带信息。** 反方限定仍要记: 跌最惨的 MRVL 量比只有 1.31x、MU 只有 1.04x, 「放量」是全场性的而非个别标的清仓。

**Sources.**
- 247wallst via yfinance (CPI 3.7% YoY vs 3.6% 共识; MoM +0.6% 年内最高): Trump Media and Rumble Decline 5% as September Inflation Runs Above Forecasts; Reddit Slides 2%
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- IBD via yfinance: Stock Market Today: Nasdaq Dives On Rate Hike Jitters, AI Woes; Taiwan Semi Earnings On Deck
- Yahoo Finance video (Baird 策略师 Ted Mortonson): CoreWeave, Intel, Micron, & other tech stocks are plummeting. Here's why.

**Cross-assets.** SPY -1.08% · QQQ -1.97% · IWM -1.93% · DIA -0.11% · VIX 16.87 (+10.48%) · TEN YEAR 5.190% (-2.7bp) · THIRTY YEAR 5.525% (-3.8bp) · TLT +0.66% · WTI +1.16% · BRENT $106.06 (30d +12.05%) · GOLD -1.23% · SILVER -5.81% · DXY 102.530 (+0.34%) · BTC -1.81% · ETH -3.40% · BREADTH 32 只中 26 跌 / 6 涨 (含 2 只反向) · VOLUME MEDIAN 量比中位数 1.02x · 17/32 过 1.0x (10/08 为 0.48x · 3/34)

**Agent read.** 


---
