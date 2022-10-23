from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Vocancy
from .forms import Find_form


def __vocancy(request) -> Vocancy:
    find_form = Find_form()
    return render(request, template_name="home.html", context={"find_form": find_form})




def _listwiew(request):
    language = request.GET.get("language_name")
    city = request.GET.get("city_name")
    _fillter = {key: value for key, value in {"language__name": language, "city__name": city}.items() if value}
    print(_fillter)
    vocancy_object = Vocancy.objects.filter(**_fillter)
    paginator = Paginator(vocancy_object, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = len(vocancy_object) // 10
    navigator = {
        key: sorted(range(key + 5 if key >= 5 and key % 5 == 0 and key + 5 < count and key > 1 else key
        if key not in range(count - 5, count) else key - 3,
                          (key + 5 if key % 5 != 0 and key + 5 < count else key - 5
                          if key not in range(count - 5, count) else key + abs(key - count) + 1),
                          1 if key % 5 != 0 or key in range(count - 5, count) and key > 0 and key != count else -1))
        for key in range(1, count + 1)}

    return render(request, template_name="list.html", context={"vocancy": vocancy_object,
                                                           "navigator": navigator, "page_obj": page_obj,
                                                           "p": paginator, "language": language, "city": city})
