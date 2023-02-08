from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from users.models import CustomUser


class Teacher(models.Model):
    number = models.IntegerField(unique=True, null=False, default=None)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_delete, sender=CustomUser)
def delete_user(sender, instance, **kwargs):
    user = Teacher.objects.get(user=instance)
    user.delete()
