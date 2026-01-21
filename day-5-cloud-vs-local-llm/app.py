import os
import streamlit as st
import subprocess
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    groq_client = Groq(api_key=api_key)
else:
    groq_client = None

st.set_page_config(page_title="Cloud vs Local LLM", page_icon="⚡")
st.title("⚡ Cloud vs Local LLM Chatbot")
st.caption("Compare Groq (Cloud) vs Ollama (Local)")

# Sidebar
mode = st.sidebar.selectbox(
    "Choose LLM Mode",
    ["Cloud (Groq)", "Local (Ollama)"]
)

local_model = st.sidebar.selectbox(
    "Choose Local Model",
    ["gemma3:1b", "mistral"]
)

# Visual indicator
if mode == "Cloud (Groq)":
    st.success("☁️ Using Cloud LLM (Groq API)")
    st.info("Model: GPT-OSS-120B (Cloud GPU)")
else:
    st.warning("🖥️ Using Local LLM (Ollama - Offline)")
    st.info(f"Model: {local_model} (Running locally)")

# -------------------------------
# SEPARATE MEMORY PER MODE
# -------------------------------
memory_key = "messages_cloud" if mode == "Cloud (Groq)" else "messages_local"

if memory_key not in st.session_state:
    st.session_state[memory_key] = []

messages = st.session_state[memory_key]

# Display chat
for msg in messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something...")

if user_input:
    messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    start_time = time.time()

    # -------- CLOUD --------
    if mode == "Cloud (Groq)":
        if not groq_client:
            reply = "GROQ_API_KEY not found."
        else:
            response = groq_client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.7,
                max_tokens=300
            )
            reply = response.choices[0].message.content

    # -------- LOCAL --------
    else:
        try:
            result = subprocess.run(
                ["ollama", "run", local_model, user_input],
                capture_output=True,
                text=True
            )
            reply = result.stdout.strip()

            if not reply:
                reply = "Ollama returned no output. Is the model running?"

        except Exception as e:
            reply = f"Ollama error: {e}"

    end_time = time.time()
    response_time = round(end_time - start_time, 2)

    messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
        st.caption(f"⏱ Response time: {response_time} seconds")
