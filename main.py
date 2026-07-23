import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()                     # reads .env into environment variables

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#print(client.models.list())  # prints a list of available models

response = client.responses.create(
    model="gpt-4.1-mini", 
    input="Write a short poem about the beauty of nature.")

print(response.output_text)