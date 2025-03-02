import requests
from aiohttp import payload_type
from bs4 import BeautifulSoup

import ollama

OLLAMA_API = "http://localhost:11434/api/chat"
MODEL = "llama3.2"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

messages = [
    {"role": "user",
     "content": "Describe some of business application of Generative AI"}
]

class Website:
    def __init__(self, url):
        self.url = url
        web_response = requests.get(self.url, headers=headers)
        web_soup = BeautifulSoup(web_response.content, 'html.parser')
        self.title = web_soup.title.string if web_soup.title else "No title found"
        for irrelevant in web_soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = web_soup.body.get_text(separator="\n", strip=True)


system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

def user_prompt_for(website):
    user_prompt = f"your are looking for a website title {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt


def message_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

def summarise(url: str):
    website = Website(url)
    summary = ollama.chat(model=MODEL, messages=message_for(website))
    return summary.get("message").get('content')



"""
below code for directly using ollama API
payload  = {
    "model" : MODEL,
    "messages": messages,
    "stream": False
}

response = requests.post(OLLAMA_API,json=payload, headers=HEADERS)
print(response.json().get("message").get("content"))
response = ollama.chat(model=MODEL, messages=messages)
print(response.get("message").get('content'))

"""


print(summarise("https://setu.co/"))

