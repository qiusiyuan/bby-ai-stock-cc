"""Search past analyses in dashboard/{YYYY-MM-DD}.md files.

Per-day dashboards have top-level H2 sections — each is one analysis unit
(Morning, Attribution, "AI capex analysis", "SPCX pressure-test", etc.).
This script scans them and returns matches by keyword / ticker / date.

CLI:
  uv run --project scripts scripts/find_analysis.py --keyword "ai capex"
  uv run --project scripts scripts/find_analysis.py --ticker SPCX
  uv run --project scripts scripts/find_analysis.py --since 2026-06-01
  uv run --project scripts scripts/find_analysis.py                       # list everything

Filter logic (AND across types, OR within):
  --keyword "X"            substring (case-insensitive) in H2 title OR body
  --ticker SPCX            ticker mentioned in title or body (also matches the
                           section's H2 title — useful for "Compare AMD vs MU")
  --since YYYY-MM-DD       inclusive
  --until YYYY-MM-DD       inclusive
  --titles-only            skip body; only match against H2 title
  --json                   raw JSON (default: pretty list)

Output (default): a markdown-style listing — date · title · tickers · 1-line preview.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DASHBOARD = ROOT / "dashboard"
STOCKS = ROOT / "stocks"
RESEARCH = ROOT / "research"

DATE_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")
RESEARCH_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+?)\.md$")
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
# Tickers: 2-6 caps, optional .EXCHANGE or ^ prefix (indexes) or =F (futures)
TICKER_RE = re.compile(r"(?<![\w.])(\^?[A-Z]{1,6}(?:\.[A-Z]{1,3})?(?:=F)?|\d{6}\.KS)(?![\w])")
# Filler words that look like tickers but aren't
NOT_TICKERS = {
    "I", "A", "AI", "US", "AM", "PM", "GMT", "ET", "USD", "PE", "EPS", "TAM",
    "PR", "FAQ", "HLD", "LLD", "FOMC", "SEC", "FTC", "DOJ", "FCC", "EU",
    "GDP", "CPI", "PPI", "PCE", "ETF", "IPO", "ARPU", "ROI", "DCF", "ROIC",
    "API", "URL", "CEO", "CFO", "CTO", "BPS", "EBITDA", "Q1", "Q2", "Q3", "Q4",
    "OK", "NO", "OK", "VS", "AKA", "AGI", "ML", "MIA",
    # Calendar etc.
    "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC",
    "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN",
}


def _fenced_ranges(md: str) -> list[tuple[int, int]]:
    """Outermost fenced [start, end) ranges (handles nested fences)."""
    ranges = []
    pos = 0
    while pos < len(md):
        m = re.search(r"^```(\w[^\n]*)$", md[pos:], re.MULTILINE)
        if not m:
            break
        start = pos + m.start()
        scan = pos + m.end()
        depth = 1
        while scan < len(md) and depth > 0:
            nxt = re.search(r"^```([^\n]*)$", md[scan:], re.MULTILINE)
            if not nxt:
                scan = len(md); break
            tag = nxt.group(1).strip()
            line_end = scan + nxt.end()
            depth += 1 if tag else -1
            scan = line_end
            if depth == 0:
                ranges.append((start, scan))
                pos = scan
                break
        if depth > 0:
            break
    return ranges


def extract_h2_sections(md: str) -> list[tuple[str, str]]:
    """Return [(title, body)] for each TOP-LEVEL H2 (outside any fence)."""
    fenced = _fenced_ranges(md)
    in_fence = lambda p: any(s <= p < e for s, e in fenced)
    h2s = [m for m in H2_RE.finditer(md) if not in_fence(m.start())]
    sections = []
    for i, m in enumerate(h2s):
        title = m.group(1).strip()
        body_start = m.end()
        body_end = h2s[i + 1].start() if i + 1 < len(h2s) else len(md)
        sections.append((title, md[body_start:body_end].strip()))
    return sections


def extract_tickers(text: str) -> list[str]:
    seen: list[str] = []
    for m in TICKER_RE.finditer(text):
        t = m.group(1)
        if t in NOT_TICKERS:
            continue
        if t not in seen:
            seen.append(t)
    return seen


def preview(body: str, limit: int = 200) -> str:
    """First non-empty prose paragraph, fenced blocks stripped."""
    # Drop fenced blocks
    body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    # Drop H3+ headers, lists markers
    lines = []
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith(">"):
            continue
        lines.append(s)
    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text)
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "…"


def _matches_filters(text: str, tickers_in: list[str], title: str,
                     kw: str | None, tk: str | None, titles_only: bool) -> bool:
    if kw:
        hay = title.lower() if titles_only else text.lower()
        if kw not in hay:
            return False
    if tk:
        if tk not in tickers_in and tk.lower() not in title.lower():
            return False
    return True


def _scan_dashboard(kw, tk, since, until, titles_only) -> list[dict]:
    out = []
    for p in sorted(DASHBOARD.glob("*.md"), reverse=True):
        m = DATE_FILE_RE.match(p.name)
        if not m:
            continue
        date_str = m.group(1)
        if since and date_str < since: continue
        if until and date_str > until: continue
        md = p.read_text()
        for title, body in extract_h2_sections(md):
            tickers_in = extract_tickers(title + " " + body)
            if not _matches_filters(title + " " + body, tickers_in, title, kw, tk, titles_only):
                continue
            out.append({
                "date": date_str,
                "kind": "dashboard",
                "title": title,
                "path": str(p.relative_to(ROOT)),
                "tickers": tickers_in[:8],
                "preview": preview(body),
            })
    return out


def _scan_research_dir(base: Path, default_ticker: str | None,
                       kw, tk, since, until, titles_only) -> list[dict]:
    """Scan one research dir. Each file is one H1 doc."""
    out = []
    if not base.exists():
        return out
    for p in sorted(base.glob("*.md"), reverse=True):
        m = RESEARCH_FILE_RE.match(p.name)
        if not m:
            continue
        date_str, topic_slug = m.group(1), m.group(2)
        if since and date_str < since: continue
        if until and date_str > until: continue
        md = p.read_text()
        # Title = first H1 line, fallback to slug
        h1 = re.search(r"^#\s+(.+?)\s*$", md, re.MULTILINE)
        title = h1.group(1) if h1 else topic_slug.replace("-", " ").title()
        tickers_in = extract_tickers(title + " " + md)
        if default_ticker and default_ticker not in tickers_in:
            tickers_in = [default_ticker] + tickers_in
        if not _matches_filters(title + " " + md, tickers_in, title, kw, tk, titles_only):
            continue
        out.append({
            "date": date_str,
            "kind": "research",
            "title": title,
            "path": str(p.relative_to(ROOT)),
            "tickers": tickers_in[:8],
            "preview": preview(md),
        })
    return out


def scan(
    keyword: str | None = None,
    ticker: str | None = None,
    since: str | None = None,
    until: str | None = None,
    titles_only: bool = False,
    include_dashboard: bool = True,
    include_research: bool = True,
) -> list[dict[str, Any]]:
    out = []
    kw = keyword.lower() if keyword else None
    tk = ticker.upper() if ticker else None

    if include_dashboard:
        out += _scan_dashboard(kw, tk, since, until, titles_only)

    if include_research:
        # Per-stock research
        if STOCKS.exists():
            for stock_dir in sorted(STOCKS.iterdir()):
                if not stock_dir.is_dir(): continue
                research_dir = stock_dir / "research"
                if not research_dir.exists(): continue
                out += _scan_research_dir(research_dir, stock_dir.name, kw, tk, since, until, titles_only)
        # Cross-cutting research
        for sub in ["sectors", "cases"]:
            out += _scan_research_dir(RESEARCH / sub, None, kw, tk, since, until, titles_only)

    out.sort(key=lambda r: r["date"], reverse=True)
    return out


def format_md(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "no analyses match."
    lines = []
    for r in rows:
        ts = ", ".join(r["tickers"][:6]) if r["tickers"] else "—"
        kind_tag = f"[{r.get('kind','?')}]"
        lines.append(f"**{r['date']}** {kind_tag} · {r['title']}  ·  _{ts}_")
        lines.append(f"  → `{r['path']}`")
        if r["preview"]:
            lines.append(f"  {r['preview']}")
        lines.append("")
    return "\n".join(lines).rstrip()


def main() -> int:
    p = argparse.ArgumentParser(description="Search past analyses in dashboard/*.md")
    p.add_argument("--keyword", help="substring match in title and body")
    p.add_argument("--ticker", help="ticker mentioned in section")
    p.add_argument("--since", help="YYYY-MM-DD inclusive")
    p.add_argument("--until", help="YYYY-MM-DD inclusive")
    p.add_argument("--titles-only", action="store_true", help="match keyword against H2 titles only")
    p.add_argument("--dashboard-only", action="store_true", help="only scan dashboard/{date}.md (skip research)")
    p.add_argument("--research-only", action="store_true", help="only scan stocks/*/research and research/")
    p.add_argument("--json", action="store_true", help="raw JSON output")
    args = p.parse_args()

    rows = scan(
        keyword=args.keyword,
        ticker=args.ticker,
        since=args.since,
        until=args.until,
        titles_only=args.titles_only,
        include_dashboard=not args.research_only,
        include_research=not args.dashboard_only,
    )
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        print(format_md(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
