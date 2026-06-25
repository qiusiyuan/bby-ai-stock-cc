# Stock Tracking Workspace Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an AI-driven personal stock-tracking workspace where the user maintains persistent per-stock investment memos, triggers on-demand data fetches via natural language, and gets pro-grade analysis (with behavioral guards baked in) — all driven through skills the agent invokes.

**Architecture:** Workspace is a flat directory of markdown + YAML files (one folder per ticker). Python CLI fetchers (`scripts/fetch.py`, `scripts/fetch_insider.py`, `scripts/fetch_13f.py`) emit JSON; skills shell out, parse, and write files. Agent behavior is governed by `CLAUDE.md` and the skill markdown files in `.skills/`. No server, no database — just files and on-demand python.

**Tech Stack:**
- Python 3.11+ via `uv` (`uv run scripts/fetch.py NVDA`)
- `yfinance`, `feedparser`, `requests`, `pyyaml`, `pytest` (in `scripts/pyproject.toml`)
- Skills as `.skills/{name}/SKILL.md` markdown files with YAML frontmatter
- Workspace root `CLAUDE.md` defines agent rules
- Git for snapshots/history

**Reference spec:** `docs/superpowers/specs/2026-06-18-stock-workspace-design.md`

---

## File structure

```
stock/
├── CLAUDE.md                          # workspace rules (Task 2)
├── README.md                          # human-facing usage notes (Task 2)
├── .gitignore                         # Task 1
├── scripts/
│   ├── pyproject.toml                 # uv project (Task 3)
│   ├── fetch.py                       # Tier-1 CLI fetcher (Tasks 4-7)
│   ├── fetch_insider.py               # SEC EDGAR Form 4 (Task 14)
│   ├── fetch_13f.py                   # SEC EDGAR 13F (Task 15)
│   └── tests/
│       ├── test_fetch.py              # (Tasks 4-7)
│       ├── test_fetch_insider.py      # (Task 14)
│       └── test_fetch_13f.py          # (Task 15)
├── stocks/
│   └── .gitkeep                       # Task 1
├── dashboard/
│   └── .gitkeep                       # Task 1
├── .skills/
│   ├── add-stock/SKILL.md             # Task 8
│   ├── check-stock/SKILL.md           # Task 9
│   ├── update-thesis/SKILL.md         # Task 10
│   ├── deactivate-stock/SKILL.md      # Task 11
│   ├── check-all/SKILL.md             # Task 12
│   ├── check-triggers/SKILL.md        # Task 13 (used by check-stock)
│   ├── weekly-review/SKILL.md         # Task 16
│   ├── quarterly-review/SKILL.md      # Task 17
│   ├── refresh-thesis/SKILL.md        # Task 18
│   └── compare-stocks/SKILL.md        # Task 19
└── docs/superpowers/
    ├── specs/2026-06-18-stock-workspace-design.md  (already exists)
    └── plans/2026-06-18-stock-workspace.md         (this file)
```

**File responsibilities:**
- `CLAUDE.md` — single source of truth for agent rules (skills-first, no auto-refresh, behavioral guards, no cost basis, append-only logs).
- `scripts/fetch.py` — Tier-1 data per ticker, JSON to stdout. The contract that all daily-checking skills depend on.
- `scripts/fetch_insider.py` / `fetch_13f.py` — Tier-2 data, separate scripts because they hit a different source (SEC EDGAR) and run on a different cadence.
- Each skill file is self-contained — describes triggers + step-by-step routine. The agent loads the skill on a matching natural-language phrase.
- `stocks/{TICKER}/thesis.md` — investment memo (Section 5 of the spec).
- `stocks/{TICKER}/state.yaml` — lifecycle metadata.
- `stocks/{TICKER}/triggers.yaml` — pre-commitment device.
- `stocks/{TICKER}/snapshots/YYYY-MM-DD.md` — dated daily check.
- `stocks/{TICKER}/snapshots/reviews/YYYY-Qn.md` — quarterly re-score.
- `dashboard/latest.md` — overwritten on each `check-all`.

**Implementation order rationale:** scaffold → fetcher → MVP loop (add + check) → lifecycle (update/deactivate) → dashboard → Tier-2 fetchers → review cadences → comparison. Each task produces working software; you can stop after any task and have a usable workspace.

---

## Task 1: Workspace scaffold

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.gitignore`
- Create: `/Users/qisiyuan/Documents/Self/stock/stocks/.gitkeep`
- Create: `/Users/qisiyuan/Documents/Self/stock/dashboard/.gitkeep`
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/.gitkeep`
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/.gitkeep`

- [ ] **Step 1: Initialize git repo**

Run from `/Users/qisiyuan/Documents/Self/stock`:
```bash
git init
```
Expected: `Initialized empty Git repository in /Users/qisiyuan/Documents/Self/stock/.git/`

- [ ] **Step 2: Create directory tree**

```bash
mkdir -p stocks dashboard scripts/tests .skills docs/superpowers/specs docs/superpowers/plans
```

- [ ] **Step 3: Create .gitignore**

Write `/Users/qisiyuan/Documents/Self/stock/.gitignore`:

```
# Python
__pycache__/
*.pyc
.venv/
.uv-cache/

# Editor / OS
.DS_Store
.idea/
.vscode/
*.swp

# Build artifacts
*.egg-info/
dist/
build/

# Local cache for fetcher (if added later)
.cache/
```

- [ ] **Step 4: Create .gitkeep files**

```bash
touch stocks/.gitkeep dashboard/.gitkeep scripts/.gitkeep .skills/.gitkeep
```

- [ ] **Step 5: Verify the tree**

Run:
```bash
ls -la
```
Expected: see `.git`, `.gitignore`, `.skills`, `dashboard`, `docs`, `scripts`, `stocks`.

- [ ] **Step 6: Commit**

```bash
git add .gitignore stocks/.gitkeep dashboard/.gitkeep scripts/.gitkeep .skills/.gitkeep
git commit -m "chore: scaffold workspace directory tree"
```

---

## Task 2: Workspace CLAUDE.md and README.md

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/CLAUDE.md`
- Create: `/Users/qisiyuan/Documents/Self/stock/README.md`

- [ ] **Step 1: Write CLAUDE.md**

Write `/Users/qisiyuan/Documents/Self/stock/CLAUDE.md`:

````markdown
# Stock Tracking Workspace

This is a personal AI-driven stock-tracking workspace. The user is a serious individual investor doing fundamental research on individual names. Behavior is driven by skills in `.skills/`, invoked through natural language.

## Core rules

1. **Skills first.** When the user asks about a stock or the workspace, map the request to a skill in `.skills/` and follow it. Do not improvise routines — if a request doesn't fit an existing skill, suggest extracting one.

2. **No auto-refresh.** Never fetch data without an explicit user request. Every data fetch is a deliberate user trigger.

3. **No cost basis.** The workspace intentionally does not store entry prices, position size in dollars, or cost basis. Do not ask for it; if the user volunteers it, do not record it. Show price vs target and vs thesis-break level only. Reason: anchoring on entry is one of the strongest documented sources of return drag.

4. **Append-only logs.** The "Stands & Updates" section in each `thesis.md` is append-only. Add new dated entries; never edit prior entries.

