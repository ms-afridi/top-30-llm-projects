import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found. Please set it in .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Page config
st.set_page_config(page_title="LLM Chatbot", page_icon="🤖")

st.title("🤖 LLM Chatbot")
st.caption("Powered by OpenAI GPT-OSS-120B via Groq")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=300
        )

        bot_reply = response.choices[0].message.content

        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

        with st.chat_message("assistant"):
            st.markdown(bot_reply)

    except Exception as e:
        st.error(f"Error: {e}")
