# NVDA attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-08-28 · -3.31% day · ▼ material
**Tags:** `macro_rates`, `sector_rotation`, `competitor_news`
**Confidence:** medium

**Primary cause.** 低量(vol 0.75x)被动下跌, 无公司新利空, 两个外生因子: (1)久期回吐主因: Warsh 鹰派→10Y 逼近52w高→最高久期 AI 龙头随折现率上升被压; 同日 gold/silver/BTC 齐跌确认是'高久期/非美元资产被利率洗'的宏观通道; (2)MRVL read-across: MRVL beat+raise 仍暴跌-10% 把'好财报被卖'情绪传导到芯片端, 'End of the Lag 7?' 叙事质疑龙头估值溢价。财报已于8/26过、大beat确认, 5d仍+2.7%, 故今日非主动抛售是板块久期洗盘被动跟跌。

**Sources.**
- : 
- {"type": "reverse_check", "note": "vol 0.75x \u4f4e\u91cf + \u65e0\u4e2a\u80a1 headline \u2192 \u786e\u8ba4\u88ab\u52a8\u8ddf\u8dcc\u975e\u4e2a\u80a1\u4e8b\u4ef6"}

**Cross-assets.** SPY -0.19% · VIX 14.46 · 10Y 4.71 · DXY +0.47% · MRVL -10.32% · AVGO -1.22%

**Agent read.** medium: 宏观久期+板块 read-across 驱动非公司特定。距 break $150 缓冲+47%无近端风险。9/3 AVGO + 9/11 CPI 决定久期压力去向。


---
### 2026-08-27 · +9.19% day · ▲ major
**Tags:** `earnings_post_print`, `guidance_raise`, `prediction_failed`, `m_and_a`
**Confidence:** high

**Primary cause.** 财报次日确认: 8/26 regular -1.16% 收 $209.95 → 盘后 +4.56% → 今日(8/27) regular +9.19% 收 $228.93, 完全接住盘后涨幅并扩大, vol 1.67× 放量逼近 52w 高 $236。驱动: Q2 营收 $96.2B 创纪录(~同比翻倍), 下季指引 $108B, ~70% 增长指引压过财报里的 memory margin warning。叠加 NVDA $5B 入股 Intel(INTC +2.9%)+ 传收购 Hugging Face。同时对 debasement-regime prediction(8/20 记录)做次日确认打分: 事件层 FAILED 坐实(beat 换来 rally 并扩大), 结构层「反应受抑」被 +9% 推翻, 仅「倍数压缩」作为静态估值事实成立(fwd PE 15.8)。净: 预测可证伪部分全 MISS。

**Sources.**
- Yahoo/aggregated: NVIDIA Surges as 70% Growth Forecast Overrides a Memory Margin Warning
- Yahoo: Intel Jumps 3.6% as Nvidia's $5 Billion Entry Price Looks Tiny
- _Corroboration:_ 卖铲子链同向: TSM +2.3%, AVGO +3.6%, INTC +2.9%; 但 hyperscaler 未跟(GOOG -0.2/AMZN -1.6/META -0.8), MU -2.8% 逆势 → 需求确认利好供给侧, 非全 AI 普涨

**Cross-assets.** SPY +0.68% · VIX 14.64 · TEN YEAR 4.658 · FWD PE 15.8

**Agent read.** debasement-regime「好财报换不来好反应」在 NVDA 这种基本面强到能自造 catalyst 的名字上不成立 — 增长确定性压过折现率逆风。regime 压制对无当期盈利的长久期标的(SPCX/humanoid)更真实。真正 regime 生死判据在 9/11 CPI + 9/17 FOMC。


---
### 2026-08-26 · -1.16% day · ▲ major
**Tags:** `earnings_print`, `prediction_failed`, `guidance_raise`, `macro_rates`
**Confidence:** high

**Primary cause.** Q2 FY2027 印后盘后 +4.56% ($219.53, 盘中峰值 $226 = +7.8%),regular 先跌 -1.16% 再拉。实际数字: 营收 $96.2B 创纪录 (~同比翻倍,逼近 $100B),下季 guidance $108B (强),Amazon 芯片订单翻三倍。SCORE 8/20 debasement-regime prediction (score_date 今天): 预测「beat 但 fail-to-rally」= 事件层证伪 (beat+rally 兑现)。但结构层反而验证: 头条『利润翻倍,估值创 2019 年来新低』= 倍数压缩机制真实存在; 且『S&P 微跌尽管 NVDA favorable + Core PCE 稳定』= 好消息没抬起大盘。分裂裁决: 需要历史级 blowout 才换来 +4.5% 克制反应,正常 regime 该 +10-15%。

