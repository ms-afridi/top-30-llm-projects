# 🤖 LLM Chatbot using Streamlit (GPT-OSS-120B)

A sleek, web-based AI chatbot built using **Streamlit** and powered by the **Groq API**. This project marks **Day 2** of a 30-day LLM project series, focusing on transitioning from a CLI-based tool to a professional web application.

---

## ✨ Features
* **ChatGPT-like UI:** Professional web interface using Streamlit's native chat components.
* **High-Speed Inference:** Powered by **GPT-OSS-120B** via the Groq LPU™ for near-instant response times.
* **Context Awareness:** Maintains chat history across the session using `st.session_state`.
* **Secure Config:** API key protection using `.env` integration.
* **Clean Code:** Modular and beginner-friendly Python implementation.

---

## 🛠 Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Inference Engine:** [Groq Cloud](https://groq.com/)
* **Model:** GPT-OSS-120B
* **Environment:** Python 3.9+ / python-dotenv

---

## 📂 Project Structure
```text
.
├── app.py              # Main Streamlit application
├── .env                # API Keys (Keep this private!)
├── .gitignore          # Environment & Cache exclusion
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
