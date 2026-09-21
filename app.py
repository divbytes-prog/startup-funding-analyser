import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Startup Funding Analyser",
    page_icon="📈",
    layout="wide",
)

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&family=Playfair+Display:wght@500;600&display=swap');

      .stApp {
        background: #f3efe7;
        color: #171512;
        font-family: 'Outfit', sans-serif;
      }

      [data-testid="stSidebar"] {
        background: #171512;
        border-right: 1px solid #2e2a25;
      }

      [data-testid="stSidebar"] * {
        color: #f4efe7;
      }

      [data-testid="stSidebar"] label,
      [data-testid="stSidebar"] p {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.72rem;
        letter-spacing: 0.05em;
      }

      h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        letter-spacing: -0.025em;
        color: #171512 !important;
      }

      h1 {
        font-size: clamp(2.8rem, 7vw, 5.7rem) !important;
        line-height: 0.95 !important;
        font-weight: 500 !important;
      }

      [data-testid="stMetric"] {
        background: #fbfaf7;
        border: 1px solid #d8d0c5;
        padding: 1.2rem 1.25rem;
      }

      [data-testid="stMetricLabel"] {
        font-family: 'IBM Plex Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #716a61;
      }

      [data-testid="stMetricValue"] {
        font-family: 'Playfair Display', serif;
        color: #171512;
      }

      .block-container {
        max-width: 1450px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
      }

      .editorial-kicker {
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: #8c6a2d;
        margin-bottom: 0.8rem;
      }

      .editorial-copy {
        color: #716a61;
        max-width: 760px;
        line-height: 1.7;
        margin-bottom: 2rem;
      }

      [data-testid="stDataFrame"] {
        border: 1px solid #d8d0c5;
      }

      .stSelectbox > div > div,
      .stTextInput > div > div > input {
        border-radius: 0 !important;
      }

      .stButton > button {
        border-radius: 0;
        background: #171512;
        color: white;
        border: 1px solid #171512;
        font-family: 'IBM Plex Mono', monospace;
        font-size: 0.72rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }

      .stButton > button:hover {
        background: #8c6a2d;
        color: white;
        border-color: #8c6a2d;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

df = pd.read_csv("startup_cleaned.csv")
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year


def intro(title, copy):
    st.markdown('<div class="editorial-kicker">INDIA / STARTUP CAPITAL</div>', unsafe_allow_html=True)
    st.title(title)
    st.markdown(f'<div class="editorial-copy">{copy}</div>', unsafe_allow_html=True)


def load_overall_analysis():
    intro(
        "Capital, mapped with context.",
        "Explore funding volume, deal concentration, startup activity and month-by-month movement from the project dataset.",
    )

    total = round(df["amount"].sum())
    max_funding = df.groupby("startup")["amount"].max().sort_values(ascending=False).head(1).values[0]
    avg_funding = df.groupby("startup")["amount"].sum().mean()
    num_startups = df["startup"].nunique()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total funding", f"{total} Cr")
    col2.metric("Largest deal", f"{max_funding} Cr")
    col3.metric("Average startup funding", f"{round(avg_funding)} Cr")
    col4.metric("Funded startups", num_startups)

    st.markdown("## Funding over time")
    selected_option = st.selectbox("Metric", ["Total", "Count"])

    if selected_option == "Total":
        temp_df = df.groupby(["year", "month"])["amount"].sum().reset_index()
    else:
        temp_df = df.groupby(["year", "month"])["amount"].count().reset_index()

    temp_df["x_axis"] = temp_df["month"].astype(str) + "-" + temp_df["year"].astype(str)

    fig, ax = plt.subplots(figsize=(13, 4.7))
    fig.patch.set_facecolor("#fbfaf7")
    ax.set_facecolor("#fbfaf7")
    ax.plot(temp_df["x_axis"], temp_df["amount"], color="#8c6a2d", linewidth=2.3)
    ax.grid(axis="y", color="#ddd4c8", alpha=0.6)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="x", rotation=75, labelsize=8)
    ax.tick_params(axis="y", labelsize=8)
    st.pyplot(fig, use_container_width=True)


