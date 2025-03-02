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


def message_gemini(prompt):
    gemini = google.generativeai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=system_message,
    )
    result = ""
    response = gemini.generate_content(prompt, stream=True)

    for chunk in response:
        text_chunk = chunk.text  # Extract text from the response
        if text_chunk:
            result += text_chunk
            yield result  # Stream the accumulated response


def stream_model(prompt, model):
    if model == "GPT":
        result = message_gpt(prompt)
    elif model == "GEMINI":
        result = message_gemini(prompt)
    else:
        raise ValueError("Unknown Model")
    for chunk in result:
        yield chunk




view = gr.Interface(fn=stream_model,
                    inputs = [gr.Textbox(label="your message"),
                    gr.Dropdown(["GPT", "GEMINI"], label = "select model")],
                    outputs= [gr.Markdown(label="Response")],
                    allow_flagging="never")
view.launch()



