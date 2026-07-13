---
name: report
description: "One-stop orchestrator for the daily brief. Use when the user wants a comprehensive report: '今天的 report', 'today's report', 'today's move', 'daily report', 'morning report', '最近的消息', '今天大盘', 'what's going on', 'give me everything'. Pops a menu (preselects defaults), runs the chosen module skills in parallel where possible, composes their H2 sections into dashboard/{date}.md, renders to HTML. The single entry point for multi-module analysis."
---

# /report

The one-trigger orchestrator. User says one phrase, gets a comprehensive brief.

## When invoked

Phrasing the user might use:
- "today's report" / "今天的 report" / "daily report"
- "today's move" / "今天的 move"
- "morning report" (distinct from bare "morning" — see [[morning]])
- "give me everything" / "full brief"
- "what's going on" / "最近的消息" / "今天大盘"
- "the report"

## Modules (the menu)

The orchestrator always asks via AskUserQuestion, preselecting defaults (1-4) and adding context-aware deep-dive candidates.

| # | Skill | Output H2 in dashboard/{date}.md | Default | Notes |
|---|---|---|---|---|
| 1 | [[pulse]] | "Pulse & Macro" | ✓ | Big-picture: indices, VIX, rates, FX, oil, policy news |
| 2 | [[watchlist]] | "Watchlist & Movers" | ✓ | Per-stock grid + threshold-crossing flags |
| 3 | [[timeline]] | "Timeline 30d" | ✓ | Catalyst calendar: earnings, FOMC, lock-ups, predictions |
| 4 | [[cluster]] × N | "Focus: {cluster name}" each | ✓ | One H2 per `focus_cluster` defined in `groups.yaml`. Order: clusters appear in the order listed in yaml. |
| 5 | [[brief]] | "Brief" | ✓ | AI synthesis — reads 1-4 outputs and writes the cross-cluster narrative + verdicts |
| 6 | [[deep-dive]] | "Deep Dive: {TICKER}" | (auto-suggested) | Per-stock full analysis on user request. |
| 7 | [[compare]] | "Compare {A} vs {B}" | – | When user asks |
| 8 | **Earnings scorecard** | "Earnings scorecard: {TICKER}" | (auto-preselected on scoring_date) | When any active stock's `state.yaml::earnings_watchlist.scoring_date == today` AND `status: pending`. Reads the linked scorecard file, fetches the actual print numbers, fills in the Tier 1 / Tier 2 grid with actual-vs-bar, writes verdict to `thesis.md` Stands & Updates, flips `status` to `scored`. |

**Why cluster tabs**: the user has specific lenses they care about — TSLA, SpaceX, DRAM/HBM, AI capex, 能源. Each cluster lives in `groups.yaml::focus_clusters` and gets its own tab so the report's structure mirrors what the user actually tracks.

For "pressure test my view on X" requests: handle inline (read the relevant `stocks/{T}/thesis.md`, write an H2 like `## Pressure test: {topic}` with user-view + agent-counter + recorded prediction). No separate skill needed.

## Steps

### 1. Detect default scope from the phrasing

Match the trigger phrase to one of these patterns:

| Trigger | Default checked | Auto-suggest |
|---|---|---|
| "today's report" / "daily report" | 1+2+3+4 | today's movers as deep-dive candidates |
| "today's move" | 2+4 | today's movers as deep-dive candidates |
| "morning report" | 1+2+3+4 + score predictions | – |
| "最近的消息" / "what's going on" | 1+2 | recent attribution stories as deep-dive |
| "full brief" / "give me everything" | 1+2+3+4 (+5 for top mover) | – |

### 2. Pre-pull today's movers for menu context

Quick fetch of focus group (parallel `fetch.py` calls). Identify any tickers with `|change_pct_1d| >= 3%` or `|change_pct_5d| >= 10%`. Add each as an **optional menu item** like `"Deep dive: NVDA (-4.5% today)"`.

### 2b. Earnings-scorecard scan (MANDATORY pre-step)

Iterate every `stocks/*/state.yaml`. For each that has an `earnings_watchlist` block with `status: pending`:

- If `today == scoring_date` → **preselect** module 8 (Earnings scorecard) in the menu, with header `🎯 EARNINGS SCORECARD DUE: {TICKER} — score 「{thesis_claim}」`. This is non-optional unless the user actively unchecks it.
- If `today` is within ±7 days of `scoring_date` → add a chat-line reminder above the menu: `⏰ {TICKER} earnings scoring window opens in N days — scorecard at {path}`.

