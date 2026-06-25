"""Render a markdown file (or string) to a visual HTML report and open it.

CLI:
  uv run scripts/render.py path/to/file.md           # render + open
  uv run scripts/render.py path/to/file.md --no-open # just render
  uv run scripts/render.py - --title "Report"        # read markdown from stdin
  uv run scripts/render.py --session 2026-06-23      # bundle dashboard/*-2026-06-23.md
                                                      # into one tabbed page
  uv run scripts/render.py file.md --session 2026-06-23
                                                      # add/refresh ONE tab in today's
                                                      # session page (use from skills)

Output: site/reports/<slug>.html, overwritten on re-render.
        site/reports/session-<DATE>.html for --session mode.

## Custom blocks (scannable visual elements)

Use fenced blocks with these languages — render.py converts them BEFORE markdown parsing:

```kpi
Price | $185 | -3.6% today
Market cap | $2.4T | largest IPO ever
P/E forward | n/a | still loss-making
ARPU (Starlink) | $66 | down from $99 (2023)
```

```scenarios
Bull | 25 | $300+ | Starship reliable cargo + Starlink 30M subs
Base | 50 | $220 | Starlink 20M subs at $55 ARPU
Bear | 25 | $130  | Starship delays + ARPU compression
```

```meter
Moat | 7 | strong
Management trust | 5 | concentrated voting control
Valuation discipline | 3 | prices the bull case
Balance sheet | 7 | $86B IPO cash, low debt
```

```callout warn
Triggers proposed — confirm thesis-break ($130) and kill conditions before next check.
```
(Other callout kinds: info, ok, danger)

```timeline
2026-06-12 | IPO at $1.77T valuation
2026-Q3   | First post-IPO earnings (likely)
2026-12-09 | Lock-up expiry (180d)
```

```compare
Metric         | NVDA       | AMD
Price          | $210       | $165
P/E forward    | 16.5       | 32.1
30d %          | +1.5%      | -2.4%
Moat           | strong     | medium
```
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

import markdown


CSS = """
:root {
  --bg: #0d1117;
  --panel: #161b22;
  --panel-2: #1c2128;
  --fg: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;
  --green: #3fb950;
  --green-bg: rgba(63, 185, 80, 0.15);
  --red: #f85149;
  --red-bg: rgba(248, 81, 73, 0.15);
  --amber: #d29922;
  --amber-bg: rgba(210, 153, 34, 0.15);
  --blue-bg: rgba(88, 166, 255, 0.12);
  --border: #30363d;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #ffffff;
    --panel: #f6f8fa;
    --panel-2: #eaeef2;
    --fg: #1f2328;
    --muted: #59636e;
    --accent: #0969da;
    --green: #1a7f37;
    --green-bg: rgba(26, 127, 55, 0.12);
    --red: #cf222e;
    --red-bg: rgba(207, 34, 46, 0.12);
    --amber: #9a6700;
    --amber-bg: rgba(154, 103, 0, 0.12);
    --blue-bg: rgba(9, 105, 218, 0.10);
    --border: #d0d7de;
  }
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  font-size: 15px;
  line-height: 1.55;
  color: var(--fg);
  background: var(--bg);
  padding: 32px;
  max-width: 1040px;
  margin: 0 auto;
}
h1, h2, h3, h4 { line-height: 1.25; margin-top: 1.6em; margin-bottom: 0.5em; }
h1 { font-size: 2em; border-bottom: 1px solid var(--border); padding-bottom: 10px; }
h2 { font-size: 1.4em; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
h3 { font-size: 1.1em; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }
p, ul, ol, table { margin: 0.6em 0; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
code {
  font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
  font-size: 0.92em;
  background: var(--panel);
  padding: 2px 6px;
  border-radius: 4px;
}
pre { background: var(--panel); padding: 14px 16px; border-radius: 6px; overflow-x: auto; border: 1px solid var(--border); }
pre code { background: transparent; padding: 0; }
table { border-collapse: collapse; width: 100%; font-size: 0.94em; }
th, td { padding: 8px 12px; border: 1px solid var(--border); text-align: left; }
th { background: var(--panel); font-weight: 600; }
tr:nth-child(even) td { background: rgba(110, 118, 129, 0.06); }
blockquote { border-left: 4px solid var(--accent); margin: 1em 0; padding: 4px 16px; color: var(--muted); background: var(--panel); border-radius: 0 4px 4px 0; }
hr { border: 0; border-top: 1px solid var(--border); margin: 2em 0; }
.meta { color: var(--muted); font-size: 0.86em; margin-bottom: 2em; border-bottom: 1px solid var(--border); padding-bottom: 12px; }
.up { color: var(--green); font-weight: 600; }
.down { color: var(--red); font-weight: 600; }
.warn { color: var(--amber); font-weight: 600; }

/* KPI grid */
.kpi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; margin: 1em 0; }
.kpi { background: var(--panel); border: 1px solid var(--border); border-radius: 8px; padding: 14px 16px; }
.kpi .label { color: var(--muted); font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.06em; }
.kpi .value { font-size: 1.5em; font-weight: 700; margin: 6px 0 4px; }
.kpi .note { color: var(--muted); font-size: 0.85em; }

/* Scenario bars */
.scenarios { margin: 1em 0; }
.scenario { display: grid; grid-template-columns: 80px 1fr 130px; gap: 12px; align-items: center; padding: 10px 0; border-bottom: 1px solid var(--border); }
.scenario:last-child { border-bottom: 0; }
.scenario .name { font-weight: 600; }
.scenario .name.bull { color: var(--green); }
.scenario .name.base { color: var(--accent); }
.scenario .name.bear { color: var(--red); }
.scenario .bar-wrap { background: var(--panel); border-radius: 4px; height: 22px; position: relative; overflow: hidden; }
.scenario .bar { height: 100%; border-radius: 4px; display: flex; align-items: center; padding: 0 10px; color: white; font-weight: 600; font-size: 0.85em; min-width: 48px; }
.scenario .bar.bull { background: var(--green); }
.scenario .bar.base { background: var(--accent); }
.scenario .bar.bear { background: var(--red); }
.scenario .target { font-weight: 600; text-align: right; }
.scenario .desc { color: var(--muted); font-size: 0.88em; padding: 4px 0 0 92px; grid-column: 1 / -1; }

/* Score meters */
.meters { display: grid; grid-template-columns: 1fr; gap: 10px; margin: 1em 0; }
.meter { display: grid; grid-template-columns: 200px 1fr 30px; gap: 12px; align-items: center; padding: 6px 0; }
.meter .name { font-weight: 500; }
.meter .track { background: var(--panel); border-radius: 4px; height: 14px; position: relative; overflow: hidden; border: 1px solid var(--border); }
.meter .fill { height: 100%; border-radius: 3px; }
.meter .fill.high { background: var(--green); }
.meter .fill.mid { background: var(--amber); }
.meter .fill.low { background: var(--red); }
.meter .score { text-align: right; font-weight: 600; font-variant-numeric: tabular-nums; }
.meter .note { grid-column: 2 / -1; color: var(--muted); font-size: 0.85em; padding-top: 2px; }

/* Callouts */
.callout { padding: 12px 16px; border-radius: 6px; border-left: 4px solid; margin: 1.2em 0; }
.callout.info { background: var(--blue-bg); border-color: var(--accent); }
.callout.ok { background: var(--green-bg); border-color: var(--green); }
.callout.warn { background: var(--amber-bg); border-color: var(--amber); }
.callout.danger { background: var(--red-bg); border-color: var(--red); }
.callout strong { display: block; margin-bottom: 4px; }

/* Timeline */
.timeline { margin: 1em 0; padding-left: 12px; border-left: 2px solid var(--border); }
.tl-item { position: relative; padding: 6px 0 6px 18px; }
.tl-item::before { content: ''; position: absolute; left: -19px; top: 14px; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); border: 2px solid var(--bg); }
.tl-item .when { font-weight: 600; color: var(--accent); font-size: 0.92em; }
.tl-item .what { color: var(--fg); }

