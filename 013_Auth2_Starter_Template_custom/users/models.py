from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    portfolio = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    username = models.EmailField('Email Address', unique=True)
    REQUIRED_FIELDS = []
