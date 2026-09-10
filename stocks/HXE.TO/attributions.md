# HXE.TO attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-09-10 · +0.96% day · ▲ minor
**Tags:** `commodity_move`, `geopolitical_war`, `macro_oil`, `flow_event`
**Confidence:** low

**Primary cause.** **当日全场最重要的异常: WTI +8.16% 破 $103 (常规时段 +7.18%), 上游/综合油气全部收跌。** 供给冲击有两个来源: (1) 胡塞武装占领也门 Mocha 港 —— 紧邻 Bab el-Mandeb (曼德海峡), 红海南端咽喉、苏伊士航线必经点; 影响的是运输而非产量, 后果是运费与到岸价永久上移 (绕行好望角约多两周) 而非一次性产量缺口。(2) 沙特产量降至 623.8 万桶/日, 环比减少约 190 万桶/日, 为 1990 年以来最低 — 约占全球供给 2%, 远超 OPEC+ 常规配额调整量级。**数据缺口: 未取到官方来源说明原因是主动减产、设施受损还是出口受阻, 三者对持续时长含义完全不同, 故置信度 medium。** 为什么油涨股跌 — 四个解释按权重排序: ① **油价穿过 $100 后市场把它从『营收顺风』改读为『需求破坏 + 通胀 + Fed 加息』** (唯一能解释符号翻转的解释; 同日八月 PPI +5.4%、2Y +13.3bp、UBS 警示航司 Q3 盈利、加州柴油触及 $9.999/加仑系统上限)。② **能源股估值锚定长期油价 (通常 $65-80) 而非即期油价** —— 战争溢价内含回吐预期, 所以市场不按 $103 定价股票; 但折现率上升不可回吐。即期油价涨的是分子的短期项, 折现率涨的是分母的全部项。③ 涨到 52 周新高后的派发 (盘中形态 + CNQ 3.26x 成交量支持)。④ 加拿大特定因素 (TSX 收六周低点, 基本金属下跌)。 HXE.TO 侧: **成交量 4.61x 为当日最高, 且是唯一收涨的能源标的 (+0.96%)。** 但这个数据点与同板块矛盾 —— SU -0.13% / CNQ -1.07% (盘中 -1.53% / -2.63%)。它在 TSX 以加元交易, 加元当日走弱 0.42% 只能解释约 0.4 个百分点, 无法解释与 CNQ 之间近 2 个百分点的裂口。可能是收盘价印刷延迟, 也可能是 ETF 成分权重与这三只显著不同。**列为待核项, 不作为『加拿大能源整体收涨』的结论使用。**

