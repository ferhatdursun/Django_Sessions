from django.shortcuts import render
from .models import Course
# Create your views here.

def index(request):
    return render(request, "courses/index.html")

def course(request):
    courses = Course.objects.all()
    context = {
        "courses" : courses
    }

    return render(request,"courses/course.html", context)