**Sources.**
- Yahoo/aggregated: Nvidia Posts Record $96.2B Revenue, Shares Jump on $108B Outlook
- Yahoo: Nvidia's Valuation Just Hit Lows Not Seen Since 2019, Even as Its Profits Doubled
- Yahoo: Amazon just tripled its order of Nvidia chips over surging demand
- Yahoo: S&P 500 Edges Lower Despite Favorable NVIDIA Results and Stable Core PCE
- _Corroboration:_ 盘后 tape (fetch_intraday): regular_close $209.95 -1.16%, post_close $219.53 +4.56%, session_high $226.25. Margin outlook reset 是财报前列的观察点,兑现。

**Cross-assets.** SECTOR ETF +1.44% · SPY +0.07% · VIX 15.44 · 10Y 4.67 · WTI 82.13

**Agent read.** Prediction 分裂裁决。事件层 (sell-the-news): FAILED — NVDA 大 beat + 盘后 +4.56% (峰值 +7.8%),好财报换来好反应,用户『beat 也不涨』未兑现。结构层 (de-rating regime): VALIDATED — 『利润翻倍估值创 2019 低』倍数压缩真实; 『S&P 不跟涨』好消息不普惠。综合: 需要营收翻倍+$108B 指引+AMZN 订单×3 的历史级 blowout 才换 +4.5% 克制反应 (正常 regime 该 +10-15%),且从 6 年估值低位起弹。用户方向 (regime de-rate) 对,量级 (beat 也不涨) 被这份财报绝对强度盖过。次日 (8/27) 开盘确认 post-market 是否 hold — 若盘后 +4.5% 到次日缩水/翻绿转跌,则事件层判断部分翻回成立。留意 margin outlook reset 电话会细节。
 · [Snapshot](snapshots/2026-08-26.md)

---
### 2026-08-20 · -0.53% day · ● minor
**Tags:** `thesis_debate`, `prediction_recorded`, `macro_rates`
**Confidence:** medium

**Primary cause.** Forward prediction (not a price-move attribution): in a hawkish-sentiment regime, even a good AI earnings print produces muted/negative price reaction (de-rating + sell-the-news). NVDA 8/26 is the first and cleanest probe.

**Sources.**
- _Corroboration:_ Historical basis: 2022 (Nasdaq -33%, all multiple compression, EPS grew); 2018 Q4 (EPS +25% but market -20%, NVDA -50%); Nifty Fifty 1973-74 (earnings grew, P/E 40-50x->10x, stocks -50-80%); NVDA 2023-24 beat-but-fell 'priced for perfection'. NVDA into 8/26: -9% off 52wH, 5d -3.9% = moderately positioned, cleanest test.

**Cross-assets.** SPY -0.62% · VIX 15.85 · 10Y 4.7 · WTI 86.53

**Agent read.** User thesis: hawkish-sentiment regime suppresses even good AI earnings reactions (de-rating -20~50% regime-level; sell-the-news -5~15% event-level). Agent agrees on direction, adds: magnitude depends on pre-print crowding (MRVL most stretched 5d+10%, AVGO beaten-down -12.8% so lower sell-news risk, MU stretched 8x-from-lows). Watch the PRICE REACTION to the beat, not the beat. NVDA 8/26 first probe. Linked note: research/sectors/2026-08-20-debasement-regime.md.
 · [Snapshot](snapshots/2026-08-20.md)

---
### 2026-08-05 · +4.27% day · ▲ major
**Tags:** `partnership_news`, `competitor_news`, `ai_demand`, `sector_rotation`
**Confidence:** high

**Primary cause.** SpaceX 选定 NVIDIA 为其 AI 基础设施供应商（配合 SpaceX 收购 xAI/运营 Grok LLM 的垂直整合 AI 平台）。头条『Nvidia 赢下 SpaceX 大单，AMD 下沉』——同一条新闻里 NVDA 是卖铲子的受益方 (+4.3%)，SpaceX 是买铲子掏钱方 (-10.8%)，AMD 是丢单老二 (-6.4%)。SpaceX $15.8B AI capex 意味着对 NVDA 的持续收入。在 AMD 财报后回吐、SPCX capex 恐慌的背景下，资金明确流向 AI 供应商龙头。5d +16.3% 显示龙头地位在过去一周持续强化。

