from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)
    define_password_token = models.CharField(max_length=10, blank=True)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    @property
    def random_password(self):
        return User.objects.make_random_password()

    def __str__(self):
        return self.email
