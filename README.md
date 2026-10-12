# Startup Funding Analyser

An interactive Streamlit dashboard for exploring startup funding data, funding trends, and investor activity.

**Live dashboard:** [startup-funding-analyser.vercel.app](https://startup-funding-analyser.vercel.app/)

The repository includes both the original Streamlit analysis and a responsive browser version used for the Vercel production deployment.

## Data freshness

The original dataset covered 2015–2020. It now includes a curated, source-backed set of major Indian startup funding rounds from 2024–2026 so the live analyser includes current companies and investors such as Pixxel, Sarvam AI, Rapido, Scapia, Juspay, Porter, Darwinbox, Infra.Market, PhysicsWallah and Zepto.

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
\n## Interpretation and limitations\n\nThe historical dataset covers 2015–2020. Only 15 curated source-linked rows\nwere added for 2024–2026; 2021–2023 are missing, not zero-funding years.\nThe newer rows preserve source URLs, reported amounts/currencies, and any\napproximate INR-crore conversion. Most historical rows do not have that source\nmetadata. The live website includes year, investor, and startup searches,\nclear empty states, and source links for the recent rows. The original\nStreamlit app now displays startup details and matches investor names by\ncomma-separated entry rather than a substring. The displayed funding\nanalysis describes this dataset and is not a complete market estimate.\n