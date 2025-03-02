import os
from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
from sympy import content

load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
openai = OpenAI()

system_message = ("Your a a helpful assistant in a cloth store, you should try to gently encourage"
                  "the customer to try items that are on sale. Hats are 60 % off and most other items are 50 % off."
                  "For Example, if customer ask 'I am looking for a hat',"
                  "You could reply something like 'wonderful- we have lots of hats - including several"
                  "that are part of sales event"
                  "encourage customer to buy hats if they are unsure to what to get ")

def chat(message, history):
    messages = [{"role": "system", "content": system_message}]
    print(f"\nHistory is {history} \n")

    for user_message, assistant_message in history:
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": assistant_message})
    if "belt" in message:
        messages.append({"role": "system", "content": "For added context, the store does not sell belts,"
                                                      "but be sure to point out other item on sale"})
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

system_message += ("\n if the customer ask for shoes , you should respond that shoes are not for sale today"
                   "but remind the customer to look for hats")
gr.ChatInterface(fn=chat).launch()