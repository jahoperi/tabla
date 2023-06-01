from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('estados1.csv')
AgGrid(df) 
