from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    #! blank=True; kullanicinin zorunlu olarak doldurmasi gereken kisim. null=True; veri tabaninda bos birakilamaz kisim. Yani null=True degil ise blank=True olamaz.

    class Meta:
        ordering = ("-first_name",) #! Basinda - oldugunda siralamayi harf sirasina göre yukaridan asagiya dogru yapar.

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    