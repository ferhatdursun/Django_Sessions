from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home(request):
    return HttpResponse("Hello to WelcomePage.")
def myapp(request):
    return HttpResponse("Hello to MyAppPage.")
def welcome(request):
    return HttpResponse("Hello to MyAPP/WelcomePage.")
