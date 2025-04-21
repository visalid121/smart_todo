import streamlit as st
import requests
from datetime import datetime

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="Smart Todo List", page_icon="🧠", layout="centered")

st.title("🧠 Smart Todo List")

# --- Add New Task ---
st.subheader("➕ Add a Task")

with st.form("add_task"):
    title = st.text_input("Task Title")
    deadline = st.date_input("Deadline")
    time = st.time_input("Time", value=datetime.now().time())
    category = st.text_input("Category (e.g. work, personal)")
    submitted = st.form_submit_button("Add Task")

    if submitted:
        full_deadline = datetime.combine(deadline, time).isoformat()
        response = requests.post(f"{API_BASE}/tasks/", params={
            "title": title,
            "deadline": full_deadline,
            "category": category
        })
        if response.status_code == 200:
            st.success("✅ Task added!")
        else:
            st.error("❌ Failed to add task")

# --- Task Suggestions ---
st.subheader("💡 Task Suggestions")

suggestion_count = st.slider("Number of suggestions", min_value=1, max_value=5, value=3)
if st.button("Get Suggestions"):
    response = requests.get(f"{API_BASE}/suggestions/", params={"count": suggestion_count})
    if response.status_code == 200:
        suggestions = response.json()
        for i, suggestion in enumerate(suggestions, 1):
            st.markdown(f"**Suggestion {i}:** {suggestion['title']} — {suggestion['category']} (Due: {suggestion['deadline']})")
    else:
        st.error("Couldn't fetch suggestions.")

# --- View Tasks ---
st.subheader("📋 Your Tasks")

response = requests.get(f"{API_BASE}/tasks/")
if response.status_code == 200:
    tasks = response.json()
    if not tasks:
        st.info("No tasks yet. Add one above!")
    else:
        for task in tasks:
            st.markdown(f"**{task['title']}** — {task['category']} (Due: {task['deadline']})")
else:
    st.error("Couldn't fetch tasks.")