/* Compare strip */
.compare { width: 100%; margin: 1em 0; border-collapse: collapse; }
.compare th, .compare td { padding: 10px 14px; border: 1px solid var(--border); }
.compare th { background: var(--panel); font-weight: 600; }
.compare th:first-child, .compare td:first-child { font-weight: 600; color: var(--muted); width: 30%; }

/* Tabs */
.tabs { display: flex; gap: 4px; margin: 1.5em 0 0; border-bottom: 1px solid var(--border); flex-wrap: wrap; }
.tab-label { padding: 10px 18px; cursor: pointer; border: 1px solid transparent; border-bottom: none; border-radius: 6px 6px 0 0; color: var(--muted); font-weight: 600; user-select: none; transition: background 0.15s; }
.tab-label:hover { background: var(--panel); color: var(--fg); }
.tab-input { display: none; }
.tab-input:checked + .tab-label { background: var(--bg); color: var(--accent); border-color: var(--border); border-bottom: 1px solid var(--bg); margin-bottom: -1px; position: relative; z-index: 2; }
.tab-panel { display: none; padding: 20px 4px; animation: fadeIn 0.15s; }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

/* Verdict pill */
.verdict { display: inline-block; padding: 6px 14px; border-radius: 999px; font-weight: 700; margin: 4px 0; }
.verdict.bull, .verdict.add { background: var(--green-bg); color: var(--green); border: 1px solid var(--green); }
.verdict.hold, .verdict.watch, .verdict.neutral { background: var(--blue-bg); color: var(--accent); border: 1px solid var(--accent); }
.verdict.trim, .verdict.caution { background: var(--amber-bg); color: var(--amber); border: 1px solid var(--amber); }
.verdict.bear, .verdict.exit, .verdict.sell { background: var(--red-bg); color: var(--red); border: 1px solid var(--red); }

