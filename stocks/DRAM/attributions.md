# DRAM attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

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
