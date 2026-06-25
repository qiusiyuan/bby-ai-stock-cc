"""Atomically record an attribution to both the per-stock MD log and the JSONL index.

CLI:
  echo '{"date":"2026-06-18", "ticker":"DRAM", ...}' | uv run scripts/record_attribution.py
  uv run scripts/record_attribution.py --file path/to/attribution.json

The input is one JSON object matching the schema in attributions/README.md.

Writes:
  - Appends a markdown entry to stocks/{TICKER}/attributions.md (creates if missing)
  - Appends one JSON line to attributions/index.jsonl (creates if missing)

Both writes happen in one process so they can't drift. Re-recording the same (date, ticker)
overwrites the prior MD entry for that day and rewrites the JSONL line in place; the index
is treated as keyed by (date, ticker).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "attributions" / "index.jsonl"

REQUIRED_FIELDS = {"date", "ticker", "direction", "magnitude", "tags", "confidence", "primary_cause"}


def _direction_emoji(direction: str) -> str:
    return "▲" if direction == "up" else "▼" if direction == "down" else "●"


def _format_md_entry(rec: dict[str, Any]) -> str:
    date = rec["date"]
    ticker = rec["ticker"]
    pct_1d = rec.get("change_pct_1d")
    pct_str = f"{pct_1d:+.2f}%" if isinstance(pct_1d, (int, float)) else "n/a"
    direction = rec.get("direction", "")
    magnitude = rec.get("magnitude", "")
    tags = rec.get("tags", [])
    tag_str = ", ".join(f"`{t}`" for t in tags) if tags else "—"
    confidence = rec.get("confidence", "")
    primary_cause = rec.get("primary_cause", "")
    sources = rec.get("sources", [])
    sources_md = "\n".join(_format_source(s) for s in sources) or "- (none)"
    cross = rec.get("cross_assets", {}) or {}
    cross_parts = []
    for k, v in cross.items():
        if v is None:
            continue
        if isinstance(v, (int, float)) and abs(v) < 100:
            cross_parts.append(f"{k.upper().replace('_PCT_1D','').replace('_',' ')} {v:+.2f}%" if "pct" in k else f"{k.upper().replace('_',' ')} {v}")
        else:
            cross_parts.append(f"{k.upper().replace('_',' ')} {v}")
    cross_str = " · ".join(cross_parts) if cross_parts else "n/a"
    agent_read = rec.get("agent_read", "")
    snapshot_link = rec.get("snapshot_path")

    arrow = _direction_emoji(direction)
    snap_md = f" · [Snapshot]({Path(snapshot_link).relative_to('stocks/' + ticker)})" if snapshot_link and Path(snapshot_link).is_relative_to(f"stocks/{ticker}") else ""
    if snapshot_link:
        try:
            rel = Path(snapshot_link)
            if rel.parts[:2] == ("stocks", ticker):
                snap_md = f" · [Snapshot]({Path(*rel.parts[2:]).as_posix()})"
            else:
                snap_md = f" · Snapshot at `{snapshot_link}`"
        except Exception:
            snap_md = ""

    return f"""\
### {date} · {pct_str} day · {arrow} {magnitude}
**Tags:** {tag_str}
**Confidence:** {confidence}

**Primary cause.** {primary_cause}

**Sources.**
{sources_md}

**Cross-assets.** {cross_str}

**Agent read.** {agent_read}
{snap_md}

---
"""


def _format_source(s: dict[str, Any]) -> str:
    kind = s.get("type", "headline")
    if kind == "headline":
        title = s.get("title", "")
        publisher = s.get("publisher", "")
        url = s.get("url", "")
        if url:
            return f"- {publisher}: [{title}]({url})"
        return f"- {publisher}: {title}"
    if kind == "corroboration":
        return f"- _Corroboration:_ {s.get('note', '')}"
    if kind == "data":
        return f"- _Data:_ {s.get('note', '')} ({s.get('source','')})"
    if kind == "quote":
        return f'- _Quote:_ "{s.get("text","")}" — {s.get("attribution","")}'
    return f"- {json.dumps(s)}"


def _ensure_md_log(ticker: str) -> Path:
    log_path = ROOT / "stocks" / ticker / "attributions.md"
    if not log_path.parent.exists():
        log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        log_path.write_text(
            f"# {ticker} attributions\n\n"
            f"Append-only log of meaningful price moves with cited causes. "
            f"Companion to the JSONL index at `../../attributions/index.jsonl`.\n\n"
            f"---\n\n"
        )
    return log_path


def _append_md_entry(log_path: Path, entry_md: str, date: str) -> None:
    """Append entry. If an entry for this date exists, replace it instead of duplicating."""
    text = log_path.read_text()
    marker = f"### {date} ·"
    if marker in text:
        # Find the existing entry block (from marker to next marker or EOF)
        start = text.index(marker)
        # Find the closing `---\n` after start
        rest = text[start:]
        # Block ends at the FIRST `\n---\n` followed by either EOF or another `### `
        block_end_rel = rest.find("\n---\n")
        if block_end_rel == -1:
            end = len(text)
        else:
            end = start + block_end_rel + len("\n---\n")
        text = text[:start] + entry_md + text[end:]
        log_path.write_text(text)
    else:
        # Insert at top below the header (after the first '---\n\n')
        header_end = text.find("---\n\n")
        if header_end == -1:
            log_path.write_text(text + entry_md)
        else:
            insert_at = header_end + len("---\n\n")
            log_path.write_text(text[:insert_at] + entry_md + text[insert_at:])


def _upsert_jsonl(rec: dict[str, Any]) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not INDEX_PATH.exists():
        INDEX_PATH.write_text("")
    lines = INDEX_PATH.read_text().splitlines()
    key = (rec["date"], rec["ticker"])
    new_lines: list[str] = []
    replaced = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            existing = json.loads(line)
        except Exception:
            new_lines.append(line)
            continue
        if (existing.get("date"), existing.get("ticker")) == key:
            new_lines.append(json.dumps(rec, default=str))
            replaced = True
        else:
            new_lines.append(line)
    if not replaced:
        new_lines.append(json.dumps(rec, default=str))
    INDEX_PATH.write_text("\n".join(new_lines) + "\n")


def record(rec: dict[str, Any]) -> dict[str, str]:
    missing = REQUIRED_FIELDS - set(rec.keys())
    if missing:
        raise ValueError(f"missing required fields: {sorted(missing)}")
    rec.setdefault("recorded_at", datetime.utcnow().isoformat(timespec="seconds") + "Z")
    log_path = _ensure_md_log(rec["ticker"])
    md_entry = _format_md_entry(rec)
    _append_md_entry(log_path, md_entry, rec["date"])
    _upsert_jsonl(rec)
    return {
        "log_path": str(log_path),
        "index_path": str(INDEX_PATH),
        "key": f"{rec['date']}/{rec['ticker']}",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Record an attribution")
    parser.add_argument("--file", help="Path to JSON file (default: stdin)")
    args = parser.parse_args()
    raw = Path(args.file).read_text() if args.file else sys.stdin.read()
    rec = json.loads(raw)
    result = record(rec)
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
