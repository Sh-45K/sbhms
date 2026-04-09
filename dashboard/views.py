from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard_home(request):
    return render(request, 'dashboard_home.html')

@login_required
def dashoard_chatbot(request):
    return render(request, 'dashboard_chatbot.html')