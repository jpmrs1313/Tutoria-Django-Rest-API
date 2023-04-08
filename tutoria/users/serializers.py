from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import serializers
from .models import CustomUser
import random


class CustomUserSerializer(serializers.ModelSerializer):
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = CustomUser
        fields = ["id", "email", "first_name", "last_name", "is_active"]

    def create(self, validated_data):
        password = CustomUser.objects.make_random_password()
        hashed_password = make_password(password)
        validated_data["password"] = hashed_password

        define_password_token = random.randint(1000000000, 9999999999)
        validated_data["define_password_token"] = define_password_token

        # Send the verification code to the user via email
        send_mail(
            "Your verification code",
            f"Your verification code is: {define_password_token}",
            "jpmrs1313@gmail.com",
            [validated_data["email"]],
            fail_silently=False,
        )

        return super(CustomUserSerializer, self).create(validated_data)
