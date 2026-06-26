# SNDK attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-06-26 · -6.69% day · ▼ major
**Tags:** `sector_rotation`, `competitor_news`, `flow_event`
**Confidence:** high

**Primary cause.** SK Hynix 韩股盘前 -8.36% 收 ₩2,673,000 (vs ₩2,917,000) → 美股 memory cluster 联动 mean-reversion。触发新闻「Samsung, SK Hynix Slide 9% Before $646 Billion Investment Update」+「Micron, SanDisk, and Western Digital Fall 7% as Memory Rally Cools」。SNDK 作为「美国版 SK Hynix 替代品」最敏感传感器，单日同步砸盘 — 但传导系数从 6/23 的 1.67x 缩小到今天的 0.96x，说明市场已学习。盘前 $2,230 → $2,137 低点 (-8.48%) → 开盘 $2,173 反弹 → 早盘 $2,178.79，vol 0.12 极低 = 流动性主导非 capitulation。MU -7.04%, DRAM ETF -7.08% 同向印证。同时 Mag-7 出现 reversal：AAPL +0.33% / MSFT +1.29% / META +0.17% 不跟跌 + Barron's「Apple/MSFT face bigger problems than memory prices」narrative 翻面。基本面（HBM3E/HBM4/Anthropic-MU/8/24 Q4 财报）无任何实质变化。

**Sources.**
- {"title": "Samsung, SK Hynix Slide 9% Before $646 Billion Investment Update", "url": "https://finance.yahoo.com/", "type": "news"}
- {"title": "Micron, SanDisk, and Western Digital Fall 7% as Memory Rally Cools", "url": "https://finance.yahoo.com/", "type": "news"}
- {"title": "Semiconductor stocks retreat over worries about memory costs", "url": "https://finance.yahoo.com/markets/article/semiconductor-stocks-retreat-over-worries-about-memory-costs-131508185.html", "type": "news"}
- {"title": "Apple, Sandisk, Marvell, and More Stocks That Explain Today's Market", "url": "https://barrons.com/", "type": "news"}
- {"title": "Apple, Microsoft Face Bigger Problems Than Micron's Memory Prices", "url": "https://barrons.com/", "type": "news"}

**Cross-assets.** SPY -0.92 · QQQ -1.77 · VIX 20.46 · 10Y 4.41 · MU -7.04 · 000660.KS -8.36 · DRAM -7.08 · NVDA -2.22 · TSM -3.36 · AAPL 0.33 · MSFT 1.29 · WTI -2.78

**Agent read.** Smoking gun: Hynix 韩股 -8.36% 隔夜 + Samsung/SK Hynix $646B 投资公告前置 de-risking。SNDK 作为美股 memory cluster 第二敏感标的 (vol 0.12 = 早盘流动性盘) 砸 -6.69%，但传导效率较 6/23 大幅下降 (1.67x → 0.96x)。盘前 W-bottom 形态在 $2,137 测试两次未破 = 第一道 confluence 支撑。Mag-7 出现反向 narrative reversal (AAPL/MSFT 反弹 + Barron's 头条「他们有比 memory 更大的问题」) — narrative 24h 内已三度翻面：(1) bull memory + bull terminal (6/25 早) → (2) bull memory + bear terminal (6/25 收) → (3) bear memory + bull terminal (6/26 早盘)。本质上是单日 +22% 后的 mean-reversion + cluster contagion 二次释放。基本面 anchor 未变：8/24 Q4 财报。**SNDK 缺 thesis.md** 是当前最大 gap — 4 天内成为 memory cluster 第二号噪音放大器，无 thesis-break 监控机制。建议本周建一份 thesis brief。下一观察窗口：(1) $2,137 是否守住；(2) 韩股 6/27 收盘走势；(3) 7/10 ADR 前是否还会有二次 cluster reset。


---
### 2026-06-23 · -14.01% day · ▼ extreme
**Tags:** `regulatory_negative`, `policy_korea`, `flow_event`, `sector_rotation`
**Confidence:** high

**Primary cause.** Korean FSS 总裁 Lee Chan-jin 公开'后悔'5月底批准 16 只 2x 杠杆单股 ETF (标的 Samsung/SK Hynix, AUM 4周翻三倍到 $9B+)，冷却警告反而引爆抛售。SanDisk 自身无公司层面催化 — Fool 明确指出两条传导: (1) 同类杠杆 ETF 担忧蔓延; (2) 之前作为'美国版 SK Hynix 替代品'被买入，今天反向解仓。SNDK 52 周累计 +4700%，今天 -14% 在此斜率前是 mean-reversion 而非趋势反转。

**Sources.**
- Motley Fool: [Why Sandisk Stock Suddenly Crashed Today](https://www.fool.com/investing/2026/06/23/why-sandisk-stock-suddenly-crashed-today/)
- CNN: [Wall Street is getting trampled by an AI sell-off. South Korean market plunges 10%](https://www.cnn.com/2026/06/23/business/stock-market-kospi-dow-nasdaq-ai)
- Axios: [AI bubble fears send tech stocks plunging](https://www.axios.com/2026/06/23/tech-stocks-ai-bubble)
- 247WallSt: [SanDisk Plunges 11%, Micron and Western Digital Slide 10% as Korean Market Crash Hits Memory Chips](https://247wallst.com/investing/2026/06/23/sandisk-plunges-11-micron-and-western-digital-slide-10-as-korean-market-crash-hits-memory-chips/)
- _Data:_ FSS Governor Lee Chan-jin 公开声明: 16 只 2x 杠杆 ETF 是 'high-risk products', AUM 4 周翻三倍到 $9B+. KOSPI 半导体板块 -10%, SK Hynix -7.56%, Samsung 005930.KS -12.43%. ()
- _Corroboration:_ MU -11.09% (vol 0.65), WDC -8.86% (vol 0.96), DRAM ETF -12.62% (vol 1.40). 同向但 SNDK 跌幅最大 = 杠杆/替代品最重。
- _Data:_ SNDK 52w +4700% ($40.10 → $2354 high)。今天 -14% / 30d 仍 +25.15%。vol_ratio 0.79 (低) — 散户/算法砸盘，无机构 capitulation。 ()

**Cross-assets.** SPY -0.97% · VIX 18.75 · TEN YEAR 4.49 · SKHYNIX -7.56% · SAMSUNG -12.43% · MU -11.09% · WDC -8.86% · DRAM ETF -12.62%

**Agent read.** Smoking gun: 韩国 FSS 监管警告 16 只 2x 杠杆 ETF (Samsung/SK Hynix 标的, AUM 4周翻三倍至 $9B+)。冷却警告反而引爆去杠杆抛售，KOSPI 半导体 -10%。SanDisk 是美股传导最严重的标的 — 既因 leverage ETF 担忧蔓延，也因前期被资金当作'美国版 SK Hynix 替代品'追涨。三层因果链清晰: 监管动作 → 韩股去杠杆 → 美股替代品/代理共振。这不是 stock-specific 也不是 AI-fundamentals-specific，而是 LEVERAGE-specific。类比 2020-09 SoftBank Nasdaq whale 反向案 和 2024-08 Yen carry unwind 的小型版。基本面（HBM3E NVIDIA 独占、HBM4 leadership、Anthropic-MU 协议）未受任何冲击。下一观察窗口: (1) FSS 是否对 16 只 ETF 进一步采取行动（强制赎回/限制申购）; (2) 韩国本土散户是否回补; (3) 卖方主流叙事是否从 'rotation' 转向 'bubble pop'。
 · Snapshot at `dashboard/attribution-2026-06-23.md`

---
