from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv() #to impor env files

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)