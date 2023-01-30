from rest_framework import serializers
from .models import Student
from teachers.serializers import TeacherSerializer

class StudentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    class Meta:
        model = Student
        fields = ['id', 'user', 'teacher']