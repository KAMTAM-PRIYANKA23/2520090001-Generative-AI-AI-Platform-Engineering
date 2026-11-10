import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables from .env
load_dotenv()

# Step 2: Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Check your .env file."
    )

# Step 3: Initialize Gemini client
client = genai.Client(api_key=api_key)

# Step 4: Send prompt to Gemini model
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Differentiate Artificial Intelligence, Machine Learning, and Deep Learning."
)

# Step 5: Display generated response
print("\nLLM Response:")
print(response.text)