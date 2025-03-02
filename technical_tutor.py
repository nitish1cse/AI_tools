from dotenv import load_dotenv
import os
from openai import OpenAI
import ollama


MODEL_GPT = 'gpt-4o-mini'
MODEL_LLAMA = 'llama3.2'

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

openai = OpenAI()

system_prompt = "You are a helpful technical tutor who answers questions about python code, software engineering, data science and LLMs"
user_prompt = "Please give a detailed explanation to the following question: " + question


messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = openai.chat.completions.create(
    model=MODEL_GPT,
    messages=messages
)

print(f"GPT - Answer{response.choices[0].message.content}")

ollama_reply = ollama.chat(model=MODEL_LLAMA, messages=messages)

print(f'Ollama - Answer{ollama_reply["message"]["content"]}')




