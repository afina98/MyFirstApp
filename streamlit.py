import streamlit as st
import numpy as np
import pandas as pd

st.header("Life Expectancy at Birth, Female")

st.write('Disclamer. This web app is for learning purpose only')
st.write ('Data is from [HERE](https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN?end=2019&locations=MY&most_recent_year_desc=false&start=1960&view=chart)')

df = pd.read_csv ('data\life_csv')
option = st.sidebar. selectbox('Select Country', ['Malaysia','Indonesia','Singapore'])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
