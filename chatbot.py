import os
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr


load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
openai = OpenAI()

system_message = "you are a helpful prompt answer in one line"

def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    print(f"\nHistory is {history} \n")

    for user_message, assistant_message in history:
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": assistant_message})
    messages.append({"role": "user", "content": message})
    print(f"And Message is : {messages} \n")

    stream = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages,
        stream=True)

    results = ""
    for chunk in stream:
        results += chunk.choices[0].delta.content or ""
        yield results


gr.ChatInterface(fn=chat).launch()