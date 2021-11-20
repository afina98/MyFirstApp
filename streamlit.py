import streamlit as st
import numpy as np
import pandas as pd

st.header("Life Expectancy at Birth, Female")

df=pd.read_csv("https://github.com/afina98/MyFirstApp/blob/main/Life%20Expectancy%20at%20birth%2C%20female.csv")
st.dataframe(df)

st.write('Disclamer. This web app is for learning purpose only')
st.write ('Data is from [HERE](https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN?end=2019&locations=MY&most_recent_year_desc=false&start=1960&view=chart)')

option = st.sidebar. selectbox('Select Country', ['Malaysia','Indonesia','Singapore'])
