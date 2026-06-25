# Report Redesign — 2026-06-23

## 你真正要的（不是 AI 那个 8-grid spec）

一份**每日综合 brief**：以"今天市场发生了什么 + 这对我持仓意味着什么 + 下一步看什么 + AI 怎么判断"为主线，**串起来叙述**，而不是 8 个孤立 grid。死板模板没有用 — 同一天可能只需要 macro + 2 只重点股，另一天可能需要 5 只全跑。**Layout 跟着内容走，不是反过来。**

## 核心设计：4 个一站式模块 + 5 个按需独立模块

**「重点」 vs 「按需」** 是关键区分：

| 类型 | 模块 | 什么时候出现 |
|---|---|---|
| **一站式核心** (默认每天) | 1. **Pulse + Macro 一体**：大盘 + 宏观 + 政策新闻 | 每次 /report 默认出 |
| **一站式核心** (默认每天) | 2. **Watchlist + Movers 一体**：持仓快照 + 异动 + trigger 距离 | 每次 /report 默认出 |
| **一站式核心** (默认每天) | 3. **Timeline 30天**：财报 / launch / FOMC / NFP / CPI / 调查结论 / lock-up | 每次 /report 默认出 |
| **一站式核心** (默认每天) | 4. **Brief 综合**：把 1+2+3 串起来 — "今天 X 跌是因为 Y，下个关键点 Z，我的判断 W" | 每次 /report 默认出 |
| **按需独立** | 5. **Deep dive**：单一股票全套分析 + thesis 重看 + probability | 用户说 "deep dive on X" 或 movers 里 flag 后追问 |
| **按需独立** | 6. **Pressure test**：用户提观点 vs agent counter-take，配 prediction 记录 | 用户表达观点 |
| **按需独立** | 7. **Compare**：N 只股票横向 | 用户说 "compare A vs B" |
| **按需独立** | 8. **Find analysis**：过往分析 / 类比归因 | 用户说 "我之前怎么看" / "类似情况" |
| **按需独立** | 9. **Sector deep**：板块深度（chip / energy / AI capex 等） | 板块大动或用户问 |

**关键点**：一站式 4 块跑完就是一份完整的 daily brief。**Brief 综合**是灵魂 — 它读其他 3 块的输出，做交叉判断，串成叙事。这就是你说的"结合起来的分析和提示"。

## 默认行为（菜单每次都弹 — 你拍板的）

```
用户："今天的 report" / "today's move" / "morning"
→
agent: 这次跑哪些？
  [✓] 1. Pulse + Macro    (大盘 + 宏观 + 政策新闻)
  [✓] 2. Watchlist + Movers (持仓快照 + 异动)
  [✓] 3. Timeline 30天    (财报 / 政策窗口 / catalyst)
  [✓] 4. Brief 综合       (把以上串起来 + AI 概率判断)
  [ ] 5. Deep dive: NVDA
  [ ] 5. Deep dive: MU
  [ ] 5. Deep dive: TSLA   (今天异动股自动列出来)
  [ ] 9. Sector deep: chip selloff
  全跑 / 默认 1-4 / 自选
→ 用户勾完 → agent 并行跑 → 生成 dashboard/{date}.md → 浏览器打开
```

**关键 UX 细节**：菜单**预填合理 default** (1-4)。今天异动股 / 关注的板块作为可选 deep-dive 项自动塞进菜单。你不需要从零开始想"今天要跑啥"。

## 各模块内容详解（不死板，按需出 block）

### 1. Pulse + Macro (合并)

**不是死板"先 4 个指数再 4 个 macro"**。按今天的重点出，可能只有 3 个 block，也可能 8 个。

可能的 block：
- `kpi` — 大盘 + VIX + 10Y + DXY + WTI 一行（一定有）
- `compare` — 板块 ETF 热力（一定有）
- `callout danger/warn` — 政策 / 战争 / Fed / 监管的重大信号（**只在有信号时出**）
- `compare` — 宏观→持仓 cross-ref（持仓被什么宏观信号触及）
- `callout info` — AI 一句话定性"今天的 tape"

数据源：fetch.py + policy-pulse 的 keyword 过滤

### 2. Watchlist + Movers (合并)

不死板"先 grid 再 movers"。**今天异动的优先排前面，平静的折叠**。

可能的 block：
- `kpi` — 今日 top 3 涨 / top 3 跌（一定有）
- `compare` — 全持仓快照表：ticker / 价 / 1D / 5D / 30D / vol / 距 thesis-break / 下次 catalyst（一定有，平静股折叠后段）
- `callout warn/danger` — Trigger breach 警告（**只在 < 10% trigger 距离时出**）
- `compare` — Attribution threshold 跨过的股票（3%+ / 10%+ 5d / 1.5x vol）— **flag 给 deep-dive 候选**

### 3. Timeline 30天 — 你强调的

**这是新模块**。一个统一时间线，把所有"接下来要看的点"放一起。

| 类型 | 来源 |
|---|---|
| 财报日 | 每只 active stock 的 `state.yaml` / yfinance next_earnings |
| 产品 / launch | 手动维护 `timeline.yaml` (workspace 级) |
| 经济数据 | FOMC / CPI / NFP / PCE / GDP（固定+预定时间表） |
| 政策 deadline | 关税生效 / 法案投票 / 调查结论窗口 |
| 个股 catalyst | 调查初步声明 / lock-up 到期 / 监管裁决 / S&P 纳入 |
| 我的 prediction score_date | 来自 `attributions/index.jsonl` |

输出：一个 `timeline` 块，按日期排，每条标 type tag。
**重点高亮**：未来 7 天内的全部红色 / 14 天内的橙色 / 30 天内的灰色。

