from pyexpat import model
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    about = models.TextField()
    register_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return f" öğrenci - {self.number} - {self.first_name}"
    

    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Student_List"
        
    def student_year_status(self):q
        "Returns the student's year status."
        import datetime
        if self.register_date < datetime.date(2019, 1, 1):
            return "Senior"
        elif self.register_date < datetime.date(2020, 1, 1):
            return "Junior"
        else:
            return "Freshman"
        
