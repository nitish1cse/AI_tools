import os

from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import json
# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"
# Initialize OpenAI client
openai = OpenAI(api_key=OPENAI_API_KEY)

# Define system message
system_message = (
    "You are a helpful assistant for an airline called AIR INDIA. "
    "Give a short and courteous answer, no more than 1 sentence. "
    "Please be accurate. If you know the answer, say so."
)



# Dictionary with ticket prices
ticket_prices = {
    "ranchi": "Rs. 5000", "lucknow": "Rs. 4800", "delhi": "Rs. 3800",
    "patna": "Rs. 7500", "chennai": "Rs. 2400", "goa": "Rs. 1900"
}

def get_ticket_price(destination_city):
    print(f"Tool get_ticket_price called for {destination_city}")
    city = destination_city.lower()
    return ticket_prices.get(city, "Unknown")


# Define ticket price function for OpenAI API
price_function = {
    "name": "get_ticket_prices",
    "description": "Retrieves the ticket price for a given destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The name of the destination city for which the ticket price is requested."
            }
        },
        "required": ["destination_city"]
    }
}

# Define available tools
tools = [{"type": "function", "function": price_function}]


def handle_tool_call(message):
    tool_call =  message.tool_calls[0]
    print(f"handle_tool_call:{tool_call}")
    argument = json.loads(tool_call.function.arguments)
    print(f"argument:{argument}")

    city = argument.get('destination_city')
    price = get_ticket_price(city)
    response = {
        "role": "tool",
        "content": json.dumps({"destination_city": city,"price": price}),
        "tool_call_id": message.tool_calls[0].id
    }
    print(f"response:{response}")
    return response, city

def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    print(f"History is {history}\n\n")

    for human, assistant in history:
        messages.append({"role":"user","content": human})
        messages.append({"role":"assistant","content": assistant})
    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    print(f"first response{response}")
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        print(f"tools_call if {message}")
        response, city = handle_tool_call(message)
        print(f"response if {response}... {city}")
        messages.append(message)
        messages.append(response)
        response = openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
        print(f"if response{response}")
    return response.choices[0].message.content


# Launch the Gradio interface
gr.ChatInterface(
    fn=chat,
    title="Air India Customer Support",
    description="Ask questions about flights and tickets"
).launch()
