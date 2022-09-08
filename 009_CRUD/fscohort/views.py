from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student


def index(request):
    return render(request, 'fscohort/index.html')


def student_list(request):
    students = Student.objects.all()
    print(students)
    context = {
        "students": students
    }
    return render(request, 'fscohort/student_list.html', context)


def student_add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'form': form,
    }

    return render(request, 'fscohort/student_add.html', context)
