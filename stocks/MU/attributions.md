# MU attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-07-02 · -5.77% day · ▼ material
**Tags:** `memory_pricing`, `ai_demand`, `hyperscaler_overcapacity`
**Confidence:** high

**发生了什么。**

MU -5.77%, DRAM ETF -9.4%, SK Hynix -17.5%, Samsung -14.4%, CoreWeave -14%, Nebius -17%, SanDisk -11%。这不是一个 ticker 跌，是整条 "AI 需要硬件" 叙事链在被 reprice。

**为什么跌 — 两条独立逻辑链在同一天汇聚:**

**逻辑链 A: OpenAI efficiency (7/1 发酵 → 7/2 Korean 确认)**

7/1 OpenAI 公布推理效率大幅提升。市场的推导路径是：
- 推理效率 ↑ → 同样的 AI workload 需要的 GPU 算力 ↓ → 需要的 HBM 容量 ↓
- 如果 AI 的 "产出/算力" 比在快速改善，那之前基于 "算力线性增长" 假设定价的 HBM 增速预期就太高了
- 7/1 美股先杀 (MU -9.3%)，但当天 Korean 盘只跌了 -3~6% — 市场一度解读为 "美国散户过度反应"
- 7/2 Korean 盘补跌: SK Hynix -17.5%, Samsung -14.4% — 本土机构用脚投票确认这不是 overreaction。这是关键拐点：不再只是美国人慌，韩国本土 (离 HBM 供给链最近的钱) 也开始卖了

**逻辑链 B: Meta Compute (7/2 新催化剂)**

7/2 CNBC Julia Boorstin 报道 Meta 将向企业出售 AI 算力 ("Meta Compute")，直接竞争 AWS/Azure/GCP/CoreWeave。市场的推导路径是：
- Meta 是过去两年 AI capex 最激进的 hyperscaler ($60B+/yr) — 如果连他们都有 **过剩算力需要对外卖**，意味着什么？
- 意味着: 当前这批 hyperscaler 的 GPU/HBM 采购已经 **超过了自身消化能力**
- 推导: 如果已买的都用不完，那未来新增订单的增速必然放缓 → MU/SK Hynix 的 HBM 出货量 growth slope 被 reprice
- CoreWeave -14%, Nebius -17% 是直接受害者 (他们的商业模式就是 "租 GPU 给企业"，现在 META 进场了)
- 但对 MU 的冲击逻辑不同于 CoreWeave: 不是竞争压力，而是 **"最大买家承认 overcapacity" 这个信号本身**

**两条链合在一起的 narrative:**

市场在 48h 内连续收到两个信号，都指向同一个结论 —— **AI capex cycle 可能比预期短 / HBM demand slope 比 MU Q3 blowout 暗示的低:**
1. 供给效率提升 (OpenAI: 用更少做更多)
2. 买方承认过剩 (META: 多到要卖给别人)

这不是 "MU 这家公司出了问题"，而是 "整个 HBM supercycle 的增速假设在被下修"。从 $1,255 ATH 到今天累计 -22.5%。

**为什么不是 panic / 为什么还能 hold:**
- Vol 0.69x — 三天连跌都没有机构 capitulation (vol > 1.5x 才算)，说明长线持仓者还没决定卖
- META 自己也跌了 -4.7% — 市场短期没把 "卖算力" 读成 positive，而是 "你承认 overbuilt"。但如果后续证明 Meta Compute 有真实 enterprise revenue，这个 read 会反转
- Thesis-break $650 仍有 +49% buffer
- 确认点: 7/16 TSM CoWoS 利用率 (供给侧真相) + 7/24 SK Hynix HBM 出货 guide (需求侧真相)

**什么会证伪这个 bearish narrative:**
- TSM 7/16 说 CoWoS 仍然 supply-constrained → 效率提升没有减少 real demand (只是 reduce per-query cost → 更多 queries → net demand up)
- SK Hynix 7/24 HBM guide 维持 / 上修 → overcapacity 是 Meta-specific 不是 industry-wide
- 若两者都确认需求强劲 → 这轮 -22.5% 就是错杀，反弹空间巨大

**Sources.**
- CNBC (Julia Boorstin): Meta wants to sell AI compute to enterprises — confirmed "Meta Compute" launch
- Motley Fool: CoreWeave -14%, Nebius -17% — "the most concerning part wasn't the size of the drops, it was who caused them"
- 247wallst / Yahoo: SanDisk Sinks 11%, Seagate Falls 7%, Micron Slides 4% on Memory Supply-Glut Fears
- 247wallst / Yahoo: Micron's CEO Says Even His Own Customers Couldn't See This Coming. Now He's Spending $200 Billion
- _Data:_ SK Hynix -17.47%, Samsung -14.37% (Korean session 7/2); 5d cumulative SK -16.6%, Samsung -16.0%
- _Data:_ DRAM ETF -8.96% vs MU -5.77% — ETF Korean weight 拖累更深

