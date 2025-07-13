# app.py
import streamlit as st
from utils.data_loader import load_csv_files
from utils.plot import plot_time_series
from components.navigation import navigation_buttons
from components.column_selector import select_column

import streamlit as st


# Load data files
data_files = load_csv_files("data")

if 'file_index' not in st.session_state:
    st.session_state.file_index = 0

current_file = data_files[st.session_state.file_index]
df = current_file['data']

# Header
st.title("Time-Series Visualizer")
st.markdown(f"**Currently showing:** `{current_file['name']}`")

# Column selection
selected_column = select_column(df)

# Plot
if selected_column:
    fig = plot_time_series(df, selected_column)
    st.plotly_chart(fig, use_container_width=True)

# Navigation buttons
navigation_buttons(len(data_files))