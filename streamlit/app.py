import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

df = pd.DataFrame({
    "c1": [1,2,3,4,5],
    "c2": [10,20,30,40,50]
    })

st.write("Here is the DataFrame")
st.write(df)

# line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)