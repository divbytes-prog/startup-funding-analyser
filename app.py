import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df = df.dropna(subset=['date', 'startup', 'amount']).sort_values('date', ascending=False).copy()
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df = df.dropna(subset=['amount'])
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_analysis():
    st.title('Overall Analysis')

    # total invested amount
    total = round(df['amount'].sum())
    # max amount infused in a startup
    max_funding = df['amount'].max()
    # avg ticket size
    avg_funding = df.groupby('startup')['amount'].sum().mean()
    # total funded startups
    num_startups = df['startup'].nunique()

    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Total',str(total) + ' Cr')
    with col2:
        st.metric('Max', str(max_funding) + ' Cr')

    with col3:
        st.metric('Avg',str(round(avg_funding)) + ' Cr')

    with col4:
        st.metric('Funded Startups',num_startups)

    st.caption('Historical coverage: 2015–2020; selected source-linked deals: 2021–2026. This dataset is not a complete record of Indian startup funding.')
    st.header('Monthly funding trend')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df = temp_df.sort_values(['year', 'month'])
    temp_df['x_axis'] = temp_df['year'].astype('str') + '-' + temp_df['month'].astype('str').str.zfill(2)

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig3)



def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investor
    investor_rows = df[df['investors'].fillna('').str.split(',').apply(
        lambda names: investor in [name.strip() for name in names]
    )].copy()
    if investor_rows.empty:
        st.info('No investments found for this investor.')
        return
    last5_df = investor_rows.head(5)[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)
    with col1:
        # biggest investments
        big_series = investor_rows.groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)

        st.pyplot(fig)

    with col2:
        verical_series = investor_rows.groupby('vertical')['amount'].sum()

        st.subheader('Sectors invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(verical_series,labels=verical_series.index,autopct="%0.01f%%")

        st.pyplot(fig1)

    year_series = investor_rows.groupby('year')['amount'].sum().sort_index()

    st.subheader('YoY Investment')
    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index,year_series.values)

    st.pyplot(fig2)

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()

elif option == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select Startup', sorted(df['startup'].unique().tolist()))
    st.title('Startup Analysis')
    startup_rows = df[df['startup'] == selected_startup]
    st.metric('Total funding in dataset', f"{startup_rows['amount'].sum():,.1f} Cr")
    st.metric('Funding records', len(startup_rows))
    st.dataframe(startup_rows[['date', 'vertical', 'city', 'investors', 'round', 'amount', 'source_url']], use_container_width=True)
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted({name.strip() for value in df['investors'].dropna() for name in value.split(',') if name.strip()}))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
