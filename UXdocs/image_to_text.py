import openai 
import os
import base64
import requests
import pkg_resources as pg
from pathlib import Path

my_api_key = os.environ["OPENAI_API_KEY"]="API_KEY"
openai.api_key=os.getenv("OPENAI_API_KEY")

path_prompt = pg.resource_filename(__name__, f'prompts/UX2.hbs')

image_path = pg.resource_filename(__name__, f'images/profile_app.png')                       
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(image_path)
headers = {
"Content-Type": "application/json",
"Authorization": f"Bearer {my_api_key}"
}

payload = {
"model": "gpt-4-vision-preview",
"messages": [
                {
                "role": "user",
                "content": [
                {
                "type": "text",
                "text": Path(path_prompt).read_text()
                },
                {
                "type": "image_url",
                "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
                ]
                }
            ]
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
response.encoding='utf-8'
response=response.json()
print(response.get("choices"))

