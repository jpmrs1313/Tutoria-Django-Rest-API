from django.db import models
from teachers.models import Teacher
from django.conf import settings

class Student(models.Model):
    number = models.IntegerField(unique=True, null=False, default=None)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)