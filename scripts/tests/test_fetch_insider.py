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
