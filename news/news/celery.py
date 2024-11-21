from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news.settings")

app = Celery(
    'news',
)
app.conf.enable_utc = False

app.conf.update(timezone= 'Asia/Kolkata')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'scrape data again every 15 min' : {
        'task': 'api.tasks.test_func',
        'schedule': crontab(hour= 20, minute=19),
        # 'args' : ()

    }
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')