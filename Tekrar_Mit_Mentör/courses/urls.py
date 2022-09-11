from django.urls import path
from .views import index,course

urlpatterns = [
    path("", index, name="home"),
    path("courses/", course, name="course"),
]
