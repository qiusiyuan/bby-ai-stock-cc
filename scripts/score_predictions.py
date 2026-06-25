"""Score predictions whose score_date has arrived.

Reads attributions/index.jsonl, finds entries tagged `prediction_recorded` whose
score_date <= today, evaluates their `prediction_spec` against actual price history
(via yfinance), and writes a `verdict` field back into the same line.

CLI:
  uv run scripts/score_predictions.py                   # score everything due
  uv run scripts/score_predictions.py --as-of 2026-08-31 # treat this date as "today"
  uv run scripts/score_predictions.py --dry-run          # report verdicts, do not persist

Exit code 0 always (this is a query, not a build step).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yfinance as yf

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "attributions" / "index.jsonl"


def _today() -> date:
    return date.today()


def _parse_date(s: str) -> date:
    return date.fromisoformat(s)


def _strip_pred_suffix(d: str) -> str:
    """The recorder uses date suffixes like '2026-06-18#pred1' to allow multiple per day."""
    return d.split("#", 1)[0]


def _fetch_closes(ticker: str, start: date, end: date) -> dict[str, float]:
    """Return {YYYY-MM-DD: close_price} for trading days in [start, end] inclusive."""
    # yfinance end is exclusive — bump by 1 day
    from datetime import timedelta
    h = yf.Ticker(ticker).history(start=start.isoformat(), end=(end + timedelta(days=1)).isoformat(), interval="1d")
    out: dict[str, float] = {}
    if h is None or len(h) == 0:
        return out
    for ts, row in h.iterrows():
        d = ts.date().isoformat() if hasattr(ts, "date") else str(ts)[:10]
        try:
            out[d] = float(row["Close"])
        except Exception:
            continue
    return out


def _eval_close_above(spec: dict[str, Any]) -> dict[str, Any]:
    ticker = spec["ticker"]
    threshold = float(spec["threshold"])
    start = _parse_date(spec["window_start"])
    end = _parse_date(spec["window_end"])
    closes = _fetch_closes(ticker, start, end)
    if not closes:
        return {"state": "pending", "evidence": f"no price data for {ticker} in {start}..{end}"}
    hits = [(d, p) for d, p in closes.items() if p >= threshold]
    if hits:
        d, p = hits[0]
        return {
            "state": "pass",
            "evidence": f"closed ${p:.2f} on {d} — passes close_above {threshold}",
            "actual_high_in_window": max(closes.values()),
            "actual_low_in_window": min(closes.values()),
        }
    return {
        "state": "fail",
        "evidence": f"never closed >= {threshold} in {start}..{end}; high was ${max(closes.values()):.2f}",
        "actual_high_in_window": max(closes.values()),
        "actual_low_in_window": min(closes.values()),
    }


def _eval_close_below(spec: dict[str, Any]) -> dict[str, Any]:
    ticker = spec["ticker"]
    threshold = float(spec["threshold"])
    start = _parse_date(spec["window_start"])
    end = _parse_date(spec["window_end"])
    closes = _fetch_closes(ticker, start, end)
    if not closes:
        return {"state": "pending", "evidence": f"no price data for {ticker} in {start}..{end}"}
    hits = [(d, p) for d, p in closes.items() if p <= threshold]
    if hits:
        d, p = hits[0]
        return {
            "state": "pass",
            "evidence": f"closed ${p:.2f} on {d} — passes close_below {threshold}",
            "actual_high_in_window": max(closes.values()),
            "actual_low_in_window": min(closes.values()),
        }
    return {
        "state": "fail",
        "evidence": f"never closed <= {threshold} in {start}..{end}; low was ${min(closes.values()):.2f}",
        "actual_high_in_window": max(closes.values()),
        "actual_low_in_window": min(closes.values()),
    }


def _eval_range(spec: dict[str, Any]) -> dict[str, Any]:
    ticker = spec["ticker"]
    low = float(spec["low"])
    high = float(spec["high"])
    hard_low = float(spec["hard_low"]) if "hard_low" in spec else None
    hard_high = float(spec["hard_high"]) if "hard_high" in spec else None
    start = _parse_date(spec["window_start"])
    end = _parse_date(spec["window_end"])
    closes = _fetch_closes(ticker, start, end)
    if not closes:
        return {"state": "pending", "evidence": f"no price data for {ticker} in {start}..{end}"}

    actual_high = max(closes.values())
    actual_low = min(closes.values())

    # hard_high / hard_low are kill-switches: if breached, range fails outright
    if hard_high is not None and actual_high > hard_high:
        d = next(d for d, p in closes.items() if p == actual_high)
        return {
            "state": "fail",
            "evidence": f"breached hard_high {hard_high} — closed ${actual_high:.2f} on {d}",
            "actual_high_in_window": actual_high,
            "actual_low_in_window": actual_low,
        }
    if hard_low is not None and actual_low < hard_low:
        d = next(d for d, p in closes.items() if p == actual_low)
        return {
            "state": "fail",
            "evidence": f"breached hard_low {hard_low} — closed ${actual_low:.2f} on {d}",
            "actual_high_in_window": actual_high,
            "actual_low_in_window": actual_low,
        }

    # Soft band: pass if every close in [low, high]; fail otherwise
    out_of_band = [(d, p) for d, p in closes.items() if p < low or p > high]
    if not out_of_band:
        return {
            "state": "pass",
            "evidence": f"every close in [{low}, {high}]; range was [{actual_low:.2f}, {actual_high:.2f}]",
            "actual_high_in_window": actual_high,
            "actual_low_in_window": actual_low,
        }
    # Tolerant pass: ≥80% of days in band counts as pass with a note
    in_band_pct = (len(closes) - len(out_of_band)) / len(closes)
    return {
        "state": "fail" if in_band_pct < 0.80 else "pass",
        "evidence": (
            f"{in_band_pct:.0%} of closes in [{low}, {high}]; "
            f"range was [{actual_low:.2f}, {actual_high:.2f}]; "
            f"{len(out_of_band)} day(s) out of band"
        ),
        "actual_high_in_window": actual_high,
        "actual_low_in_window": actual_low,
    }


def _eval_conditional(spec: dict[str, Any]) -> dict[str, Any]:
    if_v = evaluate(spec["if_spec"])
    if_state = if_v.get("state")
    if if_state == "pending":
        return {"state": "pending", "evidence": f"trigger inconclusive (no data yet): {if_v.get('evidence','')}", "trigger_verdict": if_v}
    if if_state == "fail":
        return {"state": "n/a", "evidence": f"trigger did not fire: {if_v.get('evidence','')}", "trigger_verdict": if_v}
    # if_state == "pass"
    then_v = evaluate(spec["then_spec"])
    return {
        "state": then_v.get("state", "pending"),
        "evidence": f"trigger fired ({if_v.get('evidence','')}); outcome: {then_v.get('evidence','')}",
        "trigger_verdict": if_v,
        "outcome_verdict": then_v,
    }


def _eval_trigger_chain(spec: dict[str, Any]) -> dict[str, Any]:
    trig = evaluate(spec["trigger"])
    trig_state = trig.get("state")
    if trig_state == "pending":
        return {"state": "pending", "evidence": f"chain trigger inconclusive (no data yet): {trig.get('evidence','')}", "trigger_verdict": trig}
    if trig_state == "fail":
        return {"state": "n/a", "evidence": f"chain trigger did not fire: {trig.get('evidence','')}", "trigger_verdict": trig}
    # trig_state == "pass"
    out = evaluate(spec["outcome"])
    return {
        "state": out.get("state", "pending"),
        "evidence": f"chain triggered ({trig.get('evidence','')}); outcome: {out.get('evidence','')}",
        "trigger_verdict": trig,
        "outcome_verdict": out,
    }


EVALUATORS = {
    "close_above": _eval_close_above,
    "close_below": _eval_close_below,
    "range": _eval_range,
    "conditional": _eval_conditional,
    "trigger_chain": _eval_trigger_chain,
}


def evaluate(spec: dict[str, Any]) -> dict[str, Any]:
    kind = spec.get("kind")
    fn = EVALUATORS.get(kind)
    if fn is None:
        return {"state": "pending", "evidence": f"unknown spec kind: {kind}"}
    try:
        return fn(spec)
    except Exception as e:
        return {"state": "pending", "evidence": f"evaluation error: {e}"}


def _is_due(rec: dict[str, Any], as_of: date) -> bool:
    sd = rec.get("score_date")
    if not sd:
        return False
    try:
        return _parse_date(sd) <= as_of
    except Exception:
        return False


def _is_prediction(rec: dict[str, Any]) -> bool:
    return "prediction_recorded" in (rec.get("tags") or [])


def _has_verdict(rec: dict[str, Any]) -> bool:
    v = rec.get("verdict")
    return bool(v and v.get("state") in {"pass", "fail", "n/a"})


def main() -> int:
    parser = argparse.ArgumentParser(description="Score due predictions in attributions/index.jsonl")
    parser.add_argument("--as-of", default=None, help="Treat this date as 'today' (YYYY-MM-DD)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--rescore", action="store_true", help="Re-evaluate even predictions that already have a verdict")
    args = parser.parse_args()

    as_of = _parse_date(args.as_of) if args.as_of else _today()
    if not INDEX_PATH.exists():
        print(json.dumps({"due": 0, "scored": 0, "results": []}))
        return 0

    lines = INDEX_PATH.read_text().splitlines()
    new_lines: list[str] = []
    results: list[dict[str, Any]] = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except Exception:
            new_lines.append(line)
            continue

        if not _is_prediction(rec):
            new_lines.append(line)
            continue

        if not _is_due(rec, as_of):
            new_lines.append(line)
            continue

        if _has_verdict(rec) and not args.rescore:
            new_lines.append(line)
            continue

        spec = rec.get("prediction_spec")
        if not spec:
            # No structured spec — flag for manual scoring
            rec["verdict"] = {
                "state": "pending",
                "evidence": "no prediction_spec — manual scoring required",
                "scored_on": as_of.isoformat(),
            }
            new_lines.append(json.dumps(rec, default=str))
            results.append({"key": f"{rec.get('date')}/{rec.get('ticker')}", "verdict": rec["verdict"]})
            continue

        verdict = evaluate(spec)
        verdict["scored_on"] = as_of.isoformat()
        rec["verdict"] = verdict
        new_lines.append(json.dumps(rec, default=str))
        results.append({
            "key": f"{rec.get('date')}/{rec.get('ticker')}",
            "primary_cause": (rec.get("primary_cause") or "")[:120],
            "verdict": verdict,
            "agent_probability": rec.get("agent_probability"),
        })

    if not args.dry_run:
        INDEX_PATH.write_text("\n".join(new_lines) + "\n")

    out = {
        "as_of": as_of.isoformat(),
        "due_count": len(results),
        "scored": [r for r in results if r["verdict"]["state"] in {"pass", "fail", "n/a"}],
        "still_pending": [r for r in results if r["verdict"]["state"] == "pending"],
    }
    json.dump(out, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
