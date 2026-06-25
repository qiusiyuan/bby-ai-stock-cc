"""Fetch intraday price bars (with pre/post-market) for one or more tickers.

Usage:
  uv run --project scripts scripts/fetch_intraday.py MU
  uv run --project scripts scripts/fetch_intraday.py MU --interval 5m --period 1d
  uv run --project scripts scripts/fetch_intraday.py MU --interval 1m --period 1d --no-prepost
  uv run --project scripts scripts/fetch_intraday.py MU NVDA TSM --interval 15m --period 2d

Periods that work with intraday:
  1d (today only — most useful for "what did the tape do today")
  5d (last 5 trading days)
  1mo  (with --interval 30m or larger only — yfinance restriction)

Intervals:
  1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h

Output (JSON to stdout):
  {
    "ticker": "MU",
    "fetched_at": "...",
    "interval": "5m",
    "period": "1d",
    "prepost": true,
    "bars": [
      {"t": "2026-06-24T09:30:00-04:00", "open": ..., "high": ..., "low": ..., "close": ..., "volume": ..., "session": "regular"},
      ...
    ],
    "summary": {
      "open": 1040.0, "high": 1055.5, "low": 1010.0,
      "close": 1012.21, "post_close": 1048.51,
      "regular_change_pct": -0.31,
      "post_change_pct": 3.58
    }
  }
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from typing import Any

import yfinance as yf


def classify_session(ts, market_open_hour: int = 9, market_close_hour: int = 16) -> str:
    """Classify bar as pre / regular / post by ET hour."""
    h = ts.hour
    m = ts.minute
    if h < market_open_hour or (h == market_open_hour and m < 30):
        return "pre"
    if h >= market_close_hour:
        return "post"
    return "regular"


def fetch_intraday(
    ticker_symbol: str,
    interval: str = "5m",
    period: str = "1d",
    prepost: bool = True,
) -> dict[str, Any]:
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period=period, interval=interval, prepost=prepost)

    bars: list[dict[str, Any]] = []
    if hist is not None and len(hist):
        # Convert index to US/Eastern for ET timestamps
        try:
            idx_et = hist.index.tz_convert("America/New_York")
        except Exception:
            idx_et = hist.index

        for ts_et, row in zip(idx_et, hist.itertuples(index=False)):
            session = classify_session(ts_et)
            bars.append({
                "t": ts_et.isoformat(timespec="minutes"),
                "open": round(float(row.Open), 4) if row.Open == row.Open else None,  # NaN check via inequality
                "high": round(float(row.High), 4) if row.High == row.High else None,
                "low": round(float(row.Low), 4) if row.Low == row.Low else None,
                "close": round(float(row.Close), 4) if row.Close == row.Close else None,
                "volume": int(row.Volume) if row.Volume == row.Volume else 0,
                "session": session,
            })

    summary: dict[str, Any] = {}
    if bars:
        regular = [b for b in bars if b["session"] == "regular" and b["close"] is not None]
        post = [b for b in bars if b["session"] == "post" and b["close"] is not None]
        pre = [b for b in bars if b["session"] == "pre" and b["close"] is not None]
        all_valid = [b for b in bars if b["close"] is not None]

        if regular:
            r_open = regular[0]["open"]
            r_close = regular[-1]["close"]
            r_high = max(b["high"] for b in regular if b["high"] is not None)
            r_low = min(b["low"] for b in regular if b["low"] is not None)
            summary["regular_open"] = r_open
            summary["regular_close"] = r_close
            summary["regular_high"] = r_high
            summary["regular_low"] = r_low
            summary["regular_change_pct"] = (
                round((r_close - r_open) / r_open * 100, 2)
                if r_open else None
            )
        if post:
            summary["post_close"] = post[-1]["close"]
            ref = summary.get("regular_close") or (regular[-1]["close"] if regular else None)
            if ref:
                summary["post_change_pct"] = round((post[-1]["close"] - ref) / ref * 100, 2)
        if pre:
            summary["pre_first"] = pre[0]["close"]
            summary["pre_last"] = pre[-1]["close"]
        if all_valid:
            summary["session_high"] = max(b["high"] for b in all_valid if b["high"] is not None)
            summary["session_low"] = min(b["low"] for b in all_valid if b["low"] is not None)

    return {
        "ticker": ticker_symbol.upper(),
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "interval": interval,
        "period": period,
        "prepost": prepost,
        "bars": bars,
        "summary": summary,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tickers", nargs="+", help="Ticker symbol(s)")
    ap.add_argument("--interval", default="5m", choices=["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h"])
    ap.add_argument("--period", default="1d", help="1d / 5d / 1mo (intraday limits apply)")
    ap.add_argument("--no-prepost", dest="prepost", action="store_false", default=True)
    args = ap.parse_args()

    if len(args.tickers) == 1:
        payload = fetch_intraday(args.tickers[0], args.interval, args.period, args.prepost)
        json.dump(payload, sys.stdout, indent=2, default=str)
    else:
        payloads = [fetch_intraday(t, args.interval, args.period, args.prepost) for t in args.tickers]
        json.dump(payloads, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
