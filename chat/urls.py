# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.chat_list, name='chat_list'),
    path('<str:username>/', views.private_chat, name='private_chat'),  
]
