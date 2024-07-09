from django.http import JsonResponse
from django.views import View
from .services.openai_service import OpenAIService


class ChatAnswerView(View):
    def get(self, request, *args, **kwargs):
        openai_service = OpenAIService()
        model = "gpt-3.5-turbo"
        question_message = 'что делает git checkout'
        messages = [{"role": "user", "content": f'{question_message}, отвечай пожалуйста на русcком языке'}]
        response_content = openai_service.get_chat_answer(model, messages)
        return JsonResponse({"response": response_content}