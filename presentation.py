#Imports
import numpy as np
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
df = df.sort_values(by=['Index'])
genders = ['Both', 'Male', 'Female']
graph_list = ('Height Histogram', 'Weight Histogram', 'Weight-Height Scatter')
gender_selector = st.selectbox("Select the gender:", genders)
graph_selector = st.selectbox("Select the graph to show:", graph_list)

if graph_selector == 'Weight-Height Scatter' and gender_selector != 'Both':
    fig_scatter = px.scatter(df, x=df.Weight[df['Gender'] == gender_selector], y=df.Height[df['Gender'] == gender_selector], color=df.Index[df['Gender'] == gender_selector])
    st.plotly_chart(fig_scatter)

if graph_selector == 'Weight-Height Scatter' and gender_selector == 'Both':
    fig_scatter = px.scatter(df, x=df.Weight, y=df.Height, color=df.Index)
    st.plotly_chart(fig_scatter)

if graph_selector == 'Height Histogram' and gender_selector == 'Male':
    fig_male_height_hist = px.histogram(df.Height[df['Gender'] == gender_selector], nbins=50, marginal='rug', color=df.Index[df['Gender'] == gender_selector])
    fig_male_height_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_male_height_hist)

if graph_selector == 'Height Histogram' and gender_selector == 'Female':
    fig_male_height_hist = px.histogram(df.Height[df['Gender'] == gender_selector], nbins=50, marginal='rug', color=df.Index[df['Gender'] == gender_selector])
    fig_male_height_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_male_height_hist)

if graph_selector == 'Height Histogram' and gender_selector == 'Both':
    fig_male_height_hist = px.histogram(df.Height, nbins=50, marginal='rug', color=df.Index)
    fig_male_height_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_male_height_hist)

if graph_selector == 'Weight Histogram' and gender_selector == 'Male':
    fig_male_height_hist = px.histogram(df.Weight[df['Gender'] == gender_selector], nbins=50, marginal='rug', color=df.Index[df['Gender'] == gender_selector])
    fig_male_height_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_male_height_hist)

if graph_selector == 'Weight Histogram' and gender_selector == 'Female':
    fig_male_height_hist = px.histogram(df.Weight[df['Gender'] == gender_selector], nbins=50, marginal='rug', color=df.Index[df['Gender'] == gender_selector])
    fig_male_height_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_male_height_hist)

if graph_selector == 'Weight Histogram' and gender_selector == 'Both':
    fig_male_height_hist = px.histogram(df.Weight, nbins=50, marginal='rug', color=df.Index)
    fig_male_height_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_male_height_hist)


index_means_weight = df.groupby('Index').Weight.mean().reset_index()['Weight']
index_means_height = df.groupby('Index').Height.mean().reset_index()['Height']

# index_means_height = np.reshape(index_means_height, 6)
# index_means_weight = np.reshape(index_means_weight, 6)

means_df = pd.DataFrame(data=[index_means_weight, index_means_height])
means_df = means_df.transpose()
st.dataframe(means_df)

fig = px.scatter(means_df, x=index_means_weight, y=index_means_height, color=means_df.index)
st.plotly_chart(fig)