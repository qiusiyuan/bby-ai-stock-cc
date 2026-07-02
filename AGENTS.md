# Stock Tracking Workspace

This is a personal AI-driven stock-tracking workspace. The user is a serious individual investor doing fundamental research on individual names. Behavior is driven by skills in `.claude/skills/`, invoked through natural language.

## Core rules

1. **Skills first.** When the user asks about a stock or the workspace, map the request to a skill in `.claude/skills/` and follow it. Do not improvise routines — if a request doesn't fit an existing skill, suggest extracting one.

2. **No auto-refresh.** Never fetch data without an explicit user request. Every data fetch is a deliberate user trigger.

3. **No cost basis.** The workspace intentionally does not store entry prices, position size in dollars, or cost basis. Do not ask for it; if the user volunteers it, do not record it. Show price vs target and vs thesis-break level only. Reason: anchoring on entry is one of the strongest documented sources of return drag.

4. **Append-only logs.** The "Stands & Updates" section in each `thesis.md` is append-only. Add new dated entries; never edit prior entries.

5. **Use frameworks as analytical lenses, not as forms.** When writing analysis (moat, valuation, etc.), use professional frameworks behind the scenes (Helmer's 7 Powers for moat, Mauboussin reverse-DCF for valuation) but write outputs in plain English judgment. The user reads conclusions, not jargon-laden tables.

6. **Honest data limits.** Free data sources have gaps:
   - Real institutional money flow → not free; we use volume-weighted proxies and label them as such
   - Real-time options flow → not free
   - Earnings call transcripts at scale → not free
   When a gap is material, flag it. The cheapest meaningful upgrade is Koyfin or Stock Rover ($10–25/mo).

## Presentation rule (how to reply)

**Default: reply in chat.** Don't dump markdown files at the user.

| User asked for | Reply with |
|----------------|------------|
| Quick info, single fact, status check | 1–3 sentences in chat. No file. |
| Small comparison or short list (≤8 rows) | Tiny markdown table directly in chat. No file. |
| Snapshot, dashboard, thesis, review, comparison report | **Render to HTML and open in browser.** Use `uv run --project scripts scripts/render.py <path>`. Then say one short sentence in chat: "Opened {report name} in browser." |

The render script writes to `site/reports/{slug}.html` (published via GitHub Pages) and opens it via `open` on macOS. Use it for any output longer than ~10 lines or that has tables, sections, or signal flags worth visualizing.

For ad-hoc reports (something you compose on the fly without writing to a file), pipe to render via stdin:
```bash
cat <<'EOF' | uv run --project scripts scripts/render.py - --title "NVDA quick view"
# NVDA quick view
... your markdown ...
EOF
```

When the user says "show me as text" or "just summarize", drop the HTML and reply in chat.

### Visual blocks (use these in any rendered report)

`render.py` supports custom fenced blocks that turn into visual elements. Prefer these over prose tables — they're more scannable.

| Block | Use for | Format |
|-------|---------|--------|
| ` ```chart ` | **Daily price action (canonical)** | `Label \| v1,v2,v3 \| note` — generate via `build_chart.py` |
| ` ```kpi ` | Snapshot metrics (no time dimension) | `Label \| Value \| Note` per line |
| ` ```scenarios ` | Bull/Base/Bear with bars | `Bull/Base/Bear \| prob% \| target \| descr` |
| ` ```meter ` | 0-10 score bars | `Name \| score \| note` |
| ` ```callout {info\|ok\|warn\|danger} ` | Highlighted box | Free markdown body |
| ` ```timeline ` | Catalysts list | `When \| What` |
| ` ```compare ` | Side-by-side table (categorical) | First row = headers |
| ` ```verdict {hold\|add\|trim\|exit\|watch} ` | Verdict pill | One short phrase |

**Time-series rule:** if data has a time dimension (today's chart vs yesterday's, return over 30d, etc.) → use `chart`. If snapshot-only (vol_ratio, P/E now) → `kpi`/`compare`. **Replace text price grids with charts wherever possible.**

Use them in: digests (always), snapshots (kpi + callout for triggers), comparisons (compare + meter + verdict), quarterly reviews (scenarios + meter for re-score), dashboards (kpi for movers).

### Two views per stock

Every tracked stock has **two views** — keep both in sync:
- `thesis.md` — the deep investment memo (full thesis, agent's primary working document)
- `digest.md` — the visual one-pager (60-second glance, derived from the thesis)

When the user asks about a stock, default to opening the **digest** unless they ask for the full thesis or a snapshot. The digest is the easy entry point; the thesis is for serious study. The [[digest]] skill regenerates digest.md from thesis.md on demand.

## Workflow rhythm

- **Daily** — `watchlist` for one or `watchlist` for everything active
- **Weekly** — `weekly-review` adds Tier-2 data (insider transactions, 13F changes, short interest, analyst revisions)
- **Quarterly** — `quarterly-review` after each earnings print: re-score bull/base/bear, redo reverse-DCF
- **Annual** — `refresh-thesis` for a deep re-research, merging into thesis.md while preserving Stands & Updates

## Policy/federal/military pulse — mandatory routine

Policy and macro news affects stock prices faster than company news, and the user explicitly does NOT want to have to ask each day. **Every `/morning` invocation MUST run the [[pulse]] skill.** Independent of whether any specific stock was mentioned, scan for:

- Fed / FOMC / rates / dot plot
- US politics / SEC / FTC / DOJ / FCC / Treasury / executive orders / court rulings / antitrust
- Tariffs / sanctions / export controls / trade war
- Geopolitics: Iran, China, Russia, Ukraine, Israel, Taiwan, Korea, NATO
- Military / Pentagon / defense / active conflicts
- EU regulation / EU spectrum / GDPR / digital markets

Cross-reference signals with tracked positions (e.g. Iran-Israel → SU/CVX/CNQ, US-China → TSM/NVDA/AMD, FCC → SPCX, Korea → SK Hynix). Surface signals as `callout danger` if they're high-impact (war state change, major Fed pivot, tariff >5%, regulatory action targeting a tracked stock).

Even on quiet days, run it — the absence of policy news is information.

## Attribution rule — explain today's move AND persist it

When a stock moves meaningfully (`|change_pct_1d| >= 3%` OR `|change_pct_5d| >= 10%` OR `volume_ratio >= 1.5x`), the agent MUST:

1. **Attribute** the move with cited reasoning (see `.claude/skills/deep-dive/SKILL.md`).
2. **Record** the attribution to persistent storage. This is mandatory, not optional.

### Why persist

Past attributions are the workspace's most valuable signal-detection asset. When a similar event recurs ("HBM pricing news again", "another oil-cycle scare on SU", "next post-IPO lock-up"), the agent uses the historical record to ground new analysis: "last time this happened, here's what played out."

### How attribution storage works

Two files, kept in sync atomically by `scripts/record_attribution.py`:

- **Per-stock log** — `stocks/{TICKER}/attributions.md` (append-only narrative, human-readable)
- **Structured index** — `attributions/index.jsonl` (one line per attribution, queryable by tag/ticker/date/magnitude/confidence)

### Tag vocabulary

Use ONLY tags from `attributions/README.md`. Inventing new tags pollutes the index. If nothing fits, use `unattributed` — better than fabricating.

### Confidence honesty

- `high` = direct cited catalyst (named headline + cross-stock corroboration)
- `medium` = sector/macro driver but not company-specific
- `low` = flows/sentiment/unattributable

Never inflate confidence to make a story sound cleaner than it is.

### Querying past attributions

When fresh news arrives, the agent runs [[find-similar-moves]] FIRST to surface analogs from history, then writes new analysis citing past patterns. This is how the workspace gets smarter over time.

```bash
uv run --project scripts scripts/find_attributions.py --ticker DRAM --tag memory_pricing
uv run --project scripts scripts/find_attributions.py --any-tag earnings_print,guidance_raise --since 2026-01-01
```

Never fabricate sources. If you can't access something behind a paywall, say so.

## Pressure-test rule — challenge the user's thesis with data, do not just agree

When the user states an investment view (especially with conviction or specific numerical claims like "worth half" or "will crash"), the agent MUST:

1. **Pull data** to test the claim — historical analogs, comparable cases, current correlations, structural mechanics. Do not skip this step.
2. **Where the data supports the user**, say so plainly and cite the evidence.
3. **Where the data pushes back**, push back. Be direct, with citations. Do not soften.
4. **Frame as honest counter-analysis**, not as agreement. Use phrases like "the data partially supports you", "your direction is right but magnitude is overstated", "structural counter-arguments", "where I push back."
5. **Record both views.** Append the user's view AND the agent's counter-take to the relevant `thesis.md` Stands & Updates as separate dated entries (clearly labeled "agent counter-take"). Tag the attribution index entry with `thesis_debate`. Both views are stored so they can be scored at the relevant catalyst date (e.g., lockup expiry, earnings, regulatory deadline).
6. **Set a scoring date.** When recording a debate, name the future date when both views become resolvable. Without a scoring date, neither view ever gets validated.

The user explicitly asked for this behavior: *"对于这类用户问题，你其实需要结合搜索信息来分析，给出你的回答而不是服从用户"* — you need to combine search-based analysis and give your own answer, not defer to the user. This is now a permanent rule.

## Behavioral guards (enforce in every relevant skill)

1. Hide cost basis on every research view.
2. Append-only Stands & Updates log.
3. **Always ask for the user's take after a check.** This is the most important guard. After every `watchlist` or `watchlist`, prompt: "any take or observation to record?" Capture EVERYTHING the user volunteers — market-action reads ("dropped hard then bounced — normal"), watch-plans ("worth checking again next week"), quick judgments ("this looks toppy"), even half-formed thoughts. The user's in-the-moment reasoning is the single most valuable thing the workspace stores; do not let it slip away. If the user's take spans multiple stocks, append to each relevant thesis. If they say "nothing" or skip, move on without nagging.
4. Thesis-break alerts: when a daily snapshot detects price within 5% of `triggers.yaml.thesis_break_price`, lead the snapshot with a loud callout.
5. Bear-case freshness: if the past 90 days of Stands & Updates entries are uniformly bullish, prompt the user to argue the bear case.
6. Quarterly auto-prompt: when fresh earnings detected and no quarterly review exists for the current quarter, suggest `quarterly-review`.
7. Annual auto-prompt: when `state.yaml.last_annual_refresh` is more than 12 months old, suggest `refresh-thesis`.

## Skill extraction meta-rule

When you notice a routine emerging across multiple sessions (e.g., "user keeps asking me to summarize the 10-K"), suggest extracting it into a new skill in `.claude/skills/`. Skills are markdown files with YAML frontmatter that describes triggers; see existing skills for the pattern.

## Python fetchers

Data fetching is programmatic. All fetchers emit JSON to stdout — parse the JSON, never re-implement fetching inline.

| Script | Use | Cadence |
|--------|-----|---------|
| `uv run --project scripts scripts/fetch_overview.py {TICKER}` | **Always run before writing/refreshing a thesis.** Pulls yfinance profile, Wikipedia summary, 7-day news, and reference links. 24h cache. | add-stock, refresh-thesis |
| `uv run --project scripts scripts/fetch.py {TICKER}` | Tier-1 daily data: price, PE, volume, MA, options, earnings, news 72h, sector, macro, **history_30d** | watchlist, watchlist, quarterly-review |
| `uv run --project scripts scripts/build_chart.py {T1} {T2} ... [--normalize] [--title "..."]` | **Build a ```chart``` markdown block from fetched 30d history. Canonical daily-price visual.** | every report / per-ticker tab / compare |
| `uv run --project scripts scripts/fetch_intraday.py {TICKER} [--interval 5m] [--period 1d]` | Intraday bars incl. pre/post-market. Returns full bar series + session summary. | session analysis, earnings day |
| `uv run --project scripts scripts/build_intraday_chart.py {T1} {T2} ... [--interval 5m] [--normalize]` | **Build a ```chart``` block from today's tape (or 5d) with pre/post-market.** | intraday deep-dive, earnings reaction |
| `uv run --project scripts scripts/fetch_insider.py {TICKER}` | SEC EDGAR Form 4 filings index | weekly-review |
| `uv run --project scripts scripts/fetch_13f.py {TICKER}` | SEC EDGAR 13F filings + WhaleWisdom link | weekly-review |

**Never trust training-data knowledge for company facts.** Status (private/public), IPO dates, recent valuations, executives, ARPU, subscriber counts, etc. all change. When you need facts, run `fetch_overview.py` and follow the reference links. If `fetch_overview.py` doesn't have what you need, use WebFetch on Wikipedia, the company IR site, or the EDGAR filings linked in the overview output.

## File layout

```
groups.yaml              watchlist groupings (tech, ai, energy, index, space, ...)
stocks/{TICKER}/
  thesis.md              investment memo (full)         — equities only
  digest.md              visual one-pager (derived)     — equities only
  tracker.md             lighter format                 — ETFs and indexes
  state.yaml             lifecycle metadata
  triggers.yaml          pre-commitment thesis-break + kill conditions
  snapshots/
    YYYY-MM-DD.md        daily check
    reviews/
      YYYY-Qn.md         quarterly re-score
      YYYY-annual.md     annual refresh
dashboard/{YYYY-MM-DD}.md  one file per day; skills append H2 sections (Morning,
                           Attribution, Compare, …); renderer auto-tabs them
site/                      Published artifacts (GitHub Pages source)
  reports/{date}.html      Rendered daily reports (regenerated on demand)
  index.html               Homepage listing latest reports (generated by build_index.py)
```

## Groups & watchlist

`groups.yaml` defines named groups. Stocks may belong to multiple groups; each stock's `state.yaml.tags` mirrors its group memberships. The agent supports natural-language group commands:

- "check tech" / "daily check on tech" → run watchlist on every NVDA/TSLA/IBM/AMZN/AAPL/META/GOOG/MSFT
- "compare ai stocks" → cross-cut on TSM/MU/DRAM/NVDA/INTC/AMD/AVGO/NOK/SNOW/MRVL
- "show me energy" → render dashboard scoped to the energy group
- "add NVDA to space" / "remove NOK from ai" → edit groups.yaml

When the user names a group, scope the skill to that group's members. Inactive members (state.yaml.active=false) are still excluded from reports unless explicitly requested.

## Asset types: equity vs ETF/index

Tracked entities split into two classes:

- **Equities** (companies you'd write a thesis about): get `thesis.md` + `digest.md` per the add-stock skill.
- **ETFs and indexes** (passive exposure, leveraged products, broad market): get `tracker.md` only — a much lighter doc capturing what it tracks, why it's in the watchlist, and key levels. No bull/base/bear, no moat, no reverse-DCF.

The agent decides automatically based on yfinance `quoteType`: `EQUITY` → thesis flow, `ETF`/`INDEX`/`MUTUALFUND` → tracker flow.

## Spec & plan

Design spec: `docs/superpowers/specs/2026-06-18-stock-workspace-design.md`
Implementation plan: `docs/superpowers/plans/2026-06-18-stock-workspace.md`
