import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Page configuration
st.set_page_config(page_title="System Prompt Chatbot", page_icon="🧠")

st.title("🧠 System Prompt Chatbot")
st.caption("Control AI behavior using system prompts")

# Sidebar personality selector
personality = st.sidebar.selectbox(
    "Choose AI Personality",
    [
        "AI Teacher",
        "Python Tutor",
        "Interview Coach",
        "Motivational Coach"
    ]
)

# System prompts for different personalities
SYSTEM_PROMPTS = {
    "AI Teacher": "You are a helpful teacher. Explain concepts in very simple words with examples.",
    "Python Tutor": "You are a Python tutor. Explain Python concepts step by step with code examples.",
    "Interview Coach": "You are an interview coach. Ask questions and give feedback.",
    "Motivational Coach": "You are a motivational coach. Encourage the user and give positive advice."
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPTS[personality]}
    ]

# Update system prompt when personality changes
st.session_state.messages[0]["content"] = SYSTEM_PROMPTS[personality]

# Display chat history (excluding system message)
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.messages,
        temperature=0.7,
        max_tokens=300
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.markdown(reply)
