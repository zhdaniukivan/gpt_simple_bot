from typin import list, Dict, Any
from g4f.client import Client


class OpenAIService:
    def __inti__(self):
        self.client = Client()

    def get_chat_answer(self, model: str, messages: list[Dict[str, str]]) -> str:
        response = self.client.chat.completions.create(model=model, messages=messages)
        return response.choices[0].message.content
