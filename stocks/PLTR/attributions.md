# PLTR attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-08-04 · +30.23% day · ▲ extreme
**Tags:** `earnings_print`, `guidance_raise`, `ai_demand`, `executive_comment`, `sector_rotation`
**Confidence:** high

**Primary cause.** CORRECTION AND EXPANSION of the earlier 2026-08-04 PLTR entry. Two fixes. (1) Valuation anchor: the widely quoted '42x revenue' is the FORWARD price-to-sales ratio. Trailing P/S is 87x ($391B market cap divided by FY2025 revenue of $44.8B, per Wikipedia-sourced financials). The 42x figure implies revenue rising from $44.8B to roughly $93B. Both are correct but 87x trailing is the more conservative and more relevant anchor - the stock is MORE expensive than the earlier entry implied, not less. (2) Business model verified against primary sources rather than assumed: PLTR does NOT train foundation models. It is pure software - a 2003-founded data integration company that added an LLM layer (AIP) only in 2023.

**Sources.**
- _Data:_ Wikipedia (Palantir Technologies): FY2025 revenue $4.48B... corrected: $4.48B is quarterly-scale misread; article states 2025 revenue $4.48B and net income $1.63B. Segment split 2024: Government $2.4B (53.7%), Commercial $2.07B (46.3%). Employees 4,429 (2025). (https://en.wikipedia.org/wiki/Palantir_Technologies)
- _Data:_ AIP integrates THIRD-PARTY large language models into privately operated networks; users build configurable agents via GUI connected to an organizational 'ontology'. NATO Maven Smart System is compatible with any AI system including Meta's and Mistral's. Palantir primarily integrates existing models rather than building foundation models. (https://en.wikipedia.org/wiki/Palantir_Technologies)
- _Data:_ Exception to the no-training rule: Brave1 Dataroom with Ukraine's Ministry of Defense, where ~100 companies use battlefield data to train 80+ AI models. Palantir supplies the platform, not the models. (https://en.wikipedia.org/wiki/Palantir_Technologies)
- Motley Fool: [Palantir Just Guided to 134% U.S. Commercial Growth. After a 15% Pop, the Stock Costs 42 Times Revenue.](https://www.fool.com/)

**Cross-assets.** SPY +2.02% · VIX 16.34 · TEN YEAR 4.627 · WTI 75.82

**Agent read.** Two corrections to preserve, both of which matter for how this event is reused later. FIRST, the valuation anchor is worse than first recorded: 87x trailing P/S, not 42x. Even under three consecutive years of revenue doubling ($44.8B to $358B) the multiple only compresses to about 11x; reaching a normal software 10x requires roughly 9x revenue growth. This strengthens rather than weakens the original conclusion that the information value of the print is high while the instrument attractiveness is poor. SECOND, and more useful structurally: PLTR occupies the LAST MILE of the AI value chain and competes with nothing in this portfolio. It does not train models - AIP wires third-party LLMs into private networks, and NATO's Maven is explicitly model-agnostic across Meta and Mistral. Its actual moat is the 'ontology' layer that maps enterprise business entities into a digital representation, because an LLM has no idea what a specific bank means by an 'order'. Calling an API is commodity work; connecting a model to twenty years of an enterprise's dirty data is the paid work. Chain position: chips/memory (NVDA MU AVGO MRVL AMD TSM) then cloud (AMZN MSFT GOOG) then models (OpenAI Anthropic) then ontology/deployment (PLTR, partially SNOW) then enterprise customers. PLTR is therefore a DOWNSTREAM CREATOR of compute demand, which is exactly why its print is bullish read-through for upstream holdings rather than competitive news. THIRD RISK worth logging for future reference: government revenue is 53.7% of the total, and government contracts are lumpy, opaque in procurement timing, highly concentrated, and politically exposed (ICE contracts, IDF partnership, non-competitive procurement criticism). Applying a SaaS multiple of 87x trailing revenue to a company deriving half its revenue from defense procurement is the central valuation dispute on this name, and any future reverse-DCF must model the two segments separately rather than blending them.
 · Snapshot at `dashboard/2026-08-04.md`

---
