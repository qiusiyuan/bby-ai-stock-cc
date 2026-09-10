"""Aggregate workspace timeline: hand-maintained events + active-stock earnings + recorded predictions.

Reads:
  timeline.yaml                              hand-curated events
  stocks/{T}/state.yaml + yfinance           live earnings dates for active stocks
  attributions/index.jsonl                   prediction score_dates

Output:
  JSON list of events sorted by date, each with:
    {date, kind, ticker, note, urgency}
  urgency = "red" (within 7d) | "amber" (8-14d) | "grey" (15-30d) | "future" (>30d) | "past"

CLI:
  uv run --project scripts scripts/build_timeline.py                  # next 30 days
  uv run --project scripts scripts/build_timeline.py --days 60        # next 60 days
  uv run --project scripts scripts/build_timeline.py --md             # markdown output
  uv run --project scripts scripts/build_timeline.py --as-of 2026-06-23
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
TIMELINE_YAML = ROOT / "timeline.yaml"
ATTR_INDEX = ROOT / "attributions" / "index.jsonl"
STOCKS_DIR = ROOT / "stocks"
EARNINGS_CACHE = Path(__file__).resolve().parent / ".cache" / "earnings"
EARNINGS_TTL_SECONDS = 24 * 3600


def _today_iso(as_of: str | None) -> date:
    if as_of:
        return datetime.fromisoformat(as_of).date()
    return date.today()


def _parse_date_loose(s: str) -> date | None:
    """Accept YYYY-MM-DD; or YYYY-Q1..Q4 (use mid-quarter); or YYYY-MM (use 15th)."""
    if not s:
        return None
    s = str(s).strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", s)
    if m:
        try:
            return date.fromisoformat(s)
        except Exception:
            return None
    m = re.match(r"^(\d{4})-Q([1-4])$", s)
    if m:
        y = int(m.group(1)); q = int(m.group(2))
        month = q * 3 - 1  # mid-quarter
        return date(y, month, 15)
    m = re.match(r"^(\d{4})-(\d{2})$", s)
    if m:
        return date(int(m.group(1)), int(m.group(2)), 15)
    return None


def _classify_urgency(d: date, today: date) -> str:
    delta = (d - today).days
    if delta < 0:
        return "past"
    if delta <= 7:
        return "red"
    if delta <= 14:
        return "amber"
    if delta <= 30:
        return "grey"
    return "future"


def load_yaml_events() -> list[dict[str, Any]]:
    if not TIMELINE_YAML.exists():
        return []
    data = yaml.safe_load(TIMELINE_YAML.read_text()) or {}
    out = []
    for ev in data.get("events", []) or []:
        d = _parse_date_loose(ev.get("date"))
        if not d:
            continue
        out.append({
            "date": d.isoformat(),
            "kind": ev.get("kind", "catalyst"),
            "ticker": ev.get("ticker", ""),
            "note": ev.get("note", ""),
            "source": "yaml",
        })
    return out


def load_prediction_scoredates() -> list[dict[str, Any]]:
    if not ATTR_INDEX.exists():
        return []
    out = []
    seen = set()
    for line in ATTR_INDEX.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            continue
        tags = r.get("tags", []) or []
        if "prediction_recorded" not in tags:
            continue
        sd = r.get("score_date")
        d = _parse_date_loose(sd) if sd else None
        if not d:
            continue
        key = (d.isoformat(), r.get("ticker"))
        if key in seen:
            continue
        seen.add(key)
        cause = (r.get("primary_cause") or "")[:80]
        out.append({
            "date": d.isoformat(),
            "kind": "prediction",
            "ticker": r.get("ticker", ""),
            "note": f"Score prediction: {cause}",
            "source": "attribution_index",
        })
    return out


def _active_tickers() -> list[str]:
    """Every stocks/{T}/state.yaml with active: true."""
    out = []
    for sd in sorted(STOCKS_DIR.glob("*/state.yaml")):
        try:
            meta = yaml.safe_load(sd.read_text()) or {}
        except Exception:
            continue
        if meta.get("active") is True:
            out.append(sd.parent.name)
    return out


def _earnings_cache_get(ticker: str) -> str | None | bool:
    """Return cached next_earnings (str or None) if fresh, else False for a miss."""
    f = EARNINGS_CACHE / f"{ticker.replace('/', '_')}.json"
    if not f.exists():
        return False
    try:
        blob = json.loads(f.read_text())
        fetched = datetime.fromisoformat(blob["fetched_at"])
    except Exception:
        return False
    if (datetime.now() - fetched).total_seconds() > EARNINGS_TTL_SECONDS:
        return False
    return blob.get("next_earnings")


def _earnings_cache_put(ticker: str, next_earnings: str | None) -> None:
    EARNINGS_CACHE.mkdir(parents=True, exist_ok=True)
    f = EARNINGS_CACHE / f"{ticker.replace('/', '_')}.json"
    f.write_text(json.dumps({
        "ticker": ticker,
        "fetched_at": datetime.now().isoformat(),
        "next_earnings": next_earnings,
    }))


def load_active_earnings(no_fetch: bool = False) -> list[dict[str, Any]]:
    """Live next-earnings dates for every active stock, from yfinance with a 24h
    on-disk cache. yfinance is authoritative for the *date*; timeline.yaml stays
    authoritative for the *note* (scorecards, Tier-1 thresholds) — merge_and_sort
    combines them. Pass no_fetch=True to use only what's already cached."""
    out: list[dict[str, Any]] = []
    to_fetch: list[str] = []

    for t in _active_tickers():
        cached = _earnings_cache_get(t)
        if cached is False:
            to_fetch.append(t)
            continue
        if cached:
            out.append({"date": cached, "kind": "earnings", "ticker": t,
                        "note": "Earnings (yfinance calendar)", "source": "yfinance"})

    if to_fetch and not no_fetch:
        try:
            import yfinance as yf
        except ImportError:
            return out
        for t in to_fetch:
            ne: str | None = None
            try:
                cal = yf.Ticker(t).calendar or {}
                dates = cal.get("Earnings Date") if isinstance(cal, dict) else None
                if dates:
                    first = dates[0]
                    ne = first.isoformat() if hasattr(first, "isoformat") else str(first)
            except Exception:
                ne = None
            _earnings_cache_put(t, ne)
            if ne:
                out.append({"date": ne, "kind": "earnings", "ticker": t,
                            "note": "Earnings (yfinance calendar)", "source": "yfinance"})

    # Drop unparseable dates
    clean = []
    for ev in out:
        d = _parse_date_loose(ev["date"])
        if d:
            ev["date"] = d.isoformat()
            clean.append(ev)
    return clean


