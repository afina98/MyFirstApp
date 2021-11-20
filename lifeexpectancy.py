!pip install streamlit
!pip install pyngrok

%%writefile myfirstapp.py
import streamlit as st
import numpy as np
import pandas as pd

st.header("Life Expectancy at Birth, Female")

!streamlit myfirstapp.py --server.port 80 &>/dev/null&
!streamlit run myfirstapp.py --server.port 80 &>/dev/null&

from pyngrok import ngrok
ngrok.kill()

public_url = ngrok.connect(port = 80)
public_url

%%writefile myfirstapp.py
import streamlit as st
import numpy as np
import pandas as pd

st.header("Life Expectancy at Birth, Female")

st.write('Disclamer. This web app is for learning purpose only')
st.write ('Data is from [HERE](https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN?end=2019&locations=MY&most_recent_year_desc=false&start=1960&view=chart)')

option = st.sidebar. selectbox('Select Country', ['Malaysia','Indonesia','Singapore'])
