from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import Userloginform, Userregistrationform

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

def register_view(request):
    form = Userregistrationform(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password"])
        new_user.save()
        return render(request, "register_done.html", context={"new_user": new_user})
    return render(request, "register.html", context={"form": form})
