# SPCX attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-06-29 · +7.15% day · ▲ major
**Tags:** `index_inclusion`, `post_ipo`
**Confidence:** high

**Primary cause.** EOD update: SPCX 收盘 +7.15% (盘中 +4.16%, 尾盘加速)。Nasdaq-100 纳入倒计时确认;期权链定价回归 cheap 启动衍生品 flow。SSPC -14.47% (反向 ETF, vol decay 加速)。6/18 user prediction「>=$200 by 6/26」仍然 FAIL;agent base case ($150-180) 当前价 $164.19 精确命中。距 thesis-break $130 缓冲扩大到 +26.3%。

**Sources.**
- Yahoo: [SpaceX joins Nasdaq-100 index weeks after SPCX IPO](https://finance.yahoo.com/)
- Yahoo: [SpaceX Stock Options Are Now Cheap With Nasdaq-100 Inclusion Upcoming](https://finance.yahoo.com/)
- Yahoo: [Comcast, Charter, Rocket Lab, SpaceX, Tesla, and More Stocks That Explain Today's Market](https://finance.yahoo.com/)

**Cross-assets.** SPY PCT +1.65% · QQQ PCT +2.49% · SSPC PCT -14.47%

**Agent read.** 
 · Snapshot at `dashboard/2026-06-29.md`

---
### 2026-06-22 · -10.78% day · ▼ extreme
**Tags:** `sector_rotation`, `ai_demand`, `secondary_offering`, `partnership_news`, `flow_event`
**Confidence:** high

**Primary cause.** AI-capex板块抛售第三日 — Alphabet -6% (Jumper离职去Anthropic), AMZN -4.8%, MSFT/META -3%, 合计mega-cap蒸发$248B+。SPCX因高duration新IPO + 同日宣布notes offering(债券增发) + 与Reflection AI签$6.3B/2029 compute协议(月付$150M) — 市场把这一组合解读为'AI capex负担+稀释'而非收入利好。第三个连续下跌日，仍在最近IPO狂奔后回吐。

**Sources.**
- Yahoo Finance: [U.S. tech megacaps slide as SpaceX extends slump, AI expense concerns grow](https://finance.yahoo.com/technology/ai/articles/u-tech-megacaps-slide-spacex-165325816.html)
- Yahoo Finance: [SpaceX reportedly signs $6.3B computing deal with Reflection AI](https://finance.yahoo.com/technology/ai/articles/spacex-reportedly-signs-6-3b-164616146.html)
- _Data:_ SPCX 1d -10.78% to $165.06 on vol 92.9M. SPY -0.26%, VIX 17.22, 10Y 4.51% — broad-market backdrop benign; this is mega-cap-tech specific selloff. ()
- _Corroboration:_ GOOGL -6%, AMZN -4.8%, MSFT -3%, META -3%; chip names diverged (MU +5.8% on Anthropic deal). 'Receiving the checks vs writing the checks' framing — David Wagner, Aptus Capital.
- _Data:_ Reflection AI deal terms: $6.3B total through 2029, monthly $150M from Reflection to SpaceX starting 2026-07-01, 90-day termination after initial 3 months. This is revenue, NOT capex — market mis-read or front-loaded the dilution from notes offering. ()

**Cross-assets.** SPY -0.26% · VIX 17.22 · TEN YEAR 4.51 · GOOGL -6.00% · AMZN -4.80% · MSFT -3.00% · META -3.00% · MU +5.80%

**Agent read.** 三条信号要分开: (1) 板块情绪转向 — AI capex怀疑论扩散到mega-cap, 投资者第一次系统性质疑hyperscaler的AI产出/投入比. SPCX作为新IPO的高duration名字, 是板块抛售里跌得最狠的, 不是idiosyncratic. (2) Notes offering同日宣布是叠加诱因 — 高估值新IPO同期增发债券, 信号就是'估值已到极致, 公司也要套现现金窗口'. (3) Reflection AI deal被市场误读 — 这是把Colossus闲置算力变现的revenue stream($150M/月), 但与notes offering同期发布, 又叠加'AI capex是负担'的整体叙事, 市场没拆开来读. 价格今日$165.06, 距thesis-break $130缓冲缩到21%; 用户6/18 prediction #1(下周收>=$200)从昨日就方向不利, 今天进一步证伪 — 这一组预测的early signal已经出来了, 7天后正式打分时大概率fail. 关键catalyst跟踪: lockup expiry 2026-12-09, F-1上市窗口还有6-8周.
 · Snapshot at `dashboard/morning-2026-06-22.md`

---
### 2026-06-18#pred4 · n/a day · ▲ minor
**Tags:** `prediction_recorded`, `thesis_debate`, `index_inclusion`, `ai_demand`
**Confidence:** medium

**Primary cause.** AGENT COUNTER-PREDICTION 4: SPCX grinds in $190-235 range from 2026-06-22 to 2026-08-31, never closing below $180 or above $260 sustainably. The path missing from user's binary framework.

**Sources.**
- _Data:_ CRSP inclusion 6/19, Nasdaq-100 inclusion ~7/1 = mandatory passive buying (Motley Fool 2026-06-18)
- _Data:_ Float-adjusted investable cap ~$125B vs $2.4T headline = persistent scarcity premium (Motley Fool 2026-06-18)

**Cross-assets.** n/a

**Agent read.** Index buying is mechanical (not sentiment). AI-infra narrative builds via Anthropic/Google capacity-deal news flow over weeks. Slow narrative-build supports a grind, not a parabola. No rush on bear side either — lockup not until Dec 9. This is my base case at 45%.


---
### 2026-06-18#pred3 · n/a day · ▼ material
**Tags:** `prediction_recorded`, `user_stand`, `lockup_expiry`, `flow_event`
**Confidence:** high

**Primary cause.** USER PREDICTION 3: CONDITIONAL on SPCX trading $200-220 range without breaking $230 from 2026-06-22 to 2026-07-31, reverts to <$185 by 2026-08-31. SSPC entry trigger.

**Sources.**
- _Data:_ SSPC = 2x DAILY-rebalance inverse ETF; volatility decay severe in sideways markets (ETF prospectus understanding)
- _Data:_ Lockup expiry 2026-12-09 — selling pressure not structural until then; weeks of stagnation absorbable (180-day post-IPO standard)

**Cross-assets.** n/a

**Agent read.** STRONGEST part of user's prediction — 'stall = revert' is textbook IPO pattern. Without breakout catalyst, lockup math wins. BUT: SSPC is wrong tool — 2x daily-rebalance inverse decays in choppy ranges. For 'slow grind to $170-180' view, SPCX Aug/Sep $170 puts are better implementation. Tactical concern recorded.


---
### 2026-06-18#pred2 · n/a day · ▼ material
**Tags:** `prediction_recorded`, `user_stand`, `lockup_expiry`
**Confidence:** medium

**Primary cause.** USER PREDICTION 2: CONDITIONAL on SPCX hitting $250 before 2026-08-01, price drifts back to $230-270 by 2026-09-25

**Sources.**
- _Data:_ Oppenheimer raised PT $190 → $250 on 2026-06-18 (StockAnalysis.com)
- _Data:_ Median PT $175, mean $187.80 — significant gap to $250 floor (StockAnalysis.com)

**Cross-assets.** n/a

**Agent read.** Logic structurally sound — overshoot+revert is common. $250 = Oppenheimer's freshly raised PT, so real anchor. $401 Arete is outlier; if bull case really runs, $310 likely cap. Where I'd push back: $250 floor in 3 months is high; if AI-infra narrative doesn't deliver, floor could be $200.


---
### 2026-06-18#pred1 · n/a day · ▲ material
**Tags:** `prediction_recorded`, `user_stand`
**Confidence:** medium

**Primary cause.** USER PREDICTION 1: SPCX closes ≥ $200 on at least one day during 2026-06-22 to 2026-06-26 (next week)

**Sources.**
- _Data:_ Mean analyst PT $187.80, median $175 — Oppenheimer $250 raised + Arete $401 give upside cover (StockAnalysis.com 2026-06-18)
- _Data:_ CRSP US Total Market index inclusion eligibility 2026-06-19; Nasdaq-100 inclusion eligibility 2026-07-01 — mechanical buying support (Motley Fool 2026-06-18)

**Cross-assets.** n/a

**Agent read.** Plausible at 60% — index inclusion provides mechanical floor + Oppenheimer raised PT to $250 same day. First-week post-IPO downward drift is normal settling, not thesis collapse. But not high-conviction: bimodal analyst tape (5 strong-buy, 0 hold, 1 strong-sell) means no consensus to anchor to.


---
### 2026-06-18 · -3.56% day · ▼ material
**Tags:** `thesis_debate`, `user_stand`, `lockup_expiry`, `flow_event`, `index_inclusion`
**Confidence:** medium

**Primary cause.** Recorded thesis debate: user 'worth half' bear thesis vs agent counter-take with mega-IPO historical data. User direction supported (median 12m drawdown -53% across FB/SNAP/UBER/COIN/RIVN/RBLX/ABNB) but magnitude challenged by SPCX's tiny float (~4%), passive-flow mechanics (Nasdaq-100/CRSP inclusion), and emerging AI-infrastructure narrative.

**Sources.**
- _Data:_ Mega-IPO 12m drawdowns: META -53.6%, SNAP -51.7%, UBER -64.3%, ABNB -13.8%, RBLX -40.6%, COIN -53.3%, RIVN -79.5%. Median -53.3%. (yfinance historical pulls)
- _Data:_ SPCX +14.95% since 6/12 IPO uncorrelated with AI names (NVDA +2.84%, DRAM +17.80% same window) — money flowing into AI complex, not space (yfinance)
- Motley Fool: [Index Investors: How Much SpaceX Stock You're About to Own](https://www.fool.com/investing/2026/06/18/index-investors-how-much-spacex-youre-about-to-own/)
- _Quote:_ "the most sophisticated investors are currently refraining from meaningful purchases, instead waiting for more favorable conditions" — Adam Spatacco, Motley Fool, 2026-06-18

**Cross-assets.** SPY +0.40% · VIX 14.2 · TEN YEAR 4.31

**Agent read.** User thesis: SPCX worth ~$1.2T (half), reverts post-lockup, AI is the present money story not space. Agent counter: direction right (post-IPO drawdowns are common; 6/7 mega-IPOs declined 40%+ in 12 months) but magnitude likely smaller (15-25% drawdown to $150-180) due to (a) ~4% float vs $2.4T cap = persistent scarcity premium, (b) Nasdaq-100/CRSP passive flows are mechanical floor not present for FB/SNAP/UBER analogs, (c) Anthropic/Google capacity deals positioning SPCX as AI infrastructure could re-rate before Dec 9 lockup. Probability split: Bull 25%/Base 50%/Bear 25%. Both views stored; scored at lockup expiry 2026-12-09 and 12m mark 2027-06-12. See dashboard/spcx-thesis-pressure-test-2026-06-18.md.
 · [Snapshot](snapshots/2026-06-18.md)

---
