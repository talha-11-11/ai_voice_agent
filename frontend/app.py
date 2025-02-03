import streamlit as st
import requests

st.title("AI Voice Agent Dashboard")

# Start a voice call
if st.button("Start Voice Call"):
    metadata = {"user": "test_user", "company": "Example Company"}
    response = requests.post("http://localhost:8000/voice/start", json=metadata)
    st.json(response.json())

# Start a HeyGen avatar call
text_input = st.text_input("Enter text for HeyGen Call:")
if st.button("Start HeyGen Call"):
    response = requests.post("http://localhost:8000/avatar/start", json={"text": text_input})
    st.json(response.json())