from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()


    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    class Meta:
        ordering = ['number'] #! kücükten büyüge siralama. Büyükten kücüge siralama icin -number 
        verbose_name_plural = "Ögrenciler" #! bu kod ile class ismini degistirebiliriz.
    
    
