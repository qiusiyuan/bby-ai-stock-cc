# SKHY + DRAM/HBM 板块深度研究

## 估值概览

```compare
指标 | SKHY (SK Hynix) | MU (Micron) | Samsung (005930.KS) | DRAM ETF
当前价 | $160.3 (ADS) | $882 | ₩255,000 | $54.2
市值 | $1.14T | $997B | ₩1,674T (~$248B*) | ETF
Trailing PE | 23.3x | 19.9x | N/A | 24.4x
**Forward PE** | **4.0x** | **5.9x** | **3.9x** | —
距 52w High | -17.7% | -29.7% | -32.0% | -33.4%
距 52w Low | +10.1% | +753% | +293% | +107%
30d 回撤 | ~-5% (仅7天) | -18.1% | -27.5% | -22.0%
Put/Call ratio | 2.23 (看空) | 1.51 (偏空) | — | 0.71 (偏多)
下次财报 | 7/24 (7天!) | 9/25 | 7/31 | —
```

*Samsung 市值为整体集团含手机/家电/显示器/晶圆代工；纯半导体(DS)分部约占 50-60% 营收。

```callout info
**核心估值判断: Forward PE 4-6x 是 "极度便宜" 还是 "cycle-peak trap"?**

历史上 memory 股票在 forward PE 4-6x 时有两种结局:
1. **2017-18 DRAM 超级周期:** forward PE 从 4x 涨到 8x (股价翻倍) → 然后 earnings 崩 → PE "便宜"是假象
2. **2023-24 AI 周期启动:** forward PE 从 15x 压缩到 8x (市场不信) → 然后 earnings beat → PE 继续压缩但股价涨

**当前更接近哪个?** 取决于 HBM 是否真的 structural (非周期性)。这是 7/24 SK Hynix 财报要回答的核心问题。
```

## 新闻链 (时间线)

```timeline
7/17 盘后 | ⚠️ "China Unveils Powerful New AI Model" (Kimi K3) → DeepSeek flashback → NVDA/AMD/MU/TSM 盘后暴跌 ("AI bloodbath")
7/17 盘中 | "SK Hynix Is Today's Standout Chip Stock for an Unusual Reason" — KRX 休市 → ADS 成为唯一交易窗口 → 流动性集中推高
7/17 盘中 | "The Chip Selloff Has Gone Too Far — SOX Index Turns Positive" → memory 领涨反弹
7/17 盘中 | HSBC reaffirm SKHY as top semiconductor pick → +8% 反弹催化
7/17 盘中 | "Analysts Still See Massive Upside for SK Hynix — AI Cycle Isn't Done But Questions Remain"
7/17 盘中 | "Here's What Can End Micron's Stock Pain" — 下一个 catalyst 才能止血
7/17 盘前 | Jensen Huang dismisses Vera Rubin delay report → NVDA 试图稳盘
7/16 | "SOX Index Fell 16% in Less Than a Month" → 技术性熊市边缘
7/16 | Samsung -8.8% despite "promising 1,800% jump in profits" → profit ≠ HBM 份额
7/16 | "South Korean market's extreme volatility alarms regulators"
7/15 | MU -9.9% on CXMT/YMTC 中国扩产恐惧 + CoreWeave hedging memory prices
7/10 | SKHY Nasdaq IPO $149 → open $168 (+14%) — 美国史上第二大 IPO
7/09 | MU +8% Bernstein "memory very tight" + SK Hynix ADR 7x oversubscribed
7/07 | MU -7.4% Samsung prelim + SK Hynix $28B raise → "cycle-peak fear"
7/02 | MU -5.8% OpenAI efficiency → memory supply-glut headlines → Korean 全面崩
7/01 | MU -9.3% OpenAI efficiency + BofA bubble indicator → SOX -5%
6/25 | MU +15.9% Q3 FY26 blowout (rev $41.5B, adj GM 85%) → "next NVDA" narrative born
6/23 | MU -11.1% Korean crash + leverage unwind → "Brutal Tech Rout"
```

```callout danger
**⚠️ 盘后新事件: Kimi K3 (中国 AI 模型) 引发 "DeepSeek 闪回"**

"Wall Street plunges in AI bloodbath" — NVDA/AMD/MU/TSM 盘后全线下跌。这与 2025 年 1 月 DeepSeek 事件类似: 中国展示 AI 能力 → 市场恐慌 "如果中国不需要高端 HBM → 需求假设动摇"。

**但 DeepSeek 后的 history:** 2025年1月 DeepSeek 当天 NVDA -17%, memory -10-15%。但 3 个月后全部创新高 — 因为高效模型 = 更多推理 = 更多 GPU/memory 需求。如果 Kimi K3 也是 "更高效但不替代算力" → 又是 buying opportunity。如果是 "真正替代 US AI 领导力" → 不同。需要明天开盘验证。
```

