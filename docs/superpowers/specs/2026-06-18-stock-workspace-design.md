# Stock Tracking Workspace — Design Spec

**Date:** 2026-06-18
**Owner:** qisiyuan
**Status:** Draft, awaiting user review

## 1. Purpose

A personal, AI-driven workspace for tracking individual stocks. Replaces the current
ad-hoc ChatGPT loop where context is lost between sessions. The workspace is a
persistent knowledge base + on-demand data fetcher + cross-stock dashboard, driven
through natural language by skills the agent invokes.

The user is a serious individual investor doing fundamental research on individual
names. The workspace is informational — no order routing, no portfolio P&L, no
real-time alerts. The user triggers everything explicitly.

## 2. Goals & non-goals

**Goals:**
- Persistent per-stock context (thesis, why-watching, risks, stands).
- On-demand fetching of price, news, and flow proxies — never auto-refresh.
- Pro-grade analysis (using investor frameworks as tools, not as forms the user fills out).
- Cross-stock dashboard that surfaces big movers and big news on each check-in.
- Behavioral guards baked into the workflow (anti-bias, anti-anchoring).
- Skills as repeatable routines, invoked via natural language.
- Anything that emerges as a routine during use should be extracted into a skill.

**Non-goals:**
- No automated scheduling or background fetching.
- No portfolio accounting / cost basis tracking (intentionally hidden — see §7).
- No paid data subscriptions in v1.
- No real-time options flow, dark-pool prints, or institutional money-flow data
  (these require paid tiers — proxies only).

## 3. Directory layout

```
stock/
├── CLAUDE.md                       # workspace rules — agent reads every session
├── README.md                       # human-facing usage notes
├── scripts/
│   ├── fetch.py                    # CLI: uv run fetch.py NVDA → JSON
│   ├── fetch_insider.py            # SEC EDGAR Form 4 (free)
│   ├── fetch_13f.py                # SEC EDGAR / WhaleWisdom (45d lag, free)
│   └── pyproject.toml              # uv-managed deps (yfinance, feedparser, requests)
├── stocks/
│   └── NVDA/
│       ├── thesis.md               # the investment memo (see §5)
│       ├── state.yaml              # active, tags, last_checked, position_size
│       ├── triggers.yaml           # pre-committed thesis-break + kill conditions
│       └── snapshots/
│           ├── 2026-06-18.md       # daily/on-demand snapshot
│           └── reviews/
│               ├── 2026-Q2.md      # quarterly thesis re-score
│               └── 2026-annual.md  # annual deep refresh
├── dashboard/
│   ├── latest.md                   # always overwritten; current cross-stock view
│   └── archive/                    # past dashboards (optional)
├── .skills/                        # routines the agent loads via skill descriptions
│   ├── add-stock/SKILL.md
│   ├── check-stock/SKILL.md
│   ├── check-all/SKILL.md
│   ├── weekly-review/SKILL.md
│   ├── quarterly-review/SKILL.md
│   ├── update-thesis/SKILL.md
│   ├── compare-stocks/SKILL.md
│   ├── refresh-thesis/SKILL.md
│   ├── deactivate-stock/SKILL.md
│   └── check-triggers/SKILL.md
└── docs/
    └── superpowers/specs/...       # this spec lives here
```

**Deactivation:** flips `state.yaml.active: false`. Folder stays in place. Excluded
from `check-all` dashboard but still callable via `check-stock NVDA`.

## 4. Interaction model

Natural language only. The user types things like:

- "add NVDA" / "I want to track Palantir"
- "check NVDA"
- "daily check" / "what's going on"
- "weekly review"
- "quarterly review on NVDA"
- "I'm bullish on NVDA after earnings"
- "compare NVDA vs AMD"
- "I'm done with SHOP"

The agent maps the request to the right skill via skill descriptions. Skills define
the canonical routine; CLAUDE.md tells the agent to prefer skills over ad-hoc behavior.

## 5. thesis.md — the investment memo

The thesis is the persistent knowledge for one stock. The agent **uses professional
frameworks as analytical lenses** — Helmer's 7 Powers for moat, Mauboussin reverse-DCF
for valuation — but **writes the output in plain English judgment, not as fields the
user must understand**. The user reads conclusions and reasoning; the agent does the
framework work behind the scenes.

### Sections

