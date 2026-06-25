"""Generate a ```chart``` markdown block from tickers' 30-day history.

Usage:
  uv run --project scripts scripts/build_chart.py MU NVDA TSM --title "AI/Memory 30d"
  uv run --project scripts scripts/build_chart.py MU --normalize  # rebase to 100
  uv run --project scripts scripts/build_chart.py --from-json /tmp/m_MU.json /tmp/m_NVDA.json

Outputs the markdown block to stdout — pipe or paste into the dashboard markdown.
The chart block is the canonical way to show daily price action in reports.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parent


def load_from_ticker(ticker: str) -> dict:
    """Run fetch.py for a single ticker and return its payload."""
    out = subprocess.run(
        ["uv", "run", "--project", str(SCRIPTS_DIR), str(SCRIPTS_DIR / "fetch.py"), ticker],
        capture_output=True,
        text=True,
        check=False,
    )
    if out.returncode != 0:
        sys.stderr.write(f"fetch.py {ticker} failed: {out.stderr[:200]}\n")
        return {}
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {}


def load_from_file(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as e:
        sys.stderr.write(f"failed to load {path}: {e}\n")
        return {}


def build_chart_md(
    payloads: list[dict],
    title: str | None = None,
    normalize: bool = False,
) -> str:
    """Compose a ```chart``` markdown block from fetch.py payloads."""
    lines: list[str] = ["```chart"]

    if title:
        lines.append(f"@title {title}")

    # x labels = dates from the longest series
    max_hist = max((p.get("history_30d") or [] for p in payloads), key=len, default=[])
    if max_hist:
        x_labels = ",".join(h["date"][5:] for h in max_hist)  # MM-DD
        lines.append(f"@xlabels {x_labels}")

    for p in payloads:
        t = p.get("ticker") or "?"
        hist = p.get("history_30d") or []
        if not hist:
            continue
        vals = [h["close"] for h in hist]
        if normalize and vals:
            base = vals[0]
            vals = [round(v / base * 100, 3) for v in vals] if base else vals
        # Note: last price + 1d/5d/30d in summary string
        price = p.get("price")
        c1 = p.get("change_pct_1d")
        c30 = p.get("change_pct_30d")
        note_parts = []
        if c1 is not None:
            sign = "+" if c1 >= 0 else ""
            note_parts.append(f"1d {sign}{c1}%")
        if c30 is not None:
            sign = "+" if c30 >= 0 else ""
            note_parts.append(f"30d {sign}{c30}%")
        note = " · ".join(note_parts) if note_parts else ""

        vals_str = ",".join(str(v) for v in vals)
        if note:
            lines.append(f"{t} | {vals_str} | {note}")
        else:
            lines.append(f"{t} | {vals_str}")

    lines.append("```")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tickers", nargs="*", help="Ticker symbols (e.g. MU NVDA)")
    ap.add_argument("--title", default=None, help="Chart title")
    ap.add_argument("--normalize", action="store_true", help="Rebase all series to 100 at start (compare returns)")
    ap.add_argument("--from-json", nargs="+", default=[], help="Use existing fetch.py JSON files instead of refetching")
    args = ap.parse_args()

    payloads: list[dict] = []
    for path in args.from_json:
        d = load_from_file(Path(path))
        if d:
            payloads.append(d)
    for t in args.tickers:
        d = load_from_ticker(t)
        if d:
            payloads.append(d)

    if not payloads:
        sys.stderr.write("no data\n")
        return 1

    sys.stdout.write(build_chart_md(payloads, title=args.title, normalize=args.normalize) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
