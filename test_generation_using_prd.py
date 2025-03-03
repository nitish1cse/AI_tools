import os

from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import json
from docx import Document

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"
openai = OpenAI(api_key=OPENAI_API_KEY)


system_message = (
    "You are a QA expert who generates comprehensive test cases from requirements documents."
    "You read requirements , pre - requisite , user story  to generate testcase "
    "For example :requirements- login, pre - requisite - portal should be up , user story - user should able to login,  "
    "Generated test case example : 1. Verify User should be able to login with valid credentials"
                                   "2. Verify Login should fail when  user is not valid with proper error"
                                   "3. Login should fail if password is not is valid "
    "Write separate testcases for error codes specified in the document "
    "Follow below guideline"
    """1. Analyze the requirements carefully
   Analyze pre requisite carefully
   Analyze Error codes and write seperate code
   Read the link attached and analyse associated content from requirement 
2. Generate test cases in these categories:
   - Positive scenarios
   - Negative scenarios
   - Edge cases
   - Error conditions
3. Each test case should include:
   - Test ID
   - Description
   - Prerequisites
   - Test steps
   - Expected results
   - Priority (High/Medium/Low)"""

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

def generate_tests(file_path):
    """Generate test cases from uploaded file"""
    try:
        content = read_docx(file_path)
        if content.startswith("Error"):
            return content

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Generate test cases for these requirements:\n\n{content}"}
        ]

        response = openai.chat.completions.create(
            model=MODEL, 
            messages=messages, 
            tools=tools
        )

        if response.choices[0].message.tool_calls:
            message = response.choices[0].message
            tool_response = handle_tool_call(message)
            messages.append(message)
            messages.append(tool_response)
            
            final_response = openai.chat.completions.create(
                model=MODEL,
                messages=messages
            )
            return final_response.choices[0].message.content
        
        return response.choices[0].message.content

    except Exception as e:
        return f"Error generating test cases: {str(e)}"

iface = gr.Interface(
    fn=generate_tests,
    inputs=[
        gr.File(
            label="Upload Requirements Document (.docx)",
            file_types=[".docx"],
            type="filepath"
        )
    ],
    outputs=gr.Markdown(label="Generated Test Cases"),
    title="Test Case Generator",
    description="Upload a requirements document to generate comprehensive test cases.",
    article="""
    ### Instructions
    1. Upload a .docx file containing your requirements
    2. Wait for the test cases to be generated
    3. Test cases will include:
       - Test ID and Category
       - Description and Priority
       - Prerequisites
       - Test Steps
       - Expected Results
       - Error Codes (where applicable)
    """)
if __name__ == "__main__":
    iface.launch()
