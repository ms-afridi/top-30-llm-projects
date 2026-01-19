
# 🖥️ Local AI Chatbot with Ollama

A completely offline AI chatbot built with Streamlit and Ollama. This project runs 100% locally on your machine - no internet required after setup, ensuring complete privacy!

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Ollama](https://img.shields.io/badge/Ollama-Latest-green.svg)

## 🎯 What You'll Learn

- How to run AI models locally on your computer
- Building chat interfaces with Streamlit
- Working with Ollama for local LLM deployment
- Creating privacy-focused AI applications

## ✨ Features

- 🔒 **Complete Privacy** - All data stays on your machine
- 🚀 **No API Keys Needed** - No costs, no rate limits
- 💬 **Chat History** - Maintains conversation context
- 🎨 **Clean Interface** - Simple and user-friendly UI
- 🔄 **Multiple Models** - Switch between Llama3 and Mistral

## 📋 Prerequisites

Before starting, make sure you have:
- **Python 3.8 or higher** installed on your system
- At least **10GB free disk space** (for AI models)
- **Operating System**: Windows, macOS, or Linux

## 🚀 Installation Guide

Follow these steps carefully to set up the project on your local machine.

### Step 1: Install Ollama

Ollama allows you to run large language models locally. Choose your operating system:

#### **For Windows:**
1. Visit [https://ollama.com/download](https://ollama.com/download)
2. Click on "Download for Windows"
3. Run the downloaded `.exe` file
4. Follow the installation wizard
5. Ollama will start automatically after installation

#### **For macOS:**
1. Visit [https://ollama.com/download](https://ollama.com/download)
2. Click on "Download for Mac"
3. Open the downloaded `.dmg` file
4. Drag Ollama to your Applications folder
5. Open Ollama from Applications

#### **For Linux:**
Open your terminal and run:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Verify Installation:**
```bash
ollama --version
```
You should see the Ollama version number.

📚 **Learn more about Ollama:** [https://github.com/ollama/ollama](https://github.com/ollama/ollama)

### Step 2: Download AI Models

After installing Ollama, you need to download the AI models. Open your terminal/command prompt:

```bash
# Download Llama3 model (recommended - ~4.7GB)
ollama pull llama3

# Download Mistral model (optional - ~4.1GB)
ollama pull mistral
```

⏳ **Note:** Downloads may take 10-30 minutes depending on your internet speed.

**Verify Models:**
```bash
ollama list
```
You should see your downloaded models listed.

**Test a Model:**
```bash
ollama run llama3 "Hello! Tell me a joke."
```
If you get a response, everything is working perfectly! ✅

### Step 3: Clone This Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/ms-afridi/top-30-llm-projects.git
cd top-30-llm-projects/day-4-ollama-local-chatbot
```

**Don't have Git?** Download the ZIP file:
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file
4. Navigate to the `day-4-ollama-local-chatbot` folder

### Step 4: Set Up Python Environment (Recommended)

Creating a virtual environment keeps your project dependencies isolated.

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

You'll see `(venv)` in your terminal when activated.

### Step 5: Install Dependencies

With your virtual environment activated:

```bash
pip install -r requirements.txt
```

This will install Streamlit and any other required packages.

## 🎮 Running the Application

1. **Make sure Ollama is running** (it usually runs automatically in the background)

2. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Your browser will automatically open** at `http://localhost:8501`

4. **Select your model** from the sidebar (Llama3 or Mistral)

5. **Start chatting!** Type your message and press Enter

## 📸 Screenshots

When you run the app, you'll see:
- A sidebar to select your AI model
- A chat interface to type messages
- Real-time responses from your local AI

## 🎓 Understanding the Code

### `app.py` - Main Application
```python
# The app uses Streamlit for the UI
# subprocess to call Ollama
# session_state to maintain chat history
```

**Key Components:**
- **Model Selection**: Dropdown to choose between models
- **Chat Memory**: Stores conversation history
- **Ollama Integration**: Calls local AI models via subprocess

### `requirements.txt` - Dependencies
Contains all Python packages needed for the project.

### `.gitignore` - Git Configuration
Specifies files that Git should ignore (like virtual environments).

## 🔧 Troubleshooting

### Issue: "ollama: command not found"
**Solution:**
- Restart your terminal after installing Ollama
- On Windows, restart your computer
- Verify installation: `ollama --version`

### Issue: "Model not found"
**Solution:**
```bash
# List installed models
ollama list

# Install missing model
ollama pull llama3
```

### Issue: "Streamlit not found"
**Solution:**
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

### Issue: Slow Responses
**Solution:**
- First response is always slower (model loading)
- Close other heavy applications
- Ensure your computer meets minimum requirements

### Issue: App Won't Start
**Solution:**
```bash
# Check if Ollama is running
ollama list

# Try running Ollama directly
ollama run llama3 "test"

# Restart Streamlit
streamlit run app.py
```

## 🎯 Available Models

| Model | Size | Best For | Speed |
|-------|------|----------|-------|
| **Llama3** | ~4.7GB | General conversations, coding help | Medium |
| **Mistral** | ~4.1GB | Quick responses, simple tasks | Fast |

### Want to Try More Models?

Visit [Ollama Library](https://ollama.com/library) and install any model:
```bash
ollama pull codellama    # For coding tasks
ollama pull phi         # Lightweight model
ollama pull neural-chat # Conversational AI
```

Then update the model list in `app.py`:
```python
model = st.sidebar.selectbox(
    "Choose Local Model",
    ["llama3", "mistral", "codellama", "phi"]
)
```

## 📁 Project Structure

```
day-4-ollama-local-chatbot/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## 🎓 Learning Resources

- **Ollama Documentation**: [https://github.com/ollama/ollama](https://github.com/ollama/ollama)
- **Streamlit Docs**: [https://docs.streamlit.io](https://docs.streamlit.io)
- **Python subprocess**: [Python Docs](https://docs.python.org/3/library/subprocess.html)

## 💡 Next Steps & Ideas

After completing this project, try:
1. Add more models to the selection
2. Implement conversation export (save chats to file)
3. Add system prompts for different AI personalities
4. Create a clear chat history button
5. Add token/word counting
6. Implement streaming responses for real-time output

## 🤝 Contributing

Students and developers are welcome to contribute! You can:
- Report bugs or issues
- Suggest new features
- Improve documentation
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Ollama](https://ollama.com/) - Making local AI accessible
- [Streamlit](https://streamlit.io/) - Powerful web framework
- [Meta AI](https://ai.meta.com/) - Llama3 model
- [Mistral AI](https://mistral.ai/) - Mistral model

## 📞 Questions or Issues?

If you face any problems or have questions:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Review Ollama documentation

---

**Happy Learning! 🎉 Build your own AI applications with complete privacy!**

⭐ If you found this helpful, please star this repository!
