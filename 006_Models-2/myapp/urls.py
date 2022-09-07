from django.urls import path

from .views import myapp, welcome
# after '/mayapp/':
urlpatterns = [
    path('', myapp),
    path('welcome/', welcome),
]
