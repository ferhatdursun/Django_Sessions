from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # print("request.meta : ", request.META)
    # print("request.user : ", request.path)
    # print("request.user : ", request.method)
    # print("request.user : ", request.user)
    # print("request.COOKIES : ", request.COOKIES) #! csrftoken; django kendini korumak icin kullaniyor ama bi arastir.
    # print("request.GET : ", request.GET)
    # html = request.GET.get("name")
    # return HttpResponse(html)
    
    return render(request, "fscohort/home.html", context)


def home(request):
    context = {
           
        'company': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "fscohort/home.html", context)

def index_view(request):
    context = {
        "age" : 30
    }
    return render(request, "fscohort/index.html", context)

