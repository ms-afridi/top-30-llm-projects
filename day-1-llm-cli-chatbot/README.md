# 🤖 Simple LLM Chatbot (CLI)

A beginner-friendly **Command Line Interface (CLI)** chatbot built using **Python** and the **LLaMA model** via the **Groq API**.

This project helps beginners understand the **core fundamentals of Large Language Models (LLMs)** by building a chatbot with **minimal code and no graphical UI**.

---

## 📌 Project Overview

The chatbot runs entirely in the terminal.  
Users can type questions or prompts, and the LLM responds in real time using an API-based model.

This project is ideal for:
- Beginners learning LLMs
- Students exploring AI projects
- Developers who want to understand LLM APIs without UI complexity

---

## ✨ Features

- ✅ CLI-based chatbot (no frontend required)
- ✅ Uses **LLaMA** model via **Groq API**
- ✅ Secure API key handling using `.env`
- ✅ Beginner-friendly and readable code
- ✅ Basic error handling included
- ✅ Chat history support for context-aware conversations

---

## 🛠 Tech Stack

- **Python 3.9+**
- **Groq API** (LLaMA model)
- **python-dotenv** (Environment variable management)

---

## 📂 Project Structure

```
day-1-llm-cli-chatbot/
│
├── app.py              # Main chatbot application
├── requirements.txt    # Python dependencies
├── .env               # API key (not tracked in git)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9 or higher installed
- A Groq API key ([Get one here](https://console.groq.com))

### Step 1: Clone the Repository

```bash
git clone https://github.com/ms-afridi/top-30-llm-projects.git
cd top-30-llm-projects/day-1-llm-cli-chatbot
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables

Create a `.env` file in the project directory:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

### Step 4: Run the Chatbot

```bash
python app.py
```

---

## 💬 Usage

Once you run the chatbot:

1. The terminal will display a welcome message
2. Type your question or prompt
3. Press **Enter** to get a response from the LLM
4. Type `exit`, `quit`, or `bye` to end the chat
5. The chatbot maintains conversation history for context-aware responses

### Example Interaction

```
🤖 LLM Chatbot Started! Type 'exit' to quit.

You: What is Python?
Bot: Python is a high-level, interpreted programming language known for its simplicity...

You: Give me an example
Bot: Here's a simple Python example...

You: exit
👋 Goodbye!
```

---

## ⚙️ Configuration

### Changing the Model

You can modify the model in `app.py`:

```python
model="llama-3.1-70b-versatile"  # Change to other Groq models
```

Available Groq models:
- `llama-3.1-70b-versatile`
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`
- `gemma-7b-it`

### Adjusting Response Parameters

Modify these settings in the API call:

```python
temperature=0.7,      # Creativity (0.0 - 1.0)
max_tokens=500,       # Response length
```

---

## 🔒 Security Best Practices

- ✅ Never commit your `.env` file to GitHub
- ✅ Add `.env` to `.gitignore`
- ✅ Use environment variables for all sensitive data
- ✅ Rotate your API keys regularly

---

## 🐛 Troubleshooting

### "GROQ_API_KEY not found" Error
- Ensure `.env` file exists in the same directory as `app.py`
- Check that the API key is correctly formatted in `.env`
- Verify no extra spaces around the `=` sign

### API Rate Limit Error
- Groq has rate limits on free tier
- Wait a few seconds between requests
- Consider upgrading your Groq plan

### Module Not Found Error
- Run `pip install -r requirements.txt`
- Ensure you're using Python 3.9+
- Consider using a virtual environment

---

## 📚 Learning Resources

- [Groq API Documentation](https://console.groq.com/docs)
- [LLaMA Model Information](https://ai.meta.com/llama/)
- [Python dotenv Guide](https://pypi.org/project/python-dotenv/)

---

## 🎯 Next Steps

After completing this project, you can:
1. Add conversation memory to a file
2. Implement different AI personalities
3. Create a web interface using Streamlit (see Day 2 project)
4. Add voice input/output capabilities
5. Integrate with other APIs

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**MS Afridi**
- GitHub: [@ms-afridi](https://github.com/ms-afridi)
- Repository: [Top 30 LLM Projects](https://github.com/ms-afridi/top-30-llm-projects)

---

## 🙏 Acknowledgments

- Built with [Groq API](https://groq.com/)
- Powered by Meta's LLaMA models
- Inspired by the growing AI/ML community

---

**⭐ If you found this helpful, please star the repository!**
