# Attribution memory

Every meaningful price move on a watched stock is recorded here as **data, not just narrative.** When a similar event happens later, we look up the analog and compare.

## Two stores, kept in sync

1. **Per-stock log** — `stocks/{TICKER}/attributions.md` (human-readable, append-only)
2. **Structured index** — `attributions/index.jsonl` (one JSON line per attribution, queryable)

Both are written by the [[explain-move]] skill. Reading uses the MD. Pattern matching uses the index.

## Threshold for recording

An attribution is recorded when ANY of:
- `|change_pct_1d| >= 3%`
- `|change_pct_5d| >= 10%`
- `volume_ratio >= 1.5x`
- User explicitly asks for an attribution
- A specific named catalyst occurred (earnings, guidance, regulatory action, etc.)

Below threshold = noise; recording it pollutes pattern-matching.

## Tag vocabulary (use these, do not invent new ones lightly)

**Catalyst kind** (pick 1-3):
- `earnings_print`, `earnings_pre_print`, `earnings_post_print`
- `guidance_raise`, `guidance_cut`, `guidance_inline`
- `regulatory_positive`, `regulatory_negative`
- `executive_comment` (CEO/CFO public statement)
- `analyst_upgrade`, `analyst_downgrade`, `pt_change`
- `competitor_news`, `partnership_news`, `m_and_a`
- `macro_oil`, `macro_rates`, `macro_dollar`, `macro_inflation`
- `geopolitical_war`, `geopolitical_trade`, `geopolitical_sanctions`
- `policy_us`, `policy_china`, `policy_eu`
- `index_inclusion`, `index_removal`, `lockup_expiry`, `secondary_offering`
- `commodity_move`, `sector_rotation`, `flow_event` (ETF flows / passive)
- `tech_breakthrough`, `production_milestone`, `safety_recall`
- `unattributed` (use this when nothing fits — better than fabricating)
- `thesis_debate` (use when a recorded entry captures the user's view + agent counter-take, both stored for later scoring)
- `user_stand` (use when an entry primarily records the user's evolving view, not a price-move attribution)
- `prediction_recorded` (use when an entry stores a testable forecast with a scoring date — see `predicted_for` and `score_date` fields below)
- `prediction_passed` / `prediction_failed` (use when scoring a prior `prediction_recorded` entry on its score date)

**Direction**: `up` or `down`

**Magnitude**: `minor` (<3%), `material` (3-7%), `major` (>7%), `extreme` (>15%)

**Confidence in attribution**: `high`, `medium`, `low`

## Prediction spec (structured, machine-evaluatable)

When a `prediction_recorded` entry is added, it MUST include a `prediction_spec` field that the scorer (`scripts/score_predictions.py`) can evaluate without parsing prose. Five spec kinds:

```yaml
# 1) close_above — passes if any close in the window is >= threshold
prediction_spec:
  kind: close_above
  ticker: SPCX
  threshold: 200
  window_start: 2026-06-22
  window_end: 2026-06-26

# 2) close_below — passes if any close in the window is <= threshold
prediction_spec:
  kind: close_below
  ticker: SPCX
  threshold: 185
  window_start: 2026-06-22
  window_end: 2026-08-31

# 3) range — passes if every close in the window is within [low, high]
#    Optional: also fails if it ever closes outside [hard_low, hard_high]
prediction_spec:
  kind: range
  ticker: SPCX
  low: 190
  high: 235
  hard_low: 180   # if any close < hard_low, fail
  hard_high: 260  # if any close > hard_high, fail
  window_start: 2026-06-22
  window_end: 2026-08-31

# 4) conditional — runs `if_spec`; if it fires, scores `then_spec`; else verdict = "n/a"
prediction_spec:
  kind: conditional
  if_spec:
    kind: close_above
    ticker: SPCX
    threshold: 250
    window_start: 2026-06-18
    window_end: 2026-08-01
  then_spec:
    kind: range
    ticker: SPCX
    low: 230
    high: 270
    window_start: 2026-09-25  # single-day check is allowed (start == end)
    window_end: 2026-09-25

# 5) trigger_chain — A then B; if A fires within its window, then B is scored within its window
prediction_spec:
  kind: trigger_chain
  trigger:
    kind: range
    ticker: SPCX
    low: 200
    high: 220
    hard_high: 230  # if it breaks 230 during trigger window, trigger fails (no entry)
    window_start: 2026-06-22
    window_end: 2026-07-31
  outcome:
    kind: close_below
    ticker: SPCX
    threshold: 185
    window_start: 2026-08-01
    window_end: 2026-08-31
```

### Verdict states

The scorer writes back into the same JSONL line:

```json
"verdict": {
  "state": "pass" | "fail" | "n/a" | "pending",
  "scored_on": "YYYY-MM-DD",
  "evidence": "Closed $202.30 on 2026-06-23 — passes close_above 200",
  "actual_high_in_window": 215.40,
  "actual_low_in_window": 178.20
}
```

`n/a` is reserved for conditional predictions whose trigger never fired — the prediction was conditional on something that didn't happen, so it's neither right nor wrong.

## Index schema (one JSON object per line)

```json
{
  "date": "2026-06-18",
  "ticker": "DRAM",
  "change_pct_1d": 9.66,
  "change_pct_5d": 17.80,
  "change_pct_30d": 57.58,
  "volume_ratio": 1.21,
  "direction": "up",
  "magnitude": "major",
  "tags": ["executive_comment", "memory_pricing", "ai_demand"],
  "confidence": "high",
  "primary_cause": "Tim Cook's 'unavoidable' memory price hike comment",
  "sources": [
    {"type": "headline", "title": "SanDisk Jumps 11%, Western Digital Rises 7% After Apple Flags 'Unavoidable' Memory Price Hikes", "publisher": "Yahoo", "url": "..."},
    {"type": "corroboration", "note": "SanDisk +11%, WD +7%, MU well bid same day"}
  ],
  "cross_assets": {"sector_etf_pct_1d": null, "spy_pct_1d": 0.4, "vix": 14.2, "10y": 4.31, "wti": null},
  "snapshot_path": "stocks/DRAM/snapshots/2026-06-18.md",
  "log_path": "stocks/DRAM/attributions.md",
  "agent_read": "Stage-2 of memory cycle: AI demand pulling consumer-product margins. Stage-1 was hyperscaler, stage-2 is consumer products absorbing memory cost. Stage-3 historically broader inflation pass-through, then crash."
}
```

## Per-stock log format

`stocks/{TICKER}/attributions.md`:

```markdown
# {TICKER} attributions

Append-only. Each entry = one decision-point in the stock's history.

---

### {YYYY-MM-DD} · {±%} day · {direction emoji}{magnitude tag}
**Tags:** `executive_comment`, `memory_pricing`, `ai_demand`
**Confidence:** high

**Primary cause.** Tim Cook flagged "unavoidable" memory price hikes during Apple disclosure.

**Sources.**
- Yahoo headline (cited, link)
- Multi-stock corroboration: SanDisk +11%, WD +7%, MU well bid

**Cross-assets.** SPY +0.4% · VIX 14.2 · 10Y 4.31% · WTI N/A

**Agent read.** Stage-2 of memory cycle — AI demand bleeding into consumer products. Path forward: stage-3 historically broader pass-through, then supply response, then crash.

[Snapshot](snapshots/2026-06-18.md) · [JSONL line 12](../../attributions/index.jsonl)

---
```

## How to query

The [[find-similar-moves]] skill takes either:
- A **date** ("how did NVDA react last time HBM pricing news hit?")
- A **tag set** ("show me all DRAM moves with executive_comment tag")
- A **stock + magnitude** ("biggest moves on SU with confidence:high")

Returns matching attribution lines + links to full narrative. Used to ground analysis when a similar catalyst arrives.
