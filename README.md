# Startup Funding Analyser

An interactive Streamlit dashboard for exploring startup funding data, funding trends, and investor activity.

**Live dashboard:** [startup-funding-analyser.vercel.app](https://startup-funding-analyser.vercel.app/)

The repository includes both the original Streamlit analysis and a responsive browser version used for the Vercel production deployment.

## Features

### Overall analysis

- Total funding amount
- Maximum funding received
- Average funding per startup
- Number of funded startups
- Month-over-month funding trends
- Funding-count trends

### Investor analysis

- Investor filter ordered by the combined value of funding rounds in which each investor appears
- Recent investments
- Biggest investments
- Sector-wise investment distribution
- Year-over-year investment activity

The dataset lists round totals and participant names, but does not disclose how much each investor contributed. The investor ordering therefore sums the **full round value** for every named participant; it is a measure of associated funding, not an estimate of an investor's own check sizes. Name variants beyond letter case may remain separate. A misrecorded Rapido Series B outlier was corrected to approximately ₹391 crore, with a source URL preserved in `startup_cleaned.csv`.

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
