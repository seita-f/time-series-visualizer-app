import streamlit as st

def navigation_buttons(total_files):
    col1, col2 = st.columns(2)
    with col1:
        if st.button("← Previous") and st.session_state.file_index > 0:
            st.session_state.file_index -= 1
            st.rerun()
    with col2:
        if st.button("Next →") and st.session_state.file_index < total_files - 1:
            st.session_state.file_index += 1
            st.rerun()
