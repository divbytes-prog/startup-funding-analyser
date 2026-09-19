# Startup Funding Analyser

An interactive Streamlit dashboard for exploring startup funding data, funding trends, and investor activity.

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
startup_cleaned.csv    Cleaned dataset used by the dashboard
startup_funding.csv    Original funding dataset
```

---

Built by [Divyansh Singh](https://github.com/divbytes-prog).
