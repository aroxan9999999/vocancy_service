from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from .forms import Userloginform, Userregistrationform, Userupdateform
from django.contrib import messages

User = get_user_model()

def login_view(request):
    form = Userloginform(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect("home")
    return render(request, "login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")

def register_view(request):
    form = Userregistrationform(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password"])
        new_user.save()
        messages.success(request, 'Account created successfully.')
        return render(request, "register_done.html", context={"new_user": new_user})
    return render(request, "register.html", context={"form": form})

def update_view(request):
    if request.user.is_authenticated:
        user = request.user
        form = Userupdateform(initial={"city": user.city,
                                        "language": user.language, "to_mail": user.to_mail})
        if request.method == "POST":
            form = Userupdateform(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.city = data["city"]
                user.language = data["language"]
                user.to_mail = data["to_mail"]
                user.save()
                messages.success(request, 'данные успешно обнавлены')
                return redirect("home")
        return render(request, "update.html", context={"form": form})

def delete_view(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == "POST":
            _us = User.objects.get(pk=user.pk)
            _us.delete()
            messages.error(request, 'Акаунт удален.')
    return redirect("home")
