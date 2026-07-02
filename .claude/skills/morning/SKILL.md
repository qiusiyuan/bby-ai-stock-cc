---
name: morning
description: Use as the single entry point for a session ("morning", "good morning", "let's check in", "session start", "what's up"). Scores due predictions first, then hands off to [[report]] which pops the module menu and runs the chosen modules. The session-opener — thin wrapper around /report with a predictions-scoring pre-step.
---

# morning

The session-opener. **As of the 2026-06-23 redesign, this is a thin wrapper around `/report`** with one pre-step: score due predictions first. Everything else (Pulse / Macro / Watchlist / Movers / Timeline / Brief / Deep-dive menu) goes through [[report]].

## When invoked

- "morning" / "good morning"
- "let's check in" / "session start" / "let's see what's going on"
- "what's up" (in a market context)
- A bare "/morning" or implicit start of a fresh session

If the user has typed a more specific request (e.g. "deep dive on NVDA", "compare ai stocks"), do that instead — `/morning` is for the broad opener.

## Steps

### 1. Score due predictions FIRST

This is the only thing /morning does before delegating. Past forecasts get verdict'd before anything else.

```bash
uv run --project scripts scripts/score_predictions.py
```

Read the JSON output. For each newly-scored prediction:
- **pass** → "✅ Prediction from {date} hit. {primary_cause one-liner}. Evidence: {verdict.evidence}."
- **fail** → "❌ Prediction from {date} missed. {primary_cause}. Evidence: {verdict.evidence}."
- **n/a** → "⏭ Conditional prediction from {date} did not fire. {trigger_verdict.evidence}."

If 0 predictions were due today: state "no predictions due today" and skip the formatted block.

### 2. Hand off to [[report]]

Invoke /report with the trigger phrase "morning report" so it preselects modules 1+2+3+4 (Pulse / Watchlist / Timeline / Brief). The orchestrator shows the menu (user can still uncheck or add deep-dives), runs the chosen modules, renders.

### 3. Chat reply — 3-5 lines max

```
Morning. {prediction verdicts in one line OR "no predictions due"}. {report briefly: N tabs generated, top headline}. Opened in browser.
```

Don't restate what the report contains — the user is looking at it.

## Hard rules

- **Predictions FIRST.** They're the calibration data. They never get scored if this skill doesn't score them.
- **Delegate to /report** for everything else — don't duplicate module logic here.
- **Menu still shows** — even on morning. User confirmed: morning should also pop the menu.
- **Brief in chat.** The user came here to start a session, not to read 200 lines.

## Skill linkage

- Always calls `score_predictions.py` first.
- Delegates to [[report]] for module orchestration.
- [[report]] in turn calls [[pulse]] / [[watchlist]] / [[timeline]] / [[brief]] and optionally [[deep-dive]].
