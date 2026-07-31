# SKHY — ADS「折价」结构研究：结论是溢价 30%，不是折价

> **Research note** · 2026-07-31 · scope: 结构性定价 / 入场决策 / 反驳工作区既有假设
> 涵盖: ADS 比率验证 · 折溢价逐日计算 · 时区滞后校正 · lockup 真实条款 · 流动性与套利机制 · cornerstone 投资人风险 · 与 MU 的估值对比
> 下次 review: **2026-10-08（lockup 到期）**，或 SKHY 溢价收敛到 +10% 以下时

```callout danger
**这份研究推翻了它自己的立项前提。**

7/31 日报里我写下待研究项时的假设是：「SKHY 相对韩股**折价**，Fwd P/E 4.42x vs MU 5.4x，可能是 memory cluster 里性价比最高的入口」。

用 SEC 最终招股书确认 ADS 比率后重算：**SKHY 相对韩股是持续 +30% 左右的溢价，不是折价。** 上市以来 14 个交易日，经时区滞后校正后 **14/14 全部溢价**，均值 +32.3%，区间 +19.3% ~ +42.4%。

**「性价比最高的入口」这个结论是错的，方向完全相反。** SKHY 是这个 cluster 里最贵的入口。
```

## 为什么原来的判断会错

错误源于一个具体的技术遗漏：**没有验证 ADS 比率**。

7/31 我看到的是 SKHY $148.10 和韩股 1,718,000 KRW（≈$1,190）。直觉上 $148 远低于 $1,190，加上 Fwd P/E 4.42x（SKHY）vs 3.84x（韩股）看起来接近，就默认了「ADS 大致对应 1 股，且在折价」。

**实际比率来自 SEC 424B4 最终招股书（2026-07-09 定价）：**

> "Each ADS represents **one-tenth** of a common share (par value W5,000 per common share)."
> — [424B4 final prospectus](https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm)

**1 ADS = 0.1 普通股。** 所以正确的对标价格是韩股价 ÷ 10 ÷ 汇率：

| 项目 | 数值 |
|---|---|
| 韩股 7/31 收盘 | 1,718,000 KRW |
| USDKRW 7/31 | 1,442.96 |
| 每股美元 | $1,190.61 |
| **每 ADS 的 NAV（÷10）** | **$119.06** |
| **SKHY 实际收盘** | **$147.11** |
| **溢价** | **+23.6%** |

Fwd P/E 的对比也误导了我：4.39x（SKHY）vs 3.84x（韩股）—— 这两个数字本身就直接说明 SKHY **贵 14.4%**，我当时把它读成了「接近」。这是第二个独立的、当时就在手边的反证，我漏掉了。

## 逐日折溢价（上市以来全序列）

同日收盘对比（Korea 06:30 UTC / US 20:00 UTC，同一日历日）：

| 日期 | 韩股 KRW | NAV/ADS | SKHY | 溢价 |
|---|---|---|---|---|
| 07-10（上市） | 2,180,000 | $144.76 | $168.01 | +16.1% |
| 07-13 | 1,845,000 | $123.12 | $152.35 | +23.7% |
| 07-14 | 1,913,000 | $127.73 | $193.92 | **+51.8%** |
| 07-15 | 2,082,000 | $139.93 | $176.46 | +26.1% |
| 07-16 | 1,842,000 | $123.94 | $152.31 | +22.9% |
| 07-20 | 1,764,000 | $118.60 | $151.16 | +27.5% |
| 07-21 | 1,836,000 | $124.47 | $171.94 | +38.1% |
| 07-22 | 1,830,000 | $123.67 | $165.27 | +33.6% |
| 07-23 | 1,919,000 | $130.05 | $169.50 | +30.3% |
| 07-24 | 1,759,000 | $119.33 | $154.57 | +29.5% |
| 07-27 | 1,816,000 | $124.55 | $143.02 | +14.8% |
| 07-28 | 1,550,000 | $105.84 | $130.17 | +23.0% |
| 07-29 | 1,401,000 | $96.41 | $126.79 | +31.5% |
| 07-30 | 1,322,000 | $91.66 | $149.00 | **+62.6%** |
| **07-31** | 1,718,000 | $119.06 | **$147.11** | **+23.6%** |