def merge_and_sort(today: date, all_events: list[dict]) -> list[dict]:
    """Dedup logic: two passes.
    1) Exact dedup on (date, ticker, kind, note-prefix)
    2) Same (kind, ticker) within ±2 days: keep the attribution-index entry (it's
       authoritative for prediction score_dates), drop the yaml-curated entry."""
    # Pass 1: exact dedup
    seen = set()
    pass1 = []
    for ev in all_events:
        key = (ev["date"], ev["ticker"], ev["kind"], ev["note"][:40])
        if key in seen:
            continue
        seen.add(key)
        pass1.append(ev)

    # Pass 1b: earnings reconciliation. yfinance owns the DATE, yaml owns the NOTE
    # (scorecards / Tier-1 thresholds). Within ±10 days for the same ticker, emit one
    # entry: yfinance date + yaml note, flagging the shift when the two disagree.
    yf_earnings = [e for e in pass1 if e["kind"] == "earnings" and e.get("source") == "yfinance"]
    consumed_yf: set[int] = set()
    reconciled = []
    for ev in pass1:
        if ev["kind"] != "earnings" or ev.get("source") == "yfinance":
            reconciled.append(ev)
            continue
        ev_date = date.fromisoformat(ev["date"])
        match = next((
            o for o in yf_earnings
            if o["ticker"] == ev["ticker"]
            and abs((date.fromisoformat(o["date"]) - ev_date).days) <= 10
        ), None)
        if not match:
            reconciled.append(ev)
            continue
        consumed_yf.add(id(match))
        merged = dict(ev)
        if match["date"] != ev["date"]:
            merged["note"] = (
                f"[日期已按 yfinance 校正: {ev['date']} → {match['date']}] {ev['note']}"
            )
            merged["date"] = match["date"]
            merged["date_corrected_from"] = ev["date"]
        merged["source"] = "yaml+yfinance"
        reconciled.append(merged)
    pass1 = [e for e in reconciled if id(e) not in consumed_yf]

    # Pass 2: near-date dedup for prediction kind (score_dates may drift between yaml + index)
    pass2 = []
    for ev in pass1:
        if ev["kind"] != "prediction":
            pass2.append(ev); continue
        ev_date = date.fromisoformat(ev["date"])
        # Check if an attribution_index entry exists within ±2 days for same ticker+kind
        rival = next((
            o for o in pass1
            if o is not ev
            and o["kind"] == "prediction"
            and o["ticker"] == ev["ticker"]
            and abs((date.fromisoformat(o["date"]) - ev_date).days) <= 2
        ), None)
        if rival and rival.get("source") == "attribution_index" and ev.get("source") != "attribution_index":
            # Drop ev (yaml version) in favor of authoritative attribution-index entry
            continue
        pass2.append(ev)

    # Annotate urgency, sort
    for ev in pass2:
        ev["urgency"] = _classify_urgency(date.fromisoformat(ev["date"]), today)
    pass2.sort(key=lambda e: (e["date"], e["ticker"]))
    return pass2


