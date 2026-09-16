---
name: timeline
description: "Module 3 of the daily brief — 90-day catalyst calendar (90d is the DEFAULT; see Why 90). Use when the user wants to see upcoming events: 'timeline', 'what's coming up', '下次 catalyst', 'earnings calendar', 'next 90 days', 'upcoming'. Aggregates timeline.yaml + active-stock earnings + recorded prediction score_dates. Writes '## Timeline 90d' H2 to dashboard/{date}.md."
---

# /timeline

Module 3. The unified "what's next" calendar. This is the answer to "I want to know what to look at".

## When invoked solo

- "timeline" / "what's coming up" / "upcoming"
- "earnings calendar" / "下次 catalyst" / "next 90 days"
- AUTOMATICALLY as module 3 of [[report]]

## Steps

### 1. Build the merged timeline

```bash
uv run --project scripts scripts/build_timeline.py --md --days 90
# or for a renderer-friendly block:
uv run --project scripts scripts/build_timeline.py --block --days 90
```

Sources merged:
- `timeline.yaml` — hand-curated events (earnings, FOMC dates, lock-ups, policy windows)
- `attributions/index.jsonl` — prediction `score_date` entries (auto-injected)

Each event gets an urgency tier:
- 🔥 within 7 days
- ⚠ 8–14 days
- ▢ 15–30 days
- ▢ 31–45 days
- ▢ 46–90 days

### 2. Write H2 section

Replace any existing `## Timeline 90d` H2 in place. Structure:

```markdown
## Timeline 90d

```callout {info}
{N events in the next 90 days. {Y} are 🔥 within 7 days. The single densest day: {date + what collides there}.}
```

### 🔥 Within 7 days
{markdown bullets from build_timeline.py --md}

### ⚠ 8–14 days
{...}

### ▢ 15–30 days
{...}

### ▢ 31–45 days
{...}

### ▢ 46–90 days
{...}
```

OR use the visual `timeline` block if a more compact view fits:

```markdown
## Timeline 90d
```timeline
2026-06-24 🔥 | [MU] Q3 earnings AMC
2026-06-25 🔥 | [SPCX] Score prediction (likely fail)
2026-06-30 🔥 | [TSLA] Q2 deliveries
...
```
```

### 3. If user wants to add an event

If they say "remind me about X on Y", append to `timeline.yaml`:

```yaml
- { date: 2026-MM-DD, kind: catalyst, ticker: NVDA, note: "{description}" }
```

Don't auto-edit; ask first.

### 4. Don't render — orchestrator's job

## Why 90 (not 30) — the default, set 2026-09-16

**A 30-day window run mid-quarter structurally hides the entire next earnings season.** This is not a tuning preference; it is a defect that already produced a wrong report.

Concrete case that set this rule: on 2026-09-16 the timeline was run at `--days 35`, which truncated at 10/21. That hid **10/28 — Alphabet + Meta + Microsoft + GE Vernova earnings plus the next FOMC decision, all on one day.** The same report's single most actionable conclusion (AVGO's demand-side answer arrives free on 10/28 via its customers' capex guidance, six weeks before AVGO itself reports on 12/9) pointed at a date the timeline claimed did not exist.

Why 90 specifically:
- US large-cap earnings cluster in the last ~10 days of the month following a quarter end. From any mid-month vantage point, that cluster is 30–45 days out — i.e. **just past a 30d horizon**.
- 90 days covers a full quarter, so the calendar always contains at least one complete earnings season plus the next one's leading edge.
- Multi-event collision days (3+ events on one date) are the highest-information days and are usually 30+ days out. They cannot be found in a 30d window.

**Always surface collision days explicitly.** When 3+ events land on one date, give it its own 🎯 line and explain how the events interact — a stock's move that day is the *net* of several signals, so the price alone will not reveal causation. Also flag when a company's decisive data arrives via **someone else's** report (customer capex guides, supplier prints) earlier than its own.

## Hard rules

- **90 days is the default.** Only narrow it if the user explicitly asks for a short horizon. Never run 30d for a `/report` module.
- **Don't fabricate dates** — if unsure of an earnings date or policy deadline, mark it as "estimate" or "~" in the note
- **Future events only by default** — past prediction score_dates etc. are already in attributions index
- **The timeline.yaml is hand-maintained** — agent adds entries when user asks; agent does NOT auto-add things it "noticed" in news
- **Macro calendar is included** — CPI / NFP / FOMC / GDP are pre-filled
- **Sanity-check the count against `fetch.py`.** Every active stock has a `next_earnings` field. If the timeline shows materially fewer earnings rows than there are active stocks with a `next_earnings` inside the window, the window is too short or the merge broke — check before writing.

## What this gives you

Before this skill, the workspace knew about today + recent days. Now it knows about the next 90. This makes the brief module's "下个关键点" section actually quantitative (with specific dates) rather than vague.
