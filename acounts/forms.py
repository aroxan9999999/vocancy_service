from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from .models import MyUser

class Userloginform(forms.Form):
    email = forms.CharField(max_length=50, widget=forms.EmailInput)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self, *args, **kwargs)
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            src = MyUser.objects.filter(email=email)
            if not src:
                raise forms.ValidationError("ползвателб не сушествует")
            if not  check_password(password, src[0].password):
                raise forms.ValidationError("пароль не верный")
            user = authenticate(email=email, password=password)
            if not user:
                forms.ValidationError("пользватель заблокирован")
        return super(Userloginform, self).clean(*args, **kwargs)