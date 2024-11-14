from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'log_every_hour': {
        'task': 'app.tasks.log_message',
        'schedule': crontab(minute=10, hour='*'),
    },
}

app.conf.timezone = settings.TIME_ZONE
app.conf.enable_utc = True
app.autodiscover_tasks()
