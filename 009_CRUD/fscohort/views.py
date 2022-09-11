from django.shortcuts import (
    render, 
    redirect,
    get_object_or_404
)
from django.contrib import messages

from .models import Student
from .forms import StudentForm
def index(request):
    return render(request, "fscohort/index.html")

def student_list(request):
    students = Student.objects.all()
    context = {
        #! burada ki key olan yani sari renk olan students degisirse student_list.html icinde ki for ile üstünde gezdigimiz students'in isminin de degismesi gerekiyor.
        "students" : students
    }
    return render(request, "fscohort/student_list.html", context)

def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "student created succesfully!")
            return redirect("list")
    
    context ={
        "form" : form,
    }

    return render(request, "fscohort/student_add.html", context)
    #! Formu template gönderebilmek icin context yazdik.


def student_update(request, id):
    # student = Student.objects.get(id=id) #! .get sadece tek bir veri cekiyor.
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "student update succesfully!")
            return redirect("list")

    context = {
        "form" : form
    }

    return render(request, "fscohort/student_update.html", context)



def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list") #! islemden sonra bizi list sayfasina glndermesi icin wie navigate
    context = {
        "student" : student
    }
    return render(request, "fscohort/student_delete.html", context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {
        "student" : student
    } 

    return render(request, "fscohort/student_detail.html", context)