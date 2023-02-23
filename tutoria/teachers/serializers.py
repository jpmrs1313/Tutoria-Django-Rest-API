from rest_framework import serializers
from .models import Teacher
from users.serializers import CustomUserSerializer
from django.db import transaction


class TeacherSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "number", "user"]

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        
        serializer = CustomUserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        validated_data['user'] = user

        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        
        serializer = CustomUserSerializer(instance.user, data=user_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().update(instance, validated_data)
