# gpt/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat'),
    path('test/', views.test_generate, name='test_generate'),
]