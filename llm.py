#Ollama
import requests
from config import MODEL_NAME
def ask_ollama(prompt):
    print("🤖 AI思考中...")
    url = "http://localhost:11434/api/generate"
    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    result = response.json()["response"]
    print(f"🤖 AI: {result}")
    return result