"""Tier-1 stock data fetcher. CLI: uv run fetch.py TICKER -> JSON to stdout."""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from typing import Any

import feedparser
import yfinance as yf


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _is_nan(x: Any) -> bool:
    try:
        import math

        return isinstance(x, float) and math.isnan(x)
    except Exception:
        return False


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

    history_30d: list[dict[str, Any]] = []
    if closes is not None and len(closes):
        tail = closes.tail(30)
        for ts, val in tail.items():
            if val is None or _is_nan(val):
                continue
            history_30d.append({"date": ts.strftime("%Y-%m-%d"), "close": round(float(val), 4)})

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
        "history_30d": history_30d,
    }


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
