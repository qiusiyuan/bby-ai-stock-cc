# GEV attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-28 · -1.30% day · ▼ minor
**Tags:** `earnings_print`, `guidance_raise`, `m_and_a`
**Confidence:** high

**Primary cause.** **连续四天「零基本面定价」的记录今天终止, 而答案不在此前列出的任何一个候选假设里。** 四天的候选是: 客户信用通道 (Barron's 10/22 「Blame Meta」+「financing all the growth will be tough」)、「GEV 跟着 META 走」(10/27 已判定四样本两同两反、建议停止跟踪)、以及 10/27 的「Meta 选股权而非债务 = 绕开『客户发债变贵→建设放慢』通道, 对 GEV 是实质利好」(当时记为 confidence low、零口径支持)。||**今天的财报给出第四个: 机位预订转化率 (slot conversion)。** Q3 利润**近乎三倍**、backlog 达 **$1,967亿** 创纪录、**上调 2026 指引**、**扩大回购授权** —— 但新订单与新机位预订「**missed by a mile**」(IBD 标题原文)。BNP Paribas 的措辞更精确: 「meets high bar, but **slot conversions now in focus**」。GEV 的燃气轮机业务采用机位预订模式: 客户先付费锁定未来产能槽位, 之后再转为正式订单。问题不在已有 backlog, 而在 (a) 新增机位预订低于预期、(b) 已预订机位转正式订单的速度成为焦点。||**🔴 这个答案回溯证明 10/15 那天的判断是错的。** 当天 GEV 签 Venture Global 最高 $172亿 合同却跌 3.02%, 报道**自承「头条数字 > 确定承诺额」**, 而本工作簿当时记为「跌幅零基本面成分」。**「最高 $172亿」正是机位预订型合同的典型措辞 —— 上限大、确定承诺小。市场当天定价的正是今天财报确认的那个变量, 比公司披露早了 13 天。**||**共同形态 (与同日 SPCX、Brent-WTI 价差两条修正一起记): 三次错误都不是「数据看错」, 而是「在只有一个候选机制时, 把残差归因给了那个机制」。GEV 四天列出的三个假设全部围绕「客户融资」, 因为那是当时唯一在台面上的叙事。可操作纠正: 当一个标的连续多日无法归因时, 正确的记录方式是「无法归因」, 而不是在现有叙事里挑一个最接近的。本工作簿在 GEV 上连续四天做了后者。**||**kill condition 核对三条: #1「Hyperscalers (MSFT/GOOG/AMZN/META) 公开削减数据中心建设 >20%」今天方向仍相反 (Meta 为建设募股 $975亿 + backlog 创纪录 + 公司上调指引), 离触发更远; #2 (Wind 段 2026 亏损超 2025) 与 #3 (Power 段 margin 指引下调至 13% 以下) 今天公开报道层均未给出数字, 无法核对 —— 10/27 曾把 #3 标为今天要看的门槛。** **结论: kill-condition 错配第四次记录 (GEV 自身), 今天的缺口最具体 —— 三条里零条度量「机位预订转化率」, 而这恰好是公司自己的财报日被市场挑出来的那个变量。建议补一条: 「新增机位预订连续两季同比下降, 或已预订机位的正式订单转化率被管理层下调」—— 可直接从公司披露度量, 且它是 backlog 之外唯一能预示 backlog 未来方向的指标。**||**同日被忽略的实质变化: 以 $90亿 收购 Trench Group** (高压电网设备, 卖方 Triton Partners), 现金与债务各半, 预计 **2027 年末**交割。披露: 2028 预期营收 $19亿 / 调整后 EBITDA margin 约 36% / **13x 2028 调整后 EBITDA (协同前)** / backlog 与框架协议约 $50亿 / 夏洛特新厂 2027 年末开始生产 **765kV** 设备。三点: (1) **这是纵向整合而非扩张** —— 公告原文说明 Trench 是 GEV 的**既有供应商**; 在「交不出设备」的供应链环境里把上游买下来是对自身交付能力的投资, 与今天「机位转化速度」的问题直接相关; (2) **用 35.07x 远期 PE 的股权 (加债务) 买 13x EBITDA 的现金流, 倍数上增值 —— 但 $90亿 各半意味着约 $45亿 新增债务, 而这发生在 GEV 自己的客户正因融资成本推迟订单的环境里**; 同一份财报里「扩大回购授权」与「$45亿 新增债务」并存是资本配置的重新排序, 不是单向乐观; (3) 765kV 是电网硬件最高压一级, 对应数据中心集群与远端发电的长距离连接, 是 Electrification 段最靠 AI 需求的一块 —— 而产能要到 2027 年末。||**量比 1.77x 为全场第二高 (唯二过 1.5x, 另一只是同样出财报的 SKHY 1.79x)。put/call 1.14 全场第二高 (仅次于 TSLA 1.42)。** 10/26 曾录得 put/call 1.58 (全书最高) + 期权隐含 ±5.7%。**连续三份报告期权端持续买保护, 而今天是财报日 —— 财报日的高 put/call 通常在公布后快速回落 (事件风险解除); 若明天仍维持 1.1 以上, 说明保护买的不是财报而是后续的订单转化。**||价格: MA50 ($938.73) 下方 -5.89% / MA200 ($941.52) 下方 -6.16%, **两线相距仅 $2.79 几乎重合** (任何方向突破都缺乏技术缓冲)。距 52w 高 **-26.13%** / thesis_break $700 缓冲 **+26.2%** (10/22 曾压缩到 +17.6%)。**低于最低卖方目标价: JPM $1,150 低 23.2%, BofA $1,310 低 32.6%。**||今日对照结构: 一条标题把两个 cluster 直接对立 —— 「AI Power Stocks Fell 7% to 13% in a Week While Exxon and Chevron Just Hit Record Highs」。能源四只中三只距 52w 高在 3.2% 内, 而 GEV 距 52w 高 -26.13% 且双线下方。**「AI 电力需求」与「实物能源供给」被定价为两件完全不同的事: 前者是预期, 后者是当期现金流。**||需求侧新政策变量: 「CMS Energy CEO predicts data center 'progress' **after midterms**」—— 公用事业 CEO 自己把数据中心审批进度挂在 11/03 选举结果上。||**今晚 MSFT + GOOG 的 capex 指引对 GEV 的信息量大于 GEV 自己今天的财报, 因为 kill condition #1 的度量对象正是这四家。要找的具体表述: capex 绝对金额是否仍在上调, 以及措辞里有无「优化节奏」「分阶段」「审慎」这类暗示建设放慢的限定词。**

**Sources.**
- Investor's Business Daily: GE Vernova Stock Falls; 'New Orders And New Slots Missed By A Mile'
- Investing.com: GE Vernova meets high bar, but slot conversions now in focus: BNP Paribas
- (aggregated): GE Vernova profit nearly triples as backlog hits $196.7 billion
- GE Vernova (press release): GE Vernova reports strong third quarter 2026 financial performance, raises 2026 guidance, and increases share repurchase authorization
- StockTitan / MT Newswires: GE Vernova to Acquire Trench Group for $9 Billion
- (aggregated): CMS Energy CEO predicts data center 'progress' after midterms

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-10-27 · +4.67% day · ▲ material
**Tags:** `earnings_pre_print`, `unattributed`, `pt_change`
**Confidence:** low

**Primary cause.** **「零基本面定价」第四次连续记录, 这次在财报前一天。**||四次序列: 10/15 当日签 Venture Global 最高 $172亿 合同 + 年内两次上调指引, **跌 3.02%**; 10/22 公司零负面消息、财报还在六天后, **跌 11.11%** (量比 1.75x), Barron's 点名「Blame Meta」+「financing all the growth will be tough」; 10/26 唯一「新闻」是 BofA $1,310 目标价的连续第四天重复报道, **涨 4.92%**; 今天唯一消息面是财报前瞻, **涨 4.67%**。四天净变动 **-5.87%**。||今天检索到的唯一新公司事实是**科特迪瓦 372 MW 电厂订单**, 规模不足以解释 4.67%。前瞻口径三条: 24/7 Wall St 称 GEV 带着 **$1,760亿 backlog + 刚上调的指引**进财报而「股价一个月跌超 14%」; Motley Fool 指出真正重要的数字「以吉瓦计量」而非美元 backlog (有用的框架校正 —— 美元 backlog 含服务与价格, 吉瓦量度实际产能承诺); Insider Monkey 与 Foreign Policy Journal 都用 **66x 市盈率**作为主要反驳, 后者同时引用「2026 年 Q2 88% 的有机订单增长」。||**现货与期权今天给出相反信号: 股价 +4.67% 而 put/call 升到 1.34, 为全场第二高 (仅次于 QQQ 1.57) 且高于 10/26。** 财报在明天盘前所以含大量事件对冲成分, 但绝对水平在最后一天还在上升。||**kill condition 错配第四次记录, 今天方向第一次是反的。** #1 原文「Hyperscalers publicly cut data center buildout by >20%」—— 今天 Meta 不但没削减, 反而**为建设融资近 $975亿**, 这条触发器离触发更远了。更精确的版本: **Meta 选的是股权而非债务**, 等于绕开了 10/22 以来追踪的「客户发债变贵 → 建设放慢」通道, 对 GEV 是实质利好。这可能是今天 +4.67% 的真实机制, 但**没有任何口径明确这样连线**, 故 confidence 记 low。||技术位置: 价格同时在 MA50 ($942.64) 与 MA200 ($941.08) 下方 **5.05%** (两线相距仅 $1.56, $941-943 是技术共识位); 低于已知最低卖方目标价 (JPM $1,150) **22.2%**, 低于 BofA $1,310 **31.7%**。thesis_break $700 缓冲由 +22.2% 松到 **+27.9%**。||**「GEV 跟着 META 走」第三次样本, 应停止跟踪**: 10/22 与 10/23 同向 (约 1.5 倍放大), 10/21 与 10/26 反向, 今天 GEV +4.67% 而 META -1.64% **再次反向**。四样本两同两反 → 只能解释 10/22 那一天, 不能做预测。||⚠️ **归因限制: 10/28 GEV 自己出财报, 同日还有 GOOG 财报 + MSFT capex 指引 + FOMC。明天的单日价格是四件事的净值, 对任何 GEV 假设都不构成检验。** 要看的是财报内容: Power 段 margin 指引 (kill condition #3 门槛 13%) 与吉瓦口径的容量承诺。

**Sources.**
- Motley Fool: GE Vernova Reports Oct. 28. Here's the 1 Number That Matters More Than Its Multibillion-Dollar Backlog (Hint: It's Measured in Gigawatts).
- 24/7 Wall St.: The AI Power Bill Comes Due: Will GE Vernova's Q3 Earnings Prove Its $176B Backlog Is Real?
- Zacks: GE Vernova (GEV) Lands 372 MW Côte D'Ivoire Power Plant Order
- Foreign Policy Journal: GE Vernova Builds $176B Backlog But 66x Earnings Multiple Raises Questions