**Sources.**
- Zacks/Yahoo: [NVIDIA to Power SpaceX AI Infrastructure: Will This Fuel NVDA's Growth?](https://finance.yahoo.com/quote/NVDA/)
- GuruFocus: [Nvidia Just Won a Major SpaceX AI Deal. Stock Jumps as AMD Sinks](https://finance.yahoo.com/)
- _Corroboration:_ MU +3.2% (memory 主线同步走强)；vs AMD -6.4% 剪刀差；vol 0.74x 低于均值——上涨非放量驱动而是叙事+相对强度

**Cross-assets.** SPY +0.03% · VIX 15.93 · TEN YEAR 4.62 · WTI 74.53

**Agent read.** 『买铲子 vs 卖铲子』框架的教科书正例：同一条 AI 新闻，产业链不同位置反应相反。NVDA 拿下 SpaceX 旗舰客户，强化供应商龙头地位；与 AMD 走出剪刀差=供应商内部按『谁拿旗舰客户』分化，比 supplier-vs-spender 轮动更细。8/26 NVDA 财报会验证订单能见度。vol 0.74x 提示这是叙事+相对强度驱动，非资金蜂拥，可持续性需 8/26 财报确认。
 · Snapshot at `dashboard/2026-08-05.md`

---
### 2026-08-04 · +3.06% day · ▲ moderate
**Tags:** `sector_rotation`, `ai_demand`, `competitor_news`, `macro_rates`
**Confidence:** medium

**Primary cause.** Participated in the broad semiconductor risk-on rally (PLTR earnings validating enterprise AI + US-Iran draft deal + HBF memory standard) and reclaimed its 50MA at $205.67, but MATERIALLY UNDERPERFORMED the sector: +3.06% versus SMH +6.0%, MRVL +13.8%, AMD +9.3%, AVGO +7.4%. Financial media addressed the gap directly, noting NVDA still trades at a heavy discount to chip rivals and has lagged the PHLX Semiconductor Index, which is up 61% year to date.

**Sources.**
- Barron's/Yahoo: [Why Nvidia Stock Still Trades at a Heavy Discount to Chip Rivals](https://finance.yahoo.com/)
- Investor's Business Daily/Yahoo: [Nvidia Tops Key Level As AMD Heads Into Earnings; Is Nvidia A Buy Now](https://finance.yahoo.com/)
- Barron's/Yahoo: [Today's Trade Is to Buy Chips and Sell the Magnificent 7](https://finance.yahoo.com/)
- _Corroboration:_ NVDA underperformed every tracked semi peer today: MRVL +13.8%, INTC +11.0%, AMD +9.3%, AVGO +7.4%, SMH +6.0%, TSM +3.3%, NVDA +3.1%. Forward PE 16.5 is the CHEAPEST in the cluster (AMD 38, AVGO 21.6, MRVL 35, INTC 49, PLTR 74.7).

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** The signal today is not the +3.1%, it is the underperformance, and it deserves dedicated research. NVDA is the cheapest name in its own cluster at fPE 16.5 while trading up only half as much as the sector ETF on a day when every AI-positive catalyst fired at once. Two readings point in opposite directions. Bullish: NVDA is mispriced, and the 8/26 print is the re-rating catalyst. Bearish: the market is actively pricing share erosion, with the custom-ASIC path represented by AVGO and MRVL (TPU, Trainium, MTIA) taking hyperscaler sockets away from merchant GPUs — and it is precisely AVGO +7.4% and MRVL +13.8% that outran NVDA today, which is exactly what money buying 'the NVDA alternatives' looks like. I weight the second reading higher, because the underperformance is not a one-day artifact: SOX is up 61% YTD while NVDA has lagged all year. A single day of discount can be mispricing; a year of persistent underperformance in the sector leader is usually a structural judgment. The 8/26 Q2 FY2027 print (Blackwell shipments, data-center growth rate) is the only event that can falsify this, and it is the largest single event in the tracked universe this month. Worth noting alongside this: today marked the first session since July in which AI suppliers outran AI spenders (AMZN -2.4%, META -0.1% versus the semi complex up 6-14%), reversing the dominant 30-day pattern in which spenders crushed suppliers.
 · Snapshot at `dashboard/2026-08-04.md`

---
### 2026-07-10 · +4.03% day · ▲ major
**Tags:** `ai_demand`, `competitor_news`, `sector_rotation`, `supply_chain`
**Confidence:** high

**Primary cause.** Meta MTIA 报道逆转 (Meta 新 AI 芯片不会替换 NVDA GPU) + SK Hynix Nasdaq ADS 上市首日 +13% — 两大 bear case (custom silicon + HBM 供给) 同日 de-risk

**Sources.**
- Benzinga/Yahoo: [What's Going On With Nvidia Stock Friday — Meta's New AI Chip Won't Replace Its GPUs](https://finance.yahoo.com/markets/stocks/articles/whats-going-nvidia-stock-friday-200045889.html)
- Yahoo: [SK hynix surges on first day of trading on Wall Street (+13% IPO day, $28B raise)](https://finance.yahoo.com/markets/stocks/articles/sk-hynix-surges-first-day-202106559.html)
- 247wallst: [A $28 Billion AI IPO Trading at Just 7x Earnings: Too Cheap or Too Cyclical to Trust?](https://247wallst.com/investing/2026/07/10/a-28-billion-ai-ipo-trading-at-just-7x-earnings-too-cheap-or-too-cyclical-to-trust/)
- _Corroboration:_ 5d 分化极限: NVDA +8.28% vs INTC -22.5% — AI capex winner/loser 定价确认
- _Corroboration:_ SKHY CEO: 2027 史上最严重供给短缺 → HBM 需求 >>> 供给 → NVDA GPU 稀缺定价力强化

**Cross-assets.** SPY +0.40% · VIX 14.0 · INTC PCT 5D -22.50% · AVGO PCT 5D +10.90% · MU PCT 5D NOTE MU 昨日 +8% low-vol V 反 · VOL RATIO 0.92 · PUT CALL 0.61

**Agent read.** 两大 NVDA bear case 同日 de-risk: (1) Meta MTIA custom silicon 被明确 sidelined, (2) SKHY $28B IPO 强定价反证 HBM 供给链 investable. 但 vol_ratio 0.92 < 1 说明这是 short-covering + 散户情绪, 不是机构再定价. 30d 仍 -0.77%, 未 breakout 52w high ($236.54). 结构定性: de-risk 反弹, 不是 re-rate 起点. 对比 6/18 attribution 的三种可能 (rotation/custom-silicon repricing/beta normalization), 今天数据支持 custom-silicon repricing 已被证伪. 8/26 Q2 FY27 data center 营收 print 是唯一 re-rate 触发器. 中间 7/16 TSM + 7/22 semi week + 7/24 SKHY Q2 都是过关条件.
 · Snapshot at `dashboard/2026-07-10.md`

---
### 2026-06-18 · +2.95% day · ▲ minor
**Tags:** `sector_rotation`, `ai_demand`, `competitor_news`
**Confidence:** medium

**Primary cause.** Broad chip rally (Apple memory commentary + Intel-Apple deal); NVDA participating but lagging supply chain (DRAM +57% / 30d, TSM +10% / 30d vs NVDA +1.5% / 30d)

**Sources.**
- Yahoo/IBD: [Dow Jones Futures: Nvidia Leads 5 Chips Near Buy Points](https://finance.yahoo.com/)
- _Corroboration:_ Quiet 30d (+1.5%) while DRAM (+57%) and TSM (+10%) ripped — same AI thesis, different beneficiaries

**Cross-assets.** SPY +0.40% · VIX 14.2 · TEN YEAR 4.31

**Agent read.** MOST IMPORTANT cross-stock signal: NVDA quiet while supply chain ripped is mature thesis behavior. Money already long NVDA finding leverage downstream. Custom-silicon shadow (Trainium, TPU, MTIA) remains real. Three readings: (1) healthy rotation (bullish/neutral), (2) custom-silicon repricing (bearish), (3) beta normalization (NVDA done leading semis). Only next earnings tells which.
 · [Snapshot](snapshots/2026-06-18.md)

---
