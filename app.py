import pandas as pd
import streamlit as st

df = pd.read_csv('estados1.csv')
st.dataframe(df, 500, 500) 