```
# {TICKER} — {Company name}

## One-line thesis
A single falsifiable statement: "In 18–24 months, X will Y because Z; this thesis is
wrong if W." Written by the agent during add-stock; revisable on refresh.

## Snapshot
{tagline} · {sector} · {market cap} · entry {date} · max weight {%}

## What it does
2–4 sentences. Plain English. What the company sells, to whom, and how it makes money.

## Industry & TAM
The market it operates in, total addressable market, growth dynamics. Why this market
matters and what's changing.

## Why I'm watching
The user's specific angle. Captured during add-stock. Why this stock, not the next one.

## Outlook — Bull / Base / Bear
Three scenarios with rough probabilities (sum to 100), each with a price target.
Agent writes these in plain prose: "Bull (30%): Blackwell ramps faster than expected,
data center capex stays elevated through 2027, target $200. Base (50%): ..."

## Moat
Plain-English assessment of competitive advantage. Agent uses Helmer's 7 Powers
internally as a checklist (scale economies, network effects, counter-positioning,
switching costs, branding, cornered resources, process power) but writes the
conclusion as a paragraph: "NVDA's primary moat is process power (CUDA software
ecosystem) layered with switching costs..."

## Management & capital allocation
CEO tenure, ROIC trend, buyback discipline, M&A track record, insider ownership.
Written as judgment: "Jensen Huang has founder-aligned skin in the game; buybacks
have been timed reasonably though insider selling picked up in Q1..."

## Valuation
Two readings:
1. Multiples sanity check — P/E, EV/EBITDA vs the stock's 5-year median and peers.
2. Reverse-DCF — agent computes what growth and margins the current price implies and
   reports it as: "At $142, the market is pricing in roughly 25% revenue growth for
   5 years and 55% gross margins. That's plausible given recent results but leaves
   little room for slippage."

## Balance sheet
Net debt/EBITDA, interest coverage, debt maturity, share count direction. One short
paragraph; flag risk only if real.

## Key metrics to watch
The 3–6 numbers that actually move the thesis. Bullet list.

## Catalysts
Dated events: earnings, product launches, regulatory decisions.

## Disconfirming events
What would make me sell, written in advance. Concrete.

## Position
Entry zone · price target · thesis-break level · current weight vs max
(Cost basis is intentionally not tracked. See §7.)

## Stands & Updates  (append-only)
Dated entries that record the user's evolving view. Never edited.
### 2026-06-18
Bullish on earnings — DC revenue +94% YoY. Holding through next quarter.
```

### state.yaml

```yaml
ticker: NVDA
active: true
tags: [ai, semis, mega-cap]
added: 2026-04-12
last_checked: 2026-06-18
last_quarterly_review: 2026-Q1
last_annual_refresh: 2026-04-12
max_weight_pct: 8
```

### triggers.yaml

The pre-commitment device. Written during add-stock or refresh; the user is asked to
commit explicitly. The agent checks these on every `check-stock` and surfaces hits
loudly at the top of the snapshot.

```yaml
thesis_break_price: 95.00         # if price closes below, re-read thesis or sell
kill_conditions:
  - "Data center revenue growth drops below 20% YoY for two consecutive quarters"
  - "CFO or CEO departure under controversial circumstances"
  - "Major customer (hyperscaler) signals significant own-silicon pivot"
re_read_triggers:
  - "Stock down >15% on no obvious news"
  - "Missed quarter (revenue or EPS)"
  - "Cluster insider selling > $50M in 30 days"
  - "Guidance cut"
```

## 6. Snapshots — what each check captures

### Daily snapshot (`check-stock`)

Tier 1 — every check-in. Stored as `stocks/{TICKER}/snapshots/YYYY-MM-DD.md`.

- Price · day %Δ · 5d %Δ · 30d %Δ
- Market cap · P/E (trailing & forward)
- Volume vs 30d average
- 52-week distance · 50d / 200d MA position · RSI
- Options put/call ratio
- News: 5–10 headlines from last 72h, source + 1-line summary + link
- Earnings: next date, last beat/miss
- Sector ETF relative performance (e.g. SOXX for NVDA)
- Macro line: SPY %Δ, VIX, 10Y yield
- **Trigger check** — if price near `thesis_break_price`, callout at top
- **AI analysis** — 1–2 short paragraphs: what changed vs the thesis, signal flag
  (🔥 material / ⚠ watch / ✅ quiet)

### Weekly review (`weekly-review`)

Tier 2 data, harder to find but high-signal. Written into the same dated snapshot
file when run on the same day, or its own file if standalone.

- Insider Form 4 transactions (SEC EDGAR — directional, cluster buys are the signal)
- Analyst PT/rating revisions over the past week (direction matters more than level)
- Short interest + days-to-cover (FINRA, bi-monthly)
- 13F changes for top 5 institutional holders (45d lag, free via WhaleWisdom)
- Earnings estimate revisions, 3-month trend

### Quarterly review (`quarterly-review`)

Run after each earnings print. Stored as `snapshots/reviews/YYYY-Qn.md`.

- Read 10-Q (or earnings release if 10-Q not yet filed).
- Re-score bull/base/bear probabilities. Document what changed.
- Re-run reverse-DCF — does the implied growth still pencil?
- Update key metrics with fresh numbers.
- Append a quarterly entry to thesis.md "Stands & Updates".

