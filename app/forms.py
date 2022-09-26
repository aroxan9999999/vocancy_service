from django import forms
from django.contrib.auth.views import LoginView


class Authfrom(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=456)
