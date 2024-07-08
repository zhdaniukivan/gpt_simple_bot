import os

import openai
from openai import OpenAI
import time
import httpx as httpx
from dotenv import load_dotenv

load_dotenv()

proxies = {
    'http://': os.getenv('http_proxy'),
    'https://': os.getenv('https_proxy')
           }

http_client = httpx.Client(proxies=proxies)

client = OpenAI(
    api_key=os.getenv('MY_GPT_API_KEY'),
    http_client=http_client,
    )
# openai.api_key = os.getenv('MY_GPT_API_KEY')
# openai.http_client = http_client


def make_request_with_retry(max_retries=2, delay=3):
    for attempt in range(max_retries):
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                ]
            )
            return completion
        except Exception as e:
            print(f"We have a problems {e} on attempt {attempt}")
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                raise

try:
    result = make_request_with_retry()
    print(result.choices[0].message['content'])
except Exception as yy:
    print(yy)



    




# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts"
#                                       " with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )
# print(completion.choices[0].message)


def time_check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("time fuc:", time.time() - start)
        return result
    return wrapper


