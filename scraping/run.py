import json
import os
import sys

proj = os.path.dirname(os.path.abspath("manage.py"))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()
from app.models import *



def get_vocancy() -> Vocancy:
    with open("hh.json", "r", encoding="utf-8") as file:
        language: Language = Language.objects.get(name="python")
        city: City = City.objects.get(name="london")
        obj = json.load(file)
        for i in obj:
            try:
                v = Vocancy(**i, language=language, city=city)
                v.save()
            except Exception:
                continue
            print(v)

        


            #v = Vocancy(**vocancy, Language=language)
            #v.save()



get_vocancy()

