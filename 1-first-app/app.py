#-------------------#
# SETUP
import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

#-------------------#

# IMPORT DATA

# Data import (you may need to change the path)
df = pd.read_csv('https://raw.githubusercontent.com/kirenz/datasets/master/oecd.csv')


###-------------------###
# START OF OUR APP

#-------------------#
# HEADER

# Title of our app
st.title("Text") #Hier kann ich die Überschrift ändern

# Add image
st.image('hdm-logo.jpg') #Hier kann ich das Bild ändern

# Add header
st.header("My header")

#-------------------#
# SIDEBAR

# Header
st.sidebar.header("This is my sidebar") #Seitenbalken

# Make a slider
satisfaction = st.sidebar.slider('What is your life satisfaction?', 0, 10, 1)

# Show output of slider selection
st.sidebar.write("My life satisfaction is around ", satisfaction, 'points') #Interaktiv

#-------------------#
# BODY

st.write("Take a look at my data")
# Show static DataFrame
st.dataframe(df)

st.write("Take a look at my chart")
# Make a chart with altair
c = alt.Chart(df).mark_circle().encode(
     x='life_satisfaction', 
     y='gdp_per_capita', 
     color='country'
     )

# Show plot
st.altair_chart(c, use_container_width=True)

###-------------------###
# END OF APP