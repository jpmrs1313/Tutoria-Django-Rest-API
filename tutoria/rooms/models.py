from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=64, null=False)
    building = models.CharField(max_length=64, null=False)

    class Meta:
        unique_together = ["name", "building"]

    def __str__(self):
        return f"{self.name} - {self.building}"
