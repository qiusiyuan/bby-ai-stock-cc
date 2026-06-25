---
name: research
description: "Long-form structural research — produces a standalone document (NOT a dashboard tab). Use when user wants deep multi-month-relevance analysis: company business structure, customers / supply chain / capacity, sector deep dives, historical case studies, competitive frameworks. Triggers: 'deep research on X', '深入研究 X', 'structural analysis', 'long-term framework', '长期分析', 'business structure of X', 'industry deep dive'. Writes to stocks/{T}/research/{date}-{topic}.md (per-stock) or research/sectors/{date}-{topic}.md (cross-cutting), NOT dashboard/{date}.md."
---

# /research

Long-form research that **lives outside the daily dashboard**. Used for analysis with **3-month+ shelf life** — company structure, sector frameworks, historical case studies, multi-month theses.

## When invoked

### Solo
- "deep research on MU" / "深入研究 MU"
- "structural analysis of {company/sector}"
- "long-term framework for {topic}"
- "industry deep dive on {sector}"
- "{company} 业务结构 / 客户 / 产能 / 财务历史"
- "competitive analysis: X vs Y vs Z"
- "memory cycle history" / "AI capex thesis" / "energy supercycle"

### When agent should suggest /research instead of dashboard tab

If user asks for analysis and ALL of these are true:
- Topic has shelf life ≥ 3 months
- Content is structural (not "today's move")
- Length is likely > 200 lines
- Won't be re-generated every day

→ Suggest "let me write this as a research note, not a daily tab" before proceeding.

## File layout

```
stocks/{TICKER}/research/
  {YYYY-MM-DD}-business-structure.md     单股深度
  {YYYY-MM-DD}-hbm-deep-dive.md          单股某主题
  {YYYY-MM-DD}-competitive-position.md   单股竞争分析

research/
  sectors/
    {YYYY-MM-DD}-ai-capex-thesis.md      跨公司主题
    {YYYY-MM-DD}-memory-cycle-history.md
    {YYYY-MM-DD}-energy-supercycle.md
  cases/
    {YYYY-MM-DD}-2024-yen-carry-unwind.md   历史案例参考
```

**Routing rule**:
- Single ticker → `stocks/{T}/research/`
- 2-5 tickers in a defined cluster → `stocks/{primary}/research/` with cross-refs
- Cross-cutting (sector / theme / macro) → `research/sectors/`
- Historical analog → `research/cases/`

## Steps

### 1. Confirm scope

Before writing, confirm with user (or infer from prompt):
- Single stock or cross-cutting topic?
- Target file path
- Any specific dimensions (customers / financials / competitive / valuation) to emphasize

### 2. Gather data

Standard sources (depends on topic):
- `stocks/{T}/thesis.md` for current thesis context (don't duplicate; cross-link)
- WebFetch for company filings, recent quarterly results, news
- yfinance for historical financials
- attribution/index.jsonl for past events (cite as analogs)
- find_analysis for past notes on the topic

### 3. Structure (default — adapt to topic)

```markdown
# {TICKER or TOPIC} — {分析角度}

> **Research note** · {YYYY-MM-DD} · {scope: 长期 sizing / 板块 thesis / 历史案例}
> 涵盖: {bulleted list of dimensions}
> 下次 review: {3-6 months later, or 'on thesis-break trigger'}

```callout info
{One-sentence why this note exists. Whose decision does it help?}
```

## Background / context
{Brief context. Cross-link to thesis if relevant: see [stocks/{T}/thesis.md](../thesis.md)}

## {Dimension 1 — e.g. 业务结构}
...

## {Dimension 2 — e.g. 客户名单}
...

## {Dimension N}
...

## 关键判断
{Synthesis — the WHY behind sizing / hold / cut decisions}

## 重读触发条件
- {What event would invalidate this analysis?}
- {When should I revisit?}
```

### 4. Always include "下次 review" trigger

Every research note must end with concrete conditions for re-reading:
- Date-based (3 months / 6 months)
- Event-based (next earnings / sector catalyst / thesis-break)
- Threshold-based (price moves > N% / margin compresses / market share shifts)

Otherwise the note rots silently.

### 5. Don't render to dashboard

Research notes have their own H1 and are read as standalone documents. They do NOT go into dashboard/{date}.md. If user wants today's dashboard to mention a research note, link it as a short pointer (1-2 lines).

### 6. Tell the user where it landed

After writing, in chat:
```
Wrote {filepath} ({N} lines covering {dimensions}). Next review {trigger}.
```

Optional: render the research note to HTML for browser viewing (single doc, no tabs):
```bash
uv run --project scripts scripts/render.py {filepath} --title "{TICKER} {topic}"
```

## Hard rules

- **NOT a dashboard tab**. Research lives in `stocks/{T}/research/` or `research/sectors/`.
- **Long shelf life only**. If the analysis is "what happened today" or "what should I do tomorrow", that's deep-dive in dashboard, not research.
- **Always has a review trigger** — date or event. Stale research is worse than no research.
- **Cross-link don't duplicate**: if thesis.md already says something, link to it.
- **Datasources cited**: every claim has a source — yfinance / specific webpage / SEC filing / SEC EDGAR.
- **No daily price commentary**. Research is about structure, not tape.

## Skill linkage

- Related to [[deep-dive]] — but deep-dive is a daily tab (tactical, today's events); research is a standalone doc (strategic, multi-month).
- [[find-analysis]] should be extended to scan `stocks/*/research/` and `research/**/` for prior notes.
- [[brief]] can cross-link to research notes when relevant ("see [research note on MU customer base](../stocks/MU/research/2026-06-23-business-structure.md)").
- New research note triggers an update to `stocks/{T}/state.yaml::last_research` so other skills know structural analysis exists.
