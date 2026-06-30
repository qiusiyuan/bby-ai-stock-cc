"""Build site/index.html — the GitHub Pages homepage that lists every published report.

Usage:
  uv run --project scripts scripts/build_index.py

Behavior:
  - Scans site/reports/dashboard-YYYY-MM-DD-md.html (per-day main reports).
  - Scans site/reports/stocks-{ticker}-research-YYYY-MM-DD-{slug}-md.html (per-stock
    deep dives) and lists them in a separate section.
  - Newest 5 daily dates rendered as prominent cards; remainder folded into archive.
  - Also surfaces any session-YYYY-MM-DD.html bundles if present.
  - Writes site/index.html. Idempotent.

The page is intentionally simple and styled inline so it has no build dependencies
beyond the standard library.
"""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
REPORTS = SITE / "reports"

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
# Main daily report file produced by render.py for dashboard/{date}.md
DASHBOARD_RE = re.compile(r"^dashboard-(\d{4}-\d{2}-\d{2})-md\.html$")
SESSION_RE = re.compile(r"^session-(\d{4}-\d{2}-\d{2})\.html$")
# Per-stock deep-dive file: stocks-{ticker}-research-{YYYY-MM-DD}-{slug}-md.html
DEEP_DIVE_RE = re.compile(
    r"^stocks-(?P<ticker>[a-z0-9]+)-research-(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.+)-md\.html$"
)

LATEST_COUNT = 5

CSS = """
:root {
  --bg: #0d1117; --panel: #161b22; --panel-2: #1c2128; --fg: #e6edf3;
  --muted: #8b949e; --accent: #58a6ff; --border: #30363d;
  --green: #3fb950; --red: #f85149; --amber: #d29922;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #ffffff; --panel: #f6f8fa; --panel-2: #eaeef2; --fg: #1f2328;
    --muted: #59636e; --accent: #0969da; --border: #d0d7de;
    --green: #1a7f37; --red: #cf222e; --amber: #9a6700;
  }
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  font-size: 15px;
  line-height: 1.6;
  color: var(--fg);
  background: var(--bg);
  padding: 40px 24px 64px;
  max-width: 880px;
  margin: 0 auto;
}
header { border-bottom: 1px solid var(--border); padding-bottom: 24px; margin-bottom: 32px; }
h1 { font-size: 1.8em; margin: 0 0 8px; }
.tagline { color: var(--muted); font-size: 0.95em; margin: 0; }
.disclaimer {
  background: var(--panel);
  border-left: 3px solid var(--amber);
  padding: 10px 14px;
  margin: 16px 0 0;
  border-radius: 0 4px 4px 0;
  color: var(--muted);
  font-size: 0.86em;
}
section { margin: 28px 0; }
h2 { font-size: 1.15em; color: var(--muted); text-transform: uppercase;
     letter-spacing: 0.05em; margin: 32px 0 12px; }
.cards { display: grid; gap: 12px; }
.card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px 18px;
  transition: border-color 0.15s, transform 0.15s;
}
.card:hover { border-color: var(--accent); transform: translateY(-1px); }
.card a { color: var(--fg); text-decoration: none; display: block; }
.card .date { font-size: 0.92em; color: var(--accent); font-family: ui-monospace, monospace;
              font-weight: 600; margin-bottom: 4px; }
.card .weekday { color: var(--muted); margin-left: 6px; font-weight: 400; }
.card .links { margin-top: 8px; display: flex; gap: 14px; font-size: 0.88em; }
.card .links a { color: var(--accent); text-decoration: none; }
.card .links a:hover { text-decoration: underline; }
.archive {
  background: var(--panel-2);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 8px 18px;
}
.archive summary { cursor: pointer; padding: 8px 0; color: var(--muted);
                   font-weight: 600; user-select: none; }
.archive summary:hover { color: var(--fg); }
.archive ul { list-style: none; padding: 0 0 12px; margin: 0; }
.archive li { padding: 6px 0; border-top: 1px solid var(--border); }
.archive li:first-child { border-top: none; }
.archive a { color: var(--accent); text-decoration: none; font-family: ui-monospace, monospace;
             font-size: 0.92em; }
.archive a:hover { text-decoration: underline; }
.empty { color: var(--muted); font-style: italic; }

/* Tabs */
.tabs { display: flex; gap: 4px; border-bottom: 1px solid var(--border); margin-bottom: 16px; }
.tab {
  background: none; border: none; color: var(--muted);
  padding: 10px 16px; cursor: pointer; font: inherit; font-weight: 600;
  border-bottom: 2px solid transparent; margin-bottom: -1px;
  transition: color 0.15s, border-color 0.15s;
}
.tab:hover { color: var(--fg); }
.tab.active { color: var(--accent); border-bottom-color: var(--accent); }
.tab-panel { display: none; }
.tab-panel.active { display: block; }

/* Deep dive list */
.dd-list { list-style: none; padding: 0; margin: 0; }
.dd-item { border-bottom: 1px solid var(--border); }
.dd-item:last-child { border-bottom: none; }
.dd-item a {
  display: grid;
  grid-template-columns: 110px 70px 1fr;
  gap: 12px;
  align-items: baseline;
  padding: 10px 6px;
  text-decoration: none;
  color: var(--fg);
  transition: background 0.1s;
}
.dd-item a:hover { background: var(--panel); }
.dd-date { color: var(--accent); font-family: ui-monospace, monospace;
           font-size: 0.9em; font-weight: 600; }
.dd-ticker { color: var(--fg); font-weight: 700;
             font-family: ui-monospace, monospace; font-size: 0.92em; }
.dd-title { color: var(--muted); font-size: 0.93em; }
.dd-item a:hover .dd-title { color: var(--fg); }
footer { margin-top: 64px; padding-top: 20px; border-top: 1px solid var(--border);
         color: var(--muted); font-size: 0.84em; }
footer a { color: var(--accent); text-decoration: none; }
"""

