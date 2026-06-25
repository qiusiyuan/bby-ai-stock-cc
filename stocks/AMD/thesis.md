# AMD — Advanced Micro Devices

## One-line thesis
AMD is the only credible alternative GPU/CPU vendor at scale for AI workloads, and its multi-year share-gain story in data center continues to compound — *this thesis is wrong if* AMD's MI-series GPUs fail to close the software ecosystem gap with CUDA, Nvidia retains >85% AI accelerator share through 2027, or AMD's gross margin trajectory deteriorates materially as it pursues lower-margin hyperscaler custom silicon.

## Snapshot
Semiconductors · NASDAQ · ~$876B cap · $537 (2026-06-18) · up 280% YTD · 52w range $126.82–$558.37

## What it does
AMD designs CPUs and GPUs sold into data centers, client PCs, gaming consoles, and embedded systems. Its three segments are Data Center (EPYC server CPUs + MI-series AI accelerators), Client & Gaming (Ryzen consumer CPUs/GPUs + semi-custom SoCs for PlayStation and Xbox), and Embedded (FPGAs/adaptive SoCs from the 2022 Xilinx acquisition). The company fabless — TSMC manufactures all leading-edge parts.

## Industry & TAM
The AI accelerator market alone is projected to reach $150–200B by 2028; Nvidia currently holds ~80–85% share. AMD's EPYC CPUs have already taken ~25–30% of server CPU market from Intel, demonstrating it can execute long-cycle share gains. The hyperscaler GPU TAM (Meta, Microsoft, Google, Amazon) is the primary battlefield — AMD's MI300X is the only currently shipping alternative at meaningful scale. FPGA/adaptive SoC market (legacy Xilinx) is a separate but durable segment (~$5–7B/yr) with sticky defense and communications customers.

## Why I'm watching
The CUDA moat is real but not absolute. Every hyperscaler is spending heavily to qualify AMD and build software abstraction layers (ROCm, JAX backends, PyTorch XLA) to reduce Nvidia dependence. AMD is the only semiconductor company with a competitive offering in both CPUs (EPYC) and GPUs (MI-series) simultaneously — a combination that matters for HPC and inference workloads. The Rackspace 30 MW agreement (June 2026) and Bernstein's CPU-AI note indicate the conviction is spreading beyond the usual GPU narrative.

## Outlook — Bull / Base / Bear
- **Bull (30%)**: MI300X/MI400 gain 20%+ of hyperscaler GPU spend by end-2027; ROCm software ecosystem narrows the CUDA gap; EPYC continues winning server CPU share; Data Center revenue reaches $40B+ in FY27. Target $700+.
- **Base (45%)**: AMD holds 10–15% of AI accelerator market; EPYC stable; Embedded segment recovers from inventory correction by late 2026; data center grows 35–40% CAGR. Target $550–600.
- **Bear (25%)**: CUDA moat proves impenetrable, AMD GPU share stalls below 10%; gross margin compression from chasing hyperscaler custom-silicon at lower margins; Embedded stays depressed through 2027; Intel re-accelerates with Gaudi. Target $300 or below.

## Moat
AMD's moat is narrower than Nvidia's but real and widening. **Process power**: AMD's chiplet architecture (pioneered internally, now copied by Intel) enables leading-edge compute density at cost. **Scale economies**: being the #2 AI GPU vendor matters — hyperscalers need a second source, and AMD is the only qualified one. **Switching costs** in CPUs are meaningful once racks are populated with EPYC; ripping out a data center architecture mid-cycle is expensive. The **weak spot** is software: CUDA has a decade-long head start, and ROCm still lags in coverage of ML frameworks, particularly for model training. AMD's MEXT acquisition (June 2026, memory optimization AI) signals awareness that winning in inference requires more than hardware. Branding in AI chips is Nvidia's — AMD remains the "alternative," not the default.

## Management & capital allocation
Lisa Su has been CEO since 2014 and is widely credited with engineering AMD's turnaround from near-bankruptcy to a top-10 semiconductor company. Her capital allocation record is excellent: the Xilinx acquisition ($49B, 2022) was initially controversial but has delivered durable cash flows from the Embedded segment. ROIC has improved substantially over the past five years. The MEXT acquisition is small and strategically coherent. Share buybacks have been opportunistic and measured. The main concern is whether AMD can execute on the software side — hardware wins without ROCm maturity are incomplete.

## Valuation
- **Multiples**: At $537, trailing P/E is 180× (depressed earnings base from prior-cycle lows), but forward P/E of 41× reflects rapid earnings recovery. Market cap ~$876B on ~$26–28B estimated FY2025 revenue.
- **Reverse-DCF**: At $537, the market is pricing in roughly **30–35% revenue CAGR over the next 5 years with operating margin expanding to 30%+**. That is achievable under the base case — AMD has demonstrated the ability to execute on multi-year ramps (EPYC from 2–3% to 25%+ server CPU share). The stock is not cheap, but it is not pricing in an outright bull scenario the way NVDA did at peak — there is some margin of safety baked in via the forward multiple. The recent 280% YTD run and one analyst warning about "risen too far, too fast" signals near-term risk of a pullback if next earnings disappoint.
- **Gross margin watch**: The Trefis note about AMD going "quiet" on gross margin is the single most important valuation risk. If AMD is pursuing hyperscaler custom silicon (like Trainium for Amazon) at structurally lower margins, the earnings power story changes. This needs monitoring at next earnings (2026-08-04).

## Balance sheet
Healthy. AMD carries moderate debt from the Xilinx deal but has substantially delevered. Free cash flow generation has been strong as EPYC gains scale. No balance-sheet stress risk at current trajectory.

## Key metrics to watch
- **Data Center revenue YoY growth** (was the primary driver of 2024–2026 re-rate; any decel matters)
- **MI300X/MI400 shipment volumes and hyperscaler customer disclosures** (qualitative, from earnings calls)
- **Gross margin trajectory** (target 50%+; any compression below 48% is a concern)
- **ROCm ecosystem maturity** (watch developer adoption, framework coverage parity with CUDA)
- **Embedded segment recovery** (was in inventory correction; return to growth expected H2 2026)
- **EPYC server CPU market share** (proxy: Intel data center CPU share trend, reported quarterly)

## Catalysts (next 12 months)
- **2026-08-04**: Q2 2026 earnings — first major read on MI400 ramp and gross margin trajectory
- **H2 2026**: MI400 (CDNA4) volume shipments to hyperscalers
- **Late 2026**: Embedded segment recovery confirmation
- **2026–2027**: ROCm 7.x major release targeting CUDA parity in key training frameworks
- **Ongoing**: Rackspace 30 MW AMD-based deployment start (late 2026)

## Disconfirming events (would make me sell)
- Gross margin drops below 48% for two consecutive quarters, signaling structural mix shift to low-margin custom silicon
- Hyperscaler customers publicly confirm Nvidia-only GPU procurement for 2027 cycle
- ROCm fails to achieve meaningful parity with CUDA in primary training frameworks (PyTorch, JAX) by end-2027
- EPYC server CPU share growth stalls or reverses, signaling Intel Granite Rapids/Diamond Rapids competitive recovery
- Data Center revenue growth decelerates below 25% YoY for two consecutive quarters

## Position
- Target: $580 (base case)
- Thesis-break level: $380 (~30% below current; significant and would force a re-read)
- Current weight vs max: TBD — set on first add to portfolio

## Stands & Updates

_No entries yet._
