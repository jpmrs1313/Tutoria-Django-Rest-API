from celery import shared_task
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .models import Meeting
from users.models import Teacher, Student
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def meetingsNotifications():
    tomorrow = datetime.now().date() + timedelta(days=1)

    meetings_for_tomorrow = Meeting.objects.filter(
        reservation__begin__date=tomorrow, notifiedMeetingTomorrow=False
    )

    half_an_hour_later = datetime.now() + timedelta(minutes=30)

    meetings_for_halfHour = Meeting.objects.filter(
        reservation__begin__date=half_an_hour_later, notifiedMeetingInHalfHour=False
    )

    for meeting in meetings_for_tomorrow | meetings_for_halfHour:
        teacher = Teacher.objects.get(id=meeting.teacher.id)
        student = Student.objects.get(id=meeting.student.id)

        send_notifications(
            f"You have a meeting in at {meeting.reservation.room,} at {meeting.reservation.begin}",
            [teacher.user.email, student.user.email],
        )

        meeting.notifiedMeetingTomorrow = True
        meeting.save(update_fields=["notifiedMeetingTomorrow"])

    for meeting in meetings_for_halfHour:
        teacher = Teacher.objects.get(id=meeting.teacher.id)
        student = Student.objects.get(id=meeting.student.id)

        send_notifications(
            f"You have a meeting in at {meeting.reservation.room,} at half an hour",
            [teacher.user.email, student.user.email],
        )

        meeting.notifiedMeetingInHalfHour = True
        meeting.save(update_fields=["notifiedMeetingInHalfHour"])


def send_notifications(text: str, emailsList: list[str]):
    send_mail(
        "Meeting Remember",
        text,
        "jpmrs1313@gmail.com",
        emailsList,
        fail_silently=False,
    )