Surface this scan's findings *before* the menu renders so the user can see what's queued.

### 3. Show menu (every time — user's hard rule)

Use AskUserQuestion with **multiSelect: true**. Question: "今天跑哪些模块？" Options preselected via the table above. Include at most 4 options at top level. If more candidates (e.g. 5 deep-dive options), use a second multi-select question.

**Subagent / non-interactive fallback**: If AskUserQuestion is unavailable (running as a subagent, batch mode, etc.), **skip the menu and run the default modules** for the trigger phrase from step 1. Note in the chat reply: "(non-interactive mode — ran defaults)".

Example menu:
```
跑哪些模块？  (multi-select)
  [✓] 1. Pulse & Macro     (大盘 + 宏观 + 政策新闻)
  [✓] 2. Watchlist & Movers (持仓快照 + 异动)
  [✓] 3. Timeline 30d      (财报 / 政策窗口 / catalyst)
  [✓] 4. Brief 综合        (把以上串起来 + AI 概率判断)

可选 deep-dive: (multi-select)
  [ ] Deep dive: MU (-11% today)
  [ ] Deep dive: TSLA (-6% today)
  [ ] Deep dive: SPCX (5d -15%)
```

### 4. Run chosen modules — SEQUENTIALLY, one section at a time

**CRITICAL: Write each H2 section to the dashboard file ONE AT A TIME.** Do NOT attempt to write the entire report in a single Edit/Write call — this causes context-window timeouts on large reports. The correct pattern:

1. Create the file with `# Daily Report {date}` header
2. Write `## Pulse & Macro` section → Edit/append to file
3. Write `## Watchlist & Movers` section → Edit/append to file
4. Write `## Timeline 30d` section → Edit/append to file
5. Write each `## Focus: {cluster}` section → one Edit/append per cluster
6. Write `## Brief` section LAST → Edit/append to file
7. Write any Deep Dive sections → Edit/append to file

Between sections: fetch data as needed for the next section. This keeps each tool call small and prevents timeouts.

**Dependencies:**
- Modules 1, 2, 3 (pulse / watchlist / timeline) are independent — data can be fetched in parallel, but sections are WRITTEN sequentially
- Module 4 ([[cluster]] tabs) — one section per cluster, written one at a time
- Module 5 ([[brief]]) depends on 1+2+3+4 outputs — runs sequentially LAST
- Deep-dive / compare modules are appended after Brief

Each module skill writes its own H2 to `dashboard/{date}.md`. Idempotent: re-running replaces its H2 in place.

**Resulting tab order** in the dashboard (with default modules + clusters):
1. Pulse & Macro
2. Watchlist & Movers
3. Timeline 30d
4. Focus: TSLA
5. Focus: SpaceX
6. Focus: DRAM/HBM
7. Focus: AI capex
8. Focus: 能源
9. Focus: 电力/Grid
10. Brief
(Any user-requested Deep Dive / Compare tabs appended after Brief.)

### 5. Render and open

```bash
uv run --project scripts scripts/render.py dashboard/{date}.md --title "{date}"
```

The renderer auto-tabs the H2 sections. User sees one URL with N tabs.

### 6. Chat reply — 3-5 lines max

```
{date} report. {N} tabs生成. {headline of the day in one line}. Brief tab 是 AI 综合判断. Opened in browser.
```

Don't dump module outputs into chat — the dashboard is the report.

## Hard rules

- **Always show menu**. Don't infer "user wants everything" from the trigger; the menu is the control surface.
- **Write sections ONE AT A TIME.** Never write more than one H2 section in a single tool call. This is the #1 cause of timeouts. Fetch data → write one section → fetch more data → write next section.
- **Idempotent re-runs**: same module on same day = replace its H2, don't append.
- **Brief is last**. It reads 1+2+3 markdown to write the narrative; without them it's flying blind.
- **One file, one URL**. Never open multiple browser tabs.
- **Data fetching can be parallel** — batch `fetch.py` calls in one Bash command. But writing markdown is sequential.

## Skill linkage

- Each module skill ([[pulse]], [[watchlist]], [[timeline]], [[brief]], [[deep-dive]], etc.) is also callable solo.
- [[morning]] internally invokes `/report` with predictions-scoring pre-step.
- After running, [[deep-dive]] gets flagged for any movers — but only as a *suggestion*, not auto-run.
