from celery import shared_task
from app.constants import CurrencyEnum
from app.logger import logger

COMMON_CRYPTO = [CurrencyEnum.BTCUSDT, CurrencyEnum.ETHUSDT, CurrencyEnum.SOLUSDT, CurrencyEnum.TONUSDT]

@shared_task(name="buy_common_crypto")
def buy_common_crypto():
    logger("CRYPTO TASK SUCCESS")
    # for crypto in COMMON_CRYPTO:
    #     buy_crypto(currency=crypto, qty=1)
    return "BUY CRYPTO RETURNED"


@shared_task(name="buy_pepe")
def buy_pepe():
    logger("PEPE TASK SUCCESS")
    # buy_crypto(currency=CurrencyEnum.PEPEUSDT, qty=1)
    return "BUY PEPE RETURNED"


@shared_task(name="test")
def test():
    logger("TEST TASK SUCCESS")
    # logger.info("It is working!")
    return True