INTRO = """
A personal investment journal — daily reports on equities, macro and policy signals.
Generated by a Claude Code workspace; the markdown sources and skills live in this repo.
"""

DISCLAIMER = (
    "Personal notes only. Nothing here is financial advice or a recommendation to buy or sell "
    "any security. Numbers are sourced best-effort from public feeds; do your own research."
)


def discover_reports() -> tuple[
    list[tuple[str, Path]],
    dict[str, Path],
    list[tuple[str, str, str, Path]],
]:
    """Return (sorted_daily_reports, session_bundles_by_date, deep_dives).
    sorted_daily_reports: list of (date, path) sorted newest first.
    deep_dives: list of (date, ticker, slug, path) sorted newest first.
    """
    if not REPORTS.exists():
        return [], {}, []
    daily: list[tuple[str, Path]] = []
    sessions: dict[str, Path] = {}
    deep_dives: list[tuple[str, str, str, Path]] = []
    for p in REPORTS.iterdir():
        if not p.is_file() or p.suffix != ".html":
            continue
        m = DASHBOARD_RE.match(p.name)
        if m:
            daily.append((m.group(1), p))
            continue
        m = SESSION_RE.match(p.name)
        if m:
            sessions[m.group(1)] = p
            continue
        m = DEEP_DIVE_RE.match(p.name)
        if m:
            deep_dives.append(
                (m.group("date"), m.group("ticker").upper(), m.group("slug"), p)
            )
            continue
    daily.sort(key=lambda x: x[0], reverse=True)
    deep_dives.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return daily, sessions, deep_dives


def humanize_slug(slug: str) -> str:
    return slug.replace("-", " ").strip().capitalize()


def format_deep_dive_item(date: str, ticker: str, slug: str, path: Path) -> str:
    rel = path.relative_to(SITE).as_posix()
    title = humanize_slug(slug)
    return (
        f'<li class="dd-item">'
        f'<a href="{rel}">'
        f'<span class="dd-date">{date}</span>'
        f'<span class="dd-ticker">{ticker}</span>'
        f'<span class="dd-title">{title}</span>'
        f'</a></li>'
    )


