# SKHY attributions

Append-only log of meaningful price moves with cited causes. Companion to the JSONL index at `../../attributions/index.jsonl`.

---

### 2026-07-31 · -0.60% day · ▼ minor
**Tags:** `thesis_debate`, `flow_event`, `lockup_expiry`, `sector_rotation`
**Confidence:** high

**Primary cause.** CORRECTION of a same-day workspace error. The daily report claimed SKHY trades at a DISCOUNT to the Korea line and might be 'the cheapest entry in the memory cluster'. SEC 424B4 confirms 1 ADS = 1/10 common share; correctly computed, SKHY trades at a persistent ~+30% PREMIUM (14/14 sessions lag-corrected, mean +32.3%). Direction of the original conclusion was inverted.

**Sources.**
- {"type": "filing", "title": "SK hynix Inc. 424B4 final prospectus (priced 2026-07-09 at $149.00/ADS)", "publisher": "SEC EDGAR CIK 0002120882", "url": "https://www.sec.gov/Archives/edgar/data/2120882/000119312526299963/d32785d424b4.htm", "note": "Quote: 'Each ADS represents one-tenth of a common share.' Also: 90-day lockup from prospectus date (expiry ~2026-10-07); 100% primary issuance, shares 711,075,500 -> 728,865,500; SK square bound by Korean Monopoly Regulation and Fair Trade Act 20% ownership floor; cornerstone investors Baillie Gifford Overseas, Coatue funds, Situational Awareness Partners LP for up to $7B, explicitly 'not binding agreements or commitments to purchase'."}
- _Corroboration:_ Three independent metrics agree SKHY is the expensive line: fwd P/E 4.39x vs Korea 3.84x (+14.4%); implied mktcap $1,045B vs $845B (+23.6%); price vs NAV/ADS $147.11 vs $119.06 (+23.6%). Timezone-lag correction (Korea closes 06:30 UTC, 13.5h BEFORE US 20:00 UTC) also refutes the 'decoupling' claim: SKHY rose +17.5% on 7/30 ($126.79->$149.00) and Korea caught up +30% on 7/31 — Korea followed the US, it did not decouple.
- Quartz: [Leopold Aschenbrenner's AI hedge fund collapses after margin calls — peaked at $45B, forced to sell leveraged AI infrastructure bets to Citadel at a discount](https://qz.com/situational-awareness-hedge-fund-margin-call-citadel-fire-sale-073126)

**Cross-assets.** SECTOR ETF +1.50% · SPY +0.58% · VIX 16.58 · 10Y 4.74 · WTI 84.97

**Agent read.** Process lesson outweighs the finding: ANY cross-market comparison must verify the ADS/ADR ratio FIRST — one SEC lookup. I published an investment implication built on an unverified ratio, and TWO independent refutations were already in hand and missed: (a) fwd P/E 4.39x vs 3.84x directly says SKHY is 14.4% MORE expensive — I read it as 'close', (b) Korea's session closes BEFORE the US, so a same-day divergence is a timing artifact, not decoupling. Substantive conclusions: premium is structural (2.44% float + one-way deposit friction per the prospectus warning that surrendered ADSs may not be re-deposited), so it likely does NOT converge. The lockup hypothesis is inapplicable — 100% primary, no selling shareholders, and SK square's constraint is a PERMANENT Korean 20% statutory floor, not a 90-day contract. Cheapest memory entry is the Korea line (3.84x); within US-accessible names MU (5.42x) is the cheapest with no better substitute. New independent edge for MU: it reports 2026-09-23 vs SK Hynix/Samsung 10/26-27 — MU adjudicates the peak-vs-mid-cycle question a full month before the rest of the cluster. Open risk: if Situational Awareness holds SKHY, a forced liquidator in a 2.44%-float name is severe supply — plausibly the real cause of SKHY's 7/27-7/29 -18% AND the sector-wide 'no company-specific bombshell' semi crash. Unconfirmable: cornerstone indications were non-binding. Data gaps: 424B4 Underwriting p.176 and Shares Eligible for Future Sale p.151 truncated, so the restricted-party list is unverified; no historical baseline for Korean ADR premium levels.


---
