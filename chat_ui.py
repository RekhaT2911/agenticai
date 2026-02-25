import streamlit as st
import requests

st.set_page_config(page_title="Agentic AI Chatbot", layout="centered")

st.title("🤖 Agentic AI Platform")
st.markdown("Ask anything...")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Call FastAPI backend
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"query": prompt}
    )

    if response.status_code == 200:
        result = response.json()
        reply = result
    else:
        reply = "Error connecting to backend."

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)