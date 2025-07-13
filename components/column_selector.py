import streamlit as st

def select_column(df):
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    if not numeric_columns:
        st.warning("No numeric columns found.")
        return None
    return st.selectbox("Select Column", numeric_columns)
