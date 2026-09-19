# Startup Funding Analysis

An interactive Streamlit dashboard for exploring startup funding data.

## What it does

The app reads startup funding records from `startup_cleaned.csv` and provides multiple ways to explore the dataset.

### Overall analysis

- Total funding amount
- Maximum funding received
- Average funding per startup
- Number of funded startups
- Month-over-month funding trends
- Funding count trends

### Investor analysis

- Recent investments
- Biggest investments
- Sector-wise investment distribution
- Year-over-year investment activity

The repository also contains `devik.py`, a Streamlit learning playground used to experiment with widgets, layouts, forms, file uploads, progress indicators, media, and other Streamlit components.

## Tech stack

- Python
- Streamlit
- Pandas
- Matplotlib

## Run locally

```bash
git clone https://github.com/divbytes-prog/03.git
cd 03
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