要落地这个，得新建 `timeline.yaml` (workspace 级手动维护) + `scripts/build_timeline.py` (聚合数据)。

### 4. Brief 综合 — 灵魂

**最重要的一块**。读完前 3 块的 markdown，AI 写一段叙事：

```
模板（不死板）：

**今天的故事是 {一两句 headline}**。

主因：{cause 1，引用 module 1 的 macro 信号}。
       {cause 2，引用 module 2 的具体股票动}。

对你持仓的具体影响：
- **{ticker}**：{how it's affected, distance from trigger, what to watch}
- **{ticker}**：{...}

下个关键点（按时间，引用 module 3）：
- {date}: {event} — {为什么重要，bull/bear 路径}
- {date}: {event} — {...}

AI 判断：
- Bull / Base / Bear 各多少概率
- 你最不该做的事
- 真要做事，等什么数据点
```

这里就是把你说的 **"AI 的预测 + 现在的 thesis + 重点宏观 + 异动股" 全部结合起来**。今天 Action plan / Regulatory panic / TSLA 三块的合体，就是这种 brief 写法。

### 5-9. 按需独立模块

不展开 — 它们就是当前 `deep-dive` / `compare-stocks` / `find-analysis` / `quarterly-review` 那些，**保留现有 skill，重命名 / 微改**。

## 跟现有内容的关系（保留 + 合并 + 改名）

你说"不是完全改动，现在也有很多不错的内容"。具体保留哪些：

**完全保留：**
- `attributions/index.jsonl` + `find-similar-moves` — 价格归因索引（现在 19 条，关键资产）
- `dashboard/{date}.md` + H2 auto-tabs — 文件 layout 不动
- `stocks/{T}/thesis.md` + `triggers.yaml` — 每只股票的事实源
- `find-analysis` — 散文分析查询
- `record_attribution.py` / `score_predictions.py` — 后端工具
- Prediction probability + 多场景框架（你说这个"很好"，保留）

**合并 / 改名：**
- `policy-pulse` → 并入 module 1 (Pulse + Macro)
- `check-all` + `check-stock` (grid 部分) → 并入 module 2 (Watchlist + Movers)
- `explain-move` → 重命名 `deep-dive`，作为 module 5
- `compare-stocks` → 简化并入 `deep-dive` 的 "compare mode"
- `morning` → 改为调 `/report` 内部，触发词不变

**新增：**
- `/report` — 一站式 orchestrator（弹菜单 → 并行跑 → 渲染）
- `/timeline` — module 3 实现
- `/brief` — module 4 综合写作
- `timeline.yaml` (workspace 级手动维护文件)
- `scripts/build_timeline.py`

**删除：**
- 没什么要删的。`check-all` / `check-stock` 等会被 module 2 完全覆盖，但保留 skill 文件 1-2 周作 fallback，2 周后清。

## Cross-Asset 那一块怎么办？

你说"不太清楚这个带来什么信息"— **答案：现在不做。** 因为我意识到 Cross-Asset 想做的事，**其实是 module 4 (Brief 综合) 应该做的**。把 "macro → sector mapping" / "factor exposure" 那些综合判断**塞进 brief 的叙事里**，比单开一个 tab 让用户看 4 个孤立的 grid 好得多。

如果将来真需要"系统性风险面板"那种 dashboard，再说。

## File layout（不变）

```
dashboard/
  YYYY-MM-DD.md     一个文件一天
    ## Pulse & Macro
    ## Watchlist & Movers
    ## Timeline 30d
    ## Brief
    ## Deep Dive: NVDA          (按需)
    ## Sector deep: chip selloff (按需)

.skills/
  report/                NEW  — orchestrator
  pulse/                 NEW  — module 1（吸收 policy-pulse）
  watchlist/             NEW  — module 2（吸收 check-all + check-stock grid）
  timeline/              NEW  — module 3
  brief/                 NEW  — module 4 综合
  deep-dive/             改名自 explain-move
  compare/               改名自 compare-stocks
  # Pressure-test handled inline by /report when user expresses a view — no dedicated skill
  find-analysis/         保留
  find-similar-moves/    保留
  sector-deep/           NEW  — module 9 (按需)
  morning/               保留（内部调 /report）
  add-stock/             保留
  add-tracker/           保留
  deactivate-stock/      保留
  refresh-thesis/        保留
  quarterly-review/      保留
  update-thesis/         保留
  weekly-review/         保留
  check-triggers/        保留（被 watchlist 内部调）
  digest/                保留
```

## 实现顺序

1. **timeline.yaml + build_timeline.py + /timeline skill** — module 3 (新东西，先打基础)
2. **/pulse + /watchlist** — module 1 + 2（合并现有的）
3. **/brief** — module 4 (依赖 1-3 的输出)
4. **/report 编排器 + 菜单** — 一站式入口
5. **/deep-dive** — 改名 explain-move
6. **/compare + /pressure-test + /sector-deep** — 按需模块

**MVP**: 1 + 2 + 3 + 4 + report (orchestrator)。一周内能用上。

剩下的按需模块就是重命名 / 微改现有 skill，工作量低。

## 开放问题（最后 2 个，定了就开工）

1. **Timeline.yaml 怎么填？** 第一次填我可以基于 (a) 你 active stocks 的 yfinance earnings dates、(b) 已知 catalyst（SPCX lock-up 12/9 / TSLA NHTSA / SPCX F-1 / MU Q3 / FOMC 全年表）填好初版。**之后你手动 append**。同意？

2. **菜单触发词**：你已经定了"每次弹菜单"。但 `/morning` 应该有菜单还是直接全跑？我建议 `/morning` 是 session-opener，**全跑不弹菜单**（你早上就是要快速看完）；`/report` 弹菜单（精挑细选）。同意？
