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
