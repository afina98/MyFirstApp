import streamlit as st
import pandas as pd

st.header("Life Expectancy at Birth, Female")

st.write('Disclamer. This web app is for learning purpose only')
st.write ('Data is from [HERE](https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN?end=2019&locations=MY&most_recent_year_desc=false&start=1960&view=chart)')

st.write(pd.DataFrame({
    'Country': ['Malaysia', 'Indonesia', 'Singapore'],
    'Year 1960': [10,20,30],
    'Year 1970': [10,60,30],
    'Year 1980': [11,22,33],
    'Year 1990': [33,44,55],
    'Year 2000': [11,22,33],
    'Year 2010': [33,44,55]

}))
            
option = st.sidebar. selectbox('Select Country', ['Malaysia','Indonesia','Singapore'])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
