from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    about = models.TextField()
    register_date = models.DateField(auto_now_add=True) #!ilk kayit edilme zamanini alir.
    last_update_date = models.DateTimeField(auto_now=True) #! her güncelleme zamanini alir.
    is_active = models.BooleanField(default=True)
    dogum_tarihi = models.DateField()
    


    def __str__(self):
        return f"ögrenci - {self.number} - {self.first_name}"


    class Meta:
        ordering = ["number"] #! istedigimiz verilere göre siralama yapmak icin class Meta kullaniliyor.
        verbose_name_plural = "Student_List"
