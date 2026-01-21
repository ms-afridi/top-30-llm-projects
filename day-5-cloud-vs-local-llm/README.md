# ⚡ Cloud vs Local LLM Chatbot

A Streamlit-based chatbot application that allows you to compare and interact with both cloud-based LLMs (via Groq API) and local LLMs (via Ollama). Switch between cloud and local models seamlessly with separate conversation histories for each mode.

## Features

- 🌐 **Cloud Mode**: Use Groq's high-performance cloud API with GPT-OSS-120B model
- 🖥️ **Local Mode**: Run models locally using Ollama (completely offline)
- 💬 **Separate Memory**: Independent conversation histories for cloud and local modes
- ⏱️ **Response Time Tracking**: See how fast each model responds
- 🎨 **Clean UI**: Beautiful Streamlit interface with visual mode indicators

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed (for local mode)
- Groq API key (for cloud mode)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ms-afridi/top-30-llm-projects.git
   cd top-30-llm-projects/day-5-cloud-vs-local-llm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Ollama (for local mode)**
   - Install Ollama from [https://ollama.ai/](https://ollama.ai/)
   - Pull the models you want to use:
     ```bash
     ollama pull gemma3:1b
     ollama pull mistral
     ```

4. **Configure environment variables**
   - Create a `.env` file in the project root:
     ```bash
     touch .env
     ```
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - Get your free Groq API key from [https://console.groq.com/](https://console.groq.com/)

## Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Choose your mode**
   - Select **Cloud (Groq)** for fast cloud-based responses
   - Select **Local (Ollama)** for offline, privacy-focused inference

3. **Select local model** (when using Local mode)
   - Choose between `gemma3:1b` or `mistral`
   - Add more models by pulling them with Ollama

4. **Start chatting!**
   - Each mode maintains its own conversation history
   - Response times are displayed for performance comparison

## Project Structure

```
cloud-vs-local-llm/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## How It Works

### Cloud Mode (Groq)
- Uses Groq's API to access GPT-OSS-120B model
- Requires internet connection and API key
- Fast inference with cloud GPUs
- Suitable for high-performance needs

### Local Mode (Ollama)
- Runs models directly on your machine
- Works completely offline
- Privacy-focused (no data sent to cloud)
- Suitable for sensitive data or offline scenarios

## Configuration

### Adding More Local Models

To add more Ollama models:

1. Pull the model:
   ```bash
   ollama pull <model-name>
   ```

2. Add it to the sidebar selector in `app.py`:
   ```python
   local_model = st.sidebar.selectbox(
       "Choose Local Model",
       ["gemma3:1b", "mistral", "your-new-model"]
   )
   ```

### Changing Cloud Model

Modify the model parameter in the Groq API call:
```python
model="openai/gpt-oss-120b"  # Change to any Groq-supported model
```

## Troubleshooting

### "GROQ_API_KEY not found"
- Ensure `.env` file exists with your API key
- Check that `python-dotenv` is installed

### "Ollama returned no output"
- Verify Ollama is installed and running
- Check that the model is pulled: `ollama list`
- Try running manually: `ollama run gemma3:1b`

### Slow local responses
- Local performance depends on your hardware
- Try smaller models like `gemma3:1b` for faster responses
- Ensure no other heavy applications are running

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - Web framework
- [Groq](https://groq.com/) - Cloud LLM API
- [Ollama](https://ollama.ai/) - Local LLM runtime

## Contact

For questions or feedback, please open an issue on GitHub.

**Repository**: [https://github.com/ms-afridi/top-30-llm-projects](https://github.com/ms-afridi/top-30-llm-projects)

---

**Note**: This project is part of the "Top 30 LLM Projects" series - Day 5.
