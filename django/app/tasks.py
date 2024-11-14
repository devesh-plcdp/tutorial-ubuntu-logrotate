from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def log_message():
    logger.info("Hourly log message")
    print("Hourly log message")