/* Chart block */
.chart-block { margin: 1em 0; }
.chart-svg { width: 100%; height: auto; max-width: 100%; display: block; }
.chart-legend { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 6px; padding: 0 6px; font-size: 0.88em; font-family: ui-monospace, monospace; }
.legend-item { display: inline-flex; align-items: center; gap: 6px; }
.legend-swatch { display: inline-block; width: 10px; height: 10px; border-radius: 2px; }
.legend-name { color: var(--fg); font-weight: 600; }
.legend-last { color: var(--muted); }
.legend-pct { font-weight: 600; }
.legend-note { color: var(--muted); margin-left: 4px; }
"""

PCT_RE = re.compile(r"(?<![\w.])([+-]?\d+\.?\d*)%")
FENCE_RE = re.compile(r"```(\w+)([^\n]*)\n(.*?)```", re.DOTALL)


def colorize_percentages(html_text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        full = m.group(0)
        num = m.group(1)
        if num.startswith("+"):
            return f'<span class="up">{full}</span>'
        if num.startswith("-"):
            return f'<span class="down">{full}</span>'
        return full
    return PCT_RE.sub(repl, html_text)


def _esc(s: str) -> str:
    return html.escape(s.strip())


def _split_rows(body: str) -> list[list[str]]:
    rows = []
    for line in body.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        rows.append(parts)
    return rows


def render_kpi(body: str) -> str:
    rows = _split_rows(body)
    cards = []
    for r in rows:
        label = _esc(r[0]) if len(r) > 0 else ""
        value = _esc(r[1]) if len(r) > 1 else ""
        note = _esc(r[2]) if len(r) > 2 else ""
        cards.append(
            f'<div class="kpi"><div class="label">{label}</div>'
            f'<div class="value">{colorize_percentages(value)}</div>'
            f'<div class="note">{colorize_percentages(note)}</div></div>'
        )
    return f'<div class="kpi-grid">{"".join(cards)}</div>'


def render_scenarios(body: str) -> str:
    rows = _split_rows(body)
    out = ['<div class="scenarios">']
    for r in rows:
        name = r[0] if len(r) > 0 else ""
        try:
            pct = max(0, min(100, int(float(r[1])))) if len(r) > 1 else 0
        except ValueError:
            pct = 0
        target = r[2] if len(r) > 2 else ""
        desc = r[3] if len(r) > 3 else ""
        kind = name.lower()
        css_class = "bull" if "bull" in kind else "bear" if "bear" in kind else "base"
        out.append(
            f'<div class="scenario">'
            f'<div class="name {css_class}">{_esc(name)}</div>'
            f'<div class="bar-wrap"><div class="bar {css_class}" style="width:{pct}%">{pct}%</div></div>'
            f'<div class="target">{_esc(target)}</div>'
            + (f'<div class="desc">{_esc(desc)}</div>' if desc else "")
            + "</div>"
        )
    out.append("</div>")
    return "".join(out)


def render_meter(body: str) -> str:
    rows = _split_rows(body)
    out = ['<div class="meters">']
    for r in rows:
        name = r[0] if len(r) > 0 else ""
        try:
            score = max(0, min(10, int(float(r[1])))) if len(r) > 1 else 0
        except ValueError:
            score = 0
        note = r[2] if len(r) > 2 else ""
        css_class = "high" if score >= 7 else "mid" if score >= 4 else "low"
        out.append(
            f'<div class="meter">'
            f'<div class="name">{_esc(name)}</div>'
            f'<div class="track"><div class="fill {css_class}" style="width:{score * 10}%"></div></div>'
            f'<div class="score">{score}/10</div>'
            + (f'<div class="note">{_esc(note)}</div>' if note else "")
            + "</div>"
        )
    out.append("</div>")
    return "".join(out)


def render_callout(kind: str, body: str) -> str:
    kind = (kind or "info").strip().lower()
    if kind not in {"info", "ok", "warn", "danger"}:
        kind = "info"
    return f'<div class="callout {kind}">{markdown.markdown(body.strip(), extensions=["sane_lists"])}</div>'


def render_timeline(body: str) -> str:
    rows = _split_rows(body)
    out = ['<div class="timeline">']
    for r in rows:
        when = r[0] if len(r) > 0 else ""
        what = r[1] if len(r) > 1 else ""
        out.append(
            f'<div class="tl-item">'
            f'<span class="when">{_esc(when)}</span> — '
            f'<span class="what">{_esc(what)}</span></div>'
        )
    out.append("</div>")
    return "".join(out)


def render_compare(body: str) -> str:
    rows = _split_rows(body)
    if not rows:
        return ""
    header, *body_rows = rows
    th = "".join(f"<th>{_esc(c)}</th>" for c in header)
    body_html = []
    for r in body_rows:
        cells = "".join(f"<td>{colorize_percentages(_esc(c))}</td>" for c in r)
        body_html.append(f"<tr>{cells}</tr>")
    return f'<table class="compare"><thead><tr>{th}</tr></thead><tbody>{"".join(body_html)}</tbody></table>'


def render_verdict(arg: str, body: str) -> str:
    label = arg.strip().lower() or "neutral"
    text = body.strip()
    return f'<div class="verdict {label}">{_esc(text)}</div>'


def render_chart(body: str, _counter=[0]) -> str:
    """Inline SVG line chart. Each line is one row:
        Label | v1,v2,v3,v4,...     (default — uses sequential x)
        Label | $123.45 -1.2%       (optional header line for KPI strip)
    Multiple series supported; first series gets primary color, others get muted.
    Optional first line "@title Some title" sets the chart title.
    Optional first line "@xlabels 6/1,6/2,6/3,..." sets x-axis labels.
    """
    _counter[0] += 1
    chart_id = f"chart{_counter[0]}"

    title = None
    x_labels: list[str] = []
    series: list[tuple[str, list[float], str | None]] = []  # name, values, note
    palette = ["#58a6ff", "#3fb950", "#d29922", "#f85149", "#a371f7", "#79c0ff", "#56d364"]

    for raw in body.strip().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("@title"):
            title = line[len("@title"):].strip()
            continue
        if line.startswith("@xlabels"):
            x_labels = [s.strip() for s in line[len("@xlabels"):].strip().split(",")]
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 2:
            continue
        name = parts[0]
        # parts[1] is comma-separated values; parts[2:] is optional note
        try:
            vals = [float(v.strip().replace("$", "").replace(",", "").replace("%", "")) for v in parts[1].split(",") if v.strip()]
        except ValueError:
            continue
        note = parts[2] if len(parts) >= 3 else None
        series.append((name, vals, note))

    if not series:
        return ""

    # SVG dimensions
    W, H = 720, 220
    PAD_L, PAD_R, PAD_T, PAD_B = 56, 16, 28, 26
    plot_w = W - PAD_L - PAD_R
    plot_h = H - PAD_T - PAD_B

    # Determine global y range across all series
    all_vals = [v for _, vals, _ in series for v in vals]
    if not all_vals:
        return ""
    y_min, y_max = min(all_vals), max(all_vals)
    if y_min == y_max:
        y_min -= 1
        y_max += 1
    # Pad ~5%
    rng = y_max - y_min
    y_min -= rng * 0.08
    y_max += rng * 0.08

    n = max(len(vals) for _, vals, _ in series)

    def xpos(i: int) -> float:
        if n <= 1:
            return PAD_L + plot_w / 2
        return PAD_L + (i / (n - 1)) * plot_w

    def ypos(v: float) -> float:
        return PAD_T + plot_h - ((v - y_min) / (y_max - y_min)) * plot_h

    # Build SVG
    parts = [f'<svg class="chart-svg" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img">']

    # Background
    parts.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="var(--panel-2)" rx="6"/>')

    # Y gridlines + labels (4 ticks)
    for k in range(5):
        v = y_min + (y_max - y_min) * (k / 4)
        y = ypos(v)
        parts.append(f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W - PAD_R}" y2="{y:.1f}" stroke="var(--border)" stroke-width="0.5" stroke-dasharray="2,3" opacity="0.5"/>')
        label = f"{v:,.2f}" if abs(v) < 1000 else f"{v:,.0f}"
        parts.append(f'<text x="{PAD_L - 6}" y="{y + 3:.1f}" fill="var(--muted)" font-size="10" text-anchor="end" font-family="ui-monospace, monospace">{label}</text>')

    # X labels (sparse — first / mid / last)
    label_idxs = []
    if x_labels and len(x_labels) >= 2:
        label_idxs = [0, len(x_labels) // 2, len(x_labels) - 1]
    elif n >= 2:
        label_idxs = [0, n // 2, n - 1]
    for i in label_idxs:
        if i >= n:
            continue
        lbl = x_labels[i] if i < len(x_labels) else f"t{i}"
        parts.append(f'<text x="{xpos(i):.1f}" y="{H - 8}" fill="var(--muted)" font-size="10" text-anchor="middle" font-family="ui-monospace, monospace">{_esc(lbl)}</text>')

    # Series paths + last-value dot
    for idx, (name, vals, note) in enumerate(series):
        color = palette[idx % len(palette)]
        if not vals:
            continue
        d = []
        for i, v in enumerate(vals):
            cmd = "M" if i == 0 else "L"
            d.append(f"{cmd}{xpos(i):.1f},{ypos(v):.1f}")
        path = " ".join(d)
        parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
        # Last point dot
        lx, ly, lv = xpos(len(vals) - 1), ypos(vals[-1]), vals[-1]
        parts.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="3" fill="{color}"/>')

    # Legend (top-right)
    legend_x = PAD_L + 4
    legend_y = PAD_T - 12
    if title:
        parts.append(f'<text x="{legend_x}" y="{legend_y + 4}" fill="var(--fg)" font-size="12" font-weight="600">{_esc(title)}</text>')

    legend_pieces = []
    for idx, (name, vals, note) in enumerate(series):
        color = palette[idx % len(palette)]
        last = vals[-1] if vals else 0
        first = vals[0] if vals else 0
        pct = ((last - first) / first * 100) if first else 0
        pct_color = "var(--green)" if pct >= 0 else "var(--red)"
        sign = "+" if pct >= 0 else ""
        legend_pieces.append((name, color, last, pct, pct_color, sign, note))

    # Legend strip below chart
    leg_html = ['<div class="chart-legend">']
    for name, color, last, pct, pct_color, sign, note in legend_pieces:
        last_str = f"{last:,.2f}" if abs(last) < 1000 else f"{last:,.0f}"
        note_html = f'<span class="legend-note">· {_esc(note)}</span>' if note else ""
        leg_html.append(
            f'<span class="legend-item">'
            f'<span class="legend-swatch" style="background:{color}"></span>'
            f'<span class="legend-name">{_esc(name)}</span> '
            f'<span class="legend-last">{last_str}</span> '
            f'<span class="legend-pct" style="color:{pct_color}">{sign}{pct:.2f}%</span>'
            f'{note_html}'
            f'</span>'
        )
    leg_html.append("</div>")

    parts.append("</svg>")
    return '<div class="chart-block">' + "".join(parts) + "".join(leg_html) + "</div>"


CUSTOM_BLOCKS = {
    "kpi": render_kpi,
    "scenarios": render_scenarios,
    "meter": render_meter,
    "meters": render_meter,
    "timeline": render_timeline,
    "compare": render_compare,
    "chart": render_chart,
}

TAB_RE = re.compile(r"^---tab\s+(.+?)\s*$", re.MULTILINE)
TABS_OPEN_RE = re.compile(r"```tabs\s*\n(.*?)```", re.DOTALL)


def render_tabs(body: str, _counter=[0]) -> str:
    """Render a tabs block. Inside the body, sections are delimited by `---tab Title`
    lines that sit OUTSIDE any nested fenced block. ---tab lines inside a nested
    ```tabs ... ``` are left alone for the recursive expand to handle."""
    _counter[0] += 1
    group_id = f"tabs{_counter[0]}"

    fenced = _fenced_ranges(body)
    def in_fence(pos: int) -> bool:
        return any(s <= pos < e for s, e in fenced)

    # Collect top-level ---tab markers only
    markers = [(m.start(), m.end(), m.group(1).strip())
               for m in TAB_RE.finditer(body) if not in_fence(m.start())]
    if not markers:
        return ""
    pairs = []
    for i, (start, end, title) in enumerate(markers):
        body_start = end
        body_end = markers[i + 1][0] if i + 1 < len(markers) else len(body)
        pairs.append((title, body[body_start:body_end]))

    inputs_and_labels = []
    panels = []
    for idx, (title, content) in enumerate(pairs):
        tid = f"{group_id}-{idx}"
        checked = " checked" if idx == 0 else ""
        inputs_and_labels.append(
            f'<input class="tab-input" type="radio" name="{group_id}" id="{tid}"{checked}>'
            f'<label class="tab-label" for="{tid}">{html.escape(title)}</label>'
        )
        # Recursively expand custom blocks inside the panel content, then convert to HTML
        expanded, panel_placeholders = expand_custom_blocks(content.strip())
        panel_body = markdown.markdown(
            expanded,
            extensions=["tables", "fenced_code", "sane_lists"],
            output_format="html5",
        )
        for k, v in panel_placeholders.items():
            panel_body = panel_body.replace(f"<p>{k}</p>", v).replace(k, v)
        panels.append(f'<div class="tab-panel" data-tab-for="{tid}">{panel_body}</div>')

    # Generate per-tab CSS — inputs are direct children of .tabs-group along with panels,
    # so the general-sibling selector `~` from the input down to its panel works.
    css_rules = "".join(
        f'#{group_id}-{i}:checked ~ [data-tab-for="{group_id}-{i}"] {{ display: block; }}'
        for i in range(len(pairs))
    )

    # Inputs first (so they precede panels in DOM), labels grouped in .tabs strip, then panels.
    inputs_html = "".join(
        f'<input class="tab-input" type="radio" name="{group_id}" id="{group_id}-{i}"{" checked" if i == 0 else ""}>'
        for i in range(len(pairs))
    )
    labels_html = "".join(
        f'<label class="tab-label" for="{group_id}-{i}">{html.escape(title)}</label>'
        for i, (title, _) in enumerate(pairs)
    )

    return (
        f'<div class="tabs-group">'
        f'<style>{css_rules}</style>'
        f'{inputs_html}'
        f'<div class="tabs">{labels_html}</div>'
        f'{"".join(panels)}</div>'
    )


def _extract_tabs_block(md_text: str) -> tuple[str, str | None, int, int]:
    """Find a top-level ```tabs ... ``` block, allowing nested ``` fences inside.

    Returns (lang, body, start, end) for the first tabs block, or ("", None, -1, -1).
    A 'tabs' block ends only at a closing ``` whose count of preceding open fences
    equals the count of preceding close fences after the opener.
    """
    open_re = re.compile(r"^```tabs[^\n]*\n", re.MULTILINE)
    m = open_re.search(md_text)
    if not m:
        return "", None, -1, -1
    body_start = m.end()
    pos = body_start
    depth = 1
    while pos < len(md_text):
        nxt = md_text.find("```", pos)
        if nxt == -1:
            return "", None, -1, -1
        # Determine if this is an opener (has a language tag after) or a closer
        line_end = md_text.find("\n", nxt)
        if line_end == -1:
            line_end = len(md_text)
        after_fence = md_text[nxt + 3:line_end].strip()
        if after_fence:  # has a tag → opener
            depth += 1
            pos = line_end + 1
        else:  # no tag → closer
            depth -= 1
            if depth == 0:
                return "tabs", md_text[body_start:nxt], m.start(), line_end + 1
            pos = line_end + 1
    return "", None, -1, -1


def expand_custom_blocks(md_text: str) -> str:
    """Replace custom fenced blocks with raw HTML before markdown parsing."""
    placeholders: dict[str, str] = {}

    # First pass: pull out any top-level `tabs` blocks (which may contain nested fences)
    while True:
        lang, body, start, end = _extract_tabs_block(md_text)
        if body is None:
            break
        html_block = render_tabs(body)
        key = f"\n\nCUSTOM_BLOCK_TABS_{len(placeholders)}_PLACEHOLDER\n\n"
        placeholders[key.strip()] = html_block
        md_text = md_text[:start] + key + md_text[end:]

    # Second pass: simple single-line custom blocks (kpi/scenarios/meter/callout/verdict/timeline/compare)
    def repl(m: re.Match[str]) -> str:
        lang = m.group(1).lower()
        arg = m.group(2).strip()
        body = m.group(3)
        if lang == "callout":
            html_block = render_callout(arg, body)
        elif lang == "verdict":
            html_block = render_verdict(arg, body)
        elif lang == "tabs":
            # Should already be handled, but fall through safely
            html_block = render_tabs(body)
        elif lang in CUSTOM_BLOCKS:
            html_block = CUSTOM_BLOCKS[lang](body)
        else:
            return m.group(0)
        key = f"\n\nCUSTOM_BLOCK_{len(placeholders)}_PLACEHOLDER\n\n"
        placeholders[key.strip()] = html_block
        return key

    md_text = FENCE_RE.sub(repl, md_text)
    return md_text, placeholders


# Auto-tabs: turn the H2 sections of a single-H1 document into a tabs block.
# Skip when the doc already contains an explicit ```tabs ... ``` block.
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)


def _fenced_ranges(md_text: str) -> list[tuple[int, int]]:
    """Return [start, end) char ranges of the OUTERMOST fenced code blocks.

    Handles nested fences: ```tabs may contain ```kpi or ```callout blocks. A
    fence with a language tag opens; a bare ``` closes. We only record the
    outermost open→close pair so nested-content checks treat the whole thing
    as one fenced range.
    """
    ranges = []
    pos = 0
    while pos < len(md_text):
        # find next opening fence (must have a language tag)
        m = re.search(r"^```(\w[^\n]*)$", md_text[pos:], re.MULTILINE)
        if not m:
            break
        start = pos + m.start()
        scan = pos + m.end()
        depth = 1
        while scan < len(md_text) and depth > 0:
            nxt = re.search(r"^```([^\n]*)$", md_text[scan:], re.MULTILINE)
            if not nxt:
                scan = len(md_text)
                break
            tag = nxt.group(1).strip()
            line_end = scan + nxt.end()
            if tag:
                depth += 1
            else:
                depth -= 1
            scan = line_end
            if depth == 0:
                ranges.append((start, scan))
                pos = scan
                break
        if depth > 0:
            break
    return ranges


def maybe_autowrap_h2_tabs(md_text: str) -> str:
    fenced = _fenced_ranges(md_text)
    def in_fence(pos: int) -> bool:
        return any(s <= pos < e for s, e in fenced)
    h2_matches = [m for m in H2_RE.finditer(md_text) if not in_fence(m.start())]
    if len(h2_matches) < 2:
        return md_text
    # Skip only if a top-level tabs block opens BEFORE the first H2 — i.e. the
    # whole body is already tabbed. Nested tabs inside H2 sections are fine.
    first_h2 = h2_matches[0].start()
    tabs_open = re.search(r"^```tabs\b", md_text, re.MULTILINE)
    if tabs_open and tabs_open.start() < first_h2:
        return md_text

    # Preamble = everything before the first top-level H2 (keeps H1 + intro callout/kpi)
    first = h2_matches[0]
    preamble = md_text[:first.start()].rstrip()

    sections = []
    for i, m in enumerate(h2_matches):
        title = m.group(1).strip()
        body_start = m.end()
        body_end = h2_matches[i + 1].start() if i + 1 < len(h2_matches) else len(md_text)
        body = md_text[body_start:body_end].strip()
        sections.append((title, body))

    parts = [preamble, "", "```tabs"]
    for title, body in sections:
        parts.append(f"---tab {title}")
        parts.append(body)
        parts.append("")
    parts.append("```")
    return "\n".join(parts)


def render_html(md_text: str, title: str) -> str:
    md_text = maybe_autowrap_h2_tabs(md_text)
    md_text, placeholders = expand_custom_blocks(md_text)
    body_html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "toc"],
        output_format="html5",
    )
    for key, block in placeholders.items():
        body_html = body_html.replace(f"<p>{key}</p>", block)
        body_html = body_html.replace(key, block)
    body_html = colorize_percentages(body_html)
    rendered_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="meta">📊 Stock workspace · rendered {rendered_at}</div>
{body_html}
</body>
</html>
"""


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9_-]+", "-", name).strip("-").lower()
    return s[:80] or "report"