### Annual refresh (`refresh-thesis`)

Heavy. Re-do the deep dive from scratch, read 10-K and proxy, redo reverse-DCF, reassess
moat. Merge into thesis.md preserving the Stands & Updates log. Stored as
`snapshots/reviews/YYYY-annual.md`.

## 7. Behavioral guards (baked into CLAUDE.md)

The workspace physically guards against documented retail-investor failure modes.

1. **Hide cost basis on research views.** The thesis and snapshots show price vs
   target and vs thesis-break level — never vs entry. Cost basis is not stored
   anywhere in the workspace. Reason: anchoring on entry is one of the strongest
   documented sources of return drag (disposition effect, Odean 1998).

2. **Append-only Stands & Updates log.** The agent is instructed to never edit
   prior entries — only append. Hindsight bias mitigation.

3. **Thesis-break alerts.** When `check-stock` sees price within 5% of
   `triggers.yaml.thesis_break_price`, the snapshot leads with a loud callout
   forcing a sell-or-document decision.

4. **Bear-case freshness check.** If the past 90 days of Stands & Updates entries
   are uniformly bullish, the agent prompts: "you've only added bullish updates —
   argue the bear case for 5 minutes."

5. **Quarterly auto-prompt.** When `check-stock` detects fresh earnings and the
   stock has no quarterly review for the current quarter, the agent suggests
   running `quarterly-review`.

6. **Annual auto-prompt.** When `state.yaml.last_annual_refresh` is more than 12
   months old, agent suggests `refresh-thesis`.

These guards are agent rules, not validators. The agent enforces them through how
it writes — not through code that blocks anything.

## 8. Skills

| Skill | Trigger phrases | What it does |
|-------|-----------------|--------------|
| `add-stock` | "add NVDA", "track Palantir" | Deep-dive research; write thesis.md and triggers.yaml; ask 1–2 clarifying questions about the user's angle if not obvious |
| `check-stock` | "check NVDA" | Run `fetch.py NVDA` → write Tier-1 snapshot → run trigger check → append AI analysis |
| `check-all` | "daily check", "what's going on" | Fetch all active stocks in parallel → write `dashboard/latest.md` (table + big-news + variance callouts + cross-stock prose) |
| `weekly-review` | "weekly review", "weekly NVDA" | Run Tier-2 data fetchers (insider, 13F, short, revisions) for one or all active stocks |
| `quarterly-review` | "quarterly NVDA" | Re-score bull/base/bear, update reverse-DCF, write `snapshots/reviews/YYYY-Qn.md` |
| `update-thesis` | "I'm bullish on NVDA after earnings" | Append a dated, append-only entry to thesis.md Stands & Updates |
| `compare-stocks` | "compare NVDA vs AMD", "which AI stock looks best" | Cross-cut; read multiple theses + latest snapshots; write a comparison |
| `refresh-thesis` | "refresh NVDA thesis" | Annual deep refresh; re-research, redo reverse-DCF, merge preserving Stands & Updates |
| `deactivate-stock` | "I'm done with SHOP" | Flip `state.yaml.active: false`. Folder stays. Excluded from check-all |
| `check-triggers` | (auto-runs inside check-stock) | If thesis-break or kill condition met, surface loudly at top of snapshot |

Each skill is a markdown file at `.skills/{name}/SKILL.md` with frontmatter
describing trigger phrases and a body describing the routine.

**Skill-extraction meta-rule:** any new repeatable routine that emerges during use
should be extracted into its own skill. CLAUDE.md instructs the agent to suggest
this proactively when it notices.

## 9. Dashboard

`dashboard/latest.md` is overwritten on every `check-all`. Format:

```
# Dashboard — 2026-06-18

| Ticker | Price  | %Δ    | Vol   | Signal |
|--------|-------:|------:|------:|--------|
| NVDA   | 142.30 | +3.2% | 1.4x  | 🔥     |
| PLTR   |  28.10 | -0.4% | 0.8x  |        |
| AMD    | 165.20 | +1.1% | 2.3x  | ⚠      |

## What changed
- **NVDA** 🔥 — earnings beat, raised guide. See snapshot.
- **AMD** ⚠ — volume spike on no obvious news. Worth a closer look.
- **PLTR** — quiet day.

## Macro
SPY +0.4% · VIX 14.2 · 10Y 4.31%

## Suggested follow-ups
- AMD volume spike → check news + insider Form 4 (run weekly-review on AMD)
- NVDA had earnings → quarterly-review pending
```

When the user asks for a richer view ("show me as HTML"), the agent renders
`dashboard/latest.html` from the same data with sortable columns, color cells, and
links into each stock's latest snapshot.

