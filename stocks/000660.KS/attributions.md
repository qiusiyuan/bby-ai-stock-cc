# 000660.KS attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-09-15 · -6.73% day · ▼ large
**Tags:** `macro_rates`, `sector_rotation`, `memory_pricing`
**Confidence:** medium

**Primary cause.** SK Hynix 韩国母股单日 -6.73%, 是全组合当日最大跌幅, 跌破 MA50 (₩1,746,591)。同日 Samsung (005930.KS) -4.24% / 5d -7.96%, 说明这是韩国内存板块的整体去杠杆而非个股事件。**无 HBM 或内存的公司级利空** —— 归因只剩折现率通道: 10Y 美债今天破 5.00%, 创 2007 年 7 月以来新高 (30d +6.7%), 而明天 FOMC 市场定价的是加息 (2Y 4.65% 高于 Fed funds 上限约 90bp)。**核心机制 (与 8/18 和 9/10 两次完全相同): fwd PE 3.6x 看似极便宜, 但这个倍数隐含的是「周期高点盈利能维持多年」, 而折现率上升压缩的恰恰是靠后年份的现值 —— 也就是低 PE 的全部依据。所以低 PE 在折现率上行期不提供下行保护, 反而是分子 (周期持续性被质疑) 与分母 (折现率) 双重受害。** 三次同模式对照: 8/18 (10Y 停 52w 高 4.71% + WSJ 内存定价报道) → DRAM -7.97 / MU -7.11 / SNDK -8.92 / SKHY -8.2; 9/10 (八月 PPI +5.4% + WTI 破 $103 → 10Y 4.96%) → MU -4.9 / SKHY -5.2 / DRAM -4.9 / SNDK -4.06; 今天 (10Y 破 5.00% + WTI $106) → 韩国 -6.7/-4.2。**最值得记的异常: 美国 ADS (SKHY) 今天只跌 1.20%, 与母股有 5.5 个百分点缺口。** 这是时区造成的 —— 韩国 9/15 收盘反映当地整个交易日 (含对隔夜美债的反应), 而 SKHY 的美股时段仍在进行、尚未完整消化。历史上此类缺口次日收敛, 因此 SKHY 明天有补跌压力, 且明天正好是 FOMC 决议日, 两个负向因素撞在一起。

**Sources.**
- CNBC: 10-year Treasury yield hits highest level since 2007
- Dow Jones: Dollar Rises in Anticipation of Fed Rate Increase
- {"type": "cross_stock", "title": "Samsung 005930.KS -4.24% / 5d -7.96% \u540c\u6b65; DRAM ETF 5d -10.47%; SNDK 5d -12.74%", "publisher": "workspace", "url": ""}

**Cross-assets.** SPY -0.47% · VIX 17.46 · TEN YEAR 5.0 · WTI 105.95 · DXY 99.64 · GOLD 4342.5 · BTC 75913

**Agent read.** 纯折现率去杠杆, 无公司级利空, 第三次同模式重复。韩美 5.5pp 缺口是明天的主要变量。真正能改变判断的是 9/30 MU 财报的 Tier 1 门槛。


---
### 2026-08-04 · -8.21% day · ▼ major
**Tags:** `sector_rotation`, `memory_pricing`, `competitor_news`, `unattributed`
**Confidence:** medium

**Primary cause.** SK Hynix's Korean local listing fell -8.21% on the SAME DAY its US ADS (SKHY) rose +7.79% — a 16-percentage-point divergence in one company. Primary explanation is timing plus venue: the Korean close precedes the US open by roughly 13 hours, so the local market traded on 8/3 US memory sentiment and captured NEITHER the HBF standard launch NOR the six brokerage coverage initiations, both of which are US-ADS-specific events (research quiet-period expiry only reaches the ADS market). Contributing negative: Counterpoint data showed Samsung reclaiming the #1 DRAM position at 39% Q2 share.

