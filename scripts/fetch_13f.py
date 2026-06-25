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
