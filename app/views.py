from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Vocancy
from .forms import Find_form


def __vocancy(request) -> Vocancy:
    find_form = Find_form()
    return render(request, template_name="home.html", context={"find_form": find_form})


def _listwiew(request):
    language = request.GET.get("language_name" or None)
    city = request.GET.get("city_name" or None)
    _fillter = {key: value for key, value in {"language__name": language, "city__name": city}.items() if value}
    vocancy_object = Vocancy.objects.filter(**_fillter)
    paginator = Paginator(vocancy_object, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = len(vocancy_object) // 10
    count +=1 if count %10 != 0 else 0
    navigator = {
        key: sorted(range(key + 5 if key >= 5 and key % 5 == 0 and key + 5 <= count and key > 1 else key -3
        if key not in range(count - 5, count + 1) and key not in range(0, 4) else key,
                          (key + 5 if key % 5 != 0 and key + 5 < count else key - 5
                          if key not in range(count - 5, count+1) else key + abs(key - count) + 1),
                          1 if key % 5 != 0 or key in range(count - 5, count+1) else -1))
        for key in range(1, count + 1)}

    return render(request, template_name="list.html", context={"vocancy": vocancy_object,
                                                           "navigator": navigator, "page_obj": page_obj,
                                                           "p": paginator, "language": language, "city": city})
