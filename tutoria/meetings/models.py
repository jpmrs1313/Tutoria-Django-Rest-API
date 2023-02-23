from django.db import models
from teachers.models import Teacher
from students.models import Student


class Meeting(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="meetings"
    )

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="meetings"
    )

    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.teacher} with {self.student} at {self.datetime}"
