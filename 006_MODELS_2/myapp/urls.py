from django.urls import path
from .views import myapp, welcome
urlpatterns = [
    path("", myapp),
    path("welcome/", welcome),
]