def format_md(events: list[dict], today: date) -> str:
    if not events:
        return "no upcoming events."
    lines = []
    # Group by urgency
    groups = {"red": [], "amber": [], "grey": [], "future": []}
    for ev in events:
        if ev["urgency"] == "past":
            continue
        groups.setdefault(ev["urgency"], []).append(ev)
    headers = {
        "red": "🔥 Within 7 days",
        "amber": "⚠ 8–14 days",
        "grey": "▢ 15–30 days",
        "future": "▢ 30+ days",
    }
    for tier in ["red", "amber", "grey", "future"]:
        if not groups.get(tier):
            continue
        lines.append(f"### {headers[tier]}")
        lines.append("")
        for ev in groups[tier]:
            ticker = f"**{ev['ticker']}**" if ev["ticker"] and ev["ticker"] != "macro" else ""
            kind_tag = f"`{ev['kind']}`"
            lines.append(f"- {ev['date']}  {kind_tag} {ticker}  — {ev['note']}")
        lines.append("")
    return "\n".join(lines).rstrip()


def format_timeline_block(events: list[dict]) -> str:
    """As a ```timeline visual block (renderer-friendly)."""
    if not events:
        return ""
    lines = ["```timeline"]
    for ev in events:
        if ev["urgency"] == "past":
            continue
        marker = {"red": "🔥", "amber": "⚠", "grey": "▢", "future": "▢"}.get(ev["urgency"], "")
        ticker = f"[{ev['ticker']}] " if ev["ticker"] and ev["ticker"] != "macro" else ""
        lines.append(f"{ev['date']} {marker} | {ticker}{ev['note']}")
    lines.append("```")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Build a workspace timeline")
    p.add_argument("--days", type=int, default=30, help="show events within N days (default 30)")
    p.add_argument("--as-of", help="treat this date as today (YYYY-MM-DD)")
    p.add_argument("--md", action="store_true", help="markdown output instead of JSON")
    p.add_argument("--block", action="store_true", help="render.py-compatible ```timeline``` block")
    p.add_argument("--ticker", help="filter to one ticker (or 'macro')")
    p.add_argument("--all", action="store_true", help="include past events too")
    p.add_argument("--no-fetch", action="store_true", help="use only cached earnings dates (no network)")
    args = p.parse_args()

    today = _today_iso(args.as_of)
    events = (
        load_yaml_events()
        + load_prediction_scoredates()
        + load_active_earnings(no_fetch=args.no_fetch)
    )
    events = merge_and_sort(today, events)

    if args.ticker:
        events = [e for e in events if e["ticker"].upper() == args.ticker.upper()]
    if not args.all:
        cutoff = today + timedelta(days=args.days)
        events = [
            e for e in events
            if date.fromisoformat(e["date"]) <= cutoff
            and date.fromisoformat(e["date"]) >= today
        ]

    if args.block:
        print(format_timeline_block(events))
    elif args.md:
        print(format_md(events, today))
    else:
        print(json.dumps(events, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
