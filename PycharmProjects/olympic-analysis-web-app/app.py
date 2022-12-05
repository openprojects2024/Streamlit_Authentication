# This is a sample Python script.
import streamlit as st
import pandas as pd
import prepeossesor, helper

df = pd.read_csv('athlete_events.csv')
region_df  = pd.read_csv('noc_regions.csv')

df = prepeossesor.preprocess(df,region_df)

st.sidebar.title('Olympics Analysis')
user_menu = st.sidebar.radio(
    'select an option',
    ('Medal Tally','Overall analysis','Country-wise Analysis','Athelete wise Analysis')
)
df = df.loc[~df.index.duplicated(),:].copy()
st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years, country = helper.country_yr_list(df) # import country and years list from the helper file

    # creating dropdown menu for year and country
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select Counter", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    st.dataframe(medal_tally)