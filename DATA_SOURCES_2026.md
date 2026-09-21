# Recent Funding Sources (2024–2026)

The original project dataset covered 2015–2020. On 2026-09-21, a curated recent-funding layer was added so the analyser reflects more of the current Indian startup ecosystem.

## Data method

- Historical rows are preserved unchanged.
- Recent rows are based on company announcements or reputable business/technology reporting.
- The legacy dashboard expects the `amount` column in INR crore.
- When a source reports only USD, the original value is retained in `source_amount` and `source_currency`, while `amount` contains an approximate INR-crore conversion for compatibility with the existing charts.
- Conversion assumptions used only for those compatibility values: ₹83.5/USD for 2024, ₹86/USD for 2025, and ₹94.4/USD for 2026.
- Rows where the source directly reports rupees are labelled `Reported INR crore`.
- Every new row includes `source_url` and `verified_as_of`.

## Current layer

| Date | Startup | Round | Reported amount | Key investors |
| --- | --- | --- | --- | --- |
| 2026-09-07 | Pixxel | Series C | $100M | Temasek, Seraphim, 360 ONE Asset, IMM Investment, Radical Ventures, growX ventures, M&G Catalyst |
| 2026-07-15 | Ather Energy | Preferential Issue | ₹1,200 Cr | Hero MotoCorp, India-Japan Fund, founders |
| 2026-06-15 | Sarvam AI | Series B first close | $234M / ~₹2,210 Cr | HCLTech, Bessemer Venture Partners, Khosla Ventures, Peak XV Partners |
| 2026-05-21 | Scapia | Series C | $63M | General Catalyst, Peak XV Partners, Z47 |
| 2026-05-15 | Rapido | Late-stage equity | $240M | Prosus, WestBridge Capital, Accel |
| 2026-01-23 | Juspay | Series D follow-on | $50M | WestBridge Capital |
| 2025-09-18 | Infra.Market | Pre-IPO funding | ₹732 Cr | NKSquared, Tiger Global, Accel India, founders and existing shareholders |
| 2025-06-13 | Spinny | Series F extension | ~ $170M | Accel Leaders Fund, WestBridge Capital, Elevation Capital, Think Investments, Tiger Global, Fundamentum |
| 2025-05-08 | Porter | Series F | $200M | Kedaara Capital, Wellington Management, Vitruvian Partners |
| 2025-04-07 | Juspay | Series D | $60M | Kedaara Capital, SoftBank, Accel |
| 2025-03-05 | Darwinbox | Growth investment | $140M | Partners Group, KKR, Gravity Holdings |
| 2025-01-23 | Infra.Market | Pre-IPO funding | ₹1,050 Cr | Tiger Global, Foundamental, Evolvence, Nikhil Kamath, others |
| 2024-11-21 | Zepto | Late-stage equity | $350M | Motilal Oswal and Indian family offices |
| 2024-09-20 | PhysicsWallah | Series B | $210M | Hornbill Capital, Lightspeed, GSV Ventures, WestBridge |
| 2024-08-29 | Zepto | Late-stage equity | $340M | General Catalyst, Dragon Fund, Epiq Capital, existing investors |

The CSV contains the source link for every one of these records.
