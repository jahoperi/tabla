import pandas as pd
import streamlit as st
df = pd.read_csv('tresestados.csv')
st.dataframe(df)
