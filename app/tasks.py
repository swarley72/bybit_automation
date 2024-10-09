from celery import shared_task
from app.constants import CurrencyEnum
from app.logger import logger
from app.bybit import buy_crypto

COMMON_CRYPTO = [CurrencyEnum.BTCUSDT, CurrencyEnum.ETHUSDT, CurrencyEnum.SOLUSDT, CurrencyEnum.TONUSDT]

@shared_task(name="buy_common_crypto")
def buy_common_crypto():
    for crypto in COMMON_CRYPTO:
        buy_crypto(currency=crypto, qty=1)
        logger(f"{crypto} order success")


@shared_task(name="buy_pepe")
def buy_pepe():
    buy_crypto(currency=CurrencyEnum.PEPEUSDT, qty=1)
    logger(f"{CurrencyEnum.PEPEUSDT} order success")


@shared_task(name="healthcheck")
def healthcheck():
    print("Healthy")
