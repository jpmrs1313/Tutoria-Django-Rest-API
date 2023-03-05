from django.db import models
from teachers.models import Teacher
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Student(models.Model):
    number = models.IntegerField(unique=True, null=False, default=None)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return self.user.email


@receiver(post_delete, sender=Student)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()