def load_investor_details(investor):
    intro(
        investor,
        "Investor-focused view of recent funding activity, largest startup exposures, sector mix and year-over-year deployment.",
    )

    investor_df = df[df["investors"].fillna("").str.contains(investor, regex=False)]

    st.markdown("## Most recent investments")
    recent = investor_df.sort_values("date", ascending=False).head(8)[
        ["date", "startup", "vertical", "city", "round", "amount"]
    ]
    st.dataframe(recent, use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)

    with col1:
        big_series = investor_df.groupby("startup")["amount"].sum().sort_values(ascending=False).head(7)
        st.markdown("### Biggest startup exposures")
        fig, ax = plt.subplots(figsize=(7, 4.5))
        fig.patch.set_facecolor("#fbfaf7")
        ax.set_facecolor("#fbfaf7")
        ax.barh(big_series.index[::-1], big_series.values[::-1], color="#b7765f")
        ax.grid(axis="x", color="#ddd4c8", alpha=0.55)
        ax.spines[["top", "right", "left"]].set_visible(False)
        st.pyplot(fig, use_container_width=True)

    with col2:
        sector_series = investor_df.groupby("vertical")["amount"].sum().sort_values(ascending=False).head(8)
        st.markdown("### Sector allocation")
        fig1, ax1 = plt.subplots(figsize=(7, 4.5))
        fig1.patch.set_facecolor("#fbfaf7")
        ax1.set_facecolor("#fbfaf7")
        ax1.pie(
            sector_series,
            labels=sector_series.index,
            autopct="%0.1f%%",
            colors=["#8c6a2d", "#b7765f", "#93a189", "#25221e", "#d1ab67", "#c28f7b", "#adb7a4", "#655e55"],
            textprops={"fontsize": 8},
        )
        st.pyplot(fig1, use_container_width=True)

    year_series = investor_df.groupby("year")["amount"].sum()
    st.markdown("## Year-over-year investment")

    fig2, ax2 = plt.subplots(figsize=(13, 4.5))
    fig2.patch.set_facecolor("#fbfaf7")
    ax2.set_facecolor("#fbfaf7")
    ax2.plot(year_series.index, year_series.values, color="#93a189", linewidth=2.3, marker="o")
    ax2.grid(axis="y", color="#ddd4c8", alpha=0.6)
    ax2.spines[["top", "right", "left"]].set_visible(False)
    st.pyplot(fig2, use_container_width=True)


st.sidebar.markdown("## Startup Funding")
st.sidebar.caption("INDIA / DATA EXPLORER")

option = st.sidebar.selectbox("View", ["Overall Analysis", "StartUp", "Investor"])

if option == "Overall Analysis":
    load_overall_analysis()

elif option == "StartUp":
    selected_startup = st.sidebar.selectbox("Startup", sorted(df["startup"].dropna().unique().tolist()))
    intro(
        selected_startup,
        "Startup-focused funding records from the source dataset.",
    )
    startup_df = df[df["startup"] == selected_startup].sort_values("date", ascending=False)
    total = startup_df["amount"].sum()
    largest = startup_df["amount"].max()
    deals = len(startup_df)

    c1, c2, c3 = st.columns(3)
    c1.metric("Total funding", f"{round(total, 1)} Cr")
    c2.metric("Largest deal", f"{round(largest, 1)} Cr")
    c3.metric("Funding records", deals)

    st.dataframe(
        startup_df[["date", "vertical", "city", "round", "amount", "investors"]],
        use_container_width=True,
        hide_index=True,
    )

else:
    investors = sorted(
        set(
            item.strip()
            for value in df["investors"].fillna("")
            for item in value.split(",")
            if item.strip()
        )
    )
    selected_investor = st.sidebar.selectbox("Investor", investors)
    load_investor_details(selected_investor)
