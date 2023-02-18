from rest_framework import serializers
from .models import Student
from rest_framework import serializers
from .models import Student
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from django.db import transaction


class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = ["id", "number", "user", "teacher"]

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = CustomUser.objects.create(**user_data)
        if user:
            student = Student.objects.create(user_id=user.id, **validated_data)
            return student
        else:
            raise Exception("Failed to create user")

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.user

        user.first_name = user_data.get("first_name", user.first_name)
        user.last_name = user_data.get("last_name", user.last_name)
        user.email = user_data.get("email", user.email)
        user.save()

        instance.number = validated_data.get("number", instance.number)
        instance.teacher = validated_data.get("teacher", instance.teacher)
        instance.save()

        return instance
