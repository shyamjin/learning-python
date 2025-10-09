"""
A web framework is a Python library that helps you build web applications or REST APIs easily — without writing everything from scratch.
Flask ->
fastAPI -> latest wi
Django
| Framework   | Type                     | Best For               | Description                                                |
| ----------- | ------------------------ | ---------------------- | ---------------------------------------------------------- |
| **Flask**   | Lightweight              | Beginners / small apps | Simple and flexible — you write what you need.             |
| **FastAPI** | Modern, high-performance | APIs / async apps      | Very fast, supports async, type hints, and automatic docs. |
| **Django**  | Full-featured            | Large web apps         | Comes with ORM, admin panel, user auth, etc.               |
How to write the REST API using fastAPI
GET and POST

Use case.
1. I have csv, i want to store user data on submitting of form
2. Whatever i was saving, i also want to see that in my app
"""
import streamlit as st
import requests
import pandas as pd

FASTAPI_URL = "http://127.0.0.1:8000"

st.title("👥 User Management (FastAPI + Streamlit + Text File)")

# --- Add New User ---
st.header("➕ Add User")

with st.form("add_user_form"):
    name = st.text_input("Enter name")
    email = st.text_input("Enter email")
    submitted = st.form_submit_button("Add")

    if submitted:
        if name and email:
            response = requests.post(f"{FASTAPI_URL}/users", json={"name": name, "email": email})
            if response.status_code == 200:
                st.success("✅ User added successfully!")
            else:
                st.error("❌ Failed to add user.")
        else:
            st.warning("Please enter both name and email.")

# --- Show Users ---
st.header("📋 User List")
response = requests.get(f"{FASTAPI_URL}/users")

if response.status_code == 200:
    users = response.json()
    if users:
        df = pd.DataFrame(users)
        st.dataframe(df)
    else:
        st.info("No users yet. Add a new one above!")
else:
    st.error("Failed to load user data.")
