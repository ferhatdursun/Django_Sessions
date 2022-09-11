from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now_add=False)
    update_date = models.DateTimeField(auto_now=True)
    course_pic = models.ImageField(upload_to="courses_pics/")

    def __str__(self):
        return self.name
    



