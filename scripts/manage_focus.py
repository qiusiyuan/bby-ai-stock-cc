"""Add/remove tickers from the focus list in groups.yaml.

CLI:
  uv run --project scripts scripts/manage_focus.py list
  uv run --project scripts scripts/manage_focus.py add NVDA
  uv run --project scripts scripts/manage_focus.py remove IBM
  uv run --project scripts scripts/manage_focus.py set MU TSLA SPCX DRAM    # replace
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
GROUPS_PATH = ROOT / "groups.yaml"


def load() -> dict:
    return yaml.safe_load(GROUPS_PATH.read_text()) or {}


def save(data: dict) -> None:
    # Preserve the file's leading comments by reading raw text and replacing
    # only the focus block. For simplicity here, just dump — user can re-comment.
    GROUPS_PATH.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    a = sub.add_parser("add"); a.add_argument("ticker", nargs="+")
    r = sub.add_parser("remove"); r.add_argument("ticker", nargs="+")
    s = sub.add_parser("set"); s.add_argument("ticker", nargs="+")
    args = p.parse_args()

    data = load()
    focus = data.setdefault("focus", {"members": [], "description": "重点观察", "updated": ""})
    members = list(focus.get("members") or [])

    if args.cmd == "list":
        print("\n".join(members) if members else "(empty)")
        return 0

    changed = False
    if args.cmd == "add":
        for t in args.ticker:
            t = t.upper()
            if t not in members:
                members.append(t); changed = True
    elif args.cmd == "remove":
        for t in args.ticker:
            t = t.upper()
            if t in members:
                members.remove(t); changed = True
    elif args.cmd == "set":
        members = [t.upper() for t in args.ticker]
        changed = True

    if changed:
        focus["members"] = members
        focus["updated"] = date.today().isoformat()
        save(data)
        print(f"focus = {members}")
    else:
        print("no change")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
