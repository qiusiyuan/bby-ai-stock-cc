---
name: deep-dive
description: Use when the user wants to know WHY a stock moved today, not just the number ("why is NVDA up", "what's driving DRAM", "explain SU's drop", "attribute today's move", "find sentiment on SPCX"). Searches news + online sentiment, attributes the move with cited sources, and distinguishes facts from inferences.
---

# deep-dive

Generic skill: explain a stock's price action with cited sources, not vibes. The user wants signal, not numbers.

## When invoked

- "why is NVDA up today"
- "what's driving DRAM"
- "explain SU's drop"
- "attribute today's move on TSM"
- "find what people are saying about SPCX"
- AUTOMATICALLY when running `watchlist`, `watchlist`, or any watch report and a stock has moved >3% on the day OR >10% in 5 days OR has unusual volume (>1.5× avg).

## Steps

1. **Pull current quote + news.** `uv run --project scripts scripts/fetch.py {TICKER}` returns 72h headlines from Yahoo RSS. That's the starting set.

2. **Pull sector context.** Get the sector ETF's day move and the macro line (SPY, VIX, 10Y, oil if energy). Distinguish **stock-specific** drivers from **sector** or **macro** drivers. A stock can be up because the whole sector is up — that's a different story than a company-specific catalyst.

3. **Pull commodity / cross-asset reads when relevant.**
   - Energy stocks → check WTI (`CL=F`), USO ETF, oil-services indices
   - Memory/chip stocks → check competitor moves (MU, AVGO), HBM news, Apple/hyperscaler signals
   - Auto stocks → check competitor delivery numbers, recall news
   - Bank stocks → check the 10Y curve, credit spreads
   - Recently-IPO'd stocks → check lock-up math, index inclusion timing, post-IPO float dynamics

4. **WebFetch the most-relevant headlines** — but expect 30-50% of Yahoo article URLs to 404 (they expire fast). Fall back to:
   - Wikipedia for company-specific structural facts
   - Motley Fool (`www.fool.com` — usually durable)
   - SEC EDGAR for filings
   - Issuer pages (e.g. globalx.ca for the ETF)
   - Reuters / Bloomberg / CNBC mirrors when accessible

5. **Search sentiment when asked.** For "what people say":
   - Try Reddit search via Google: `site:reddit.com {TICKER} {topic}`
   - Try Stocktwits: `stocktwits.com/symbol/{TICKER}` — note this is sentiment data, treat with skepticism
   - Don't pretend to have access to private posts or paywalled content

6. **Synthesize attribution — 讲清叙事，不贴标签。**

   核心原则: **归因的价值不在列出 "发生了什么"，而在讲清 "市场为什么在卖/买"。** 催化剂是事实，但市场的推理路径才是归因。

   **叙事深度规则:**
   - 如果一个 move 的原因是显而易见的（earnings miss, 明确的利空 headline），一句话带过。
   - 如果原因复杂（多催化剂叠加、因果链 ≥ 3 步、多个板块联动、跌幅超预期），必须展开写:
     - 每个催化剂各是什么（事实层）
     - 市场怎么解读每个催化剂（推理层）
     - 为什么这个解读导致卖出/买入（行为层）
     - 各催化剂之间的关系 — 独立? 叠加? 互相强化?
   - **特别注意 "跌幅超预期" 的情况**（e.g. 预测 -3~5% 实际 -8%）：这意味着有额外催化剂没被识别。必须追问: 超出部分是什么贡献的? 是宏观叠加? 是新催化剂? 是流动性/仓位结构?

   **多源归因 checklist (每个 deep-dive 必须覆盖):**
   - [ ] 公司层面: 有没有今天 specific 的 headline (earnings, guidance, product, personnel, legal)?
   - [ ] 板块层面: 同行怎么动? 是 beta 还是 alpha? (比较 SOX/sector ETF)
   - [ ] 宏观层面: 今天有没有 macro data release / Fed / geopolitics?
   - [ ] 资金流/仓位层面: vol_ratio 高低? 大单? 空头? ETF rebalance? lockup?
   - [ ] 叙事层面: 有没有更大的 narrative shift 在进行? (e.g. "AI efficiency reduces demand", "hyperscaler overcapacity") — 这往往是跌幅超预期的真正原因
   - [ ] 跨市场确认: 其他相关资产的 move 是否 confirm 你的归因? (e.g. CoreWeave -14% 确认 META compute 冲击)
   - [ ] 逆向检验: 有没有 "该跌没跌" 或 "该涨没涨" 的反例? (e.g. RIVN +8% 同日 → EV sector 没问题 → TSLA 是个股问题)

   **输出结构:**

   ```markdown
   ## Deep Dive: {TICKER} ({±%} day, {±%} 5d)

   **发生了什么。**
   {1-3 sentences: the raw facts — price, related assets, what's notable}

   **为什么。** (核心叙事 — 逻辑链展开)
   {如果简单: 1 段。如果复杂: 分链展开，每条链写清 "催化剂 → 市场解读 → 为什么导致卖/买"}

   **为什么跌幅/涨幅超出预期。** (optional — 仅当幅度显著超出 "正常" 时)
   {追问 extra 部分是什么贡献的}

   **什么会证伪 / 反转条件。**
   {具体数据点 + 日期: 如果 X 在 date 确认 → 当前 narrative 被推翻}

   **Cross-assets / confidence / sources.**
   ```

   避免: "sell-off", "sector rotation", "supply-glut fears", "risk-off" 等标签。这些是描述，不是解释。如果你发现自己在用这类词，停下来问: "市场具体在想什么才导致了这个行为?"

