from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)