import os


CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://guest@localhost:5672")
BYBIT_API_KEY = os.getenv("BYBIT_API_KEY", "BYBIT_API_KEY")
BYBIT_SECRET_KEY = os.getenv("BYBIT_SECRET_KEY", "BYBIT_SECRET_KEY")