## 10. Python fetcher contract

Single CLI script. Skills shell out to it and parse JSON.

```
$ uv run scripts/fetch.py NVDA
{
  "ticker": "NVDA",
  "fetched_at": "2026-06-18T14:32:00Z",
  "price": 142.30,
  "change_pct_1d": 3.2,
  "change_pct_5d": 4.1,
  "change_pct_30d": 12.7,
  "market_cap": 3500000000000,
  "pe_trailing": 68.2,
  "pe_forward": 42.1,
  "volume": 51234567,
  "volume_avg_30d": 36000000,
  "volume_ratio": 1.42,
  "high_52w": 153.10,
  "low_52w": 78.20,
  "ma_50d": 138.40,
  "ma_200d": 121.80,
  "rsi_14": 62.3,
  "put_call_ratio": 0.78,
  "next_earnings": "2026-08-21",
  "last_earnings_eps_actual": 0.78,
  "last_earnings_eps_estimate": 0.71,
  "sector_etf": "SOXX",
  "sector_etf_change_pct_1d": 1.8,
  "macro": {"spy_pct": 0.4, "vix": 14.2, "ten_year": 4.31},
  "news": [
    {"title": "...", "source": "Reuters", "ts": "...", "url": "...", "summary": "..."}
  ]
}
```

Dependencies pinned in `scripts/pyproject.toml`, managed by `uv`. No virtualenv
ceremony — `uv run` handles it.

Separate scripts for Tier-2 data:
- `fetch_insider.py NVDA` — Form 4 transactions for the past N days from EDGAR
- `fetch_13f.py NVDA` — top 5 institutional holders + recent changes from EDGAR

## 11. Data sources (free, v1)

| Data | Source | Notes |
|------|--------|-------|
| Price, PE, market cap, volume, options, earnings | yfinance | Primary |
| Filings, Form 4 insider, 13F | SEC EDGAR JSON API | 10 req/s rate limit |
| Short interest | FINRA | Bi-monthly |
| News headlines | Yahoo News / Google News RSS | Free, decent coverage |
| Macro (10Y, VIX) | yfinance / Yahoo | |
| Sector ETF performance | yfinance | |

**Acknowledged gaps (not fixed in v1):**
- Real-time options flow → would need Unusual Whales (~$50/mo) or similar
- Earnings call transcripts at scale → Seeking Alpha Premium or AlphaSense
- Intraday estimate revisions → Visible Alpha or Bloomberg

If a gap becomes painful, the cheapest meaningful upgrade is **Koyfin or Stock Rover
($10–25/mo)** — flag this in CLAUDE.md as the path.

## 12. CLAUDE.md (workspace rules — outline)

The workspace root CLAUDE.md tells the agent:

1. This is a stock-tracking workspace; behavior is driven by skills in `.skills/`.
2. Never auto-fetch or auto-refresh — only on explicit user request.
3. Map natural-language requests to skills; prefer skills over ad-hoc routines.
4. When a new repeatable routine emerges, suggest extracting it into a skill.
5. Behavioral guards (§7) are mandatory — list them.
6. Use professional frameworks (7 Powers, reverse-DCF) as analytical lenses, but
   write outputs in plain English judgment, not jargon-laden forms.
7. Append-only Stands & Updates log. Never edit prior entries.
8. Cost basis is intentionally not stored — do not ask the user for it, do not
   accept it. Surface price vs target/stop only.
9. The honest data limits — what's a proxy, what's free, when to flag a gap.

## 13. Open questions / future work

- Whether to add a "watchlist" tier (lighter than full thesis — for stocks the user
  is just monitoring before committing to a deep dive). Defer to v2.
- Whether to add a portfolio-level view (correlation, sector concentration, factor
  exposure). Defer — this is portfolio management, not stock research.
- Whether to wire any LLM-summarization of earnings call transcripts when they're
  available (free via IR sites, irregular formats). Defer.
- Whether to add a search index across all theses for cross-cutting queries
  ("which of my stocks have CUDA exposure"). Defer until library size warrants.

## 14. Implementation order (rough)

1. Workspace skeleton (CLAUDE.md, README.md, directory tree).
2. `scripts/fetch.py` with `pyproject.toml`.
3. `add-stock` and `check-stock` skills (the MVP loop — add a stock and check it).
4. `update-thesis` and `deactivate-stock` (lifecycle minimums).
5. `check-all` and dashboard generation.
6. `weekly-review` (Tier-2 fetchers — insider, 13F, short).
7. `quarterly-review` and `refresh-thesis`.
8. `compare-stocks`.
9. Behavioral guard refinements based on real usage.

The detailed implementation plan is produced separately by the writing-plans skill
after this spec is approved.