5. **Use frameworks as analytical lenses, not as forms.** When writing analysis (moat, valuation, etc.), use professional frameworks behind the scenes (Helmer's 7 Powers for moat, Mauboussin reverse-DCF for valuation) but write outputs in plain English judgment. The user reads conclusions, not jargon-laden tables.

6. **Honest data limits.** Free data sources have gaps:
   - Real institutional money flow → not free; we use volume-weighted proxies and label them as such
   - Real-time options flow → not free
   - Earnings call transcripts at scale → not free
   When a gap is material, flag it. The cheapest meaningful upgrade is Koyfin or Stock Rover ($10–25/mo).

## Workflow rhythm

- **Daily** — `check-stock` for one or `check-all` for everything active
- **Weekly** — `weekly-review` adds Tier-2 data (insider transactions, 13F changes, short interest, analyst revisions)
- **Quarterly** — `quarterly-review` after each earnings print: re-score bull/base/bear, redo reverse-DCF
- **Annual** — `refresh-thesis` for a deep re-research, merging into thesis.md while preserving Stands & Updates

## Behavioral guards (enforce in every relevant skill)

1. Hide cost basis on every research view.
2. Append-only Stands & Updates log.
3. Thesis-break alerts: when a daily snapshot detects price within 5% of `triggers.yaml.thesis_break_price`, lead the snapshot with a loud callout.
4. Bear-case freshness: if the past 90 days of Stands & Updates entries are uniformly bullish, prompt the user to argue the bear case.
5. Quarterly auto-prompt: when fresh earnings detected and no quarterly review exists for the current quarter, suggest `quarterly-review`.
6. Annual auto-prompt: when `state.yaml.last_annual_refresh` is more than 12 months old, suggest `refresh-thesis`.

## Skill extraction meta-rule

When you notice a routine emerging across multiple sessions (e.g., "user keeps asking me to summarize the 10-K"), suggest extracting it into a new skill in `.skills/`. Skills are markdown files with YAML frontmatter that describes triggers; see existing skills for the pattern.

## Python fetchers

Data fetching is programmatic. Use `uv run scripts/fetch.py {TICKER}` for Tier-1 data, `uv run scripts/fetch_insider.py {TICKER}` and `uv run scripts/fetch_13f.py {TICKER}` for Tier-2. All emit JSON to stdout. Parse the JSON; never re-implement fetching inline.

## File layout

```
stocks/{TICKER}/
  thesis.md              investment memo
  state.yaml             lifecycle metadata
  triggers.yaml          pre-commitment thesis-break + kill conditions
  snapshots/
    YYYY-MM-DD.md        daily check
    reviews/
      YYYY-Qn.md         quarterly re-score
      YYYY-annual.md     annual refresh
dashboard/latest.md      cross-stock view
```

## Spec & plan

Design spec: `docs/superpowers/specs/2026-06-18-stock-workspace-design.md`
Implementation plan: `docs/superpowers/plans/2026-06-18-stock-workspace.md`
````

- [ ] **Step 2: Write README.md**

Write `/Users/qisiyuan/Documents/Self/stock/README.md`:

```markdown
# Stock Tracking Workspace

A personal AI-driven workspace for tracking individual stocks. Persistent investment memos per stock + on-demand data fetching + cross-stock dashboard, all driven through natural language.

## How to use

Just talk to the agent in natural language. Example phrases:

- "add NVDA" / "I want to track Palantir" → deep-dive research, write the thesis
- "check NVDA" → fetch latest data, write a dated snapshot, analyze vs thesis
- "daily check" / "what's going on" → check everything active, build the dashboard
- "weekly review" → pull Tier-2 data (insider transactions, 13F, short interest)
- "quarterly review on NVDA" → post-earnings re-score
- "I'm bullish on NVDA after earnings" → append a stand to the thesis log
- "compare NVDA vs AMD" → cross-cut analysis
- "refresh NVDA thesis" → annual deep refresh
- "I'm done with SHOP" → deactivate

## Setup

Once:

```bash
cd scripts
uv sync
```

Then the agent runs `uv run scripts/fetch.py {TICKER}` itself when needed.

## Structure

- `stocks/` — one folder per ticker
- `dashboard/latest.md` — cross-stock view, regenerated on `daily check`
- `scripts/` — python data fetchers
- `.skills/` — natural-language routines the agent uses
- `CLAUDE.md` — workspace rules
- `docs/superpowers/` — spec and plan
```

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md README.md
git commit -m "docs: add CLAUDE.md (agent rules) and README"
```

---

## Task 3: Python project (scripts/pyproject.toml)

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/pyproject.toml`

- [ ] **Step 1: Write pyproject.toml**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/pyproject.toml`:

```toml
[project]
name = "stock-fetchers"
version = "0.1.0"
description = "Python data fetchers for the stock tracking workspace"
requires-python = ">=3.11"
dependencies = [
    "yfinance>=0.2.40",
    "feedparser>=6.0.11",
    "requests>=2.32.0",
    "pyyaml>=6.0.2",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "pytest-mock>=3.12",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 2: Verify uv resolves the project**

```bash
cd scripts && uv sync --extra dev
```
Expected: `Resolved N packages in ...` and `.venv/` created inside `scripts/`. No errors.

- [ ] **Step 3: Verify pytest is available**

```bash
cd scripts && uv run pytest --version
```
Expected: `pytest 8.x.x`

- [ ] **Step 4: Commit**

```bash
git add scripts/pyproject.toml scripts/uv.lock
git commit -m "chore: init python project for fetchers"
```

---

## Task 4: fetch.py — price/quote core (TDD)

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/fetch.py`
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/tests/__init__.py`
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`

This task builds the price/PE/volume/MA core. News, earnings, options, macro come in Tasks 5-7.

- [ ] **Step 1: Create empty test package init**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/tests/__init__.py` with empty content (single empty line).

- [ ] **Step 2: Write the failing test**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`:

```python
"""Tests for fetch.py — price/quote core."""
from unittest.mock import MagicMock, patch

import pandas as pd

from fetch import build_quote


def _mock_ticker(*, info, history):
    t = MagicMock()
    t.info = info
    t.history.return_value = history
    return t


def test_build_quote_extracts_core_fields():
    history = pd.DataFrame(
        {"Close": [100.0] * 199 + [142.30], "Volume": [50_000_000] * 199 + [70_000_000]},
        index=pd.date_range("2025-09-01", periods=200),
    )
    info = {
        "currentPrice": 142.30,
        "marketCap": 3_500_000_000_000,
        "trailingPE": 68.2,
        "forwardPE": 42.1,
        "fiftyTwoWeekHigh": 153.10,
        "fiftyTwoWeekLow": 78.20,
    }
    ticker = _mock_ticker(info=info, history=history)

    quote = build_quote("NVDA", ticker)

    assert quote["ticker"] == "NVDA"
    assert quote["price"] == 142.30
    assert quote["market_cap"] == 3_500_000_000_000
    assert quote["pe_trailing"] == 68.2
    assert quote["pe_forward"] == 42.1
    assert quote["high_52w"] == 153.10
    assert quote["low_52w"] == 78.20
    # 1d change vs prior close (100.0 → 142.30)
    assert round(quote["change_pct_1d"], 2) == 42.30
    # volume ratio = 70M / 30d avg
    assert quote["volume"] == 70_000_000
    assert quote["volume_ratio"] > 1.0
    # MAs
    assert quote["ma_50d"] is not None
    assert quote["ma_200d"] is not None


def test_build_quote_handles_missing_pe_gracefully():
    history = pd.DataFrame(
        {"Close": [100.0] * 50, "Volume": [10_000_000] * 50},
        index=pd.date_range("2026-04-30", periods=50),
    )
    info = {"currentPrice": 100.0, "marketCap": 1_000_000}  # no PE keys
    ticker = _mock_ticker(info=info, history=history)

    quote = build_quote("XYZ", ticker)

    assert quote["pe_trailing"] is None
    assert quote["pe_forward"] is None
    # 200d MA can't be computed with only 50 rows
    assert quote["ma_200d"] is None
    assert quote["ma_50d"] is not None
```

- [ ] **Step 3: Run the test, expect ImportError**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: `ModuleNotFoundError: No module named 'fetch'` (or ImportError on `build_quote`).

- [ ] **Step 4: Implement fetch.py**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/fetch.py`:

```python
"""Tier-1 stock data fetcher. CLI: uv run fetch.py TICKER -> JSON to stdout."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from typing import Any

import yfinance as yf


def build_quote(ticker_symbol: str, ticker: yf.Ticker) -> dict[str, Any]:
    """Build the price/quote core from a yfinance Ticker."""
    info = ticker.info or {}
    history = ticker.history(period="1y", interval="1d")

    closes = history["Close"] if "Close" in history.columns else None
    volumes = history["Volume"] if "Volume" in history.columns else None

    price = info.get("currentPrice") or (float(closes.iloc[-1]) if closes is not None and len(closes) else None)

    def pct_change(window: int) -> float | None:
        if closes is None or len(closes) <= window:
            return None
        prior = float(closes.iloc[-(window + 1)])
        if prior == 0:
            return None
        return round((price - prior) / prior * 100, 2)

    def moving_avg(window: int) -> float | None:
        if closes is None or len(closes) < window:
            return None
        return round(float(closes.iloc[-window:].mean()), 2)

    volume = int(volumes.iloc[-1]) if volumes is not None and len(volumes) else None
    avg_vol_30d = (
        int(volumes.iloc[-30:].mean())
        if volumes is not None and len(volumes) >= 30
        else None
    )
    volume_ratio = (
        round(volume / avg_vol_30d, 2)
        if volume is not None and avg_vol_30d
        else None
    )

    return {
        "ticker": ticker_symbol,
        "price": price,
        "change_pct_1d": pct_change(1),
        "change_pct_5d": pct_change(5),
        "change_pct_30d": pct_change(30),
        "market_cap": info.get("marketCap"),
        "pe_trailing": info.get("trailingPE"),
        "pe_forward": info.get("forwardPE"),
        "volume": volume,
        "volume_avg_30d": avg_vol_30d,
        "volume_ratio": volume_ratio,
        "high_52w": info.get("fiftyTwoWeekHigh"),
        "low_52w": info.get("fiftyTwoWeekLow"),
        "ma_50d": moving_avg(50),
        "ma_200d": moving_avg(200),
    }


def fetch(ticker_symbol: str) -> dict[str, Any]:
    ticker_symbol = ticker_symbol.upper()
    ticker = yf.Ticker(ticker_symbol)
    payload = {
        "ticker": ticker_symbol,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    payload.update(build_quote(ticker_symbol, ticker))
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Tier-1 data for a ticker")
    parser.add_argument("ticker", help="Ticker symbol, e.g. NVDA")
    args = parser.parse_args()
    payload = fetch(args.ticker)
    json.dump(payload, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run the tests, expect PASS**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: 2 passed.

- [ ] **Step 6: Smoke-test the CLI against real network (optional but useful)**

```bash
cd scripts && uv run python fetch.py NVDA
```
Expected: JSON object with `ticker`, `price`, `pe_trailing`, etc. Network call to Yahoo. If it fails (offline / rate-limited), the unit tests still pass — that's the point.

- [ ] **Step 7: Commit**

```bash
git add scripts/fetch.py scripts/tests/__init__.py scripts/tests/test_fetch.py
git commit -m "feat(fetch): add price/quote core with tests"
```

---

## Task 5: fetch.py — earnings & options (TDD)

**Files:**
- Modify: `/Users/qisiyuan/Documents/Self/stock/scripts/fetch.py`
- Modify: `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`

- [ ] **Step 1: Append failing tests**

Append to `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`:

```python
import pandas as pd
from datetime import date

from fetch import build_earnings, build_options


def test_build_earnings_extracts_next_date_and_last_print():
    calendar = {"Earnings Date": [date(2026, 8, 21)]}
    earnings_dates = pd.DataFrame(
        {
            "EPS Estimate": [0.71, 0.65],
            "Reported EPS": [0.78, 0.66],
            "Surprise(%)": [9.86, 1.54],
        },
        index=pd.to_datetime(["2026-05-22", "2026-02-21"]),
    )
    ticker = MagicMock()
    ticker.calendar = calendar
    ticker.earnings_dates = earnings_dates

    earnings = build_earnings(ticker)

    assert earnings["next_earnings"] == "2026-08-21"
    assert earnings["last_earnings_eps_actual"] == 0.78
    assert earnings["last_earnings_eps_estimate"] == 0.71


def test_build_earnings_handles_missing_data():
    ticker = MagicMock()
    ticker.calendar = {}
    ticker.earnings_dates = None

    earnings = build_earnings(ticker)

    assert earnings == {
        "next_earnings": None,
        "last_earnings_eps_actual": None,
        "last_earnings_eps_estimate": None,
    }


def test_build_options_computes_put_call_ratio():
    ticker = MagicMock()
    ticker.options = ("2026-07-18",)
    chain = MagicMock()
    chain.calls = pd.DataFrame({"openInterest": [100, 200, 300]})  # total 600
    chain.puts = pd.DataFrame({"openInterest": [150, 150]})  # total 300
    ticker.option_chain.return_value = chain

    options = build_options(ticker)

    assert options["put_call_ratio"] == 0.5  # 300 / 600


def test_build_options_handles_no_chain():
    ticker = MagicMock()
    ticker.options = ()

    options = build_options(ticker)

    assert options == {"put_call_ratio": None}
```

- [ ] **Step 2: Run, expect failures**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: ImportError on `build_earnings` and `build_options`.

- [ ] **Step 3: Implement build_earnings and build_options**

Insert into `/Users/qisiyuan/Documents/Self/stock/scripts/fetch.py` *before* `def fetch(`:

```python
def build_earnings(ticker: yf.Ticker) -> dict[str, Any]:
    """Next earnings date + last beat/miss."""
    next_earnings: str | None = None
    try:
        cal = ticker.calendar or {}
        dates = cal.get("Earnings Date") if isinstance(cal, dict) else None
        if dates:
            first = dates[0]
            next_earnings = first.isoformat() if hasattr(first, "isoformat") else str(first)
    except Exception:
        next_earnings = None

    last_actual: float | None = None
    last_estimate: float | None = None
    try:
        ed = ticker.earnings_dates
        if ed is not None and len(ed):
            ed_sorted = ed.sort_index(ascending=False)
            for _, row in ed_sorted.iterrows():
                actual = row.get("Reported EPS")
                estimate = row.get("EPS Estimate")
                if actual is not None and not _is_nan(actual):
                    last_actual = float(actual)
                    last_estimate = float(estimate) if estimate is not None and not _is_nan(estimate) else None
                    break
    except Exception:
        pass

    return {
        "next_earnings": next_earnings,
        "last_earnings_eps_actual": last_actual,
        "last_earnings_eps_estimate": last_estimate,
    }


def build_options(ticker: yf.Ticker) -> dict[str, Any]:
    """Put/call ratio from nearest expiration's open interest."""
    try:
        expirations = ticker.options or ()
        if not expirations:
            return {"put_call_ratio": None}
        chain = ticker.option_chain(expirations[0])
        calls_oi = float(chain.calls["openInterest"].fillna(0).sum()) if "openInterest" in chain.calls else 0.0
        puts_oi = float(chain.puts["openInterest"].fillna(0).sum()) if "openInterest" in chain.puts else 0.0
        if calls_oi == 0:
            return {"put_call_ratio": None}
        return {"put_call_ratio": round(puts_oi / calls_oi, 2)}
    except Exception:
        return {"put_call_ratio": None}


def _is_nan(x: Any) -> bool:
    try:
        import math

        return isinstance(x, float) and math.isnan(x)
    except Exception:
        return False
```

Modify `fetch()` so the payload includes the new sections — replace the body of `fetch()` with:

```python
def fetch(ticker_symbol: str) -> dict[str, Any]:
    ticker_symbol = ticker_symbol.upper()
    ticker = yf.Ticker(ticker_symbol)
    payload: dict[str, Any] = {
        "ticker": ticker_symbol,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    payload.update(build_quote(ticker_symbol, ticker))
    payload.update(build_earnings(ticker))
    payload.update(build_options(ticker))
    return payload
```

- [ ] **Step 4: Run, expect PASS**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: 6 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/fetch.py scripts/tests/test_fetch.py
git commit -m "feat(fetch): add earnings + options sections"
```

---

## Task 6: fetch.py — news from Yahoo RSS (TDD)

**Files:**
- Modify: `/Users/qisiyuan/Documents/Self/stock/scripts/fetch.py`
- Modify: `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`

- [ ] **Step 1: Append failing test**

Append to `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`:

```python
from fetch import build_news


def test_build_news_filters_to_72h_and_caps_at_10(mocker):
    now = datetime(2026, 6, 18, 14, 0, tzinfo=timezone.utc)
    fresh_ts = (now.replace(hour=10)).timestamp()
    stale_ts = (now.replace(day=14)).timestamp()  # 4 days old
    fake_feed = MagicMock()
    fake_feed.entries = [
        MagicMock(
            title=f"Headline {i}",
            link=f"https://example.com/{i}",
            published_parsed=_to_struct_time(fresh_ts),
            summary=f"Summary {i}",
            source=MagicMock(title="Yahoo"),
        )
        for i in range(15)
    ] + [
        MagicMock(
            title="Stale",
            link="https://example.com/stale",
            published_parsed=_to_struct_time(stale_ts),
            summary="Old news",
            source=MagicMock(title="Yahoo"),
        )
    ]
    mocker.patch("fetch.feedparser.parse", return_value=fake_feed)
    mocker.patch("fetch._utcnow", return_value=now)

    news = build_news("NVDA")

    assert len(news) == 10
    titles = [n["title"] for n in news]
    assert "Stale" not in titles
    assert all(n["url"].startswith("https://example.com/") for n in news)


def _to_struct_time(epoch: float):
    import time

    return time.gmtime(epoch)
```

Add at the top of `test_fetch.py` if not already present:

```python
from datetime import datetime, timezone
```

- [ ] **Step 2: Run, expect ImportError**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: ImportError on `build_news`.

- [ ] **Step 3: Implement build_news**

Add the import at the top of `fetch.py` (with the other imports):

```python
import time
import feedparser
```

Add helper before `build_quote`:

```python
def _utcnow() -> datetime:
    return datetime.now(timezone.utc)
```

Add `build_news` before `def fetch(`:

```python
def build_news(ticker_symbol: str, limit: int = 10, hours: int = 72) -> list[dict[str, Any]]:
    """Fetch headlines from Yahoo Finance RSS, filter to last `hours`, cap at `limit`."""
    url = f"https://finance.yahoo.com/rss/headline?s={ticker_symbol}"
    feed = feedparser.parse(url)
    cutoff = _utcnow().timestamp() - hours * 3600
    out: list[dict[str, Any]] = []
    for entry in getattr(feed, "entries", []):
        ts_struct = getattr(entry, "published_parsed", None)
        if not ts_struct:
            continue
        ts_epoch = time.mktime(ts_struct)  # struct_time is UTC from feedparser
        if ts_epoch < cutoff:
            continue
        source = ""
        src_obj = getattr(entry, "source", None)
        if src_obj is not None:
            source = getattr(src_obj, "title", "") or ""
        out.append({
            "title": getattr(entry, "title", ""),
            "url": getattr(entry, "link", ""),
            "source": source or "Yahoo",
            "published_at": datetime.fromtimestamp(ts_epoch, tz=timezone.utc).isoformat(timespec="seconds"),
            "summary": getattr(entry, "summary", "") or "",
        })
        if len(out) >= limit:
            break
    return out
```

Modify `fetch()` to include news:

```python
def fetch(ticker_symbol: str) -> dict[str, Any]:
    ticker_symbol = ticker_symbol.upper()
    ticker = yf.Ticker(ticker_symbol)
    payload: dict[str, Any] = {
        "ticker": ticker_symbol,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    payload.update(build_quote(ticker_symbol, ticker))
    payload.update(build_earnings(ticker))
    payload.update(build_options(ticker))
    payload["news"] = build_news(ticker_symbol)
    return payload
```

- [ ] **Step 4: Run, expect PASS**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: 7 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/fetch.py scripts/tests/test_fetch.py
git commit -m "feat(fetch): add Yahoo RSS news with 72h window"
```

---

## Task 7: fetch.py — sector ETF + macro (TDD)

**Files:**
- Modify: `/Users/qisiyuan/Documents/Self/stock/scripts/fetch.py`
- Modify: `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`

- [ ] **Step 1: Append failing tests**

Append to `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch.py`:

```python
from fetch import build_macro, sector_etf_for


def test_sector_etf_lookup_known_ticker():
    assert sector_etf_for("NVDA") == "SOXX"
    assert sector_etf_for("AAPL") == "XLK"
    assert sector_etf_for("UNKNOWN_TICKER") is None


def test_build_macro_pulls_spy_vix_tnx(mocker):
    def fake_history(self, **kwargs):
        return pd.DataFrame(
            {"Close": [100.0, 100.4]},
            index=pd.date_range("2026-06-17", periods=2),
        )

    mocker.patch("fetch.yf.Ticker.history", autospec=True, side_effect=fake_history)

    macro = build_macro()

    assert macro["spy_pct"] == 0.4
    assert macro["vix"] == 100.4
    assert macro["ten_year"] == 100.4
```

- [ ] **Step 2: Run, expect ImportError**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: ImportError on `build_macro` / `sector_etf_for`.

- [ ] **Step 3: Implement helpers**

Add to `fetch.py` before `def fetch(`:

```python
SECTOR_ETF_MAP = {
    "AAPL": "XLK", "MSFT": "XLK", "GOOGL": "XLK", "META": "XLK",
    "NVDA": "SOXX", "AMD": "SOXX", "AVGO": "SOXX", "TSM": "SOXX", "INTC": "SOXX",
    "JPM": "XLF", "BAC": "XLF", "GS": "XLF", "MS": "XLF",
    "JNJ": "XLV", "PFE": "XLV", "UNH": "XLV", "LLY": "XLV",
    "XOM": "XLE", "CVX": "XLE",
    "TSLA": "XLY", "AMZN": "XLY", "HD": "XLY", "NKE": "XLY",
    "PLTR": "XLK", "SHOP": "XLY",
}


def sector_etf_for(ticker_symbol: str) -> str | None:
    return SECTOR_ETF_MAP.get(ticker_symbol.upper())


def _last_pct(history) -> float | None:
    closes = history["Close"] if "Close" in history.columns else None
    if closes is None or len(closes) < 2:
        return None
    prior = float(closes.iloc[-2])
    last = float(closes.iloc[-1])
    if prior == 0:
        return None
    return round((last - prior) / prior * 100, 2)


def _last_close(history) -> float | None:
    closes = history["Close"] if "Close" in history.columns else None
    if closes is None or len(closes) == 0:
        return None
    return round(float(closes.iloc[-1]), 2)


def build_macro() -> dict[str, Any]:
    """SPY %1d, VIX level, 10Y yield level (^TNX)."""
    spy = yf.Ticker("SPY").history(period="5d", interval="1d")
    vix = yf.Ticker("^VIX").history(period="5d", interval="1d")
    tnx = yf.Ticker("^TNX").history(period="5d", interval="1d")
    return {
        "spy_pct": _last_pct(spy),
        "vix": _last_close(vix),
        "ten_year": _last_close(tnx),
    }


def build_sector(ticker_symbol: str) -> dict[str, Any]:
    etf = sector_etf_for(ticker_symbol)
    if etf is None:
        return {"sector_etf": None, "sector_etf_change_pct_1d": None}
    history = yf.Ticker(etf).history(period="5d", interval="1d")
    return {"sector_etf": etf, "sector_etf_change_pct_1d": _last_pct(history)}
```

Modify `fetch()`:

```python
def fetch(ticker_symbol: str) -> dict[str, Any]:
    ticker_symbol = ticker_symbol.upper()
    ticker = yf.Ticker(ticker_symbol)
    payload: dict[str, Any] = {
        "ticker": ticker_symbol,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    payload.update(build_quote(ticker_symbol, ticker))
    payload.update(build_earnings(ticker))
    payload.update(build_options(ticker))
    payload["news"] = build_news(ticker_symbol)
    payload.update(build_sector(ticker_symbol))
    payload["macro"] = build_macro()
    return payload
```

- [ ] **Step 4: Run, expect PASS**

```bash
cd scripts && uv run pytest tests/test_fetch.py -v
```
Expected: 9 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/fetch.py scripts/tests/test_fetch.py
git commit -m "feat(fetch): add sector ETF and macro line"
```

---

## Task 8: add-stock skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/add-stock/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/add-stock/SKILL.md`:

````markdown
---
name: add-stock
description: Use when the user wants to start tracking a new stock ("add NVDA", "I want to track Palantir", "research SHOP for me"). Performs a deep investor-grade dive and writes thesis.md, state.yaml, and triggers.yaml for the new ticker.
---

# add-stock

Add a new stock to the workspace. The output is a complete investment memo the user could re-read in 6 months and remember where they stood.

## When invoked

The user has named a ticker or company and wants it tracked. Examples:
- "add NVDA"
- "I want to track Palantir"
- "research SHOP"
- "let's add Hims to the watchlist"

Resolve the company name to a ticker if needed (PLTR for Palantir, etc.). Confirm with the user if ambiguous.

## Steps

1. **Check for duplicate.** If `stocks/{TICKER}/` already exists, ask if the user wants to refresh instead (point to refresh-thesis skill) or overwrite. Do not silently overwrite.

2. **Ask 1–2 clarifying questions.** Skip these only if the user already volunteered the angle.
   - "What's your angle on this stock — what made you want to track it?"
   - If the user mentioned a thesis, skip and use it.

3. **Pull current data.** Run:
   ```bash
   uv run scripts/fetch.py {TICKER}
   ```
   Use the JSON for the Snapshot section (price, market cap, etc.) and to ground the analysis in current reality.

4. **Research the company in depth.** Use general knowledge + the news headlines from the fetcher. Cover:
   - What the company does (plain English, 2–4 sentences)
   - Industry & TAM
   - Bull / Base / Bear scenarios with rough probabilities (sum to 100) and price targets
   - Moat — use Helmer's 7 Powers as an internal checklist (scale, network, counter-positioning, switching costs, branding, cornered resource, process power) but write the conclusion as a paragraph, not a checklist
   - Management & capital allocation (CEO tenure, ROIC, buyback discipline, M&A track record)
   - Valuation: multiples sanity check (current P/E vs 5-year median + peers) AND a reverse-DCF — compute what growth and margin the current price implies and report it as a sentence ("at $X, the market is pricing in roughly Y% growth and Z% margins")
   - Balance sheet (only flag if there's real risk)
   - Key metrics to watch (3–6 specifics)
   - Catalysts (with dates)
   - Disconfirming events — what would make the user sell

5. **Write `stocks/{TICKER}/thesis.md`** following the schema in the spec (§5). Plain English. Use frameworks behind the scenes; never lecture the reader on terminology.

6. **Write `stocks/{TICKER}/state.yaml`:**
   ```yaml
   ticker: {TICKER}
   active: true
   tags: []  # ask the user if they want tags, or leave empty
   added: {YYYY-MM-DD}
   last_checked: {YYYY-MM-DD}
   last_quarterly_review: null
   last_annual_refresh: {YYYY-MM-DD}  # add-stock counts as the first refresh
   max_weight_pct: null  # leave for the user to fill in
   ```

7. **Write `stocks/{TICKER}/triggers.yaml`** as a pre-commitment device. Propose values based on the thesis, then **explicitly ask the user to confirm or edit**. Reason: pre-commitment only works if the user actually commits.
   ```yaml
   thesis_break_price: null  # propose a value below the bear-case target
   kill_conditions:
     - "..."  # 2-3 events that would make the thesis untenable
   re_read_triggers:
     - "Stock down >15% on no obvious news"
     - "Missed quarter (revenue or EPS)"
     - "..."  # 1-2 stock-specific triggers
   ```

8. **Create `stocks/{TICKER}/snapshots/` directory** (empty for now — first snapshot comes from check-stock).

9. **Tell the user what was written and what's next.** Suggest running `check-stock {TICKER}` next.

## Behavioral guards (apply here)

- Do not ask for or record cost basis or position size in dollars.
- Do not write a "Stands & Updates" entry for the user — that's their voice. Leave the section header in thesis.md and let `update-thesis` handle additions.
- Position section in thesis.md should have target / thesis-break / max-weight only. Never an entry price.

## Output format

After writing files, give the user a 4–6 line summary in chat:
- One-line thesis
- Bull/base/bear probability split
- Reverse-DCF takeaway
- Three numbers to watch
- "Triggers proposed; confirm thesis_break_price and kill_conditions before continuing."
````

- [ ] **Step 2: Commit**

```bash
git add .skills/add-stock/SKILL.md
git commit -m "feat(skills): add-stock — deep-dive memo writer"
```

---

## Task 9: check-stock skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/check-stock/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/check-stock/SKILL.md`:

````markdown
---
name: check-stock
description: Use when the user wants the current state of one tracked stock ("check NVDA", "what's NVDA doing", "pull NVDA"). Fetches Tier-1 data, writes a dated snapshot, runs the trigger check, and writes a 1–2 paragraph analysis vs the thesis.
---

# check-stock

## When invoked

User asks for an on-demand check of one stock. Examples:
- "check NVDA"
- "pull data for NVDA"
- "what's NVDA doing"
- "give me the latest on Palantir"

If the stock is not yet tracked (`stocks/{TICKER}/thesis.md` missing), ask the user if they want to add it first via add-stock.

## Steps

1. **Verify the stock is tracked.** If `stocks/{TICKER}/` doesn't exist, prompt the user to run add-stock first.

2. **Read the thesis** — load `stocks/{TICKER}/thesis.md`, `state.yaml`, `triggers.yaml`. The analysis must reference the thesis; otherwise it's just data restatement.

3. **Fetch data:**
   ```bash
   uv run scripts/fetch.py {TICKER}
   ```
   Parse the JSON.

4. **Run trigger check.** This is mandatory.
   - If `price <= triggers.yaml.thesis_break_price`: snapshot must lead with `## 🔥 THESIS-BREAK BREACHED`. Reproduce the relevant triggers verbatim. Tell the user to either re-read the thesis or sell.
   - If `price <= 1.05 * thesis_break_price` (within 5%): snapshot leads with `## ⚠ Approaching thesis-break (within 5%)`.
   - If any of the `re_read_triggers` matches today's data (e.g., "down >15% on no obvious news" — check `change_pct_30d`): mention it.

5. **Quarterly auto-prompt.** If `payload["next_earnings"]` is in the past or `change_pct_30d` shows an earnings move, AND `state.yaml.last_quarterly_review` doesn't reflect the most recent quarter, suggest running `quarterly-review` after the snapshot.

6. **Annual auto-prompt.** If today is more than 365 days after `state.yaml.last_annual_refresh`, suggest `refresh-thesis` at the end.

7. **Bear-case freshness check.** Read `thesis.md` "Stands & Updates" section. If all entries from the past 90 days are bullish-toned, add at the bottom of the snapshot: `> Bear-case freshness: you've added only bullish updates lately. Worth a 5-minute steelman of the bear case.`

8. **Write the snapshot** to `stocks/{TICKER}/snapshots/{YYYY-MM-DD}.md`:

   ```markdown
   # {TICKER} — Snapshot {YYYY-MM-DD}

   {trigger callout if any}

   ## Quote
   - Price: ${price}  ({change_pct_1d:+.2f}% day · {change_pct_5d:+.2f}% 5d · {change_pct_30d:+.2f}% 30d)
   - Market cap: ${market_cap_human}
   - P/E: {pe_trailing} trailing · {pe_forward} fwd
   - Volume: {volume_human} ({volume_ratio}x 30d avg)
   - 52w: from ${low_52w} to ${high_52w}  ({distance from 52w high}% off high)
   - 50d / 200d MA: ${ma_50d} / ${ma_200d}  ({above|below} both)
   - Put/call: {put_call_ratio}

   ## Earnings
   - Next: {next_earnings or "—"}
   - Last: EPS ${last_earnings_eps_actual} vs ${last_earnings_eps_estimate} estimate  ({beat|miss} by {delta})

   ## Macro & sector
   - SPY {spy_pct:+.2f}% · VIX {vix} · 10Y {ten_year}%
   - Sector ({sector_etf}): {sector_etf_change_pct_1d:+.2f}%

   ## News (last 72h)
   - **{title}** — {source}, {YYYY-MM-DD}. {summary}. [link]({url})
   - ...

   ## Analysis
   {1–2 short paragraphs: what changed vs the thesis. Reference the thesis explicitly. Signal flag at the end: 🔥 material / ⚠ watch / ✅ quiet.}

   ## Signal
   {🔥 / ⚠ / ✅}  — {one-line reason}

   ---
   _Bear-case freshness note here, if triggered._
   ```

9. **Update `stocks/{TICKER}/state.yaml`:** set `last_checked: {YYYY-MM-DD}`.

10. **Tell the user.** Print the path to the snapshot, plus the signal flag and any auto-prompts (quarterly review, annual refresh, bear-case steelman).

## Behavioral guards

- Reference price vs `thesis_break_price` and vs price targets — never vs entry / cost basis.
- Snapshot file is dated; if today's snapshot already exists, ask whether to overwrite or append a `## Re-check {HH:MM}` section.
- Do not invent data. If a field is `None` in the JSON, write "—" or omit it.

## Output format in chat

A 3–5 line summary:
- Signal flag + one-line reason
- Path to the snapshot file
- Any auto-prompts ("Last quarterly review was 2026-Q1 — earnings just printed. Run quarterly-review?")
````

- [ ] **Step 2: Commit**

```bash
git add .skills/check-stock/SKILL.md
git commit -m "feat(skills): check-stock — daily snapshot + trigger check"
```

---

## Task 10: update-thesis skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/update-thesis/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/update-thesis/SKILL.md`:

````markdown
---
name: update-thesis
description: Use when the user is recording an evolving view on a tracked stock ("I'm bullish on NVDA after earnings", "I'm worried about PLTR competition", "moved to neutral on AMD"). Appends a dated entry to thesis.md "Stands & Updates" section. NEVER edits prior entries.
---

# update-thesis

## When invoked

User volunteers a stand, view shift, or new piece of information about a tracked stock. Examples:
- "I'm bullish on NVDA after earnings"
- "I'm worried PLTR's growth is decelerating"
- "Trimmed my view on AMD — competitive pressure"
- "Reading the Hims 10-K, more confident in the LTV story"

If the user is *checking* the stock, not stating a view, use check-stock instead.

## Steps

1. **Identify the ticker.** If ambiguous ("the AI stock"), ask which.

2. **Read existing `stocks/{TICKER}/thesis.md`.** Find the `## Stands & Updates` section. If it doesn't exist (legacy thesis), append it at the very bottom.

3. **Capture the user's view in their own words.** Don't editorialize. If the user said "bullish after earnings," don't expand to "extremely bullish given the magnitude of the beat" — write what they said and add at most one sentence of context.

4. **Append a dated entry.** Format:
   ```markdown
   ### {YYYY-MM-DD}  {tone tag — Bullish / Bearish / Neutral / Risk flag / Note}
   {1–4 sentences. The user's view, in their voice. Optional one-sentence context line citing the news/event/snapshot that prompted it.}
   ```

5. **Cross-check against triggers.** If the user's stand contradicts the thesis (e.g., they said "bearish on NVDA" but `triggers.yaml` doesn't reflect this), ask: "Want me to update `triggers.yaml` (kill conditions / thesis-break) to match?" Don't edit triggers without confirmation.

6. **Confirm in chat.** Print: "Appended {date} {tone} entry to {TICKER} thesis."

## Hard rules — these cannot be violated

1. **Append-only.** Never edit prior entries in "Stands & Updates". Even typos. Even if the user contradicts an old entry — append a new one, leave the old.
2. **No agent commentary in the user's voice.** If the agent has its own analytical view, that goes in a `check-stock` snapshot, not in Stands & Updates.
3. **No cost basis.** If the user says "I'm down 12% on NVDA" — record the sentiment, not the number.
````

- [ ] **Step 2: Commit**

```bash
git add .skills/update-thesis/SKILL.md
git commit -m "feat(skills): update-thesis — append-only Stands & Updates"
```

---

## Task 11: deactivate-stock skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/deactivate-stock/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/deactivate-stock/SKILL.md`:

````markdown
---
name: deactivate-stock
description: Use when the user is done tracking a stock for now ("I'm done with SHOP", "deactivate PLTR", "drop NVDA from the dashboard"). Flips state.yaml.active to false. The folder stays in place — nothing is deleted or moved. Reactivate by running this skill again or saying "reactivate".
---

# deactivate-stock

## When invoked

The user wants a stock excluded from `check-all` / dashboard but doesn't want to delete the history. Examples:
- "I'm done with SHOP"
- "drop PLTR from the dashboard"
- "deactivate AMD"

To reactivate:
- "reactivate NVDA"
- "I'm watching SHOP again"

## Steps

1. **Find the ticker.** If `stocks/{TICKER}/` doesn't exist, tell the user it's not tracked.

2. **Read `state.yaml`.**

3. **Flip the `active` flag** (true → false, or false → true if reactivating). Write it back.

4. **Append a dated entry to thesis.md "Stands & Updates"** noting the change:
   ```markdown
   ### {YYYY-MM-DD}  {Deactivated / Reactivated}
   {Optional 1-line reason if the user gave one.}
   ```

5. **Confirm in chat.** "{TICKER} is now {inactive / active}. Folder stays at stocks/{TICKER}/. It {will / won't} appear in check-all."

## Hard rules

- **Do not delete or move the folder.** The user's history is sacred.
- **Do not flip flags silently.** Always append the Stands & Updates entry so the deactivation is visible in the log.
- Inactive stocks are still callable via `check-stock {TICKER}` and `refresh-thesis` — the flag only affects `check-all`.
````

- [ ] **Step 2: Commit**

```bash
git add .skills/deactivate-stock/SKILL.md
git commit -m "feat(skills): deactivate-stock — flip active flag"
```

---

## Task 12: check-all skill + dashboard

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/check-all/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/check-all/SKILL.md`:

````markdown
---
name: check-all
description: Use when the user wants the cross-stock view ("daily check", "what's going on", "morning check"). Fetches Tier-1 data for every active stock in parallel, writes individual snapshots, and regenerates dashboard/latest.md with movers, news, and macro.
---

# check-all

## When invoked

User wants to see everything at once. Examples:
- "daily check"
- "what's going on"
- "morning check"
- "what does the dashboard say"

## Steps

1. **Find active stocks.** List `stocks/*/state.yaml` and filter to `active: true`. If none, tell the user the workspace is empty and suggest `add-stock`.

2. **Run check-stock on each in parallel.** For each active ticker, follow the check-stock skill (snapshot file + trigger check). Use parallel agent dispatches if available; otherwise serially. Collect:
   - signal flag (🔥 / ⚠ / ✅)
   - one-line "what changed" summary
   - any trigger breaches

3. **Regenerate `dashboard/latest.md`:**

   ```markdown
   # Dashboard — {YYYY-MM-DD}

   ## Movers & signals

   | Ticker | Price  | %Δ 1d | %Δ 5d | Vol  | Signal |
   |--------|-------:|------:|------:|-----:|--------|
   | NVDA   | 142.30 | +3.2% | +4.1% | 1.4x | 🔥     |
   | PLTR   |  28.10 | -0.4% | -1.2% | 0.8x | ✅     |

   Sort by signal severity (🔥 first, then ⚠, then ✅) then by absolute %Δ 1d.

   ## What changed
   - **NVDA** 🔥 — earnings beat, raised guide. [snapshot](../stocks/NVDA/snapshots/2026-06-18.md)
   - **AMD** ⚠ — volume spike on no obvious news. [snapshot](../stocks/AMD/snapshots/2026-06-18.md)
   - **PLTR** — quiet day. [snapshot](../stocks/PLTR/snapshots/2026-06-18.md)

   ## Macro
   SPY +0.4% · VIX 14.2 · 10Y 4.31%

   ## Suggested follow-ups
   - {Quarterly auto-prompts collected from individual snapshots}
   - {Annual refresh prompts}
   - {Bear-case freshness flags}
   - {Triggers approaching}
   ```

4. **Cross-stock prose narrative.** Below the dashboard table in chat (not in the file unless asked), give the user 3–5 sentences: what story does the day tell? Sector themes? Single-stock outliers vs the macro? This is the qualitative judgment that distinguishes this from a dump of data.

5. **HTML dashboard on demand.** If the user asks for the richer view ("show as HTML", "give me the dashboard in HTML"), write `dashboard/latest.html` with the same data, sortable columns, and links into each stock's snapshot. Use a minimal self-contained HTML file (inline CSS, no JS frameworks). Do not generate HTML by default.

## Behavioral guards

- Inactive stocks are excluded from the dashboard entirely.
- The dashboard surfaces trigger breaches loudly — anything 🔥 sorts to the top.
- No cost basis ever.
````

- [ ] **Step 2: Commit**

```bash
git add .skills/check-all/SKILL.md
git commit -m "feat(skills): check-all — cross-stock dashboard"
```

---

## Task 13: check-triggers skill (helper, used by check-stock)

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/check-triggers/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/check-triggers/SKILL.md`:

````markdown
---
name: check-triggers
description: Helper skill called from inside check-stock and check-all. Given a ticker and the latest snapshot data, evaluates triggers.yaml and returns a structured result the caller uses to format alerts. Not typically invoked directly by the user.
---

# check-triggers

## When invoked

Almost always called from another skill (check-stock, check-all). User can invoke directly with "evaluate triggers for NVDA" — useful when triggers were just edited.

## Inputs

- Ticker
- Latest fetched data (price, change_pct_30d, etc. — from fetch.py JSON)

## Steps

1. **Read `stocks/{TICKER}/triggers.yaml`.** If missing, return `{ "status": "no_triggers" }` and suggest the user run add-stock or refresh-thesis to set them.

2. **Evaluate `thesis_break_price`:**
   - If `price <= thesis_break_price`: status `breach`. Severity 🔥. Message: "Price ${price} is at or below thesis-break ${thesis_break_price}. Re-read thesis or sell."
   - If `price <= 1.05 * thesis_break_price`: status `near`. Severity ⚠. Message: "Price ${price} is within 5% of thesis-break ${thesis_break_price}."

3. **Evaluate `re_read_triggers`** — these are written as natural-language strings, so the agent has to interpret. Common patterns:
   - "Stock down >X% on no obvious news" → check `change_pct_30d` and assess news (was there a clear catalyst?)
   - "Missed quarter" → check whether `last_earnings_eps_actual < last_earnings_eps_estimate`
   - "Cluster insider selling" → out of scope for daily fetch (Tier-2 data)
   - For any trigger that requires data not in the JSON, return `status: "needs_review"` and surface to the user.

4. **Evaluate `kill_conditions`** — these are usually qualitative ("CFO departure under controversial circumstances"). Surface them in the snapshot for the user to evaluate; do not auto-decide.

5. **Return structure:**
   ```yaml
   status: ok | near | breach | needs_review | no_triggers
   severity: 🔥 | ⚠ | ✅
   alerts:
     - kind: thesis_break_near
       message: "..."
     - kind: re_read_trigger
       message: "..."
   ```

## Hard rules

- Never edit `triggers.yaml` from this skill. Triggers are user-committed; only the user can change them.
- If a trigger is ambiguous, surface it to the user — do not assume.
````

- [ ] **Step 2: Commit**

```bash
git add .skills/check-triggers/SKILL.md
git commit -m "feat(skills): check-triggers — trigger evaluation helper"
```

---

## Task 14: fetch_insider.py — SEC EDGAR Form 4 (TDD)

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/fetch_insider.py`
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch_insider.py`

- [ ] **Step 1: Write failing test**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch_insider.py`:

```python
"""Tests for fetch_insider.py — SEC EDGAR Form 4 fetcher."""
from unittest.mock import MagicMock

from fetch_insider import parse_form4_index, summarize_transactions


def test_parse_form4_index_extracts_filings():
    edgar_json = {
        "filings": {
            "recent": {
                "form": ["4", "10-K", "4"],
                "filingDate": ["2026-06-15", "2026-04-30", "2026-06-10"],
                "accessionNumber": ["0001-001", "0001-002", "0001-003"],
                "primaryDocument": ["doc1.xml", "doc2.htm", "doc3.xml"],
            }
        }
    }
    filings = parse_form4_index(edgar_json, max_age_days=30, today="2026-06-18")
    assert len(filings) == 2
    assert filings[0]["accession"] == "0001-001"
    assert filings[1]["accession"] == "0001-003"


def test_summarize_transactions_groups_buys_sells():
    transactions = [
        {"type": "Buy", "shares": 1000, "price": 140.0, "insider": "Jensen", "date": "2026-06-15"},
        {"type": "Sell", "shares": 5000, "price": 142.0, "insider": "Colette", "date": "2026-06-12"},
        {"type": "Buy", "shares": 500, "price": 138.0, "insider": "Director A", "date": "2026-06-10"},
    ]
    summary = summarize_transactions(transactions)
    assert summary["total_buys"] == 1500
    assert summary["total_sells"] == 5000
    assert summary["buy_value_usd"] == 1000 * 140.0 + 500 * 138.0
    assert summary["sell_value_usd"] == 5000 * 142.0
    assert summary["unique_buyers"] == 2
    assert summary["unique_sellers"] == 1
```

- [ ] **Step 2: Run, expect ImportError**

```bash
cd scripts && uv run pytest tests/test_fetch_insider.py -v
```
Expected: ImportError on `fetch_insider`.

- [ ] **Step 3: Implement fetch_insider.py**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/fetch_insider.py`:

```python
"""SEC EDGAR Form 4 (insider transactions) fetcher.

CLI: uv run fetch_insider.py TICKER [--days 30]

Emits JSON to stdout with summary + per-filing list. Free, rate-limited at SEC's 10 req/s.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from typing import Any

import requests

USER_AGENT = "stock-workspace qisiyuan@personal-research.local"
EDGAR_BASE = "https://data.sec.gov"
TICKER_LOOKUP_URL = "https://www.sec.gov/files/company_tickers.json"

_TICKER_TO_CIK: dict[str, str] | None = None


def _ticker_to_cik(ticker: str) -> str | None:
    global _TICKER_TO_CIK
    if _TICKER_TO_CIK is None:
        resp = requests.get(TICKER_LOOKUP_URL, headers={"User-Agent": USER_AGENT}, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        _TICKER_TO_CIK = {row["ticker"].upper(): str(row["cik_str"]).zfill(10) for row in data.values()}
    return _TICKER_TO_CIK.get(ticker.upper())


def parse_form4_index(edgar_json: dict[str, Any], max_age_days: int, today: str) -> list[dict[str, Any]]:
    """Filter the EDGAR submissions feed to Form 4 filings within max_age_days."""
    today_d = date.fromisoformat(today)
    cutoff = today_d - timedelta(days=max_age_days)
    recent = edgar_json.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    docs = recent.get("primaryDocument", [])
    out: list[dict[str, Any]] = []
    for form, fdate, accession, doc in zip(forms, dates, accessions, docs):
        if form != "4":
            continue
        if date.fromisoformat(fdate) < cutoff:
            continue
        out.append({
            "form": form,
            "filing_date": fdate,
            "accession": accession,
            "primary_doc": doc,
        })
    return out


def summarize_transactions(transactions: list[dict[str, Any]]) -> dict[str, Any]:
    """Aggregate a list of normalized transactions into a summary."""
    total_buys = sum(t["shares"] for t in transactions if t["type"] == "Buy")
    total_sells = sum(t["shares"] for t in transactions if t["type"] == "Sell")
    buy_value = sum(t["shares"] * t["price"] for t in transactions if t["type"] == "Buy")
    sell_value = sum(t["shares"] * t["price"] for t in transactions if t["type"] == "Sell")
    unique_buyers = len({t["insider"] for t in transactions if t["type"] == "Buy"})
    unique_sellers = len({t["insider"] for t in transactions if t["type"] == "Sell"})
    return {
        "total_buys": total_buys,
        "total_sells": total_sells,
        "buy_value_usd": buy_value,
        "sell_value_usd": sell_value,
        "unique_buyers": unique_buyers,
        "unique_sellers": unique_sellers,
        "net_shares": total_buys - total_sells,
        "filing_count": len(transactions),
    }


def fetch_filings_index(cik: str) -> dict[str, Any]:
    url = f"{EDGAR_BASE}/submissions/CIK{cik}.json"
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=15)
    resp.raise_for_status()
    return resp.json()


def fetch(ticker: str, days: int) -> dict[str, Any]:
    cik = _ticker_to_cik(ticker)
    if cik is None:
        return {"ticker": ticker.upper(), "error": "ticker not found in EDGAR lookup"}
    index = fetch_filings_index(cik)
    today_iso = date.today().isoformat()
    filings = parse_form4_index(index, max_age_days=days, today=today_iso)
    # NOTE: parsing each Form 4 XML for line-item transactions is non-trivial.
    # This v1 returns the filings list + counts only. Per-transaction parsing is a future
    # task; see "Open questions" in the spec.
    summary = {
        "ticker": ticker.upper(),
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "window_days": days,
        "form4_filings_count": len(filings),
        "filings": filings[:50],
        "note": "Transaction-level parsing not implemented in v1. Open the linked filings on EDGAR for details.",
    }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Form 4 insider activity")
    parser.add_argument("ticker")
    parser.add_argument("--days", type=int, default=30)
    args = parser.parse_args()
    payload = fetch(args.ticker, args.days)
    json.dump(payload, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run, expect PASS**

```bash
cd scripts && uv run pytest tests/test_fetch_insider.py -v
```
Expected: 2 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/fetch_insider.py scripts/tests/test_fetch_insider.py
git commit -m "feat(fetch): SEC EDGAR Form 4 insider filings index (v1: filing list only)"
```

---

## Task 15: fetch_13f.py — SEC EDGAR 13F summary (TDD)

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/fetch_13f.py`
- Create: `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch_13f.py`

This task ships a v1 that lists the most recent 13F filings (which institutions report holdings) without parsing the XML in detail. Full holding-level parsing is deferred — the spec acknowledges WhaleWisdom or paid sources as alternatives.

- [ ] **Step 1: Write failing test**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/tests/test_fetch_13f.py`:

```python
"""Tests for fetch_13f.py — SEC 13F filings index (v1: list filings only)."""
from fetch_13f import filter_13f_filings


def test_filter_13f_filings_picks_most_recent():
    edgar_json = {
        "filings": {
            "recent": {
                "form": ["13F-HR", "10-K", "13F-HR/A", "13F-HR"],
                "filingDate": ["2026-05-15", "2026-04-01", "2026-05-20", "2026-02-15"],
                "accessionNumber": ["a", "b", "c", "d"],
                "primaryDocument": ["1.xml", "2.htm", "3.xml", "4.xml"],
            }
        }
    }
    filings = filter_13f_filings(edgar_json, limit=3)
    # Only 13F-HR and 13F-HR/A, sorted newest-first
    assert [f["accession"] for f in filings] == ["c", "a", "d"]
```

- [ ] **Step 2: Run, expect ImportError**

```bash
cd scripts && uv run pytest tests/test_fetch_13f.py -v
```
Expected: ImportError.

- [ ] **Step 3: Implement fetch_13f.py**

Write `/Users/qisiyuan/Documents/Self/stock/scripts/fetch_13f.py`:

```python
"""SEC 13F-HR filings index for a ticker's institutional context.

NOTE v1 limitation: This script lists 13F filings by reporting institutions but does NOT
join across them to compute "top 5 holders of TICKER". That join requires either parsing
each 13F XML for the target ticker's CUSIP or using WhaleWisdom's free tier. See spec §11.

CLI: uv run fetch_13f.py TICKER
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from typing import Any

import requests

USER_AGENT = "stock-workspace qisiyuan@personal-research.local"
EDGAR_BASE = "https://data.sec.gov"


def filter_13f_filings(edgar_json: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    recent = edgar_json.get("filings", {}).get("recent", {})
    forms = recent.get("form", [])
    dates = recent.get("filingDate", [])
    accessions = recent.get("accessionNumber", [])
    docs = recent.get("primaryDocument", [])
    rows = [
        {"form": f, "filing_date": d, "accession": a, "primary_doc": p}
        for f, d, a, p in zip(forms, dates, accessions, docs)
        if f in ("13F-HR", "13F-HR/A")
    ]
    rows.sort(key=lambda r: r["filing_date"], reverse=True)
    return rows[:limit]


def fetch(ticker: str) -> dict[str, Any]:
    return {
        "ticker": ticker.upper(),
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": (
            "v1 of this script returns guidance only. Free per-ticker top-5-holders "
            "cross-13F join is not implemented. Use https://whalewisdom.com (free tier) "
            "or the SEC full-text search at https://efts.sec.gov/LATEST/search-index?"
            f"q=%22{ticker.upper()}%22&forms=13F-HR for institutional ownership of {ticker.upper()}."
        ),
        "links": {
            "whalewisdom": f"https://whalewisdom.com/stock/{ticker.lower()}",
            "edgar_full_text": (
                f"https://efts.sec.gov/LATEST/search-index?q=%22{ticker.upper()}%22&forms=13F-HR"
            ),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="13F institutional context (v1: guidance + links)")
    parser.add_argument("ticker")
    args = parser.parse_args()
    payload = fetch(args.ticker)
    json.dump(payload, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run, expect PASS**

```bash
cd scripts && uv run pytest tests/test_fetch_13f.py -v
```
Expected: 1 passed.

- [ ] **Step 5: Commit**

```bash
git add scripts/fetch_13f.py scripts/tests/test_fetch_13f.py
git commit -m "feat(fetch): 13F filings filter + per-ticker WhaleWisdom guidance (v1)"
```

---

## Task 16: weekly-review skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/weekly-review/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/weekly-review/SKILL.md`:

````markdown
---
name: weekly-review
description: Use weekly or when user asks for Tier-2 signals ("weekly review", "weekly NVDA", "what's the insider activity", "what changed in 13F"). Pulls insider transactions, 13F filing index, short interest, and analyst-revision context. Writes findings into the next daily snapshot or its own file.
---

# weekly-review

## When invoked

User asks for the slower-cadence signals. Examples:
- "weekly review"
- "weekly NVDA"
- "what's insider activity look like"
- "any 13F changes for AMD"

## Steps

1. **Pick scope.** If a single ticker is named, just that one. If "weekly review" with no ticker, run for all active stocks (parallel).

2. **For each ticker, run the Tier-2 fetchers:**
   ```bash
   uv run scripts/fetch_insider.py {TICKER} --days 30
   uv run scripts/fetch_13f.py {TICKER}
   ```
   Parse the JSON.

3. **Pull short interest.** v1: include a manual link to FINRA's reg SHO daily files: `https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data` and Nasdaq's bi-monthly short interest page. The agent reads no API for this in v1. If the user wants it filled in, suggest doing it manually or upgrading to Koyfin.

4. **Pull analyst revisions.** v1: open `https://finance.yahoo.com/quote/{TICKER}/analysis` and summarize what's there using a fetch tool — recent estimate revisions, PT changes. If unavailable, surface as a gap.

5. **Write findings** to `stocks/{TICKER}/snapshots/{YYYY-MM-DD}-weekly.md`:

   ```markdown
   # {TICKER} — Weekly review {YYYY-MM-DD}

   ## Insider activity (last 30 days)
   - Form 4 filings: {count}
   - Notable: {plain-English summary, e.g. "CEO bought $2.1M at $138 average — first open-market buy in 18 months"}
   - Filings list: see fetch_insider output JSON or [EDGAR](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={CIK}&type=4)

   ## 13F context
   - {Latest 13F filings count, link to WhaleWisdom for cross-institution view}
   - {Notable changes if user flags or paid source available}

   ## Short interest
   - {Latest from FINRA / Nasdaq, plain text}

   ## Analyst revisions (last 7 days)
   - {Recent PT changes, ratings revisions if found}

   ## Synthesis
   {1–2 paragraphs. Does insider behavior align with the thesis? Any institutional flow that contradicts the user's view? Are analysts moving in the same direction as the thesis?}
   ```

6. **Update state.yaml** with `last_weekly_review: {YYYY-MM-DD}`.

7. **Tell the user.** Path to the file plus 2–3 line summary per ticker.

## Behavioral guards

- Insider buys (especially clusters) and 13F-superinvestor moves are higher-signal than analyst revisions. Weight the synthesis accordingly.
- Don't over-interpret a single insider trade — small option-grant exercises happen routinely.
- Surface gaps honestly: "Short interest data not pulled in v1 — see manual link above."
````

- [ ] **Step 2: Commit**

```bash
git add .skills/weekly-review/SKILL.md
git commit -m "feat(skills): weekly-review — Tier-2 signal pull"
```

---

## Task 17: quarterly-review skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/quarterly-review/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/quarterly-review/SKILL.md`:

````markdown
---
name: quarterly-review
description: Use after each earnings print to re-score the thesis ("quarterly NVDA", "review NVDA after earnings", "Q2 review"). Re-scores bull/base/bear probabilities, redoes reverse-DCF, updates key metrics, and writes snapshots/reviews/{YYYY-Qn}.md. Appends a quarterly note to thesis.md Stands & Updates.
---

# quarterly-review

## When invoked

User wants a thesis-level re-score after fresh earnings data. Examples:
- "quarterly NVDA"
- "review NVDA after earnings"
- "Q2 review on Palantir"

## Steps

1. **Read existing `thesis.md`, `state.yaml`, `triggers.yaml`.** Identify current bull/base/bear weights and price targets.

2. **Pull current data:**
   ```bash
   uv run scripts/fetch.py {TICKER}
   ```

3. **Read the earnings release** if linked from news headlines or available on the company IR site. Use the news section of fetch.py output as a starting point — find the headline link to the release and fetch it. If transcript is paywalled, work from the release alone and note the gap.

4. **Re-score bull/base/bear:**
   - Did the print confirm the bull case, base case, or surface a bear-case risk?
   - Adjust probability weights (must still sum to 100).
   - Update price targets if needed.
   - Write the scoring as plain prose, with old vs new weights side by side.

5. **Redo reverse-DCF.** Compute what current price implies for revenue growth and margins given the new data. If the implied numbers no longer pencil (e.g., requires growth above the historical max), flag it.

6. **Update key metrics with the latest reported numbers.** Plain numerical update.

7. **Write `stocks/{TICKER}/snapshots/reviews/{YYYY-Qn}.md`:**

   ```markdown
   # {TICKER} — Quarterly review {YYYY-Qn}

   ## Earnings summary
   - Revenue: ${X}B vs ${Y}B est ({beat/miss} {%})
   - EPS: ${X} vs ${Y} est
   - Guide: {raised / maintained / cut}
   - Key segment: {segment metric, e.g. DC revenue +94% YoY}

   ## Thesis re-score

   |              | Prior | New |
   |--------------|------:|----:|
   | Bull weight  | 30%   | 35% |
   | Base weight  | 50%   | 50% |
   | Bear weight  | 20%   | 15% |

   What changed: {plain-English why the weights moved}

   ## Reverse-DCF re-run
   At ${current_price}, the market is now pricing in roughly {X}% revenue growth and {Y}% margins. {Plausibility judgment.}

   ## Key metrics — updated
   - {metric}: {value} ({direction vs prior})

   ## Triggers — any updates?
   {Comment on whether thesis-break or kill conditions need editing. Don't auto-edit; suggest if needed.}

   ## Verdict
   {Hold / Trim / Add / Re-read full thesis}, with one-sentence reason.
   ```

8. **Append to `thesis.md` Stands & Updates:**
   ```markdown
   ### {YYYY-MM-DD}  Quarterly review — {YYYY-Qn}
   {2–4 sentence summary of the re-score and verdict. Link to the review file.}
   ```

9. **Update `state.yaml`:** `last_quarterly_review: {YYYY-Qn}`.

10. **Tell the user.** Paths + the verdict line.

## Behavioral guards

- Append-only Stands & Updates. The quarterly entry goes at the bottom, never edits prior entries.
- If reverse-DCF implies numbers no longer plausible, recommend re-reading the full thesis or sizing down — but don't tell the user to sell. Decisions are theirs.
- If the print fundamentally breaks the thesis (a kill condition was hit), say so plainly. Don't soften.
````

- [ ] **Step 2: Commit**

```bash
git add .skills/quarterly-review/SKILL.md
git commit -m "feat(skills): quarterly-review — post-earnings re-score"
```

---

## Task 18: refresh-thesis skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/refresh-thesis/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/refresh-thesis/SKILL.md`:

````markdown
---
name: refresh-thesis
description: Use annually or when the thesis feels stale ("refresh NVDA thesis", "redo PLTR research", "annual review on AMD"). Re-runs the deep-dive from scratch (re-read 10-K, fresh competitive scan, redo reverse-DCF), then merges into thesis.md while preserving Stands & Updates verbatim.
---

# refresh-thesis

## When invoked

The user wants the thesis re-grounded. Examples:
- "refresh NVDA thesis"
- "redo PLTR research"
- "annual review on AMD"
- "is my thesis on SHOP still right"

## Steps

1. **Read existing `thesis.md`** (the whole file). Take note of:
   - The current one-line thesis
   - Bull/base/bear weights
   - Existing Stands & Updates entries (these MUST be preserved verbatim)

2. **Pull current data:**
   ```bash
   uv run scripts/fetch.py {TICKER}
   ```

3. **Re-research the company from a blank-slate perspective.** Use general knowledge + news headlines + (if accessible) company IR site for the latest 10-K. Specifically reassess:
   - Industry & TAM — has the market grown / shrunk / changed?
   - Bull / base / bear scenarios — do the old probabilities still hold?
   - Moat — is the 7 Powers picture intact? Any erosion?
   - Management — any changes? Capital allocation track record holding up?
   - Valuation — fresh multiples comparison + reverse-DCF
   - Balance sheet — any new red flags?
   - Key metrics — are the right things still being measured?
   - Catalysts — what's on the calendar for the next 12 months?
   - Disconfirming events — does the kill list still match the risks?

4. **Write a "Refresh delta"** at the top of `stocks/{TICKER}/snapshots/reviews/{YYYY}-annual.md`:

   ```markdown
   # {TICKER} — Annual refresh {YYYY-MM-DD}

   ## What changed in the thesis

   - One-line: {old} → {new, if updated}
   - Probability weights: bull {old}→{new}, base {old}→{new}, bear {old}→{new}
   - Targets: {old → new}
   - Moat: {still intact / weakening / strengthening — and why}
   - Risk profile: {key new risks; killed risks no longer relevant}

   ## Verdict
   {Continue / Reduce conviction / Exit candidate}, with one-sentence reason.
   ```

5. **Rewrite `thesis.md` in place with the updated content.** This is the one place the agent edits an existing thesis section freely (except Stands & Updates, which is append-only).
   - All sections except "Stands & Updates" are rewritten with fresh content.
   - "Stands & Updates" is preserved verbatim. Append a new entry at the bottom noting the refresh.

6. **Append to Stands & Updates:**
   ```markdown
   ### {YYYY-MM-DD}  Annual refresh
   {2-4 sentence summary of the delta. Verdict line. Link to the review file.}
   ```

7. **Review and propose updates to `triggers.yaml`** — but require user confirmation before writing. Propose new thesis_break_price, kill_conditions, re_read_triggers; show diff; ask "apply?"

8. **Update `state.yaml`:** `last_annual_refresh: {YYYY-MM-DD}`.

9. **Tell the user.** Path to refresh file, verdict line, and the proposed triggers.yaml diff.

## Behavioral guards

- **Stands & Updates is sacred.** Never edit, never reorder, only append.
- **No silent triggers.yaml edits.** Always require user confirmation for any change to pre-committed triggers.
- **Be willing to recommend exit.** If the refresh shows the thesis is dead, say so. The point of an annual refresh is to find dead theses.
````

- [ ] **Step 2: Commit**

```bash
git add .skills/refresh-thesis/SKILL.md
git commit -m "feat(skills): refresh-thesis — annual deep refresh"
```

---

## Task 19: compare-stocks skill

**Files:**
- Create: `/Users/qisiyuan/Documents/Self/stock/.skills/compare-stocks/SKILL.md`

- [ ] **Step 1: Write the skill**

Write `/Users/qisiyuan/Documents/Self/stock/.skills/compare-stocks/SKILL.md`:

````markdown
---
name: compare-stocks
description: Use when the user wants a side-by-side ("compare NVDA vs AMD", "which of my AI stocks looks best", "rank my semi names"). Reads multiple theses + latest snapshots and writes a comparison.
---

# compare-stocks

## When invoked

User wants a cross-stock view at the thesis level. Examples:
- "compare NVDA vs AMD"
- "which of my AI stocks looks best right now"
- "rank my semi names by conviction"

## Steps

1. **Resolve the set.** Either explicit tickers ("NVDA vs AMD") or a tag-based filter ("AI stocks" → all active stocks with tag `ai` in state.yaml).

2. **For each, read:**
   - `stocks/{TICKER}/thesis.md`
   - `stocks/{TICKER}/state.yaml`
   - The latest snapshot in `stocks/{TICKER}/snapshots/` (most recent dated file)

3. **Optional fresh-pull.** If the latest snapshot is more than 7 days old, ask the user: "Snapshots are old — pull fresh data first?" Run check-stock on each if confirmed.

4. **Write a comparison.** This is a chat output by default; offer to save to `dashboard/compare-{tickers}-{YYYY-MM-DD}.md` if the user wants it persistent.

   ```markdown
   # Comparison — {TICKER A} vs {TICKER B}  ({YYYY-MM-DD})

   |                  | {A} | {B} |
   |------------------|-----|-----|
   | One-line thesis  | ... | ... |
   | Bull/base/bear   | 30/50/20 | 25/55/20 |
   | Price vs break   | $X (8% above) | $Y (1% above ⚠) |
   | P/E forward      | ... | ... |
   | Reverse-DCF gap  | "implies 25% growth, plausible" | "implies 20% growth, tight" |
   | Moat strength    | high (process power + switching) | medium (scale only) |
   | Catalysts in 90d | ... | ... |
   | Last quarter     | beat | in-line |
   | Stands trend     | bullish | neutral |

   ## Synthesis

   {2–4 paragraphs. Which one has the better risk/reward at current prices? Where are the theses diverging? Any stock that's clearly "dead to me" by its own kill conditions? Acknowledge what you can't see (cost basis, sizing decisions).}

   ## Verdict
   {If user asked "which looks best": one explicit pick with the reasoning. If they asked for comparison only: short summary, no pick.}
   ```

5. **Behavioral guards.**
   - The comparison must reference each stock's *own* thesis, not a generic frame. NVDA's bear case isn't "AI cools"; it's whatever the user wrote.
   - Don't compare on cost basis or P&L (workspace doesn't track them anyway).
   - If a kill condition has been hit on one of the stocks, surface it loudly even if the user didn't ask.
````

- [ ] **Step 2: Commit**

```bash
git add .skills/compare-stocks/SKILL.md
git commit -m "feat(skills): compare-stocks — cross-cut analysis"
```

---

## Task 20: end-to-end smoke test (one real ticker)

**Files:**
- (No new files — runs the real flow against a real ticker)

This task verifies the workspace works end-to-end with a real stock. Pick a high-liquidity name (NVDA) so data is reliably available.

- [ ] **Step 1: Verify pyproject is synced**

```bash
cd scripts && uv sync --extra dev && cd ..
```
Expected: no errors.

- [ ] **Step 2: Smoke-test fetch.py against the network**

```bash
cd scripts && uv run python fetch.py NVDA | head -50
```
Expected: JSON object with `ticker: "NVDA"`, a numeric `price`, a `news` array. If network is offline, skip this step and rely on unit tests.

- [ ] **Step 3: Run all tests**

```bash
cd scripts && uv run pytest -v
```
Expected: all tests pass. Document the pass count in the commit message below.

- [ ] **Step 4: Verify all skill files have well-formed frontmatter**

```bash
for f in .skills/*/SKILL.md; do
  echo "=== $f ===";
  head -5 "$f";
done
```
Expected: each starts with `---`, has `name:` and `description:` fields.

- [ ] **Step 5: Verify CLAUDE.md is present and references the skills**

```bash
grep -E "skills|guards" CLAUDE.md | head -20
```
Expected: hits on workspace rules, behavioral guards, and skill references.

- [ ] **Step 6: Commit if anything was missed**

If the previous steps revealed missing wiring, fix it, then:
```bash
git add -A
git commit -m "chore: end-to-end smoke test pass"
```
If nothing needed fixing, skip the commit and move on.

- [ ] **Step 7: Final summary to the user**

Print to chat:
- Workspace is ready.
- Try: "add NVDA" to start.
- Test count: {N} passing.
- Open gaps the user should know about (Tier-2 short interest manual, 13F join not implemented v1, no real-time options flow).

---

## Self-review notes

**Spec coverage check:**
- §3 directory layout → Tasks 1, 2, 3 (scaffold) + Tasks 4-7 (scripts) + Tasks 8-19 (skills). All present.
- §4 interaction model (natural language → skills) → covered by all skill files; CLAUDE.md (Task 2) ties them together.
- §5 thesis schema → add-stock (Task 8) and refresh-thesis (Task 18) implement it; quarterly-review (Task 17) uses it.
- §6 snapshot tiers → Task 4-7 (Tier-1 fetcher), Task 14-15 (Tier-2 fetchers), Task 9 (check-stock skill writes snapshot), Task 16 (weekly-review uses Tier-2).
- §7 behavioral guards → enumerated in CLAUDE.md (Task 2) AND repeated in each relevant skill (8, 9, 10, 11, 17, 18, 19).
- §8 skills table → Tasks 8-13, 16-19 cover all 10 skills.
- §9 dashboard → Task 12.
- §10 fetcher contract → Tasks 4-7 implement the schema.
- §11 data sources → all sources used in fetcher tasks; gaps acknowledged in CLAUDE.md and weekly-review.
- §12 CLAUDE.md outline → Task 2.
- §14 implementation order → matches Task 1 → 20 ordering.

**Type/identifier consistency check:**
- `build_quote`, `build_earnings`, `build_options`, `build_news`, `build_macro`, `build_sector`, `sector_etf_for`, `_utcnow`, `_is_nan`, `_last_pct`, `_last_close` — all defined in fetch.py and referenced consistently.
- `parse_form4_index`, `summarize_transactions`, `fetch_filings_index`, `_ticker_to_cik` — all in fetch_insider.py.
- `filter_13f_filings` — in fetch_13f.py.
- `triggers.yaml` keys: `thesis_break_price`, `kill_conditions`, `re_read_triggers` — referenced consistently across add-stock, check-stock, check-triggers, refresh-thesis.
- `state.yaml` keys: `ticker`, `active`, `tags`, `added`, `last_checked`, `last_quarterly_review`, `last_annual_refresh`, `max_weight_pct` — consistent across add-stock, check-stock, deactivate-stock, weekly-review (adds `last_weekly_review`), quarterly-review, refresh-thesis. Note: `last_weekly_review` is introduced by Task 16 — that's intentional, not a contradiction.
- Snapshot path: `stocks/{TICKER}/snapshots/{YYYY-MM-DD}.md` — consistent.
- Review path: `stocks/{TICKER}/snapshots/reviews/{YYYY-Qn}.md` and `{YYYY}-annual.md` — consistent.

**Placeholder scan:** no TBDs, no "implement later", no "similar to Task N" stubs, no naked "add error handling". Every code step has the actual code.

**Open gaps explicitly acknowledged in plan, not glossed over:**
- Form 4 transaction-level XML parsing (Task 14 returns filings list only; full per-transaction parse is future work)
- 13F per-ticker top-5-holders join (Task 15 returns guidance + WhaleWisdom link)
- Short interest data (Task 16 includes manual link only)
- HTML dashboard (Task 12 marks it as on-demand only)

These are documented as v1 limitations in CLAUDE.md and the spec.