**Cross-assets.** SPY +0.57% · VIX 17.52 · TEN YEAR 4.993 · FIVE YEAR 4.84 · THIRTY YEAR 5.305 · WTI 100.66 · BRENT 110.07 · DXY 102.344 · GOLD 4075.9 · SILVER 54.45 · BTC 80650.73

**Agent read.** 四次连续零基本面定价, 四天净 -5.87%。最可能的新机制是「Meta 用股权绕开信用市场 → 客户建设能力未受约束 → 对 GEV 利好」, 但无口径支持故置信度 low; 它若成立会以 hyperscaler 直签 gas 容量的 PPA 公告形式出现, 而不是以股价形式出现。明天的价格不可归因, 只看 Power 段 margin。
 · Snapshot at `dashboard/2026-10-27.md`

---
### 2026-10-26 · +4.92% day · ▲ material
**Tags:** `unattributed`, `sector_rotation`, `earnings_pre_print`
**Confidence:** low

**Primary cause.** **「零基本面定价」第三次连续出现, 这次方向向上。** 10/15 -3.02% (当日刚签 Venture Global 最高 $172亿 + 年内两次上调指引, 跌幅零基本面成分); 10/22 **-11.11%** (量比 1.75x, Barron's 点名 "Blame Meta" + "financing all the growth will be tough"); 今天 **+4.92%**, 而唯一的「新闻」是 BofA 维持 Buy $1,310 —— **这是 10/21、10/22、10/23、10/26 连续四天的重复报道, 不是新动作。** 置信度只能给 low。||**从 10/06 高点到 10/23 低点, GEV 在 12 个交易日跌 20.8%, 全程零公司级坏消息, 而财报一直在前面没发生。** 今天收回约四分之一。||**🔴 今天最重要的发现是一个否证: 「GEV 跟着 META 走」这个 10/22 建立的关系断了。** 逐日核对 —— 10/21 META +0.47% / GEV +4.00% (同向但幅度差 8.5 倍); 10/22 META -6.98% / GEV -10.64% (✅ 同向, 1.52 倍); 10/23 META -0.96% / GEV -1.50% (✅ 同向, 1.56 倍); **10/26 META -1.88% / GEV +4.92% (❌ 反向)**。→ 相关性是间歇的, 只在 META 大幅波动日出现, **不能用来做预测**。今天 +4.92% 更可能与 INTC +4.04% 同类: 30d 已跌多 + 财报前定位。||**put/call 1.58 是全书 36 只最高 (TSLA 0.63 / SPCX 1.14 / MU 0.76 对照), 期权隐含单日 ±5.7%。** 财报前两天, 现货在涨而期权在买保险 —— 今天的上涨没有得到衍生品市场的认可。||**位置: 同时跌破 MA50 ($945.37, -9.55%) 与 MA200 ($939.48, -8.98%)**, 自 52w 高 $1,195.94 回撤 28.5%, 低于最低卖方目标价 (JPMorgan $1,150) **25.6%**。10 月卖方两次下调 (Susquehanna → $1,270 / JPMorgan → $1,150), 零次上调。||**🔴 kill condition 错配第三次记录。** 预设 kill condition 是「hyperscaler 削减建设 >20%」, 而实际发生的是: META 10/21 **上调** capex 指引下沿 (按预设判据为利好) + GEV 跌 20.8% 零公司消息 + Barron's 给出的原因是 "**financing** all the growth will be tough"。**预设覆盖的是「客户不想建」, 实际在定价的是「客户建得起但借钱变贵」** —— 后者不触发任何现有 kill condition, 却直接压 Power 段利润率 (backlog 保留但转化节奏拖长、定价权转移)。||**10/28 的结构性难题: GEV 财报与 MSFT/GOOG capex 指引 + FOMC + SK Hynix 同日 (五重叠加), 股价反应不可归因。** 唯一解法是提前写死判据, 并只用电话会表述判读自身那一侧: Power 段营业利润率 + 融资相关表述 + Wind 段 break-even (后者是当天唯一不被叠加污染的一项)。

**Sources.**
- 24/7 Wall St.: The AI Power Bill Comes Due: Will GE Vernova's Q3 Earnings Oct. 28 Prove Its $176B Backlog Is Real?
- ad-hoc-news.de: BofA keeps Buy rating for GE Vernova stock at USD 1,310 target (重复报道 10/21-10/26)
- Investing.com Canada: GE Vernova options signal 5.7% move on Oct. 28 earnings
- ad-hoc-news.de: Susquehanna trims target to USD 1,270 for GE Vernova stock
- TipRanks: Defiance launches AIBN, billed as the first US ETF for the Bonds Funding the AI Buildout

**Cross-assets.** SPY +0.71% · VIX 18.39 · TEN YEAR 4.99 · FIVE YEAR 4.82 · THIRTY YEAR 5.3 · WTI 101.32 · BRENT 115.3 · DXY 102.018 · GOLD 4027.5 · SILVER 53.97 · BTC 79704.67

**Agent read.** 低置信度上涨: 唯一「新闻」是连续四天的重复报道。真正的信息有两条 —— (1) 「GEV 跟 META 走」被直接否证, 该简化模型只能解释 10/22 那一天, 不能做预测; (2) put/call 1.58 全书最高说明衍生品市场不认可今天的上涨。AI 信用通道在 10/24-10/26 仍在恶化 (Fortune 称 AI 牛市论有核心经济缺陷 / Apollo 称大科技之外无利润回报 / AIBN ETF 挂牌 / Musk 放贷挤压警告), 所以 10/22 的具名原因没有任何反向证据。最优先的动作与价格无关: 修 kill condition, 补一条客户融资侧的条件 (Power 段利润率连续两季收缩 / 客户预付款比例下降 / 大型 PPA 延期)。
 · Snapshot at `dashboard/2026-10-26.md`

---
### 2026-10-22 · -11.11% day · ▼ extreme
**Tags:** `sector_rotation`, `competitor_news`, `earnings_pre_print`, `flow_event`
**Confidence:** high

**Primary cause.** **GEV 在它最大需求来源加大支出的那一天跌 11.11%，量比 1.75x (全场第二)，而财报还在六天后 (10/28)。** META 把 2026 capex 下沿从 $1,300亿**上调**到 $1,350亿 —— 而 GEV 预设的 kill condition 是「hyperscalers (MSFT/GOOG/AMZN/META) 公开削减数据中心建设 >20%」。**今天发生的事和那条触发器方向完全相反，价格却给出了本轮最大单日跌幅。**||具名归因毫无歧义: Barron's 标题 "GE Vernova Stock Is Down 10%. **Blame Meta.**"，副标题给出机制 "AI demand is off the charts, but **financing** all the growth will be tough."||**这是本 workspace 记录过的最干净的「零基本面成分」下跌，而且是第二次。** 10/15 记录过结构相同的一次: GEV 当日签下 Venture Global 最高 **$172亿**合同 (16 台 × 720MW 燃气电力岛 + 变压器，支撑 10GW)、年内两次上调指引、12 个月 +66.5%，**仍跌 3.02%**，当时的结论是「跌幅零基本面成分；市场不给上限定价，只给信用环境定价」。**今天是同一机制，幅度放大 3.7 倍。**||逐条核对今天 GEV 自身的消息: Barchart 财报前瞻称「将报告强劲 Q3 增长，受稳健需求与有利定价驱动」(正面); Zacks 称「GEV 盈利预期增长」(正面); 另一篇称「Q3 回调反映获利了结，AI capex 需求持续」(中性偏正)。**公司自身负面消息: 零。跌幅: -11.11% 带 1.75x 量。**||**这个区分决定了 10/28 财报有没有用，必须说准:** 若跌的是**需求** → 10/28 的订单、backlog、指引可以直接反驳。若跌的是**买方的融资能力** → 10/28 财报**无法反驳** —— GEV 可以报出完美 backlog，但市场担心的是「签了约的客户 (META / 数据中心开发商) 两年后还付不付得出钱」，这不在 GEV 的财报里。**所以 10/28 最大的陷阱是: 一份好财报可能换来继续下跌。10/15 已经出现过这个形状一次，今天第二次，10/28 是第三次机会。**||**同组外部确认传导是板块性的: Vertiv 一周 -14% / Bloom Energy -15% / GEV -11%** ("GE Vernova Sinks 11%, Vertiv 14%, Bloom Energy 15% in a Week as AI Power Stocks Slide")。三只都是 AI 电力/散热/发电设备，三只都没有公司负面消息。**板块同向且无个股消息 = 共同的折现变量在动；而今天那个变量已被排除为利率 (2Y -17.3bp / 10Y -18.1bp 是顺风)，所以只能是客户信用。**||**风控: 距 thesis_break $700 的缓冲从 10/15 的 +32.3% 压缩到今天的 +17.6% —— 一周压缩 14.7pp，是全书本周最快的。** vs MA50 ($954.13) 偏离 -13.7%; 距 52w 高 $1,195.94 为 -31.18%。||**触发器体系的缺口 (今天跨 NOK/GEV/META/SPCX 四个标的的同一个问题)。** kill condition 1「hyperscalers 公开削减建设 >20%」: 今天方向相反，且事件把它推得更远。kill condition 2「2026 年 Wind 段亏损超 2025 年、盈亏平衡推迟到 2028+」: 10/28 检验，今天无信息。**两条都不覆盖今天实际发生的事。建议补一条可观测的新 kill condition: 「任一已签约的大型数据中心客户公开推迟或重新谈判交付节奏 / 融资安排」。**||**对 10/28 的预先判别结构 (四件事同日: GEV 财报 + GOOG capex + MSFT capex + FOMC，当天价格是净效应，事后难归因，所以要预先定):** (a) GEV 财报好 + GOOG/MSFT capex 上调且明确由内生现金流覆盖 + GEV 涨 → 融资担忧被定价错了，10/15 与 10/22 两次零基本面下跌是机会; (b) GEV 财报好 + capex 上调 + GEV **仍跌** → 第三次确认「好消息不被定价」，此时 thesis_break $700 应当作真实路径而非理论值; (c) GEV 财报好 + GOOG/MSFT 暗示外部融资 → 融资担忧被证实，与 GEV 自身财报无关。

**Sources.**
- Barron's/Yahoo: [GE Vernova Stock Is Down 10%. Blame Meta. — "AI demand is off the charts, but financing all the growth will be tough"](https://finance.yahoo.com/m/e4c2f7ec-18d9-36a7-aeb7-f9dba40251f8/ge-vernova-stock-is-down-10%25..html)
- TIKR: [GE Vernova Sinks 11%, Vertiv 14%, Bloom Energy 15% in a Week as AI Power Stocks Slide](https://www.tikr.com/blog/ge-vernova-sinks-11-vertiv-14-bloom-energy-15-in-a-week-as-ai-power-stocks-slide)
- Barchart: [GEV Stock Earnings Preview: 将报告强劲 Q3 增长, 受稳健需求与有利定价驱动 (财报在 10/28, 今天未发)](https://www.barchart.com/story/news/8314748/gev-stock-earnings-preview-what-to-expect-from-ge-vernovas-q3-2026-report)
- {"type": "cross_stock", "title": "Vertiv -14% / Bloom -15% (\u4e00\u5468) \u540c\u5411\u4e14\u5747\u65e0\u516c\u53f8\u8d1f\u9762\u6d88\u606f \u2014 \u677f\u5757\u6027\u6298\u73b0\u53d8\u91cf", "publisher": "workspace"}
- {"type": "computed", "title": "thesis_break $700 \u7f13\u51b2\u4e00\u5468\u5185\u7531 +32.3% \u538b\u7f29\u5230 +17.6% (\u538b\u7f29 14.7pp, \u5168\u4e66\u672c\u5468\u6700\u5feb)", "publisher": "workspace"}
- {"type": "contradiction", "title": "kill condition\u300chyperscalers \u524a\u51cf\u5efa\u8bbe >20%\u300d\u4e0e\u4eca\u5929\u4e8b\u5b9e (META \u4e0a\u8c03 capex \u4e0b\u6cbf) \u65b9\u5411\u76f8\u53cd", "publisher": "workspace"}

**Cross-assets.** SPY -1.44% · VIX 19.37 · TEN YEAR 4.957 · TWO YEAR 4.65 · WTI 99.19 · DXY 101.6 · GOLD 4055.4 · BTC 81063

**Agent read.** 今天的跌幅完全来自外部传导，且传导的那条线是融资不是需求 — 这决定了 10/28 财报无法修复它。10/15 已验证过一次 ($172亿 合同当日跌 3.02%)，今天是第二次且幅度放大 3.7 倍。解锁条件不在 GEV 自己的财报里，而在同日 GOOG + MSFT 的 capex 指引是否提及外部融资安排。
 · Snapshot at `dashboard/2026-10-22.md`

---
### 2026-10-15 · -3.02% day · ▼ material
**Tags:** `partnership_news`, `sector_rotation`, `ai_demand`, `flow_event`
**Confidence:** high

**Primary cause.** **今天 GEV 是全书最清晰的一例「公司消息极好、股价仍跌」—— 跌幅里零基本面成分。** 当日与 Venture Global 签署最高 **$172 亿** 电力协议: 最多 **16 台 720MW 燃气电力岛** + 配套变压器设备, 支撑一个可达 **10GW** 的离网工业电力网络 (覆盖其 LNG 站点与潜在 AI 数据中心); Baker Hughes 是另一家供应商。年内公司已**两次**上调 2026 年营收与自由现金流指引, Power 与 Electrification 两段订单持续增长, 12 个月回报 (至 10/13) **+66.5%** vs S&P 500 +20.5%。股价仍跌 3.02%。||把五个输入分开列, 结论唯一: 两个强利好是**公司级**的 (订单 + 指引上调), 三个利空全部是**客户信用级**的 (Gartner neocloud 报告 / 数据中心融资成本审视 / 10/14 CoreWeave 债券通道的延续), **而股价跟了利空。**||**今天 AI 融资质疑第一次拿到三个相互独立的具名来源 (10/08 时只有 Burry 的口头警告)**: (1) **Gartner 研究报告** — 预测多数 neocloud (新型 AI 云服务商) 到本十年结束前将失去独立性; 当日 IREN -5% / CoreWeave -5% / Nebius -4%。(2) **Saxo Bank (Charu Chanana)** — 明确表态「尚无充分证据显示存在系统性 AI 信用危机」, 但同时承认「融资挤压可能打到供应链」。注意这是**反驳方**的表态: 连反驳者都承认传导路径存在, 只否认它已经发生。(3) **巴克莱** — 同时下调 Dell 与 HPE 至 Hold (Dell -8% / HPE -4% / Super Micro -5%), 理由明确不是需求崩塌, 而是「供应链里一股安静的力量一直在虚增服务器营收」, 即**内存成本上涨计入 OEM 营收但不带毛利**。另有两条框架层输入: BlackRock CEO Larry Fink 称「若美国数据中心建设停摆将把经济推入衰退」(并提到国债从 2000 年 $8万亿 到今天 $40万亿); Michael Burry 称痛苦交易可以持续、Mag 7 弱势可能加深「红色十月」, 点名 2000 年科技泡沫类比。**Fink 那句话的双向性值得单记**: 表面是警告不要停, 反过来读却承认了「美国经济增长现在实质依赖 AI 资本开支」—— 这正是空头论点的前提。支持方的辩护词可以直接改写成空头论点, 说明这个结构性依赖是双方共识, 分歧只在可不可持续。||**数据中心融资成本审视的第二组证据**: Cipher Digital -9% / Applied Digital -6%, 而广义数据中心基金几乎没动 —— 分化本身指出了哪些公司最暴露于「以未来租金抵押借款」的定价方式。||**这干净地暴露了 GEV 论点的结构: GEV 的订单质量取决于下单方的融资能力, 而不只取决于 GEV 自己的执行能力。** 16 台 720MW 燃气轮机的订单若对方融不到钱, 它就只是一份框架协议。⚠️ 报道自己点出了这件事 —— **「头条数字大于确定承诺额」, $172 亿是上限不是订单簿**。市场今天的定价方式和这条限定一致: **不给上限数字定价, 只给信用环境定价。** 所以 -3.02% 不是市场犯错, 是市场在对一个**条件性订单**打信用折扣。||**连续三个放量日是今天最该记的二阶信息**: 10/13 → 10/14 (量比 **1.65x**, 当日全场最大, Barron's 具名 CoreWeave 债券收益率) → 10/15 (1.23x)。GEV 不是在无量漂移, 而是有资金连续三天离场。配合 30d **-0.93%** (几乎平) 与 12 个月 +66.5%: **这是一个累积了大量浮盈的标的在一个具名叙事变化下开始被减仓, 而不是一个无人问津的标的在跟跌。**||10/28 是全年最高信息密度的一天, 且对 GEV 是双重的: **自己的 Q3 财报** (要回答 Venture Global 这类协议的确定承诺额究竟多少 + Power 段毛利率) 与**最大终端客户群的 capex 指引** (GOOG + MSFT) **同一天**到手, 外加 FOMC。||价格位置: $913.34, 已在 MA50 $965.16 下方 5.4%; 距 52w 高 $1,195.94 -23.6%; 距 `thesis_break_price` $700 缓冲 **+30.5%** (该线定义为熊市情景: Power 段毛利率 + Wind 段亏损导致预期崩塌); PE 27.91x。||**建议加入 focus 名单**: 连续三个交易日 (10/13、10/14、10/15) 进入阈值穿越名单, 连续三日放量, 10/28 财报在 13 天内。||**宏观共因 (今天的共因只有一个, 但它的形状是反直觉的).** 九月 PPI (Producer Price Index, 生产者物价指数 — BLS 每月发布, 衡量生产者卖出价格, 通常领先 CPI 一到两个季度) 环比 **+1.3%** (8月 +0.5% / 7月 +0.2%, 2022年3月 +1.7% 以来最大单月), 同比 **+6.3%** (2022年12月 +6.4% 以来最大年度涨幅); 核心 (除食品/能源/贸易服务) 环比 +0.5% / 同比 +5.0%; 商品 +2.6% 其中**能源 +10.8% / 汽油 +20.3%**。接在 10/14 CPI 同比 3.7% (共识 3.6%) 之后, 是连续两天的下游+上游双向确认。零售销售同时跳升、失业申领保持稳健 —— 三项数据同向意味着经济不弱而价格在涨, 这是加息路径最不利的组合。||**❗但长端的反应方向和教科书相反, 本条必须作为限定随附**: 3M (^IRX) 4.088% **仅 +0.3bp**, 5Y 4.903% **-8.9bp**, 10Y 5.089% **-10.1bp**, 30Y 5.424% **-10.1bp**, TLT +1.52% (5d +2.85%)。**前端一动不动而 5年到30年平行下行 10bp —— 这个形状不可能是 Fed 政策定价 (政策定价必先动前端), 只能是对久期本身的避险需求。** 当天新闻口径直接说出了这件事 ('Tech slumps as AI financing worries grow, investors flock to bonds')。||**⭐ 方法论升级 (改写 10/05、10/07、10/08、10/14 四份报告的同一条限定)**: 那四天记录的都是「长端**不动**」—— 即对利空/利多都无响应, 属于零信息的否证, 只能说明「没有反证」。**今天长端第一次动了, 而且方向是下行**, 也就是折现率给了权益一个**顺风**, 权益却继续跌。结论因此从「无反证」升级为「有正面证据」: 折现率通道今天是负贡献 (利好), 跌幅必须由风险溢价**全额**解释。||**横截面否证「加息打击高倍数/长久期股」—— 本周第三次**: PE 从 SKHY 9.74x / DRAM 9.84x / MU 12.79x 一直到 AMD 148.2x / PLTR 172.0x / TSLA 340.0x, 跨 35 倍; 跌幅区间只有 -0.26% ~ -4.14% 且与倍数**无关** (TSLA 340x 跌 1.84% 却轻于 DRAM 9.8x 的 3.18%)。真正把跌幅排序出来的是「是否在 AI 供给/融资链上」。||**参与度限定 (与 10/14 相反)**: 38 只标的量比中位数 **0.755x**, 仅 11 只过 1.0x, 4 只过 1.5x。10/14 为中位数 1.02x / 17-of-32, 当时记为「本轮下跌序列第一个全参与度日」—— **一天后没有延续, 那是一个点不是趋势**。且今天放量的位置极度集中在韩国两条本线 (2.06x / 1.96x) + DRAM ETF (1.55x) + TSM (1.52x 财报日), 美国大型科技几乎无成交 (MSFT 0.54x / AMZN 0.54x / TSLA 0.47x / GOOG 0.39x / META 0.36x)。**这是对一个特定位置的定向抛售, 不是广泛降风险。**||**指数层面第一次方向分离**: QQQ -0.61% (跌破 MA50 $726.34) vs Dow +0.86% vs IWM +0.74%, 裂口 1.47pp。前四个下跌日 (10/07、10/08、10/13、10/14) 都是全指数同向。30d 口径 QQQ +2.26% vs IWM -6.77% 裂口从 10/14 的 12.4pp 收窄到 9.0pp, **且是用纳指跌、小盘涨的方式收窄 —— 轮动而非普跌的硬证据**。落点新闻一致: Moderna +6% (资金流入医疗) / Walmart +3% (德银上调) / Opendoor-Zillow +7% (长端回落直接利好住房)。VIX 16.88 (+0.06%) 几乎零反应, 第五次确认「不是系统性恐慌」。

**Sources.**
- Barron's via Yahoo: GE Vernova and Venture Global Sign a Power Deal Worth Up to $17.2 Billion. Here's What's Firm — up to 16 gas-fired power islands of 720 MW each; headline number is bigger than the firm commitment
- Simply Wall St via Yahoo: GE Vernova (GEV) Is Down 5.5% After Major AI Power Deal With Venture Global – Has The Bull Case Changed? — up to 10 GW of future capacity
- Simply Wall St via Yahoo: Is GE Vernova (GEV) Undervalued After Raising Guidance And Landing Data Center Power Deals? — raised 2026 revenue and FCF guidance twice; 12m return +66.5% vs S&P 500 +20.5%
- Yahoo: Data Center Stocks Tumble as Financing Costs Draw Scrutiny: Cipher Digital Drops 9%, Applied Digital Falls 6%
- Gartner via 247wallst: AI Cloud Stocks Sink as Gartner Warns Most Neoclouds Won't Survive Independently
- {"type": "cross_stock", "title": "\u8fde\u7eed\u4e09\u4e2a\u653e\u91cf\u65e5: 10/13 \u2192 10/14 (1.65x, \u5f53\u65e5\u5168\u573a\u6700\u5927) \u2192 10/15 (1.23x); 30d -0.93% \u5bf9\u7167 12 \u4e2a\u6708 +66.5%", "publisher": "workspace"}

**Cross-assets.** SPY +0.09% · VIX 16.88 · TEN YEAR 5.089 · WTI 96.58 · DXY 102.101 · GOLD 4168.2 · BTC 82171

**Agent read.** 全书最清晰的「好消息日仍跌」样本 — 跌幅零基本面成分, 100% 客户信用传染。这干净地暴露了论点结构: 订单质量取决于下单方的融资能力。报道自己提示「头条数字 > 确定承诺额」, 市场的定价方式与该限定一致 — 不给上限定价, 只给信用环境定价。连续三日放量 + 12 个月 +66.5% 浮盈 = 浮盈标的在具名叙事变化下开始被减仓。10/28 财报与客户 capex 指引同日。


---
### 2026-10-14 · -6.20% day · ▼ major
**Tags:** `macro_inflation`, `sector_rotation`, `competitor_news`, `analyst_downgrade`
**Confidence:** high

**Primary cause.** **今天是 GEV 归因史上第三条传导通道的首次出现, 且这一条在性质上与前两条不同。** 已建立的两条: 9/08 +3.16% (量比 0.47x) 主导通道是**板块情绪** (核电转正: NuScale +13% / Oklo +7%); 10/01 +3.89% 与 10/07 -3.12% (量比 0.84x) 主导通道是**折现率 + 估值质疑** (「70% 涨幅后估值偏高」·「GEV 47x vs Eaton 29x」)。**今天 -6.20% 且量比 1.65x 为全场最大, 成因是具名的新通道: CoreWeave 债券收益率上行外溢到 AI 相关工业股** (Barron's 标题点名 GE Vernova / Vertiv / Eaton)。**为什么这条通道不同**: 10/07 的归因按久期框架把 GEV 归入「远 × 高确定性」象限, 原话是「订单真实 (backlog 在手) 但现金流落在未来 5-10 年, **分子不变**分母变大, 价格必跌」。**今天的信用通道攻击的恰恰是分子: 若 AI 数据中心融资成本上升, 下游燃气轮机与电网订单可能被推后甚至取消 — backlog 的「高确定性」这一半开始被质疑。从「贵」变成「订单可能不算数」。** 且注意 10Y 今天实际**下跌** 2.7bp, 而 GEV 跌 6.2% — 折现率通道与信用通道今天明确背离, 这是通道已切换的直接证据。**量能证据**: 1.65x 是 GEV 近期归因里第一次出现放量 (9/08 为 0.47x「全部持仓最薄之一」、10/07 为 0.84x「低于平均」)。**三次事件里只有今天有真实成交量 — 按 workspace 一贯量能判据, 今天的幅度可信, 前两次不可信。** **⭐ 10/07 留下的待核实项今天正好被测试**: 原文「一条反向证据待核实: 『GEV 订单簿只有 **20%** 来自数据中心, 这是看多理由而非风险』— 若口径准确, GEV 收入基础比『AI 电力纯标的』叙事所暗示的更分散」。**若订单簿只有 20% 暴露于数据中心, 一次客户侧信用恐慌不该产生 -6.20% 且全场最大放量。** 两种读法: (A) 20% 口径不准确或市场认为真实暴露度远高于 20% → GEV「分散收入基础」看多理由被削弱, 10/07 待核实项判为不成立; (B) 20% 口径准确, 今天是过度反应 → -6.20% 创造了与基本面脱节的价格。**无法今天裁决, 但有 14 天后免费到手的裁决点: 10/28 财报里 Power segment 的订单构成与客户集中度披露** (同时回答 watch_items 里的 Power segment margin 与 transformer/grid backlog 两项)。⚠️ 诚实限定: 只取到 Barron's 标题与摘要 (「CoreWeave 的债券收益率正在扰动 AI 基础设施股, 包括 GE Vernova、Vertiv 和 Eaton」), **CoreWeave 债券的具体收益率、价格或信用利差数字未能核实** (正文付费墙)。信用通道的存在有具名报道支持, 压力量级无法量化。**基本面与价格的张力 (这组数字解释为什么能跌 6.2%, 而不是矛盾)**: Q2 有机订单 +88%、总 backlog $1,760亿、单季 FCF 超 2025 全年; fwd PE 37.3x (trailing 约 66x)。**基本面越强、倍数越高, 对「订单能否兑现」的敏感度就越大 — $1,760亿 backlog 的价值等于订单金额乘以客户付款概率, 而今天被重定价的正是后者。高倍数 + 订单依赖客户融资 = 信用通道的完美传导目标。** 这正是 Barron's 把 GEV 与 Vertiv、Eaton 并列的理由。跌破 MA50 $967.25 (低 2.6%), 自 10/06 高点 $1,029.21 六个交易日回撤 -8.5%, 距 thesis_break $700 缓冲 +34.5%。同方向独立声音 (列为情绪背景非论据): Steve Eisman 警告 S&P 500 超 65% 已与 AI 挂钩、「我持有 NVDA 而我担心」(该报道标签含 GEV); AVGO CEO Hock Tan 发出 AI 投资警告 (Musk 回「No Crying in the Casino」); 10/08 已记的 Michael Burry「denial」说法。|| 宏观共因 (三个独立的因, 不可压成一个): **(1) 九月 CPI**: 同比 +3.7% (共识 3.6%)、环比 **+0.6% 为过去一年最高**。CPI = Consumer Price Index, BLS 每月发布的美国最主要通胀指标。环比年化约 7.4%, 远高于 Fed 2% 目标。timeline 在今天之前已记 Oxford Economics 的提示 — 九月调查窗口内柴油 +60 美分/加仑、汽油 +20 美分, 油价冲击会进入这份读数, 所以这个数字是可预告的。它接在 9/17 FOMC 转鹰 + 9 月纪要 (10/07 公布) 指向今年再加一次息 (市场当时只给 19%) 之上, 是纪要后第一个硬数据且站在纪要一边。**(2) ❗长端拒绝配合 — 本条必须作为限定随附**: CPI 超预期而 10Y -2.7bp / 30Y -3.8bp / TLT +0.66%。媒体口径写的是 'rate-hike jitters'、'rising bond yields', 债市当天的实际方向与之相反。所以今天的跌**不能用「当天利率上行」解释** — 实现通道是风险溢价 (VIX +10.48%) 与叙事, 不是折现率。这是本月第四次长端对本应推高它的消息不配合 (10/01 失败突破 / 10/02 非农利多无响应 / 10/08 诱因缓解不修复 / 今天 CPI 超预期不涨)。**(3) 横截面否证「加息打击高倍数股」的单一叙事**: 倍数最高的 TSLA (fwd PE 168x) 跌 2.15%, 低于倍数中等的MRVL (33.7x) -8.73%、SNOW (111x) -6.34%、GEV (37x) -6.20%。跌幅与 **30d 涨幅**的相关性明显优于与倍数的相关性(MRVL 30d +16.61→-8.73 · AMD +24.20→-5.73 · META +27.58→-3.27 vs AVGO 30d -6.17→-3.10 全组最小跌幅)。**今天卖的是一个月里的涨幅, 不是久期。** **⭐ 方法论变化 (改写前三份报告的限定)**: 10/05、10/07、10/08 三份归因都写了同一句「半量里的下跌属『没有买盘』而非『出现卖盘』, 方向可信幅度不可信」。**今天不成立**: 量比中位数 1.02x (10/08 为 0.48x / 10/07 0.79x / 10/05 0.49x), 17/32 过 1.0x (10/08 为 3/34), 放量集中在跌最多的标的 (GEV 1.65x / QQQ 1.53x / TSM 1.45x / KOID 1.39x / MRVL 1.31x / DRAM 1.30x)。**这是这轮下跌序列里第一个全参与度的下跌日 — 幅度本身开始带信息。** 反方限定仍要记: 跌最惨的 MRVL 量比只有 1.31x、MU 只有 1.04x, 「放量」是全场性的而非个别标的清仓。

**Sources.**
- 247wallst via yfinance (CPI 3.7% YoY vs 3.6% 共识; MoM +0.6% 年内最高): Trump Media and Rumble Decline 5% as September Inflation Runs Above Forecasts; Reddit Slides 2%
- Yahoo Finance: Nvidia stock sinks as chip sell-off deepens on hot inflation data
- IBD via yfinance: Stock Market Today: Nasdaq Dives On Rate Hike Jitters, AI Woes; Taiwan Semi Earnings On Deck
- Yahoo Finance video (Baird 策略师 Ted Mortonson): CoreWeave, Intel, Micron, & other tech stocks are plummeting. Here's why.
- Barron's via yfinance — 点名 GE Vernova / Vertiv / Eaton; 正文付费墙, 债券收益率数字未核实: CoreWeave's Bond Scare Is Spreading to AI-Linked Industrial Stocks
- Zacks via yfinance: GE Vernova (GEV) Registers a Bigger Fall Than the Market: Important Facts to Note
- via yfinance (10/13) — Q2 有机订单 +88%, 单季 FCF 超 2025 全年: GE Vernova (GEV): A $176B Backlog Meets a 66x Price Tag
- Benzinga via yfinance: Steve Eisman Warns S&P 500 Is One Giant AI Bet: 'I Own NVDA and I Worry'
- via yfinance AVGO news: Elon Musk Fires Back at Broadcom CEO Hock Tan's AI Investment Warning: 'No Crying in the Casino'
- {"type": "attribution", "title": "2026-10-07 GEV -3.12% \u2014 \u6298\u73b0\u7387+\u4f30\u503c\u901a\u9053, \u5e76\u7559\u4e0b\u300c\u6570\u636e\u4e2d\u5fc3\u4ec5\u5360 backlog 20%\u300d\u5f85\u6838\u5b9e\u9879", "publisher": "stocks/GEV/attributions.md"}

**Cross-assets.** SPY -1.08% · QQQ -1.97% · IWM -1.93% · DIA -0.11% · VIX 16.87 (+10.48%) · TEN YEAR 5.190% (-2.7bp) · THIRTY YEAR 5.525% (-3.8bp) · TLT +0.66% · WTI +1.16% · BRENT $106.06 (30d +12.05%) · GOLD -1.23% · SILVER -5.81% · DXY 102.530 (+0.34%) · BTC -1.81% · ETH -3.40% · BREADTH 32 只中 26 跌 / 6 涨 (含 2 只反向) · VOLUME MEDIAN 量比中位数 1.02x · 17/32 过 1.0x (10/08 为 0.48x · 3/34)

**Agent read.** 主导变量从分母 (折现率) 换到了分子 (订单确定性), 这个区别决定了该监测什么: 折现率通道看 10Y, 信用通道看客户融资成本, 而两者今天明确背离 (10Y -2.7bp vs GEV -6.2%)。若重复 10/07 的解释 (「估值高 + 利率」) 就会漏掉全部新信息。新增实时免费代理指标: CoreWeave 债券收益率 — 且与 SPCX 共用同一个压力表。


---
### 2026-10-07 · -3.12% day · ▼ material
**Tags:** `analyst_downgrade`, `macro_rates`, `sector_rotation`
**Confidence:** high

**Primary cause.** 估值质疑 + 利率双因子，无任何业务层面坏消息，量比 0.84x 低于平均。GEV 10/06 刚收在 $1,029.21 (30 天新高)，今天 -3.12% 跌破 $1,000 收 $997.09 — 典型『刚创新高即被估值质疑打下』形态。两条质疑同日出现且非常具体: 『70% 涨幅后估值偏高』与『GEV vs Eaton: 47x 还是 29x 更值』—— 把 GEV 的 47x 与 Eaton 的 29x 直接对标。传导机制是久期: 在 10Y 5.277% (Fed 9 月纪要偏鹰 + 本周 $1,190 亿国债供给) 环境下, 47x 对 29x 的差额需要更快增长证明, 而 GEV 的增长以多年 backlog 交付形式实现 —— 时间越远折现率伤害越大。按已记录的久期框架, GEV 属『远 × 高确定性』象限: 订单真实 (backlog 在手) 但现金流落在未来 5-10 年, 分子不变分母变大, 价格必跌。**对照 10/01: 当天 10Y 出现九月首次失败突破、久期资产全线反打时 GEV +3.89% — 今天的 -3.12% 与那天是同一机制的两个方向, 确认 GEV 当前的主导变量是折现率而非业务。** 当日久期筛选中 GEV 与 NOK -3.19% / SPCX -2.51% / META -2.38% 同侧 (远期叙事无当期对价), 对立面是 MU +4.06% / AMZN +1.42% (有当期现金流地板)。一条反向证据待核实: 『GEV 订单簿只有 20% 来自数据中心, 这是看多理由而非风险』—— 若口径准确, GEV 收入基础比『AI 数据中心电力』叙事更宽, 该用工业设备倍数而非 AI 概念倍数定价, 估值质疑力度会减弱; 需在 10/28 财报核实。技术面最该记的事实: **MA50 $966.26, 缓冲仅剩 3.19%** — 30 天来第一次压到 3% 以内, 比 thesis-break $700 (缓冲 +42.4%) 更有近期意义。10/28 是双重暴露日: 自身财报 (Power 段毛利率/backlog 增速/20% 口径) + 最大潜在客户 GOOG/META/MSFT 的 capex 指引 (需求侧) + FOMC 决议 (折现率, 直接作用于 47x)。三因子方向可相反 — 好财报+好 capex+鹰派 Fed 可能净为负, 当天价格无法单独归因, 须拆开读 (FOMC 盘中 2pm ET, 财报与 capex 盘后)。

**Sources.**
- via yfinance GEV news: GE Vernova (GEV) Stock Appears Overvalued Following Its 70% Run
- via yfinance GEV news: GE Vernova vs. Eaton: Which AI Power Stock Can Earn Its 47x or 29x Price?
- via yfinance GEV news: Only 20% of GE Vernova's Order Book Is Data Centers. Here's Why That's the Bull Case, Not the Risk.
- via yfinance INTC news: Stock Market Today, Oct. 7: Markets Edge Lower as Treasury Yields Surge
- via yfinance ^TNX news: Higher rates are pummeling consumer discretionary stocks — here's the damage: Chart of the Day

**Cross-assets.** n/a

**Agent read.** 


---
### 2026-09-08 · +3.16% day · ▲ material
**Tags:** `sector_rotation`, `macro_oil`, `executive_comment`
**Confidence:** medium

**Primary cause.** **没有公司级硬催化; 驱动是板块情绪 + 宏观间接项。** (1) 板块级: 核电情绪转正 — NuScale +13%, Oklo +7% (标题为『核电抛售终于见底了吗』), Bloom Energy 被纳入 S&P 500 后 +8%。这些都不是 GEV 的业务对标, 但同属『AI 数据中心缺电 → 发电与电网资产重估』主题, 而 GEV 是该主题唯一同时覆盖燃气轮机 + 电网 + 服务的美股纯标的。(2) 宏观间接: WTI 5 日 +8.3% — 能源资本开支与油价正相关, 燃气轮机订单是其一部分, 但传导以季度/年计, 不解释单日。(3) 人事: 从 Rivian 挖来 CFO。**注意 30 日仍 -2.49%: 这是从 8/17 高点 $1,079 回撤 -9.9% 后的反弹, 不是新高突破。且 vol 0.47x 为全部持仓最薄之一。**

**Sources.**
- 24/7 Wall St via Yahoo: NuScale Power Spikes 13%, Oklo Climbs 7%: Is the Nuclear Selloff Finally Exhausted?
- 24/7 Wall St via Yahoo: Bloom Energy Surges 8% as S&P 500 Swaps It In for Trade Desk
- Yahoo Finance: Rivian (RIVN) Loses its CFO to GE Vernova (GEV) Right in the Middle of its Biggest Bet Yet
- Yahoo Finance: GE's $12 Billion Bet on the Unsexy Industry SpaceX Is Trying to Disrupt
- _Corroboration:_ 反向叙事仍在扩散: 『SpaceX 进入燃气轮机业务 / SpaceX 是否会来抢 GEV 生意』这条 8/31 已记录, 本周继续出现且同时挂在 SPCX 与 GEV 的新闻流。

**Cross-assets.** SPY -0.48% · VIX 15.3 · TEN YEAR 4.8 · WTI 92.87

**Agent read.** 置信度 medium: 涨幅由板块情绪解释, 但情绪的三个来源 (NuScale/Oklo/Bloom) 都不是 GEV 的业务对标, 且 Bloom 的上涨部分来自指数纳入的机械买盘 — 因此传导链条比表面看起来弱。**关于 SpaceX 燃气轮机威胁, 需要一次明确的重量评估: 真实但时间尺度极长。** 支持担忧的理由: SpaceX 在高温合金、涡轮机械、量产制造上能力真实, 技术栈与燃气轮机重叠, 且已在发射服务上证明过一次打破传统制造业成本曲线的能力。反对现在就担忧的理由更强: (a) 燃气轮机的护城河不在制造而在服役记录与全球服务网络 — 电力公司采购 500MW 级机组的决策周期 3-7 年, 核心考量是 30 年寿命内的可靠性数据; (b) GEV 利润大头在 Service 段 (已装机机组的长期服务合同), 新进入者几乎无法侵蚀; (c) SpaceX 尚无任何燃气轮机产品、客户或订单公告。**结论: 现阶段影响情绪不影响基本面; 第一个需要重新评估的时点是 SpaceX 拿到第一个电力公司订单。** 估值: fwd PE 38.4x 在 10Y 4.80% 环境里不便宜, 且今天 +3.16% 在 0.47x 薄量上完成, 可持续性低于放量反弹。相对优势有一条本周新增: BoJ 加息预期使日股对手 (Mitsubishi Heavy 7011.T / Hitachi Energy 6501.T) 的汇率风险上升, 强化了 GEV 作为唯一美股纯标的的可投资性。10/28 财报的 backlog 增速与 Power 段利润率是 38.4x 的裁决点。距 thesis-break $700 缓冲 +38.8%。


---
### 2026-08-20 · -4.21% day · ▼ major
**Tags:** `sector_rotation`, `macro_rates`
**Confidence:** medium

**Primary cause.** Sector-wide behind-the-meter/power selloff (FTAI -7%, CAT -4%, Fluence/Bloom/Redwire/Ameresco all down) driven by duration squeeze on high-valuation AI-power names + defense-ETF (ITA -3.1%) drag; no company-specific bad news, $176B backlog intact

**Sources.**
- Yahoo: Behind-the-Meter Energy Stocks Fall Tuesday: FTAI Aviation Down 7%, GE Vernova Down 6%, Caterpillar Down 4%
- Yahoo: Fluence Energy, Bloom Energy, Redwire, Ameresco, and GE Vernova Shares Plummet
- _Corroboration:_ GEV $176B backlog intact; gas turbine boom offsets wind -40%; vol 0.52 = no panic. Still above MA200 $865.

**Cross-assets.** SECTOR ETF -3.12% · SPY -0.62% · VIX 15.85 · 10Y 4.7 · WTI 86.53

**Agent read.** Valuation drawdown, not thesis deterioration. Board-wide power/behind-the-meter beta on a duration-squeeze day; FTAI/CAT/Fluence confirm it is sector, not GEV-specific. Fundamentals (backlog, gas-turbine cycle) intact. MA200 $865 is the line that matters; break with PPA/backlog bad news = real risk. Distance to thesis-break $700 still +35%. Continuation of the 8/18 macro_rates + sector_rotation squeeze that also hit SNDK/MRVL/INTC.
 · [Snapshot](snapshots/2026-08-20.md)

---
### 2026-08-18 · -5.77% day · ▼ material
**Tags:** `sector_rotation`, `macro_rates`
**Confidence:** low

**Primary cause.** GEV −5.8%，情绪面而非基本面回调。公司自身新闻全是利好：$176B backlog（在增长）、核电 AI 协议、近期 +8.9%。今日下跌是被「AI 开支质疑 + AI Election Backlash」的 AI 基建板块情绪拖累 + 前期涨幅获利回吐。作为 AI 数据中心电力纯标的，被归入 AI 基建受害者一并抛售。距 thesis-break $700 缓冲 +45.3%，基本面无损。独立风险：Wind 段有头条称下滑 40%，目前被 Gas+Grid+核电强势掩盖，需跟踪。信心 low：无 GEV 公司级利空催化，纯板块情绪归因。

**Sources.**
- secondary: [AI Election Backlash Is Shaping Wall Street’s Stock Market Views](https://finance.yahoo.com/)
- secondary: [GE Vernova (GEV) Is Up 8.9% After Backlog Surges To $176 Billion And Nuclear AI Deal](https://finance.yahoo.com/)
- _Corroboration:_ GEV 自身消息利好，跌因板块情绪；同日 AI 基建/开支方普遍承压 (META −3.1, neocloud −5~7%)。

**Cross-assets.** SPY -0.52% · VIX 15.66 · TEN YEAR 4.71 · WTI 84.14

**Agent read.** 


---
### 2026-06-30 · +6.56% day · ▲ major · 创历史新高，突破 base target
**Tags:** `ai_demand`, `thesis_validation`, `new_high`
**Confidence:** high

**Primary cause.** GEV 收 +6.56% 到 $1,174.86，**创历史新高并冲破 base target $1,150 收在上方**。catalyst 明确：「AI-Driven Turbine Demand Propels GE Vernova, IBD Stock Of The Day, Toward All-Time High」——燃气轮机需求被 AI 数据中心电力叙事点燃。同日 risk-on（道指收新高）+ Q2 季末 window-dressing 助推。vol 0.87x 接近均值 = 有真实买盘，不是纯 beta。

**Sources.**
- Yahoo/IBD: [AI-Driven Turbine Demand Propels GE Vernova, IBD Stock Of The Day, Toward All-Time High](https://finance.yahoo.com/)
- Yahoo: [JP Morgan's Top 3 Stocks for 2026: The Halftime Scorecard](https://finance.yahoo.com/)
- Yahoo: [These 2 Industrial Giants Have Crushed Tesla's Returns Over the Last 12 Months](https://finance.yahoo.com/)

**Cross-assets.** SPY +0.79% · QQQ +1.70% · DJI 收历史新高 · vol_ratio 0.87 · 30d +12.0%

**Agent read.** **价格突破预承诺 base $1,150 = 触发 re-rate 决策点。** 按工作区规则，突破 base 不该被动持有，应主动重估目标价。当前判断：7/22 Q2 财报前把 base 暂调到观察区间 $1,150-1,250；财报若 Power margin guide ≥14% + SMR PPA 签约 → 正式上调 base 到 $1,350-1,400；若不及预期，$1,150 突破可能是 false breakout（季末 window-dressing 助涨需在 7/1-7/2 验证）。verdict 从 hold 降到 **trim**（momentum 顶不追高，可部分获利了结）。距 thesis-break $700 缓冲 +68%。
 · Snapshot at `dashboard/2026-06-30.md`

---

### 2026-06-29 · +5.49% day · ▲ major
**Tags:** `ai_demand`, `policy_positive`
**Confidence:** medium

**Primary cause.** GEV 收盘 +5.49% — SMR / 核电 / 数据中心电力 narrative 双重加分:Yahoo 'Nuclear Stocks And Small Modular Reactors Ace Big Wins. A DOE Deadline Looms' + 'SpaceX Has Real Value—But These 3 Stocks Have Better Odds Right Now' (GEV 被点名);Vol 0.87x 接近均值,有真实 flow。GEV 已和 SU/CVX/CNQ 解耦,driver 切换为 AI capex/SMR 而非油气。groups.yaml 已拆分:能源(油气) vs 电力/Grid。距 base target $1,150 还差 +4.3%。

**Sources.**
- Yahoo: [Nuclear Stocks And Small Modular Reactors Ace Big Wins. A DOE Deadline Looms.](https://finance.yahoo.com/)
- Yahoo: [SpaceX Has Real Value—But These 3 Stocks Have Better Odds Right Now](https://finance.yahoo.com/)

**Cross-assets.** SPY PCT +1.65% · QQQ PCT +2.49% · VOLUME RATIO 1D 0.87

**Agent read.** 
 · Snapshot at `dashboard/2026-06-29.md`

---
