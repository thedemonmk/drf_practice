from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_practice.settings')

app = Celery('drf_practice')

# app.conf.enable_utc = False
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()