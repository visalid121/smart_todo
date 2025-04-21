import os
import requests
from dotenv import load_dotenv

load_dotenv()

AIML_API_KEY = os.getenv("AIMLAPI_KEY")

def generate_suggestion(prompt: str):
    url = "https://api.aimlapi.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {AIML_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "deepseek-chat",  # Ensure this matches AIML’s current models
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that gives daily task suggestions."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print("AI API Error:", e)
        print("Response content:", getattr(response, "text", "No response"))
        return "Sorry, I couldn't generate a suggestion right now."
