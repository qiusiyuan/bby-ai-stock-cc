"""Query the attribution index. Used by the find-similar-moves skill.

CLI:
  uv run scripts/find_attributions.py --ticker DRAM
  uv run scripts/find_attributions.py --tag executive_comment --tag memory_pricing
  uv run scripts/find_attributions.py --ticker DRAM --tag earnings_print --magnitude major
  uv run scripts/find_attributions.py --since 2026-01-01 --confidence high
  uv run scripts/find_attributions.py --any-tag tech_breakthrough,production_milestone

Filter logic:
  - --ticker, --since, --until, --magnitude, --confidence, --direction: AND
  - --tag (repeatable): ALL tags must match (AND)
  - --any-tag X,Y,Z: ANY of these tags must match (OR)

Output: JSON array, one object per match, sorted newest-first.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "attributions" / "index.jsonl"


def _load() -> list[dict[str, Any]]:
    if not INDEX_PATH.exists():
        return []
    out = []
    for line in INDEX_PATH.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except Exception:
            continue
    return out


def _matches(rec: dict[str, Any], args) -> bool:
    if args.ticker and rec.get("ticker", "").upper() != args.ticker.upper():
        return False
    if args.since and rec.get("date", "") < args.since:
        return False
    if args.until and rec.get("date", "") > args.until:
        return False
    if args.magnitude and rec.get("magnitude") != args.magnitude:
        return False
    if args.confidence and rec.get("confidence") != args.confidence:
        return False
    if args.direction and rec.get("direction") != args.direction:
        return False

    rec_tags = set(rec.get("tags", []) or [])
    if args.tag:
        required = set(args.tag)
        if not required.issubset(rec_tags):
            return False
    if args.any_tag:
        any_required = set(args.any_tag.split(","))
        if not (any_required & rec_tags):
            return False
    if args.verdict:
        v = (rec.get("verdict") or {}).get("state")
        if v != args.verdict:
            return False
    if args.has_score_date:
        if not rec.get("score_date"):
            return False
    if args.score_date_due:
        from datetime import date as _d
        sd = rec.get("score_date")
        if not sd:
            return False
        try:
            if _d.fromisoformat(sd) > _d.fromisoformat(args.score_date_due):
                return False
        except Exception:
            return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Query attribution index")
    parser.add_argument("--ticker")
    parser.add_argument("--tag", action="append", default=[], help="Tag that MUST match (repeatable; AND semantics)")
    parser.add_argument("--any-tag", help="Comma-separated tags; ANY match passes (OR)")
    parser.add_argument("--magnitude", choices=["minor", "material", "major", "extreme"])
    parser.add_argument("--confidence", choices=["high", "medium", "low"])
    parser.add_argument("--direction", choices=["up", "down"])
    parser.add_argument("--since")
    parser.add_argument("--until")
    parser.add_argument("--verdict", choices=["pass", "fail", "n/a", "pending"], help="Filter by verdict state")
    parser.add_argument("--has-score-date", action="store_true", help="Only entries with a score_date set")
    parser.add_argument("--score-date-due", help="Only entries whose score_date is on or before this YYYY-MM-DD")
    parser.add_argument("--limit", type=int, default=50)
    args = parser.parse_args()

    records = _load()
    matches = [r for r in records if _matches(r, args)]
    matches.sort(key=lambda r: r.get("date", ""), reverse=True)
    matches = matches[: args.limit]
    json.dump(matches, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
