from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.mail import send_mail
from rest_framework import serializers
import random
from .models import CustomUser, Admin, Teacher, Student


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


class PasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(required=True)

    class Meta:
        fields = ["email", "password", "token"]

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        token = validated_data["token"]

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist as error:
            raise serializers.ValidationError(error)

        if user.is_active:
            raise serializers.ValidationError(
                f"User {user.email} already defined the password"
            )

        if token != user.define_password_token:
            raise serializers.ValidationError(f"The token is incorrect")

        try:
            validate_password(password=password)
        except Exception as error:
            raise serializers.ValidationError(error)

        user.set_password(password)
        user.is_active = True
        user.save()

        return validated_data


class UserSerializerMixin:
    def create(self, validated_data):
        user_data = validated_data.pop("user")

        serializer = CustomUserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        validated_data["user"] = user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")

        serializer = CustomUserSerializer(instance.user, data=user_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().update(instance, validated_data)


class AdminSerializer(UserSerializerMixin, serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Admin
        fields = ["user"]


class TeacherSerializer(UserSerializerMixin, serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "number", "user"]


class StudentSerializer(UserSerializerMixin, serializers.ModelSerializer):
    user = CustomUserSerializer()
    teacher = serializers.IntegerField(source="teacher_id")

    class Meta:
        model = Student
        fields = ["id", "number", "user", "teacher"]
