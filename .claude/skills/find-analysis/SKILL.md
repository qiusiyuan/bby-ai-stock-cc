---
name: find-analysis
description: Use when the user wants to find past analyses written into dashboard files ("what did I write about AI capex", "past SPCX analyses", "show pressure-tests on SPCX", "what was that AVGO/MRVL deep dive"). Searches dashboard/YYYY-MM-DD.md by keyword / ticker / date and returns dated titles + 1-line previews. Different from `find-similar-moves` (price-attribution lookup) — this is prose-analysis lookup.
---

# find-analysis

The per-day dashboards (`dashboard/YYYY-MM-DD.md`) are the workspace's analysis archive — every H2 section is one analysis unit. This skill finds them by topic.

## When invoked

- "what did I write about AI capex"
- "past SPCX analyses"
- "show me old pressure-tests"
- "what was that AVGO/MRVL deep dive last week"
- "find analyses on memory pricing"
- "what have I written about <topic>"
- AUTOMATICALLY before writing a fresh deep-dive on a topic — query first to avoid redoing analysis already in the archive.

## Difference from find-similar-moves

| Skill | What it queries | Output |
|---|---|---|
| [[find-similar-moves]] | `attributions/index.jsonl` (price-attribution events, tagged) | Dated price moves + named catalysts |
| **find-analysis** | `dashboard/YYYY-MM-DD.md` H2 sections (prose deep-dives) | Dated analysis titles + previews + paths |

Use both when researching: attributions tell you *what moved*, analyses tell you *what I thought*.

## Steps

1. **Run `find_analysis.py` with the most specific filter you can infer:**

   ```bash
   # By keyword (substring in title or body, case-insensitive)
   uv run --project scripts scripts/find_analysis.py --keyword "ai capex"

   # By ticker (matches mentions in title or body)
   uv run --project scripts scripts/find_analysis.py --ticker SPCX

   # By date window
   uv run --project scripts scripts/find_analysis.py --since 2026-06-01 --until 2026-06-23

   # Combine
   uv run --project scripts scripts/find_analysis.py --ticker SPCX --keyword pressure

   # Titles only (cheaper, less recall)
   uv run --project scripts scripts/find_analysis.py --keyword memory --titles-only
   ```

   Default output is markdown — dated entries with title, mentioned tickers, and 1-line preview. Add `--json` if you need structured output.

2. **Inline in chat** — list the matches as a short bulleted block. Each entry should include:
   - Date · Title (linked to the file)
   - Tickers mentioned
   - The 1-line preview (the script already extracts it)

3. **Offer to open** — if the user picks one, render the day file:
   ```bash
   uv run --project scripts scripts/render.py dashboard/{YYYY-MM-DD}.md --title "{YYYY-MM-DD}"
   ```
   Then in chat tell them which tab to click (the H2 title).

4. **Suggest writing fresh** — if the keyword returns 0 matches, suggest the user write one now (typically via brainstorming / deep-dive / a new H2 in today's dashboard).

## Hard rules

- **Never fabricate matches.** If nothing comes back, say "no past analyses match" — do not invent dates.
- **Recency-first.** Output is reverse-chronological. Newer analyses usually supersede older ones; flag any pre-existing analysis older than 60 days as "may be stale".
- **Cross-link.** When citing a past analysis in fresh writing, use the form `[[2026-06-22 AI capex analysis]]` so future searches find the linkage.

## Skill linkage

- Called before deep-dive writing — see if the user already wrote a similar piece.
- Companion to [[find-similar-moves]] (which queries the attribution index).
- The [[morning]] skill can auto-suggest "look at your past analyses on {today's hot ticker}" when surfacing attribution candidates.
