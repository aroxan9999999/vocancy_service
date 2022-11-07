import os
import sys
from django.contrib.auth import get_user_model
from scraping.module.functions import html_send_file

proj = os.path.dirname(os.path.abspath("manage.py"))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django
django.setup()
from app.models import Vocancy
import smtplib
from email.mime.text import MIMEText
from django.db.models import Q
from dotenv import load_dotenv
load_dotenv()


def __send_email(to):
    print(to)
    sender = "aroxan.999@gmail.com"
    # your password = "your password"
    password = "rxfmntgwvyfwnmdx"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        with open("email_template.html", "r", encoding='utf-8') as file:
            template = file.read()
    except Exception:
        return "The template file doesn't found!"

    try:
        server.login(sender, password)
        msg = MIMEText(template, "html")
        msg["From"] = sender
        msg["To"] = to
        msg["Subject"] = "Расылка Вокансии"
        server.sendmail(sender, to, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        print(to, "ok")
        return f"{_ex}\nCheck your login or password please!"


User = get_user_model()
qs = User.objects.filter(to_mail=True).values("city__name", "language__name", "email")
if qs:
    filter_city_language = {"city__name__in": [i.get("city__name") for i in qs], "language__name__in": [i.get("language__name")
                                                                                            for i in qs]}
    filter_city = {"city__name__in": [i.get("city__name") for i in qs if None in i.values() and i["city__name"]]}
    filter_language = {"language__name__in": [i.get("language__name") for i in qs]}

    vaues_list_city = filter_city_language.get("city__name__in")
    vocancy_list_language = filter_city_language.get("language__name__in")
    for i in qs:
        email = i["email"]
        if None not in i.values():
            vocancy = Vocancy.objects.filter(**filter_city_language).order_by('-timer')[:10]
            if not vocancy:
                vocancy = Vocancy.objects.filter(Q(language__name__icontains__in=vaues_list_city) |
                                                 Q(city__name__icontains__in=vaues_list_city)).order_by('-timer')[:10]
                if not vocancy:
                    vocancy = Vocancy.objects.all().order_by('-timer')[:10]
            html_send_file(vocancy)
            __send_email(email)
        elif None in i.values() and i["city__name"]:
            vocancy = Vocancy.objects.filter(**filter_city)
            if not vocancy:
                vocancy = Vocancy.objects.filter(city__name__icontains__in=vaues_list_city).order_by('-timer')[:10]
                if not vocancy:
                    vocancy = Vocancy.objects.all().order_by('-timer')[:10]
            html_send_file(vocancy)
            __send_email(email)
        elif None in i.values() and i["language__name"]:
            vocancy = Vocancy.objects.filter(**filter_language).order_by('-timer')[:10]
            if not vocancy:
                vocancy = Vocancy.objects.filter(language__name__icontains__in=vocancy_list_language).order_by('-timer')[:10]
                if not vocancy:
                    vocancy = Vocancy.objects.all().order_by('-timer')[:10]
            html_send_file(vocancy)
            __send_email(email)
        else:
            vocancy = Vocancy.objects.all().order_by('-timer')[:10]
            html_send_file(vocancy)
            __send_email(email)










