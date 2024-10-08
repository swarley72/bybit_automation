from enum import Enum


class CurrencyEnum(Enum):
    BTCUSDT = "BTCUSDT"
    ETHUSDT = "ETHUSDT"
    SOLUSDT = "SOLUSDT"
    PEPEUSDT = "PEPEUSDT"
    TONUSDT = "TONUSDT"


class OrderTypeEnum(Enum):
    MARKET = "Market"
    LIMIT = "Limit"
