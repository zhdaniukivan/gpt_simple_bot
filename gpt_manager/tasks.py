from celery import Celery

app = Celery('gpt_simple_bot', broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y