**均值 +30.3%，最小 +14.8%，从未出现折价。**

### 时区滞后校正 —— 更严格的检验

同日对比有个方法论缺陷：韩国收盘（06:30 UTC）**早于**美国收盘（20:00 UTC）13.5 小时，所以韩股收盘时还没看到当天的美股走势。更公平的比法是把 SKHY 的 D 日收盘对标韩国 **D+1** 的收盘（那时韩国已消化美国信息）：

| | 同日对比 | 滞后校正 |
|---|---|---|
| 均值溢价 | +30.3% | **+32.3%** |
| 区间 | +14.8% ~ +62.6% | +19.3% ~ +42.4% |
| 溢价交易日 | 15/15 | **14/14** |

**两种算法都得出持续溢价，且滞后校正后溢价更高、波动更小。** 说明溢价是结构性的，不是时区错位的假象。

```callout warn
**这同时推翻了 7/31 日报里另一个判断。** 我当时写「7/31 韩股 +30% 而 ADS -0.6%，是严重脱钩」，并推断是流动性未同步。

滞后校正后的真相：**7/30 SKHY 先涨 +17.5%（$126.79 → $149.00），7/31 韩国开盘才补涨 +30%。韩股是在跟随美股，不是脱钩。** 两个市场对同一批信息（MSFT/AMZN 财报 + Samsung 指引）的反应只是隔了一个时区。

7/30 那天溢价冲到 +62.6% 的峰值，正是因为美股已经涨完而韩国还没开盘。7/31 韩国补涨后溢价回落到 +23.6% —— **这是溢价的正常呼吸，不是新的脱钩。**
```

## Lockup：日期确认，但它不是主要变量

**原假设：** 折价可能由 10/8 的 90 天 lockup 造成，若如此则不会收敛。

**确认的条款**（424B4，招股书日期 2026-07-09）：

> "We and certain of our affiliates may agree with the underwriters, subject to certain exceptions, not to sell, transfer or otherwise dispose of any ADSs, common shares or similar securities for a period of **90 days** after the date of this prospectus."

90 天自 2026-07-09 起 → **到期约 2026-10-07**（我原先估的 10/08 基本正确，差一天）。

**但 lockup 在这里几乎不重要，原因有三，且第三条是决定性的：**

**1. 这是 100% 增发（primary），没有老股东减持。** 股份从 711,075,500 增至 728,865,500，增量 17,790,000 正好等于发行量。募资 $26.5B 全部进公司。**没有 IPO 前股东在这次发行里卖出，所以没有"解禁后老股东抛售"的经典结构。** 这跟 SPCX 的情形完全不同。

**2. Lockup 覆盖的是发行人和"某些关联方"，条款措辞是"may agree"（可能同意），不是确定性表述。** 招股书摘要没有点名 SK square，也没有列出受限股东清单。真正的条款在 Underwriting 章节（p.176）和 "Shares Eligible for Future Sale"（p.151），这两节在我抓取的内容里被截断了 —— **这是本研究的一个明确数据缺口，我不做推断。**

**3. 真正约束大股东的不是 lockup，是韩国法律。**

> "the requirement under the Monopoly Regulation and Fair Trade Act that SK square Co., Ltd. ('SK square'), our largest shareholder, maintain ownership of **at least 20%** of our issued common shares"

这是《垄断规制与公平交易法》对控股公司的**长期持股要求**，不是 90 天的合约限制。发行规模被刻意压到只有 2.50% 就是为了满足这条。**一个永久性的法定持股下限，比任何 lockup 都更能限制大股东供给。**

```callout ok
**结论：lockup 假设不成立。** 10/07-10/08 不会有老股东抛售潮，因为(a)这是纯增发无老股减持，(b)最大股东受法定 20% 下限约束。

**所以"折价源于 lockup、不会收敛"这条推断从根上就不适用 —— 因为首先就不存在折价。**
```

## 溢价的真实来源：极薄流通盘 + 单向套利摩擦

