from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_delete, sender=Admin)
def delete_user(sender, instance, **kwargs):
    instance.user.delete()
