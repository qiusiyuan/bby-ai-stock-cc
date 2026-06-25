# MU — 业务结构与长期决策框架

> **Research note** · 2026-06-23 · 长期 sizing 用，非每日分析
> 涵盖: 业务 segment / 客户名单 / 产能 / 结算机制 / 历史财务 / 5 年场景
> 下次 review: 2026-09-23 (3 个月后) 或下次 thesis-break 触发


```callout info
这一节是为了让你**绕过 24 小时 trading noise，做长期 sizing 决策**。覆盖：业务结构 → 客户 → 产能 → 结算机制 → 历史数据 → 关键判断点。读这一节再读财报预期。
```

### 业务结构 — 钱从哪里来

**4 个 reporting segment**（按 FY2025 营收 $37.4B 计）：

```compare
| Segment | 占比 (估) | 主要产品 | 主要客户类型 | HBM 在哪
| Compute & Networking (CNBU) | ~45% | DC DRAM / HBM / GDDR | NVIDIA / AMD / Hyperscaler | ✓ HBM 在这里
| Mobile (MBU) | ~22% | LPDDR | Apple / 三星 / 小米 / 联发科 | ✗
| Storage (SBU) | ~18% | NAND / SSD / 企业 SSD | AWS / Hyperscaler / 企业 | ✗
| Embedded (EBU) | ~15% | 汽车 DRAM / 工控 | Auto OEM / 工业 | ✗
```

**产品维度**：DRAM ~60% / NAND ~40%；但 HBM 是 DRAM 内增速最快、毛利最高的小类。**HBM 单价是普通 DDR5 的 3-5 倍。**

### 谁是 MU 的买家 — 已知客户名单

```compare
| 客户 | 产品 | 已知关系 | 公开消息
| **NVIDIA** | HBM3E / GDDR6X | Blackwell GPU 内存供应商之一 | 2024-02 HBM3E 通过 qualification；Q3 FY2024 起出货
| **AMD** | HBM3 / HBM4 | Instinct MI300/350 系列 | MI430X 是首款用 HBM4 的 GPU
| **Apple** | LPDDR | iPhone / iPad / Mac (10+ 年长期供应商) | 通过 Elpida 收购后入选 Apple 供应链；Tim Cook 6/18 暗示 memory 价格 "unavoidable" hikes
| **Anthropic** | HBM (估) | 2026-06 战略协议 | 6/22 公布 — MU 当日 +5.26%；具体金额未披露
| **Hyperscalers (AWS / Google / Microsoft / Meta)** | DC DRAM / SSD / HBM | 多年伙伴 | 没有公开 multi-year 合同金额；典型走 quarterly purchase orders
| **Samsung / Apple (NAND)** | NAND | 通过 LTAs | 部分长协；spot 部分占 ~30-40%
| **PC OEM (Dell, HP, Lenovo)** | PC DRAM | 长期 | spot + 季度合约混合
| **汽车 OEM (Tesla, Ford, GM, 等)** | Auto-grade DRAM | 多年规格锁定 | 长期价 vs 季度调价混合
```

**最重要事实**: **NVIDIA / AMD / AWS / Google 没有任何"已公布金额"的长期合同公开** —— hyperscaler 不喜欢锁定价格，因为内存周期性强。这意味着**MU 财报"未来订单"披露大部分是 management guidance + qualitative**，不是 backlog 硬数字。这是判断财报的关键。

### 产能 — 物理供给

```compare
| 设施 | 投资 | 主要产品 | 状态 | 上线
| Boise, Idaho | $15B+ (CHIPS Act 受益) | 新 DRAM/HBM 厂 | 在建 | 首产 2026-2027
| Clay, New York | $100B (20 年计划) | 大型 DRAM 复合体 | 早期阶段 | 首产 2028+
| Singapore (Manyung) | $24B 追加 (2026-01) | NAND 扩产 +700k sqft cleanroom | 在建 | 2027 上线
| Taichung (台湾) | 现有 | DRAM 主产能 | 满产 | —
| Hiroshima (日本) | 现有 | DRAM | 满产 | —
| Xi'an (中国) | 现有 | NAND 后段封测 | 缩减 | —
```

**关键洞察 — 物理供给的硬天花板**：
- 当前 HBM 产能（Hynix + Samsung + MU 加总）**远小于 NVIDIA 需求**，导致 +200% 涨价（2025 早期到 2026）
- **3:1 HBM:DDR5 wafer 换算比** — 每多生产 1 单位 HBM，挤掉 3 单位 commodity DRAM 产能 → **HBM 涨价 + DRAM 间接紧缺**两个效应叠加
- MU 的 HBM 市占 ~15%（vs SK Hynix ~50%、Samsung ~35%）但**增速最快** —— 目标 2026 底到 25-30%
- 物理产能 lead time **18-24 个月**，所以 MU 现在的资本投入决定 2027-2028 的 HBM 收入

### 结算机制 — 钱怎么进来

```compare
| 客户类型 | 价格机制 | 现金周期 | 风险
| Hyperscaler DC DRAM | 季度合约 + 部分 spot | DSO ~30-45 天 | 价格随 spot 调整, downturn 时痛苦
| Hyperscaler HBM | **半固定 / 长期协议** | DSO ~45-60 天 | 当前**HBM 量是瓶颈，价格固定 12+ 个月**
| Apple LPDDR | 多年价格协议 (renegotiated annually) | DSO ~60 天 | Apple 议价权极强
| Auto-grade DRAM | 长期合约 (2-5 年) | DSO ~75-90 天 | 量低但稳，毛利率不错
| PC OEM DRAM | spot + 季度 | DSO ~45 天 | 完全周期性
| 通过 distributors | 季度合约 + spot | DSO ~30 天 | 风险传递给 distributors
```

