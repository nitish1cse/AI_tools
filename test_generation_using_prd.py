import os

from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import json
from docx import Document

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"
# Initialize OpenAI client
openai = OpenAI(api_key=OPENAI_API_KEY)


# Define system message
system_message = (
    "You are a helpful assistant for testcases from given documents "
    "You read requirements , pre - requisite , user story  to generate testcase "
    "For example :requirements- login, pre - requisite - portal should be up , user story - user should able to login,  "
    "Generated test case example : 1. Verify User should be able to login with valid credentials"
                                   "2. Verify Login should fail when  user is not valid with proper error"
                                   "3. Login should fail if password is not is valid "
)

def read_docx(file_path):
    """Reads a .docx file and returns its content as a string."""
    doc = Document(file_path)
    context = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if text:  # Avoid empty lines
            context.append(text)

    return "\n".join(context)




# Define ticket price function for OpenAI API
doc_content = {
    "name": "read_docx",
    "description": "Extracts and returns the content of a .docx file as a structured text format.",
    "parameters": {
        "type": "object",
        "properties": {
            "content": {
                "type": "string",
                "description": "The extracted text content of the document, structured as a single string."
            }
        },
        "required": ["content"]
    },
}

# Define available tools
tools = [{"type": "function", "function": doc_content}]


def handle_tool_call(message):
    tool_call =  message.tool_calls[0]
    print(f"handle_tool_call:{tool_call}")
    content = read_docx("Deemed Debit in UPI Reserve.docx")
    response = {
        "role": "tool",
        "content": content,
        "tool_call_id": message.tool_calls[0].id
    }
    print(f"response:{response}")
    return response

def chat(message):
    messages = [{"role": "system", "content": system_message}]
    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    print(f"first response{response}")
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        print(f"tools_call if {message}")
        response = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
        print(f"if response{response}")
    yield response.choices[0].message.content


# Launch the Gradio interface

view = gr.Interface(fn=chat,
                    inputs = [gr.Textbox(label="your message")],
                    outputs= [gr.Markdown(label="Response")]).launch()