**Sources.**
- CNN: [Global oil hits $108 per barrel while bond yields surge](https://www.cnn.com/2026/09/10/investing/oil-iran-war-diesel)
- Yahoo/MT Newswires: [Update: US Equity Indexes Fall as Hot Producer Prices, Soaring Crude Oil Boost Treasury Yields (WTI +6.3% to $102.06, Brent +6% to $107.23; drivers: Houthi seizure of Mocha near Bab el-Mandeb, Saudi output falling 1.9M bpd to 6.238M bpd, weakest since 1990)](https://finance.yahoo.com/economy/articles/us-equity-indexes-fall-hot-195114785.html)
- Yahoo: [TSX Closer: Index Falls to Six-Week Low As Base Metals Slide; Oil Surges on Middle East Supply Fears](https://finance.yahoo.com/markets/world-indices/articles/tsx-closer-index-falls-six-203057283.html)
- Yahoo: [Sector Update: Energy Stocks Decline Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-decline-afternoon-195829985.html)
- Yahoo: Why Did CVX, COP, VLO Stocks Jump To 52-Week Highs?
- _Corroboration:_ 时间序列排除『油是收盘后才涨』的技术解释: CL=F 常规时段从 $95.88 涨到 $102.76 (+7.18%), 盘后再到 $103.89。而 CVX 盘前最后价 $217.31、开盘 $217.40 (52w 高), 从第一根 K 线就被卖, 全天横盘无反弹, 收 $212.76 (盘中 -2.13%); SU 开 $70.00 收 $68.93 (盘中 -1.53%); CNQ 开 $52.15 收 $50.78 (盘中 -2.63%)。教科书 gap-and-fade。
- _Corroboration:_ 相关性翻符号的历史对照: 8/4 WTI -5.63% 至 $75.82 → SU -1.92% (正相关); 8/10 Hormuz 紧张油涨 → SU +4.61/CVX +4.17/CNQ +4.09 (正相关); 8/31 美伊交火 WTI +3.06% 至 $85.94 → SU +2.19/CVX +2.01/CNQ +2.28 (正相关); 今日 WTI +8.16% 至 $103.83 → SU -0.13/CVX -0.49/CNQ -1.07 (负相关)。前三次 WTI 都在 $75-86, 今天在 $103 — $100 是行为学门槛。
- _Corroboration:_ 矛盾数据点, 不采信为结论: HXE.TO +0.96% (vol 4.61x) vs 同期 SU -0.13% / CNQ -1.07% / CVX -0.49%, 且 TSX 整体收于六周低点。加元 -0.42% 的计价效应不足以弥合裂口。

**Cross-assets.** SPY -0.58% · VIX 17.84 · TEN YEAR 4.944 · WTI 103.83

**Agent read.** 记录理由是 4.61x 的异常成交量 (过阈值) 加上方向与板块矛盾, 而非幅度。置信度 low: 无法确定 +0.96% 是真实的资金流入还是数据印刷问题。**未来若再出现 HXE.TO 与 SU/CNQ 方向背离, 应回查此条判断是 ETF 构成差异 (可复现) 还是数据质量问题 (不可复现)。**
 · [Snapshot](snapshots/2026-09-10.md)

---
### 2026-08-04 · -2.59% day · ▼ moderate
**Tags:** `macro_oil`, `commodity_move`, `geopolitical_war`, `flow_event`, `policy_us`
**Confidence:** high

**Primary cause.** US and Qatar signalled progress on a draft US-Iran agreement, easing Strait of Hormuz risk. WTI fell -5.63% to $75.82, unwinding most of July's war premium. HXE.TO was the largest decliner and the ONLY energy name on elevated volume (1.39x) while single-name energy stocks traded quietly (SU 0.97x, CVX 0.73x, CNQ 0.60x).

**Sources.**
- Yahoo: [Oil Extends Losses After US, Qatar Signal Progress on Iran Draft Deal](https://finance.yahoo.com/)
- _Corroboration:_ Energy complex all lower but far less than crude: HXE.TO -2.59%, SU -1.92%, CVX -1.09%, CNQ -0.10%. HXE.TO had the largest decline AND the only above-average volume.

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** The volume signature here is the most actionable detail in the energy complex today. HXE.TO was the only energy holding to trade on elevated volume (1.39x) while every single-name energy stock was quiet. ETFs typically reflect allocator and asset-allocation flows; single names reflect trader flows. The read is that allocators have begun reducing Canadian energy exposure while traders in individual names are holding into earnings (SU tonight, CNQ 8/6). Allocators are usually earlier than traders. This matters because the underlying gap is large and measurable: crude has surrendered 96% of its July war premium (30d from a +25.9% peak to +1.2%) while the energy equities have surrendered under 15% of theirs. If crude holds near $75, fair value for the group is roughly 30d +3-6% reflecting real cash-flow improvement rather than geopolitical premium, implying meaningful catch-down risk. HXE.TO at 30d +10.5% therefore has roughly 5-8% of premium still to give back under a signed-deal scenario. Framing for the user: this is not a sell recommendation but a factual record that the SOURCE of energy's 30-day excess return is being removed, and that the first evidence of institutional repositioning appeared today in the ETF rather than in the single names.
 · Snapshot at `dashboard/2026-08-04.md`

---
