import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutoria.settings")
app = Celery("django_celery")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "meeting_notifications": {
        "task": "meetings.tasks.meetingsNotifications",
        "schedule": timedelta(minutes=1),
    },
}
