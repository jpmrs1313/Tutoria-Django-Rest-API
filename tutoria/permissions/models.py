from django.db import models
from django.contrib.contenttypes.models import ContentType
from enum import Enum


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
        return f"{self.content_type} - {self.operation}"
