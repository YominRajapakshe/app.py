from Libraries import *
import streamlit as st
st.title('SIL Covid-19 Dashboard')
countries = ['USA', 'Australia', 'China', 'Egypt', 'Sri Lanka', 'France', 'Canada', 'India', 'Brazil', 'Denmark', 'Turkey', 'Vietnam', 'Argentina', 'Mexico', 'Japan']
data_types = ['cases', 'deaths', 'recovered']

country_code = {'Sri Lanka': 'lk', 'USA': 'us',
                'China': 'cn', 'India': 'in', 'Mexico': 'mx', 'Denmark': 'dk', 'Brazil': 'br', 'France': 'fr', 'Vietnam': 'vn', 'Argentina': 'ar', 'Japan': 'jp', 'Canada': 'ca', 'Turkey': 'tr', 'Australia': 'au', 'Egypt': 'eg'}

data_types = ['cases', 'deaths', 'recovered']
country = st.sidebar.selectbox('Select Country', countries)
st.image(f"https://flagcdn.com/80x60/{country_code[country]}.png")
days = st.sidebar.slider('Select Days', min_value=1, max_value=100)
data_type = st.sidebar.multiselect('Select data type', data_types)
total_cases = get_historic_cases(country, str(days))
total_deaths = get_historic_deaths(country, str(days))
total_recoveries = get_historic_recoveries(country, days)
total_df = pd.concat(
    [total_cases, total_deaths, total_recoveries], axis=1).astype(int)
daily_cases = get_daily_cases(country, str(days))
daily_deaths = get_daily_deaths(country, str(days))
daily_recoveries = get_daily_recoveries(country, str(days))
daily_df = pd.concat(
    [daily_cases, daily_deaths, daily_recoveries], axis=1).astype(int)
yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_recoveries = get_yesterday_recoveries(country)
st.metric('Selected country', country)
col1, col2, col3 = st.columns(3)
col1.metric('Total Cases', yesterday_cases)
col2.metric('Total Deaths', yesterday_deaths)
col3.metric('Total Recovered', yesterday_recoveries)
st.line_chart(daily_df[data_type])
st.video('https://www.youtube.com/watch?v=5DGwOJXSxqg')

