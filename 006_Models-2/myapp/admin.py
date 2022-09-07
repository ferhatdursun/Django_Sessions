from django.contrib import admin

# Show in admin:
from .models import Student
admin.site.register(Student)