---
name: publish
description: "Render markdown to HTML, rebuild the site index, commit, and push. The single command for making any workspace artifact live on GitHub Pages. Triggers: '发布', 'publish', 'push', 'deploy', '上线'. Handles two content types (daily report vs deep dive) with different file paths and index routing."
---

# /publish

The final step that makes any workspace artifact visible on the published site. Handles rendering, index rebuild, git commit, and push in one command.

## When invoked

- "发布" / "publish" / "push it" / "deploy" / "上线"
- AUTOMATICALLY at the end of [[report]] after all modules are composed
- After creating a deep dive, research doc, or any artifact the user wants published

## Two content types → two paths

| Type | Source location | Rendered filename pattern | Index tab |
|------|----------------|--------------------------|-----------|
| **Daily report** | `dashboard/{YYYY-MM-DD}.md` | `dashboard-{YYYY-MM-DD}-md.html` | "Daily reports" (cards) |
| **Deep dive / research** | `stocks/{T}/research/{date}-{slug}.md` OR `research/{date}-{slug}.md` | `stocks-{t}-research-{date}-{slug}-md.html` OR `research-{date}-{slug}-md.html` | "Deep dives" (list) |

### How to decide which type

- **Daily report**: anything that goes into `dashboard/{date}.md` — the main daily brief with Pulse/Watchlist/Timeline/Clusters/Brief/Deep Dive sections. One per day.
- **Deep dive (per-stock)**: analysis of a specific company → lives in `stocks/{TICKER}/research/{date}-{slug}.md`
- **Deep dive (topic/cross-stock)**: sector analysis, thematic study, structural reference → lives in `research/{date}-{slug}.md`. Shows as "TOPIC" in the deep dives tab.

## Steps

### 1. Identify what to publish

If the user just says "发布" with no argument, publish whatever was just created/modified in this session. If ambiguous, ask.

### 2. Pre-render fence check (MANDATORY)

Before rendering, validate that all fenced code blocks are balanced. Unmatched fences break the tab parser silently (tabs collapse into a single blob).

```bash
python3 -c "
import re, sys
text = open('{source_path}').read()
lines = text.split('\n')
stack = []
errors = []
for i, line in enumerate(lines, 1):
    if re.match(r'^\`\`\`\w+', line):
        stack.append((i, line.strip()))
    elif re.match(r'^\`\`\`\s*$', line):
        if stack:
            stack.pop()
        else:
            errors.append(f'L{i}: extra closing fence (no matching open)')
if stack:
    for ln, tag in stack:
        errors.append(f'L{ln}: unclosed {tag}')
if errors:
    print('❌ Fence errors:'); [print(f'  {e}') for e in errors]; sys.exit(1)
print('✅ Fences balanced')
"
```

**If this fails**: fix the markdown BEFORE rendering. Common causes:
- Plain ` ``` ` used for ASCII art / flow diagrams → remove the fences or use indented code block (4 spaces)
- Missing closing ` ``` ` after a custom block

### 3. Render

```bash
uv run --project scripts scripts/render.py {source_path} --title "{title}"
```

This outputs to `site/reports/{slug}.html`. The slug is auto-derived from the source path.

### 4. Rebuild site index

```bash
uv run --project scripts scripts/build_index.py
```

This regenerates `site/index.html` with:
- **Daily reports tab**: scans `dashboard-{date}-md.html` files; newest 5 as cards, rest in archive
- **Deep dives tab**: scans `stocks-{ticker}-research-{date}-{slug}-md.html` AND `research-{date}-{slug}-md.html`; listed with date, ticker (or TOPIC), and title

### 5. Git commit + push

```bash
git add {source_file} {rendered_html} site/index.html
git commit -m "publish {date} {type}: {short description}"
git push
```

### 6. Confirm to user

```
已发布。{commit_hash} pushed. Index 已更新 — {type} tab 可见。
```

## File naming conventions

### Daily reports
- Source: `dashboard/2026-07-01.md`
- Rendered: `site/reports/dashboard-2026-07-01-md.html`
- Title: the date (e.g. "2026-07-01")

### Per-stock deep dives
- Source: `stocks/MU/research/2026-06-23-business-structure.md`
- Rendered: `site/reports/stocks-mu-research-2026-06-23-business-structure-md.html`
- Index shows: `2026-06-23 | MU | Business structure`

### Topic/cross-stock deep dives
- Source: `research/2026-07-01-ai-value-chain.md`
- Rendered: `site/reports/research-2026-07-01-ai-value-chain-md.html`
- Index shows: `2026-07-01 | TOPIC | Ai value chain`

## Hard rules

- **Always rebuild index after rendering.** A rendered file without index update = invisible to readers.
- **Always push.** Publish means live. If the user just wants to render locally without pushing, they'll say "render" not "publish".
- **One commit per publish.** Don't bundle unrelated changes.
- **Index is the source of truth** for what's publicly visible. If it's not in index, it's not published.
- **Don't duplicate**: if re-publishing same-day report, the render overwrites in place (idempotent). Index rebuild picks up whatever's on disk.

## Skill linkage

- [[report]] calls /publish at the end after composing dashboard/{date}.md
- [[deep-dive]] calls /publish if the user asked for a standalone deep dive to be published
- [[research]] calls /publish for any topic research output
- Manual: user says "发布" after any artifact creation
