import os
import sys

from django.contrib.auth import get_user_model


proj = os.path.dirname(os.path.abspath("manage.py"))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


import django
django.setup()
from django.template import Context, Template
from app.models import Vocancy
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

def __send_email(to):
    sender = "aroxan.999@gmail.com"
    # your password = "your password"
    password = "rxfmntgwvyfwnmdx"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        with open("email_template.html") as file:
            template = file.read()
    except IOError:
        return "The template file doesn't found!"

    try:
        server.login(sender, password)
        msg = MIMEText(template, "html")
        msg["From"] = sender
        msg["To"] = to
        msg["Subject"] = "С Днем Рождения! Только сегодня скидка по промокоду до 90%!"
        server.sendmail(sender, to, msg.as_string())

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"



User = get_user_model()
qs = User.objects.filter(to_mail=True).values("email", "language", "city")
user_dict = {}
for i in qs:
    user_dict.setdefault((i["city"],i["language"]), [])
    user_dict[(i["city"], i["language"])].append(i["email"])

    if user_dict:
        params = {"city_id__in": [], "language_id__in": []}
        for pairs in user_dict.keys():
            print(pairs)
            params["city_id__in"].append(pairs[0])
            params["language_id__in"].append(pairs[1])
            print(params)
        qs = Vocancy.objects.filter(**params).values()
        vocancies = dict()
        for i in qs:
            vocancies.setdefault((i["city_id"], i["language_id"]), [])
            vocancies[(i["city_id"], i["language_id"])].append(i)
        for key, emails in user_dict.items():
            rows = vocancies.get(key, [])

        html = ""
        from django.template import Context, Template
        template = Template("email_template.html")
        context = Context({"text": rows})
        template.render(context)
        for email in emails:
            __send_email(email)
