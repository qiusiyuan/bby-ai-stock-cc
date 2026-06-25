#!/usr/bin/env bash
# Publish today's (or a specific date's) report to GitHub Pages.
#
# Usage:
#   scripts/publish.sh                   # publish today's dashboard
#   scripts/publish.sh 2026-06-25        # publish a specific date
#   scripts/publish.sh --no-push         # render + commit but don't push
#   scripts/publish.sh 2026-06-25 --no-push
#
# What it does:
#   1. Renders dashboard/{date}.md → site/reports/dashboard-{date}-md.html
#   2. Rebuilds site/index.html with the latest reports list
#   3. git add site/ dashboard/{date}.md (+ any other clean changes)
#   4. git commit -m "publish {date}"
#   5. git push (unless --no-push)
#
# Live URL: https://qiusiyuan.github.io/bby-ai-stock-cc/
set -euo pipefail

# cd to repo root regardless of where this script is invoked from
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

DATE=""
PUSH=true
for arg in "$@"; do
  case "$arg" in
    --no-push) PUSH=false ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# //;s/^#//'
      exit 0 ;;
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9])
      DATE="$arg" ;;
    *)
      echo "error: unknown argument '$arg'" >&2
      exit 1 ;;
  esac
done

if [[ -z "$DATE" ]]; then
  DATE="$(date +%Y-%m-%d)"
fi

DASHBOARD_MD="dashboard/${DATE}.md"
if [[ ! -f "$DASHBOARD_MD" ]]; then
  echo "error: $DASHBOARD_MD not found — generate the report first" >&2
  exit 1
fi

echo "→ rendering $DASHBOARD_MD"
uv run --project scripts scripts/render.py "$DASHBOARD_MD" --title "$DATE" --no-open

echo "→ rebuilding site/index.html"
uv run --project scripts scripts/build_index.py

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "error: not a git repo. Run scripts/git_init.sh first." >&2
  exit 1
fi

echo "→ staging changes"
git add site/ "$DASHBOARD_MD" 2>/dev/null || true
# Also pick up any other clean changes (skill edits, thesis updates, attributions)
git add -A

if git diff --cached --quiet; then
  echo "→ nothing to commit"
  exit 0
fi

echo "→ committing"
git commit -m "publish ${DATE}"

if $PUSH; then
  echo "→ pushing to origin"
  git push
  echo ""
  echo "✓ published. Live URL: https://qiusiyuan.github.io/bby-ai-stock-cc/"
  echo "  (Pages rebuild typically takes 30–90 seconds)"
else
  echo "→ skipped push (--no-push)"
fi
