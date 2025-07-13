import os
import streamlit as st
from utils.data_loader import load_csv_files
from utils.plot import plot_time_series
from components.navigation import navigation_buttons
from components.column_selector import select_columns

import streamlit as st

# import pandas as pd
# from io import StringIO

# Load data files
st.sidebar.title("Time-Series Visualizer")
st.sidebar.header("📁 Data Directory")
default_dir = "data"
data_dir = st.sidebar.text_input("Enter directory path containing CSV files:", value=default_dir)

# Check if the directory exists
if not os.path.exists(data_dir):
    st.error(f"Directory does not exist: `{data_dir}`")
    st.stop()

# load CSV
data_files = load_csv_files(data_dir)
if not data_files:
    st.error(f"No csv files in `{data_dir}`")
    st.stop()

if 'file_index' not in st.session_state:
    st.session_state.file_index = 0

current_file = data_files[st.session_state.file_index]
df = current_file['data']

# Column selection
st.subheader("📈 Plot")
selected_columns = select_columns(df)

# st.markdown(f"**Currently showing:** `{current_file['name']}`")

# Plot
if selected_columns:
    fig = plot_time_series(df, selected_columns, current_file['name'])
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Select one or more columns to plot.")

# pagenation
navigation_buttons(len(data_files))