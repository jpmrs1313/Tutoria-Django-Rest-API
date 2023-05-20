from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group


class Operations(models.TextChoices):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"


class Policy(models.Model):
    ContentType = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="policies"
    )
    Operation = models.CharField(max_length=10, choices=Operations.choices)

    def __str__(self):
        return f"{self.ContentType} - {self.Operation}"


class RolePolicy(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    policy = models.ForeignKey(Policy, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.group} - {self.policy}"
