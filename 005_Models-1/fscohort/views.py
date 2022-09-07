from django.shortcuts import render
from django.http import HttpResponse


def homeview(request):
    # database den veriyi burda çekiyoruz
    return HttpResponse("Welcome Backend")