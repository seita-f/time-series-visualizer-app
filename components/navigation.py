import streamlit as st


def navigation_buttons(num_files: int):
    col1, col2, col3 = st.columns([1, 2, 1])

    # Previous button
    if col1.button("◀︎ Previous", use_container_width=True):
        if st.session_state.file_index > 0:
            st.session_state.file_index -= 1

    # Current page / Total
    current = st.session_state.file_index + 1
    col2.markdown(
        f"<div style='text-align: center; font-weight: bold;'>📄 {current} / {num_files}</div>",
        unsafe_allow_html=True
    )

    # Next button
    if col3.button("Next ▶︎", use_container_width=True):
        if st.session_state.file_index < num_files - 1:
            st.session_state.file_index += 1