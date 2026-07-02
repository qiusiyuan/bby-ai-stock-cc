---
name: earnings-scorecard
description: "Use when a tracked stock's earnings_watchlist scoring_date arrives, or the user explicitly asks to 'score the earnings' / '财报打分' / 'run the scorecard'. Reads the pre-committed scorecard file at stocks/{T}/research/*-next-earnings-watchlist.md, fetches the actual print, fills in Tier 1/2 grid actual-vs-bar, writes verdict to thesis.md Stands & Updates, flips state.yaml::earnings_watchlist.status to 'scored'. The whole point: enforce pre-commitment so a single blowout can't fool us into a regime change."
---

# /earnings-scorecard

The mechanism that turns "this earnings is amazing" into a falsifiable scoring exercise against bars we set *before* the print.

## Why this skill exists

After a blowout earnings, the market always says "this is the new regime." Sometimes it is. Usually it isn't. Without a pre-committed scoring exercise, the agent (and the user) reads each subsequent print fresh and unconsciously moves the goalposts. The earnings_watchlist + this skill enforce: **you set the bar before the print, and you grade the print against the bar you set, not against whatever consensus drifted to by then**.

## When invoked

**Automatically:**
- AUTOMATICALLY from `/report` and `/watchlist` when any `stocks/{T}/state.yaml::earnings_watchlist.scoring_date == today` AND `status: pending`.
- AUTOMATICALLY when the user asks `生成 report` / `今天 report` / `daily report` on a scoring date.

**Manually:**
- "score MU earnings" / "MU 财报打分" / "run the scorecard on MU"
- "did MU's print confirm the thesis"

## Steps

### 1. Find the active scorecard

```bash
# Iterate stocks/*/state.yaml, find any with earnings_watchlist.status == pending
# Pick the one(s) whose scoring_date matches today (or that the user named)
```

For each candidate:
- Read `state.yaml::earnings_watchlist` — get `scorecard`, `thesis_claim`, `baseline_print`
- Read the scorecard markdown file at `earnings_watchlist.scorecard`
- The Tier 1 / Tier 2 / Tier 3 tables in that file are the bars

### 2. Pull the actual print

```bash
uv run --project scripts scripts/fetch.py {TICKER}  # price, vol, news headlines
```

For the actual earnings numbers, the scorecard's metrics are typically in the company's press release. Look in the 72h news for headlines containing "earnings", "reports", "Q{n}". WebFetch the press release / Yahoo earnings recap. **Never invent numbers.** If a Tier 1 metric isn't disclosed in time, mark it `n/a — pending 10-Q`.

### 3. Fill in actual-vs-bar

Open the scorecard, but DO NOT edit it (it's the pre-commitment artifact — append-only context). Instead, write a NEW H2 section to today's `dashboard/{YYYY-MM-DD}.md` titled `## Earnings scorecard: {TICKER}`. Inside:

```markdown
## Earnings scorecard: {TICKER}

> 评分 claim: 「{thesis_claim}」（基准: {baseline_print} Q{X} 财报）
> Scorecard 源文件: [{scorecard path}]({scorecard path})

### Tier 1 — verdict drivers

```compare
指标 | 「Secular 确认」门槛 | 「Cycle peak」门槛 | 实际 | 命中?
{...每一行 Tier 1 从 scorecard 抄过来, 加上实际数字, 加 ✅ / ❌ / ⚠ 命中标记...}
```

### Tier 2 — confirms or contradicts

{同样的 actual-vs-bar 表}

### 命中模式 → verdict

- Tier 1 命中：{N}/5
- Verdict: {根据 scorecard 的「如何打分」三档对应输出}

### 我对叙事的判断

{1-3 段：claim 是否成立？为什么？市场反应（盘后/次日）与我的判断是否一致？需要更新 thesis 哪一块（bull/base/bear 权重？thesis_break_price？kill conditions？）}
```

### 4. Append verdict to thesis.md Stands & Updates

Per the append-only rule:

```markdown
### {YYYY-MM-DD}  {tone — Bullish/Bearish/Neutral/Risk flag}
**Earnings scorecard 评分（claim: {thesis_claim}）。** Tier 1 命中 {N}/5。{1-2 句结论}. 详见 dashboard 当天 H2「Earnings scorecard: {TICKER}」。
```

### 5. Flip state.yaml status

Edit `stocks/{T}/state.yaml::earnings_watchlist.status` from `pending` to `scored`. If the verdict is "narrative breaks", also bump it to `invalidated`. Add a new field `scored_on: {YYYY-MM-DD}` and `scored_verdict: {validated|mixed|breaks}`.

If the user wants to track the NEXT earnings (likely, if verdict was mixed), prompt:
> Verdict 是 mixed — 要为下次财报建一份新的 scorecard 吗？（更新 thesis、设新的 scoring_date）

### 6. Update triggers.yaml if verdict warrants

- **Validated** → likely raise `thesis_break_price`. Ask the user before editing.
- **Breaks** → confirm `kill_conditions` triggered; remind user.
- **Mixed** → no automatic edits.

### 7. Render dashboard

Run `uv run --project scripts scripts/render.py dashboard/{YYYY-MM-DD}.md` to refresh the HTML.

### 8. Chat reply (3-5 lines)

```
{TICKER} 财报评分完成。Tier 1 {N}/5 命中。Verdict: {validated|mixed|breaks}。
{一句话叙事判断}.
已写入 dashboard 和 thesis.md。state.yaml 标记为 scored。
```

## Hard rules

- **Bars from the pre-committed scorecard, not consensus.** If the analyst expectations drifted between scorecard creation and the print, that doesn't move the bar. The point of pre-commitment is to prevent goal-post moving.
- **Tier 1 命中模式 决定 verdict**, not any single number. Re-read the scorecard's grading table — it's explicit.
- **Numbers come from the press release, not from sell-side recaps.** Sell-side spins. The PR is the primary source.
- **Append, don't edit.** Stands & Updates is append-only. The scorecard file is also append-only (it's the historical artifact of what we believed before the print).
- **Distinguish business performance from claim verdict.** A company can have a great quarter and have the *specific claim* still fail (e.g. GM held but FY27 guide turned cautious → "next NVDA" framing weakens, business is fine).

## Skill linkage

- Created by writing `stocks/{T}/research/*-next-earnings-watchlist.md` + populating `state.yaml::earnings_watchlist` (typically right after the print that spawned the claim).
- Auto-invoked by [[report]], [[watchlist]], [[morning]] on scoring_date.
- Writes to: `dashboard/{date}.md`, `stocks/{T}/thesis.md` (Stands & Updates), `stocks/{T}/state.yaml`, optionally `stocks/{T}/triggers.yaml`.
