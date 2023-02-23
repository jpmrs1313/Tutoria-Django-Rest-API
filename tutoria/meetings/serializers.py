from rest_framework import serializers
from .models import Meeting
from teachers.serializers import TeacherSerializer
from students.serializers import StudentSerializer


class MeetingSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    student = StudentSerializer()

    class Meta:
        model = Meeting
        fields = ["id", "teacher", "student", "datetime"]