既然是溢价，要解释的问题变成「为什么美国投资者愿意为同一份现金流多付 30%」。

### 流通盘只有公司的 2.44%

| 项目 | 数值 |
|---|---|
| 发行普通股 | 17,790,000 股 |
| 发行后总股本 | 728,865,500 股 |
| **美国线流通占比** | **2.44%** |
| 对应 ADS 数量 | 177,900,000 ADS |
| 发行价 | $149.00 / ADS |
| 募资总额 | ~$26.5B |

**约 97.6% 的股份留在 KOSPI，美国线是一个极小的独立池子。** 需求（想在美股账户买 HBM 龙头的美国机构和散户）撞上固定的小供给，价格必然高于 NAV。这就是溢价的第一性原因。

### 套利机制是单向可堵的

正常情况下 ADS 溢价会被套利抹平：买韩股 → 存入托管行 → 生成 ADS → 在美国卖出。但招股书明确警告反向路径受限：

> "If you surrender your ADSs in order to withdraw the underlying common shares, you may not be allowed to deposit the common shares again to obtain ADSs."

**存入端（创造新 ADS）如果受韩国外汇管制或托管协议限制，溢价就无法被套利消除。** 这是 ADR 溢价能长期存在的标准机制 —— 历史上韩国、台湾、印度的 ADR 都出现过长期两位数溢价，正是因为跨境存管有额度或审批限制。

具体的 ADS 创造额度写在 "Korean Foreign Exchange Controls and Securities Regulations"（p.153），我抓取时被截断。**这是第二个数据缺口，也是判断溢价能否收敛的最关键一环。**

### 溢价历史参照的诚实标注

我没有拉到韩国 ADR 长期溢价的历史统计数据来做定量对标。**+30% 是高还是正常，我无法给出有数据支撑的判断。** 只能说：溢价的机制（薄流通盘 + 单向套利摩擦）是清晰且可验证的，但「它会不会收敛到 +10%」这个问题我没有历史基准来回答。这是本研究的第三个缺口。

## ⚠️ 意外发现：Cornerstone 投资人正是本周爆仓的那只基金

这是本研究最重要的意外收获。

424B4 列出三家 cornerstone investors，表达了最多 **$7B**（占发行额 26%）的认购意向：

1. Baillie Gifford Overseas Limited
2. Coatue 管理的基金
3. **Situational Awareness Partners LP**

而 7/31 的新闻（Quartz，URL slug 直接确认基金名）：

