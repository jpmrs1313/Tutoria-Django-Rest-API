from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
