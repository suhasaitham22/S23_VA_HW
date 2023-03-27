import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

data=pd.read_csv('data.csv')
st.write(data)

st.sidebar.header("Pick two variables for your scatterplot")

# list of columns to exclude
exclude_cols = ['OPE ID', 'Zip Code']

# filter out the columns to exclude from the dataframe
numeric_cols = [col for col in data.select_dtypes(include=np.number).columns.tolist() if col not in exclude_cols]

# select the y-axis variable from the remaining numeric columns
x_variable = st.sidebar.selectbox("Pick your x-axis", numeric_cols)

y_variable = st.sidebar.selectbox("Pick your y-axis", numeric_cols)

scatter = alt.Chart(data, title=f"Correlation between {x_variable} and {y_variable}").mark_point().encode(
    alt.X(x_variable,title=f'{x_variable}'),
    alt.Y(y_variable,title=f'{y_variable}'),
    tooltip=[x_variable, y_variable]).configure(background='#D9E9F0')
st.altair_chart(scatter, use_container_width=True)





st.sidebar.header("Pick two variables for your Bar Graph")

x_variable2 = st.sidebar.selectbox("Pick your 2nd x-axis",data.columns.tolist())
y_variable2 = st.sidebar.selectbox("Pick your 2nd y-axis",data.columns.tolist())

bars = alt.Chart(data, title=f"Bar Graph between {x_variable} and {y_variable}").mark_bar().encode(alt.X(x_variable2,title=f'{x_variable2}'), alt.Y(y_variable2,title=f'{y_variable2}'), tooltip=[x_variable2, y_variable2]).configure(background='#D9E9F0')
st.altair_chart(bars, use_container_width=True)