> "Leopold Aschenbrenner's AI hedge fund collapses after margin calls — The fund, which peaked at **$45 billion** this month, was forced to sell leveraged bets on AI infrastructure stocks to Ken Griffin's **Citadel at a discount**"
> — [qz.com/situational-awareness-hedge-fund-margin-call-citadel-fire-sale-073126](https://qz.com/situational-awareness-hedge-fund-margin-call-citadel-fire-sale-073126)

**Situational Awareness = Aschenbrenner 的基金 = SKHY 的 cornerstone 投资人之一 = 本周被迫向 Citadel 折价抛售杠杆 AI 基础设施持仓的那只基金。**

```callout danger
**这条把两件原本无关的事连起来了，且对 SKHY 是特定的、当前的供给风险。**

**关键限定（必须诚实标注）：** 招股书明确说 cornerstone 的意向 **"not binding agreements or commitments to purchase"**（非约束性），所以我**无法确认 Situational Awareness 实际获配了多少 SKHY，甚至无法确认它是否真的买了**。招股书也没有显示 cornerstone 配额本身受 lockup 限制。

**但如果它确实持有 SKHY：**
- 一只被迫清算的基金，持有一个流通盘只有 2.44% 的标的
- 三家 cornerstone 最多认购 26% 的发行量 —— 相对于极薄的流通盘，任何一家的清仓都是巨量
- 强制卖家不看基本面，会砸价出货
- **这可能同时解释了 7/27-7/29 SKHY 的暴跌**（$154.57 → $126.79，三天 -18%）—— 当时正是该基金爆仓的时间窗口

**更大的结构含义：** 一只在一个月内从峰值 $45B 崩掉的基金，持有杠杆 AI 基础设施多头。这可能也是 7/27-7/29 整个 semi 板块「无公司层面利空」暴跌的真实主因（当时新闻原话："Memory stocks are cratering for the second straight session with no company-specific bombshell to blame"）。这条已记入 7/31 日报和 MU thesis。
```

**待确认（无法从当前来源解决）：** Situational Awareness 是否实际持有 SKHY、持仓规模、以及清算是否已完成。13F 不覆盖（外国私人发行人的 ADS 持仓披露有滞后且规则不同），最快的信号是 SKHY 的成交量异常。

## 与 MU 的估值对比 —— 修正后

原假设「SKHY Fwd P/E 4.42x vs MU 5.4x，SKHY 更便宜」。这个比较本身没错，但要放进正确的语境：

| | SKHY (US ADS) | 000660.KS (韩股) | MU |
|---|---|---|---|
| Fwd P/E | 4.39x | **3.84x** | 5.42x |
| Trailing P/E | 20.27x | — | 18.84x |
| 隐含市值 | **$1,045B** | **$845B** | $942B |
| 30d | — (上市仅3周) | -36.0% | -20.0% |
| 距 52周高 | -24.5% | -42.5% | -33.5% |
| 下次财报 | 2026-10-27 | 2026-10-26 | **2026-09-23** |

**三个独立指标一致指向同一结论：**
1. Fwd P/E：SKHY 比韩股贵 **14.4%**
2. 隐含市值：SKHY $1,045B vs 韩股 $845B → 贵 **23.6%**
3. 价格 vs NAV：贵 **23.6%**

**所以真正的排序是：韩股（3.84x）< MU（5.42x）< SKHY（4.39x 但含 24% 溢价，实际对应韩股的 3.84x + 溢价）。**

**如果目标是「买 HBM 短缺周期的最便宜入口」，答案是韩股 000660.KS，不是 SKHY。** SKHY 的唯一优势是美股账户可直接买、无需韩国券商和外汇手续 —— 这个便利性的定价是 +24%~32%。

```callout info
**注意 MU 的财报日期优势：MU 2026-09-23（yfinance 最新口径，比我原先记的 9/25 早两天），SK Hynix 2026-10-26/27。**

MU 先出数据，且 MU 有工作区预先承诺的 scorecard（GM ≥82%、rev ≥$43B、EPS ≥$27、HBM QoQ ≥+20%）。**MU 的财报是整个 memory cluster 在 9 月的唯一裁判，SKHY/韩股要多等一个月。** 这意味着 MU 仍然是这个 cluster 里信息效率最高的持仓 —— 它最早给出可验证的数字。
```

## 关键判断

```verdict watch
不买 SKHY。溢价 +30% 是结构性的（2.44% 流通盘 + 单向套利摩擦），不是待收敛的错价。真正的便宜标的是韩股，但美股账户买不到。现有 MU 持仓不动。
```

**1. 原立项假设完全错误，方向相反。** SKHY 不是折价而是持续溢价 +30%（14/14 交易日），不是「性价比最高的入口」而是最贵的入口。**教训：任何跨市场比价，第一步必须验证 ADS/ADR 比率，这是一次 SEC 文件查询就能解决的事。** 我在 7/31 报告里基于未验证的比率写了一条投资含义 —— 这个流程错误比结论错误更值得记住。

**2. Lockup 假设不适用。** 10/07 到期，但这是 100% 增发无老股减持，且大股东受韩国法定 20% 持股下限（永久约束）限制。**不存在解禁抛售的经典结构。** 与 SPCX 的 12/09 lockup 是完全不同的性质 —— SPCX 有真实的老股东和 IPO 分配盘要解禁，SKHY 没有。

**3. 溢价大概率不收敛，但我无法定量证明。** 机制清晰（薄流通盘 + 存管单向受限），但缺三个数据：ADS 创造的具体额度限制、韩国 ADR 长期溢价的历史基准、以及 Underwriting 章节的完整 lockup 条款。**在补上这些之前，"溢价会不会收敛"是开放问题，我不给结论。**

**4. Situational Awareness 的连结是当前最值得跟踪的单一风险。** 一只爆仓基金可能持有一个 2.44% 流通盘标的的大额头寸。这既是 SKHY 的特定下行风险，也可能是 7/27-7/29 整个 semi 暴跌的真实解释。**但因为 cornerstone 意向是非约束性的，我无法确认它实际持有 —— 这是推测，标注为 medium confidence。**

**5. 对现有持仓的操作含义：什么都不做。** 结论是「不买 SKHY」，而工作区本来也没有 SKHY 持仓。MU 持仓的逻辑不受本研究影响 —— 反而因为发现 MU 财报（9/23）比 SK Hynix（10/26）早一个月，MU 作为 cluster 信息入口的地位被加强了。

**6. 如果一定要在 memory cluster 加仓，排序是：** 韩股 000660.KS（3.84x，最便宜，但需韩国券商 + 外汇）> MU（5.42x，美股可买，9/23 最早给数据，有 scorecard）>> SKHY（含 +24~32% 溢价，无独立优势）。

## 重读触发条件

- **2026-10-07/08（lockup 到期）** — 验证「无老股减持 → 无抛售潮」这个判断。若 SKHY 在到期前后放量下跌，说明我漏掉了受限股东清单里的某方（Underwriting 章节缺口）
- **SKHY 溢价收敛到 +10% 以下** — 说明套利通道比我判断的通畅，需重新评估存管限制的实际约束力
- **SKHY 溢价扩张到 +50% 以上并维持** — 说明供需失衡加剧，届时韩股-SKHY 价差可能成为可交易机会（需先确认存管机制）
- **Situational Awareness 清算细节披露** — 若确认持有 SKHY 且尚未出清，是明确的短期下行风险
- **2026-09-23 MU Q4 FY26 财报** — cluster 层面的裁判日，会重设整个 memory 的估值基准
- **2026-10-26/27 SK Hynix Q3 财报** — SKHY 上市后第二份财报
- **补齐三个数据缺口** — 424B4 的 Underwriting（p.176）、Shares Eligible for Future Sale（p.151）、Korean Foreign Exchange Controls（p.153）三节全文。这是把本研究从「机制清晰但无定量」升级到「可定价」的必要条件

## 数据来源

- ADS 比率 / lockup / 发行结构 / cornerstone 名单：[SEC 424B4 final prospectus, 2026-07-10](https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm)（定价日 2026-07-09，发行价 $149.00/ADS）
- 完整申报记录：[SEC EDGAR CIK 0002120882](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002120882)（DRS 2026-03-24 → F-1 06-24 → F-1/A 06-30, 07-06 → F-6 07-01 → EFFECT + CERT + 8-A12B 07-09 → 424B4 07-10 → 6-K ×5）
- 价格 / 汇率 / 估值：yfinance via `scripts/fetch.py`（SKHY, 000660.KS, 005930.KS, MU, USDKRW=X），2026-07-31
- Situational Awareness 爆仓：[Quartz, 2026-07-31](https://qz.com/situational-awareness-hedge-fund-margin-call-citadel-fire-sale-073126)
- 相关工作区文档：[MU thesis](../../MU/thesis.md) · [MU 业务结构](../../MU/research/2026-06-23-business-structure.md) · [MU earnings scorecard](../../MU/research/2026-06-25-next-earnings-watchlist.md) · [2026-07-31 日报](../../../dashboard/2026-07-31.md)

## 未解决的问题（明确的数据缺口）

1. **ADS 创造的具体额度限制** — 决定溢价能否被套利消除。在 424B4 p.153「Korean Foreign Exchange Controls and Securities Regulations」
2. **完整 lockup 条款** — 受限方名单、carve-outs、是否有价格触发的提前解禁。在 p.176「Underwriting」
3. **韩国 ADR 长期溢价的历史基准** — +30% 是异常还是常态，需要历史统计
4. **Situational Awareness 是否实际持有 SKHY 及规模** — cornerstone 意向非约束性，无法从招股书确认
5. **DRAM 反垄断诉讼** — 424B4 披露 2026-06-25 加州北区间接购买者集体诉讼。本研究未评估其影响
