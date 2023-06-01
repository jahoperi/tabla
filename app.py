import pandas as pd
import streamlit as st
df = pd.read_csv('tresestados1.csv')
st.dataframe(df)
