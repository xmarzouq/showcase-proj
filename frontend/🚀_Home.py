import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Welcome to the Student-Teacher Platform")

col1, col2 = st.columns(2)

with col1:
    if st.button("Teachers"):
        switch_page("teacher")

with col2:
    if st.button("Students"):
        switch_page("student")