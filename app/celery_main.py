import logging
from datetime import timedelta
from celery import Celery
from celery.signals import after_setup_logger
from app.settings import CELERY_BROKER_URL

celery_app = Celery("tasks", broker=CELERY_BROKER_URL, include=["app.tasks"])
logger = logging.getLogger(__name__)

celery_app.conf.update(
    timezone="UTC",
    enable_utc=True,
    worker_hijack_root_logger=False, # Переопределяем настройки логгирования
)


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler('logs.log')
    fh.setFormatter(formatter)
    logger.addHandler(fh)


celery_app.conf.beat_schedule = {
    "beat_buy_common_crypto": {
        "task": "buy_common_crypto",
        "schedule": timedelta(hours=2),
    },
    "beat_buy_pepe": {
        "task": "buy_pepe",
        "schedule": timedelta(hours=5),
    },
    "beat_healthcheck": {
        "task": "healthcheck",
        "schedule": timedelta(seconds=30),
    },
}