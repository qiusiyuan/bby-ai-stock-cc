# MSFT attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-10-28 · -0.06% day · ▲ material
**Tags:** `earnings_print`, `guidance_inline`
**Confidence:** high

**Primary cause.** **正常时段收 $531.01 / −0.06%, 盘后财报后 $543.12 / +2.28% (ET 17:08 快照; 另有来源报 +4.5% 与「over 2%」, 采用 Yahoo 的 +2.28%)。方向按盘后记。** 数据取自 Microsoft FY27 Q1 新闻稿 + SEC XBRL 10-Q 口径, 非媒体转述。||**FQ1 FY27 (7–9 月): 营收 $922.79亿 +19% / 营业利润 $459.15亿 +21% / GAAP 摊薄 EPS $4.92 +32% (剔除 OpenAI 投资影响的调整后 EPS $4.89 +18%) / 净利 $366亿 +32%。Microsoft Cloud $639亿 +30% 且在加速, Azure 营收 +48% (产品线口径 $331.65亿)。商业 remaining performance obligation +73% 至 $6,770亿。** 分段: Agents and Infra $767.95亿 +25% (营业利润 $405.58亿 vs $327.18亿 = +24%); Devices and Consumer $154.84亿 −3% (营业利润 $53.57亿), 其中 Windows OEM and Devices −22%。本季返还股东 $102亿 (股息+回购)。||**★与同日 GOOG 构成本工作簿最干净的一次对照 —— 同一个 7–9 月季度, 两家 capex 都翻倍, 而自由现金流符号相反。** MSFT: 经营现金流 **$580亿** (SEC XBRL `NetCashProvidedByUsedInOperatingActivities`, 10-Q 口径) / capex **$393.67亿** (`PaymentsToAcquirePropertyPlantAndEquipment`, 同比 $193.94亿 = **+103%**) → **自由现金流 +$186.33亿**, **capex ÷ 经营现金流 = 67.9%**, 本季债务发行口径为 0。GOOG: 经营现金流 $422.90亿 / capex $513.55亿 (+114%) → **自由现金流 −$90.65亿**, **比率 121.4%**, 同季另募 $411亿 外部资本。**同季自由现金流裂口 $277亿, 盘后裂口 11.7pp。**||**这把 10/22 建立的「内生融资 vs 需要外部资本」判别轴从定性推进到一个可每季计算的比率: capex ÷ 经营现金流是否小于 1。** 10/22 当时给 MSFT 的理由原文是「capex 全由内生现金流覆盖」—— 今天得到数字确认(67.9%), 而且是在 capex 本身翻倍的前提下。**关键修正: 区分变量不是「capex 的绝对金额」也不是「AI 需求强弱」(需求侧两家都在加速: Azure +48% / Cloud +103%), 而是现金流覆盖率。** 盘中报告 AI capex tab 写的判据是「MSFT 的 capex 指引是否仍声称由内生运营现金流覆盖」—— 方向对, 但度量应换成这个比率。||**★同日第三个样本是最强确认: ORCL +10.73%**, 理由(Investing.com 原文框架)是「eases AI spending worries by guiding **capex to peak this fiscal year** and **turning cash-flow positive**」。三个样本: MSFT (+103% capex / FCF 正 / 67.9%) → 盘后 +2.28%; ORCL (指引 capex 见顶 + 现金流转正) → **+10.73%**; GOOG (+114% capex / FCF 负两季 / 121.4%) → **−9.41%**; META (10/28 日内, capex 继续升 + 自 2012 年以来首次 FCF 为负) → −1.52% / 5d −12.44%。**市场定价的是「capex 的峰值在哪里」与「自由现金流的符号」, 不是 capex 的大小。**||**kill conditions 三条: #1「Azure 增速连续两季低于 20%」→ 被 +48% 且加速明确否定, 推得最远; #2「M365 Copilot 付费席位到 FY2026 末低于 1,000 万」→ 今天未披露席位数; #3「OpenAI 把大部分推理负载迁出 Azure」→ 今天无进展。** re_read_trigger「营业利润率低于 38% 而 AI capex 攀升且收入未加速」→ 本季营业利润率 49.8% 且收入加速, 未触发。||**未取到: capex 前瞻指引。** 电话会 17:30 ET (2:30pm PT) 开始, 新闻稿明确说明前瞻指引只在电话会给出。**要找的具体表述: capex 绝对金额是否仍在上调, 以及有无「优化节奏」「分阶段」「审慎」这类暗示放慢的限定词。ORCL 今天用「capex 见顶 + 现金流转正」换来 +10.73%, 这是市场明确标好价的路径 —— MSFT 若给出类似路径, 它与 GOOG 的差距会从「现金流符号」扩大到「终点可见性」; 若继续无上限上调, 区别会缩小到只剩覆盖率。**||read-through: **GEV** kill #1「hyperscaler 削减建设 >20%」被两家 capex 翻倍推得更远(利好), 但 GOOG 靠 $411亿 外部资本支撑 capex 正是「客户建得起但借钱变贵」的机制, 对 GEV 的机位转化问题是双刃; **SKHY/MU/DRAM** 得到来自两个独立最终客户的需求确认(Azure +48% 加速 + Cloud +103%), 直接支持 SK Hynix「售罄至 2029 / 缺口到 2030」; **AVGO** —— Alphabet 原文「TPU systems sales were also a meaningful contributor to revenue growth」是 AVGO custom ASIC 论点今天唯一的客户侧具名证据; **AMZN (10/29)** 观察指标应从「AWS 营业利润率(约 39%)」扩展为「AWS 利润率 + capex ÷ 经营现金流」, 它决定 121.4% 是 Alphabet 的个体选择还是 hyperscaler 普遍状态。||风控: thesis_break $310, 盘后 $543.12 缓冲 **+75.2%** (全组最宽之一)。盘中 MA50 上方 +3.16% 为 AI capex 组唯一, 30d +7.54%。

**Sources.**
- {"type": "filing", "title": "Microsoft FY2027 Q1 earnings press release (and SEC 8-K accession 0001193125-26-436149; XBRL 10-Q cash-flow tags)", "publisher": "Microsoft IR / SEC EDGAR"}
- (aggregated): Microsoft beats Wall Street estimates as Azure growth hits 48%
- Investor's Business Daily: Microsoft Tops Quarterly Estimates As Azure Growth Accelerates
- Investor's Business Daily: Dow Jones Futures: Microsoft Rises Late, But Google, ServiceNow And Fortinet Dive On Earnings
- Investing.com: Oracle eases AI spending worries, guiding capex to peak this fiscal year and turning cash-flow positive (ORCL +10.73%)

**Cross-assets.** n/a

**Agent read.** 


---
