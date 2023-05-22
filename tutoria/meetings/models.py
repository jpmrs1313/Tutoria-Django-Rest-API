from django.db import models
from users.models import Teacher, Student
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Room(models.Model):
    name = models.CharField(max_length=64, null=False)
    building = models.CharField(max_length=64, null=False)

    class Meta:
        unique_together = ["name", "building"]

    def __str__(self):
        return f"{self.name} - {self.building}"


class RoomReservation(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="roomreservation"
    )
    begin = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.room} : From {self.begin} To {self.end}"


class Meeting(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="meetings"
    )

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="meetings"
    )

    reservation = models.OneToOneField(RoomReservation, on_delete=models.CASCADE)

    notifiedMeetingTomorrow = models.BooleanField(default=False)

    notifiedMeetingInHalfHour = models.BooleanField(default=False)

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
