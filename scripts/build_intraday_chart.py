"""Build a ```chart``` markdown block from intraday bars (with pre/post-market).

Usage:
  uv run --project scripts scripts/build_intraday_chart.py MU
  uv run --project scripts scripts/build_intraday_chart.py MU --interval 5m
  uv run --project scripts scripts/build_intraday_chart.py MU NVDA TSM --interval 15m

Outputs the chart block to stdout. Each bar = one point; session is encoded as
note (pre/regular/post). The chart renderer doesn't draw session backgrounds
(yet), so we put '|' separators in the legend note to flag where pre/post ends.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parent


def fetch(ticker: str, interval: str, period: str, prepost: bool) -> dict:
    cmd = [
        "uv", "run", "--project", str(SCRIPTS_DIR),
        str(SCRIPTS_DIR / "fetch_intraday.py"),
        ticker, "--interval", interval, "--period", period,
    ]
    if not prepost:
        cmd.append("--no-prepost")
    out = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if out.returncode != 0:
        sys.stderr.write(f"fetch_intraday {ticker} failed: {out.stderr[:200]}\n")
        return {}
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {}


def format_time(ts_iso: str) -> str:
    """Convert '2026-06-24T09:30-04:00' to '09:30'."""
    try:
        t = ts_iso.split("T")[1][:5]
        return t
    except Exception:
        return ts_iso


def build(
    payloads: list[dict],
    title: str | None = None,
    normalize: bool = False,
    label_step: int = 12,
) -> str:
    """Compose chart block. label_step controls x-label density."""
    lines: list[str] = ["```chart"]
    if title:
        lines.append(f"@title {title}")

    # Build x-axis labels from the longest bar series
    longest = max(payloads, key=lambda p: len(p.get("bars", [])), default={"bars": []})
    bars = longest.get("bars", [])

    # Sparse x labels: every label_step-th bar
    if bars:
        labels = []
        for i, b in enumerate(bars):
            if i % label_step == 0 or i == len(bars) - 1:
                labels.append(format_time(b["t"]))
            else:
                labels.append("")  # keep alignment
        # Compact: only emit labels that are non-empty, but renderer takes sparse hint already
        compact_labels = [labels[0]]
        # Add at intervals
        for i in range(label_step, len(labels), label_step):
            compact_labels.append(labels[i] if labels[i] else format_time(bars[i]["t"]))
        if compact_labels[-1] != format_time(bars[-1]["t"]):
            compact_labels.append(format_time(bars[-1]["t"]))
        lines.append(f"@xlabels {','.join(compact_labels)}")

    for p in payloads:
        if not p:
            continue
        t = p.get("ticker", "?")
        bars = p.get("bars", [])
        summary = p.get("summary", {})
        if not bars:
            continue
        closes = [b["close"] for b in bars if b["close"] is not None]
        if not closes:
            continue
        if normalize:
            base = closes[0]
            closes = [round(v / base * 100, 3) for v in closes] if base else closes

        # Note: regular % + post %
        note_parts = []
        if summary.get("regular_change_pct") is not None:
            sign = "+" if summary["regular_change_pct"] >= 0 else ""
            note_parts.append(f"reg {sign}{summary['regular_change_pct']}%")
        if summary.get("post_change_pct") is not None:
            sign = "+" if summary["post_change_pct"] >= 0 else ""
            note_parts.append(f"post {sign}{summary['post_change_pct']}%")
        if summary.get("session_high") and summary.get("session_low"):
            note_parts.append(f"range ${summary['session_low']:.2f}-${summary['session_high']:.2f}")
        note = " · ".join(note_parts)

        vals_str = ",".join(str(v) for v in closes)
        if note:
            lines.append(f"{t} | {vals_str} | {note}")
        else:
            lines.append(f"{t} | {vals_str}")

    lines.append("```")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tickers", nargs="+")
    ap.add_argument("--interval", default="5m")
    ap.add_argument("--period", default="1d")
    ap.add_argument("--no-prepost", dest="prepost", action="store_false", default=True)
    ap.add_argument("--title", default=None)
    ap.add_argument("--normalize", action="store_true")
    ap.add_argument("--label-step", type=int, default=12, help="emit an x-label every N bars (default 12)")
    args = ap.parse_args()

    payloads = [fetch(t, args.interval, args.period, args.prepost) for t in args.tickers]
    payloads = [p for p in payloads if p]
    if not payloads:
        sys.stderr.write("no data\n")
        return 1

    sys.stdout.write(build(payloads, title=args.title, normalize=args.normalize, label_step=args.label_step) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
