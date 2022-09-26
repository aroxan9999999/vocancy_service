from django.urls import path, include
from .views import Auth, home

urlpatterns = [
    path(" ", Auth.as_view()),
    path("home", home),
]