from django.db import models
from rooms.models import Room


class RoomReservation(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="roomreservation"
    )
    begin = models.DateTimeField()
    end = models.DateTimeField()
