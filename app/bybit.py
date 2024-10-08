from pybit.unified_trading import HTTP
from app.constants import CurrencyEnum, OrderTypeEnum
from app.settings import BYBIT_API_KEY, BYBIT_SECRET_KEY

session = HTTP(
    testnet=False,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_SECRET_KEY,
)


def buy_crypto(*, currency: CurrencyEnum,
               order_type: OrderTypeEnum = OrderTypeEnum.MARKET,
               qty: int = 1):
    session.place_order(
        category="spot",
        symbol=currency.value,
        side="Buy",
        orderType=order_type.value,
        qty=qty
    )
