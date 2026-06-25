"""Reusable company-overview fetcher.

CLI: uv run fetch_overview.py TICKER

Pulls the basic public-record context an investor wants when researching a name:
- yfinance company info (name, sector, industry, summary, website)
- Wikipedia summary (often the cleanest plain-English description, kept current)
- Yahoo Finance profile URL (for the agent to follow up on)
- SEC EDGAR filings link (10-K/10-Q/8-K + Form 4 indices)
- Macrotrends + StockAnalysis links (free fundamentals history)
- Recent news headlines (reuse fetch.py's news puller, 7-day window)

The point: when adding a new stock, the agent shells out to this script INSTEAD of
relying on training-data knowledge. Caches results in scripts/.cache/overview/ for
24h to keep repeated calls fast.

Output: JSON to stdout.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests
import yfinance as yf

from fetch import build_news

USER_AGENT = "stock-workspace overview-fetcher (research@local)"
CACHE_DIR = Path(__file__).parent / ".cache" / "overview"
CACHE_TTL_SEC = 24 * 3600  # 24h


def _cache_path(ticker: str) -> Path:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha1(ticker.upper().encode()).hexdigest()[:12]
    return CACHE_DIR / f"{ticker.upper()}-{h}.json"


def _load_cache(ticker: str) -> dict[str, Any] | None:
    path = _cache_path(ticker)
    if not path.exists():
        return None
    if time.time() - path.stat().st_mtime > CACHE_TTL_SEC:
        return None
    try:
        return json.loads(path.read_text())
    except Exception:
        return None


def _save_cache(ticker: str, payload: dict[str, Any]) -> None:
    _cache_path(ticker).write_text(json.dumps(payload, default=str, indent=2))


def fetch_yfinance_profile(ticker_symbol: str) -> dict[str, Any]:
    """Pull yfinance's company-info fields. Best for sector/industry/summary."""
    try:
        info = yf.Ticker(ticker_symbol).info or {}
    except Exception as exc:
        return {"error": f"yfinance: {exc}"}
    keys = [
        "longName", "shortName", "sector", "industry", "industryDisp",
        "longBusinessSummary", "country", "city", "state", "fullTimeEmployees",
        "website", "phone", "address1", "marketCap", "currency", "exchange",
        "quoteType", "symbol", "ipoExpectedDate", "firstTradeDateEpochUtc",
    ]
    return {k: info.get(k) for k in keys if info.get(k) is not None}


def fetch_wikipedia_summary(query: str) -> dict[str, Any]:
    """Wikipedia REST summary. `query` should be the company name, not the ticker."""
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(query)}"
    try:
        resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=10)
        if resp.status_code != 200:
            return {"error": f"wikipedia HTTP {resp.status_code}", "url": url}
        data = resp.json()
        return {
            "title": data.get("title"),
            "description": data.get("description"),
            "extract": data.get("extract"),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page"),
        }
    except Exception as exc:
        return {"error": f"wikipedia: {exc}"}


def reference_links(ticker_symbol: str) -> dict[str, str]:
    t = ticker_symbol.upper()
    t_lower = ticker_symbol.lower()
    return {
        "yahoo_profile": f"https://finance.yahoo.com/quote/{t}/profile",
        "yahoo_analysis": f"https://finance.yahoo.com/quote/{t}/analysis",
        "yahoo_holders": f"https://finance.yahoo.com/quote/{t}/holders",
        "stockanalysis": f"https://stockanalysis.com/stocks/{t_lower}/",
        "macrotrends": f"https://www.macrotrends.net/stocks/charts/{t}/_/profile",
        "edgar_filings": (
            f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={t}&type=&dateb=&owner=include&count=40"
        ),
        "edgar_10k": (
            f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={t}&type=10-K&dateb=&owner=include&count=10"
        ),
        "edgar_form4": (
            f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={t}&type=4&dateb=&owner=include&count=40"
        ),
        "whalewisdom": f"https://whalewisdom.com/stock/{t_lower}",
        "openinsider": f"http://openinsider.com/screener?s={t}",
    }


def build_overview(ticker_symbol: str, *, use_cache: bool = True) -> dict[str, Any]:
    ticker_symbol = ticker_symbol.upper()
    if use_cache:
        cached = _load_cache(ticker_symbol)
        if cached is not None:
            cached["from_cache"] = True
            return cached

    profile = fetch_yfinance_profile(ticker_symbol)
    company_name = profile.get("longName") or profile.get("shortName") or ticker_symbol
    wiki = fetch_wikipedia_summary(company_name)
    news = build_news(ticker_symbol, limit=10, hours=7 * 24)

    payload: dict[str, Any] = {
        "ticker": ticker_symbol,
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "from_cache": False,
        "profile": profile,
        "wikipedia": wiki,
        "news_7d": news,
        "links": reference_links(ticker_symbol),
        "research_hints": [
            "Read profile.longBusinessSummary for the 1-paragraph company description.",
            "wikipedia.extract is often more current than yfinance summary; cross-reference.",
            "links.edgar_10k for the latest annual filing (free, authoritative).",
            "links.openinsider for free Form 4 insider transactions, real-time.",
            "links.whalewisdom for free 13F institutional ownership (45-day lag).",
            "links.stockanalysis and links.macrotrends for free fundamentals history.",
            "If profile is sparse (recent IPO, foreign listing), use Wikipedia + news headlines + the EDGAR S-1 if available.",
        ],
    }
    _save_cache(ticker_symbol, payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Reusable company-overview fetcher")
    parser.add_argument("ticker")
    parser.add_argument("--no-cache", action="store_true", help="Bypass the 24h cache")
    args = parser.parse_args()
    payload = build_overview(args.ticker, use_cache=not args.no_cache)
    json.dump(payload, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
