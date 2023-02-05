from django.db import models
from django.conf import settings

class Teacher(models.Model):
    number = models.IntegerField(unique=True, null=False, default=None)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)