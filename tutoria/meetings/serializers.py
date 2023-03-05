from rest_framework import serializers
from .models import Meeting
from roomsreservations.serializers import RoomReservationSerializer
from django.db import transaction


class MeetingSerializer(serializers.ModelSerializer):
    student = serializers.IntegerField(source="student_id")
    # reservation = serializers.IntegerField(source="reservation_id")
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
