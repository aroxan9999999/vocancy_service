from django import forms
from django.contrib.auth.views import LoginView
from . models import City, Language



class Find_form(forms.Form):
    language_name = forms.ModelChoiceField(queryset=Language.objects.all(),
                                           widget=forms.Select(attrs={"class": "form-control"}),
                                           required=False,
                                           label="Специалность",
                                           to_field_name="slug")
    city_name = forms.ModelChoiceField(queryset=City.objects.all(),
                                       widget=forms.Select(attrs={"class": "form-control"}),
                                       required=False,
                                       label="Город",
                                       to_field_name="slug"
                                       )



