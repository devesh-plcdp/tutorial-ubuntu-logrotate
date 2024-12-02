from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def log_message():
    logger.info("Minutely log message")
    print("Minutely log message")
