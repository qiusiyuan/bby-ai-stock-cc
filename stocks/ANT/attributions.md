# ANT attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-11-20 · -10.90% day · ▼ extreme
**Tags:** `sector_rotation`, `macro_rates`
**Confidence:** high

**Primary cause.** **上市第二个交易日。盘中最低 $83.05 — 距 $83 发行价仅 5 美分 (52 周低点即为此价)。**||**两日形态**: 11/19 开盘 $111.50 即全天最高，盘中高 $113.31，四小时单边回落至 $97.42 收盘。今天从 $97.17 再跌 10.9% 至 $86.58。两日累计较开盘 −22.3%，较发行价仅剩 +4.3%。首日的「开盘即高点、全天消化」形态今天是直接延续，不是消化完成。||**与 11/18 记录的预测的关系**: 11/18 记录了预测「ANT 在挂牌后 8 周内至少有一次**收盘价**跌破 $83 发行价」，评分日 2027-01-14。依据是 SpaceX 用 5 周破发，而 Anthropic 大盘背景更差 / 表外义务更重 ($8,954 亿采购承诺) / 被动资金地板更弱，唯一有利项是定价已被压低 25%，故给 8 周而非 5 周。**第二个交易日盘中就触到距成立 5 美分的位置，但收盘口径未破，预测仍 pending。**||**估值无锚**: fPE −1,289x (为负)，九个月累计净亏损 $1,040 亿，无盈利支撑，纯叙事定价。||**对 11/19 判断的更新**: 11/19 的结论是「资金分流的对手方第一次来自板块外部 — 一个新上市的需求端标的」。今天这个判断需要修正: **需求端标的自己也在跌，分流叙事失去了对手方。** 钱不是流向 ANT，是流出整个 AI 复合体 (^SOX −8.12%)。七家配售方 (AMD / AVGO / GOOG / MU / MSFT / NVDA / TSMC Partners) 今天只有 GOOG 收正，其中三家处于破位状态 (GOOG / NVDA / MU)、一家在警戒带 (AVGO)。||**被动资金地板的时点**: 12/19 Nasdaq-100 年度重构 (~估计日期) 是最可能的第一个被动资金地板 — Nasdaq-100 不要求盈利。S&P 500 要求 GAAP 盈利 (前四季合计为正且最近一季为正)，以九个月 $1,040 亿净亏损短期内不符合。在 12/19 之前它没有其他买方结构。||**距预设 thesis-break $65 缓冲 +33.2%。**

**Sources.**
- Yahoo: [Anthropic Sinks 9% on Day Two as AI Selloff Deepens: Strategist Warns Against Chasing the IPO](https://finance.yahoo.com/)
- Yahoo Finance: [Nasdaq wipes out gains for the year as Anthropic IPO fails to quell AI nerves](https://finance.yahoo.com/)
- _Corroboration:_ 七家配售方今日仅 GOOG +0.04% 收正; SPCX −6.23% (ANT 是其最大算力租户)

**Cross-assets.** SPY -1.98% · QQQ -3.47% · SOX -8.12% · VIX 31.78 · 10Y 4.944 · WTI 83.05 · DXY 103.83 · GOLD 3519.1 · BTC 58988

**Agent read.** 预测的方向在第二个交易日就得到强支持 — 盘中距成立 5 美分。但收盘口径是设计上的保守选择，应继续按收盘评分，不提前判定。更重要的结构性更新是: ANT 作为分流对手方的角色在第二天就失效了，说明 11/19 观察到的不是资金在 AI 复合体内部重新分配，而是整体撤出的第一天。12/19 Nasdaq-100 重构是唯一已知的买方结构事件。
 · Snapshot at `dashboard/2026-11-20.md`

---
### 2026-11-19 · -12.60% day · ▼ extreme
**Tags:** `post_ipo`, `flow_event`, `sector_rotation`
**Confidence:** high

**Primary cause.** Anthropic (ANT) Nasdaq 挂牌首日。$83 定价 (区间 $70-78，上穿上沿 6.4%)，募资 $81.3B 为史上最大 IPO (超 SpaceX $75B)，全面摊薄估值约 $1.5 万亿。开盘 $111.50 (+34.3% vs 发行价)，盘中最高 $113.31，随后 18 根 5 分钟 bar 单边下行至 $94.04 低点，ET 13:44 报 $97.42 —— 较开盘 -12.6%，较首日高 -14.0%，但较发行价仍 +17.4%。形态为「开盘即高点、全天单边消化」，与 SpaceX 首日「开盘 $150 → 收盘 $161.11 继续走高」方向相反。三条回落成因按权重: (1) 大盘背景 —— 挂牌当天 SPY 跌破 200 日均线 (-1.11%，11/16 时还在 +0.44% 上方)、QQQ -2.40%、VIX +11.64% 至 27.42，而流通盘仅 5.4% 的新股没有被动资金地板接盘 (Nasdaq-100 重构要到 12/19，S&P 500 的 GAAP 盈利门槛以九个月 $1,040 亿净亏损短期内不符合); (2) 资金从同一池子抽出 —— 「Nvidia, Broadcom, and Micron stocks erase gains as Anthropic goes public」，三家 $260 亿配售参与方的盘中涨幅被完整回收 (AVGO 曾 +4.21% → -1.13% / TSM 曾 +3.11% → -1.37% / MU 曾 +6.63% → +0.07%)，市场的净判断是配售是支出而非资产; (3) 估值可观测性极差 —— 空方公允值 $1,500 亿 vs 定价 $1.5 万亿差一个数量级 (SpaceX 当时 Morningstar $7,800 亿 vs 目标 $1.77 万亿仅差 2.2 倍)，分歧宽到 10 倍时没有模型能锚定价格。交叉风险: $260 亿供应商无投票权配售的七家 (AMD/AVGO/GOOG/MU/MSFT/NVDA/TSMC Partners) 全部是跟踪标的，其中 NVDA (-0.55%) 与 GOOG (-0.74%) 同日首次跌破各自 thesis-break，MU (+8.58%) 在警戒带内 —— 若 ANT 跌破 $83，减值同时落在七家损益表上，而这个压力源不在任何一家的预设 kill condition 里。

**Sources.**
- Reuters: [Anthropic blows past $2 trillion in Nasdaq debut, tops SpaceX's June listing](https://www.reuters.com/)
- WSJ: [Anthropic IPO Live Updates: ANT Stock Opens at $111.50, Capping High-Stakes Offering](https://www.wsj.com/)
- Forbes: [Anthropic IPO Live Updates: Shares Fall Below $100 After Opening At $111.50](https://www.forbes.com/)
- Yahoo Finance: [Nvidia, Broadcom, and Micron stocks erase gains as Anthropic goes public](https://finance.yahoo.com/)
- Yahoo Finance: [Anthropic Jumps 17% in Record Nasdaq Debut but Fades From $111.50 Open; Alphabet Ticks Up, Amazon Dips](https://finance.yahoo.com/)

**Cross-assets.** SPY PCT -1.10% · QQQ PCT -2.40% · VIX 27.42 · NVDA PCT -1.18% · GOOG PCT -0.46% · AVGO PCT -1.13% · MU PCT +0.07% · TSM PCT -1.37% · AMD PCT -8.52%

**Agent read.** 
 · Snapshot at `dashboard/2026-11-19.md`

---
