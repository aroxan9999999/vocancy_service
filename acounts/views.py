from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import Userloginform

def login_view(request):
    form = Userloginform(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect("home")
    return render( request, "login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")