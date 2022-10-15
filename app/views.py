from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import Vocancy
from .forms import Find_form


def __vocancy(request) -> Vocancy:
    find_form = Find_form()
    if request.method == "GET":
        vocancy_object = Vocancy.objects.all()
        return render(request, template_name="home.html", context={"vocancy": vocancy_object, "find_form": find_form})



