import os
import requests
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI
from io import BytesIO
from PyPDF2 import PdfReader


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")


openai = OpenAI()

class Article:
    def __init__(self, url):
        self.url = url
        response  = requests.get(self.url)

        if response.status_code == 200:
            pdf_bytest = BytesIO(response.content)
            reader = PdfReader(pdf_bytest)

            text = ""
            for page in reader.pages:
                text += page.extract_text()

            self.text = text
            self.title = reader.metadata.get("/Title", "No title found")

        else:
            print(f"Failed to fetch PDF. Status code: {response.status_code}")
            self.text = "No text found"
            self.title = "No title found"



def craft_user_prompt(article):
    user_prompt = f"You are looking at a research article titled {article.title}\n Based on the body of the article, how are micro RNAs produced in the cell? State the function of the proteins \
    involved. The body of the article is as follows."
    user_prompt += article.text
    return user_prompt

# Step 2: Make the messages list
def craft_messages(article):
    system_prompt = "You are an assistant that analyses the contents of a research article and provide answers to the question asked by the user in 250 words or less. \
                Ignore text that doesn't belong to the article, like headers or navigation related text. Respond in markdown. Structure your text in the form of question/answer."
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": craft_user_prompt(article)}
    ]


def summarize(url):
    article = Article(url)
    response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = craft_messages(article)
    )
    return response.choices[0].message.content


summary = summarize("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7960g_7940g/sip/5_1/english/administration/guide/5_1/sipaxa51.pdf")
print(summary)