def format_card(date: str, path: Path, session_path: Path | None) -> str:
    try:
        dt = datetime.strptime(date, "%Y-%m-%d")
        weekday = dt.strftime("%A")
    except ValueError:
        weekday = ""
    rel = path.relative_to(SITE).as_posix()
    links = [f'<a href="{rel}">Open report →</a>']
    if session_path is not None:
        rel_session = session_path.relative_to(SITE).as_posix()
        links.append(f'<a href="{rel_session}">Full session bundle</a>')
    links_html = " · ".join(links)
    return (
        f'<div class="card">'
        f'<div class="date">{date}<span class="weekday">{weekday}</span></div>'
        f'<div class="links">{links_html}</div>'
        f'</div>'
    )


def format_archive_item(date: str, path: Path) -> str:
    rel = path.relative_to(SITE).as_posix()
    return f'<li><a href="{rel}">{date}</a></li>'


def build() -> Path:
    daily, sessions, deep_dives = discover_reports()
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    # ----- Daily reports panel -----
    if not daily:
        daily_html = '<p class="empty">No daily reports yet. Run a report and re-publish.</p>'
    else:
        latest = daily[:LATEST_COUNT]
        archive = daily[LATEST_COUNT:]
        latest_html = "".join(format_card(d, p, sessions.get(d)) for d, p in latest)
        daily_html = (
            f'<section><h2>Latest reports</h2>'
            f'<div class="cards">{latest_html}</div></section>'
        )
        if archive:
            archive_html = "".join(format_archive_item(d, p) for d, p in archive)
            daily_html += (
                f'<section><h2>Archive</h2>'
                f'<details class="archive"><summary>{len(archive)} earlier report(s)</summary>'
                f'<ul>{archive_html}</ul></details></section>'
            )

    # ----- Deep dives panel -----
    if not deep_dives:
        dd_html = '<p class="empty">No deep dives yet.</p>'
    else:
        dd_items = "".join(
            format_deep_dive_item(d, t, s, p) for d, t, s, p in deep_dives
        )
        dd_html = (
            f'<section><h2>Per-stock deep dives ({len(deep_dives)})</h2>'
            f'<ul class="dd-list">{dd_items}</ul></section>'
        )

    tabs_html = (
        '<div class="tabs">'
        '<button class="tab active" data-target="daily">Daily reports</button>'
        f'<button class="tab" data-target="deep-dives">Deep dives ({len(deep_dives)})</button>'
        '</div>'
        f'<div id="daily" class="tab-panel active">{daily_html}</div>'
        f'<div id="deep-dives" class="tab-panel">{dd_html}</div>'
    )
    body = tabs_html

    html = f"""<!doctype html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2KN3NVQZ7P"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-2KN3NVQZ7P');
</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>bby's stock notes</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>bby's stock notes</h1>
  <p class="tagline">{INTRO.strip()}</p>
  <div class="disclaimer">⚠️ {DISCLAIMER}</div>
</header>
{body}
<footer>
  Generated {generated_at} · <a href="https://github.com/qiusiyuan/bby-ai-stock-cc">source on GitHub</a>
</footer>
<script>
(function() {{
  var tabs = document.querySelectorAll('.tab');
  var panels = document.querySelectorAll('.tab-panel');
  function activate(target) {{
    tabs.forEach(function(t) {{
      t.classList.toggle('active', t.getAttribute('data-target') === target);
    }});
    panels.forEach(function(p) {{
      p.classList.toggle('active', p.id === target);
    }});
    if (history.replaceState) {{
      history.replaceState(null, '', '#' + target);
    }}
  }}
  tabs.forEach(function(t) {{
    t.addEventListener('click', function() {{
      activate(t.getAttribute('data-target'));
    }});
  }});
  // Restore from hash on page load
  var hash = (window.location.hash || '').replace('#', '');
  if (hash && document.getElementById(hash)) {{
    activate(hash);
  }}
}})();
</script>
</body>
</html>
"""
    SITE.mkdir(parents=True, exist_ok=True)
    out = SITE / "index.html"
    out.write_text(html)
    return out


if __name__ == "__main__":
    out = build()
    print(out)
