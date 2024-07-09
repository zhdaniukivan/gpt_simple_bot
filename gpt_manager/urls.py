from django.urls import path
from .views import ChatAnswerView


urlpatterns = [
    path('chat/', ChatAnswerView.as_view(), name='chat_answer'),
]