## 数据链 (估值深度)

### SKHY 估值拆解

```kpi
ADS 价格 | $160.3 | IPO $149, 开盘 $168, 一度 $194
Market cap | $1.14T | 全球第二大 memory (仅次 Samsung 整体)
Trailing PE | 23.3x | 反映过去周期 trough 利润
Forward PE | 4.0x | 基于 consensus FY2027 EPS — 如果 HBM 持续
EV/Sales (est) | ~3.5x | 基于 HBM 收入 $50B+ 目标
52w range | $145.6 - $194.8 | 仅 7 天历史!
IPO 募资 | $26.5B | 美国史上第二大 (仅次 SpaceX)
Lockup | 90 天 (vs 标配 180) | 解禁 ~10月初
```

**为什么 forward PE 4x 可能是真便宜:**
- HBM 收入不是周期性的 — 每一代 AI GPU 需要更多 HBM (H100→H200→B200→Rubin 每代 2x)
- 供给 capex 即使 SK Hynix 花 $28B，新产能要 18-24 个月才 online
- CEO 公开声明 "2027 will be the worst supply shortage year in memory history"
- Samsung 掉队 = 双寡头格局 (SK Hynix + Micron)，定价权更强

**为什么 forward PE 4x 可能是 trap:**
- Memory 行业 forward PE 在 cycle peak 永远看起来便宜 (因为 forward earnings = peak earnings)
- 如果 AI capex 任何一家 hyperscaler 砍投入 → HBM 需求增速断崖
- 中国 CXMT/YMTC 在 conventional DRAM 扩产 → 即使 HBM 稳，conventional DRAM ASP 可能崩
- Kimi K3 类事件 → 如果推理效率提升 10x → 每 GPU 需要的 memory 量下降

### MU 估值拆解

```kpi
股价 | $882 | 距 ATH $1,255 回撤 -30%
Market cap | $997B | 接近跌破 $1T 心理关口
Trailing PE | 19.9x | 包含上一周期尾部低利润
Forward PE | 5.9x | 基于 FY27 consensus ~$150 EPS
MA50 | $934 | 当前在 MA50 以下 (偏弱)
MA200 | $483 | 远高于 — 长期趋势仍完好
Thesis-break | $650 | 当前 buffer +36%
Scorecard date | 9/25 | Q4 FY26 验证 "next NVDA" claim
```

**MU vs SKHY 估值对比:**
- MU forward PE 5.9x vs SKHY 4.0x → SKHY 更便宜
- 原因: Korean discount + IPO 初期定价保守 + HBM 纯度更高 (SK Hynix HBM 收入占比 > MU)
- MU 有 35% NAND 业务拖累混合估值; SKHY 的 HBM premium 更纯

### Samsung 为什么暴跌

```kpi
Samsung 股价 | ₩255,000 | 30d -27.5% — 跌幅远超板块
Forward PE | 3.9x | 看起来最便宜!
HBM 市占率 | ~15% | 落后 SK Hynix (~50%) 和 MU (~25%)
HBM3E 良率 | 50-60% (传闻) | vs SK Hynix 80%+
NVDA 验证 | 未通过 (HBM3E) | 结构性份额损失
```

**Samsung "便宜" 是 value trap:**
- 利润增长 1,800% (from trough) 但 HBM 份额在缩小
- "Samsung stock drops DESPITE profit jump" = 市场在定价 **结构性落后** 不是周期
- 如果 Samsung 不能通过 NVDA HBM4 验证 → 份额继续流向 SK Hynix/MU

## 板块整体画像

### 30d 回撤对比

```chart
@title MU vs SKHY vs DRAM ETF (normalized from SKHY IPO 7/10)
@xlabels 06-04,06-05,06-08,06-09,06-10,06-11,06-12,06-15,06-16,06-17,06-18,06-22,06-23,06-24,06-25,06-26,06-29,06-30,07-01,07-02,07-06,07-07,07-08,07-09,07-10,07-13,07-14,07-15,07-16,07-17
MU | 100.0,86.748,95.309,93.965,89.546,99.987,98.555,109.236,102.486,104.738,113.854,121.624,105.599,105.272,121.843,113.688,114.988,115.893,103.643,97.948,98.886,94.229,95.276,99.578,98.338,94.091,98.722,90.805,85.676,88.791 | 1d +3.64% · 30d -18.08%
SKHY | 100.0,90.679,115.422,105.029,90.655,95.524 | 1d +5.37%
DRAM | 100.0,84.916,92.116,91.111,87.321,99.117,98.95,108.174,103.683,106.469,116.758,122.861,105.358,106.438,117.032,109.406,109.498,112.405,100.244,92.283,98.569,92.222,94.429,97.96,95.951,87.215,93.196,87.367,79.665,82.785 | 1d +3.92% · 30d -21.98%
```