**Sources.**
- _Data:_ 000660.KS -8.21% versus SKHY ADS +7.79% same date — 16pp gap. Korean market closes ~13 hours before US open. ()
- Yahoo: [MU, SNDK, DRAM Stocks Advance Premarket: Samsung Reclaims DRAM Lead, Micron Narrows Gap With SK Hynix](https://finance.yahoo.com/)
- Yahoo: [SK Hynix rises as brokerages launch coverage with bullish ratings](https://finance.yahoo.com/)

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** This is the single most diagnostic anomaly in today's tape and it is worth logging precisely because it will recur. A 16-point same-day divergence between an ADS and its home listing is not a data error; it is the predictable result of venue-specific catalysts (coverage initiations reach only ADS holders) landing inside a 13-hour timezone gap. TESTABLE PREDICTION for the 8/5 Korean open: if 000660.KS rallies 6% or more, the timezone-plus-venue explanation is confirmed and the ADS premium is justified by information that the local market simply had not yet seen; if it gains under 3% or falls again, then today's ADS +7.8% was one-sided US sentiment and the premium should mean-revert. The local listing is also -43.0% over 30 days versus the ADS being far shallower, which is itself evidence that the ADS has been carrying a widening premium — exactly the structure flagged in the existing 7/31 research (stocks/SKHY/research/2026-07-31-ads-premium-structure.md). Today supplies the first live stress test of that framework. Separately, the Samsung share-reclaim datapoint is a genuine competitive negative for SK Hynix that the Korean market may have weighted more heavily than US ADS buyers did, and it carries a mildly negative read-through to MU's 9/23 scorecard on HBM share dynamics.
 · Snapshot at `dashboard/2026-08-04.md`

---
### 2026-06-22 · +5.61% day · ▲ extreme
**Tags:** `ai_demand`, `memory_pricing`, `production_milestone`, `sector_rotation`
**Confidence:** high

**Primary cause.** HBM超级周期赢家集中度进一步扩大。SK Hynix 30d +76.5% vs Samsung 30d +32.9% — 差距43个百分点(上周还是38),市场用脚投票确认SK Hynix是HBM3E NVIDIA独占+HBM4领跑的'唯一胜者',Samsung是落后者. 同日MU +5.26% (上市MU 30d +84.6%)受Anthropic战略协议催化, 形成'三个winner层级'清晰画面: SK Hynix (顶级) > MU (次级,从消费端切入) > Samsung (掉队). DRAM ETF 1d +4.6% / 30d +72.4%, 与SK Hynix基本同步, ETF忠实跟踪标的.

**Sources.**
- _Data:_ SK Hynix 000660.KS: ₩2,919,000 close, +5.61% 1d / +27.58% 5d / +76.51% 30d. 52w-high. 直接KRX拉取. (yfinance)
- _Data:_ Samsung 005930.KS: ₩353,500 close, -2.48% 1d / +9.61% 5d / +32.89% 30d. 30d 差距43个百分点. (yfinance)
- _Data:_ MU: $1,193.66, +5.26% 1d / +21.6% 5d / +84.6% 30d. Anthropic战略协议公告日. (yfinance)
- _Data:_ DRAM ETF: $80.24, +4.6% 1d / +23.4% 5d / +72.4% 30d. 与SK Hynix同步度极高. (yfinance)
- Yahoo: [Micron Stock Roars Higher on Supply Deal with Anthropic](https://finance.yahoo.com/news/micron-stock-supply-deal-anthropic)
- Yahoo: SK Hynix ETF Raises Options Cap After Stock's 340% Surge

**Cross-assets.** SAMSUNG 5D PCT +9.61% · SAMSUNG 30D PCT +32.89% · SKHYNIX 30D PCT +76.51% · MU 30D PCT +84.60% · DRAM ETF 30D PCT +72.40% · SPREAD SKHYNIX MINUS SAMSUNG 30D 43.6

**Agent read.** 三层winner结构现在非常清晰: SK Hynix(HBM3E+HBM4独占, 30d +77%) > MU(消费端/Anthropic协议催化, 30d +85%但基数小) > Samsung(掉队, 30d +33%). 关键判断: 这不是'memory周期'整体, 而是'AI HBM子周期'的赢家集中. 持有DRAM ETF的优势 = 自动权重SK Hynix(25-30%)+Samsung(~15%)+MU; 缺点 = 没有完全捕获SK Hynix的alpha. 用户若要纯HBM alpha, 应该考虑直接持SK Hynix或MU; 若要分散+省事, DRAM ETF够用. F-1上市窗口正在打开 — 52w-high + 市值$1.5T级别的公司, 不会浪费这种equity window, NYSE F-1的概率在6-8周内进一步上修. 当前关键风险: 一旦HBM4 yield新闻或Samsung突破出现, 这种spread会快速收敛, 持仓应保留. 该归因为'HBM赢家集中度'的关键证据点, 未来若Samsung反超应回查此条.
 · Snapshot at `dashboard/morning-2026-06-22.md`

---
### 2026-06-19 · +2.94% day · ▲ major
**Tags:** `ai_demand`, `memory_pricing`, `production_milestone`, `sector_rotation`
**Confidence:** high

**Primary cause.** SK Hynix closed at 52-week high ₩2,764,000 (~$1.43T market cap). HBM3E NVIDIA monopoly + HBM4 leadership driving +58.4% / 30d move. Samsung Electronics lagging by 38 percentage points over 30d (Samsung +20.5% vs SK Hynix +58.4%) — market explicitly choosing SK Hynix as the HBM cycle winner.

**Sources.**
- _Data:_ SK Hynix 000660.KS direct KRX pull: ₩2,764,000 close on 2026-06-19, +2.94% day (yfinance)
- _Data:_ Samsung 005930.KS comparison: ₩354,000 close 2026-06-19, ~+20% over 30d — significant lag vs SK Hynix (yfinance)
- _Corroboration:_ DRAM ETF +57.58% / 30d ≈ SK Hynix +58.42% / 30d. ETF faithfully tracking underlying; ~25-30% SK Hynix weight.
- _Data:_ Korean market traded today; no holiday (Memorial Day was June 6). (Wikipedia public holidays in South Korea verified)

**Cross-assets.** SAMSUNG 30D PCT +20.50% · DRAM ETF 30D PCT +57.58% · SKHYNIX 30D PCT +58.42%

**Agent read.** Yesterday I underweighted direct SK Hynix data — relied on DRAM ETF as proxy. Correction: SK Hynix is the direct beneficiary and the dominant signal of the HBM super-cycle. At 52w high with $1.43T market cap and the listing-friendly equity window wide open, the probability of NYSE F-1 going public in the next 6-8 weeks just went up materially. Companies don't sit on confidential filings when equity is at ATH. For DRAM holders: SK Hynix direct exposure outperforms ETF dilution. Samsung lagging by 38 points over 30d is the cleanest fundamental confirmation that the cycle has a specific winner, not a category.
 · Snapshot at `stocks/DRAM/snapshots/2026-06-19.md`

---
