from django.db import models
from rooms.models import Room


class RoomReservation(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="roomreservation"
    )
    begin = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.room} : From {self.begin} To {self.end}"