"""Tests for fetch.py — price/quote core."""
from datetime import datetime, timezone
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
