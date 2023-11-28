
import streamlit as st
import matplotlib as mpl
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy as sp

from collections import Counter
from scipy import stats

st.title("Open-Source Pitchtype Card")
st.write('This app is designed to allow a user to upload their own pitch-level data and generate cards for the various pitchtypes of the players included.')
st.write('Code is located [here](https://github.com/Blandalytics/PLV_viz/blob/main/open_source_pitch_card.py), and a CSV with 2023 MLB Statcast data formatted for this app can be found [here](https://drive.google.com/file/d/1cWKBBSsWNlZbAz3Mwex-g9VMp99mr7cQ/view?usp=sharing)')
st.write('For questions, contact me [@Blandalytics](https://twitter.com/blandalytics)')

# Load Data
pitch_file = st.file_uploader("Please upload a pitch-level CSV file:")
if pitch_file is not None:
    df = pd.read_csv(pitch_file)

    # Dropdown to select a pitcher
    pitcher_names = df['Pitcher Name'].unique()
    selected_pitcher = st.selectbox('Select a Pitcher', pitcher_names)

    # Filter the dataframe for the selected pitcher
    df = df[df['Pitcher Name'] == selected_pitcher]

    # The rest of your code for visualizations and data displays goes here
    # Make sure to use 'df' which is now filtered based on the selected pitcher

    # Example: Displaying the filtered DataFrame (you can replace this with your visualization code)
    st.write(df)

# Rest of the existing code continues here...
