import streamlit as st
import requests

API_BASE_URL = "http://backend:8002"
TEACHERS_ENDPOINT = f"{API_BASE_URL}/teachers"
STUDENTS_ENDPOINT = f"{API_BASE_URL}/student"

@st.cache_data()
def load_teachers():
    response = requests.get(TEACHERS_ENDPOINT)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to load teachers.")
        return []

teachers = load_teachers()
teacher_ids = [teacher['id'] for teacher in teachers]
teacher_names = [teacher['name'] for teacher in teachers]

st.title("Add a New Student")

with st.form("student_form", clear_on_submit=True):
    name = st.text_input("Student Name")
    email = st.text_input("Student Email")
    selected_teacher_ids = st.multiselect(
        "Select Teachers",
        options=teacher_ids,
        format_func=lambda x: teacher_names[teacher_ids.index(x)]
    )
    submit_button = st.form_submit_button("Add Student")

if submit_button:
    student_data = {
        "name": name,
        "email": email,
        "teacher_ids": selected_teacher_ids
    }    
    response = requests.post(STUDENTS_ENDPOINT, json=student_data)
    if response.status_code == 200:
        st.success(f"HOORRAAYYY!\n- Student added successfully :)")
    else:
        st.error(f"Failed to add student: {response.json().get('detail', 'Unknown error')}")