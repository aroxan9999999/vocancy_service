from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from app.models import City, Language
from .models import MyUser

class Userloginform(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.EmailInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            src = MyUser.objects.filter(email=email)
            if not src:
                raise forms.ValidationError("Ползватель не сушествует")
            if not check_password(password, src[0].password):
                raise forms.ValidationError("пароль не верный")
            user = authenticate(email=email, password=password)
            if not user:
                forms.ValidationError("пользватель заблокирован")
        return super(Userloginform, self).clean(*args, **kwargs)

class Userregistrationform(forms.ModelForm):
    email = forms.CharField(max_length=50, widget=forms.EmailInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput, label="Password-rpeat")

    class Meta:
        model = MyUser
        fields = ("email",)

    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("пароли не совпадают")
        return data["password2"]


class Userupdateform(forms.Form):
    language = forms.ModelChoiceField(queryset=Language.objects.all(),
                                           required=True,
                                           label="Специальность",
                                           to_field_name="name")

    city = forms.ModelChoiceField(queryset=City.objects.all(),
                                       required=False,
                                       label="Город",
                                       to_field_name="name")

    to_mail = forms.BooleanField(required=False, widget=forms.CheckboxInput, label="получить расылку")

    class Meta:
        model = MyUser
        fields = ("city_name", "language_name", "to_mail")
