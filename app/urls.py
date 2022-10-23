from django.urls import path, include
from .views import __vocancy, _listwiew

urlpatterns = [
    path("", __vocancy, name="home"),
    path("list", _listwiew, name="list"),
]

