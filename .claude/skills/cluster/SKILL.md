---
name: cluster
description: "Generate a focused tab for ONE focus cluster — a stock, topic, or sector defined in groups.yaml focus_clusters. Each cluster produces a `## Focus: {name}` H2 with today's tape across its members, inter-stock dynamics, key catalysts, and a verdict. Triggers: 'focus on {cluster}', '{cluster} 板块', 'TSLA focus', 'DRAM focus', 'energy focus', 'AI capex focus', '能源 focus'. Run by /report automatically for every defined cluster; can also be called solo."
---

# /cluster

Module for **focused multi-stock analysis** along a defined cluster (stock / topic / sector). Each cluster lives in `groups.yaml::focus_clusters` and produces one tab in the day's dashboard.

## When invoked

### Solo
- "focus on TSLA" / "TSLA focus tab"
- "DRAM cluster" / "DRAM/HBM focus" / "memory cluster"
- "AI capex focus" / "hyperscaler cluster"
- "能源 focus" / "energy focus"
- "SpaceX focus"

### From /report
After modules 1-3 (Pulse / Watchlist / Timeline) finish, /report iterates **every** cluster in `focus_clusters` and emits one tab per cluster, BEFORE invoking Brief.

## Steps

### 1. Read the cluster spec

```yaml
- name: DRAM/HBM
  kind: topic
  members: [MU, "000660.KS", "005930.KS", DRAM]
  description: ...
  watch_items: [...]
```

`kind` controls layout emphasis:
- `stock`  — single ticker deep view (price detail + thesis + catalysts)
- `topic`  — multi-stock correlated set (inter-stock dynamics matter most)
- `sector` — multi-stock distinct theses (each gets its own row)

### 2. Fetch fresh quotes for all members in parallel

```bash
for t in $MEMBERS; do
  uv run --project scripts scripts/fetch.py "$t" > "/tmp/cluster_$t.json" 2>/dev/null &
done; wait
```

**Null handling**: `fetch.py` returns `null` for unavailable fields (recent IPOs, indices, foreign tickers). Render as `n/a`. yfinance prints "No fundamentals data" to stderr for ETFs/indices — harmless, ignore.

### 3. Pull cluster-specific signals

For each cluster, ALSO check:
- **stock kind**: triggers.yaml for thesis-break distance; latest stocks/{T}/attributions.md
- **topic kind**: cross-correlation (do members all move together today? if not, why?)
- **sector kind**: which name is leading, which lagging; capex vs revenue dynamic

### 4. Find a historical analog

Run [[find-similar-moves]] with relevant tags for the cluster. Cite a date + outcome if a match exists.

### 5. Write the H2 section

Replace any existing `## Focus: {cluster.name}` H2 in place. Boundary: from that H2 to next `## ` or EOF.

Structure (adapt to kind, but always include all of these):

```markdown
## Focus: {cluster.name}

```callout {info|warn|danger}
{One sentence: where this cluster is today + the single most important thing.}
```

### 今日数据
```kpi
{Each member: ticker | $price / 1D% / 5D% / 30D% | signal + 1-line read}
```

### 今日的故事
{2-3 short paragraphs. What drove the cluster today? Was the movement correlated or divergent? Cite specific catalysts. Reference attribution entries if any were recorded today.}

### Inter-member dynamics  (for topic / sector kinds)
```compare
| Member | 1D% | Driver | Read
| ...    | ... | ...    | ...
```

For `stock` kind: skip this — single member, no inter-stock dynamic. Replace with "## Position vs thesis":
- Distance to thesis-break: ${X} / +Y% buffer
- Closest kill condition: {state}
- Active re-read triggers: {any fired?}

### 下次关键 catalyst (top 3 from watch_items + timeline.yaml)
```timeline
{date} 🔥/⚠/▢ | {event} — {why it matters for this cluster}
```

### Verdict
```verdict {hold|add|trim|exit|watch}
{One sentence: what to do or not do based on cluster state.}
```

```callout info
**Don't**: {1 concrete don't given today's state}.
**If acting**: {what data point unlocks action}.
```
```

### 6. Don't render — /report's job

If invoked solo, render at the end. If invoked from /report, orchestrator renders once after Brief.

## Hard rules

- **One H2 per cluster** — `## Focus: TSLA`, `## Focus: DRAM/HBM`, etc.
- **Idempotent**: same-day re-run replaces in place
- **Members include externals**: if `members_external` is set (e.g. SK Hynix Korean ticker), still fetch and include them in the data table — they're not "active stocks" in the workspace but they're load-bearing for the cluster narrative
- **Cite analogs**: when a similar cluster move happened before, name the date + outcome (1 line)
- **Topic kind = correlation matters**: if MU is down but SK Hynix is up, that's the lead — surface it
- **Verdict is mandatory** — every cluster ends with a verdict pill + don't/if-acting callout

## Skill linkage

- Each cluster lives in `groups.yaml::focus_clusters`
- [[report]] iterates all clusters and calls /cluster per cluster
- [[brief]] reads cluster outputs to write the cross-cluster synthesis
- [[find-similar-moves]] / [[find-analysis]] used to ground each cluster's narrative
- Adding a cluster: user says "add cluster: {name} with members [...]" → agent edits groups.yaml
