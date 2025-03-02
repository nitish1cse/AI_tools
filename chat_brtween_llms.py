import os
from dotenv import load_dotenv
from openai import OpenAI, completions
import google.generativeai


load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


openai = OpenAI(api_key=OPEN_API_KEY)
google.generativeai.configure(api_key=GOOGLE_API_KEY)

gpt_model = "gpt-4o-mini"

gpt_system = "you are a chatbot who is rude and very argumentative; \
you disagree with anything the conversation and you challenge, in  a snarky way"

gemini_model = "gemini-1.5-flash"

gemini_system = "you are rude and very insulting chatbot. you try to agree with \
everything the other person says, or find a common ground. If the other person \
is argumentative, you try to calm them down and keep chatting "





def call_gpt():
    messages = [{"role":"system", "content": gpt_system}]
    for gpt, gemini in zip(gpt_message, gemini_message):
        messages.append({"role":"assistant", "content": gpt})
        messages.append({"role": "user", "content": gemini})

    completion = openai.chat.completions.create(model = gpt_model, messages=messages)
    return completion.choices[0].message.content




def call_gemini():
    messages_input = []
    for gpt, gemini in zip(gpt_message, gemini_message):
        messages_input.append({"role": "assistant", "parts": [{"text": gpt}]})
        messages_input.append({"role": "user", "parts": [{"text": gemini}]})

    messages_input.append({"role": "assistant", "parts": [{"text": gemini_message[-1]}]})

    gemini = google.generativeai.GenerativeModel(model_name=gemini_model, system_instruction=gemini_system)

    response = gemini.generate_content(messages_input)
    return response.text


gpt_message = ["Hi There"]
gemini_message = ["Hi"]

print(f"GPT: \n {gpt_message[0]}\n")
print(f"GPT: \n {gemini_message[0]}\n")

for i in  range(5):
    gpt_next = call_gpt()
    print(f"GPT: \n {gpt_next}\n")
    gpt_message.append(gpt_next)

    gemini_next = call_gemini()
    print(f"Gemini: \n {gemini_next}\n")
    gemini_message.append(gemini_next)