7. **NEVER fabricate sources.** If a URL 404s, say "Article URL no longer accessible — falling back to Wikipedia / Fool / etc." If sentiment isn't accessible (paywall, login required, blocked), say so plainly.

8. **PERSIST the attribution.** After producing the analysis, record it to memory. This is mandatory whenever the move clears the threshold. Build a JSON object matching the schema in `attributions/README.md` and pipe it to:

   ```bash
   uv run --project scripts scripts/record_attribution.py
   ```
   (reads JSON from stdin)

   This atomically:
   - Appends to `stocks/{TICKER}/attributions.md` (human-readable log, replaces today's entry if re-run)
   - Upserts the matching JSON line to `attributions/index.jsonl` (queryable index, keyed by date+ticker)

   **Tag discipline.** Use ONLY tags from the vocabulary in `attributions/README.md`. If nothing fits, use `unattributed`. Inventing new tags pollutes the index.

   **Confidence honesty.** `high` = direct cited catalyst. `medium` = sector/macro driver but not company-specific. `low` = flows/sentiment/unattributable. Don't inflate.

9. **Output rule.**
   - **Inline in chat** for single-stock quick attribution if the answer is short (≤8 lines).
   - **Append to today's per-day file** for multi-stock attribution reports or anything with tables / multiple sources:
     - Open or create `dashboard/{YYYY-MM-DD}.md`
     - Append a new `## Attribution` H2 section (if one already exists from earlier today, replace it in place — same rule as morning)
     - Use H3 (`###`) for ticker-level subsections inside the Attribution block
     - Re-render the per-day file:
       ```bash
       uv run --project scripts scripts/render.py dashboard/{YYYY-MM-DD}.md --title "{YYYY-MM-DD}"
       ```
     The renderer auto-generates browser tabs from each H2 in the day file. The user sees one URL per day, growing tabs as the session progresses, instead of one new browser tab per skill.

10. **When a similar setup appears later, query first.** Before writing fresh analysis, run [[find-similar-moves]] to surface analogs from history. The agent gets smarter as the index grows. Cite past analogs in new attributions where relevant.

## Hard rules

- **Cite. Always.** A claim without a source is worth nothing in this skill. If you can't cite, say so.
- **Distinguish stated from inferred.** "Reuters said X" ≠ "I think X happened because of Y." Both are useful — but they get different weight.
- **Don't overweight retail sentiment.** Reddit/Stocktwits is what retail thinks now. It is rarely the explanation.
- **Volume matters.** A 5% move on 0.5× volume is a different story than 5% on 2× volume. Note volume in the attribution.
- **Distinguish the move's CAUSE from its CONFIRMATION.** If TSM is up 7% and AVGO is up 6% on the same day, neither caused the other; both reacted to the same underlying signal. Identify the signal.
- **For ETF moves, attribute to the largest holdings' moves.** DRAM up 9% likely tracks SK Hynix / Samsung / Micron's moves — pull each holding's day to confirm.

## Skill linkage

- Called automatically from [[watchlist]] and [[watchlist]] when threshold conditions hit (>3% day, >10% 5d, vol >1.5×).
- Called directly when user asks "why" / "what's driving" / "explain" / "attribute" / "what are people saying".
- Findings get appended as a `## Attribution` H2 section in `dashboard/{YYYY-MM-DD}.md` (auto-rendered as a tab). Per-stock snapshot under `stocks/{TICKER}/snapshots/{date}.md` still gets the same content under `## Attribution` for stock-level lookup.
