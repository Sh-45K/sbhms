from django.urls import path
from .views import dashboard_home, dashoard_chatbot

urlpatterns = [
    path('', dashboard_home),
    path('ai/', dashoard_chatbot)
]
