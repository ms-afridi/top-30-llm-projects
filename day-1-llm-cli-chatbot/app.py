
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env file
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please set it in .env file")

# Initialize Groq client
client = Groq(api_key=api_key)

print("\n Simple LLM Chatbot")
print("Type 'exit' to quit\n")

# Start chat loop
while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit": 
        print("\nGoodbye 👋")
        break

    if not user_input:
        print(" Please type something.")
        continue

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=300
        )

        bot_reply = response.choices[0].message.content
        print("Bot:", bot_reply, "\n")

    except Exception as e:
        print(" Error:", e)
