# 🧠 System Prompt Chatbot

A Streamlit-based chatbot application that demonstrates how different system prompts can control AI behavior. Switch between multiple AI personalities to get specialized responses tailored to different use cases.

## Features

- **Multiple AI Personalities**: Choose from 4 different AI personas:
  - AI Teacher - Explains concepts in simple terms with examples
  - Python Tutor - Provides step-by-step Python programming guidance
  - Interview Coach - Conducts mock interviews and provides feedback
  - Motivational Coach - Offers encouragement and positive advice

- **Interactive Chat Interface**: Clean, user-friendly chat interface built with Streamlit
- **Persistent Chat History**: Maintains conversation context throughout the session
- **Easy Personality Switching**: Change AI behavior on-the-fly using the sidebar selector

## Prerequisites

- Python 3.8 or higher
- A Groq API key (get one from [Groq Console](https://console.groq.com))

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ms-afridi/top-30-llm-projects.git
cd top-30-llm-projects/day-3-system-prompt-chatbot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

Replace `your_groq_api_key_here` with your actual Groq API key.

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### How to Use

1. Select an AI personality from the sidebar dropdown
2. Type your message in the chat input at the bottom
3. Press Enter to send your message
4. The AI will respond according to the selected personality
5. Continue the conversation or switch personalities as needed

## Project Structure

```
system-prompt-chatbot/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not tracked in git)
├── .env.example          # Example environment file
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Configuration

### Adding New Personalities

To add custom AI personalities, modify the `SYSTEM_PROMPTS` dictionary in `app.py`:

```python
SYSTEM_PROMPTS = {
    "Your Personality Name": "Your system prompt instructions here.",
    # Add more personalities...
}
```

### Adjusting AI Parameters

Modify these parameters in the `client.chat.completions.create()` call:

- `temperature`: Controls randomness (0.0 = deterministic, 1.0 = creative)
- `max_tokens`: Maximum response length
- `model`: Change the Groq model being used

## API Information

This project uses the Groq API with the `openai/gpt-oss-120b` model. For more information about available models and features, visit the [Groq Documentation](https://console.groq.com/docs).

## Troubleshooting

**"GROQ_API_KEY not found" error**
- Ensure your `.env` file exists and contains a valid API key
- Check that the `.env` file is in the same directory as `app.py`

**Dependencies installation issues**
- Try upgrading pip: `pip install --upgrade pip`
- Use a virtual environment to avoid conflicts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/)
- Uses the `python-dotenv` library for environment management

## Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: Keep your API keys secure and never commit them to version control. Always use environment variables for sensitive information.
