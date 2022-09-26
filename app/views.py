from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import Authfrom

class Auth(LoginView):
    template_name = "login.html"
    context = {
        "form": Authfrom
    }

def home(request):
    return render(request, "login.html", {"form": Authfrom})