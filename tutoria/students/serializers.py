from rest_framework import serializers
from .models import Student
from users.models import CustomUser
from teachers.models import Teacher
from users.serializers import CustomUserSerializer
from teachers.serializers import TeacherSerializer

class StudentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Student
        fields = ["id", "number", "user", "teacher"]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        if user:
            student = Student.objects.create(user_id=user.id, **validated_data)
            return student
        return None