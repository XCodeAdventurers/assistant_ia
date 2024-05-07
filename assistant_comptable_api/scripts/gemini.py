
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY="AIzaSyBm6qXO2Br_0wnqd_UVNsN7NrdhTVhsBz4"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def run():
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         print(m.name)
    response = model.generate_content("C'est quoi google ?", stream=False)
    print(response)
    