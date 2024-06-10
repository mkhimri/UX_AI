
import openai
import os
import pkg_resources as pg
from pathlib import Path


os.environ["OPENAI_API_KEY"]="API-key"

openai.api_key=os.getenv("OPENAI_API_KEY")
path = pg.resource_filename(__name__, f'prompts/UX1.hbs')
response = openai.ChatCompletion.create(
          model="gpt-4",
          messages=[
            {"role": "user", "content": Path(path).read_text()}
        ],
          temperature=0,
        )

path2 = pg.resource_filename(__name__, f'results/output.txt')
with open(path2, 'w') as f:
    f.write(response.choices[0]["message"]["content"])
