# ANT attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

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
