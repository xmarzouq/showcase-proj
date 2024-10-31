import streamlit as st
import requests
from faker import Faker

API_URL = "http://backend:8002/teachers"
fake = Faker()

st.title("Our Teachers")

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    teachers = response.json()
except requests.exceptions.RequestException as e:
    st.error("Failed to load teachers.")
    st.error(str(e))
    teachers = []

if teachers:
    cols = st.columns(4)

    for idx, teacher in enumerate(teachers):
        with cols[idx % 4]:
            with st.container():
                st.subheader(teacher['name'])
                st.write(f"Subject: {teacher['subject']}")

                st.empty()

                if st.button("BOOK!", key=f"book_{teacher['id']}"):
                    st.info(f"Coming Soon! {fake.sentence()}")
                st.divider()
else:
    st.warning("No teachers available.")