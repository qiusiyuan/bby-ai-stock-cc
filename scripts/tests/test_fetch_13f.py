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
