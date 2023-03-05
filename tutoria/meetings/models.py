from django.db import models
from teachers.models import Teacher
from students.models import Student
from roomsreservations.models import RoomReservation
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Meeting(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="meetings"
    )

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="meetings"
    )

    reservation = models.OneToOneField(RoomReservation, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} with {self.student} at {self.reservation}"

    def save(self, *args, **kwargs):
        if self.pk:  # if updating an existing instance
            old_student = self.student
            if self.student != old_student:
                self.teacher = self.student.teacher
        else:  # if creating a new instance
            self.teacher = self.student.teacher
        super().save(*args, **kwargs)


@receiver(post_delete, sender=Meeting)
def delete_user(sender, instance, **kwargs):
    instance.reservation.delete()
