from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db import models
from django import dispatch


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

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, "admin", "admin", password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)

    define_password_token = models.CharField(max_length=10, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    @property
    def random_password(self):
        return User.objects.make_random_password()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return self.is_staff


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Teacher(models.Model):
    number = models.IntegerField(unique=True, null=False, default=None)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Student(models.Model):
    number = models.IntegerField(unique=True, null=False, default=None)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="students"
    )


@dispatch.receiver(models.signals.post_delete, sender=Teacher)
@dispatch.receiver(models.signals.post_delete, sender=Admin)
@dispatch.receiver(models.signals.post_delete, sender=Student)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()
