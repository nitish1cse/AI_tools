import os

from click import launch
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai
import anthropic
import gradio as gr

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

openai = OpenAI(api_key=OPEN_API_KEY)
claude = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
google.generativeai.configure(api_key=GOOGLE_API_KEY)

system_message = "you are an helpful assistant who responds in mark down"


def message_gpt(prompt):
    prompts = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    stream = openai.chat.completions.create(
        model='gpt-4o-mini',
        messages=prompts,
        stream=True)

    results = ""
    for chunk in stream:
        results += chunk.choices[0].delta.content or ""
        yield results





"""
default gradio launch
view = gr.Interface(fn=shout, inputs="textbox", outputs="textbox", allow_flagging='never').launch(share=True) 
"""

"""

below code for label text filed and lines
view = gr.Interface(fn=message_gpt,
                    inputs=[gr.Textbox(label="Your Message", lines=6)],
                    outputs=[gr.Textbox(label="Response", lines=6)],
                    allow_flagging='never').launch(share=True)
                    
"""

view = gr.Interface(fn=message_gpt,
                    inputs = [gr.Textbox(label="your message")],
                    outputs= [gr.Markdown(label="Response")],
                    allow_flagging="never")
view.launch()