def output_path(input_path: Path | None, title: str) -> Path:
    base = Path(__file__).resolve().parent.parent / "site" / "reports"
    base.mkdir(parents=True, exist_ok=True)
    if input_path is not None:
        rel = input_path
        try:
            rel = input_path.relative_to(Path(__file__).resolve().parent.parent)
        except ValueError:
            pass
        slug = slugify("-".join(rel.parts))
    else:
        slug = slugify(title)
    return base / f"{slug}.html"


def open_in_browser(path: Path) -> None:
    if sys.platform == "darwin":
        subprocess.run(["open", str(path)], check=False)
    else:
        webbrowser.open(path.as_uri())


def _tab_title_from_filename(stem: str, date: str) -> str:
    """`morning-2026-06-23` → `Morning`; `attribution-2026-06-23` → `Attribution`;
    `attribution-dram-mu-2026-06-23` → `Attribution Dram Mu`."""
    s = stem.replace(f"-{date}", "").replace(date, "").strip("-")
    return " ".join(p.capitalize() for p in s.split("-") if p) or "Report"


def _tab_order_key(stem: str) -> tuple[int, str]:
    """Sort tabs so the day reads chronologically: morning first, then per-stock,
    then attribution, then anything else."""
    s = stem.lower()
    if s.startswith("morning"):
        return (0, s)
    if "attribution" in s:
        return (2, s)
    if "watch" in s or "policy" in s:
        return (1, s)
    return (3, s)


