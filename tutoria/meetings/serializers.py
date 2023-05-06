from rest_framework import serializers
from .models import Meeting, RoomReservation, Room
from django.db import transaction
from django.utils import timezone


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "building"]


class RoomReservationSerializer(serializers.ModelSerializer):
    room = serializers.IntegerField(source="room_id")

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


class MeetingSerializer(serializers.ModelSerializer):
    student = serializers.IntegerField(source="student_id")
    reservation = RoomReservationSerializer()

    class Meta:
        model = Meeting
        fields = ["id", "teacher", "student", "reservation"]
        read_only_fields = ["teacher"]

    @transaction.atomic
    def create(self, validated_data):
        reservation_data = validated_data.pop("reservation")
        reservation_data["room"] = reservation_data["room_id"]

        serializer = RoomReservationSerializer(data=reservation_data)
        serializer.is_valid(raise_exception=True)

        reservation = serializer.save()

        validated_data["reservation"] = reservation

        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        reservation_data = validated_data.pop("reservation")
        reservation_data["room"] = reservation_data["room_id"]

        serializer = RoomReservationSerializer(
            instance.room, data=reservation_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().update(instance, validated_data)