### Selloff 驱动因素分解 (6/23 → 7/17)

| 驱动因素 | 占比 | 证据链 |
|---------|------|--------|
| 1. AI demand slope 质疑 | 30% | OpenAI efficiency (7/1), Kimi K3 (7/17 after-hours), MSFT 自研 chip |
| 2. Supply-side overinvestment恐惧 | 25% | SK Hynix $28B raise, Samsung capex, CXMT/YMTC 中国扩产 |
| 3. 技术性 mean-reversion | 20% | MU 从 $103 → $1,255 (+1,118%) 一年内; 回撤 -30% = 正常 |
| 4. Semi sector rotation (非 memory specific) | 15% | SOX -16%, MRVL -36%, INTC -13% — 全板块无差别 |
| 5. 地缘/宏观 | 10% | 中国限制传闻, 韩国市场 bear market, VIX +19% |

### 谁在买/谁在卖

```kpi
SKHY put/call | 2.23 | 做空力量大 — 对冲基金在 bet 反弹失败
MU put/call | 1.51 | 偏空但不极端 — 机构在等 9/25 earnings
DRAM ETF put/call | 0.71 | 偏多! ETF 层面反而有人在建仓
MU volume ratio | 0.87x | 今天反弹量不充分 (< 1x)
DRAM ETF vol ratio | 1.71x | ETF 放量! 资金通过 ETF 进入
```

**解读:** 个股层面做空力量仍在 (SKHY 2.23 极高 put/call = 很多人在 bet IPO breakdown)。但 ETF 层面放量 + 偏多 = **机构在用 DRAM ETF 建底仓**，不想暴露个股敞口。这是经典的 "early accumulation via ETF" 行为。

## 核心问题: HBM 是结构性还是周期性?

```scenarios
结构性 (HBM 非周期) | 55% | SKHY → $200-250, MU → $1,100+ | 每代 GPU 需 2x HBM; 供给追不上; Samsung 无法追赶
周期性 (memory 本色) | 30% | SKHY → $130-150, MU → $700-800 | 2027 年供给上线 + hyperscaler 砍 capex → 传统周期回归
黑天鹅 (AI paradigm shift) | 15% | SKHY → $100, MU → $500 | 中国 AI 模型证明不需要 HBM → DeepSeek 2.0 剧本
```

## Catalyst 优先级

```timeline
7/18 (明天!) | Kimi K3 反应 — 开盘是否复制 DeepSeek 剧本? 关键看幅度和持续性
7/24 | SK Hynix Q2 earnings — HBM3E 收入占比、HBM4 时间表、NVDA 供货 guide
7/28 | SKHY next_earnings (yfinance 显示 7/28) — 可能就是同一个 7/24 KRX earnings 的 ADS call
7/31 | Samsung Q2 final — HBM yield 进展、份额变化
8/26 | NVDA Q2 FY27 — HBM 消费量 = 对 SKHY/MU 最终验证
9/25 | MU Q4 FY26 — "next NVDA" scorecard 验证
```

## 投资判断

```verdict hold
**整体 HOLD — 不加仓但不卖。** Forward PE 4-6x 在 HBM 叙事未被证伪前确实便宜。但三重逆风 (VIX 上升 + 中国 AI 事件 + 韩国 bear market 监管恐慌) 意味着短期还有下行风险。关键验证点是 7/24 SK Hynix Q2 — 如果 HBM 收入超预期 + 管理层确认 "supply shortage extending" → 加仓窗口打开。如果 in-line 或 disappoint → SKHY 会重新测试 $145 (52w low = IPO 低点区域)。
```

### 具体场景

```callout warn
**如果明天 Kimi K3 = DeepSeek 2.0 (开盘 -10%+):**
- 不恐慌卖出 — DeepSeek 历史: 当天 -17% → 3 个月后全部新高
- 但如果连续 3 天跌 + 卖方下调 → re-assess
- SKHY thesis-break $115 是安全线 (当前 buffer 28%)

**如果 7/24 SK Hynix beat:**
- 确认 HBM structural → SKHY 目标 $200-220 (thesis base case)
- MU 联动 → 9/25 scorecard 预期被抬高

**如果 7/24 SK Hynix miss/in-line:**
- "Dead-cat bounce confirmed" → SKHY 可能回测 $145-150
- 等更好价格再评估 entry
```
