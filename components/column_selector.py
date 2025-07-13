import streamlit as st


def select_columns(df):
    numeric_columns = df.select_dtypes(include='number').columns.tolist()

    if "last_selected_columns" not in st.session_state:
        st.session_state["last_selected_columns"] = numeric_columns[:1]

    valid_defaults = [col for col in st.session_state["last_selected_columns"] if col in numeric_columns]

    selected = st.multiselect(
        "Please select column(s)",
        options=numeric_columns,
        default=valid_defaults
    )

    st.session_state["last_selected_columns"] = selected

    return selected
