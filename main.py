import os
from dotenv import load_dotenv
import requests

load_dotenv() #to import env files

api_key = os.getenv("OPENAI_API_KEY")

uri = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content_Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "You are a movie review expert"},
        {"role": "user", "content" : "name one movie for software engineers apart from social network, just the name"}
    ],
}


response = requests.post(uri, headers=headers, json=payload)

print(response.json()["choices"][0]["message"]["content"])
#print(response.json())