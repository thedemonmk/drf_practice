from __future__ import absolute_import, unicode_literals
# from celery.decorators import task
from celery.utils.log import get_task_logger

from .email import send_review_email
from celery import shared_task

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_review_email_task(name, email, review):
    logger.info("Sent review email")
    return send_review_email(name, email, review)