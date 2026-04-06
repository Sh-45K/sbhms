from django.urls import path
from .views import home, contact
# Create your views here.

urlpatterns = [
    path('', home),
    path('contact/', contact)
]