---
name: timeline
description: "Module 3 of the daily brief — 30-day catalyst calendar. Use when the user wants to see upcoming events: 'timeline', 'what's coming up', '下次 catalyst', 'earnings calendar', 'next 30 days', 'upcoming'. Aggregates timeline.yaml + active-stock earnings + recorded prediction score_dates. Writes '## Timeline 30d' H2 to dashboard/{date}.md."
---

# /timeline

Module 3. The unified "what's next" calendar. This is the answer to "I want to know what to look at".

## When invoked solo

- "timeline" / "what's coming up" / "upcoming"
- "earnings calendar" / "下次 catalyst" / "next 30 days"
- AUTOMATICALLY as module 3 of [[report]]

## Steps

### 1. Build the merged timeline

```bash
uv run --project scripts scripts/build_timeline.py --md --days 30
# or for a renderer-friendly block:
uv run --project scripts scripts/build_timeline.py --block --days 30
```

Sources merged:
- `timeline.yaml` — hand-curated events (earnings, FOMC dates, lock-ups, policy windows)
- `attributions/index.jsonl` — prediction `score_date` entries (auto-injected)

Each event gets an urgency tier:
- 🔥 within 7 days
- ⚠ 8–14 days
- ▢ 15–30 days
- ▢ 30+ days (excluded by default; shown only with `--days 60` etc.)

### 2. Write H2 section

Replace any existing `## Timeline 30d` H2 in place. Structure:

```markdown
## Timeline 30d

```callout {info}
{N events in the next 30 days. {Y} are 🔥 within 7 days. The most important: {top-1 event}.}
```

### 🔥 Within 7 days
{markdown bullets from build_timeline.py --md}

### ⚠ 8–14 days
{...}

### ▢ 15–30 days
{...}
```

OR use the visual `timeline` block if a more compact view fits:

```markdown
## Timeline 30d
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

## Hard rules

- **Don't fabricate dates** — if unsure of an earnings date or policy deadline, mark it as "estimate" or "~" in the note
- **Future events only by default** — past prediction score_dates etc. are already in attributions index
- **The timeline.yaml is hand-maintained** — agent adds entries when user asks; agent does NOT auto-add things it "noticed" in news
- **Macro calendar is included** — CPI / NFP / FOMC / GDP are pre-filled

## What this gives you

Before this skill, the workspace knew about today + recent days. Now it knows about the next 30. This makes the brief module's "下个关键点" section actually quantitative (with specific dates) rather than vague.
