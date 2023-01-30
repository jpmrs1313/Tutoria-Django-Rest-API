from rest_framework import serializers
from .models import Teacher
from students.models import Student

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'