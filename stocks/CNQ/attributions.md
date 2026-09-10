# CNQ attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-09-10 · -1.07% day · ▼ minor
**Tags:** `commodity_move`, `geopolitical_war`, `macro_oil`, `macro_rates`, `sector_rotation`
**Confidence:** medium

**Primary cause.** **当日全场最重要的异常: WTI +8.16% 破 $103 (常规时段 +7.18%), 上游/综合油气全部收跌。** 供给冲击有两个来源: (1) 胡塞武装占领也门 Mocha 港 —— 紧邻 Bab el-Mandeb (曼德海峡), 红海南端咽喉、苏伊士航线必经点; 影响的是运输而非产量, 后果是运费与到岸价永久上移 (绕行好望角约多两周) 而非一次性产量缺口。(2) 沙特产量降至 623.8 万桶/日, 环比减少约 190 万桶/日, 为 1990 年以来最低 — 约占全球供给 2%, 远超 OPEC+ 常规配额调整量级。**数据缺口: 未取到官方来源说明原因是主动减产、设施受损还是出口受阻, 三者对持续时长含义完全不同, 故置信度 medium。** 为什么油涨股跌 — 四个解释按权重排序: ① **油价穿过 $100 后市场把它从『营收顺风』改读为『需求破坏 + 通胀 + Fed 加息』** (唯一能解释符号翻转的解释; 同日八月 PPI +5.4%、2Y +13.3bp、UBS 警示航司 Q3 盈利、加州柴油触及 $9.999/加仑系统上限)。② **能源股估值锚定长期油价 (通常 $65-80) 而非即期油价** —— 战争溢价内含回吐预期, 所以市场不按 $103 定价股票; 但折现率上升不可回吐。即期油价涨的是分子的短期项, 折现率涨的是分母的全部项。③ 涨到 52 周新高后的派发 (盘中形态 + CNQ 3.26x 成交量支持)。④ 加拿大特定因素 (TSX 收六周低点, 基本金属下跌)。 CNQ 侧: 收盘 -1.07% 但盘中 -2.63%, **成交量 3.26x 为当日全部追踪标的最高** —— 3 倍量能配上从 52 周高位开盘一路走低, 是派发形态而非恐慌抛售。叠加 TSX 收于六周低点、基本金属下跌。USD/CAD +0.42% (加元走弱) 理论上对以美元计价销售的加拿大生产商有利, 因此汇率不能解释下跌。

**Sources.**
- CNN: [Global oil hits $108 per barrel while bond yields surge](https://www.cnn.com/2026/09/10/investing/oil-iran-war-diesel)
- Yahoo/MT Newswires: [Update: US Equity Indexes Fall as Hot Producer Prices, Soaring Crude Oil Boost Treasury Yields (WTI +6.3% to $102.06, Brent +6% to $107.23; drivers: Houthi seizure of Mocha near Bab el-Mandeb, Saudi output falling 1.9M bpd to 6.238M bpd, weakest since 1990)](https://finance.yahoo.com/economy/articles/us-equity-indexes-fall-hot-195114785.html)
- Yahoo: [TSX Closer: Index Falls to Six-Week Low As Base Metals Slide; Oil Surges on Middle East Supply Fears](https://finance.yahoo.com/markets/world-indices/articles/tsx-closer-index-falls-six-203057283.html)
- Yahoo: [Sector Update: Energy Stocks Decline Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-decline-afternoon-195829985.html)
- Yahoo: Why Did CVX, COP, VLO Stocks Jump To 52-Week Highs?
- _Corroboration:_ 时间序列排除『油是收盘后才涨』的技术解释: CL=F 常规时段从 $95.88 涨到 $102.76 (+7.18%), 盘后再到 $103.89。而 CVX 盘前最后价 $217.31、开盘 $217.40 (52w 高), 从第一根 K 线就被卖, 全天横盘无反弹, 收 $212.76 (盘中 -2.13%); SU 开 $70.00 收 $68.93 (盘中 -1.53%); CNQ 开 $52.15 收 $50.78 (盘中 -2.63%)。教科书 gap-and-fade。
- _Corroboration:_ 相关性翻符号的历史对照: 8/4 WTI -5.63% 至 $75.82 → SU -1.92% (正相关); 8/10 Hormuz 紧张油涨 → SU +4.61/CVX +4.17/CNQ +4.09 (正相关); 8/31 美伊交火 WTI +3.06% 至 $85.94 → SU +2.19/CVX +2.01/CNQ +2.28 (正相关); 今日 WTI +8.16% 至 $103.83 → SU -0.13/CVX -0.49/CNQ -1.07 (负相关)。前三次 WTI 都在 $75-86, 今天在 $103 — $100 是行为学门槛。

**Cross-assets.** SPY -0.58% · VIX 17.84 · TEN YEAR 4.944 · WTI 103.83

**Agent read.** 距 thesis-break $30 缓冲 +69.3%, 无风险信号。今天的机制变化是真实的 (常规时段油就涨了 7.18%, 时间序列排除技术解释), 但它是估值层面而非现金流层面 —— 三家公司在 $103 油价下的实际现金流显著改善, 只是市场不愿按此定价。反向读法更准确: 股票没跟涨意味着没把战争溢价计入价格, 溢价回吐时也不需要回吐。需要跟踪: 明日 CNQ 若继续放量下跌 = 派发延续; 量能回落且价格稳住 = 一次性换手。最有信息量的待补数据是沙特减产原因。
 · [Snapshot](snapshots/2026-09-10.md)

---
### 2026-08-10 · +4.09% day · ▲ medium
**Tags:** `macro_oil`, `geopolitical_war`, `earnings_post_print`, `sector_rotation`
**Confidence:** high

**Primary cause.** Hormuz 地缘 + CNQ 创纪录 Q2 并重启 oil sands 扩产。板块与 SU/CVX 同步 +4%。

**Sources.**
- news: Canadian Natural Resources (TSX:CNQ) Posts Record Q2 And Revisits Oil Sands Expansion
- news: Canadian Natural Resources (TSX:CNQ) Stock Still Looks Cheap As Its 294% Run Continues

**Cross-assets.** SU +4.61% · CVX +4.17%

**Agent read.** CNQ 30d +20% 领跑能源 cluster (记录 Q2 + 扩产)。growth discipline 叙事延续。


---
