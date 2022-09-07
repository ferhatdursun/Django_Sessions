from django.urls import path
from .views import home, index_view

urlpatterns = [
    path("", home, name="home"),
    path("index/", index_view, name="index"),
]
