import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai
import anthropic


load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

openai = OpenAI(api_key=OPEN_API_KEY)
claude = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
google.generativeai.configure(api_key=GOOGLE_API_KEY)


system_message = "you are an assistant who is great in telling jokes"
user_prompt = "Tell a very funny joke for a audience of QA engineer"

prompts = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_prompt}
    ]

completion = openai.chat.completions.create(model='gpt-4o' , messages=prompts, temperature=1)
print(f"GPTRespone {completion.choices[0].message.content}")


# """
# Claude API
# """
#
# message  = claude.messages.create(
#     model="claude-3-5-sonnet-20240620",
#     max_tokens=200,
#     temperature=0.7,
#     system=system_message,
#     messages=[{"role":"user", "content": user_prompt}]
# )
#
# print(message.content[0].text)


gemini = google.generativeai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_message,

)

response = gemini.generate_content(user_prompt)
print(response.text)



