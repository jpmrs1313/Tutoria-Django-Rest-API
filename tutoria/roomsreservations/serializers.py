from .models import RoomReservation
from rest_framework import serializers
from django.utils import timezone


class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = ["id", "room", "begin", "end"]

    def validate_begin(self, value):
        if value.time() < timezone.datetime.strptime("08:00", "%H:%M").time():
            raise serializers.ValidationError("Meeting cannot start before 08:00 AM.")
        elif value.time() > timezone.datetime.strptime("19:30", "%H:%M").time():
            raise serializers.ValidationError("Meeting cannot start after 19:30 PM.")
        return value

    def validate_end(self, value):
        if value.time() > timezone.datetime.strptime("20:00", "%H:%M").time():
            raise serializers.ValidationError("Meeting cannot end after 20:00 PM.")
        return value

    def validate(self, data):
        begin = data.get("begin")
        end = data.get("end")
        room = data.get("room")

        # Check if the end time is before the begin time
        if begin >= end:
            raise serializers.ValidationError(
                "The start time must be before the end time."
            )

        # Check if there is a meeting in the room in the begin/end period
        existing_reservations = RoomReservation.objects.filter(
            room=room, end__gt=begin, begin__lt=end
        )

        if existing_reservations.exists():
            message = (
                "There is already a reservation for this room during this time period"
            )
            for existing_reservation in existing_reservations:
                message = f"{message}: from {existing_reservation.begin} - {existing_reservation.end}"

            raise serializers.ValidationError(message)

        # Check if the meeting starts and ends on same day
        if begin.date() != end.date():
            raise serializers.ValidationError(
                "The reservation must be for the same day."
            )

        return data
