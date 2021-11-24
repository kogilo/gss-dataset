# Imports
from pandas.core.frame import DataFrame
import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image
import plotly.express as px 
import csv 
import plotly.graph_objects as go

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.write(df)

# File_Path "/Users/abullaothuw/Documents/trainings_hub/upwaedglobal/coursera/gss_project/data/.gss2016.csv"

gss_data = pd.read_csv("gss2016.csv", delimiter=",")

st.title("The General Social Survey Data Analytics Web App")
st.write(f'<iframe width="560", height="315" src="https://www.youtube.com/embed/hyirTanipAc"</iframe>', unsafe_allow_html=True,)



st.write('''''')
st.write('''''')
st.write('''''')

st.header("GSS 2016 Dataset")
st.write('''''')

st.write(gss_data)

gss_data_filtered=gss_data[["sex", "race", "age", "degree", "wrkstat", "income", "happy"]]

st.write('''''')
st.write('''''')
st.write('''''')

st.header("GSS 2016 Dataset Filtered on sex, Race, Age, Degree, Work Status, Income and Happiness")
st.write(gss_data_filtered)



columns = {"sex", "race", "age", "degree", "wrkstat", "income", "happy"}

st.write('''''')
st.write('''''')
st.write('''''')

st.header("GSS 2016 Dataset Aggregated by count")
pick_columns = st.selectbox("Count by column: ", list(columns) )

gss_data_filtered["Count"]=0

gss_data_filtered_count = gss_data_filtered.groupby(pick_columns).count()
gss_data_filtered_count = gss_data_filtered_count[["Count"]]
# gss_data_filtered_count.columns = ['Count']
gss_data_filtered_count["percentages"]=(gss_data_filtered_count.Count/gss_data_filtered_count.Count.sum())* 100

st.write(gss_data_filtered_count)


st.write('''''')
st.write('''''')
st.write('''''')

st.header("GSS 2016 Dataset Correlation between columns")
multi_select_column = st.multiselect("Multi-select columns for corelation", list(columns), default=['sex'])
multi_select_gss_data_filtered=gss_data_filtered[multi_select_column]
st.write(multi_select_gss_data_filtered)

st.write('''''')
st.write('''''')
st.write('''''')
st.header("GSS 2016 Dataset Correlation between columns multi-select")

multi_select_column2 = st.multiselect("Multi-select columns groupby:", list(columns), default=["sex"])
multi_select_groupby = gss_data_filtered[multi_select_column2].groupby(multi_select_column2).size().reset_index(name="Count")

multi_select_groupby["percentages"]= (multi_select_groupby.Count/multi_select_groupby.Count.sum())*100

st.write(multi_select_groupby)

st.write('''''')
st.write('''''')
st.write('''''')

st.header("GSS 2016 Dataset Aggregated by Count Pie Chart")
pick_columns_visualized =st.selectbox("Visualize by Column", list(columns))
gss_data_filtered_count_visual = gss_data_filtered.groupby(pick_columns_visualized).count()

gss_data_filtered_count_visual['x-axis'] = gss_data_filtered_count_visual.index
fig = go.Figure(data=[go.Pie(labels=gss_data_filtered_count_visual["x-axis"], values=gss_data_filtered_count_visual["Count"])])

st.plotly_chart(fig)



# st.DataFrame(gss_data_filtered)