def discover_session_files(date: str) -> list[Path]:
    base = Path(__file__).resolve().parent.parent / "dashboard"
    candidates = [
        p for p in base.glob(f"*-{date}.md") if p.is_file()
    ] + [
        p for p in base.glob(f"*{date}*.md") if p.is_file() and f"-{date}" not in p.name
    ]
    # de-dup, sort
    seen = set()
    unique = []
    for p in candidates:
        if p.resolve() in seen:
            continue
        seen.add(p.resolve())
        unique.append(p)
    unique.sort(key=lambda p: _tab_order_key(p.stem))
    return unique


def build_session_markdown(date: str, files: list[Path]) -> str:
    """Wrap the day's markdown files in a ```tabs ... ``` block."""
    if not files:
        return f"# Session {date}\n\nNo reports found for `{date}`.\n"
    lines = [f"# Session — {date}", "", "```tabs"]
    for p in files:
        title = _tab_title_from_filename(p.stem, date)
        body = p.read_text().strip()
        # Strip a leading H1 — the tab label already shows the title
        body = re.sub(r"^#\s+[^\n]+\n+", "", body, count=1)
        lines.append(f"---tab {title}")
        lines.append(body)
        lines.append("")
    lines.append("```")
    return "\n".join(lines)


def session_output_path(date: str) -> Path:
    base = Path(__file__).resolve().parent.parent / "site" / "reports"
    base.mkdir(parents=True, exist_ok=True)
    return base / f"session-{date}.html"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown to a visual HTML report")
    parser.add_argument("input", nargs="?", help="Path to markdown file, or '-' for stdin (omit when using --session alone)")
    parser.add_argument("--title", default=None, help="Page title")
    parser.add_argument("--no-open", action="store_true", help="Render only; do not open browser")
    parser.add_argument(
        "--session",
        metavar="YYYY-MM-DD",
        default=None,
        help="Render all dashboard/*-DATE.md files into one tabbed page. "
             "If a positional input is given too, that file is included in the bundle "
             "(useful from skills: render today's new report and refresh the session page).",
    )
    args = parser.parse_args()

    # Session mode: bundle the day's reports into one tabbed HTML
    if args.session:
        date = args.session
        files = discover_session_files(date)
        # If a positional input was provided, ensure it's in the bundle (helps skills
        # that just wrote a new file and want it to appear immediately)
        if args.input and args.input != "-":
            extra = Path(args.input).resolve()
            if extra.exists() and extra not in {p.resolve() for p in files}:
                files.append(extra)
                files.sort(key=lambda p: _tab_order_key(p.stem))
        if not files:
            print(f"error: no dashboard/*-{date}.md files found", file=sys.stderr)
            return 1
        md_text = build_session_markdown(date, files)
        title = args.title or f"Session {date}"
        out = session_output_path(date)
        out.write_text(render_html(md_text, title))
        print(out)
        if not args.no_open:
            open_in_browser(out)
        return 0

    if not args.input:
        parser.error("input is required when --session is not used")

    if args.input == "-":
        md_text = sys.stdin.read()
        in_path = None
        title = args.title or "Report"
    else:
        in_path = Path(args.input).resolve()
        if not in_path.exists():
            print(f"error: {in_path} not found", file=sys.stderr)
            return 1
        md_text = in_path.read_text()
        title = args.title or in_path.stem.replace("-", " ").replace("_", " ").title()

    out = output_path(in_path, title)
    out.write_text(render_html(md_text, title))
    print(out)
    if not args.no_open:
        open_in_browser(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
