from django.shortcuts import render
from openai import OpenAI
import time

# client = OpenAI(
#     organization='',
#     project='',
# )


def time_check(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print("time fuc:", time.time() - start)
        return result
    return wrapper


simple_print()
