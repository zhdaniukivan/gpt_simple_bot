import os
import httpx
from openai import OpenAI


proxy = '138.201.202.99:8218'
login = 'mhrflgdk'
password = 'zassspnu'


proxy_options = {
    'proxy': {
        'http': f'http://{login}:{password}@{proxy}',
        'https': f'https://{login}:{password}@{proxy}',
        'no_proxy': 'localhost,127.0.0.1'
    },
}


OPENAI_API_KEY = os.getenv('MY_GPT_API_KEY')


client = OpenAI(
  organization='Personal',
  project=f'{OPENAI_API_KEY}',
)
