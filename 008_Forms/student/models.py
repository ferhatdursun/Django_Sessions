from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    #! buradaki cod dan dolayi media altinda profile_pics diye klasör olusturdu ve ekledigimiz resim otomatik olarak altina kayit edildi. 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
      