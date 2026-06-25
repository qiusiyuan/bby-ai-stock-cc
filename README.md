# bby's stock notes

A personal investment journal driven by an AI workspace.

**Live site:** [qiusiyuan.github.io/bby-ai-stock-cc](https://qiusiyuan.github.io/bby-ai-stock-cc/)

> ⚠️ Personal notes only. Nothing here is financial advice or a recommendation to
> buy or sell any security. Numbers are sourced best-effort from public feeds;
> do your own research.

---

## What this is

I track a handful of individual stocks (mostly AI / semis / energy) and write a
short report most evenings — combining the day's price action, news, my own take,
and a running thesis per name. The whole thing runs inside a Claude Code
workspace and the markdown reports get rendered to HTML and published here.

- **Per-day reports:** [`dashboard/{YYYY-MM-DD}.md`](dashboard/) — published as
  HTML at `site/reports/dashboard-{date}-md.html`
- **Per-stock thesis:** [`stocks/{TICKER}/thesis.md`](stocks/) — the long-form
  memo (bull / base / bear, moat, valuation, kill conditions)
- **Per-stock digest:** [`stocks/{TICKER}/digest.md`](stocks/) — the 60-second
  visual one-pager
- **Skills:** [`.skills/`](.skills/) — natural-language routines the agent uses
  (one markdown file per skill)
- **Fetchers:** [`scripts/`](scripts/) — Python scripts pulling yfinance + SEC
  data; no API keys; all JSON-out for clean parsing

## How daily publishing works

```
1. Generate today's report (talk to the agent: "今天的 report")
   → writes dashboard/2026-06-25.md
2. scripts/publish.sh
   → renders site/reports/dashboard-2026-06-25-md.html
   → rebuilds site/index.html
   → git commit + push
3. GitHub Pages picks up the new HTML (≈ 30–90 seconds)
4. Live at https://qiusiyuan.github.io/bby-ai-stock-cc/
```

The publish script is in [`scripts/publish.sh`](scripts/publish.sh). It accepts
an optional date (`scripts/publish.sh 2026-06-25`) and a `--no-push` flag if you
want to stage commits locally without pushing.

## How a single report gets built

The day's report is composed by an orchestrator skill ([`.skills/report/`](
.skills/report/SKILL.md)) which delegates to module skills:

- **pulse** — indices, VIX, rates, FX, oil, top headlines, policy scan
- **watchlist** — per-stock grid + threshold-crossing flags
- **timeline** — earnings / FOMC / catalysts in the next 30d
- **cluster** — one tab per topic ("DRAM/HBM", "AI capex", "TSLA", etc.)
- **brief** — AI synthesis of the above
- **earnings-scorecard** — when a tracked stock has a pre-committed evaluation
  on a print day, scores the actuals against the bars set in advance

## Local setup (if you want to run it yourself)

```bash
cd scripts
uv sync
```

That installs Python deps. The agent runs everything else
(`uv run --project scripts scripts/fetch.py {TICKER}`) when prompted.

## Conventions

The workspace has explicit rules to keep the notes honest:

- **No cost basis stored.** Entry price / position size / dollar amounts are
  intentionally not recorded. Reasoning: anchoring on entry price is one of the
  best-documented sources of return drag for individual investors.
- **Stands & Updates is append-only.** Once a view is logged with a date, it
  stays. Even if I'm wrong later, the original entry doesn't get edited.
- **Pre-commit scorecards.** When a single blowout earnings spawns a "this is
  the next NVDA" narrative, I write a scorecard *before* the next print
  specifying the bars that would validate or break the claim — then score
  against those bars when the print lands. (See `stocks/MU/research/` for the
  current live example.)
- **Honest data limits.** Free data sources have gaps. When something material
  isn't available (real institutional flow, options flow, transcripts at scale),
  the agent flags it rather than fabricating.

## Repo layout

```
.skills/                 Natural-language routines (markdown w/ YAML frontmatter)
scripts/                 Python: fetchers, render, build_index, publish
stocks/{TICKER}/
  thesis.md              Investment memo (full)
  digest.md              Visual one-pager (derived)
  state.yaml             Lifecycle metadata (active, tags, earnings_watchlist)
  triggers.yaml          Thesis-break + kill conditions
  research/              Pre-commit scorecards, deeper dives
  attributions.md        Append-only log of meaningful price moves with cited causes
  snapshots/             Daily / weekly / quarterly check-ins
dashboard/{date}.md      One file per day; renderer auto-tabs by H2 section
site/                    Published artifacts (GitHub Pages source)
  index.html             Homepage listing latest reports
  reports/{date}.html    Rendered daily reports
groups.yaml              Watchlist groupings (focus / tech / ai / energy / …)
timeline.yaml            Catalyst calendar (manually + auto-merged from yfinance)
attributions/index.jsonl Structured index of attributions (queryable by tag)
AGENTS.md                Workspace rules for the agent (CLAUDE.md equivalent)
```

## License

Source code in `scripts/` is MIT. The markdown notes in `stocks/` and
`dashboard/` are personal opinions — you're welcome to read them, but don't
republish them as a service or as financial advice.
