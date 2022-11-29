import streamlit as st
import pandas as pd
import numpy as np
import plotly as px

st.title ("Police Department Incident Reports")
st.markdown('Reporting incidents is **_really_ cool**.')

df = pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")
###@st.experimental_singleton###
###st.dataframe(df)###

day_week = st.sidebar.selectbox("Day of week",df['Incident Day of Week'].unique())
year = st.select_slider("Year",(2018,2019,2020))
district = st.sidebar.selectbox("District",df['Police District'].unique())

dfconfiltros = df[df['Police District']==district]
dfconfiltros = dfconfiltros[dfconfiltros['Incident Year']==year]
dfconfiltros = dfconfiltros[dfconfiltros['Incident Day of Week'] == day_week]

mapa = pd.DataFrame()
mapa['lat'] = dfconfiltros['Latitude']
mapa['lon'] = dfconfiltros['Longitude']
mapa = mapa.dropna()

promedio = int(((df['Latitude'].count()/7)/11)/3)
cuenta = int(mapa['lat'].count())

col1, col2 = st.columns([3, 1])
with col1:
   st.map(mapa)
with col2:
    st.metric(label="Conteo contra el promedio**:",value=cuenta,delta=(cuenta-promedio))
    st.write("**(día/año/distrito)")