**关键判读**：
- HBM 现在是**半固定价格 12 个月**（因为供给紧）—— 这是 bull 案的底层数学：MU 的 HBM 收入有 12 个月的可见性
- Commodity DRAM 完全 spot 化 —— **PC / mobile DRAM 价格 indices 是 MU EPS 最直接的领先指标**
- DSO 总体 30-60 天 —— MU 是**正现金流业务**（与设备制造商不同）

### 历史财务 — 周期性必须看懂

```compare
| FY | 营收 | 净利 | 营业利润 | 周期阶段
| 2021 | $27.7B | $5.9B | $6.8B | 上行
| 2022 | $30.8B | $8.7B | $9.7B | **周期峰**
| 2023 | $15.5B | **-$5.8B** | **-$3.6B** | **周期谷** (-50% 营收)
| 2024 | $25.1B | $0.8B | $1.3B | 复苏
| 2025 | $37.4B | $8.5B | $9.8B | **新峰** (远超 2022)
| FY2026 Q2 (3 月) | $23.86B/Q | $13.8B (累计) | EPS $12.20 | 单季度
```

**关键观察**:
1. **MU 是真正的周期股** — 2023 单年净亏 $5.8B，从 2022 高点 -50% 营收
2. **FY2025 营收 $37.4B 已超过 2022 峰值 $30.8B** —— 因为 HBM 加入营收结构
3. **FY2026 Q2 单季营收 $23.86B (累计) 意味着年化 $50B+** —— 如果延续，FY2026 全年可能 **$55-65B**
4. **历史毛利率波动**: 谷底 (-7%) → 峰值 (~58%)。当前 58.44% 是**周期顶**

### 估值参考

```compare
| 指标 | 当前 | 周期峰均值 | 周期均值 | 周期谷
| Trailing P/E | 49.4× | 周期峰看 forward 更准 | ~15× | NM (亏损)
| Forward P/E (10× consensus) | 10× | 8-12× | ~12× | NM
| P/Book | 17.65× | ~5-7× | ~3× | ~1.5-2×
| ROE | 39.8% | 30-40% | ~15% | <0%
| 营业现金流 (FY2025) | $17.5B | — | ~$8B | <0
| Capex (FY2025) | ~$14B | — | ~$10B | $5-8B
| 自由现金流 (FY2025) | **-$0.9B** | 应为正 | ~$0 | <0
```

**最关键的数字**: FY2025 营收 $37.4B + 净利 $8.5B 但 **FCF -$0.9B** —— 公司**全部利润再投到产能扩张**。这是**经典周期顶投资模式**：业绩好的时候疯狂建厂，建厂完成时通常正赶上下行周期。这就是为什么 MU 历史上是 "stock 涨 5x 后跌 70%" 的剧本。

### 长期判断框架 — 你做 sizing 决策需要回答的 6 个问题

```meter
1. HBM 是否真的"结构性不同" (而非周期性炒作) | ? | 关键判断：3:1 wafer 换算 + AI capex 12-18 月 lead time
2. MU 能否把 HBM 市占从 15% 提到 25%+ | ? | 取决于 HBM4 yield；Samsung 反扑是最大威胁
3. CommodityDRAM 在 2026-2027 会不会崩 | ? | PC/mobile pricing 是领先指标
4. HBM 价格能否维持 +200% 溢价超 18 个月 | ? | 一旦产能跟上，单价会大跌
5. Apple 在 LPDDR 上的议价权变化 | ? | iPhone 销量决定 MU 22% 营收
6. CHIPS Act 资金到位节奏 | ? | 影响 Idaho/NY 产能上线
```

### 真正决定长期 thesis 的 3 个事件

```timeline
2026-06-24 🔥 | MU Q3 财报 — 第一次披露 HBM 营收硬数字 (此前都是 management guidance)
2026-08-26 ⚠ | NVDA Q2 FY2027 — Blackwell 出货量披露 = MU HBM 真实需求
2027-Q1 ▢ | HBM4 量产 — Samsung 反扑 vs Micron 维持的关键节点
```

### 我给你的具体长期判断（基于以上数据）

**HBM 故事的"硬度"评估**：
- ✅ **物理层硬**: 3:1 wafer 换算是真的，TSV stacking 工艺难，产能 lead time 18-24 月
- ✅ **需求侧硬**: NVIDIA Blackwell + AMD MI400 + 推理负载启动 = 多个 leg
- ⚠ **市占争夺软**: MU 15% 想到 25%+ 是 fragile，Samsung 反扑会决定 2027+
- ⚠ **价格弹性软**: +200% 涨价无法持续 18+ 月

**MU 在 5 年时间窗内的合理 thesis**：
1. **如果 HBM 真是结构性 + MU 保住 20%+ 市占** → 2027-2028 年化营收 $50-60B + 毛利率 55%+ → 公允估值 $1,200-1,500 区间长期成立
2. **如果 HBM 是 2-3 年急涨周期 + Samsung 反扑成功** → 营收下行至 $35-40B, 毛利率回到 35% → 公允估值 $500-700
3. **概率分布个人判断**: 1 概率 50% / 2 概率 35% / 其他 (黑天鹅) 15%

**当前 $1,051 隐含什么**：基本 pricing-in 上述场景 1 的 50-60% 概率。这意味着 **如果你 strongly 相信 HBM 是结构性，当前价合理偏低；如果你认为 50/50，当前价合理；如果你认为 HBM 是周期性炒作，当前价高估 30-40%**。

**最重要事实 — 财报后判断**：明天财报 **HBM 营收** 这一个数字相对于一年前同期的同比增速，是判断"结构性 vs 周期性"的关键。$2.5B+ 同比 +150%+ = 结构性；$2B 同比 +80% = 周期性减速。
