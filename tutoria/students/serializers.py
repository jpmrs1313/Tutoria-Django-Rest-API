from rest_framework import serializers
from .models import Student
from users.serializers import CustomUserSerializer
from django.db import transaction


class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    teacher = serializers.IntegerField(source="teacher_id")

    class Meta:
        model = Student
        fields = ["id", "number", "user", "teacher"]

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")

        serializer = CustomUserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        validated_data["user"] = user

        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")

        serializer = CustomUserSerializer(instance.user, data=user_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().update(instance, validated_data)