**Cross-assets.** SPY -0.54% · VIX 16.75 · 10Y 4.48 · SK Hynix -17.47% · Samsung -14.37% · DRAM ETF -8.96% · META -4.68% · CRWV -14% · NBIS -17%
 · Snapshot at `dashboard/2026-07-02.md`

---
### 2026-07-01 · -9.30% day · ▼ major
**Tags:** `ai_demand`, `memory_pricing`, `sector_rotation`
**Confidence:** high

**Primary cause.** OpenAI efficiency gains announcement reprices HBM demand slope; BofA bubble indicator same-day; SOX -5% broad semi selloff

**Sources.**
- market coverage: OpenAI efficiency gains hammer chip stocks; SOX slides 5%
- Yahoo: BofA Bubble Risk Indicator Shows Rising Risks For Tech, Semiconductor Stocks
- Yahoo: Micron Drops 8%, SanDisk Slumps 10%, Western Digital Falls 7% as Memory Stocks Pull Back
- _Corroboration:_ DRAM -9.9%, SK Hynix -3.4%, Samsung -5.8%, TSM -6.7%, AMD -5.2%, MRVL -7.7% — full sector sync

**Cross-assets.** SPY +0.08% · VIX 16.37 · TEN YEAR 4.47 · SKHYNIX -3.40% · DRAM ETF -9.90% · META +9.70%

**Agent read.** 8天内第二次-9%+暴跌(6/23: Korean unwind, 7/1: OpenAI efficiency)。关键区别: 6/23是技术性(leverage unwind), 7/1是叙事性(efficiency reduces demand slope)。但vol 0.5x仍然低=非机构capitulation。从ATH $1,255累计-16.6%。确认点: TSM 7/16 CoWoS利用率 + SK Hynix 7/24 HBM出货guide。在此之前是情绪定价。距thesis-break $650缓冲+61%。
 · Snapshot at `dashboard/2026-07-01.md`

---
### 2026-06-23 · -11.09% day · ▼ extreme
**Tags:** `memory_pricing`, `sector_rotation`, `ai_demand`
**Confidence:** high

**Primary cause.** Korean market crash 蔓延 + MU 被市场点名为板块代理 ticker (Nasdaq Tumbles as Micron, Chip Giants Lead Brutal Tech Rout)。但 vol_ratio 0.65 (低于平均) — 没有机构 capitulation；BofA/Wedbush 当日仍唱多 (Wedbush '"Buying Opportunity"'); Anthropic 协议未撤销。这是 30d +84.6% 涨幅的 mean-reversion，非基本面恶化。

**Sources.**
- Yahoo: [Nasdaq Tumbles as Micron, Chip Giants Lead Brutal Tech Rout](https://finance.yahoo.com/markets/stocks/articles/nasdaq-tumbles-micron-chip-giants-170022578.html)
- Yahoo: [Intel, Micron Among Winners as BofA Supercharges Semiconductor Outlook](https://finance.yahoo.com/technology/articles/intel-micron-among-winners-bofa-172016994.html)
- Yahoo: [Wedbush Sees 'Buying Opportunity' After Brutal AI Chip Stock Selloff](https://finance.yahoo.com/technology/ai/articles/wedbush-sees-buying-opportunity-brutal-171808102.html)
- TheStreet: [One Micron number could reshape entire AI trade narrative](https://www.thestreet.com/investing/stocks/mu-micron-stock-q3-2026-earnings-high-bandwidth-memory)
- _Corroboration:_ SK Hynix -7.56%, SanDisk -11%, WD -10%, DRAM ETF -12.62% — 全板块同步

**Cross-assets.** SPY -0.97% · VIX 18.75 · TEN YEAR 4.49 · SKHYNIX -7.56% · DRAM ETF -12.62%

**Agent read.** MU 是板块代理 ticker, 不是 idiosyncratic 风险。三个反转标志: (1) vol_ratio 0.65 = 散户/算法砸盘不是机构出货; (2) 卖方一致看多 + 重挫 = 经典分歧场景; (3) Anthropic 协议、HBM3E 独占、HBM4 leadership 全部未碎。下个决定性数据点是 Q3 earnings (TheStreet 框定为 'could reshape entire AI trade narrative')。距 thesis-break $650 仍有 +66% 缓冲。真正 capitulation 标志: vol_ratio 升至 1.5x 以上或卖方下调评级。
 · Snapshot at `dashboard/attribution-2026-06-23.md`

---
