import streamlit as st
import subprocess

st.set_page_config(page_title="Local AI Chatbot", page_icon="🖥️")

st.title("🖥️ Local AI Chatbot (Ollama)")
st.caption("Runs completely offline using Ollama")

# Sidebar model selector
model = st.sidebar.selectbox(
    "Choose Local Model",
    ["gemma3:1b", "mistral"]
)

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Ollama locally
    result = subprocess.run(
        ["ollama", "run", model, user_input],
        capture_output=True,
        text=True
    )

    reply = result.stdout.strip()

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)
