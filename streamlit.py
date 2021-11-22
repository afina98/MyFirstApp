import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

st.header("Life Expectancy at Birth, Female")

st.write('Disclamer. This web app is for learning purpose only')
st.write ('Data is from [HERE](https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN?end=2019&locations=MY&most_recent_year_desc=false&start=1960&view=chart)')

st.write(pd.DataFrame({
    'Country': ['Malaysia', 'Indonesia', 'Singapore'],
    'Year 1960': [61.396,49.009,69.196],
    'Year 1970': [66.329,54.536,71.706],
    'Year 1980': [70.379,59.608,74.7],
    'Year 1990': [72.858,63.727,77.6],
    'Year 2000': [74.786,67.185,80],
    'Year 2010': [76.732,71.311,84]

    }))


st.write('The result shown below is by using select box. It only show result for one country only')

option = st.sidebar. selectbox('Select Country', ['Malaysia','Indonesia','Singapore'])

if option == 'Malaysia':
 st.write(pd.DataFrame({
    'Country': ['Malaysia'],
    'Year 1960': [61.396],
    'Year 1970': [66.329],
    'Year 1980': [70.379],
    'Year 1990': [72.858],
    'Year 2000': [74.786],
    'Year 2010': [76.732]

    }))
 
 if option == 'Indonesia':
  st.write(pd.DataFrame({
    'Country': ['Indonesia'],
    'Year 1960': [49.009],
    'Year 1970': [54.536],
    'Year 1980': [59.608],
    'Year 1990': [63.727],
    'Year 2000': [67.185],
    'Year 2010': [71.311]

    }))
 
 if option == 'Singapore':
  st.write(pd.DataFrame({
    'Country': ['Singapore'],
    'Year 1960': [69.196],
    'Year 1970': [71.706],
    'Year 1980': [74.7],
    'Year 1990': [77.6],
    'Year 2000': [80],
    'Year 2010': [84]

    }))
            
option = st.sidebar. selectbox('Select Country', ['Malaysia','Indonesia','Singapore'])

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
