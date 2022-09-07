from django.shortcuts import render
from django.http import HttpResponse


def home(request):  
    
    context = {
        'company': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "fscohort/home.html", context)


def index_view(request):
    context = {
        "age" :  32
    }
    return render(request, "fscohort/index.html", context)