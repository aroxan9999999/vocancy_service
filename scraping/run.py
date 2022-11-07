import json
import os
import sys

from scraping.module.functions import get_url__KomBo
from scraping.module.functions import __

proj = os.path.dirname(os.path.abspath("manage.py"))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()
from app.models import *
from hh_ru import find_vocancy__hh
from work_ua import main_work


language = Language.objects.all()
__vocancy_dict__hh = {}
__vocancy_dict__wk = {}
for index in range(language.count()):
    _language = language[index].name
    for page in range(10):
        get_url__KomBo(find_vocancy__hh, "https://hh.ru", "/search/vacancy?text=", language=_language, x="&", page=page, index=index, __domen="https://hh.ru")
__result_hh = __(_return=True)


for index in range(language.count()):
    _language = language[index].name
    for page in range(10):
        get_url__KomBo(main_work, "https://www.work.ua/ru/", "jobs-", language=_language, x="/?", page=page, index=index+10, __domen='https://www.work.ua')
__result_wk = __(_return=True)

def get_vocancy() -> Vocancy:
    result = []
    for _i in [__result_hh, __result_wk]:
        if _i:
            result.extend(_i)

    for filter in result:
        if filter[2]:
            for _filter in filter[2]:
                    _language__name = filter[0]
                    print(_language__name)
                    language = Language.objects.get(name=_language__name)
                    city_name = _filter.get("city")
                    print(city_name)
                    if city_name:
                        try:
                            print(city_name)
                            city = City(name=city_name)
                            city.save()
                            city = City.objects.get(name=city_name)
                        except Exception:
                            city = City.objects.get(name=city_name)
                    else:
                        city = City.objects.get(name="неизвестный")
                    _filter["city"] = city
                    try:
                        v = Vocancy(**_filter, language=language)
                        v.save()
                    except Exception as exc:
                        continue




get_vocancy()



