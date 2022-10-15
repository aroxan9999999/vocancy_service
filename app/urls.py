from django.urls import path, include
from .views import __vocancy


urlpatterns = [
    path("", __vocancy),
]

