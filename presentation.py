#Imports
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from geopy.geocoders import Nominatim
import plotly


#Title
st.title("Data Presentation / Felix  & Jeno")

df = pd.read_csv("https://raw.githubusercontent.com/chriswmann/datasets/master/500_Person_Gender_Height_Weight_Index.csv")

if st.button('Show data'):
    st.dataframe(df)
genders = df['Gender'].drop_duplicates()
graph_list = ('Height Histogram', 'Weight Histogram', 'Weight-Height Scatter')
gender_selector = st.selectbox("Select the gender:", genders)
graph_selector = st.selectbox("Select the graph to show:", graph_list)

if graph_selector == 'Weight-Height Scatter':
    fig_scatter = px.scatter(df, x=df.Weight[df['Gender'] == gender_selector], y=df.Height[df['Gender'] == gender_selector], color=df.Index[df['Gender'] == gender_selector])
    st.plotly_chart(fig_scatter)


