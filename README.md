# Startup Funding Analyser

An interactive Streamlit dashboard for exploring startup funding data, funding trends, and investor activity.

**Live dashboard:** [startup-funding-analyser.vercel.app](https://startup-funding-analyser.vercel.app/)

The repository includes both the original Streamlit analysis and a responsive browser version used for the Vercel production deployment.

## Data freshness

The original dataset covered 2015–2020. It now includes a curated, source-backed set of major Indian startup funding rounds from 2021–2026 so the live analyser includes current companies and investors such as Pixxel, Sarvam AI, Rapido, Scapia, Juspay, Porter, Darwinbox, Infra.Market, PhysicsWallah and Zepto.

Recent rows include source metadata in the CSV. See `DATA_SOURCES_2026.md` for methodology and provenance.

## Features

### Overall analysis

- Total funding amount
- Maximum funding received
- Average funding per startup
- Number of funded startups
- Month-over-month funding trends
- Funding-count trends

### Investor analysis

- Recent investments
- Biggest investments
- Sector-wise investment distribution
- Year-over-year investment activity

The repository also includes `devik.py`, which was used as a Streamlit experimentation file while learning widgets, layouts, forms, uploads, progress indicators, and media components.

## Tech stack

- Python
- Streamlit
- Pandas
- Matplotlib

## Run locally

```bash
git clone https://github.com/divbytes-prog/startup-funding-analyser.git
cd startup-funding-analyser
pip install streamlit pandas matplotlib
streamlit run app.py
```

## Main files

```text
app.py                 Main startup-funding dashboard
devik.py               Streamlit experimentation file
index.html              Vercel-ready interactive dashboard
startup_cleaned.csv    Cleaned dataset used by the dashboard
startup_funding.csv    Original funding dataset
vercel.json             Production hosting configuration
```

---

Built by [Divyansh Singh](https://github.com/divbytes-prog).

## Interpretation and limitations

The historical dataset covers 2015–2020. There are 23 selected source-linked rounds from 2021–2023 and 15 from 2024–2026. The additions are a curated sample, not a complete market record. The newer rows preserve source URLs, reported amounts and currencies, and approximate INR-crore conversions. Most historical rows lack that source metadata.
